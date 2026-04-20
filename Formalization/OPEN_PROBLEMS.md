# Open Problems

Canonical tracker for unsolved problems across the ACP program. Each entry has an ID, a short statement, status (open / partial / resolved), and pointers to the documents where it is discussed.

When a problem is resolved, do not delete it — move it to the "Resolved" section and record how and where it was closed. Open problems decay into stale reminders when their context disappears; keeping the resolution trail is cheap and useful.

---

## Open

### OP-1 — Quantitative erosion constant
**Statement.** Channel Erosion Theorem (Appendix A.10) establishes that anti-coherent mechanisms decay, with positive decay rate. A sharp general bound on the erosion constant as a function of the coupling strength and mechanism geometry has not been given.
**Status.** Open.
**Where discussed.** `proofs/coherent_steering_derivation.md` (the theorem itself); `bridges/non_gaussian_bounds.md` (partial quantitative work in the Gaussian / χ²-contraction regime).
**Why it matters.** Without a quantitative erosion rate, the self-grounding argument (Coherent Steering as necessary consequence rather than external assumption) remains qualitative. A quantitative version would let us predict timescales of coherence crises empirically.
**Adjacent to.** Prediction #8 (regulatory-network aging) in `bridges/empirical_predictions.md` — erosion timescale is the natural observable.

### OP-2 — Coherence crisis transient dynamics
**Statement.** What happens during the regime change when one mechanism erodes another? The steady-state endpoints are known (the loser is shed); the transient — possibly exhibiting oscillation, delayed collapse, or hysteresis — is not characterized.
**Status.** Open.
**Where discussed.** `proofs/coherent_steering_derivation.md`.
**Why it matters.** The transient dynamics are where empirical signatures live. A monotone-exponential prediction and an oscillatory prediction look different in data.

### OP-3 — Schur bridge: precision-matrix regularity conditions
**Statement.** The four identifications in `bridges/schur_complement.md` (productive interval ↔ well-conditioned internal block; crystallization ↔ rank-deficient D; etc.) assume the partitioned precision matrix is well-defined and invertible on the internal block. State precisely the regularity conditions needed on the full system so that these identifications apply, particularly in infinite-dimensional / continuum cases.
**Status.** Open.
**Where discussed.** `bridges/schur_complement.md`.

### OP-4 — Schur bridge: rank-reduction dynamics
**Statement.** The identification *crystallization drift ↔ progressive rank reduction of D* is stated structurally. The rate at which rank is lost, and under what dynamical conditions this is monotone, is not derived.
**Status.** Open. May follow from the CDT applied to the partitioned system, but the derivation hasn't been written.
**Where discussed.** `bridges/schur_complement.md`.

### OP-5 — Schur bridge: anti-crystallization as rank restoration
**Statement.** *Anti-crystallization mechanisms ↔ operations that restore D's rank / condition number.* Characterize which operations in the mechanism algebra achieve this — i.e., produce a formal bijection or at least a structural correspondence between "noise injection," "environmental perturbation," and "regularization" on one side, and rank-restoring operations on the Schur side.
**Status.** Open.
**Where discussed.** `bridges/schur_complement.md`.

### OP-6 — Heisenberg derivation: reconciliation with A.20
**Statement.** The schur bridge posed the Heisenberg derivation as an open problem. A.20 (Restraint-Power, in `bridges/restraint_power.md`) now delivers Heisenberg as the quantum-scale instantiation of the coordination floor for a two-MASA operator-algebra partition. Reconcile the two: does A.20 close the schur-bridge's Heisenberg problem entirely, or do they answer slightly different questions?
**Status.** Partial — needs reconciliation pass.
**Where discussed.** `bridges/schur_complement.md` (question); `bridges/restraint_power.md` (A.20 result).
**Action.** Next pass: write a short reconciliation note. If A.20 closes it fully, move this problem to Resolved.

### OP-7 — Coordination neutrality under tree composition
**Statement.** Two-argument coordination-neutral operators B(x,y) satisfy B(y,x) = 1/B(x,y). Log-lift L(x,y) = log|B(x,y)| is swap-antisymmetric. The bridge family (exp–log operators, e.g. Odrzywolek's eml(x,y) = exp(x) − ln(y)) is CN pairwise. Under tree composition required for multi-party coordination, this family fails joint-inversion invariance, which is the preservation condition. **Characterize which operator families preserve CN under composition.**
**Status.** Open.
**Where discussed.** `bridges/coordination_neutrality.md`; external reference `references/odrzywolek_2026_eml_operator.pdf`.
**Why it matters.** Without a CN-preserving composition, multi-party coordination cannot be built purely from pairwise primitives — has consequences for how A.20's subsystem-partition argument scales beyond binary partitions.

### OP-9 — Tier-1 computational tests for Predictions 8 and 9
**Statement.** Legacy memory names "Tier-1 computational tests for Predictions 8 and 9" as on-the-horizon work. Scope this: (a) which predictions in `bridges/empirical_predictions.md` are numbered 8 and 9 in v10, (b) define the tier system formally (Tier-1 vs 2 vs 3), (c) propose the minimal simulation pipeline for each.
**Status.** Open.
**Where discussed.** `bridges/empirical_predictions.md`; legacy `memory.md`.

### OP-10 — Downstream inquiry-space bound under theory dominance
**Statement.** (Conjecture 4.2 of `bridges/generativity_criterion.md`.) For a dominant theory $T$ with compressive ratio $\rho$ on domain $D$, the collective semantic field $S$ of downstream researchers has an effective inquiry-space $I_t(S) \leq f(\rho) \cdot I_t(T)$ for some decreasing $f$. As $\rho \to 1$, $I_t(S)$ can approach zero even while $I_t(T)$ remains positive (the latter being guaranteed by the incompleteness quartet applied to $T$). The ACP protects $T$'s internal openness; it does not automatically protect the openness of researchers who think *through* $T$.
**Status.** Open. Structurally motivated; no proof.
**Where discussed.** `bridges/generativity_criterion.md` §4.2; `proofs/meta_theoretic_coherence_theorem.md` §A.21.6; companion essay `essays/the_incompleteness_quartet.md`.
**Why it matters.** This is the formal basis of the restraint obligation on dominant theories. If provable, restraint becomes a structural necessity rather than a normative preference. Likely needs a generalization of A.20's MASA partition to a "compressive partition" between a theory and its downstream.

### OP-11 — Measure-theoretic meaning-space with ACP structure
**Statement.** (§4.3 of `bridges/generativity_criterion.md`.) Formalize a meaning-space measure $\mu$ given a set of observers $\{O_i\}$ with conditional distributions $p_i$ over world-states. Show that a dominant frame $T$ acts as a coarsening $\kappa_T$ on each $p_i$; that *semantic crystallization* is the fixed point where all $\kappa_T \circ p_i$ agree and conditional entropy over interpretations is zero; that *semantic dissolution* is the opposite extreme. Show the nondegenerate interval between the two satisfies the CDT in this register.
**Status.** Open — setup sketched only.
**Where discussed.** `bridges/generativity_criterion.md` §4.3; `proofs/meta_theoretic_coherence_theorem.md` §A.21.6.
**Why it matters.** If this goes through, the ACP extends from physical/dynamical systems to the collective semantic field of a scientific or intellectual community. Would also supply a formal target for OP-10.

### OP-12 — Quantitative form of the generativity criterion
**Statement.** The generativity ratio $G_t(T) > 1$ (see `bridges/generativity_criterion.md` §2) is currently stated as a threshold condition. Derive a sharp quantitative bound analogous to A.17's non-Gaussian drift-rate bounds: given a theory with specified representational capacity and domain complexity, what is the minimum achievable $G$? Is there a theory-analogue of the Gaussian conservative bound (slowest crystallization case) in A.17?
**Status.** Open.
**Where discussed.** `bridges/generativity_criterion.md` §5; `proofs/meta_theoretic_coherence_theorem.md` §A.21.6.
**Why it matters.** A quantitative generativity bound would let us distinguish healthy research programs from stalled ones empirically, and would make Corollary 4.1 (ACP's own generativity) falsifiable.

### OP-14 — Bibliography packaging policy for the main paper
**Statement.** `paper/acp_main_v10.md` appears to carry a bibliography broader than its own visible citations, likely because some references are used in the externally stored appendix documents. Decide whether the active paper should have (a) a paper-only bibliography, or (b) a shared bibliography for the paper-plus-appendix submission bundle, and reconcile the references accordingly.
**Status.** Open.
**Where discussed.** `audits/integrity_audit_v10.md`; `paper/acp_main_v10.md`.
**Why it matters.** This is a submission-packaging issue rather than a theory flaw, but unresolved bibliography policy creates avoidable reviewer/editor friction.

### OP-15 — Arithmetic shadows of coordination-neutral operators
**Statement.** Characterize the coordination-neutral operators $B : D \subseteq \mathbb{R}_{>0}^2 \to \mathbb{R}_{>0}$ for which there exist an abelian group $G$, an injective encoding $\eta : \operatorname{im}(B) \to G$, and a one-variable coordinate map $\psi$ such that $\eta(B(x,y)) = \psi(x) - \psi(y)$ on the regular domain. The ratio operator on $\mathbb{Q}_{>0}^{\times}$ realizes this with $G = \bigoplus_p \mathbb{Z}$ via prime valuations; determine whether this is an isolated case or the first member of a wider arithmetic class.
**Status.** Partial — the smooth real-target case is now largely closed in `bridges/valuation_cocycle_bridge.md`: the one-dimensional real-coordinate case is classified by Theorem 6.2 and Corollary 6.3, and Theorem 7.2 shows that every smooth finite-dimensional real-vector-valued shadow collapses to that scalar normal form. The discrete free-arithmetic valuation-type case is also classified there: Theorem 9.3 identifies every valuation-type shadow as a weighted valuation-difference shadow, and Corollary 9.5 shows the primitive case is canonically equivalent to the usual prime-valuation picture. Theorem 9.9 sharpens the obstruction further: any additive shadow on a free arithmetic state space whose one-variable coordinate respects orthogonal-support additivity and prime-ray additivity is automatically valuation-type. Proposition 9.14 then applies this to the exp-log bridge family, ruling out factor-respecting arithmetic shadows for its rational regular-domain restriction. Proposition 9.19 sharpens the residual frontier one step further by giving an exact decomposition of any additive arithmetic shadow into a weighted-valuation baseline plus a defect coboundary. The remaining open part is therefore narrower than "the whole discrete/infinite-rank regime": it is the search for genuinely non-valuation additive shadows with nonzero defect term, which must break unique-factorization separability, rely on singular encodings, or move to more exotic abelian targets.
**Where discussed.** `bridges/valuation_cocycle_bridge.md`; `bridges/coordination_neutrality.md`.
**Why it matters.** This is the cleanest current route from the operator program into number theory. If a nontrivial arithmetic-shadow class exists, it would supply an expert-legible discrete model of coordination-neutral composition and a baseline for measuring when genuine interaction information first appears. If none exists beyond the valuation class under natural arithmetic regularity, that itself is a strong rigidity signal: the first genuinely new compounding laws may have to appear exactly in the defect term, i.e. by breaking unique factorization at the coordinate level or leaving the abelian setting entirely.
**Adjacent to.** OP-7 (CN under tree composition); OP-RP-5 in `bridges/restraint_power.md` (operator-algebra extension).

---

## Resolved

### OP-13 — Quartet → ACP reduction: one theorem or four?
**Resolved:** 2026-04-20.
**Resolution summary.** Resolved methodologically by writing the unified A.21-style proof document `proofs/meta_theoretic_coherence_theorem.md`. The quartet now enters as a single inquiry-floor theorem with four richness registers bundled into one meta-theoretic coherence result, rather than as four separate standalone reductions.
**Closed in.** `proofs/meta_theoretic_coherence_theorem.md`; `bridges/generativity_criterion.md`; session log `sessions/2026-04-20_meta_theoretic_coherence.md`.

### OP-8 — Re-audit v10 against v07 audit findings
**Resolved:** 2026-04-20.
**Resolution summary.** Completed in `audits/integrity_audit_v10.md`. The old Section 4 numbering gaps are gone; the `T`/temperature clash is fixed via `T_env`; the remaining `ε*(T)` inconsistency in Section 6.7 was corrected to `ε*(T*)`; and the live manuscript now points to the new audit file rather than the stale v07 report.
**Closed in.** `audits/integrity_audit_v10.md`; `paper/acp_main_v10.md`; session log `sessions/2026-04-20_v10_integrity_audit.md`.
