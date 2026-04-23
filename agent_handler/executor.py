from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Protocol, Sequence

from .models import ActionResult, BreathPhase, Episode, MemoryRecord, Mode, PlanStep, Task
from .policy import clamp


class ExecutionAdapter(Protocol):
    def execute(
        self,
        task: Task,
        step: PlanStep,
        history: Sequence[Episode],
        memories: Sequence[MemoryRecord],
    ) -> ActionResult:
        ...


@dataclass(frozen=True)
class OpenAIExecutorConfig:
    api_key: str | None
    model: str
    reasoning_effort: str | None
    max_output_tokens: int
    timeout_seconds: float
    base_url: str | None
    organization: str | None
    project: str | None

    @classmethod
    def from_env(cls) -> "OpenAIExecutorConfig":
        api_key = os.getenv("OPENAI_API_KEY")
        model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")
        reasoning_effort = os.getenv("OPENAI_REASONING_EFFORT", "medium") or None
        max_output_tokens = int(os.getenv("OPENAI_MAX_OUTPUT_TOKENS", "800"))
        timeout_seconds = float(os.getenv("OPENAI_TIMEOUT_SECONDS", "60"))
        base_url = os.getenv("OPENAI_BASE_URL") or None
        organization = os.getenv("OPENAI_ORG_ID") or None
        project = os.getenv("OPENAI_PROJECT_ID") or None
        return cls(
            api_key=api_key,
            model=model,
            reasoning_effort=reasoning_effort,
            max_output_tokens=max_output_tokens,
            timeout_seconds=timeout_seconds,
            base_url=base_url,
            organization=organization,
            project=project,
        )


class DemoExecutionAdapter:
    def execute(
        self,
        task: Task,
        step: PlanStep,
        history: Sequence[Episode],
        memories: Sequence[MemoryRecord],
    ) -> ActionResult:
        grounded = any(
            episode.step.mode is Mode.GROUND
            or episode.step.breath_phase is BreathPhase.INHALE
            for episode in history
        )
        pondered = any(episode.step.breath_phase is BreathPhase.HOLD_IN for episode in history)
        diversified = any(episode.step.mode is Mode.DIVERSIFY for episode in history)
        memory_help = min(0.18, 0.06 * len(memories))
        contradiction = 0.0

        if step.mode is Mode.ESCALATE:
            provided = self._provided_fields(task, 0.85, completed=False)
            return ActionResult(
                step=step,
                summary=f"Escalated {task.task_id} for human review.",
                provided_fields=provided,
                schema_valid=True,
                evidence_ratio=0.85,
                novelty_coverage=0.45,
                confidence=0.40,
                completed=False,
                requested_human=True,
            )

        if step.breath_phase is BreathPhase.INHALE:
            route_bias = {
                "synthesis": (0.10, 0.04),
                "research": (0.14, 0.02),
                "what_if": (0.05, 0.14),
            }
            evidence_bonus, novelty_bonus = route_bias.get(step.route, (0.08, 0.04))
            evidence = clamp(0.46 + evidence_bonus + (0.12 * task.risk) + memory_help)
            novelty = clamp(0.34 + novelty_bonus + (0.22 * task.novelty))
            confidence = clamp(0.56 + (0.18 * (1.0 - task.novelty)))
            completed = task.novelty < 0.35 and task.risk < 0.45
            if task.novelty >= 0.80 and not grounded:
                contradiction = 0.55
            provided = self._provided_fields(task, evidence, completed=completed)
            return ActionResult(
                step=step,
                summary=f"Inhaled context for {task.task_id} via {step.route}.",
                provided_fields=provided,
                schema_valid=True,
                evidence_ratio=evidence,
                novelty_coverage=novelty,
                confidence=confidence,
                completed=completed,
                annotations={"contradiction": contradiction},
            )

        if step.breath_phase is BreathPhase.HOLD_IN:
            evidence = clamp(0.52 + (0.12 * task.risk) + (0.06 * grounded) + memory_help)
            novelty = clamp(0.48 + (0.18 * task.novelty))
            confidence = 0.50
            provided = self._provided_fields(task, evidence, completed=False)
            return ActionResult(
                step=step,
                summary=f"Held and pondered {task.task_id}.",
                provided_fields=provided,
                schema_valid=True,
                evidence_ratio=evidence,
                novelty_coverage=novelty,
                confidence=confidence,
                completed=False,
            )

        if step.breath_phase is BreathPhase.RELEASE:
            evidence = clamp(
                0.62
                + (0.14 * grounded)
                + (0.08 * pondered)
                + (0.06 * diversified)
                + (0.10 * task.risk)
                + memory_help
            )
            novelty = clamp(
                0.54
                + (0.20 * task.novelty)
                + (0.08 * pondered)
                + (0.06 * diversified)
            )
            confidence = clamp(0.66 + (0.06 * grounded) + (0.04 * pondered))
            provided = self._provided_fields(task, evidence, completed=True)
            return ActionResult(
                step=step,
                summary=f"Released competing predictions for {task.task_id} via {step.route}.",
                provided_fields=provided,
                schema_valid=evidence >= 0.45,
                evidence_ratio=evidence,
                novelty_coverage=novelty,
                confidence=confidence,
                completed=True,
            )

        evidence = clamp(0.58 + (0.10 * grounded) + (0.06 * pondered) + memory_help)
        novelty = clamp(0.42 + (0.12 * task.novelty))
        confidence = 0.52
        provided = self._provided_fields(task, evidence, completed=False)
        return ActionResult(
            step=step,
            summary=f"Held after release and consolidated {task.task_id}.",
            provided_fields=provided,
            schema_valid=True,
            evidence_ratio=evidence,
            novelty_coverage=novelty,
            confidence=confidence,
            completed=False,
        )

    @staticmethod
    def _provided_fields(task: Task, evidence: float, completed: bool) -> list[str]:
        fields = list(task.expected_fields)
        if not completed:
            cutoff = max(1, len(fields) // 2)
            return fields[:cutoff]
        if evidence < 0.55 and len(fields) > 1:
            return fields[:-1]
        return fields


class OpenAIExecutionAdapter:
    def __init__(self, config: OpenAIExecutorConfig | None = None) -> None:
        self.config = config or OpenAIExecutorConfig.from_env()
        if not self.config.api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Set it before using the OpenAI execution backend."
            )
        try:
            from openai import OpenAI
        except ImportError as exc:  # pragma: no cover - depends on local install
            raise RuntimeError(
                "The `openai` package is not installed. Install it with "
                "`python3 -m pip install -r agent_handler/requirements.txt`."
            ) from exc

        client_kwargs: dict[str, object] = {
            "api_key": self.config.api_key,
            "timeout": self.config.timeout_seconds,
        }
        if self.config.base_url:
            client_kwargs["base_url"] = self.config.base_url
        if self.config.organization:
            client_kwargs["organization"] = self.config.organization
        if self.config.project:
            client_kwargs["project"] = self.config.project
        self._client = OpenAI(**client_kwargs)

    def execute(
        self,
        task: Task,
        step: PlanStep,
        history: Sequence[Episode],
        memories: Sequence[MemoryRecord],
    ) -> ActionResult:
        if step.mode is Mode.ESCALATE:
            provided = self._fallback_fields(task, completed=False)
            return ActionResult(
                step=step,
                summary=f"Escalated {task.task_id} for human review.",
                provided_fields=provided,
                schema_valid=True,
                evidence_ratio=0.85,
                novelty_coverage=0.45,
                confidence=0.40,
                completed=False,
                requested_human=True,
            )

        response = self._client.responses.create(**self._request_kwargs(task, step, history, memories))
        payload = self._parse_payload(self._response_text(response))
        return self._to_action_result(task, step, payload)

    def _request_kwargs(
        self,
        task: Task,
        step: PlanStep,
        history: Sequence[Episode],
        memories: Sequence[MemoryRecord],
    ) -> dict[str, object]:
        kwargs: dict[str, object] = {
            "model": self.config.model,
            "instructions": self._instructions(),
            "input": self._input_text(task, step, history, memories),
            "max_output_tokens": self.config.max_output_tokens,
            "text": {"format": {"type": "json_object"}},
        }
        if self.config.reasoning_effort:
            kwargs["reasoning"] = {"effort": self.config.reasoning_effort}
        return kwargs

    @staticmethod
    def _instructions() -> str:
        return (
            "You are the execution backend inside an ACP agent handler. "
            "Return only a valid JSON object. "
            "Assess the current breath phase and task state carefully. "
            "Use these rules: inhale gathers and synthesizes, hold_in ponders without finalizing, "
            "release compares and selects a provisional winner, hold_out consolidates after release. "
            "Only mark completed=true when the step has genuinely produced a usable result for the current phase. "
            "If the work needs human approval or is too risky to finalize, set requested_human=true. "
            "All score fields must be numbers between 0 and 1. "
            "provided_fields must be a subset of expected_fields."
        )

    def _input_text(
        self,
        task: Task,
        step: PlanStep,
        history: Sequence[Episode],
        memories: Sequence[MemoryRecord],
    ) -> str:
        prior_steps = []
        for episode in history[-4:]:
            prior_steps.append(
                {
                    "mode": episode.step.mode.value,
                    "breath_phase": episode.step.breath_phase.value,
                    "route": episode.step.route,
                    "summary": episode.result.summary,
                    "issues": episode.review.issues,
                    "support_score": episode.review.support_score,
                }
            )
        memory_items = [
            {
                "key": record.key,
                "tags": list(record.tags),
                "summary": record.summary,
                "reinforcement": round(record.reinforcement, 4),
            }
            for record in memories[:3]
        ]
        output_contract = {
            "summary": "short string",
            "provided_fields": list(task.expected_fields),
            "schema_valid": "boolean",
            "evidence_ratio": "float 0..1",
            "novelty_coverage": "float 0..1",
            "confidence": "float 0..1",
            "completed": "boolean",
            "requested_human": "boolean",
            "annotations": {"contradiction": "float 0..1"},
        }
        payload = {
            "task": {
                "task_id": task.task_id,
                "description": task.description,
                "novelty": task.novelty,
                "risk": task.risk,
                "tags": list(task.tags),
                "expected_fields": list(task.expected_fields),
            },
            "step": {
                "mode": step.mode.value,
                "breath_phase": step.breath_phase.value,
                "route": step.route,
                "objective": step.objective,
                "attempt": step.attempt,
            },
            "history": prior_steps,
            "memories": memory_items,
            "output_contract": output_contract,
        }
        return json.dumps(payload, indent=2, sort_keys=True)

    @staticmethod
    def _response_text(response: object) -> str:
        text = getattr(response, "output_text", None)
        if isinstance(text, str) and text.strip():
            return text
        output = getattr(response, "output", None)
        if isinstance(output, list):
            chunks: list[str] = []
            for item in output:
                content = getattr(item, "content", None)
                if not isinstance(content, list):
                    continue
                for part in content:
                    part_text = getattr(part, "text", None)
                    if isinstance(part_text, str):
                        chunks.append(part_text)
            if chunks:
                return "\n".join(chunks)
        raise RuntimeError("OpenAI response did not contain output text.")

    @staticmethod
    def _parse_payload(raw_text: str) -> dict[str, object]:
        try:
            parsed = json.loads(raw_text)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            pass

        start = raw_text.find("{")
        end = raw_text.rfind("}")
        if start >= 0 and end > start:
            snippet = raw_text[start : end + 1]
            parsed = json.loads(snippet)
            if isinstance(parsed, dict):
                return parsed
        raise RuntimeError("Could not parse JSON from OpenAI response.")

    def _to_action_result(
        self,
        task: Task,
        step: PlanStep,
        payload: dict[str, object],
    ) -> ActionResult:
        completed = bool(payload.get("completed", False))
        if step.breath_phase in {BreathPhase.HOLD_IN, BreathPhase.HOLD_OUT}:
            completed = False
        if step.breath_phase is BreathPhase.INHALE and not (task.novelty < 0.35 and task.risk < 0.45):
            completed = False

        requested_human = bool(payload.get("requested_human", False))
        if task.risk >= 0.90 and step.breath_phase is BreathPhase.RELEASE:
            requested_human = True

        provided_fields = self._normalize_fields(task, payload.get("provided_fields"), completed)
        evidence_ratio = clamp(self._as_float(payload.get("evidence_ratio"), default=0.55))
        novelty_coverage = clamp(self._as_float(payload.get("novelty_coverage"), default=0.50))
        confidence = clamp(self._as_float(payload.get("confidence"), default=0.55))
        summary = str(payload.get("summary") or f"Executed {step.route} for {task.task_id}.")
        annotations = self._normalize_annotations(payload.get("annotations"))

        return ActionResult(
            step=step,
            summary=summary,
            provided_fields=provided_fields,
            schema_valid=bool(payload.get("schema_valid", True)),
            evidence_ratio=evidence_ratio,
            novelty_coverage=novelty_coverage,
            confidence=confidence,
            completed=completed,
            requested_human=requested_human,
            annotations=annotations,
        )

    @staticmethod
    def _normalize_annotations(raw_annotations: object) -> dict[str, float]:
        if not isinstance(raw_annotations, dict):
            return {}
        annotations: dict[str, float] = {}
        contradiction = raw_annotations.get("contradiction")
        if contradiction is not None:
            annotations["contradiction"] = clamp(OpenAIExecutionAdapter._as_float(contradiction, default=0.0))
        return annotations

    @staticmethod
    def _normalize_fields(
        task: Task,
        raw_fields: object,
        completed: bool,
    ) -> list[str]:
        expected = list(task.expected_fields)
        if not isinstance(raw_fields, list):
            return OpenAIExecutionAdapter._fallback_fields(task, completed=completed)
        provided = [field for field in raw_fields if isinstance(field, str) and field in expected]
        if provided:
            return provided
        return OpenAIExecutionAdapter._fallback_fields(task, completed=completed)

    @staticmethod
    def _fallback_fields(task: Task, completed: bool) -> list[str]:
        expected = list(task.expected_fields)
        if completed:
            return expected
        if not expected:
            return []
        cutoff = max(1, len(expected) // 2)
        return expected[:cutoff]

    @staticmethod
    def _as_float(value: object, default: float) -> float:
        try:
            return float(value)
        except (TypeError, ValueError):
            return default


def build_execution_adapter(backend: str) -> ExecutionAdapter:
    normalized = backend.strip().lower()
    if normalized == "demo":
        return DemoExecutionAdapter()
    if normalized == "openai":
        return OpenAIExecutionAdapter()
    raise ValueError(f"Unsupported backend: {backend}")
