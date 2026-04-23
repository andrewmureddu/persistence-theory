# Session log — 2026-04-21: Heisenberg reconciliation after A.20

## What I worked on

I took the cleanest partial item left behind by the A.20 expansion: reconciling the older Schur-bridge "derive Heisenberg from persistence" program with the newer restraint-power result that already identifies Heisenberg as a special case.

## Why this was the right frontier

The project trackers were carrying a mild ambiguity:

1. `bridges/schur_complement.md` still phrased the uncertainty-principle connection as an open derivation chain.
2. `bridges/restraint_power.md` already proved Theorem A.20.27, which identifies the Robertson bound with the coordination floor on a two-MASA partition.
3. `OPEN_PROBLEMS.md` therefore had a hybrid OP-6 whose real task was not "solve Heisenberg" but "say exactly what A.20 did and did not solve."

That made this a good housekeeping-plus-clarity pass: it tightens the conceptual architecture without forcing a new theorem.

## What I changed

### `bridges/schur_complement.md`

- Rewrote §6.4 so it no longer treats "Heisenberg from persistence" as a single undifferentiated open problem.
- Recorded the precise split:
  - A.20 **does** close the structural question by showing that, given a conjugate two-MASA partition with commutator `[A,B] = i\kappa I`, the restraint-power floor coincides with the Robertson bound.
  - A.20 does **not** derive the canonical commutator / CCR structure from ACP axioms alone.
- Redirected the residual stronger problem to the already sharper tracker `OP-RP-5` in `bridges/restraint_power.md`.

### `OPEN_PROBLEMS.md`

- Moved OP-6 from Open to Resolved.
- Wrote the resolution summary so future passes do not reopen the wrong question.

### `STATUS.md`

- Updated the Schur-bridge inventory line to reflect that the Heisenberg connection is now reconciled with A.20.
- Updated the open-problem summary so it points to OP-3 through OP-5 as the remaining Schur-bridge items.
- Added a changelog entry for this session.

## What this resolves

- The workspace no longer has two documents talking past each other about whether Heisenberg is "open."
- The exact boundary is now explicit:
  - **Closed:** Heisenberg as the quantum-scale coordination floor, once the conjugate partition is given.
  - **Open:** derivation of the commutator / CCR structure itself from ACP persistence.

## Best next step

The natural continuation is either:

1. write the short bibliography-policy pass for OP-14, or
2. push the stronger operator-algebra frontier by sharpening OP-RP-5 and asking what minimal hypotheses would let `rank(D) > 0` force non-commutativity in a von Neumann-algebra setting.
