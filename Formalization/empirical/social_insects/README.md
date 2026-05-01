# Social-Insect Empirical Track

This directory holds the Tier-2 observational program for testing ACP signatures in existing ant and honey-bee datasets. The aim is not to promote social insects to a completed formal reduction. The aim is to use unusually rich collective-behavior data as an empirical proving ground for ACP observables that are hard to measure in firms, institutions, or laboratory dissipative systems.

## Why Ants and Bees

Social insects make the ACP variables unusually concrete:

- the colony is a persistent macro-system;
- workers, foragers, task groups, dance followers, and interaction partners are measurable subsystems;
- perturbations, such as nest-space expansion or resource change, are often recorded explicitly;
- social interaction, spatial occupancy, and communication diversity are observable proxies for conditional macrostate entropy;
- rigidity can be measured as repertoire narrowing, spatial over-concentration, partner-network concentration, or loss of response diversity.

The working scientific opportunity is a publishable reanalysis: ask whether existing colony datasets show ACP-predicted signatures of perturbation absorption, adaptive coherence steering, and success-crystallization coupling.

## Initial Datasets

1. **Ant density perturbation / social homeostasis.**
   - Source: Modlmeier et al., "Ant colonies maintain social homeostasis in the face of decreased density", Dryad DOI `10.5061/dryad.sh4m4s6`.
   - Size: about 23 MB.
   - Current local access: Dryad direct download is still blocked by 403/WAF behavior, but the authors' companion GitHub repository includes the formatted colony trophallaxis spreadsheets.
   - ACP target: perturbation absorption and interaction-network entropy after nest-space expansion.
   - Primary observables: interaction rate, local density, spatial entropy, partner entropy, region-transition entropy.

2. **Honey-bee waggle drift and dance following.**
   - Source: Dormagen et al., "Machine learning reveals the waggle drift's role in the honey bee dance communication system", Zenodo DOI `10.5281/zenodo.7928121`.
   - Small first-pass files: `Berlin2019_dances.csv`, `Berlin2019_followers.csv`, `Berlin2019_waggle_phases.csv`, `Berlin2021_waggle_phases.csv`.
   - ACP target: communication-repertoire concentration, dance-floor partitioning, and success-to-recruitment crystallization.
   - Primary observables: angular entropy, spatial dance-floor entropy, dancer/follower concentration, feeder-vector concentration.

3. **Whole-colony honey-bee tracking.**
   - Source: Bozek et al., "Markerless tracking of an entire insect colony", Zenodo DOI `10.5281/zenodo.4462215`.
   - Size: about 3.3 GB, so this is a second-pass target.
   - ACP target: accessible behavioral modes and spatial/task repertoire narrowing.

4. **Co-localized honey-bee foraging / waggle bioindicator data.**
   - Source: Virginia Tech / Figshare dataset `26276062`.
   - Size: about 374 MB.
   - ACP target: colony-level foraging partitioning versus convergence, and whether successful resource exploitation narrows future advertised-resource diversity.

## Test Families

### SI-1: Perturbation Absorption In Ant Colonies

**Question.** After nest-space expansion reduces density, do colonies preserve interaction-function throughput by reorganizing spatial and partner-network structure?

**ACP readout.** A successful colony should maintain food/information interaction rate while changing the entropy allocation across space and partners. The signature is not simply "entropy high" or "entropy low"; it is constrained reallocation under perturbation.

**Primary statistics.**

- pre/post change in interaction rate;
- pre/post change in spatial occupancy entropy;
- pre/post change in partner entropy or edge entropy;
- recovery time of these observables after perturbation;
- colony-level heterogeneity in which entropy channel absorbs the perturbation.

### SI-2: Communication-Repertoire Concentration In Bees

**Question.** Do successful dance systems concentrate recruitment communication into narrower spatial, angular, feeder, or follower channels over time?

**ACP readout.** If recruitment success reinforces stable communication pathways, the colony should show increased concentration in dance floor regions, advertised vectors, dancer identities, or follower attendance networks unless environmental variation reopens the repertoire.

**Primary statistics.**

- angular entropy of waggle orientations by time window;
- spatial entropy of dance-floor locations by time window;
- concentration of dances by dancer, feeder, or follower;
- follower-network entropy conditional on dancer or feeder;
- lagged relationship between dance volume/recruitment and later repertoire narrowing.

### SI-3: Collective Early-Warning Signals

**Question.** Do colonies approaching rigid collective organization show increasing autocorrelation, decreasing response variance, or slower response to novel perturbations?

**ACP readout.** This is the social-insect version of Prediction 6. It is most feasible in datasets with explicit perturbations or long time series.

## Analysis Conventions

- Treat each colony, hive, or recording as the independent unit when possible.
- Prefer within-colony before/after or time-lagged tests over pooled correlations.
- Report both entropy and concentration because ACP's crystallization boundary is about loss of accessible futures, not raw disorder.
- Always compare against a mechanical null: density-only, time-of-day-only, or sampling-rate-only models where available.
- Mark any result as "Tier-2 observational support" unless the perturbation is controlled and the ACP observable is intervention-defined.

## Scripts

- `social_insect_observables.py`: dependency-free first-pass summaries for waggle-phase and interaction-style CSV files.
- `bee_waggle_coupling_analysis.py`: first-pass coupling analysis for Berlin 2019 dance and follower CSVs. Lag models now default to clock-contiguous windows; use `--lag-mode active-window` only to reproduce the older exploratory next-active-window pass.
- `bee_waggle_controlled_lag_analysis.py`: residualized lag diagnostics for the bee coupling result, with baseline outcome, current dance count, next-window sampling effort, hour-of-day, and optional day fixed effects.
- `ant_trophallaxis_summary.py`: dependency-free first-pass summaries for the Modlmeier companion trophallaxis spreadsheets.

## Current First-Pass Result

See `first_pass_results_2026-05-01.md`.

The corrected Berlin 2019 waggle-dance pass uses true contiguous one-hour lags. Higher follower activity per dance predicts higher follower entropy and lower dominant-follower concentration one hour later. This is not a simple crystallization result; it suggests a possible adaptive coherence steering signature in which successful recruitment broadens the follower channel. Basic sampling-effort controls attenuate the effect, so the honest next step is a rarefaction or identity-shuffle null rather than claiming publication-grade confirmation.

The first ant pass is now real rather than blocked: the companion GitHub trophallaxis spreadsheets yield 3,262 deduplicated interaction events across three colonies. Under low density, interaction-location entropy rises in all three colonies, while interaction throughput rises in colonies 1 and 2 and falls modestly in colony 3. That is a useful ACP-shaped asymmetry, but the full Dryad location data is still needed for spatial occupancy and transition-entropy tests.
