# Session log - 2026-04-30: workflow generativity check

## Goal

Review whether the ACP project is obeying its own A.21 requirement: a living theory should open more disciplined questions than it closes. The immediate workflow issue was that the project already states this principle, but the session closeout routine did not yet require a compact generativity ledger.

## What changed

- Added `WORKFLOW.md` as an operating protocol for session-level ACP self-application.
- Added the workflow file to the `README.md` starting map.
- Updated `CLAUDE.md` so future theory-building sessions read `WORKFLOW.md` and include a generativity ledger when theory content changes.
- Updated `agent_handler/README.md` so non-routine research tasks treat successor questions, new observables, and new tests as first-class expected fields.
- Updated `STATUS.md` with this changelog entry.

## Generativity ledger

- Closed / strengthened (`C_closed`):
  - Strengthened the operating workflow by making A.21's "open more questions than it closes" rule an explicit closeout gate.

- New questions (`Q_new`):
  - Should the agent handler eventually enforce `successor_questions` mechanically in `ActionResult` and `Critic`, rather than only documenting the expected field?
  - Should `STATUS.md` maintain a rolling session-level `G_session` audit, or is per-session logging enough?
  - Which sessions should be exempt as maintenance so the workflow does not manufacture artificial questions?

- New observables or bridge variables (`O_new`):
  - Session-level `G_session`.
  - Boundary-pressure labels: crystallization pressure from over-closure; dissolution pressure from ungrounded probing.

- New tests, falsifiers, or simulations (`P_new`):
  - Future session logs can be audited for presence of a generativity ledger.
  - Non-routine agent-handler tasks can be checked for `successor_questions`, `new_observables`, or `new_tests` in expected fields.

- Workflow check: `G_session = (3 + 2 + 2) / max(1, 1) = 7`.
- Boundary assessment: the project is passing the A.21 test at the formal/research-tracker level, but needed a workflow-level restraint mechanism so the check is made before closure hardens.

## Assessment

The recent project trajectory is generative: A.21, the cross-domain protocol, the historical blind-spot audit, the control bridge, and the three-stroke operator bridge all leave explicit open fronts. The weaker spot was process: question-opening lived in `STATUS.md` and the bridge notes, but not yet as a mandatory session-close habit.
