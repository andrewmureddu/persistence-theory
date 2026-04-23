from __future__ import annotations

from dataclasses import dataclass

from .models import ACPState, BreathPhase, Mode, PlanStep, Task
from .policy import normalized_entropy


@dataclass
class RouteStat:
    route: str
    attempts: float = 0.0
    approvals: float = 0.0

    @property
    def quality(self) -> float:
        return (self.approvals + 1.0) / (self.attempts + 2.0)


class RouteRegistry:
    def __init__(self) -> None:
        self.routes = {
            "synthesis": RouteStat("synthesis"),
            "research": RouteStat("research"),
            "what_if": RouteStat("what_if"),
            "ponder": RouteStat("ponder"),
            "precision": RouteStat("precision"),
            "counterfactual": RouteStat("counterfactual"),
            "challenge": RouteStat("challenge"),
            "consolidate": RouteStat("consolidate"),
            "human_review": RouteStat("human_review"),
        }
        self.history: list[str] = []

    def decay(self, factor: float) -> None:
        for stat in self.routes.values():
            stat.attempts *= factor
            stat.approvals *= factor

    def record(self, route: str, approved: bool) -> None:
        stat = self.routes[route]
        stat.attempts += 1.0
        if approved:
            stat.approvals += 1.0
        self.history.append(route)

    def snapshot_stats(self) -> list[RouteStat]:
        return [
            RouteStat(route=stat.route, attempts=stat.attempts, approvals=stat.approvals)
            for stat in self.routes.values()
        ]

    def load_snapshot(
        self,
        stats: list[RouteStat],
        *,
        history: list[str] | None = None,
    ) -> None:
        for stat in stats:
            target = self.routes.setdefault(stat.route, RouteStat(stat.route))
            target.attempts = stat.attempts
            target.approvals = stat.approvals
        self.history = list(history or [])

    def route_entropy(self) -> float:
        return normalized_entropy([stat.attempts for stat in self.routes.values()])

    def route_dominance(self) -> float:
        weights = [stat.attempts for stat in self.routes.values() if stat.attempts > 0]
        if not weights or sum(weights) < 2.0:
            return 0.0
        total = sum(weights)
        return max(weights) / total

    def same_route_streak(self) -> int:
        if not self.history:
            return 0
        streak = 1
        latest = self.history[-1]
        for route in reversed(self.history[:-1]):
            if route != latest:
                break
            streak += 1
        return streak

    def choose_route(
        self,
        task: Task,
        mode: Mode,
        state: ACPState,
        phase: BreathPhase,
    ) -> str:
        if mode is Mode.ESCALATE:
            return "human_review"
        if phase is BreathPhase.INHALE:
            if task.novelty >= 0.75:
                candidates = ["what_if", "research", "synthesis"]
            elif task.risk >= 0.50:
                candidates = ["research", "synthesis", "what_if"]
            else:
                candidates = ["synthesis", "research", "what_if"]
            for route in candidates:
                if route != state.last_route:
                    return route
            return candidates[0]
        if phase is BreathPhase.HOLD_IN:
            return "ponder"
        if phase is BreathPhase.RELEASE:
            candidates = ["counterfactual", "challenge", "precision"]
            if mode is not Mode.DIVERSIFY:
                candidates = ["precision", "challenge", "counterfactual"]
            ranked = sorted(
                candidates,
                key=lambda route: (self.routes[route].attempts, self.routes[route].quality),
            )
            for route in ranked:
                if route != state.last_route:
                    return route
            return ranked[0]
        return "consolidate"


class Router:
    def __init__(self, registry: RouteRegistry | None = None) -> None:
        self.registry = registry or RouteRegistry()

    def next_step(
        self,
        task: Task,
        state: ACPState,
        mode: Mode,
        phase: BreathPhase,
    ) -> PlanStep:
        route = self.registry.choose_route(task, mode, state, phase)
        objective_by_phase = {
            BreathPhase.INHALE: "breathe in through synthesis, research, and what-if generation",
            BreathPhase.HOLD_IN: "hold and ponder the emerging hypotheses",
            BreathPhase.RELEASE: "release and let competing predictions contend",
            BreathPhase.HOLD_OUT: "hold after release and consolidate the provisional winner",
        }
        return PlanStep(
            mode=mode,
            breath_phase=phase,
            route=route,
            objective=objective_by_phase[phase],
            attempt=state.retry_depth + 1,
        )
