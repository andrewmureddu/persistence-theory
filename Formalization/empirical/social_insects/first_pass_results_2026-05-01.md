# First-Pass Social-Insect Results

**Date:** 2026-05-01

## Dataset Acquisition

Downloaded first-pass honey-bee files from Zenodo record `10.5281/zenodo.7928121`:

- `Berlin2019_waggle_phases.csv` — 275,915 waggle-phase observations after header.
- `Berlin2019_dances.csv` — 1,993 dance rows after header.
- `Berlin2019_followers.csv` — 97,319 follower / attendance rows after header.

Dryad ant homeostasis data (`10.5061/dryad.sh4m4s6`) is visible from the dataset page, but terminal download currently returns WAF / authorization responses. It remains the first ant target, but acquisition may require browser-mediated download.

The authors' companion GitHub repository for the ant homeostasis paper is accessible and includes formatted trophallaxis spreadsheets:

- `Colony_1_trophallaxis_final.xlsx`
- `Colony_2_trophallaxis_final.xlsx`
- `Colony_3_trophallaxis_final.xlsx`

These do not replace the full Dryad tracking files, but they do provide a first ant-side interaction dataset.

## Methodological Correction

The first pass exposed and fixed two analysis-tooling issues:

1. `window_key` was rounding timestamps in minutes but converting them back as seconds. Hourly grouping was preserved, but output labels were wrong. This is fixed in both `social_insect_observables.py` and `bee_waggle_coupling_analysis.py`.
2. The first bee coupling pass treated lag 1 as the next active window, which can jump across gaps. `bee_waggle_coupling_analysis.py` and `bee_waggle_controlled_lag_analysis.py` now default to clock-contiguous lags. The old behavior remains available as `--lag-mode active-window` for reproduction only.

## Waggle-Phase Repertoire Summary

Command:

```bash
python3 Formalization/empirical/social_insects/social_insect_observables.py waggle \
  --input-csv Formalization/empirical/social_insects/data/raw/Berlin2019_waggle_phases.csv \
  --output-dir Formalization/empirical/social_insects/output/berlin2019_waggle_observables_60m \
  --window-minutes 60 \
  --spatial-bin-size 25 \
  --angle-bins 24
```

Results:

- 767 hourly windows.
- Corrected window labels span 2019-08-15 through the Berlin 2019 record rather than the earlier erroneous 1970 labels.
- Total observations: 275,915.
- Mean observations per hour: about 359.7.
- Maximum observations in one hour: 4,377.
- Mean angular entropy: about 2.918 nats.
- Mean dance-floor spatial entropy: about 3.603 nats.
- Mean dominant spatial-bin fraction: about 0.120.

## Dance-Follower Coupling

Command:

```bash
python3 Formalization/empirical/social_insects/bee_waggle_coupling_analysis.py \
  --dances-csv Formalization/empirical/social_insects/data/raw/Berlin2019_dances.csv \
  --followers-csv Formalization/empirical/social_insects/data/raw/Berlin2019_followers.csv \
  --output-dir Formalization/empirical/social_insects/output/berlin2019_dance_follower_coupling_60m \
  --window-minutes 60 \
  --lag-windows 1 \
  --min-dances 3
```

Data included in the merged dance/follower analysis:

- 51 hourly windows with dance/follower events.
- 1,993 dances.
- 97,319 follower/attendance events.
- 29,549 `follower` events.
- 67,770 `attendance` events.

Strongest contiguous one-hour lagged Spearman signals:

| Predictor at hour t | Outcome at hour t+1 | n | Spearman |
|---|---:|---:|---:|
| follower_events_per_dance | follower_entropy | 27 | 0.610 |
| follower_events_per_dance | dominant_follower_fraction | 27 | -0.607 |
| follow_events | follower_entropy | 27 | 0.566 |
| follower_events | follower_entropy | 27 | 0.557 |
| follow_events | dominant_follower_fraction | 27 | -0.505 |
| follower_events | dominant_follower_fraction | 27 | -0.504 |

At a contiguous three-hour lag, only five paired windows survive, so the result is not publication-grade. The signs are still in the same direction for follower concentration, but the sample is too small to interpret.

## Controlled Bee Lag Diagnostics

Command:

```bash
python3 Formalization/empirical/social_insects/bee_waggle_controlled_lag_analysis.py \
  --dances-csv Formalization/empirical/social_insects/data/raw/Berlin2019_dances.csv \
  --followers-csv Formalization/empirical/social_insects/data/raw/Berlin2019_followers.csv \
  --output-dir Formalization/empirical/social_insects/output/berlin2019_controlled_lag_60m_basic \
  --window-minutes 60 \
  --lag-windows 1 \
  --min-dances 3 \
  --permutations 1000
```

Basic controls residualize predictor and outcome against baseline outcome level, current dance count, next-window sampling effort, and hour-of-day. Under this conservative control set, the follower broadening result attenuates:

| Predictor at hour t | Outcome at hour t+1 | n | Raw Spearman | Partial Spearman |
|---|---:|---:|---:|---:|
| follower_events_per_dance | follower_entropy | 27 | 0.610 | 0.146 |
| follower_events_per_dance | dominant_follower_fraction | 27 | -0.607 | -0.311 |
| follow_events | follower_entropy | 27 | 0.566 | -0.035 |
| follow_events | dominant_follower_fraction | 27 | -0.505 | -0.033 |

The optional day-fixed-effects diagnostic preserves some stronger signs, including `follower_events_per_dance -> follower_entropy` partial Spearman about `0.577` and `follower_events_per_dance -> dominant_follower_fraction` partial Spearman about `-0.465`, but it fits 19 terms with only 26-27 observations. Treat it as a robustness probe, not as a primary estimate.

Interpretation: the bee result is promising but not yet controlled. The next methodological step should be a sample-size-aware follower null: rarefied follower entropy and/or within-window follower-identity shuffles that hold event count fixed.

## Bee Follower Null Diagnostics

Command:

```bash
python3 Formalization/empirical/social_insects/bee_follower_null_analysis.py \
  --dances-csv Formalization/empirical/social_insects/data/raw/Berlin2019_dances.csv \
  --followers-csv Formalization/empirical/social_insects/data/raw/Berlin2019_followers.csv \
  --output-dir Formalization/empirical/social_insects/output/berlin2019_follower_null_60m_r50 \
  --window-minutes 60 \
  --lag-windows 1 \
  --min-dances 3 \
  --rarefaction-size 50 \
  --rarefaction-replicates 1000 \
  --identity-permutations 1000
```

The null script adds two checks:

- rarefaction: compute follower entropy and dominant-follower concentration after drawing the same number of follower events from each later window;
- identity shuffling: keep each later window's follower-event count fixed, then shuffle follower identities across compatible event slots. The basic condition is day; the targeted follow-up also supports day+feeder, day+dancer, and day+dancer+feeder conditions.

With a stricter 50-event rarefaction, 24 one-hour pairs remain. The directional follower-channel signal survives the sample-size-aware outcome:

| Predictor at hour t | Outcome at hour t+1 | n | Raw Spearman | Rarefied Spearman | Identity-shuffle Spearman p |
|---|---:|---:|---:|---:|---:|
| follower_events_per_dance | follower_entropy | 24 | 0.496 | 0.576 | 1.000 |
| follower_events_per_dance | dominant_follower_fraction | 24 | -0.499 | -0.659 | 0.958 |
| follow_events | follower_entropy | 24 | 0.503 | 0.565 | 1.000 |
| follow_events | dominant_follower_fraction | 24 | -0.436 | -0.642 | 0.984 |

Interpretation: the rarefaction result argues against a trivial "more follower events mechanically produce higher entropy" explanation. But the within-day identity-shuffle null is more sobering: once later-window event counts and day-level follower identity pools are preserved, null correlations are typically as strong as or stronger than the observed correlations. The current bee result should therefore be treated as a sharpened candidate signal, not as controlled evidence of recruitment-specific follower-channel broadening.

Targeted conditioned-null follow-up:

```bash
python3 Formalization/empirical/social_insects/bee_follower_null_analysis.py \
  --dances-csv Formalization/empirical/social_insects/data/raw/Berlin2019_dances.csv \
  --followers-csv Formalization/empirical/social_insects/data/raw/Berlin2019_followers.csv \
  --output-dir Formalization/empirical/social_insects/output/berlin2019_follower_null_60m_r50_day_feeder_targeted \
  --window-minutes 60 \
  --lag-windows 1 \
  --min-dances 3 \
  --rarefaction-size 50 \
  --rarefaction-replicates 500 \
  --identity-permutations 200 \
  --identity-shuffle-condition day-feeder \
  --predictors follower_events_per_dance follow_events \
  --outcomes follower_entropy dominant_follower_fraction
```

The same targeted command was run for `day`, `day-feeder`, `day-dancer`, and `day-dancer-feeder`. These are exploratory 200-permutation p-values, but the result is directionally clear:

| Identity shuffle condition | Strata | `follower_events_per_dance -> follower_entropy` p | `follower_events_per_dance -> dominant_follower_fraction` p | `follow_events -> follower_entropy` p | `follow_events -> dominant_follower_fraction` p |
|---|---:|---:|---:|---:|---:|
| day | 12 | 1.000 | 0.975 | 1.000 | 0.995 |
| day+feeder | 24 | 0.960 | 0.905 | 0.801 | 0.965 |
| day+dancer | 275 | 1.000 | 0.980 | 1.000 | 1.000 |
| day+dancer+feeder | 280 | 1.000 | 0.965 | 1.000 | 1.000 |

Conditioning the identity shuffle by feeder and dancer does not rescue the recruitment-specific reading. The observed one-hour follower broadening is best treated as a day / feeder / dancer composition artifact until a stronger event-level model, a multi-hive replication, or an intervention-defined recruitment measure says otherwise.

Stratum-driver diagnostic:

```bash
python3 Formalization/empirical/social_insects/bee_follower_strata_diagnostics.py \
  --dances-csv Formalization/empirical/social_insects/data/raw/Berlin2019_dances.csv \
  --followers-csv Formalization/empirical/social_insects/data/raw/Berlin2019_followers.csv \
  --output-dir Formalization/empirical/social_insects/output/berlin2019_follower_strata_drivers_60m_r50 \
  --window-minutes 60 \
  --lag-windows 1 \
  --min-dances 3 \
  --min-later-follower-events 50 \
  --predictors follower_events_per_dance follow_events
```

This follow-up asks which composition strata make the identity-shuffle null so strong. It writes per-pair stratum event shares and per-stratum driver summaries for `day`, `day-feeder`, `day-dancer`, and `day-dancer-feeder` conditions.

Among strata with at least 100 later-window follower events, current `follower_events_per_dance` is already aligned with the later pooled follower identity pool:

| Stratum condition | Event-rich strata | Spearman with pooled follower entropy | Spearman with pooled dominant-follower fraction |
|---|---:|---:|---:|
| day | 12 | 0.783 | -0.853 |
| day+feeder | 24 | 0.741 | -0.730 |
| day+dancer | 158 | 0.516 | -0.593 |
| day+dancer+feeder | 158 | 0.519 | -0.593 |

The day and day+feeder confounds are especially concrete. For example, `2019-09-02 | feeder=1.0` has 10,339 later-window follower events, mean current `follower_events_per_dance` about `98.47`, pooled follower entropy `5.823`, and dominant-follower fraction `0.012`; `2019-08-21 | feeder=1.0` has 778 events, mean current `follower_events_per_dance` about `6.57`, pooled follower entropy `4.709`, and dominant-follower fraction `0.042`. Shuffling follower identities inside these strata preserves the identity-pool gradient that already tracks the predictor, so the null can reproduce the headline broadening without any recruitment-specific channel-opening effect.

Next bee step: either fit an event-level mixed model with later-window follower effort, day, dancer, feeder, and follower identity structure explicit, or treat the bee follower result as a useful negative-control appendix and pivot the empirical track toward the ant perturbation program where the treatment contrast is cleaner.

## Ant Trophallaxis First Pass

Command:

```bash
python3 Formalization/empirical/social_insects/ant_trophallaxis_summary.py \
  --input-dir Formalization/empirical/social_insects/data/raw/ant_homeostasis_github \
  --output-dir Formalization/empirical/social_insects/output/ant_homeostasis_trophallaxis_60m \
  --window-seconds 3600
```

The script reads the three companion spreadsheets, removes reciprocal duplicate rows, and writes treatment, window, event, and high/low contrast summaries.

- Deduplicated trophallaxis events: 3,262.
- Colonies: 3.
- Treatments: high density and low density.
- Window size: one hour.

Density contrasts:

| Colony | High rate/hr | Low rate/hr | Low vs high rate change | Edge entropy delta | Location entropy delta |
|---:|---:|---:|---:|---:|---:|
| 1 | 124.0 | 151.8 | +22.4% | +0.194 | +0.687 |
| 2 | 80.0 | 138.3 | +72.8% | +0.455 | +0.724 |
| 3 | 168.5 | 153.8 | -8.7% | -0.174 | +0.811 |

This is a useful first ant signal. Low-density interaction-location entropy rises in every colony, as expected when nest space expands. Interaction throughput is preserved or increased in colonies 1 and 2 but falls modestly in colony 3. The pattern is not a monotone density story; it suggests colony-specific entropy reallocation across location and partner channels.

Limit: these spreadsheets contain trophallaxis events, not the full ant-location time series. They can test interaction throughput, partner/edge entropy, and interaction-location entropy, but not the full spatial occupancy or transition-entropy program.

## Interpretation

The first bee result is not the naive crystallization signature. Higher follower activity is followed by **higher** follower entropy and **lower** dominant-follower concentration. In ACP terms, the follower channel initially appears to reopen or broaden after recruitment activity rather than narrowing immediately.

The follower-null diagnostics make that reading much less secure. Rarefaction shows the direction is not just a sample-size artifact, but day / feeder / dancer conditioned identity shuffles show that the observed correlations are compatible with the follower identities already available in those strata. Stratum-driver diagnostics then show that current recruitment activity is already aligned with later follower-identity-pool diversity across event-rich day / feeder / dancer strata. The bee result is therefore a candidate adaptive-coherence pattern, not controlled evidence of recruitment-specific channel broadening.

The first ant result gives the complementary perturbation-side pattern: nest expansion raises interaction-location entropy in all colonies, while interaction throughput is colony-specific rather than mechanically density-determined.

The publication-grade next steps are:

- decide whether to fit a stronger event-level bee mixed model or pivot the empirical push toward the cleaner ant perturbation contrast;
- use the ant trophallaxis spreadsheets for a colony-level mixed model of interaction rate versus location/edge entropy;
- acquire the full Dryad ant location files for spatial occupancy and transition entropy.
