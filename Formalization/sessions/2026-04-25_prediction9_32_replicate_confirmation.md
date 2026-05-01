# Session log — 2026-04-25: Prediction 9 32-replicate aligned confirmation

## Goal

Continue the top empirical front by running the larger aligned confirmation that `STATUS.md` identified as the next step for Prediction 9.

The target configuration was the surviving lead setting:

- `fitness_threshold = 0.85`
- `population_size = 28`
- `stability_weight = 0.2`

The important constraint was to preserve the direct simulator's canonical defaults after the 2026-04-22 helper/default alignment fix.

## Command

```bash
python3 Formalization/simulations/prediction9_boolean_network.py \
  --regimes selected neutral_post_threshold \
  --replicates 32 \
  --population-size 28 \
  --fitness-threshold 0.85 \
  --stability-weight 0.2 \
  --output-dir Formalization/simulations/output/prediction9_lead_aligned_32_2026-04-25
```

The run wrote the normal provenance bundle:

- `generation_metrics.csv`
- `simulation_config.json`
- `replicate_summaries.json`
- `aggregate_summary.json`

## Results

Both regimes reached threshold in `30/32` replicates.

Selected regime:

- mean post-optimal slope: `~0.00382`
- median post-optimal slope: `~0.00114`
- positive-slope fraction: `22/30`
- mean final best frozen fraction: `~0.859`
- mean final best lambda: `~1.145`

Neutral post-threshold control:

- mean post-optimal slope: `~0.00121`
- median post-optimal slope: `~0.00010`
- positive-slope fraction: `15/30`
- mean final best frozen fraction: `~0.945`
- mean final best lambda: `~1.234`

Difference summary:

- mean slope gap: `~0.00261`
- median slope gap: `~0.00103`
- positive-fraction gap: `~0.233`

## Interpretation

The lead setting survived the larger confirmation, but the result is still modest. The selected regime continues to show a stronger positive post-optimal frozen-fraction slope than the neutral control, yet the neutral control is not stationary. This means the current simulator is detecting a selected-vs-neutral separation, but not a clean decisive Tier-1 confirmation of the appendix-scale prediction.

The best next move is therefore proxy refinement rather than another broad grid search. The likely targets are:

- make the null more discriminating by preserving function while removing stability selection more cleanly;
- inspect whether the frozen-fraction estimator is being inflated by high final frozen fractions in both regimes;
- consider paired-seed comparisons or a direct selected-minus-neutral statistic rather than independent regime summaries;
- only then decide whether a larger replicate count is worth the compute.

## Status

Prediction 9 remains alive as an empirical lead. The project should describe the current result as supportive pilot evidence with a noisy proxy, not as a settled confirmation.
