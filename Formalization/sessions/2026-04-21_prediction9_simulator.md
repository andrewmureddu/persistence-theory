# Session log — 2026-04-21: Prediction 9 simulator scaffold

## What I worked on

I turned the new Tier-1 scope for Prediction 9 into a working prototype by adding the first simulation code to the repository.

## Why this was the right frontier

The previous pass resolved OP-9 at the design level and made the next move very clear:

1. Prediction 9 was the cleanest immediate implementation target because A.15 already gives the bridge variable `f(t)` directly.
2. The project had no existing simulation layout, so the cost of delaying the first prototype was mostly coordination overhead rather than theoretical uncertainty.
3. A lightweight end-to-end simulator is more useful now than a perfect one later, because it lets the project discover parameter and measurement problems while they are still cheap to fix.

## What I changed

### `simulations/README.md`

- Created a short guide for the new simulation area.
- Documented the design intent: dependency-light, laptop-verifiable, prototype-first.
- Added an example command and listed the output artifacts.

### `simulations/prediction9_boolean_network.py`

- Added a pure-Python simulator for the Tier-1 Prediction 9 pipeline.
- Implemented random Boolean networks with:
  - fixed input nodes,
  - synchronous update,
  - random wiring and Boolean tables,
  - mutation by rewiring and truth-table bit flips.
- Implemented three regimes:
  - `selected`,
  - `neutral_post_threshold`,
  - `mutation_only`.
- Implemented evaluation metrics:
  - task correctness against a fixed target function,
  - a stability score across multiple initial conditions,
  - frozen component fraction,
  - approximate Derrida parameter,
  - attractor cycle length.
- Implemented CSV/JSON output:
  - generation metrics,
  - per-replicate summaries,
  - aggregate regime summaries.
- Implemented post-optimal slope estimation for the best-network frozen fraction once the fitness threshold is reached.

## Verification

I ran two local checks:

1. `python3 -m py_compile Formalization/simulations/prediction9_boolean_network.py`
2. A small smoke run with tiny settings to verify file writing and summary generation.
3. A second low-threshold pilot run to verify that the threshold-reaching branch and post-optimal slope reporting both execute.

The low-threshold pilot produced a positive post-optimal slope in the `selected` regime, which is not evidence yet, but it does confirm that the measurement path is wired correctly.

## What this resolves

- The repository now has an actual simulation entry point rather than only a written plan.
- The Tier-1 empirical program has a concrete code path for Prediction 9.
- Future work can now focus on calibration and sweep design instead of starting from zero.

## Best next step

Run small parameter sweeps to locate a stable operating region where:

1. the `selected` regime reliably reaches threshold,
2. the post-optimal window is long enough to estimate the slope of `f(t)`,
3. the `neutral_post_threshold` and `mutation_only` controls remain meaningfully separated.
