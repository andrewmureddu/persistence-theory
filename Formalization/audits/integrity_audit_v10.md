# ACP v0.9 Integrity Audit

**Date:** April 20, 2026
**Scope:** Full cross-reference, numbering, notation, and manuscript-state audit of `paper/acp_main_v10.md`

---

## Executive summary

The highest-severity v07 audit issues have mostly been cleared in v10. Section 4's formal-object numbering is now gapless; the old `T` overloading has been resolved by renaming environmental temperature to `T_env`; and the stale "resolved" header language that previously made the manuscript look like an internal checklist has been removed. Three manuscript-state issues remained at audit time:

1. **Prediction 7 notation drift** in Section 6.7 (`ε*(T)` instead of `ε*(T*)`), inconsistent with Section 4.4.7 and the notation table.
2. **Section 7.7 framing drift**: the section was still titled as if the multi-scale problem were open, even though the section preamble and Appendix A.18 both state that the main extension has been resolved and only residual questions remain.
3. **Stale open-problem label in Discussion**: the text referred to "OP2" as the non-Gaussian-bounds problem, but the canonical `OPEN_PROBLEMS.md` now assigns `OP-2` to coherence-crisis transient dynamics.

All three have been corrected in `paper/acp_main_v10.md` during this audit pass.

---

## 1. Re-audit of v07 findings

### 1.1 Numbering gaps

**Status:** Fixed.

The v07 numbering gaps at Section 4.4 have been resolved. The live sequence is now:

- `Lemma 4.13`
- `Lemma 4.14`
- `Lemma 4.15`
- `Lemma 4.16`
- `Theorem 4.17`
- `Corollary 4.18`
- `Remark 4.19`
- `Corollary 4.20`
- `Corollary 4.21`
- `Remark 4.22`

No Section 4 gap analogous to the old 4.15 / 4.18 problem remains.

### 1.2 `ε` / `ε*` consistency

**Status:** Mostly fixed; one residual inconsistency found and corrected.

The threshold quantity is now consistently defined as `ε*(t)` in Corollary 4.21, used correctly in Section 4.4.7, and listed correctly in the notation table. One residual mismatch persisted in Section 6.7:

- Section 4.4.7: `ε*(T*)` at the defining threshold time
- Section 6.7 (pre-fix): `ε*(T)`

This has now been corrected to `ε*(T*)`.

### 1.3 `T` overloading

**Status:** Fixed in the core paper.

The thermodynamic temperature symbol has been disambiguated to `T_env` in Axiom 1, eliminating the direct clash with the time-evolution operator `T` from Definition 2.1.

### 1.4 `σ` overloading

**Status:** Acceptably mitigated, not fully eliminated.

The paper still uses `σ` for the coarse-graining map and `σ_P` for Prigogine-specific entropy production. This is now explicit in the notation table and context-local, so the live issue is much weaker than in v07. I would not treat this as a blocking flaw, though a fully submission-polished version could mention in Section 5.1 that `σ_P` is a domain-local symbol.

---

## 2. New v10-specific findings

### 2.1 Section 7.7 was framed as unresolved after Appendix A.18 resolved the main extension

**Severity:** Important, but easy to fix.

Section 7 opens by stating that the list contains "genuine remaining gaps" and explicitly says the multi-scale problem has been resolved via Appendix A.18. But Section 7.7 was still titled `The multi-scale problem`, which reads as if the entire extension remained open. The content itself already described resolved results plus residual questions.

**Fix applied:** Retitled the section to `Residual multi-scale open problems` and tightened the opening sentence to match the actual state.

### 2.2 Discussion used a stale open-problem identifier

**Severity:** Important for workspace coherence.

The Discussion referred to "the resolution of OP2 (non-Gaussian bounds, Appendix A.17)." In the canonical tracker, `OP-2` is now the coherence-crisis transient-dynamics problem. This creates a document-to-tracker mismatch that will confuse future sessions and any attempt to cite the open-problem list from the paper text.

**Fix applied:** Replaced the stale identifier with descriptive prose: `the quantitative non-Gaussian-bounds problem`.

### 2.3 Main-paper bibliography still appears broader than main-paper citations

**Severity:** Submission-readiness issue, not a logic flaw.

Several references appear to be present only in the bibliography and not cited in the main paper body, including at least:

- DeLong et al. (1988)
- Glansdorff & Prigogine (1971)
- Kubo (1966)
- Langton (1990)
- Lewontin (1978)
- Onsager (1931)
- Pinsker (1964)
- Stein et al. (2025)
- Tsybakov (2009)

This may be intentional if the bibliography is meant to cover the paper plus the externally stored appendix documents as a single submission package. If the main manuscript is expected to stand on its own, the reference list should be reconciled against actual main-text citations.

**Recommendation:** Decide explicitly between:

- a unified bibliography for paper + appendix documents, or
- a paper-only bibliography in `acp_main_v10.md` with appendix-local reference lists elsewhere.

Until that decision is made, I would not remove entries mechanically.

---

## 3. Cross-reference and manuscript-state assessment

### 3.1 Intro roadmap

**Status:** Good.

The introduction now says "seven steps" and lists seven items. The old v07 count mismatch is gone.

### 3.2 Section 7 internal state language

**Status:** Improved.

The old `RESOLVED` / `PARTIALLY RESOLVED` section-header style is gone. Section 7 now reads like a research paper rather than an internal project checklist.

### 3.3 Open-problem honesty markers

**Status:** Good.

The paper continues to distinguish resolved results from residual gaps cleanly in prose. The old inline warning-marker style has been reduced without losing epistemic honesty.

---

## 4. Bottom line

`acp_main_v10.md` is materially cleaner than v07 and no longer carries the old Section 4 numbering defects. After this audit pass, the most important remaining manuscript-state issue is **bibliography policy**: whether the paper's references are meant to serve the paper alone or the paper-plus-appendix bundle. That is a submission-packaging decision, not a core-theory defect.
