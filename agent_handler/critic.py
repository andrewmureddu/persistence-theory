from __future__ import annotations

from .models import ACPState, ActionResult, BreathPhase, ReviewResult, Task
from .policy import clamp


class Critic:
    def review(self, task: Task, result: ActionResult, state: ACPState) -> ReviewResult:
        issues: list[str] = []
        missing_fields = sorted(set(task.expected_fields) - set(result.provided_fields))
        if result.completed and not result.schema_valid:
            issues.append("schema invalid")
        if result.completed and missing_fields:
            issues.append(f"missing fields: {', '.join(missing_fields)}")

        support_score = self._support_score(task, result)
        min_evidence = 0.50 + (0.30 * task.risk)
        contradiction = result.annotations.get("contradiction", 0.0) >= 0.5
        disagreement = clamp(abs(result.confidence - support_score))
        requires_release = task.novelty >= 0.45 or task.risk >= 0.50

        if support_score < min_evidence and result.completed:
            issues.append("insufficient grounding for task risk")
        if task.novelty >= 0.60 and result.novelty_coverage < 0.50 and result.completed:
            issues.append("novel task handled without enough exploratory coverage")
        if (
            result.completed
            and requires_release
            and result.step.breath_phase is not BreathPhase.RELEASE
        ):
            issues.append("defer finalization until release phase")
        if result.completed and disagreement > 0.28:
            issues.append("executor confidence outpaced critic support")
        if result.completed and contradiction:
            issues.append("contradictory evidence detected")

        requires_human = (
            task.risk >= 0.88
            and result.completed
            and (support_score < 0.82 or disagreement > 0.20)
        )
        if result.requested_human:
            requires_human = True
        if requires_human:
            issues.append("human review required")

        blocking = bool(issues)
        approved = result.completed and not blocking
        return ReviewResult(
            approved=approved,
            blocking=blocking,
            requires_human=requires_human,
            issues=issues,
            disagreement=disagreement,
            contradiction=contradiction,
            support_score=support_score,
        )

    @staticmethod
    def _support_score(task: Task, result: ActionResult) -> float:
        novelty_weight = 0.40 if task.novelty >= 0.60 else 0.20
        evidence_weight = 1.0 - novelty_weight
        return clamp(
            (evidence_weight * result.evidence_ratio)
            + (novelty_weight * result.novelty_coverage)
        )
