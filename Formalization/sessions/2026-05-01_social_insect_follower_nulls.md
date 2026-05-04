# 2026-05-01 — Social-Insect Follower Nulls

## Aim

Continue the social-insect empirical track by testing whether the Berlin 2019
honey-bee follower-channel broadening result survives sample-size-aware nulls.

## What changed

- Added `empirical/social_insects/bee_follower_null_analysis.py`.
- Implemented rarefied follower entropy and dominant-follower concentration
  for lagged later windows.
- Implemented within-day follower-identity shuffles that preserve each later
  window's follower-event count while breaking the association between clock
  window and follower identity composition.
- Updated `empirical/social_insects/README.md`,
  `empirical/social_insects/first_pass_results_2026-05-01.md`, and
  `STATUS.md` with the sharper caveat.

## Diagnostic result

The stricter 50-event rarefaction leaves 24 contiguous one-hour lag pairs. The
directional signal survives rarefaction:

| Predictor at hour t | Outcome at hour t+1 | n | Raw Spearman | Rarefied Spearman | Identity-shuffle Spearman p |
|---|---:|---:|---:|---:|---:|
| follower_events_per_dance | follower_entropy | 24 | 0.496 | 0.576 | 1.000 |
| follower_events_per_dance | dominant_follower_fraction | 24 | -0.499 | -0.659 | 0.958 |
| follow_events | follower_entropy | 24 | 0.503 | 0.565 | 1.000 |
| follow_events | dominant_follower_fraction | 24 | -0.436 | -0.642 | 0.984 |

Interpretation: the follower broadening result is not explained away by the
mechanical fact that higher later-window sample size raises entropy. However,
the within-day identity-shuffle null is not passed. Once later-window event
counts and day-level follower identity pools are preserved, null correlations
are as strong as or stronger than the observed correlations.

## What remains open

- Build a dancer / feeder / day-conditioned null.
- Test whether the effect survives a mixed model with later-window follower
  effort, day, dancer, and feeder structure explicit.
- Decide whether follower broadening is recruitment-specific or mostly a
  day-level identity-composition artifact.

## Generativity ledger

- Closed / strengthened (`C_closed`): the bee result now has its first
  sample-size-aware null rather than only raw and residualized correlations.
- New questions (`Q_new`): does the signal survive dancer / feeder / day
  conditioning; is follower broadening recruitment-specific or day-composition
  driven; which follower identities contribute most to the null structure?
- New observables or bridge variables (`O_new`): rarefied follower entropy,
  rarefied dominant-follower fraction, within-day identity-shuffle null
  correlations.
- New tests, falsifiers, or simulations (`P_new`): dancer / feeder / day
  conditioned permutation null; mixed model with follower effort and day /
  feeder / dancer terms.
- Workflow check: `G_session = (3 + 3 + 2) / max(1, 1) = 8`.
- Boundary assessment: the result is more honest and more useful because it
  preserves the candidate signal while blocking premature publication-grade
  interpretation.
