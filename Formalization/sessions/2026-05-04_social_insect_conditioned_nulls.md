# 2026-05-04 — Social-Insect Conditioned Follower Nulls

## Aim

Continue the Berlin 2019 honey-bee follower-channel check by asking whether the
candidate one-hour follower-broadening signal survives identity shuffles that
preserve more of the dancer / feeder / day event structure.

## What changed

- Extended `empirical/social_insects/bee_follower_null_analysis.py` with
  `--identity-shuffle-condition`.
- Supported four shuffle conditions:
  - `day`
  - `day-feeder`
  - `day-dancer`
  - `day-dancer-feeder`
- Kept each later window's follower-event slots fixed while shuffling follower
  identities only within the chosen compatible event-slot stratum.
- Added `empirical/social_insects/bee_follower_strata_diagnostics.py` to
  identify which day / feeder / dancer strata align current recruitment
  predictors with later follower identity-pool diversity.
- Updated `empirical/social_insects/README.md`,
  `empirical/social_insects/first_pass_results_2026-05-01.md`, and
  `STATUS.md` with the sharper negative result.

## Diagnostic Result

The targeted follow-up used the two headline predictors and two follower-channel
outcomes, with 50-event rarefaction, 500 rarefaction replicates, and 200
identity permutations per condition.

| Identity shuffle condition | Strata | `follower_events_per_dance -> follower_entropy` p | `follower_events_per_dance -> dominant_follower_fraction` p | `follow_events -> follower_entropy` p | `follow_events -> dominant_follower_fraction` p |
|---|---:|---:|---:|---:|---:|
| day | 12 | 1.000 | 0.975 | 1.000 | 0.995 |
| day+feeder | 24 | 0.960 | 0.905 | 0.801 | 0.965 |
| day+dancer | 275 | 1.000 | 0.980 | 1.000 | 1.000 |
| day+dancer+feeder | 280 | 1.000 | 0.965 | 1.000 | 1.000 |

The 50-event rarefaction still preserves the directional signal:
`follower_events_per_dance -> follower_entropy` rarefied Spearman is about
`0.58`, and `follower_events_per_dance -> dominant_follower_fraction` is about
`-0.67` across the targeted runs. But the conditioned identity-shuffle nulls
still produce correlations at least as strong as the observed ones.

## Stratum-Driver Follow-Up

The follow-up script used the same 60-minute, one-lag, minimum-three-current
dance, and minimum-50-later-follower-event filter as the rarefaction headline.

Among strata with at least 100 later-window follower events, current
`follower_events_per_dance` is already aligned with later pooled follower
identity diversity:

| Stratum condition | Event-rich strata | Spearman with pooled follower entropy | Spearman with pooled dominant-follower fraction |
|---|---:|---:|---:|
| day | 12 | 0.783 | -0.853 |
| day+feeder | 24 | 0.741 | -0.730 |
| day+dancer | 158 | 0.516 | -0.593 |
| day+dancer+feeder | 158 | 0.519 | -0.593 |

The strongest day+feeder contrast is easy to read:
`2019-09-02 | feeder=1.0` has 10,339 later-window follower events, mean current
`follower_events_per_dance` about `98.47`, pooled follower entropy `5.823`, and
dominant-follower fraction `0.012`; `2019-08-21 | feeder=1.0` has 778 events,
mean current `follower_events_per_dance` about `6.57`, pooled follower entropy
`4.709`, and dominant-follower fraction `0.042`.

This makes the null behavior intelligible: shuffling follower identities inside
day / feeder / dancer strata preserves an identity-pool gradient that already
tracks the current-window predictor.

## Interpretation

Conditioning the identity shuffle by feeder and dancer does not rescue the
recruitment-specific reading. The best current interpretation is that the
hourly bee follower result is dominated by day / feeder / dancer composition,
not controlled evidence that successful recruitment broadens follower identity
channels.

This is useful negative evidence: it prevents the social-insect track from
overclaiming a publishable bee effect and points the empirical program toward
either a stronger event-level model or the cleaner ant perturbation contrast.

## What Remains Open

- Fit an event-level mixed model with later-window follower effort, day, dancer,
  feeder, and follower identity structure explicit.
- Decide whether to keep the bee follower result as a negative-control appendix
  or retire it from the main empirical push.
- Decide whether the next empirical push should stay with bee recruitment or
  pivot to the ant density-perturbation program where the treatment contrast is
  cleaner.

## Generativity Ledger

- Closed / strengthened (`C_closed`): the previous "build a dancer / feeder /
  day-conditioned null" next step is now implemented and run; the successor
  "which strata drive the null?" question is answered at first-pass diagnostic
  level.
- New questions (`Q_new`): whether an event-level mixed model can isolate any
  residual recruitment effect; whether the bee follower result belongs only as
  a negative-control appendix; whether the ant perturbation track is now the
  better empirical vehicle.
- New observables or bridge variables (`O_new`): conditioned follower-identity
  shuffle strata, stratum counts, later-window stratum event shares, and pooled
  stratum follower diversity / concentration.
- New tests, falsifiers, or simulations (`P_new`): day+feeder, day+dancer, and
  day+dancer+feeder identity-shuffle nulls; stratum-driver diagnostics for
  day, day+feeder, day+dancer, and day+dancer+feeder composition artifacts.
- Workflow check: `G_session = (3 + 4 + 7) / max(1, 2) = 7`.
- Boundary assessment: the social-insect track is stronger because the bee
  result is now honestly downgraded rather than overread.
