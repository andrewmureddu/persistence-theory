from __future__ import annotations

from .critic import Critic
from .executor import DemoExecutionAdapter, ExecutionAdapter
from .memory import MemoryGovernor
from .models import ACPState, BreathPhase, Episode, RunOutcome, Task
from .operator import BreathingOperator
from .policy import ACPPolicy
from .router import Router


class AgentHandler:
    def __init__(
        self,
        policy: ACPPolicy | None = None,
        router: Router | None = None,
        critic: Critic | None = None,
        executor: ExecutionAdapter | None = None,
        memory: MemoryGovernor | None = None,
        breathing_operator: BreathingOperator | None = None,
    ) -> None:
        self.policy = policy or ACPPolicy()
        self.router = router or Router()
        self.critic = critic or Critic()
        self.executor = executor or DemoExecutionAdapter()
        self.breathing_operator = breathing_operator or BreathingOperator()
        self.memory = memory or MemoryGovernor(
            ttl_ticks=self.policy.config.memory_ttl_ticks,
            decay=self.policy.config.memory_decay,
        )

    def handle(self, task: Task) -> RunOutcome:
        episodes: list[Episode] = []
        state = self._bootstrap_state(task)

        for _ in range(self.policy.config.max_cycles):
            mode = self.policy.choose_mode(state)
            phase = self.breathing_operator.choose_phase(state, mode)
            memories = self.memory.retrieve(task, mode)
            step = self.router.next_step(task, state, mode, phase)
            result = self.executor.execute(task, step, episodes, memories)
            review = self.critic.review(task, result, state)

            self.router.registry.decay(self.policy.config.route_decay)
            self.router.registry.record(step.route, review.approved)

            episode = Episode(step=step, result=result, review=review)
            self.memory.remember(task, episode)
            self.memory.advance_tick()

            state = self._update_state(task, state, episode, len(episodes))
            episode.state_after = state
            episodes.append(episode)

            if review.approved:
                return RunOutcome(
                    task=task,
                    status="completed",
                    episodes=episodes,
                    final_state=state,
                    final_summary=result.summary,
                )

            if review.requires_human or mode.value == "escalate":
                return RunOutcome(
                    task=task,
                    status="escalated",
                    episodes=episodes,
                    final_state=state,
                    final_summary=result.summary,
                )

        return RunOutcome(
            task=task,
            status="incomplete",
            episodes=episodes,
            final_state=state,
            final_summary="Max cycles reached without approval.",
        )

    def _bootstrap_state(self, task: Task) -> ACPState:
        return ACPState(
            task_id=task.task_id,
            novelty=task.novelty,
            risk=task.risk,
            route_entropy=self.router.registry.route_entropy(),
            route_dominance=self.router.registry.route_dominance(),
            memory_concentration=self.memory.dominant_share(),
            same_route_streak=self.router.registry.same_route_streak(),
            breath_phase=None,
        )

    def _update_state(
        self,
        task: Task,
        previous: ACPState,
        episode: Episode,
        completed_cycles: int,
    ) -> ACPState:
        updated = ACPState(
            task_id=task.task_id,
            novelty=task.novelty,
            risk=task.risk,
            confidence=episode.result.confidence,
            route_entropy=self.router.registry.route_entropy(),
            route_dominance=self.router.registry.route_dominance(),
            memory_concentration=self.memory.dominant_share(),
            critic_disagreement=episode.review.disagreement,
            retry_depth=completed_cycles + 1,
            same_route_streak=self.router.registry.same_route_streak(),
            last_mode=episode.step.mode,
            last_route=episode.step.route,
            breath_phase=episode.step.breath_phase,
            breath_cycle=previous.breath_cycle
            + (
                1
                if episode.step.breath_phase is BreathPhase.INHALE
                and previous.breath_phase is BreathPhase.HOLD_OUT
                else 0
            ),
        )
        updated.dissolution_score = self.policy.compute_dissolution_score(
            episode.result,
            episode.review,
            retry_depth=updated.retry_depth,
        )
        updated.crystallization_score = self.policy.compute_crystallization_score(
            updated,
            episode.result,
        )
        return updated
