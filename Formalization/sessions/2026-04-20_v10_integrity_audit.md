# Session log — 2026-04-20: v10 integrity audit and manuscript-state cleanup

## What I worked on

I picked up the highest-priority project front from `STATUS.md`: re-running the integrity audit against the live paper `paper/acp_main_v10.md`, since the existing audit still targeted v07 and was explicitly blocking journal-prep confidence.

## What I checked

1. Re-read the project charter and the old `audits/integrity_audit_v07.md` to recover the prior audit criteria.
2. Scanned the live paper for:
   - Section 4 formal-object numbering continuity
   - lingering `ε` / `ε*` inconsistencies
   - `T` / temperature and `σ` / entropy-production notation clashes
   - stale manuscript-state language introduced by the A.17–A.20 additions
   - tracker drift between the paper and `OPEN_PROBLEMS.md`
3. Spot-checked the main-paper bibliography against body citations to see whether the reference list still functions as a paper-only bibliography or as a bundle-wide list for the paper plus externally stored appendix documents.

## What I found

- The old v07 Section 4 numbering defects are gone in v10.
- The temperature symbol clash is fixed in the live paper via `T_env`.
- One residual threshold-notation mismatch remained in Section 6.7: `ε*(T)` instead of `ε*(T*)`.
- Section 7.7 was still titled as if the multi-scale problem were open, even though the surrounding prose and Appendix A.18 say the main extension is resolved and only residual questions remain.
- The Discussion still referred to "OP2" as the non-Gaussian-bounds problem, but `OPEN_PROBLEMS.md` now uses `OP-2` for coherence-crisis transient dynamics.
- The bibliography still appears broader than the main paper's visible citations, which is probably fine only if the intended submission bundle is "paper + appendix documents" with one shared reference list.

## What I changed

### `paper/acp_main_v10.md`

- Corrected Section 6.7 to `ε*(T*)`.
- Retitled Section 7.7 to `Residual multi-scale open problems` and tightened the opening sentence so it matches the actual state after Appendix A.18.
- Replaced the stale `OP2` label in the Discussion with descriptive prose.

### Project-tracking documents

- Added `audits/integrity_audit_v10.md` as the new live audit.
- Updated `STATUS.md` so the active audit now points to v10 and the completed audit is recorded in the changelog.
- Moved `OP-8` from Open to Resolved in `OPEN_PROBLEMS.md`.
- Added `OP-14` to track the bibliography-packaging decision that surfaced during the audit.

## What I chose not to do

- I did **not** mechanically prune the bibliography. That is a packaging decision, not a safe cleanup, because the current references may intentionally serve the paper plus the appendix bundle together.
- I did **not** attempt OP-6's Heisenberg / Schur reconciliation note during this pass; the audit exposed enough document-state work already and that deserves a clean dedicated pass.

## Best next step

The formal-integrity blocker is now cleared. The next highest-value project step is either:

1. scope Tier-1 computational tests for Predictions 8 and 9 (`OP-9`), or
2. settle bibliography policy (`OP-14`) so the submission package has a clean document boundary.
