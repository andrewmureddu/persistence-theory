# 2026-05-01 — CDT Maintenance Renewal

## Aim

Work on the CDT open problems, focusing on OP-16: the maintenance lemma / net
reinforcement pressure gap behind the full load, basin, and asymptotic version
of the Crystallization Drift Theorem.

## What changed

- Extended `proofs/maintenance_lemma.md` with a first model-class closure:
  deficit-responsive renewal systems.
- Defined loss hazards $\ell_t(R)$, replacement probabilities $q_t(R)$,
  expected replacement pressures $y_t(R)$, survivor/coherent increment $U_t$,
  and the renewal-dominance inequality.
- Proved that renewal dominance makes net entropy-reducing pressure $\Pi(t)$ a
  submartingale, with pathwise monotonicity when the dominance inequality holds
  pathwise.
- Added unit-replacement and load-renewal corollaries.
- Updated `OPEN_PROBLEMS.md`, `STATUS.md`, `paper/acp_main_v10.md`, and
  `proofs/crystallization_drift_theorem.md` so OP-16 is recorded as partial with
  a first model-class closure, not as generically resolved.

## Technical result

The new theorem decomposes the pressure increment as

$$
\Pi(t+h)-\Pi(t)=I_t+U_t-D_t,
$$

where $D_t$ is shed pressure, $I_t$ is incoming replacement pressure, and $U_t$
is survivor strengthening plus coherent-excess change. In a
deficit-responsive renewal system,

$$
\mathbb E[I_t\mid\mathcal F_t]
\geq
\sum_{R\in\mathcal R_t}\ell_t(R)q_t(R)y_t(R),
$$

while

$$
\mathbb E[D_t\mid\mathcal F_t]
=
\sum_{R\in\mathcal R_t}\ell_t(R)\pi(R,t).
$$

Thus the renewal-dominance inequality is exactly the condition that expected
replacement pressure plus survivor/coherent increment dominate expected shed
pressure. Lemma OP-16.1 then yields the maintained-pressure hypothesis required
by the CDT core.

## Generativity ledger

- Closed / strengthened (`C_closed`): OP-16 now has a first target-class theorem
  rather than only a bookkeeping lemma.
- New questions (`Q_new`): Which ACP systems possess detectable deficit-response
  channels? When does maintenance use renewal rather than shrinking to fewer
  high-pressure mechanisms? Which control, ecological, or population-genetic
  systems satisfy renewal dominance?
- New observables or bridge variables (`O_new`): loss hazard $\ell_t(R)$,
  replacement probability $q_t(R)$, replacement pressure $y_t(R)$,
  survivor/coherent increment $U_t$, renewal-dominance margin.
- New tests, falsifiers, or simulations (`P_new`): estimate the
  renewal-dominance margin in adaptive-controller, organizational, ecological,
  or evolutionary simulations; failure of the margin falsifies the
  model-class maintenance claim for that system.
- Workflow check: `G_session = (3 + 5 + 1) / max(1, 1) = 9`.
- Boundary assessment: progress is theorem-shaped but remains productive rather
  than closed, because the new result exposes measurable renewal variables and a
  sharper classification problem.
