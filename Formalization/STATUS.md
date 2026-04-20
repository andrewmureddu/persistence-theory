# STATUS

**Last updated:** 2026-04-20
**Active paper:** `paper/acp_main_v10.md` (internal masthead: "WORKING DRAFT — v0.9")
**Active special-cases catalog:** `special_cases/acp_special_cases_v03.md`
**Active integrity audit:** `audits/integrity_audit_v10.md`

---

## Where the paper stands

v10 includes, relative to what `memory.md` (legacy) describes as the v09 state:

- **A.20 Restraint-Power Theorem** + **Heisenberg uncertainty principle as the quantum-scale instantiation** of the coordination floor for a two-MASA operator-algebra partition. This is a substantial new result not reflected in the legacy memory file.
- The Price / Fisher reduction (A.19) is fully integrated.
- Ten testable predictions are stated with experimental protocols and falsification criteria (Section 6 + Appendix A.16).
- Quantitative lower bounds on the drift rate for non-Gaussian systems (A.17).

The full result inventory, as of v10 plus current standalone appendix drafts:

| # | Result | Where |
|---|---|---|
| 1–5 | Core proof chain (ACP statement, CDT, compounding lemma, Claim A.3 interventional, induction to k mechanisms) | `paper/` + `proofs/` |
| 6–10 | A.11–A.15: five reductions (Friston, Zurek, Bergstrom–Lachmann, Prigogine, Kauffman) | `reductions/` |
| 11 | A.16 empirical predictions (10 predictions, 3 novel from unification) | `bridges/empirical_predictions.md` |
| 12 | A.17 non-Gaussian bounds (non-Gaussian systems crystallize *faster* than Gaussian — Gaussian is the conservative lower bound) | `bridges/non_gaussian_bounds.md` |
| 13 | A.18 multiscale RG (C/D asymmetry, productive interval as RG-invariant subset) | `reductions/multiscale_rg.md` |
| 14 | A.19 Price / Fisher (selection = crystallization drift; Fisher's theorem = CDT applied to fitness space) | `reductions/price_equation.md` |
| 15 | A.20 Restraint-Power + Coordination Conservation; Heisenberg as special case | `bridges/restraint_power.md` + `bridges/syndrome_coordination.md` + `bridges/coordination_neutrality.md` |
| 16 | Schur complement bridge — four identifications unifying thermodynamic (ACP) and algebraic (Schur) registers; proposes Heisenberg derivation (now delivered by A.20) | `bridges/schur_complement.md` |
| 17 | A.21 draft meta-theoretic coherence — generativity as the anti-crystallization condition for theory evolution; quartet inquiry floor; ACP self-application | `proofs/meta_theoretic_coherence_theorem.md` |
| 18 | Valuation / arithmetic bridge — ratio operator on $\mathbb{Q}_{>0}^{\times}$ lifts exactly to the prime-valuation lattice, giving an additive arithmetic shadow of coordination-neutrality | `bridges/valuation_cocycle_bridge.md` |
| 19 | Unique-factorization rigidity for arithmetic shadows — on free arithmetic state spaces, any additive shadow whose one-variable coordinate respects orthogonal-support additivity and prime-ray additivity is forced to be valuation-type | `bridges/valuation_cocycle_bridge.md` |
| 20 | Bridge-family exclusion in the arithmetic regime — the exp-log coordination-neutral bridge family is not ratio-class constant on the rational regular domain and therefore cannot admit a factor-respecting arithmetic shadow | `bridges/valuation_cocycle_bridge.md` |
| 21 | Canonical defect decomposition for arithmetic shadows — every additive shadow on a free arithmetic state space splits exactly into a weighted-valuation baseline plus a defect coboundary built from prime-ray distortion and cross-prime mixing | `bridges/valuation_cocycle_bridge.md` |

## Active fronts

**1. Bibliography / submission packaging cleanup.** The v10 integrity audit is now complete and the paper-level inconsistencies it found have been corrected. The main remaining manuscript-state issue is bibliography policy: decide whether `paper/acp_main_v10.md` carries a paper-only reference list or a shared bibliography for the paper plus external appendix documents. *(Priority: medium; important for submission packaging, but no longer blocking formal integrity.)*

**2. Tier-1 computational tests for Predictions 8 and 9.** Named in legacy memory as on-the-horizon work. Need scoping: which empirical predictions in `bridges/empirical_predictions.md` are Tier-1 and what does "Tier-1" mean precisely? *(Priority: medium — not blocking, but a credibility multiplier if done.)*

**3. Journal selection.** Not yet decided. Candidates depend on whether we pitch the paper as (a) a thermodynamic first-principles paper (PRE, J. Stat. Phys.), (b) a unification across disciplines (Physics Reports, Reviews of Modern Physics), or (c) an information-theoretic paper (IEEE TIT, Entropy). This is a strategic call I should make once the v10 audit is clean. *(Priority: medium.)*

**4. Heisenberg / A.20 consequences.** If A.20 genuinely recovers Heisenberg as a special case of the coordination floor, there is a large downstream program: are there other canonical commutation relations recoverable? Is A.20 compatible with the Robertson bound's tightness conditions? Does it extend to infinite-dimensional MASAs? *(Priority: exploratory; open problem territory.)*

**5. Meta-theoretic coherence / A.21 integration.** The core of the generativity program is now formalized in `proofs/meta_theoretic_coherence_theorem.md`: the theory-evolution state space, the $G_t(T) > 1$ anti-crystallization identity, the quartet inquiry floor, and the ACP self-application corollary. The next question is packaging: integrate this as Appendix A.21 in `paper/acp_main_v10.md`, or leave it as a standalone proof until the submission boundary is clearer. *(Priority: medium — important for the theory's internal consistency story; not blocking journal prep.)*

**6. Arithmetic / operator bridge.** The valuation bridge now has six layers of closure: the scalar smooth case collapses to ratio, the smooth finite-dimensional vector-valued case collapses with it, the free-arithmetic valuation-type discrete case collapses to weighted prime ledgers with the primitive case canonically equivalent to the usual valuation map, any additive shadow whose coordinate map respects unique factorization is forced into that same valuation-type class, the exp-log coordination-neutral bridge family is excluded from that factor-respecting arithmetic subclass, and every additive shadow now splits exactly into a valuation baseline plus an explicit defect coboundary measuring prime-ray distortion and cross-prime mixing. The remaining frontier is therefore sharper still: can that defect term ever be nonzero in a genuine coordination-neutral arithmetic shadow without collapsing back to the valuation class, or does the canonical valuation picture exhaust the abelian arithmetic regime entirely? *(Priority: exploratory, but now tightly localized.)*

## Open problems

Canonical tracker: `OPEN_PROBLEMS.md`. Headline items:

- **OP-1: Quantitative erosion constant** (named "OP-new-2" in legacy memory). Channel Erosion (A.10) gives the rate is positive; we don't have a sharp numerical bound in general.
- **OP-2: Coherence crisis transient dynamics.** What happens *during* the regime change when one mechanism erodes another?
- **OP-3 through OP-6: Schur complement bridge open problems.** Four listed at the bottom of `bridges/schur_complement.md`, including the original Heisenberg derivation (partly answered by A.20 — needs reconciliation).
- **OP-7: Coordination neutrality under tree composition.** Named in `bridges/coordination_neutrality.md`. The bridge family (exp / log operators — cf. Odrzywolek's eml in `references/`) is CN pairwise but may fail joint-inversion invariance under composition.
- **OP-15: Arithmetic shadows of coordination-neutral operators.** Now partial from `bridges/valuation_cocycle_bridge.md`: the entire smooth finite-dimensional real-target case collapses to ratio-up-to-reparameterization, and the free-arithmetic valuation-type discrete case collapses to weighted prime-valuation shadows. The open part is the genuinely non-valuation discrete/infinite-rank case.

## Changelog

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
