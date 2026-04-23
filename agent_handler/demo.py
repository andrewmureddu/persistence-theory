from __future__ import annotations

from .models import Task
from .runtime import AgentHandler


def build_demo_tasks() -> list[Task]:
    return [
        Task(
            task_id="routine-1",
            description="Summarize a familiar internal SOP and return key actions.",
            novelty=0.15,
            risk=0.20,
            tags=("ops", "summary", "sop"),
            expected_fields=("summary", "actions", "owner"),
        ),
        Task(
            task_id="routine-2",
            description="Draft a routine rollout checklist from the same playbook family.",
            novelty=0.20,
            risk=0.30,
            tags=("ops", "checklist", "rollout"),
            expected_fields=("checklist", "owner", "rollback"),
        ),
        Task(
            task_id="breath-1",
            description="Explore a moderately novel internal workflow and compare candidate approaches before deciding.",
            novelty=0.55,
            risk=0.45,
            tags=("design", "workflow", "comparison"),
            expected_fields=("options", "tradeoffs", "recommendation"),
        ),
        Task(
            task_id="novel-1",
            description="Design a new cross-functional agent workflow for a task family the handler has not seen.",
            novelty=0.85,
            risk=0.55,
            tags=("design", "agent", "workflow", "novel"),
            expected_fields=("architecture", "risks", "controls", "metrics"),
        ),
        Task(
            task_id="high-risk-1",
            description="Propose a high-risk policy change that affects approvals and production actions.",
            novelty=0.65,
            risk=0.94,
            tags=("policy", "approvals", "production"),
            expected_fields=("proposal", "controls", "rollback", "approvals"),
        ),
    ]


def main() -> None:
    handler = AgentHandler()
    for task in build_demo_tasks():
        outcome = handler.handle(task)
        print(f"\nTask {task.task_id}: {outcome.status}")
        print(f"  Final summary: {outcome.final_summary}")
        for index, episode in enumerate(outcome.episodes, start=1):
            state = episode.state_after
            print(
                "  "
                f"{index}. {episode.step.mode.value}/{episode.step.breath_phase.value}/{episode.step.route} "
                f"support={episode.review.support_score:.2f} "
                f"conf={episode.result.confidence:.2f} "
                f"diss={state.dissolution_score:.2f} "
                f"cryst={state.crystallization_score:.2f}"
            )
            if episode.review.issues:
                print(f"     issues: {', '.join(episode.review.issues)}")


if __name__ == "__main__":
    main()
