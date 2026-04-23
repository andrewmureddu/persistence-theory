from __future__ import annotations

import math
from dataclasses import dataclass

from .models import ActionResult, ACPState, Mode, ReviewResult


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def normalized_entropy(weights: list[float]) -> float:
    active = [weight for weight in weights if weight > 0]
    if len(active) <= 1:
        return 0.0 if active else 1.0
    total = sum(active)
    entropy = 0.0
    for weight in active:
        probability = weight / total
        entropy -= probability * math.log(probability)
    return entropy / math.log(len(active))


@dataclass(frozen=True)
class PolicyConfig:
    dissolution_threshold: float = 0.58
    crystallization_threshold: float = 0.62
    escalation_threshold: float = 0.88
    max_cycles: int = 6
    route_decay: float = 0.85
    memory_decay: float = 0.87
    memory_ttl_ticks: int = 4
    same_route_streak_limit: int = 3


class ACPPolicy:
    def __init__(self, config: PolicyConfig | None = None) -> None:
        self.config = config or PolicyConfig()

    def choose_mode(self, state: ACPState) -> Mode:
        if state.risk >= self.config.escalation_threshold and state.retry_depth >= 2:
            return Mode.ESCALATE
        if state.dissolution_score >= self.config.dissolution_threshold:
            return Mode.GROUND
        if state.crystallization_score >= self.config.crystallization_threshold:
            return Mode.DIVERSIFY
        return Mode.EXPLOIT

    def min_evidence(self, risk: float) -> float:
        return clamp(0.50 + (0.30 * risk))

    def compute_dissolution_score(
        self,
        result: ActionResult,
        review: ReviewResult,
        retry_depth: int,
    ) -> float:
        schema_pressure = 0.0 if result.schema_valid else 1.0
        evidence_gap = 1.0 - review.support_score
        retry_pressure = clamp(retry_depth / 3.0)
        contradiction = 1.0 if review.contradiction else 0.0
        blocking_pressure = 1.0 if review.blocking else 0.0
        score = (
            0.35 * blocking_pressure
            + 0.25 * contradiction
            + 0.20 * schema_pressure
            + 0.10 * retry_pressure
            + 0.10 * evidence_gap
        )
        return clamp(score)

    def compute_crystallization_score(
        self,
        state: ACPState,
        result: ActionResult,
    ) -> float:
        dominance_pressure = state.route_dominance
        memory_pressure = state.memory_concentration
        disagreement_collapse = 1.0 - state.critic_disagreement
        streak_pressure = clamp(
            state.same_route_streak / float(self.config.same_route_streak_limit)
        )
        novelty_gap = 1.0 - result.novelty_coverage
        score = (
            0.30 * dominance_pressure
            + 0.25 * memory_pressure
            + 0.20 * disagreement_collapse
            + 0.15 * streak_pressure
            + 0.10 * novelty_gap
        )
        return clamp(score)
