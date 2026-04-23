# 2026-04-21 — reviewer-driven rigor remediation

## Goal

Address the reviewer-style rigor findings by making the live paper and appendix stack say exactly what the current proofs support, no more and no less.

## Main changes

- Recast `paper/acp_main_v10.md` so the CDT is presented in two layers:
  - a closed core entropy-drift theorem under maintained net entropy-reducing pressure
  - stronger repertoire-geometry consequences (load growth, basin shrinkage, default approach to C) stated only conditionally on the missing maintenance lemma
- Softened public-facing language in the abstract, introduction, discussion, and Appendix C proof-chain summary so the repo no longer claims the full CDT package is already closed.
- Updated the paper's discussion of Appendix A.9 so the Gaussian branch is distinguished from the generic branch.

## Appendix-specific fixes

- `proofs/induction_step_k_mechanisms.md`
  - made the hidden intersection-closure hypotheses explicit in Lemma A.9.1
  - downgraded the appendix from "resolved" to "Gaussian-closed / generic-conditional"
  - rewrote the summary chain so it no longer treats the generic induction as unconditional
- `bridges/restraint_power.md`
  - tightened Definition A.20.10a to the kernel-preserving mechanism-preserving notion actually used in the proof
  - propagated that stronger premise through Theorems A.20.10 and A.20.22 and their summaries
- `bridges/non_gaussian_bounds.md`
  - reframed the appendix as a partial quantitative program rather than a full resolution
  - marked Theorem A.17.7 as conditional on the linear-conservatism hypothesis
  - recast the drift-rate and time-to-crystallization claims as strongest-current templates rather than fully settled universal bounds

## Tracking updates

- Updated `STATUS.md` to reflect the new theorem architecture and to add newly isolated open problems.
- Added OP-16 through OP-18 to `OPEN_PROBLEMS.md`:
  - maintenance lemma / net reinforcement pressure
  - generic k-mechanism closure under intersection
  - mechanism-preserving vs kernel-preserving conservation

## Outcome

The project is now more reviewer-resistant in the narrow but important sense that the public-facing manuscript, the appendix notes, and the canonical tracker all tell the same story about what is closed, what is conditional, and what remains open.
