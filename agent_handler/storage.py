from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .models import ACPState, Episode, MemoryRecord, RunOutcome, Task
from .router import RouteStat

DEFAULT_DB_PATH = Path(__file__).resolve().with_name("agent_handler.db")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class SQLiteStore:
    def __init__(self, db_path: str | Path | None = None) -> None:
        self.db_path = Path(db_path or DEFAULT_DB_PATH)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def initialize(self) -> None:
        with self._connect() as connection:
            connection.executescript(
                """
                PRAGMA journal_mode=WAL;

                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    description TEXT NOT NULL,
                    novelty REAL NOT NULL,
                    risk REAL NOT NULL,
                    tags_json TEXT NOT NULL,
                    expected_fields_json TEXT NOT NULL,
                    status TEXT NOT NULL,
                    final_summary TEXT,
                    requires_human INTEGER NOT NULL DEFAULT 0,
                    approved INTEGER NOT NULL DEFAULT 0,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS episodes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id TEXT NOT NULL,
                    step_no INTEGER NOT NULL,
                    mode TEXT NOT NULL,
                    breath_phase TEXT NOT NULL,
                    route TEXT NOT NULL,
                    objective TEXT NOT NULL,
                    attempt INTEGER NOT NULL,
                    summary TEXT NOT NULL,
                    provided_fields_json TEXT NOT NULL,
                    schema_valid INTEGER NOT NULL,
                    evidence_ratio REAL NOT NULL,
                    novelty_coverage REAL NOT NULL,
                    confidence REAL NOT NULL,
                    completed INTEGER NOT NULL,
                    requested_human INTEGER NOT NULL,
                    approved INTEGER NOT NULL,
                    blocking INTEGER NOT NULL,
                    requires_human INTEGER NOT NULL,
                    issues_json TEXT NOT NULL,
                    disagreement REAL NOT NULL,
                    contradiction INTEGER NOT NULL,
                    support_score REAL NOT NULL,
                    state_after_json TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    FOREIGN KEY(task_id) REFERENCES tasks(id)
                );

                CREATE TABLE IF NOT EXISTS approvals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id TEXT NOT NULL,
                    approver TEXT NOT NULL,
                    decision TEXT NOT NULL,
                    notes TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    FOREIGN KEY(task_id) REFERENCES tasks(id)
                );

                CREATE TABLE IF NOT EXISTS route_stats (
                    route TEXT PRIMARY KEY,
                    attempts REAL NOT NULL,
                    approvals REAL NOT NULL,
                    updated_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS route_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id TEXT NOT NULL,
                    route TEXT NOT NULL,
                    approved INTEGER NOT NULL,
                    created_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS memories (
                    key TEXT PRIMARY KEY,
                    tags_json TEXT NOT NULL,
                    summary TEXT NOT NULL,
                    reinforcement REAL NOT NULL,
                    expires_at_tick INTEGER NOT NULL,
                    last_used_tick INTEGER NOT NULL,
                    updated_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS runtime_meta (
                    name TEXT PRIMARY KEY,
                    value_json TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );
                """
            )

    def create_task(self, task: Task) -> None:
        timestamp = utc_now()
        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO tasks (
                    id, description, novelty, risk, tags_json, expected_fields_json,
                    status, final_summary, requires_human, approved, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    task.task_id,
                    task.description,
                    task.novelty,
                    task.risk,
                    json.dumps(task.tags),
                    json.dumps(task.expected_fields),
                    "pending",
                    None,
                    0,
                    0,
                    timestamp,
                    timestamp,
                ),
            )

    def get_task(self, task_id: str) -> dict[str, Any] | None:
        with self._connect() as connection:
            task_row = connection.execute(
                "SELECT * FROM tasks WHERE id = ?",
                (task_id,),
            ).fetchone()
            if task_row is None:
                return None
            return self._task_payload(connection, task_row)

    def get_task_model(self, task_id: str) -> Task | None:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM tasks WHERE id = ?",
                (task_id,),
            ).fetchone()
            if row is None:
                return None
            return self._row_to_task(row)

    def list_tasks(self, limit: int = 50) -> list[dict[str, Any]]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT * FROM tasks
                ORDER BY updated_at DESC, created_at DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
            return [self._task_payload(connection, row) for row in rows]

    def replace_task_run(
        self,
        outcome: RunOutcome,
        route_stats: list[RouteStat],
        memories: list[MemoryRecord],
        *,
        memory_tick: int,
    ) -> None:
        timestamp = utc_now()
        status = "awaiting_approval" if outcome.status == "escalated" else outcome.status
        requires_human = 1 if outcome.status == "escalated" else 0
        with self._connect() as connection:
            connection.execute(
                """
                UPDATE tasks
                SET status = ?, final_summary = ?, requires_human = ?, updated_at = ?
                WHERE id = ?
                """,
                (
                    status,
                    outcome.final_summary,
                    requires_human,
                    timestamp,
                    outcome.task.task_id,
                ),
            )

            connection.execute(
                "DELETE FROM episodes WHERE task_id = ?",
                (outcome.task.task_id,),
            )
            for step_no, episode in enumerate(outcome.episodes, start=1):
                connection.execute(
                    """
                    INSERT INTO episodes (
                        task_id, step_no, mode, breath_phase, route, objective, attempt,
                        summary, provided_fields_json, schema_valid, evidence_ratio,
                        novelty_coverage, confidence, completed, requested_human,
                        approved, blocking, requires_human, issues_json, disagreement,
                        contradiction, support_score, state_after_json, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        outcome.task.task_id,
                        step_no,
                        episode.step.mode.value,
                        episode.step.breath_phase.value,
                        episode.step.route,
                        episode.step.objective,
                        episode.step.attempt,
                        episode.result.summary,
                        json.dumps(episode.result.provided_fields),
                        int(episode.result.schema_valid),
                        episode.result.evidence_ratio,
                        episode.result.novelty_coverage,
                        episode.result.confidence,
                        int(episode.result.completed),
                        int(episode.result.requested_human),
                        int(episode.review.approved),
                        int(episode.review.blocking),
                        int(episode.review.requires_human),
                        json.dumps(episode.review.issues),
                        episode.review.disagreement,
                        int(episode.review.contradiction),
                        episode.review.support_score,
                        json.dumps(self._serialize_state(episode.state_after)),
                        timestamp,
                    ),
                )

            connection.execute("DELETE FROM route_stats")
            connection.executemany(
                """
                INSERT INTO route_stats (route, attempts, approvals, updated_at)
                VALUES (?, ?, ?, ?)
                """,
                [
                    (stat.route, stat.attempts, stat.approvals, timestamp)
                    for stat in route_stats
                ],
            )

            for episode in outcome.episodes:
                connection.execute(
                    """
                    INSERT INTO route_events (task_id, route, approved, created_at)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        outcome.task.task_id,
                        episode.step.route,
                        int(episode.review.approved),
                        timestamp,
                    ),
                )

            connection.execute("DELETE FROM memories")
            connection.executemany(
                """
                INSERT INTO memories (
                    key, tags_json, summary, reinforcement, expires_at_tick,
                    last_used_tick, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        record.key,
                        json.dumps(record.tags),
                        record.summary,
                        record.reinforcement,
                        record.expires_at_tick,
                        record.last_used_tick,
                        timestamp,
                    )
                    for record in memories
                ],
            )

            self._set_meta(connection, "memory_tick", memory_tick)

    def record_route_event(
        self,
        task_id: str,
        route: str,
        approved: bool,
    ) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO route_events (task_id, route, approved, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (task_id, route, int(approved), utc_now()),
            )

    def get_route_stats(self) -> list[RouteStat]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT route, attempts, approvals FROM route_stats"
            ).fetchall()
            return [
                RouteStat(
                    route=row["route"],
                    attempts=row["attempts"],
                    approvals=row["approvals"],
                )
                for row in rows
            ]

    def get_recent_route_history(self, limit: int = 20) -> list[str]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT route FROM route_events
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
            return [row["route"] for row in reversed(rows)]

    def get_memories(self) -> list[MemoryRecord]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT key, tags_json, summary, reinforcement, expires_at_tick, last_used_tick
                FROM memories
                """
            ).fetchall()
            return [
                MemoryRecord(
                    key=row["key"],
                    tags=tuple(json.loads(row["tags_json"])),
                    summary=row["summary"],
                    reinforcement=row["reinforcement"],
                    expires_at_tick=row["expires_at_tick"],
                    last_used_tick=row["last_used_tick"],
                )
                for row in rows
            ]

    def get_memory_tick(self) -> int:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT value_json FROM runtime_meta WHERE name = 'memory_tick'"
            ).fetchone()
            if row is None:
                return 0
            return int(json.loads(row["value_json"]))

    def record_approval(
        self,
        task_id: str,
        *,
        approver: str,
        decision: str,
        notes: str,
    ) -> None:
        timestamp = utc_now()
        approved = 1 if decision == "approve" else 0
        status = "approved" if approved else "rejected"
        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO approvals (task_id, approver, decision, notes, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (task_id, approver, decision, notes, timestamp),
            )
            connection.execute(
                """
                UPDATE tasks
                SET status = ?, approved = ?, updated_at = ?
                WHERE id = ?
                """,
                (status, approved, timestamp, task_id),
            )

    def get_runtime_snapshot(self) -> dict[str, Any]:
        with self._connect() as connection:
            task_count = connection.execute("SELECT COUNT(*) AS n FROM tasks").fetchone()["n"]
            approval_count = connection.execute(
                "SELECT COUNT(*) AS n FROM approvals"
            ).fetchone()["n"]
        route_stats = self.get_route_stats()
        memories = self.get_memories()
        return {
            "db_path": str(self.db_path),
            "task_count": task_count,
            "approval_count": approval_count,
            "memory_tick": self.get_memory_tick(),
            "memory_count": len(memories),
            "route_stats": [
                {
                    "route": stat.route,
                    "attempts": stat.attempts,
                    "approvals": stat.approvals,
                }
                for stat in route_stats
            ],
            "recent_routes": self.get_recent_route_history(),
        }

    def _task_payload(
        self,
        connection: sqlite3.Connection,
        row: sqlite3.Row,
    ) -> dict[str, Any]:
        episodes = connection.execute(
            """
            SELECT * FROM episodes
            WHERE task_id = ?
            ORDER BY step_no ASC
            """,
            (row["id"],),
        ).fetchall()
        approvals = connection.execute(
            """
            SELECT approver, decision, notes, created_at
            FROM approvals
            WHERE task_id = ?
            ORDER BY id ASC
            """,
            (row["id"],),
        ).fetchall()
        return {
            "task_id": row["id"],
            "description": row["description"],
            "novelty": row["novelty"],
            "risk": row["risk"],
            "tags": json.loads(row["tags_json"]),
            "expected_fields": json.loads(row["expected_fields_json"]),
            "status": row["status"],
            "final_summary": row["final_summary"],
            "requires_human": bool(row["requires_human"]),
            "approved": bool(row["approved"]),
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
            "episodes": [self._episode_payload(episode) for episode in episodes],
            "approvals": [dict(approval) for approval in approvals],
        }

    @staticmethod
    def _episode_payload(row: sqlite3.Row) -> dict[str, Any]:
        return {
            "step_no": row["step_no"],
            "mode": row["mode"],
            "breath_phase": row["breath_phase"],
            "route": row["route"],
            "objective": row["objective"],
            "attempt": row["attempt"],
            "summary": row["summary"],
            "provided_fields": json.loads(row["provided_fields_json"]),
            "schema_valid": bool(row["schema_valid"]),
            "evidence_ratio": row["evidence_ratio"],
            "novelty_coverage": row["novelty_coverage"],
            "confidence": row["confidence"],
            "completed": bool(row["completed"]),
            "requested_human": bool(row["requested_human"]),
            "review": {
                "approved": bool(row["approved"]),
                "blocking": bool(row["blocking"]),
                "requires_human": bool(row["requires_human"]),
                "issues": json.loads(row["issues_json"]),
                "disagreement": row["disagreement"],
                "contradiction": bool(row["contradiction"]),
                "support_score": row["support_score"],
            },
            "state_after": json.loads(row["state_after_json"]),
            "created_at": row["created_at"],
        }

    @staticmethod
    def _serialize_state(state: ACPState | None) -> dict[str, Any]:
        if state is None:
            return {}
        payload = asdict(state)
        for key in ("last_mode", "last_route", "breath_phase"):
            value = payload.get(key)
            if hasattr(value, "value"):
                payload[key] = value.value
        return payload

    @staticmethod
    def _row_to_task(row: sqlite3.Row) -> Task:
        return Task(
            task_id=row["id"],
            description=row["description"],
            novelty=row["novelty"],
            risk=row["risk"],
            tags=tuple(json.loads(row["tags_json"])),
            expected_fields=tuple(json.loads(row["expected_fields_json"])),
        )

    @staticmethod
    def _set_meta(
        connection: sqlite3.Connection,
        name: str,
        value: Any,
    ) -> None:
        connection.execute(
            """
            INSERT INTO runtime_meta (name, value_json, updated_at)
            VALUES (?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET
                value_json = excluded.value_json,
                updated_at = excluded.updated_at
            """,
            (name, json.dumps(value), utc_now()),
        )

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path, timeout=5.0)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA busy_timeout=5000")
        return connection
