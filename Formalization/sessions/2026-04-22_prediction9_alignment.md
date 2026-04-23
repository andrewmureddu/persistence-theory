# Session log — 2026-04-22: Prediction 9 helper/default alignment

## What I worked on

I continued the top empirical front in Prediction 9 by checking the lead calibration region directly rather than assuming the helper summaries and direct simulator runs were still on the same footing.

## What I found

The sweep helper and the direct simulator had silently drifted apart on several defaults:

- `settle_steps`: helper `8`, simulator `12`
- `attractor_steps`: helper `64`, simulator `96`
- `derrida_samples`: helper `6`, simulator `8`
- `max_generations`: helper `70`, simulator `80`
- `post_optimal_generations`: helper `24`, simulator `40`

That meant a helper-driven calibration summary and a direct simulator rerun could disagree for methodological reasons rather than because the lead configuration was genuinely unstable.

I confirmed the discrepancy empirically before editing:

- old helper defaults, `(0.85, 28, 0.2)`, `8` replicates: slope gap `~-0.00319`
- direct simulator defaults, same visible configuration and replicate count: selected mean slope `~0.00342`, neutral mean slope `~4.36e-05`, so slope gap `~0.00337`

So this was a real comparability bug, not just ordinary stochastic noise.

## What I changed

### `simulations/prediction9_boolean_network.py`

- Introduced a single canonical `DEFAULT_CONFIG`.
- Added a small `build_config(...)` helper so other entry points can derive configs from the same source of truth.
- Made the CLI defaults read from that canonical config.
- Added `simulation_config.json` to each run's output directory.

### `simulations/prediction9_calibration_sweep.py`

- Removed the stale duplicate default values and made the helper inherit defaults from `prediction9_boolean_network.py`.
- Added `sweep_parameters.json` so each sweep records the exact arguments used.

### `simulations/README.md`

- Documented the new provenance files and noted that the sweep helper now inherits the simulator defaults by default.

## Verification

I ran:

1. `python3 -m py_compile Formalization/simulations/prediction9_boolean_network.py Formalization/simulations/prediction9_calibration_sweep.py`
2. Direct aligned rerun:
   `python3 Formalization/simulations/prediction9_boolean_network.py --regimes selected neutral_post_threshold --replicates 8 --population-size 28 --fitness-threshold 0.85 --stability-weight 0.2 ...`
3. Helper aligned rerun on the same single configuration:
   `python3 Formalization/simulations/prediction9_calibration_sweep.py --replicates 8 --fitness-thresholds 0.85 --population-sizes 28 --stability-weights 0.2 ...`
4. Larger aligned direct confirmation on the same lead configuration:
   `python3 Formalization/simulations/prediction9_boolean_network.py --regimes selected neutral_post_threshold --replicates 16 --population-size 28 --fitness-threshold 0.85 --stability-weight 0.2 ...`

The two aligned runs now agree numerically:

- selected mean post-optimal slope `~0.00342`
- neutral mean post-optimal slope `~4.36e-05`
- slope gap `~0.00337`
- selected positive-slope fraction `~0.857`
- neutral positive-slope fraction `0.25`

I also ran one aligned check on the previously tracked backup setting `(0.85, 24, 0.4)`. In that aligned eight-replicate rerun it was effectively flat / slightly negative, with slope gap `~-2.7e-4` and no positive-fraction advantage.

The larger aligned sixteen-replicate confirmation on the lead setting remained positive, but the effect attenuated:

- selected mean post-optimal slope `~0.00207`
- neutral mean post-optimal slope `~0.000586`
- slope gap `~0.00149`
- selected positive-slope fraction `~0.733`
- neutral positive-slope fraction `0.375`

## Outcome

The live empirical picture is cleaner now:

- `(0.85, 28, 0.2)` remains the only meaningful lead candidate under aligned settings.
- The lead still weakens as replicate count rises, so the next question is stability under larger aligned confirmation rather than whether the sign can be made positive once.
- `(0.85, 24, 0.4)` should no longer be treated as a serious backup without fresh evidence.
- The next step is a larger aligned confirmation run on the lead setting, not a wider helper-driven search on mismatched defaults.
