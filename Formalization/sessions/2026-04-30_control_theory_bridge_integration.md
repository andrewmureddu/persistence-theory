# Session log — 2026-04-30: control-theory bridge integration

## Goal

Continue the ACP project by absorbing the new standalone control-theory reduction into the live manuscript and tracker layer without overstating it as a completed numbered appendix.

## What changed

### `paper/acp_main_v10.md`

- Added control-theory language to §4.4.6, identifying the viable continuation count \(N_h(m_t)\) as the control-native entropy proxy.
- Added §7.10 to name the remaining control-theory continuation-variety problem:
  - quantitative nonlinear / continuous-time bridge;
  - tracking-versus-crystallization criterion;
  - decentralized visibility through action-as-signal;
  - adaptive-controller CDT closure.
- Added discussion language clarifying that the control note extends the reduction pattern as a standalone bridge, not as a numbered seventh appendix reduction.
- Added Appendix C summary language for the working-note status of `reductions/control_theory.md`.

### `OPEN_PROBLEMS.md`

- Added OP-20, tracking the control-theory continuation-variety bridge.

### `STATUS.md`

- Updated the live timestamp.
- Added the control-theory bridge to the result inventory.
- Added a new active front for the control-theory bridge and continuation-variety program.
- Added OP-20 to the headline open-problem list.
- Added a changelog entry for this integration pass.

### Website copy

- Updated the landing page's recent-additions note.
- Updated the theory page to mention the control-theory bridge front.

## Status split

**Now established:**

- The control-theory note is visible from the main paper's live framing.
- The six-reduction headline remains intact: control theory is a standalone bridge / future-appendix front.
- The main open control-theory obligations are now canonical in OP-20.

**Still open:**

- A quantitative nonlinear viable-continuation bridge.
- A sharp exact-tracking versus crystallization criterion.
- A Witsenhausen-style decentralized visibility note.
- A saturated-control toy simulator or adaptive-controller aging prototype.

## Verification

- `npm run build` succeeds for the website.
- The generated library includes `reductions/control_theory`, the new session logs, and the existing `metaphysical_game_protocols` essay.

## Recommended next move

Choose between:

1. write the Witsenhausen / action-as-signal restraint-power note;
2. build a saturated-control toy simulator around anti-windup and continuation variety;
3. start the quantitative viable-tube / covering-number bridge for OP-20.
