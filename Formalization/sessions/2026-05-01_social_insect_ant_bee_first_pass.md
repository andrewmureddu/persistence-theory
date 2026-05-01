# 2026-05-01 Social-Insect Ant/Bee First Pass

## What changed

- Continued the Tier-2 social-insect empirical track in `empirical/social_insects/`.
- Fixed a timestamp-labeling bug in both social-insect windowing scripts: rounded minute buckets are now converted back to seconds before calling `datetime.fromtimestamp`.
- Changed bee lag analyses to default to true clock-contiguous lags rather than "next active window" lags. The old exploratory behavior remains available as `--lag-mode active-window`.
- Added `bee_waggle_controlled_lag_analysis.py` for residualized bee lag diagnostics.
- Retrieved the authors' ant-homeostasis companion GitHub archive after Dryad terminal access returned 403, copied the three trophallaxis workbooks into ignored raw data, and added `ant_trophallaxis_summary.py`.

## Bee result

The corrected Berlin 2019 contiguous one-hour lag pass strengthens the raw follower-channel broadening signal:

- `follower_events_per_dance -> follower_entropy`: Spearman `~0.610`, `n = 27`.
- `follower_events_per_dance -> dominant_follower_fraction`: Spearman `~-0.607`, `n = 27`.
- `follow_events -> follower_entropy`: Spearman `~0.566`, `n = 27`.

Basic controls for baseline outcome, current dance count, next-window sampling effort, and hour-of-day attenuate the result. The day-fixed-effects diagnostic preserves stronger signs but is high-dimensional relative to `n`, so the publication-grade next step is a sample-size-aware follower null: rarefaction and/or within-window follower-identity shuffles.

## Ant result

The companion trophallaxis spreadsheets yielded 3,262 deduplicated events across three colonies and high/low density treatments.

Density contrasts:

| Colony | Low vs high rate change | Edge entropy delta | Location entropy delta |
|---:|---:|---:|---:|
| 1 | +22.4% | +0.194 | +0.687 |
| 2 | +72.8% | +0.455 | +0.724 |
| 3 | -8.7% | -0.174 | +0.811 |

Low-density interaction-location entropy rises in every colony, while throughput is colony-specific. This supports the empirical framing that density perturbation is not merely a scalar density story; interaction function can be preserved through different reallocations across location and partner channels.

## Next steps

- Build rarefied / shuffled bee follower-channel nulls.
- Fit colony-level ant models for interaction rate versus interaction-location and edge entropy.
- Acquire the full Dryad ant location data for spatial occupancy and transition-entropy tests.
