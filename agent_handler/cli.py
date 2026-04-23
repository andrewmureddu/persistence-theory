from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .service import AgentService
from .storage import DEFAULT_DB_PATH


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python3 -m agent_handler.cli",
        description="Codex-native CLI for the ACP agent handler service.",
    )
    parser.add_argument(
        "--db",
        default=str(DEFAULT_DB_PATH),
        help="Path to the SQLite database file.",
    )
    parser.add_argument(
        "--backend",
        default=None,
        choices=("demo", "openai"),
        help="Execution backend. Defaults to AGENT_HANDLER_BACKEND or demo.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    submit = subparsers.add_parser("submit", help="Create a task.")
    submit.add_argument("--task-id", default=None, help="Optional explicit task id.")
    submit.add_argument("--description", required=True, help="Task description.")
    submit.add_argument("--novelty", type=float, required=True, help="Task novelty, 0-1.")
    submit.add_argument("--risk", type=float, required=True, help="Task risk, 0-1.")
    submit.add_argument(
        "--tags",
        nargs="*",
        default=[],
        help="Task tags used for routing and memory overlap.",
    )
    submit.add_argument(
        "--fields",
        nargs="*",
        default=[],
        help="Expected output fields.",
    )
    submit.add_argument(
        "--run-now",
        action="store_true",
        help="Run the task immediately after creation.",
    )

    run = subparsers.add_parser("run", help="Run an existing task.")
    run.add_argument("task_id", help="Task id to run.")

    show = subparsers.add_parser("show", help="Show a task.")
    show.add_argument("task_id", help="Task id to display.")

    list_tasks = subparsers.add_parser("list", help="List tasks.")
    list_tasks.add_argument("--limit", type=int, default=20, help="Maximum tasks to return.")

    approve = subparsers.add_parser("approve", help="Approve an escalated task.")
    approve.add_argument("task_id", help="Task id to approve.")
    approve.add_argument("--approver", required=True, help="Approver name.")
    approve.add_argument("--notes", default="", help="Optional approval notes.")
    approve.add_argument(
        "--decision",
        choices=("approve", "reject"),
        default="approve",
        help="Approval decision.",
    )

    subparsers.add_parser("runtime", help="Show shared runtime state.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    service = AgentService(Path(args.db), backend=args.backend)

    try:
        if args.command == "submit":
            payload = service.submit_task(
                task_id=args.task_id,
                description=args.description,
                novelty=args.novelty,
                risk=args.risk,
                tags=args.tags,
                expected_fields=args.fields,
                run_now=args.run_now,
            )
        elif args.command == "run":
            payload = service.run_task(args.task_id)
        elif args.command == "show":
            payload = service.get_task(args.task_id)
        elif args.command == "list":
            payload = service.list_tasks(limit=args.limit)
        elif args.command == "approve":
            payload = service.approve_task(
                args.task_id,
                approver=args.approver,
                notes=args.notes,
                decision=args.decision,
            )
        elif args.command == "runtime":
            payload = service.runtime_state()
        else:  # pragma: no cover - argparse should prevent this
            parser.error(f"Unknown command: {args.command}")
            return 2
    except KeyError as exc:
        parser.exit(1, f"Task not found: {exc.args[0]}\n")
    except ValueError as exc:
        parser.exit(1, f"{exc}\n")
    except RuntimeError as exc:
        parser.exit(1, f"{exc}\n")

    print(render_json(payload))
    return 0


def render_json(payload: Any) -> str:
    return json.dumps(payload, indent=2, sort_keys=True)


if __name__ == "__main__":
    raise SystemExit(main())
