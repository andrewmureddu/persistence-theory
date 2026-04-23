# Session log — 2026-04-22: Prediction 8 simulator scaffold

## What I worked on

I turned the Tier-1 Prediction 8 design from `bridges/empirical_predictions.md` A.16.11.3 into a working reduced simulator.

## Why this was the right frontier

The project already had:

1. a resolved Tier-1 scope for Predictions 8 and 9,
2. a working Prediction 9 simulator and calibration helper,
3. an explicit statement that Prediction 8 should *not* begin with a bare fixed-coefficient Bénard solver.

That made the next move unusually clear: build the cheapest same-codebase object that actually contains the slow reinforcement mechanism named in A.14.5, then test whether the ACP-style directional contrast appears at all.

## What I changed

### `simulations/prediction8_dissipative_modes.py`

- Added a pure-Python reduced mode-competition simulator for dissipative aging.
- Implemented a fast amplitude competition layer over a finite mode family under constant drive.
- Implemented a slow reinforcement field that accumulates on active modes and feeds back into their stability.
- Implemented two regimes:
  - `reinforced`
  - `no_reinforcement`
- Used paired seeds across regimes so the null and reinforced branches begin from the same settled pre-aging state rather than from unrelated initial conditions.
- Implemented the appendix's probe logic explicitly:
  - clone the current state,
  - apply a fixed library of equal-magnitude targeted kicks,
  - relax the fast dynamics with the slow reinforcement field frozen,
  - classify the recovered macroscopic pattern,
  - count distinct recovered patterns as the operational `N_epsilon(t)`.
- Implemented a lower-bound estimate of `epsilon*(t)` by sweeping kick magnitudes and finding the smallest perturbation level that ejects the incumbent pattern in a specified fraction of competitor-directed probes.
- Wrote CSV/JSON outputs:
  - `probe_metrics.csv`
  - `replicate_summaries.json`
  - `aggregate_summary.json`

### `simulations/README.md`

- Documented the new Prediction 8 simulator.
- Added an example command and listed its output artifacts.
- Updated the simulation-area next-step list so it now includes Prediction 8 calibration rather than only the Prediction 9 follow-ons.

### `STATUS.md`

- Updated the active-front entry for Prediction 8 so it now reflects that the simulator exists and the frontier has moved from implementation to calibration.
- Added a changelog entry summarizing the new scaffold and its smoke-test result.

## Verification

I ran:

1. `python3 -m py_compile Formalization/simulations/prediction8_dissipative_modes.py`
2. `python3 Formalization/simulations/prediction8_dissipative_modes.py --replicates 4 --output-dir /tmp/prediction8_smoke_final`

The smoke pilot produced the intended directional split under the current defaults:

- `reinforced`: mean accessible-mode slope `~-0.23`, negative-slope fraction `1.0`, mean `epsilon*(t)` slope `~0.043`
- `no_reinforcement`: mean accessible-mode slope `0.0`, negative-slope fraction `0.0`, mean `epsilon*(t)` slope `~0.0014`

That is not evidence yet, but it is enough to say the minimal measurement path is wired correctly and the null behaves as an actual same-codebase control rather than an unrelated baseline.

## What this resolves

- The repository now has first-pass Tier-1 simulation entry points for **both** immediate empirical targets named in A.16.11.
- Prediction 8 is no longer only a prose design; it has an executable reduced model with the intended observables.
- Future work on this front can focus on parameter robustness and measurement quality rather than on first implementation.

## Best next step

Run a small calibration helper or scripted sweep for Prediction 8 over:

1. kick magnitude / `epsilon*(t)` grid design,
2. drive asymmetry (`drive_jitter`),
3. reinforcement strength / decay,
4. competition strength and persistence strength.

The main question is not whether one tuned pilot can show the sign. It is how broad the parameter region is in which the reinforced branch keeps shrinking `N_epsilon(t)` while the no-reinforcement branch stays approximately stationary.
