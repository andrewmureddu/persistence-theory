from __future__ import annotations

from .models import ACPState, BreathPhase, Mode


class BreathingOperator:
    def choose_phase(self, state: ACPState, mode: Mode) -> BreathPhase:
        if mode is Mode.GROUND:
            return BreathPhase.INHALE
        if mode is Mode.DIVERSIFY:
            return BreathPhase.RELEASE
        if mode is Mode.ESCALATE:
            return BreathPhase.HOLD_OUT
        if state.breath_phase is None:
            return BreathPhase.INHALE
        return self._next_phase(state.breath_phase)

    @staticmethod
    def _next_phase(phase: BreathPhase) -> BreathPhase:
        sequence = (
            BreathPhase.INHALE,
            BreathPhase.HOLD_IN,
            BreathPhase.RELEASE,
            BreathPhase.HOLD_OUT,
        )
        index = sequence.index(phase)
        return sequence[(index + 1) % len(sequence)]
