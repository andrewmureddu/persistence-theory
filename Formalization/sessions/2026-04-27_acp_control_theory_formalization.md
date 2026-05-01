# Session log — 2026-04-27: ACP control-theory formalization

## Goal

Write the first theorem-style control-theory note in the ACP workspace instead of leaving control as scattered literature-survey evidence. The target was a clean ACP register, not yet a main-paper integration.

## What changed

### `reductions/control_theory.md`

- Added a standalone control-theory reduction note.
- Defined the control-native macrostate as a regulation profile built from:
  - state estimate;
  - active controller mode;
  - horizon-\(h\) viable continuation set;
  - actuator headroom.
- Introduced the key bridge object: the **information-conditioned viable continuation count** \(N_h(m_t)\).
- Proved the support-size bridge:
  - \(0 \le H(m_{t+h}\mid m_t) \le \log N_h(m_t)\);
  - \(N_h = 1\) iff local control entropy is zero;
  - \(1 < N_h < N_{\max,h}\) is the productive interval in control language.
- Formalized the lower ACP boundary with the data-rate theorem:
  - below the unstable-mode information floor, bounded regulation fails and the loop dissolves.
- Formalized the upper ACP boundary with saturation-locked regulation:
  - if all viable recoveries in a task neighborhood collapse to the same saturated sequence, the loop crystallizes.
- Added structural corollaries:
  - Bode sensitivity integral as productive-interval geometry / fragility conservation;
  - anti-windup as anti-crystallization;
  - a local restraint-power reading of the same anti-windup move.
- Added a deliberately weaker CDT neighbor:
  - adaptive / gain-scheduled / learned controllers likely contract continuation variety under repeated envelope-specific success, but this is left as a conjectural corollary pending the broader maintenance front.
- Added three testable predictions and four scoped open problems.

### `STATUS.md`

- Updated the workspace timestamp.
- Added the new control-theory note to the session index.

## Status split

**Now established:**

- Control theory has a domain-native ACP register using viable continuation variety rather than analogy alone.
- The control-side dissolution boundary can be stated sharply using data-rate-limited stabilization.
- The control-side crystallization boundary can be stated sharply using local saturation lock and headroom collapse.
- Bode’s waterbed law gives a clean explanation of why the productive interval is structurally unavoidable.
- Anti-windup is best read not only as a performance patch, but as an explicit adaptive coherence steering device.

**Still open:**

- Quantitative entropy / viable-volume mapping for nonlinear and continuous-time plants.
- A sharper criterion distinguishing ordinary exact tracking from genuine crystallization.
- Decentralized visibility formalization via Witsenhausen-style action-as-signal.
- Full CDT closure for adaptive / learned controllers via a control-native maintenance theorem.

## Recommended next move

One of three follow-ons now looks natural:

1. Promote a compressed version of this note into the main paper’s “existing results / neighbors” discussion, tightening the control-theory language around Section 4.4.6.
2. Build a second note around Witsenhausen + anti-windup to formalize the control-theoretic restraint-power layer more directly.
3. Add a small saturated-control toy simulator so the new predictions are operationalized rather than only stated.
