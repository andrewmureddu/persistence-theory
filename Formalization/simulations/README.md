# Simulations

This directory holds the first computational prototypes for the ACP empirical program.

## Current prototype

- `prediction8_dissipative_modes.py`
  - First-pass Tier-1 simulator for **Prediction 8: Dissipative Aging**.
  - Implements the reduced dissipative-mode competition model scoped in `bridges/empirical_predictions.md` A.16.11.3.
  - Tracks the probe-based accessible mode count `N_epsilon(t)` and the perturbation-threshold estimate `epsilon*(t)` under two regimes:
    - `reinforced`
    - `no_reinforcement`
- `prediction9_boolean_network.py`
  - First-pass Tier-1 simulator for **Prediction 9: Regulatory Network Aging**.
  - Implements an evolutionary random Boolean network (RBN) ensemble under a fixed target function.
  - Tracks the frozen component fraction `f(t)`, an approximate Derrida parameter `lambda(t)`, and a simple attractor statistic through the post-optimality window described in `bridges/empirical_predictions.md` A.16.11.2.
  - Includes three regimes:
    - `selected`
    - `neutral_post_threshold`
    - `mutation_only`
- `prediction9_calibration_sweep.py`
  - Grid sweep helper for Prediction 9 calibration.
  - Inherits the canonical defaults from `prediction9_boolean_network.py` unless overridden, so sweep and direct-run results stay comparable.
  - Runs the simulator over a small threshold / population / stability-weight grid.
  - Writes ranked configuration summaries so the selected-vs-neutral slope separation can be compared systematically.
- `prediction5_success_crystallization_analysis.py`
  - Analysis helper for the Kauffman-domain version of **Prediction 5: Success-Crystallization Coupling**.
  - Reads `generation_metrics.csv` from the Prediction 9 simulator.
  - Reports within-replicate correlations between correctness and cumulative frozen-fraction increase, plus lagged forward and reverse readouts.
- `prediction8_calibration_sweep.py`
  - Grid sweep helper for Prediction 8 calibration.
  - Runs the reduced dissipative-mode simulator across probe-kick magnitudes, drive asymmetry, and reinforcement-feedback strengths.
  - Writes ranked configuration summaries for the reinforced-vs-null accessible-mode slope gap and epsilon-threshold slope gap.
- `partition_selector_toy.py`
  - Dependency-free toy checker for `bridges/partition_generating_functors.md`.
  - Compares a fully symmetric finite graph, where the Fiedler selector is degenerate and no nontrivial partition is selected, against a two-community graph, where the spectral selector recovers the two-block partition.

## Design intent

This is a **prototype**, not a publication-scale simulator. The defaults are chosen so the full pipeline can be verified quickly on a laptop:

- modest network size,
- modest population size,
- short generation counts,
- no external dependencies beyond the Python standard library.

Once the pipeline is behaving sensibly, the natural next steps are:

1. increase the replicate count and post-optimality window,
2. calibrate the Prediction 8 kick library and reduced-mode parameters against wider sweeps,
3. tune the Prediction 9 stability weighting and mutation rates,
4. decide whether the attractor and frozen-fraction estimators should be made more expensive,
5. extend the same code path to the Kauffman-domain version of Prediction 5.

## Example

From the repository root:

Prediction 8:

```bash
python3 Formalization/simulations/prediction8_dissipative_modes.py \
  --replicates 4 \
  --output-dir Formalization/simulations/output/prediction8_pilot
```

The script writes:

- `probe_metrics.csv`
- `replicate_summaries.json`
- `aggregate_summary.json`

Prediction 9:

```bash
python3 Formalization/simulations/prediction9_boolean_network.py \
  --replicates 3 \
  --population-size 24 \
  --max-generations 80 \
  --post-optimal-generations 40 \
  --output-dir Formalization/simulations/output/prediction9_pilot
```

The script writes:

- `generation_metrics.csv`
- `simulation_config.json`
- `replicate_summaries.json`
- `aggregate_summary.json`

Prediction 5 analysis, using a Prediction 9 generation-metrics file:

```bash
python3 Formalization/simulations/prediction5_success_crystallization_analysis.py \
  --input-csv Formalization/simulations/output/prediction9_pilot/generation_metrics.csv \
  --output-dir Formalization/simulations/output/prediction5_from_prediction9_pilot \
  --lag 5
```

The analyzer writes:

- `replicate_analysis.csv`
- `analysis_parameters.json`
- `aggregate_analysis.json`

## Sweep example

```bash
python3 Formalization/simulations/prediction9_calibration_sweep.py \
  --replicates 4 \
  --fitness-thresholds 0.82 0.85 0.88 \
  --population-sizes 24 \
  --stability-weights 0.2 0.3 \
  --output-dir Formalization/simulations/output/prediction9_calibration
```

The sweep helper writes:

- `config_summaries.csv`
- `config_summaries.json`
- `replicate_summaries.json`
- `sweep_parameters.json`

Prediction 8 calibration:

```bash
python3 Formalization/simulations/prediction8_calibration_sweep.py \
  --replicates 8 \
  --probe-kicks 0.42 0.54 0.66 \
  --drive-jitters 0.0 0.01 0.03 \
  --reinforcement-feedbacks 0.6 1.2 1.8 \
  --output-dir Formalization/simulations/output/prediction8_calibration
```

The sweep helper writes:

- `config_summaries.csv`
- `config_summaries.json`
- `replicate_summaries.json`
- `sweep_parameters.json`

Partition selector toy:

```bash
python3 Formalization/simulations/partition_selector_toy.py
```

The default smoke check prints no selected partition for the fully symmetric case and the split `[0, 1, 2, 3] | [4, 5, 6, 7]` for the two-community case.
