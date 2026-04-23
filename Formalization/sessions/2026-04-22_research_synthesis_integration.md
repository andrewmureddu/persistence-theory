# 2026-04-22 — research synthesis integration for CDT and restraint-power

## Goal

Use the second-pass literature scan to make the CDT and restraint-power presentation more rigorous, not by pretending the scan closes open lemmas, but by tightening how the project positions itself relative to existing results.

## Main changes

- Rewrote the CDT "Relationship to Existing Results" sections in `proofs/crystallization_drift_theorem.md` and `paper/acp_main_v10.md`.
- Recast the CDT's external positioning into three clusters:
  - productive-interval / cascade geometry,
  - rigidity-from-success / lock-in,
  - release / reset.
- Distinguished formal reductions already proved in-repo (especially Kauffman and Friston) from merely structural neighbors in adjacent literatures.
- Added positioning remarks to `bridges/restraint_power.md` clarifying that the theorem's two defining clauses live in different neighboring literatures:
  - strongest-goes-first in self-binding, anti-saturation, and backoff settings,
  - visibility / decodability in public-commitment and common-knowledge settings.
- Recast the A.20 domain table as a disciplined test map rather than evidence that every domain has already proved the theorem under another name.

## Outcome

The live documents now make a narrower but stronger claim. CDT and restraint-power are not justified by analogy, but the nearest external analogs are now charted more accurately, which reduces reviewer attack surface around novelty and overreach.
