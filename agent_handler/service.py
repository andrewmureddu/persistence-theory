from __future__ import annotations

import os
import sqlite3
from pathlib import Path
from uuid import uuid4

from .executor import build_execution_adapter
from .memory import MemoryGovernor
from .models import RunOutcome, Task
from .policy import ACPPolicy
from .runtime import AgentHandler
from .router import Router
from .storage import DEFAULT_DB_PATH, SQLiteStore


class AgentService:
    def __init__(
        self,
        db_path: str | Path | None = None,
        *,
        backend: str | None = None,
    ) -> None:
        self.store = SQLiteStore(db_path or DEFAULT_DB_PATH)
        self.store.initialize()
        self.backend = backend or os.getenv("AGENT_HANDLER_BACKEND", "demo")

    def submit_task(
        self,
        *,
        description: str,
        novelty: float,
        risk: float,
        tags: list[str] | tuple[str, ...],
        expected_fields: list[str] | tuple[str, ...],
        task_id: str | None = None,
        run_now: bool = False,
    ) -> dict:
        task = Task(
            task_id=task_id or self._generate_task_id(),
            description=description,
            novelty=novelty,
            risk=risk,
            tags=tuple(tags),
            expected_fields=tuple(expected_fields),
        )
        try:
            self.store.create_task(task)
        except sqlite3.IntegrityError as exc:
            raise ValueError(f"Task {task.task_id} already exists.") from exc
        if run_now:
            return self.run_task(task.task_id)
        return self.get_task(task.task_id)

    def run_task(self, task_id: str) -> dict:
        task = self.store.get_task_model(task_id)
        if task is None:
            raise KeyError(task_id)

        handler = self._build_handler()
        outcome = handler.handle(task)
        self.store.replace_task_run(
            outcome,
            handler.router.registry.snapshot_stats(),
            handler.memory.snapshot_records(),
            memory_tick=handler.memory.tick,
        )
        return self.get_task(task_id)

    def get_task(self, task_id: str) -> dict:
        task = self.store.get_task(task_id)
        if task is None:
            raise KeyError(task_id)
        return task

    def list_tasks(self, limit: int = 50) -> list[dict]:
        return self.store.list_tasks(limit=limit)

    def approve_task(
        self,
        task_id: str,
        *,
        approver: str,
        notes: str = "",
        decision: str = "approve",
    ) -> dict:
        if decision not in {"approve", "reject"}:
            raise ValueError("decision must be 'approve' or 'reject'")
        if self.store.get_task(task_id) is None:
            raise KeyError(task_id)
        self.store.record_approval(
            task_id,
            approver=approver,
            decision=decision,
            notes=notes,
        )
        return self.get_task(task_id)

    def runtime_state(self) -> dict:
        snapshot = self.store.get_runtime_snapshot()
        snapshot["backend"] = self.backend
        return snapshot

    def _build_handler(self) -> AgentHandler:
        policy = ACPPolicy()
        router = Router()
        router.registry.load_snapshot(
            self.store.get_route_stats(),
            history=self.store.get_recent_route_history(),
        )
        memory = MemoryGovernor(
            ttl_ticks=policy.config.memory_ttl_ticks,
            decay=policy.config.memory_decay,
        )
        memory.load_snapshot(
            self.store.get_memories(),
            tick=self.store.get_memory_tick(),
        )
        executor = build_execution_adapter(self.backend)
        return AgentHandler(
            policy=policy,
            router=router,
            memory=memory,
            executor=executor,
        )

    @staticmethod
    def _generate_task_id() -> str:
        return f"task-{uuid4().hex[:10]}"


def _service_demo() -> None:
    service = AgentService()
    created = service.submit_task(
        description="Explore a new internal synthesis workflow.",
        novelty=0.7,
        risk=0.4,
        tags=["design", "workflow"],
        expected_fields=["options", "tradeoffs", "recommendation"],
        run_now=True,
    )
    print(created["task_id"], created["status"])


if __name__ == "__main__":
    _service_demo()
