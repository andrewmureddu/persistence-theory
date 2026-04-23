from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from .service import AgentService
from .storage import DEFAULT_DB_PATH

_APP_IMPORT_ERROR: str | None = None


def create_app(
    db_path: str | Path | None = None,
    *,
    backend: str | None = None,
):
    try:
        from fastapi import FastAPI, HTTPException, Query
    except ImportError as exc:
        raise RuntimeError(
            "FastAPI dependencies are not installed. "
            "Install them with `python3 -m pip install -r agent_handler/requirements.txt`."
        ) from exc

    service = AgentService(
        db_path or DEFAULT_DB_PATH,
        backend=backend or os.getenv("AGENT_HANDLER_BACKEND"),
    )
    app = FastAPI(title="ACP Agent Handler", version="0.1.0")

    def translate_error(exc: Exception) -> HTTPException:
        if isinstance(exc, KeyError):
            return HTTPException(status_code=404, detail="Task not found.")
        if isinstance(exc, ValueError):
            return HTTPException(status_code=400, detail=str(exc))
        return HTTPException(status_code=500, detail=str(exc))

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {"status": "ok", "runtime": service.runtime_state()}

    @app.get("/tasks")
    def list_tasks(limit: int = Query(default=50, ge=1, le=200)) -> list[dict[str, Any]]:
        return service.list_tasks(limit=limit)

    @app.get("/tasks/{task_id}")
    def get_task(task_id: str) -> dict[str, Any]:
        try:
            return service.get_task(task_id)
        except Exception as exc:  # pragma: no cover - exercised through HTTP
            raise translate_error(exc) from exc

    @app.post("/tasks")
    def create_task(payload: dict[str, Any]) -> dict[str, Any]:
        try:
            return service.submit_task(
                task_id=payload.get("task_id"),
                description=str(payload["description"]),
                novelty=float(payload["novelty"]),
                risk=float(payload["risk"]),
                tags=list(payload.get("tags", [])),
                expected_fields=list(payload.get("expected_fields", [])),
                run_now=bool(payload.get("run_now", False)),
            )
        except KeyError as exc:
            raise HTTPException(status_code=400, detail=f"Missing field: {exc.args[0]}") from exc
        except Exception as exc:  # pragma: no cover - exercised through HTTP
            raise translate_error(exc) from exc

    @app.post("/tasks/{task_id}/run")
    def run_task(task_id: str) -> dict[str, Any]:
        try:
            return service.run_task(task_id)
        except Exception as exc:  # pragma: no cover - exercised through HTTP
            raise translate_error(exc) from exc

    @app.post("/tasks/{task_id}/approve")
    def approve_task(task_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        try:
            return service.approve_task(
                task_id,
                approver=str(payload["approver"]),
                notes=str(payload.get("notes", "")),
                decision=str(payload.get("decision", "approve")),
            )
        except KeyError as exc:
            raise HTTPException(status_code=400, detail=f"Missing field: {exc.args[0]}") from exc
        except Exception as exc:  # pragma: no cover - exercised through HTTP
            raise translate_error(exc) from exc

    @app.get("/runtime")
    def runtime() -> dict[str, Any]:
        return service.runtime_state()

    return app


try:
    app = create_app()
except RuntimeError as exc:  # pragma: no cover - depends on local deps
    app = None
    _APP_IMPORT_ERROR = str(exc)


if __name__ == "__main__":
    if _APP_IMPORT_ERROR is not None:
        raise SystemExit(_APP_IMPORT_ERROR)
    try:
        import uvicorn
    except ImportError as exc:  # pragma: no cover - depends on local deps
        raise SystemExit(
            "Uvicorn is not installed. Install it with "
            "`python3 -m pip install -r agent_handler/requirements.txt`."
        ) from exc
    uvicorn.run("agent_handler.api:app", host="127.0.0.1", port=8000, reload=False)
