# Session log — 2026-04-24: main paper mathematical review

## Goal

Read `paper/acp_main_v10.md` as a mathematician and tighten the places where the prose was leaning on an implicit bridge assumption.

## Main changes

- Changed the abstract's ACP statement from an overstrong "if and only if" phrasing to an "only inside the productive interval" statement, matching Theorem 4.3's proved direction.
- Added the finite-macrostate convention for the core formalism: continuous or countably infinite versions require a reference measure and finite resolution scale.
- Added a boundary-compatibility remark clarifying that high Boltzmann/Gibbs entropy and high conditional macrostate entropy are distinct, and that the theorem uses a bridge from the domain reduction to identify the dissolution coordinate.
- Tightened the CDT hypotheses from generic self-reinforcement to **entropy-contracting self-reinforcement**. A residence bias alone does not imply Shannon entropy contraction; the entropy-contracting condition is now explicit in Definition 4.7, Lemma 4.13, and Theorem 4.17.
- Corrected the Boltzmann constant notation in Definition 2.2 from a bad glyph to `k_B`.
- Corrected the prediction provenance sentence so Prediction 4 is attributed to A.20 rather than to the core ACP theorem.

## Mathematical status

The paper's strongest current layer remains intact:

- The productive-interval theorem is cleaner after the boundary-compatibility convention.
- The CDT core is now stated as a maintained-pressure theorem for entropy-contracting mechanisms, which is the mathematically defensible version.
- The maintenance lemma, generic k-mechanism closure, non-Gaussian quantitative refinements, and A.20 kernel-preservation premise remain the correct live proof debts.

The key lesson of this pass: the project should distinguish **stability bias** from **entropy contraction** everywhere. Stability bias is a dynamical tendency; entropy contraction is what feeds the CDT.

## Continuation — mathematician's-eye pass

- Tightened Lemma 4.14 in the main paper and CDT proof note: survivorship selection now gives a monotone self-reinforcing fraction only under explicit fixed-composition or ordered birth-death assumptions; otherwise it is an enrichment pressure, not a literal monotonicity theorem.
- Propagated that correction through the Theorem 4.17 proof, Appendix C proof-chain summary, OP-16, `STATUS.md`, and `audits/proof_debt_v11.md`.
- Softened the Price/Fisher reduction language so Fisher's theorem is treated as a crystallization-drift statement only after the selection-entropy bridge fixes the fitness/trait coordinate. Transmission, balancing selection, and changing environments are now explicitly preserved as variation-reopening qualifications.

Mathematical status after continuation: OP-16 is now sharper. The gap is no longer "fraction monotonicity does not imply load monotonicity"; it is "survivorship selection itself only becomes monotone fraction growth under a specified population dynamics, and even then it still does not imply load monotonicity."
