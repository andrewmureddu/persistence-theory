# Session log — 2026-04-21: Prediction 9 broader ranked sweep

## What I worked on

I let the broader helper-driven post-fix sweep finish and used its ranked summary table to replace the earlier, weaker targeted-grid picture.

## Why this mattered

The targeted sweep was useful as a workflow test, but it was too small to say much. The broader grid was the first calibration pass large enough to answer a better question:

1. Is there any parameter region where the selected regime separates clearly from the neutral post-threshold null?
2. If so, which settings deserve larger-replicate confirmation rather than more blind searching?

## Sweep definition

The completed grid covered:

- fitness thresholds: `0.82`, `0.85`, `0.88`
- population sizes: `24`, `28`
- stability weights: `0.2`, `0.3`, `0.4`
- replicates per configuration: `4`

The helper ranked each configuration by:

1. slope gap,
2. positive-fraction gap,
3. selected threshold-reaching fraction.

## Main result

The broad sweep did produce genuinely promising candidates.

### Top candidate

- threshold: `0.85`
- population size: `28`
- stability weight: `0.4`
- selected threshold-reaching fraction: `1.0`
- neutral threshold-reaching fraction: `1.0`
- selected mean post-optimal slope: about `0.0552`
- neutral mean post-optimal slope: about `-0.0025`
- slope gap: about `0.0577`

### Second candidate

- threshold: `0.85`
- population size: `24`
- stability weight: `0.2`
- selected threshold-reaching fraction: `0.75`
- neutral threshold-reaching fraction: `0.5`
- selected mean post-optimal slope: about `0.0566`
- neutral mean post-optimal slope: about `0.00129`
- slope gap: about `0.0553`

## Interpretation

This is materially better than the earlier targeted-grid result, which only found a barely positive best slope gap.

At the same time, the result is still not strong enough to freeze a default configuration:

1. replicate counts are still small,
2. the top configuration's positive-slope fractions are mixed rather than cleanly separated,
3. some neighboring settings remain weak or negative.

So the right conclusion is:

- the helper-driven workflow is now paying off,
- a real candidate region has appeared,
- larger-replicate confirmation is the next step before any claim of stable calibration.

## Best next step

Rerun the top two configurations with larger replicate counts and inspect replicate-level slope distributions directly. The question is no longer "is there any promising region at all?" but "does the apparent separation survive once the sample is no longer tiny?"
