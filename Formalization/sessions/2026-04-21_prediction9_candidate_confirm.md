# Session log — 2026-04-21: Prediction 9 candidate confirmation

## What I worked on

I took the top region from the broader ranked sweep and ran a larger-replicate confirmation pass to see which candidates survive once the sample is no longer tiny.

## Why this mattered

The broader grid had finally produced promising parameter settings, but they were still based on only four replicates per configuration. At that stage the main risk was obvious:

1. a lucky small-sample separation could masquerade as a stable calibration win,
2. the wrong default could get locked in simply because it looked best first,
3. the project would then waste time calibrating around a false lead.

So the correct next move was confirmation, not expansion.

## Confirmation sweep

I ran a focused follow-up at:

- fitness threshold: `0.85`
- population sizes: `24`, `28`
- stability weights: `0.2`, `0.4`
- replicates per configuration: `8`

This directly tests the four most relevant candidates after the broader sweep.

## Result

The earlier ranking changed in a meaningful way.

### Best confirmed setting

- threshold: `0.85`
- population size: `28`
- stability weight: `0.2`
- selected threshold-reaching fraction: `0.75`
- neutral threshold-reaching fraction: `0.75`
- selected mean post-optimal slope: about `0.00829`
- neutral mean post-optimal slope: about `0.00055`
- slope gap: about `0.00774`
- positive-fraction gap: about `0.30`

### Secondary setting

- threshold: `0.85`
- population size: `24`
- stability weight: `0.4`
- slope gap: about `0.00566`
- positive-fraction gap: about `0.15`

### Failed small-sample winners

Two earlier small-sample candidates did not survive the confirmation pass:

- `(0.85, 24, 0.2)` flipped negative
- `(0.85, 28, 0.4)` flipped clearly negative

That is a useful result, not a setback. It means the confirmation pass did exactly what it was supposed to do: stop the project from overcommitting to unstable candidates.

## Interpretation

The calibration picture is now cleaner than it was before:

- there is one lead candidate,
- one weaker backup,
- and two discarded false leads.

At the same time, the lead candidate is still only modestly separated. The next question is no longer "which broad region should we look at?" but "is the current lead genuinely stable, or is the entire proxy still too noisy?"

## Best next step

Inspect the replicate-level summaries for `(0.85, 28, 0.2)` and decide between two paths:

1. scale replicates again if the replicate distribution looks coherent, or
2. revisit the target-function / stability proxy if the distribution is still too erratic to justify more brute-force sampling.
