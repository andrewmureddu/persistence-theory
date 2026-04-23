from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Sequence, Tuple


class Mode(str, Enum):
    GROUND = "ground"
    EXPLOIT = "exploit"
    DIVERSIFY = "diversify"
    ESCALATE = "escalate"


class BreathPhase(str, Enum):
    INHALE = "inhale"
    HOLD_IN = "hold_in"
    RELEASE = "release"
    HOLD_OUT = "hold_out"


@dataclass(frozen=True)
class Task:
    task_id: str
    description: str
    novelty: float
    risk: float
    tags: Tuple[str, ...]
    expected_fields: Tuple[str, ...]


@dataclass
class ACPState:
    task_id: str
    novelty: float
    risk: float
    confidence: float = 0.0
    dissolution_score: float = 0.0
    crystallization_score: float = 0.0
    route_entropy: float = 1.0
    route_dominance: float = 0.0
    memory_concentration: float = 0.0
    critic_disagreement: float = 0.0
    retry_depth: int = 0
    same_route_streak: int = 0
    last_mode: Optional[Mode] = None
    last_route: Optional[str] = None
    breath_phase: Optional[BreathPhase] = None
    breath_cycle: int = 0


@dataclass(frozen=True)
class PlanStep:
    mode: Mode
    breath_phase: BreathPhase
    route: str
    objective: str
    attempt: int


@dataclass
class ActionResult:
    step: PlanStep
    summary: str
    provided_fields: List[str]
    schema_valid: bool
    evidence_ratio: float
    novelty_coverage: float
    confidence: float
    completed: bool
    requested_human: bool = False
    annotations: Dict[str, float] = field(default_factory=dict)


@dataclass
class ReviewResult:
    approved: bool
    blocking: bool
    requires_human: bool
    issues: List[str]
    disagreement: float
    contradiction: bool
    support_score: float


@dataclass
class MemoryRecord:
    key: str
    tags: Tuple[str, ...]
    summary: str
    reinforcement: float
    expires_at_tick: int
    last_used_tick: int


@dataclass
class Episode:
    step: PlanStep
    result: ActionResult
    review: ReviewResult
    state_after: Optional[ACPState] = None


@dataclass
class RunOutcome:
    task: Task
    status: str
    episodes: Sequence[Episode]
    final_state: ACPState
    final_summary: str
