# Session log — 2026-04-21: Prediction 9 calibration and score-ranking fix

## What I worked on

I took the new Prediction 9 simulator and ran the first actual calibration sweeps to see whether the selected regime and the neutral post-threshold null separate in the way the Tier-1 scope expects.

## Why this was the right frontier

The simulator already existed, so the highest-value next step was no longer architecture but measurement:

1. Find out whether the target threshold is reachable at all in a practical parameter region.
2. Check whether the post-optimal slope of `f(t)` is measurable rather than drowned in noise.
3. Check whether the nulls remain meaningfully distinct from the selected regime.

Those are exactly the calibration questions that determine whether the prototype is ready for broader sweeps.

## What I did

I ran several small sweeps in `/tmp`, varying:

- fitness threshold,
- population size,
- post-optimal window length,
- stability weight.

This produced one important methodological result almost immediately: the `--stability-weight` knob was not actually live.

## Bug found

Inside `simulations/prediction9_boolean_network.py`, network ranking was using the tuple `(correctness, stability)` instead of the already-computed weighted `score = correctness + stability_weight * stability`.

That meant:

- the calibration runs comparing different stability weights were partly misleading,
- the selected regime was not actually using the main selection rule the script claimed to expose,
- the `stability_weight` parameter was effectively ignored.

## What I changed

### `simulations/prediction9_boolean_network.py`

- Fixed the ranking key so selection now uses the weighted `score`.
- Tightened the tie-break semantics so correctness is the only tie-breaker.
- This also prevents stability from leaking into the `stability_weight = 0.0` case through a secondary ordering rule.

## What the post-fix pilots suggest

After the fix, I reran small comparison pilots. The cleanest provisional region so far is:

- `fitness_threshold = 0.85`
- `population_size = 24`
- `stability_weight = 0.3`

In that region, the selected regime tends to show a weakly positive mean post-optimal slope while the neutral post-threshold null stays near zero or negative. The separation is present but still noisy at the current replicate counts.

That means the simulator is now behaving plausibly enough to justify broader sweeps, but not stably enough to justify any substantive empirical claim yet.

## What this resolves

- The main calibration control is now actually wired into selection.
- The project has a first provisional operating region for broader sweeps.
- The simulator is in a better state for honest iteration than it was before the calibration pass.

## Best next step

Run broader post-fix sweeps centered on the current candidate region to answer three questions more cleanly:

1. How often does the selected regime reach threshold there?
2. How often is the selected post-optimal slope positive?
3. How large is the gap between selected and neutral-post-threshold slope distributions?
