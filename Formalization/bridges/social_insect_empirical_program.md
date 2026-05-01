# Social-Insect Empirical Program

*Tier-2 observational track for ACP/CDT testing*

## 1. Purpose

This note opens a publishable empirical track for the Adaptive Coherence Principle (ACP) using existing social-insect datasets. It is not a seventh formal reduction. It is a near-term observational program: use ants and honey bees as collective systems where colony-level persistence, perturbation response, communication diversity, and repertoire narrowing can be measured directly.

The central claim is modest but important:

> Social-insect datasets provide a tractable Tier-2 setting for testing whether persistent collectives preserve function by reallocating entropy across interaction, spatial, and communication channels, and whether successful collective mechanisms tend to narrow future behavioral or communicative repertoires.

If this track works, the results could stand as an independent empirical paper: ACP-derived observables applied to existing colony data, with falsifiable predictions and domain-native nulls.

## 2. Why Social Insects Are a Strong Test Bed

Ant and honey-bee colonies have a rare combination of properties:

1. The colony is a coherent macro-system with measurable collective functions.
2. Individual workers can be tracked, at least in several modern datasets.
3. Perturbations and environmental changes are often explicit: density manipulation, feeder changes, seasonal variation, resource landscapes.
4. Communication and interaction channels are measurable rather than inferred only from outcomes.
5. Rigidity can be operationalized without metaphor: concentration of interactions, spatial over-localization, reduced dance-vector diversity, narrowed follower networks, or loss of task-region transitions.

This lets the ACP empirical program move beyond synthetic simulations while still avoiding the measurement ambiguity of firms, institutions, or historical systems.

## 3. Dataset Ladder

### 3.1 Ant Density Perturbation

**Dataset.** Modlmeier et al., "Ant colonies maintain social homeostasis in the face of decreased density" (Dryad DOI `10.5061/dryad.sh4m4s6`).

**Current access.** Dryad's direct file stream currently returns a 403 response in terminal access, but the authors' companion GitHub repository includes formatted colony trophallaxis spreadsheets for the three colonies under high- and low-density treatments. Those spreadsheets support a first-pass interaction-network analysis while the full location data remains blocked.

**Existing result.** The study manipulated density in carpenter ant colonies by expanding nest space, tracked millions of ant locations and thousands of interactions, and found that colonies could preserve key interaction functions despite reduced density.

**ACP opportunity.** Reinterpret "social homeostasis" as adaptive coherence steering: a perturbation reduces one channel of coordination, and the colony compensates by reallocating movement, spatial occupancy, and interaction-network structure.

**Primary ACP questions.**

- Does interaction throughput recover after density perturbation?
- Is recovery mediated by spatial entropy, partner-network entropy, or both?
- Do colonies differ in which entropy channel absorbs the perturbation?
- Are more homeostatic colonies more spatially or socially crystallized afterward?

### 3.2 Honey-Bee Waggle Drift

**Dataset.** Dormagen et al., "Machine learning reveals the waggle drift's role in the honey bee dance communication system" (Zenodo DOI `10.5281/zenodo.7928121`).

**Existing result.** The dataset includes long-term waggle-phase detections, dance detections, follower/attendance detections, feeder logs, and individual tracks for behavior-adjacent windows.

**ACP opportunity.** Treat the dance floor as a communication state space. Dance orientations, dance locations, dancer identities, and follower networks define a repertoire whose entropy can expand, narrow, or partition over time.

**Primary ACP questions.**

- Does dance-floor spatial entropy decline as certain recruitment pathways become successful?
- Does follower-network concentration increase after high-volume or high-success dance periods?
- Do angular entropy and spatial entropy trade off, indicating adaptive repartitioning rather than simple disorder/order change?
- Does dance drift reopen communication entropy or stabilize a crystallized recruitment path?

### 3.3 Whole-Colony Bee Tracking

**Dataset.** Bozek et al., "Markerless tracking of an entire insect colony" (Zenodo DOI `10.5281/zenodo.4462215`).

**ACP opportunity.** This is larger and more expensive, but it can support whole-colony activity-mode analysis: spatial occupancy entropy, local-flow entropy, behavioral mode clustering, and accessible-mode count across recordings.

### 3.4 Co-Localized Honey-Bee Foraging

**Dataset.** Ohlinger et al., "Honey bee waggle dance data and code to analyze the spatial foraging patterns of co-localized colonies in Virginia" (Figshare / Virginia Tech, DOI `10.6084/m9.figshare.26276062`).

**ACP opportunity.** This dataset directly concerns convergence versus partitioning in foraging vectors. ACP predicts that stable persistence should not be read as simply maximizing convergence. It should involve a productive interval between incoherent scatter and over-concentrated foraging lock-in.

## 4. Observable Map

| ACP construct | Ant operationalization | Bee operationalization |
|---|---|---|
| Macrostate | colony spatial-interaction profile | hive communication / foraging profile |
| Conditional entropy proxy | spatial occupancy entropy, partner entropy, region-transition entropy | waggle-angle entropy, dance-floor entropy, dancer/follower entropy |
| Dissolution side | interaction breakdown, unstructured motion, loss of local exchange | diffuse uncoordinated dances, low follower coupling |
| Crystallization side | over-concentrated partners/regions, reduced transitions | narrowed dance vectors, fixed dance-floor zones, follower concentration |
| Adaptive coherence steering | spatial reallocation preserving interactions after perturbation | dance drift / partitioning preserving recruitment diversity |
| Perturbation | nest-space expansion, density reduction | feeder/resource variation, time-of-day/seasonal resource change |

## 5. First Publishable Tests

### SI-P1: Social Homeostasis as Entropy Reallocation

**Prediction.** After density perturbation, colonies that preserve interaction rate will show compensatory changes in spatial entropy or partner-network entropy.

**Null.** Interaction rate changes only as a function of density; entropy-channel reallocation adds no explanatory power.

**Test.** Within-colony pre/post models predicting interaction rate from density, spatial entropy, partner entropy, and their changes. With the companion trophallaxis spreadsheets, the immediate version is interaction rate versus partner/edge entropy and interaction-location entropy. The full Dryad tracking files are still needed for occupancy entropy and region-transition entropy.

### SI-P2: Communication Repertoire Narrowing After Recruitment Success

**Prediction.** In honey-bee waggle data, high dance/recruitment volume should be followed by lower communication entropy in at least one channel: dance location, advertised angle, dancer concentration, or follower network.

**First-pass surprise.** The Berlin 2019 first pass found the opposite sign in the follower channel: high follower activity per dance is followed by higher follower entropy and lower dominant-follower concentration in the next contiguous hour. This should be treated as an adaptive-coherence steering candidate rather than as a failed result: successful recruitment may reopen the follower channel instead of immediately crystallizing it.

**Null.** Dance entropy is explained by time-of-day, sampling effort, follower-event count, or feeder availability only.

**Test.** Time-binned lag models: dance volume or feeder-associated activity at time \(t\) predicts entropy/concentration at \(t+\ell\), controlling for hour/day and sample count.

### SI-P3: Productive Partitioning Rather Than Monotone Convergence

**Prediction.** Co-localized colonies should avoid both random scatter and total convergence on identical resource vectors. Successful foraging should occupy an intermediate partitioned regime.

**Null.** Optimal foraging predicts monotone convergence on the highest-value patches, or neutral sampling predicts no structured partitioning.

**Test.** Compare within-colony and between-colony vector entropy, local cluster purity, and distance distributions against shuffled colony labels.

## 6. Publication Shape

A standalone paper could be organized as follows:

1. **Theory.** Introduce ACP observables for collective systems: interaction entropy, spatial entropy, communication entropy, and repertoire concentration.
2. **Datasets.** Ant perturbation data plus one honey-bee communication dataset.
3. **Methods.** Pre-registered entropy/channel reallocation tests; time-lagged success-to-narrowing models; density/time-of-day nulls.
4. **Results.** Report whether perturbation recovery and recruitment success are associated with entropy reallocation or repertoire narrowing.
5. **Interpretation.** Social insects maintain persistence not by maximizing flexibility or order, but by staying inside a productive interval and moving entropy among channels.

## 7. Claim Boundary

This empirical track can strongly support the ACP research program, but it should not be used as a formal reduction until the following are explicit:

- a domain-native definition of colony macrostate;
- a bridge from measured entropies to \(H(m_{t+1}\mid m_t)\);
- perturbation or success variables with clear causal timing;
- null models that remove sampling, density, time-of-day, and environmental availability effects;
- colony-level replication rather than only pooled event-level statistics.

Until then, the correct status is:

> Tier-2 observational tests of ACP-derived signatures in social-insect collectives.
