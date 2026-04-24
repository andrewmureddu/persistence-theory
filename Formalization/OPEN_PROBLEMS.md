# Open Problems

Canonical tracker for unsolved problems across the ACP program. Each entry has an ID, a short statement, status (open / partial / resolved), and pointers to the documents where it is discussed.

When a problem is resolved, do not delete it — move it to the "Resolved" section and record how and where it was closed. Open problems decay into stale reminders when their context disappears; keeping the resolution trail is cheap and useful.

---

## Open

### OP-1 — Quantitative erosion constant
**Statement.** Channel Erosion Theorem (Appendix A.10) establishes that anti-coherent mechanisms decay, with positive decay rate. A sharp general bound on the erosion constant as a function of the coupling strength and mechanism geometry has not been given.
**Status.** Partial — `bridges/non_gaussian_bounds.md` now supplies a computable lower-bound route via maximal correlation, but not a sharp characterization.
**Where discussed.** `proofs/coherent_steering_derivation.md` (the theorem itself); `bridges/non_gaussian_bounds.md` (partial quantitative work in the Gaussian / χ²-contraction regime).
**Why it matters.** Without a quantitative erosion rate, the self-grounding argument (Coherent Steering as necessary consequence rather than external assumption) remains qualitative. A quantitative version would let us predict timescales of coherence crises empirically.
**Adjacent to.** Prediction #9 (regulatory-network aging) in `bridges/empirical_predictions.md` — erosion timescale is the natural observable.

### OP-2 — Coherence crisis transient dynamics
**Statement.** What happens during the regime change when one mechanism erodes another? The steady-state endpoints are known (the loser is shed); the transient — possibly exhibiting oscillation, delayed collapse, or hysteresis — is not characterized.
**Status.** Open.
**Where discussed.** `proofs/coherent_steering_derivation.md`.
**Why it matters.** The transient dynamics are where empirical signatures live. A monotone-exponential prediction and an oscillatory prediction look different in data.

### OP-16 — Maintenance lemma / net reinforcement pressure
**Statement.** The paper now isolates a closed core entropy-drift theorem: if the active self-reinforcing repertoire exerts non-decreasing net entropy-reducing pressure, then conditional macrostate entropy contracts. The missing step has been narrowed: `proofs/maintenance_lemma.md` supplies a sufficient balance lemma showing that load grows when newly stabilized mechanisms compensate for losses, and that net pressure is maintained when incoming pressure, survivor strengthening, and coherent-excess change compensate for shed pressure. What remains is to derive that balance inequality from lower-level ACP dynamics in useful system classes, rather than stipulating it model by model.
**Status.** Partial.
**Where discussed.** `proofs/maintenance_lemma.md`; `paper/acp_main_v10.md` §4.4, §7; `proofs/crystallization_drift_theorem.md`; `audits/proof_debt_v11.md`.
**Why it matters.** This is still the sharpest remaining gap in the full four-part CDT package. The bookkeeping step is now explicit, but the load / basin / asymptotic claims remain conditional until the maintenance-balance inequality is derived in the target dynamics.

### OP-17 — Generic k-mechanism closure under intersection
**Statement.** Appendix A.9 now states explicitly what earlier drafts used implicitly: the generic k-mechanism induction needs an intersection-compatibility hypothesis for compound basins and a threshold ensuring the combined return channels dominate the exterior return probability to the intersection. Derive those hypotheses from the ACP / CDT setting rather than assuming them outside the Gaussian branch.
**Status.** Open.
**Where discussed.** `proofs/induction_step_k_mechanisms.md`; `audits/proof_debt_v11.md`.
**Why it matters.** The Gaussian induction is clean, but the generic induction is only as strong as the closure lemma carrying the compound basin forward. Closing this would remove the most serious remaining overreach in the k > 2 story.

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

### OP-7 — Coordination neutrality under tree composition
**Statement.** Two-argument coordination-neutral operators B(x,y) satisfy B(y,x) = 1/B(x,y). Log-lift L(x,y) = log|B(x,y)| is swap-antisymmetric. The bridge family (exp–log operators, e.g. Odrzywolek's eml(x,y) = exp(x) − ln(y)) is CN pairwise. Under tree composition required for multi-party coordination, this family fails joint-inversion invariance, which is the preservation condition. **Characterize which operator families preserve CN under composition.**
**Status.** Open.
**Where discussed.** `bridges/coordination_neutrality.md`; external reference `references/odrzywolek_2026_eml_operator.pdf`.
**Why it matters.** Without a CN-preserving composition, multi-party coordination cannot be built purely from pairwise primitives — has consequences for how A.20's subsystem-partition argument scales beyond binary partitions.

### OP-18 — Mechanism-preserving vs kernel-preserving conservation
**Statement.** Appendix A.20 now states coordination conservation for kernel-preserving mechanism-preserving transformations, i.e. transformations that explicitly commute with the transition kernel. The residual question is whether the weaker physical idea of "mechanism-preserving" (no recruitment, no shedding, no coherence crisis, no large external perturbation) implies this kernel-preserving automorphism condition in useful generality.
**Status.** Open.
**Where discussed.** `bridges/restraint_power.md`; `paper/acp_main_v10.md` §8.
**Why it matters.** This is the exact premise-sharpening step that prevents the coordination-conservation theorem from becoming circular. Either it should be proved, or the kernel-preserving form should remain the permanent theorem statement.

### OP-19 — Partition-generating functors for A.20
**Statement.** Characterize classes of ACP systems for which there exists an admissible partition-generating functor $\Pi : \mathsf{C} \to \mathsf{Part}$ that is equivariant under system isomorphisms, stable under perturbations, and sufficient to type A.20's coordination-capacity decomposition. The first candidate bridge proves a symmetry obstruction: primitive automorphism actions admit no nontrivial invariant partition, so no universal canonical $\Pi$ can exist. It also gives a conditional spectral construction when a stable selector datum has a simple isolated eigenvalue.
**Status.** Open / partial. The obstruction and first conditional construction are written in `bridges/partition_generating_functors.md`; classification of admissible selectors and invariance across selector families remains open.
**Where discussed.** `bridges/partition_generating_functors.md`; `research/blind_spot_atlas_2026-04-24.md`; WI-E.3 in `WHAT_IF.md`.
**Why it matters.** A.20 assumes a subsystem or MASA-like partition. Some systems may satisfy ACP/CDT while lacking a primitive partition, especially critical, scale-free, or all-to-all systems. This problem decides whether A.20 can be typed by generated partitions in such systems, or whether no-partition systems are a genuine scope boundary.
**Adjacent to.** OP-3 (Schur regularity), OP-18 (kernel-preserving conservation), OP-RP-8 in `bridges/restraint_power.md` (partition invariance), A.18 multiscale RG.

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

### OP-6 — Heisenberg derivation: reconciliation with A.20
**Resolved:** 2026-04-21.
**Resolution summary.** Resolved by splitting the old single question into two layers in `bridges/schur_complement.md` §6.4. Appendix A.20 closes the structural Heisenberg question: once a two-MASA partition with commutator `[A,B] = i\kappa I` is given, the restraint-power coordination floor coincides with the Robertson bound, so Heisenberg is indeed the quantum-scale coordination floor. What remains open is the stronger ACP-internal derivation of the commutator / CCR structure itself from the persistence condition `rank(D) > 0`, and that residual problem is already tracked more precisely as OP-RP-5 in `bridges/restraint_power.md`.
**Closed in.** `bridges/schur_complement.md`; `bridges/restraint_power.md`; session log `sessions/2026-04-21_heisenberg_reconciliation.md`.

### OP-14 — Bibliography packaging policy for the main paper
**Resolved:** 2026-04-21.
**Resolution summary.** Resolved by choosing policy (b): `paper/acp_main_v10.md` now explicitly states that its references section is a shared bibliography for the main paper plus the externally stored appendix documents cited throughout the manuscript. This matches the paper's current architecture, where the body repeatedly cites appendices A.8-A.20 that are maintained outside the file. The bibliography was therefore reconciled by clarifying scope rather than mechanically pruning entries to a paper-only list.
**Closed in.** `paper/acp_main_v10.md`; `STATUS.md`; session log `sessions/2026-04-21_bibliography_policy.md`.

### OP-9 — Tier-1 computational tests for Predictions 8 and 9
**Resolved:** 2026-04-21.
**Resolution summary.** Resolved by operationalizing the tier system directly inside `bridges/empirical_predictions.md` §A.16.11, explicitly identifying Prediction 8 as Dissipative Aging and Prediction 9 as Regulatory Network Aging, and specifying a first-pass simulation pipeline for each. The resolution also records an important modeling distinction: Prediction 9 can be tested in a standard evolutionary Boolean-network simulator, while Prediction 8's minimal Tier-1 test should be an ACP-informed reduced mode-competition model with slow reinforcement memory rather than a bare fixed-coefficient Bénard solver.
**Closed in.** `bridges/empirical_predictions.md`; session log `sessions/2026-04-21_tier1_scope.md`.
