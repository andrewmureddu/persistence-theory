# 2026-05-01 — CDT Intersection Closure

## Aim

Continue the CDT open-problem work by attacking OP-17: the generic
k-mechanism intersection-closure gap in Appendix A.9.

## What changed

- Extended `proofs/induction_step_k_mechanisms.md` with a first structured
  non-Gaussian closure class: aligned positive-association kernels.
- Defined the averaged one-step transition probability
  \(K_t(A,B)=P(m(t+\Delta t)\in B\mid m(t)\in A)\).
- Added depth advantage, positive return association, and a product-overlap
  threshold as checkable sufficient conditions for a compound basin to remain
  self-reinforcing.
- Proved that if
  \(K_t(\bar R,R_1\cap R_2)\geq K_t(\bar R,R_1)K_t(\bar R,R_2)\) and the
  product dominates exterior return to \(\bar R\), then \(\bar R\) is
  self-reinforcing.
- Added an iterated closure corollary and a monotone / MTP2 sufficient form via
  the FKG positive-correlation inequality.
- Updated `OPEN_PROBLEMS.md`, `STATUS.md`, `paper/acp_main_v10.md`,
  `audits/proof_debt_v11.md`, and `proofs/coherent_steering_derivation.md` so
  OP-17 is recorded as partial, not generically resolved.

## Technical result

The old generic branch needed the inclusion-exclusion threshold

$$
K_t(\bar R,R_1)+K_t(\bar R,R_2)-1
>
K_t(M\setminus\bar R,\bar R).
$$

The new positive-association branch uses the product lower bound

$$
K_t(\bar R,R_1\cap R_2)
\geq
K_t(\bar R,R_1)K_t(\bar R,R_2),
$$

so compound self-reinforcement follows whenever

$$
K_t(\bar R,R_1)K_t(\bar R,R_2)
>
K_t(M\setminus\bar R,\bar R).
$$

This captures order-aligned systems where return to one active basin makes
return to another active basin more likely rather than less likely. Monotone /
MTP2 kernels give a checkable sufficient form because increasing basin events
are positively associated and deeper compounds stochastically dominate
individual basins.

## What remains open

OP-17 is not closed in full. The remaining classification problem is sharper:

- Which ACP systems generate aligned positive association internally?
- Which domains require alignment as a separate hypothesis?
- Which systems fail intersection closure because active basins are
  antagonistic, non-comparable, or weakly overlapping?
- Can the exterior-leakage product threshold be estimated from observable
  return probabilities in Boolean-network, ecological, or control-theory
  examples?

## Generativity ledger

- Closed / strengthened (`C_closed`): OP-17 now has a first non-Gaussian
  model-class theorem rather than only a conditional closure lemma.
- New questions (`Q_new`): classify internally generated alignment, domain-level
  alignment assumptions, and closure-failure regimes; determine whether
  product-overlap thresholds can be estimated in target domains.
- New observables or bridge variables (`O_new`): depth-advantage margin,
  positive-return-association gap, exterior-leakage probability,
  product-overlap margin.
- New tests, falsifiers, or simulations (`P_new`): simulate aligned vs
  antagonistic basin families in Boolean-network or monotone birth-death
  systems; failure of the product-overlap margin falsifies this closure route
  for a target model.
- Workflow check: `G_session = (4 + 4 + 1) / max(1, 1) = 9`.
- Boundary assessment: progress is proof-shaped but remains productive rather
  than closed, because the theorem exposes a classification problem and
  measurable margins instead of claiming generic intersection closure.
