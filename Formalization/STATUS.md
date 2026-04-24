# STATUS

**Last updated:** 2026-04-24
**Active paper:** `paper/acp_main_v10.md` (internal masthead: "WORKING DRAFT — v0.9")
**Active special-cases catalog:** `special_cases/acp_special_cases_v03.md`
**Active integrity audit:** `audits/integrity_audit_v10.md`

---

## Where the paper stands

v10 includes, relative to what `memory.md` (legacy) describes as the v09 state:

- **A.20 Restraint-Power Theorem** + **Heisenberg uncertainty principle as the quantum-scale instantiation** of the coordination floor for a two-MASA operator-algebra partition, with the coordination-conservation premise now stated explicitly on kernel-preserving mechanism-preserving transformations.
- **A.21 meta-theoretic coherence** is now integrated into the main paper at the abstract / introduction / limitations / discussion / appendix-summary level: ACP self-application is stated as a generativity requirement rather than a total-closure claim.
- The Price / Fisher reduction (A.19) is fully integrated.
- Ten testable predictions are stated with experimental protocols and falsification criteria (Section 6 + Appendix A.16).
- A partial quantitative lower-bound program for the drift rate in non-Gaussian systems (A.17): the maximal-correlation route is the strongest current generic template, while the sharper copula/cumulant routes remain partly conditional.
- Bibliography policy is now explicit: `paper/acp_main_v10.md` carries a shared references list for the main paper plus the externally stored appendix documents cited throughout it.
- A second-pass research-positioning synthesis now distinguishes formal reductions already proved in-repo from merely adjacent structural neighbors, especially for the CDT and the restraint-power / visibility package.
- Prediction 10 is now framed as the decisive shared drift-template test across the currently operationalized reduced domains, rather than as a blanket universality forecast.

Best current reading of the overall claim: (i) the productive-interval geometry is theorem-level in six explicit reductions; (ii) the CDT's core entropy-drift theorem is the principal new result, with the stronger load / basin / asymptotic package still dependent on the maintenance and generic-closure problems tracked in `OPEN_PROBLEMS.md`; (iii) restraint-power plus vulnerable-margin are currently supported by a disciplined structural-neighbor map and empirical program, not yet by the same kind of completed cross-domain reduction stack; and (iv) the theory now explicitly predicts its own need to remain generative rather than closed, with the downstream semantic-field extension still open.

The full result inventory, as of v10 plus current appendices and bridge drafts:

| # | Result | Where |
|---|---|---|
| 1–5 | Core proof chain (ACP statement, CDT core entropy theorem, compounding lemma, Claim A.3 interventional, induction to k mechanisms with Gaussian-strongest / generic-conditional split) | `paper/` + `proofs/` |
| 6–10 | A.11–A.15: five reductions (Friston, Zurek, Bergstrom–Lachmann, Prigogine, Kauffman) | `reductions/` |
| 11 | A.16 empirical predictions (10 predictions, 3 novel from unification, now with operational tier definitions and first-pass Tier-1 simulation scope for Predictions 8 and 9) | `bridges/empirical_predictions.md` |
| 12 | A.17 non-Gaussian quantitative program (strongest current generic route via maximal correlation / reinforcement strength; sharper Gaussian-copula and cumulant routes still partly conditional) | `bridges/non_gaussian_bounds.md` |
| 13 | A.18 multiscale RG (C/D asymmetry, productive interval as RG-invariant subset) | `reductions/multiscale_rg.md` |
| 14 | A.19 Price / Fisher (selection = crystallization drift under the selection-entropy bridge; Fisher's theorem = CDT applied to the fixed fitness-space coordinate) | `reductions/price_equation.md` |
| 15 | A.20 Restraint-Power + Coordination Conservation under kernel-preserving transformations; Heisenberg as special case | `bridges/restraint_power.md` + `bridges/syndrome_coordination.md` + `bridges/coordination_neutrality.md` |
| 16 | Schur complement bridge — four identifications unifying thermodynamic (ACP) and algebraic (Schur) registers; Heisenberg connection now reconciled with A.20 so the residual open piece is the stronger CCR / operator-algebra derivation | `bridges/schur_complement.md` |
| 17 | A.21 meta-theoretic coherence — generativity as the anti-crystallization condition for theory evolution; quartet inquiry floor; ACP self-application, now integrated into the main paper's claim architecture | `paper/acp_main_v10.md` + `proofs/meta_theoretic_coherence_theorem.md` |
| 18 | Valuation / arithmetic bridge — ratio operator on $\mathbb{Q}_{>0}^{\times}$ lifts exactly to the prime-valuation lattice, giving an additive arithmetic shadow of coordination-neutrality | `bridges/valuation_cocycle_bridge.md` |
| 19 | Unique-factorization rigidity for arithmetic shadows — on free arithmetic state spaces, any additive shadow whose one-variable coordinate respects orthogonal-support additivity and prime-ray additivity is forced to be valuation-type | `bridges/valuation_cocycle_bridge.md` |
| 20 | Bridge-family exclusion in the arithmetic regime — the exp-log coordination-neutral bridge family is not ratio-class constant on the rational regular domain and therefore cannot admit a factor-respecting arithmetic shadow | `bridges/valuation_cocycle_bridge.md` |
| 21 | Canonical defect decomposition for arithmetic shadows — every additive shadow on a free arithmetic state space splits exactly into a weighted-valuation baseline plus a defect coboundary built from prime-ray distortion and cross-prime mixing | `bridges/valuation_cocycle_bridge.md` |
| 22 | Partition-generating functors — A.20 typing for no-partition systems; symmetry obstruction to universal canonical partitions; first conditional spectral selector construction | `bridges/partition_generating_functors.md` |

## Active fronts

**1. Prediction 9 aligned confirmation after helper-default fix.** A methodological issue surfaced in the calibration tooling: `simulations/prediction9_calibration_sweep.py` had drifted away from the direct simulator's defaults (`settle_steps`, `attractor_steps`, `derrida_samples`, `max_generations`, `post_optimal_generations`), so helper-driven rankings and direct runs were not fully comparable. The defaults are now unified and both tools write explicit config snapshots. Under the aligned settings, the lead candidate `(fitness_threshold = 0.85, population_size = 28, stability_weight = 0.2)` remains positive but modest: the aligned eight-replicate rerun gave slope gap `~0.00337` and positive-fraction gap `~0.61`, while a larger aligned sixteen-replicate direct rerun reduced that to slope gap `~0.00149` and positive-fraction gap `~0.36`. The previously tracked backup `(0.85, 24, 0.4)` is now effectively flat / slightly negative in the aligned check (`slope gap ~-2.7e-4`). The next step is therefore not a broader grid search but one more larger aligned confirmation run on `(0.85, 28, 0.2)`, followed by proxy refinement if the effect keeps shrinking with sample size. *(Priority: medium — still the fastest route to concrete empirical traction, now on firmer methodological footing.)*

**2. Prediction 8 reduced simulator + calibration.** The first reduced Tier-1 simulator now exists at `simulations/prediction8_dissipative_modes.py`. It implements the scoped same-codebase comparison between a `reinforced` regime and a `no_reinforcement` null, uses a slow reinforcement field plus fast mode competition, and reads out both probe-based accessible mode count $N_\epsilon(t)$ and perturbation threshold estimate $\epsilon^*(t)$. The current paired-seed smoke settings produce the intended directional contrast: the reinforced regime contracts from mean accessible-mode count `5.0` to `1.0` with mean slope `~-0.23`, while the null stays flat at `5.0` with mean slope `0.0`; the reinforced $\epsilon^*(t)$ slope is also positive while the null is essentially stationary. The next step is a broader calibration sweep over kick magnitudes, drive asymmetry, and reinforcement strength to see how robust that contrast is away from the tuned pilot defaults. *(Priority: medium — now concrete and ready for parameter sweeps rather than design work.)*

**3. Journal selection.** Not yet decided. Candidates depend on whether we pitch the paper as (a) a thermodynamic first-principles paper (PRE, J. Stat. Phys.), (b) a unification across disciplines (Physics Reports, Reviews of Modern Physics), or (c) an information-theoretic paper (IEEE TIT, Entropy). This is a strategic call I should make once the v10 audit is clean, the bibliography policy is explicit, and the Tier-1 pilot runs are in hand. *(Priority: medium.)*

**4. Heisenberg / A.20 consequences.** If A.20 genuinely recovers Heisenberg as a special case of the coordination floor, there is a large downstream program: are there other canonical commutation relations recoverable? Is A.20 compatible with the Robertson bound's tightness conditions? Does it extend to infinite-dimensional MASAs? *(Priority: exploratory; open problem territory.)*

**5. Meta-theoretic coherence / A.21 integration.** The core of the generativity program is formalized in `proofs/meta_theoretic_coherence_theorem.md` and is now integrated into `paper/acp_main_v10.md`: the theory-evolution state space, the $G_t(T) > 1$ anti-crystallization identity, the quartet inquiry floor, and the ACP self-application corollary are part of the manuscript's claim architecture. The cross-domain generativity protocol now operationalizes the next methodological step: unexpected domains can improve the theory when their incomplete mappings produce new observables, falsification paths, or sharply named gaps. The first historical blind-spot audit is now complete: it extracts the reusable signature that stable regularities can precede the carrier, partition, or transformation vocabulary that makes them explainable. `research/blind_spot_atlas_2026-04-24.md` generalizes this into a diagnostic map of hidden carriers, multiplicities, transformations, partitions, conservation laws, observables, falsifiers, scope boundaries, and normative filters. Its immediate consequence has now been cashed out in `bridges/partition_generating_functors.md`: no universal canonical A.20 partition can exist because primitive automorphism actions obstruct nontrivial invariant partitions, but stable selector data can generate partitions conditionally. The open frontier is no longer packaging but extension: quantitative generativity bounds (OP-12), downstream inquiry-space under theory dominance (OP-10), measure-theoretic meaning-space (OP-11), concrete protocol applications to candidate domains, and the classification of admissible partition-generating selectors (OP-19). *(Priority: medium — integrated at the self-consistency level; frontier work remains outside the proved core.)*

**6. Arithmetic / operator bridge.** The valuation bridge now has six layers of closure: the scalar smooth case collapses to ratio, the smooth finite-dimensional vector-valued case collapses with it, the free-arithmetic valuation-type discrete case collapses to weighted prime ledgers with the primitive case canonically equivalent to the usual valuation map, any additive shadow whose coordinate map respects unique factorization is forced into that same valuation-type class, the exp-log coordination-neutral bridge family is excluded from that factor-respecting arithmetic subclass, and every additive shadow now splits exactly into a valuation baseline plus an explicit defect coboundary measuring prime-ray distortion and cross-prime mixing. The remaining frontier is therefore sharper still: can that defect term ever be nonzero in a genuine coordination-neutral arithmetic shadow without collapsing back to the valuation class, or does the canonical valuation picture exhaust the abelian arithmetic regime entirely? *(Priority: exploratory, but now tightly localized.)*

## Open problems

Canonical tracker: `OPEN_PROBLEMS.md`. Headline items:

- **OP-1: Quantitative erosion constant** (named "OP-new-2" in legacy memory). Channel Erosion (A.10) gives the rate is positive, and A.17 now supplies a computable lower-bound route, but we still do not have a sharp numerical characterization in general.
- **OP-2: Coherence crisis transient dynamics.** What happens *during* the regime change when one mechanism erodes another?
- **OP-3 through OP-5: Schur complement bridge open problems.** Three listed at the bottom of `bridges/schur_complement.md`. The old Heisenberg reconciliation item (OP-6) is now closed: A.20 settles the structural uncertainty-floor question, and the stronger residual operator-algebra problem is tracked as OP-RP-5 in `bridges/restraint_power.md`.
- **OP-7: Coordination neutrality under tree composition.** Named in `bridges/coordination_neutrality.md`. The bridge family (exp / log operators — cf. Odrzywolek's eml in `references/`) is CN pairwise but may fail joint-inversion invariance under composition.
- **OP-15: Arithmetic shadows of coordination-neutral operators.** Now partial from `bridges/valuation_cocycle_bridge.md`: the entire smooth finite-dimensional real-target case collapses to ratio-up-to-reparameterization, and the free-arithmetic valuation-type discrete case collapses to weighted prime-valuation shadows. The open part is the genuinely non-valuation discrete/infinite-rank case.
- **OP-16: Maintenance lemma / net reinforcement pressure.** The core entropy form of the CDT is isolated, but the stronger load / basin / asymptotic package still needs the missing lemma upgrading Lemma 4.14's survivorship-selection enrichment to sustained reinforcement pressure or monotone load growth.
- **OP-17: Generic k-mechanism closure under intersection.** Appendix A.9 is now honest about its closure hypotheses; what remains is to derive those hypotheses generically rather than assume them outside the Gaussian branch.
- **OP-18: Mechanism-preserving vs kernel-preserving conservation.** Appendix A.20 now states the exact premise it uses. The residual question is whether the weaker physical notion of "mechanism-preserving" implies the kernel-preserving automorphism condition in useful generality.
- **OP-19: Partition-generating functors for A.20.** The first bridge proves a symmetry obstruction to universal canonical partitions and gives a conditional spectral selector construction; what remains is to classify admissible selectors and test invariance across selector families.

## Changelog

### 2026-04-24 — partition-generating functors
- Added `bridges/partition_generating_functors.md`, a candidate bridge that makes the WI-E.3 no-partition problem mathematically sharp.
- Defined A.20-untyped systems and partition-generating functors $\Pi : \mathsf{C} \to \mathsf{Part}$ with typing, equivariance, A.20-admissibility, and nontriviality requirements.
- Proved a symmetry obstruction: finite systems with primitive automorphism action admit no nontrivial invariant partition, so no universal canonical A.20 partition selector can exist.
- Proved a first conditional construction: a self-adjoint selector with a simple isolated eigenvalue generates an equivariant spectral partition when the eigenvector has nonzero separated coordinates of both signs.
- Added `simulations/partition_selector_toy.py`, a dependency-free smoke checker showing that the spectral selector refuses the fully symmetric case and recovers the two-community partition under a Fiedler gap.
- Added OP-19 to track classification of admissible selectors, obstruction classes, and invariance across selector families.

### 2026-04-24 — historical blind-spot audit
- Added `research/historical_blind_spot_audit_2026-04-24.md`, the first application of the historical audit mode from the cross-domain generativity protocol.
- Audited three episodes: thermodynamics before statistical mechanics, heredity before DNA, and critical phenomena before renormalization.
- Extracted a reusable blind-spot signature: stable regularities can precede the carrier, partition, or transformation vocabulary that makes them explainable.
- Added `research/blind_spot_atlas_2026-04-24.md`, a reusable diagnostic map classifying hidden carriers, multiplicities, transformations, partitions, conservation laws, observables, falsifiers, scope boundaries, and normative filters.
- Sharpened WI-E.3 into the recommended next bridge target: partition-generating functors for systems that do not present a natural A.20 partition at the outset.
- Session log: `sessions/2026-04-24_historical_blind_spot_audit.md`.

### 2026-04-24 — cross-domain generativity protocol
- Added `bridges/cross_domain_generativity_protocol.md`, a methodological bridge for using unexpected domains as disciplined theory-improvement probes rather than loose analogies.
- Defined cross-domain intake objects, a generativity-gain score $G_X$, a promotion ladder from probe to theorem, and failure-set categories that turn incomplete mappings into research questions.
- Updated `bridges/generativity_criterion.md` with §4.1a connecting the protocol to A.21 self-application.
- Updated `WHAT_IF.md` with Section G, including failed reductions as sensors, cross-domain generativity gain as an intake score, and analogy friction as a possible selection principle.
- Added `research/cross_domain_intake_triage_2026-04-24.md`, applying the protocol to language, model collapse, and no-partition systems; the no-partition candidate is now the recommended next bridge target because it can sharpen the scope boundary between ACP/CDT and A.20.
- Session log: `sessions/2026-04-24_cross_domain_generativity_protocol.md`.

### 2026-04-24 — A.21 meta-theoretic integration
- Integrated the meta-theoretic coherence / generativity result into `paper/acp_main_v10.md` at the abstract, keywords, introduction roadmap, layered-claim paragraph, limitations, discussion, notation summary, references, and Appendix C proof-chain summary.
- Framed the project explicitly as a unifying theory that does not seek total closure: if ACP is correct and self-representing, it must remain generative by opening disciplined successor questions faster than it closes explanatory uncertainty.
- Preserved the honesty split: A.21's productive-step generativity identity and quartet inquiry floor are treated as the proved core, while the downstream semantic-field extension and quantitative generativity bound remain OP-10 through OP-12.
- Session log: `sessions/2026-04-24_meta_theoretic_integration.md`.

### 2026-04-22 — Prediction 9 helper/default alignment
- Found a methodological mismatch in the empirical tooling: `simulations/prediction9_calibration_sweep.py` had diverged from `simulations/prediction9_boolean_network.py` on several hidden simulation defaults, so helper-driven calibration results were not directly comparable to direct simulator runs.
- Centralized the canonical Prediction 9 defaults inside `simulations/prediction9_boolean_network.py` and made the sweep helper inherit them rather than maintaining a stale copy.
- Added explicit output-side provenance files: `simulation_config.json` for direct simulator runs and `sweep_parameters.json` for sweep runs.
- Verified the fix by rerunning the lead configuration through both entry points and confirming they now agree numerically on the same slope-gap summary.
- Ran one larger aligned direct confirmation at `16` replicates for `(0.85, 28, 0.2)`. The lead remained positive but attenuated, with mean slope gap `~0.00149` and positive-fraction gap `~0.36`, so the live question is now stability under further replication rather than helper/direct comparability.
- Session log: `sessions/2026-04-22_prediction9_alignment.md`.

### 2026-04-22 — tracker refresh after conversation review
- Reviewed the recent `sessions/` logs against `STATUS.md` and `memory.md` to make sure the continuity layer still matches the actual project conversations.
- Added the missing continuity note for the 2026-04-22 overall-claim rigor pass, including the narrower Prediction 10 framing.
- Refreshed `memory.md` with a brief live addendum while preserving the pre-migration legacy snapshot below for audit.
- Session log: `sessions/2026-04-22_tracker_refresh.md`.

### 2026-04-22 — overall-claim rigor pass
- Tightened `paper/acp_main_v10.md` so the top-level claim is now stated in three layers: six explicit productive-interval reductions, the CDT core entropy-drift theorem as the principal new theorem, and restraint-power / vulnerable-margin as the broader comparative and empirical program.
- Softened local overextensions in the Zurek and Bergstrom-Lachmann reductions so the "What the ACP adds" language no longer implies theorem-level reduction where the project currently has only disciplined structural adjacency.
- Recast Prediction 10 in `paper/acp_main_v10.md` and `bridges/empirical_predictions.md` as the decisive test of a shared normalized drift template across the currently operationalized reduced domains, rather than as a blanket universality forecast.
- Session log: `sessions/2026-04-22_overall_claim_rigor.md`.

### 2026-04-22 — Prediction 8 simulator scaffold
- Added `simulations/prediction8_dissipative_modes.py`, a pure-Python reduced dissipative-mode competition simulator for the Tier-1 Prediction 8 program.
- Implemented two same-codebase regimes: `reinforced` (slow pathway reinforcement active) and `no_reinforcement` (slow field frozen), with paired seeds so both branches start from the same settled pre-aging state.
- Implemented the appendix's intended observables directly: probe-based accessible mode count `N_epsilon(t)` from a fixed kick library, plus a lower-bound estimate of the perturbation threshold `epsilon*(t)`.
- Updated `simulations/README.md` to document the new simulator and its output files.
- Verified the code path with `python3 -m py_compile` and a four-replicate smoke pilot. Under the current defaults, the reinforced regime shows declining `N_epsilon(t)` and rising `epsilon*(t)`, while the null remains effectively stationary.
- Session log: `sessions/2026-04-22_prediction8_simulator.md`.

### 2026-04-22 — cathedral map / restraint framing
- Added `sessions/2026-04-22_cathedral_of_restraint.md` to capture the project's current architectural reading: ACP as foundation, restraint as cornerstone, restraint-power / vulnerable-margin as the power geometry, and generativity as the theory-level self-application.
- Recorded the sharper philosophical-program claim that the ethical implications are not merely downstream commentary: in asymmetric systems, restraint becomes load-bearing wherever persistence depends on keeping the productive interval open.
- Clarified the current honesty line for this framing: parts of it are already formal in A.20 and A.21, while the downstream semantic-field extension, vulnerable-margin closure, and the full maintenance lemma remain open.
- Session log: `sessions/2026-04-22_cathedral_of_restraint.md`.

### 2026-04-22 — research synthesis integrated into theorem positioning
- Used `reductions/restraint_power_literature_scan.md` to recast the CDT and restraint-power writeups in terms of structural-neighbor clusters rather than implying a single pre-existing analog theorem.
- Tightened `proofs/crystallization_drift_theorem.md` and `paper/acp_main_v10.md` so the CDT now distinguishes formal reductions already carried by the project (notably Kauffman and Friston) from adjacent external literatures that capture only part of the theorem.
- Tightened `bridges/restraint_power.md` so the appendix now says explicitly that the "strongest goes first" clause and the "visibility / decodability" clause are best supported by different adjacent literatures, and that A.20's distinctiveness is their conjunction under a coordination-floor argument.
- Session log: `sessions/2026-04-22_research_synthesis_integration.md`.

### 2026-04-21 — reviewer-driven rigor remediation
- Recast `paper/acp_main_v10.md` so the CDT is presented in two layers: a closed core entropy-drift theorem plus stronger conditional repertoire-geometry consequences.
- Tightened `proofs/induction_step_k_mechanisms.md` by making the generic intersection-closure hypotheses explicit and downgrading the appendix from "resolved" to "Gaussian-closed / generic-conditional."
- Tightened `bridges/restraint_power.md` so coordination conservation is stated only for kernel-preserving mechanism-preserving transformations, matching the proof actually given.
- Reframed `bridges/non_gaussian_bounds.md` as a partial quantitative program rather than a fully resolved non-Gaussian rate theorem.
- Added new canonical open problems OP-16 through OP-18 to track the newly isolated proof obligations.
- Session log: `sessions/2026-04-21_review_rigor_remediation.md`.

### 2026-04-20 — valuation cocycle bridge / arithmetic entry
- New bridge: `bridges/valuation_cocycle_bridge.md` — opens the number-theoretic entry to the operator program by treating the ratio operator on $\mathbb{Q}_{>0}^{\times}$ as a coordination-neutral baseline with an exact lift to the prime-valuation lattice $\bigoplus_p \mathbb{Z}$.
- Proved in the bridge note: the valuation map is the arithmetic log-lift of the ratio operator, the lift is a swap-antisymmetric additive cocycle, and ratio-tree compositions linearize exactly as signed sums in valuation space.
- Added OP-15 to `OPEN_PROBLEMS.md`: characterize the wider class of coordination-neutral operators admitting an arithmetic shadow $\eta(B(x,y)) = \psi(x) - \psi(y)$.
- This creates a genuine arithmetic/operator front without yet overclaiming an ACP reduction theorem for number theory.

### 2026-04-20 — arithmetic-shadow rigidity
- Extended `bridges/valuation_cocycle_bridge.md` with a partial solution to OP-15: a mixed-derivative criterion (Theorem 6.2) classifying one-dimensional smooth real-coordinate arithmetic shadows.
- Derived the rigidity corollary that every such operator is ratio-like up to input/output reparameterization.
- Updated OP-15 from fully open to partial: what remains is the genuinely higher-rank / non-real-target abelian-group case.

### 2026-04-20 — finite-dimensional shadow collapse
- Extended `bridges/valuation_cocycle_bridge.md` again: Theorem 7.2 shows that every smooth finite-dimensional real-vector-valued arithmetic shadow has image in an affine line, so no genuinely higher-rank smooth real shadows exist.
- Corollary 7.3 reduces the finite-dimensional vector-valued case to the same scalar ratio normal form as before.
- This sharpens OP-15 substantially: the surviving frontier is no longer "higher-rank real targets" but the genuinely arithmetic regime of discrete or infinite-rank abelian groups.

### 2026-04-20 — abelian-shadow linearization
- Added Theorem 8.1 to `bridges/valuation_cocycle_bridge.md`: any additive shadow into an abelian group linearizes arbitrary binary tree compositions as a signed sum of leaf coordinates in the target group.
- This shows the ratio / valuation tree formulas are not ad hoc but the canonical special case of a general abelian-shadow combinatorics.
- Conceptually, it isolates the exact algebraic meaning of "zero-synergy coordination": if an additive shadow exists, tree composition cannot generate new interaction terms inside that shadow.

### 2026-04-20 — discrete valuation-type classification
- Extended `bridges/valuation_cocycle_bridge.md` with a number-theoretic formulation of the discrete frontier using free arithmetic state spaces $M(P)$ and $K(P)$.
- Proved Theorem 9.3: every valuation-type shadow on a free arithmetic state space is a weighted valuation-difference shadow.
- Proved Corollary 9.5: the primitive case is canonically equivalent to the usual prime-valuation shadow up to target-group isomorphism.
- This narrows OP-15 again: the remaining question is no longer the whole discrete/infinite-rank regime, but whether any genuinely non-valuation additive shadows survive there.

### 2026-04-20 — factor-respecting shadow rigidity
- Extended `bridges/valuation_cocycle_bridge.md` once more with Theorem 9.9: any additive shadow on a free arithmetic state space whose one-variable coordinate respects orthogonal-support additivity and prime-ray additivity is automatically valuation-type.
- Added Corollary 9.10: every genuinely non-valuation shadow must therefore break unique-factorization separability by mixing distinct prime sectors or distorting a prime ray.
- This sharpens OP-15 from "find any non-valuation additive shadow" to the more specific obstruction question: can such a shadow exist without violating the arithmetic structures number theorists would regard as natural?

### 2026-04-20 — bridge-family arithmetic exclusion
- Extended `bridges/valuation_cocycle_bridge.md` again with Proposition 9.12 / Corollary 9.13: valuation-type, hence factor-respecting, arithmetic shadows are ratio-class constant on the arithmetic domain.
- Applied that criterion to the exp-log coordination-neutral bridge family in Proposition 9.14, showing that its rational regular-domain restriction is not ratio-class constant and therefore cannot admit a factor-respecting arithmetic shadow.
- This converts the new rigidity theorem from an abstract obstruction into a concrete exclusion: if the bridge family has any arithmetic shadow at all, it must already break unique-factorization separability.

### 2026-04-20 — canonical defect decomposition
- Extended `bridges/valuation_cocycle_bridge.md` with Definition 9.16 / Theorem 9.17 / Corollary 9.18 / Proposition 9.19, giving a canonical decomposition of any additive arithmetic shadow into a weighted-valuation baseline plus a defect coboundary.
- The defect splits into two exact pieces: prime-ray distortion and cross-prime mixing.
- This reframes the residual OP-15 frontier in measurable terms: exotic shadows are no longer just "non-valuation" in the abstract; they are precisely shadows with nonzero defect term $\Delta_\psi$.




### 2026-04-20 — meta-theoretic coherence / A.21 draft
- New proof document: `proofs/meta_theoretic_coherence_theorem.md` — formalizes theory evolution as an ACP state space $(I_t, U_t)$ with dissolution and crystallization boundaries, proves that for productive research steps $G_t(T) > 1$ is exactly the condition that the trajectory move away from the crystallization boundary, proves a quartet-based inquiry floor for self-representing theories, and derives the ACP self-application corollary.
- Updated `bridges/generativity_criterion.md` so the proved core now points to the A.21 draft while leaving the downstream semantic-field program explicitly open.
- Resolved the methodological fork formerly tracked as OP-13 by choosing the single-theorem route: a unified A.21-style proof document rather than four disjoint reductions.
- Session log: `sessions/2026-04-20_meta_theoretic_coherence.md`.

### 2026-04-21 — Heisenberg reconciliation after A.20
- Reconciled `bridges/schur_complement.md` §6.4 with `bridges/restraint_power.md` A.20.27 / A.20.28.
- Closed OP-6 in `OPEN_PROBLEMS.md`: A.20 settles the structural question "where does the uncertainty floor live?" by identifying Heisenberg with the coordination floor on a two-MASA partition.
- Isolated the residual stronger question as the already-existing operator-algebra extension OP-RP-5: derive the commutator / CCR structure itself from the ACP persistence condition `rank(D) > 0`.
- Session log: `sessions/2026-04-21_heisenberg_reconciliation.md`.

### 2026-04-21 — bibliography policy resolved
- Made the references scope explicit in `paper/acp_main_v10.md`: the bibliography is shared across the main paper and the externally stored appendix documents cited by it.
- Closed OP-14 in `OPEN_PROBLEMS.md` by choosing the shared-bibliography policy rather than a brittle paper-only prune.
- This removes the last manuscript-state ambiguity surfaced by `audits/integrity_audit_v10.md`; remaining fronts are now substantive or strategic rather than packaging-ambiguous.
- Session log: `sessions/2026-04-21_bibliography_policy.md`.

### 2026-04-21 — Tier-1 computational scope resolved
- Operationalized the four empirical tiers in `bridges/empirical_predictions.md` by defining them through the cheapest decisive falsification path rather than informal difficulty labels.
- Closed OP-9 in `OPEN_PROBLEMS.md` by explicitly identifying Predictions 8 and 9 as the Tier-1 targets and specifying first-pass simulation pipelines for both.
- Recorded the key modeling distinction that Prediction 9 can be tested in a standard evolutionary Boolean-network simulator, whereas Prediction 8's Tier-1 computational object should be a reduced dissipative-mode model with slow reinforcement memory, not a bare fixed-coefficient Bénard solver.
- Session log: `sessions/2026-04-21_tier1_scope.md`.

### 2026-04-21 — Prediction 9 simulator scaffold
- Created `simulations/` as the workspace home for empirical prototypes and added `simulations/README.md`.
- Added `simulations/prediction9_boolean_network.py`, a pure-Python first-pass Tier-1 simulator for regulatory-network aging with three regimes: `selected`, `neutral_post_threshold`, and `mutation_only`.
- The script writes generation-level metrics plus replicate and aggregate summaries, including post-optimal slope estimates for the frozen component fraction when the target threshold is reached.
- Verified the code path with a smoke test and a low-threshold pilot run to confirm that the post-optimal branch and slope reporting execute end-to-end.
- Session log: `sessions/2026-04-21_prediction9_simulator.md`.

### 2026-04-21 — Prediction 9 calibration + score-ranking fix
- Ran the first calibration sweeps for `simulations/prediction9_boolean_network.py` and used them to compare threshold-reaching fractions and post-optimal `f(t)` slopes across selected and neutral-post-threshold regimes.
- Found and fixed an implementation bug in the simulator: network ranking was using `(correctness, stability)` and therefore ignoring the weighted `score`, which meant `--stability-weight` had no effect on selection.
- Tightened the ranking semantics further so `score` is primary and correctness is the only tie-breaker, preventing stability from leaking into the `stability_weight = 0.0` case.
- Post-fix pilot checks suggest that `fitness_threshold = 0.85`, `population_size = 24`, and `stability_weight = 0.3` are a reasonable provisional operating region, but the replicate-level sign split is still noisy enough that broader sweeps are the next step.
- Session log: `sessions/2026-04-21_prediction9_calibration.md`.

### 2026-04-21 — Prediction 9 sweep helper + targeted ranked grid
- Added `simulations/prediction9_calibration_sweep.py`, which runs small calibration grids for Prediction 9 and writes ranked configuration summaries instead of scattered one-off pilot outputs.
- Updated `simulations/README.md` to document the sweep helper and its output files.
- Ran the first helper-driven targeted grid over thresholds `0.82, 0.85`, population size `24`, and stability weights `0.2, 0.3`.
- The best tested configuration in that grid was `threshold = 0.82`, `population = 24`, `weight = 0.2`, but its slope gap was only barely positive (`~5.6e-4`), so no robust operating region has been established yet.
- Session log: `sessions/2026-04-21_prediction9_sweep_helper.md`.

### 2026-04-21 — Prediction 9 broader ranked sweep
- Let the larger helper-driven post-fix grid complete over thresholds `0.82, 0.85, 0.88`, population sizes `24, 28`, and stability weights `0.2, 0.3, 0.4`.
- The strongest tested candidate was `(0.85, 28, 0.4)`, with selected mean post-optimal slope `~0.0552`, neutral mean post-optimal slope `~-0.0025`, and slope gap `~0.0577`.
- The next-best candidate was `(0.85, 24, 0.2)`, with slope gap `~0.0553` and a small positive positive-fraction gap.
- This materially improves the calibration picture relative to the earlier targeted grid, but still calls for larger-replicate confirmation before treating either configuration as the new default.
- Session log: `sessions/2026-04-21_prediction9_ranked_sweep.md`.

### 2026-04-21 — Prediction 9 candidate confirmation
- Ran a larger-replicate follow-up sweep focused on the four `(threshold = 0.85)` candidates generated by the broader ranked grid: populations `24, 28` crossed with stability weights `0.2, 0.4`.
- The confirmed best setting in that follow-up was `(0.85, 28, 0.2)`, with slope gap `~0.0077` and positive-fraction gap `~0.30`.
- `(0.85, 24, 0.4)` remained weakly positive, but `(0.85, 24, 0.2)` and `(0.85, 28, 0.4)` both flipped negative, showing that the earlier four-replicate ranking was materially sample-sensitive.
- This narrows the live calibration frontier: the project no longer has "many plausible candidates," but one lead configuration plus one weaker backup.
- Session log: `sessions/2026-04-21_prediction9_candidate_confirm.md`.

### 2026-04-18 — generativity criterion + incompleteness quartet
- New essay: `essays/the_incompleteness_quartet.md` — argues Heisenberg, Gödel, Turing, Chaitin share a structural signature (sufficiently-powerful representational systems cannot close over themselves) that is exactly the ACP's crystallization boundary being unreachable.
- New bridge: `bridges/generativity_criterion.md` — formalizes a generativity ratio $G(T)$ for theories and conjectures that $G > 1$ is the ACP's nondegenerate-interval condition applied to the (theory, domain) pair. Implies the ACP is self-applying: a correct unifying theory must persistently open more questions than it closes.
- Four new open problems added: OP-10 (downstream inquiry-space under theory dominance), OP-11 (measure-theoretic meaning-space), OP-12 (quantitative form of generativity criterion), OP-13 (methodological fork on whether the quartet→ACP reduction should be one theorem or four parallel arguments in the main paper; now resolved by the A.21 draft).
- Session log: `sessions/2026-04-18_generativity_quartet.md`.

### 2026-04-20 — v10 integrity audit completed
- New audit: `audits/integrity_audit_v10.md` — re-audits the live paper against the old v07 findings and records the new state.
- Confirmed fixed from v07: Section 4 numbering gaps, introduction roadmap count, `T`/temperature overloading via `T_env`, and stale internal-tracking section-header language.
- Corrected three residual v10 manuscript issues in `paper/acp_main_v10.md`: `ε*(T)` → `ε*(T*)` in Section 6.7, retitled Section 7.7 to reflect that only residual multi-scale questions remain, and removed the stale `OP2` label from the Discussion.
- New medium-priority packaging issue surfaced: reconcile whether the paper bibliography is paper-only or shared with the appendix bundle.

### 2026-04-17 — workspace migration to Cowork
- Reorganized from flat `docs/` layout into topic-specific folders.
- Archived v01–v09 of the paper; promoted v10 as the single active paper at `paper/acp_main_v10.md`.
- Identified that `memory.md` is stale — asserts v09 is current, missed the v10 A.20 addition.
- Ported memory to Cowork system; legacy `memory.md` preserved for audit.
- Established this STATUS.md, `OPEN_PROBLEMS.md`, and `CLAUDE.md` as the living-document layer.
- Session log: `sessions/2026-04-17_setup.md`.

### (pre-migration sessions)
- Tracked in legacy `memory.md`. Summary: 14 sessions produced v01 → v10, integrating six reductions plus non-Gaussian bounds, multiscale RG, empirical predictions, Schur bridge, Restraint-Power / Heisenberg.
