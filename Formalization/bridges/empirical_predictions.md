**Appendix A.16: Empirical Predictions and Experimental Protocols**

*Anti-Crystallization Principle — Formalized Testable Predictions*

## **A.16.1 Introduction**

This appendix formalizes the seven testable predictions stated in Section 6 of the main paper. For each prediction, we specify: (i) the measurable quantities derived from the ACP formalism, (ii) the null hypothesis that a weaker or alternative framework would predict, (iii) a concrete experimental or observational protocol, (iv) the statistical test and expected effect, and (v) the domain(s) and data sources where the test is most tractable. We also derive three additional predictions from the unification reductions (Appendices A.11–A.15) that are novel to the ACP and not present in any of the five parent frameworks.

The goal is to move the ACP from a theoretical unification to an empirically falsifiable framework. Each prediction is stated in a form that could be refuted by data—the hallmark of a scientific rather than merely mathematical result.

**Notation. **We use the notation established in the main paper and appendices. In particular: H(m′ | m) denotes conditional macrostate entropy, C and D denote the crystallization and dissolution boundaries respectively, ε*(t) denotes the critical perturbation threshold at time t, and the productive interval is the set of macrostates m such that m ∉ C and m ∉ D. We write σ for entropy production rate (Prigogine domain), f(t) for frozen component fraction (Kauffman domain), F for variational free energy (Friston domain), Rδ for quantum redundancy (Zurek domain), and H(x) for strategy entropy (Bergstrom–Lachmann domain).

## **A.16.2 Prediction 1: Boundary Symmetry**

### **A.16.2.1 Formal Statement**

**Prediction 1 (Boundary Symmetry). **Let S be a population of persistent dynamical systems in domain Ω. Let NC denote the number of systems that cease future-bearing dynamics by approaching C (crystallization failures), and ND the number approaching D (dissolution failures), over observation period [0, T]. Then:

*N*C* / N*D = Θ(1)

That is, the ratio of crystallization failures to dissolution failures is of order unity—neither failure mode dominates by more than a small constant factor.

### **A.16.2.2 Null Hypothesis**

Standard frameworks predict asymmetry. The second law of thermodynamics predicts dissolution as the dominant failure mode. Organizational theory focuses on environmental disruption (dissolution). The null hypothesis is NC / ND ≪ 1: crystallization failures should be rare relative to dissolution failures.

### **A.16.2.3 Experimental Protocol**

**Domain 1: Evolutionary biology. **Measure extinction causes in the fossil record. Classify extinctions as (a) environmental catastrophe / resource collapse (dissolution) or (b) over-specialization / loss of adaptive capacity (crystallization). Use clade-level data from the Paleobiology Database (PBDB). Operational criterion: a lineage that narrows its niche width (measured by geographic range, dietary breadth, or morphological disparity) in the 5 Myr preceding extinction is classified as crystallization; a lineage maintaining or expanding niche width is classified as dissolution. Time period: Phanerozoic (541 Ma–present).

**Domain 2: Firm dynamics. **Use Compustat/CRSP data for publicly traded firms. Classify firm deaths as (a) bankruptcy/insolvency due to market disruption, demand collapse, or liquidity crisis (dissolution) or (b) acquisition/decline due to failure to adapt, loss of market relevance despite adequate resources (crystallization). Operational criteria: firms dying with above-median cash reserves and below-median R&D diversity are classified as crystallization failures. Sample: all US-listed firms 1950–2020.

**Domain 3: Biological cells. **In cell biology, cell death occurs via necrosis (dissolution of cellular integrity—the D boundary) or senescence/terminal differentiation (crystallization of cellular program—the C boundary). Use tissue-level data from aging studies. Measure the ratio of senescent cells to necrotic cells across tissue types and ages.

### **A.16.2.4 Statistical Test**

Two-sided binomial test against the null H0: pC ≤ 0.1 (crystallization accounts for ≤10% of failures). The ACP predicts pC ∈ [0.2, 0.8]. Reject the null at α = 0.01 if the observed proportion of crystallization failures exceeds 0.15. Power analysis: with n = 200 system failures, we have >99% power to detect pC = 0.3 against the null of pC = 0.1.

## **A.16.3 Prediction 2: Dual Critical Slowing Down**

### **A.16.3.1 Formal Statement**

**Prediction 2 (Dual Critical Slowing Down). **Let τ(m) denote the recovery time of a system at macrostate m following a small perturbation δm. Let dC(m) and dD(m) denote distances (in macrostate space) from the crystallization and dissolution boundaries respectively. Then:

τ(m) ~ [min(dC(m), dD(m))]⁻¹

Recovery time diverges as the system approaches *either* boundary. Near D, this is the well-known critical slowing down (Scheffer et al. 2009). Near C, this is a novel prediction: recovery time from *novel* perturbations (those outside the system’s reinforced repertoire) increases as crystallization proceeds, even though recovery from *familiar* perturbations remains fast or accelerates.

### **A.16.3.2 Null Hypothesis**

Standard critical slowing down theory predicts τ → ∞ only near phase transitions or D-type boundaries. The null hypothesis is that highly ordered (near-C) systems should exhibit *faster* recovery times due to strong restoring forces. The ACP’s novel prediction is the distinction between familiar and novel perturbation responses near C.

### **A.16.3.3 Experimental Protocol**

**Domain: Regulatory gene networks (Kauffman). **Use Boolean network simulations (N = 100–1000 nodes, K = 2–4) under selection for a target function. Measure: (a) frozen component fraction f(t) as a proxy for distance to C; (b) Derrida parameter λ as a conditional entropy proxy; (c) recovery time from random single-node perturbations (classified as ‘familiar’ if the perturbed node is in the frozen component, ‘novel’ if unfrozen). Run M = 1000 independent evolutionary trajectories. Track τfamiliar and τnovel as functions of f(t).

**Domain: Organizational behavior. **Longitudinal data on firm response times. Measure how quickly firms respond to (a) demand fluctuations within their core market (familiar perturbations) versus (b) technological disruptions from adjacent industries (novel perturbations). Use event-study methodology around identifiable disruption events. Track response latency as a function of firm age and organizational complexity (proxies for dC).

### **A.16.3.4 Statistical Test**

Mixed-effects regression of log(τ) on dC, perturbation type (familiar/novel), and their interaction. The ACP predicts a significant negative interaction: the coefficient on dC × novel should be positive (novel perturbation recovery time increases as dC decreases), while the coefficient on dC × familiar should be non-positive. Test at α = 0.01 with Bonferroni correction for multiple domains.

## **A.16.4 Prediction 3: Perturbation Absorption Scaling**

### **A.16.4.1 Formal Statement**

**Prediction 3 (Perturbation Absorption Scaling). **The maximum perturbation magnitude εmax(m) that a system at macrostate m can absorb while retaining future-bearing dynamics satisfies:

εmax(m) ∝ min(dC(m), dD(m))

Systems near the center of the productive interval can absorb larger perturbations than systems near either boundary.

### **A.16.4.2 Experimental Protocol**

**Domain: Dissipative structures (Prigogine). **Use Bénard convection cells or Belousov–Zhabotinsky reactions. Vary the driving parameter (temperature gradient for Bénard, reagent concentration for BZ) to position the system at different distances from the ordered (C) and disordered (D) regimes. Apply controlled perturbations (mechanical vibration for Bénard, local injection of reagent for BZ) of varying magnitude. Measure the critical perturbation size that disrupts the pattern permanently. Map εmax as a function of the driving parameter.

**Domain: Ecosystems. **Use the resilience framework (Holling 1973). Measure perturbation tolerance of ecosystems at varying distances from monoculture (C) and fully random species assemblages (D). Operational metric: Shannon diversity index as proxy for position in the productive interval; perturbation magnitude measured by species removal fraction that triggers regime shift.

### **A.16.4.3 Statistical Test**

Quadratic regression of εmax on boundary distance. The ACP predicts a concave parabola (maximum absorption at the center, declining toward both boundaries). The null hypothesis (standard resilience theory) predicts a monotonic relationship: systems further from D are more resilient, with no C-boundary effect. Test via comparison of adjusted R² between concave-parabola and monotone-increasing models. Use F-test for nested model comparison at α = 0.01.

## **A.16.5 Prediction 4: Voluntary Restraint and Longevity**

### **A.16.5.1 Formal Statement**

**Prediction 4 (Voluntary Restraint). **Among systems with the capacity to close their own productive interval (i.e., systems whose self-reinforcing mechanisms could, if unchecked, drive them to C), the longest-persisting systems will be those exhibiting maximal *voluntary restraint*—defined as the ratio of potential crystallization rate to actual crystallization rate. Let R(S) = (dH/dt)potential / (dH/dt)actual denote the restraint ratio. Then system longevity L(S) satisfies:

L(S) ∝ R(S)

### **A.16.5.2 Experimental Protocol**

**Domain: Institutional longevity. **Measure dominance concentration (HHI or equivalent) across organizations with varying lifespans. The ACP predicts that long-lived institutions (e.g., the Catholic Church, the British monarchy, certain Japanese firms) will exhibit lower dominance concentration relative to their peak capacity than shorter-lived institutions of comparable peak power. Operational metric: peak-to-average dominance ratio over the institution’s lifespan. Data sources: political science databases (Polity IV/V), corporate databases (Compustat), religious institution records.

**Domain: Biological regulation. **In multicellular organisms, apoptosis and immune tolerance represent voluntary restraint—mechanisms that prevent any single cell lineage from dominating. Compare cancer suppression mechanisms (p53 pathway activity, telomere regulation) across species with varying lifespans. The ACP predicts that longer-lived species invest proportionally more in crystallization-preventing mechanisms (tumor suppressors, immune diversity maintenance) relative to dissolution-preventing mechanisms (DNA repair, antioxidant defense).

### **A.16.5.3 Statistical Test**

Rank correlation (Spearman’s ρ) between R(S) and L(S), controlling for system size and environmental variability. The ACP predicts ρ > 0. The null hypothesis (power predicts longevity) predicts no relationship or negative ρ after controlling for peak capacity. Test at α = 0.01 with permutation-based p-values to avoid distributional assumptions.

## **A.16.6 Prediction 5: Success–Crystallization Coupling**

### **A.16.6.1 Formal Statement**

**Prediction 5 (Success–Crystallization Coupling). **Let Ψ(t) denote a system’s cumulative success metric (persistence duration, competitive fitness, resource accumulation). Let ΔH(t) = H(m′ | m)|t=0 − H(m′ | m)|t denote the cumulative decrease in conditional macrostate entropy. The Crystallization Drift Theorem (Theorem 4.19) implies:

Corr(Ψ(t), ΔH(t)) > 0

More successful systems crystallize faster. This is the formal content of the ‘competency trap’ (Levitt & March 1988) derived as a theorem.

### **A.16.6.2 Experimental Protocol**

**Domain: Kauffman networks. **Simulate N = 500 Boolean networks under selection for a specified function over T = 10,000 generations. Fitness metric: fraction of correct input–output mappings. Crystallization metric: frozen component fraction f(t). Measure Corr(fitness at generation t, Δf from generation 0 to t). Run M = 500 independent replicates to estimate the distribution of correlations.

**Domain: Corporate strategy. **Use longitudinal panel data on firm performance and strategic flexibility. Success metric: cumulative abnormal returns over 5-year windows. Crystallization proxy: declining patent class diversity, shrinking product line breadth, increasing market concentration of revenue. Measure the time-lagged correlation between 5-year cumulative returns and subsequent 5-year change in strategic diversity metrics.

**Domain: Neural systems (Friston). **In reinforcement learning agents, measure the relationship between cumulative reward (success) and policy entropy (conditional macrostate entropy proxy). The ACP predicts that agents that accumulate more reward will exhibit faster policy entropy decline—a formal version of the exploitation–exploration tradeoff that emerges as a theorem rather than a hyperparameter choice.

### **A.16.6.3 Statistical Test**

Panel vector autoregression (VAR) with Granger causality tests. Test whether past success Granger-causes future crystallization (decline in diversity/entropy). The ACP predicts unidirectional Granger causality from success to crystallization, not vice versa. Use Akaike Information Criterion for lag selection. Apply Newey–West robust standard errors for heteroskedasticity. Significance threshold: α = 0.01 with Bonferroni correction across domains.

## **A.16.7 Prediction 6: Crystallization Early Warning Signals**

### **A.16.7.1 Formal Statement**

**Prediction 6 (Crystallization Early Warning Signals). **As a system approaches the crystallization boundary C, the following three quantities exhibit monotonic trends:

(i) Autocorrelation of organizational patterns, ρ1(t) → 1;

(ii) Variance of responses to perturbation, Var(δm), decreasing;

(iii) Recovery time from novel perturbations, τnovel(t) → ∞.

These three signals form a *crystallization early warning index* (CEWI):

CEWI(t) = w1ρ1(t) + w2[1 − Var(δm)(t)/Var(δm)(0)] + w3log τnovel(t)

where the weights wi are calibrated empirically. The ACP predicts that CEWI precedes system failure by crystallization with lead time proportional to the remaining distance to C.

### **A.16.7.2 Experimental Protocol**

**Domain: Prigogine systems. **In Bénard convection, gradually reduce the temperature gradient (driving the system toward the ordered/conductive regime). Measure: (i) autocorrelation of convection roll positions over time; (ii) variance of roll displacement after mechanical perturbation; (iii) recovery time after displacing one roll. The ACP predicts all three signals will track the approach to the purely conductive (crystallized) state.

**Domain: Corporate failure. **Using quarterly data for firms that eventually failed due to rigidity (crystallization deaths, as classified in Prediction 1), compute the CEWI in rolling 20-quarter windows preceding failure. Compare to matched control firms that survived or failed by dissolution. The ACP predicts CEWI trends upward specifically for crystallization-type failures and not for dissolution-type failures.

### **A.16.7.3 Statistical Test**

ROC analysis of CEWI as a classifier for crystallization-type failure, with the standard dissolution early-warning index (Scheffer et al. 2009) as a comparison. The ACP predicts: (a) CEWI has AUC > 0.7 for crystallization failures; (b) the dissolution early-warning index has AUC ≈ 0.5 (no discriminative power) for crystallization failures; (c) the two indices are complementary—their combination outperforms either alone for all-cause failure prediction. Test (c) via DeLong’s test for comparison of AUC values at α = 0.01.

## **A.16.8 Prediction 7: Characteristic Reformation Timescale**

### **A.16.8.1 Formal Statement**

**Prediction 7 (Reformation Timescale). **If the critical perturbation threshold ε*(t) is monotonically non-decreasing under the Crystallization Drift Theorem, and the maximum environmentally available perturbation εenv is bounded, then there exists a characteristic time T* satisfying:

ε*(T*) = εenv

Beyond T*, self-reformation (endogenous correction without system replacement) becomes increasingly improbable. The ACP predicts that across domains, the distribution of organizational ages at reformation should be right-truncated at a domain-specific T*, beyond which replacement (death and rebirth) dominates reformation (internal restructuring).

### **A.16.8.2 Experimental Protocol**

**Domain: Political institutions. **Compile data on major institutional reforms (constitutional revisions, regime changes) versus institutional replacements (revolutions, state collapses) as a function of institutional age. Data sources: Polity V, Varieties of Democracy (V-Dem). For each polity, classify transitions as reformation (continuity of institutional identity) or replacement (discontinuity). Plot the reformation-to-replacement ratio as a function of institutional age in 50-year bins.

**Domain: Religious organizations. **Track major doctrinal/structural reforms versus schisms/new movements as a function of organizational age. Historical data for Christianity, Islam, Buddhism, Hinduism. Classify changes as internal reformation versus external replacement. The ACP predicts that the reformation/replacement ratio declines with organizational age, crossing unity at a characteristic T*.

**Domain: Biological species. **In paleontology, compare within-lineage morphological innovation rates versus speciation (lineage splitting) rates as a function of lineage age. Use trait disparity indices from morphometric databases. The ACP predicts declining within-lineage innovation relative to speciation as lineage age increases.

### **A.16.8.3 Statistical Test**

Survival analysis with competing risks (reformation and replacement as competing events). Use a Cox proportional hazards model with age as the primary covariate. The ACP predicts: (a) the hazard ratio for replacement relative to reformation increases with age; (b) there exists a crossover age T* where the two hazard functions intersect. Estimate T* with 95% confidence interval using bootstrap resampling. The null hypothesis (no age effect on the reformation/replacement ratio) predicts a constant hazard ratio.

## **A.16.9 Novel Predictions from the Unification Reductions**

The five formal reductions (A.11–A.15) yield predictions that are novel to the ACP—they are not present in any of the five parent frameworks and emerge only through the unifying lens.

### **A.16.9.1 Prediction 8: Dissipative Aging (from A.14)**

**Prediction 8 (Dissipative Aging). **A dissipative structure maintained under constant boundary conditions will exhibit a monotonic decrease in the number of accessible dissipative modes N(m)(t) over time (Proposition A.14.5). Equivalently, the set of distinct spatiotemporal patterns the structure can exhibit narrows over time, even with no change in the driving force.

**Protocol: **Maintain Bénard convection cells at a fixed Rayleigh number above the convective threshold for extended periods (103–104 characteristic times). Periodically apply identical perturbations and count the number of distinct recovery patterns. The ACP predicts this count decreases over time. Compare to the null prediction of a time-independent pattern repertoire under constant boundary conditions.

**Statistical test: **Poisson regression of pattern count on time, with the ACP predicting a negative time coefficient (βtime < 0). Test at α = 0.01.

### **A.16.9.2 Prediction 9: Regulatory Network Aging (from A.15)**

**Prediction 9 (Regulatory Network Aging). **Under sustained selection for a fixed function, Boolean regulatory networks will exhibit monotonic increase in frozen component fraction f(t) even after the target function is achieved (Proposition A.15.5). Selection for function is selection for rigidity: the freezing continues as a drift, not as optimization.

**Protocol: **Evolve random Boolean networks (N = 200, K = 3) under selection for a target Boolean function. After the target is achieved (fitness ≥ 0.99), continue selection for an additional 10,000 generations with no fitness gain possible. Track f(t) during this ‘post-optimality’ phase. The ACP predicts continued increase in f(t) after optimality is reached. Compare to the null prediction that f(t) stabilizes once the fitness optimum is achieved.

**Statistical test: **Linear regression of f(t) on generation number in the post-optimality phase. The ACP predicts a positive slope (β > 0). Replicate across M = 500 independent evolutionary runs. Report the fraction of runs with β > 0 at α = 0.05 (one-sided). Under the null, this fraction should be ≤0.05.

### **A.16.9.3 Prediction 10: Cross-Domain Drift Rate Universality**

**Prediction 10 (Drift Rate Universality). **If the common CDT template recovered by the current formal reductions is quantitatively real and not merely qualitative, then the *normalized* drift rate—the rate of conditional entropy decrease per self-reinforcing mechanism per characteristic time—should be of the same order across the five currently operationalized reduced domains. Define the normalized drift rate:

γ = |ΔH(m′ | m)| / (k · τchar)

where k is the number of identified self-reinforcing mechanisms and τchar is the domain-specific characteristic time (reaction time for Prigogine, generation time for Kauffman, model update time for Friston, decoherence time for Zurek, selective generation for Bergstrom–Lachmann). The ACP predicts that γ values across the five domains cluster within two orders of magnitude, despite the domains spanning >40 orders of magnitude in physical timescale.

**Protocol: **Measure the conditional entropy decrease rate in each of the five domains using domain-appropriate metrics (N(m) for Prigogine, f(t) for Kauffman, policy entropy for Friston, redundancy Rδ for Zurek, strategy entropy for Bergstrom–Lachmann). Normalize by mechanism count and characteristic time. Compare the resulting γ values.

**Statistical test: **Coefficient of variation (CV) of log(γ) across domains. The ACP predicts CV < 1 (values cluster within a few orders of magnitude). The null hypothesis (domain-specific dynamics with no shared normalized drift template) predicts CV ≫ 1. This is the most ambitious prediction—it would, if confirmed, provide the strongest evidence that the reduced cases share one recurring drift law rather than only a loose family of structural parallels.

## **A.16.10 Summary of Predictions and Protocols**

| **#** | **Prediction** | **Key Quantity** | **Primary Domain** | **Statistical Test** | **Difficulty** |
| --- | --- | --- | --- | --- | --- |
| 1 | Boundary Symmetry | N_C / N_D ratio | Paleobiology, Firms | Binomial test | Moderate |
| 2 | Dual Critical Slowing Down | τ_familiar vs τ_novel | Boolean networks, Firms | Mixed-effects regression | Moderate |
| 3 | Perturbation Absorption | ε_max vs boundary distance | Bénard cells, Ecosystems | Quadratic regression | Tractable |
| 4 | Voluntary Restraint | Restraint ratio R(S) | Institutions, Cancer biology | Rank correlation | Hard |
| 5 | Success–Crystallization | Corr(Ψ, ΔH) | Networks, Firms, RL agents | Panel VAR / Granger | Moderate |
| 6 | Crystallization EWS | CEWI index | Prigogine systems, Firms | ROC / AUC analysis | Moderate |
| 7 | Reformation Timescale | T* crossover age | Political, Religious, Species | Competing risks survival | Hard |
| 8 | Dissipative Aging | Pattern count N(m)(t) | Bénard cells | Poisson regression | Tractable |
| 9 | Regulatory Network Aging | Post-optimal f(t) | Boolean networks | Linear regression | Tractable |
| 10 | Drift Rate Universality | Normalized γ | All five domains | CV of log(γ) | Very Hard |

## **A.16.11 Discussion**

The ten predictions range from immediately tractable (Predictions 3, 8, 9—achievable with existing simulation or standard experimental infrastructure) to deeply ambitious (Prediction 10—requiring coordinated measurement across five domains spanning quantum to institutional scales). We recommend the following priority ordering for initial empirical investigation.

To make the tier language operational rather than rhetorical, we define the tiers by the *cheapest decisive falsification path* for the prediction:

**Tier 1 (immediate, computational).** A closed in silico experiment suffices. All state variables, interventions, and readouts are generated inside the simulator; the ACP observable is computed directly from the simulated trajectory; the null can be implemented in the same codebase by removing or freezing the candidate self-reinforcing mechanism; and a workstation-scale parameter sweep is enough to determine the sign of the effect.

**Tier 2 (near-term, observational).** Existing empirical datasets suffice, but the ACP observables must be recovered indirectly through operational proxies, labeling rules, or event classification. No new laboratory apparatus is required, but the main difficulty is measurement design rather than simulation design.

**Tier 3 (medium-term, experimental).** A decisive test requires new controlled physical experiments in which the perturbation protocol or boundary conditions are actively imposed. Existing data are insufficient because the relevant ACP quantities are intervention-defined.

**Tier 4 (long-term, coordinated).** The test requires cross-domain measurement programs, long historical curation, or coordinated data collection across multiple communities. The difficulty is organizational and comparative, not only computational.

Under this definition, the immediate Tier-1 targets in v10 are specifically **Prediction 8 (Dissipative Aging, A.16.9.1)** and **Prediction 9 (Regulatory Network Aging, A.16.9.2)**. Prediction 5 in the Kauffman domain remains a natural extension once the Prediction 9 simulator exists, but it is not required for the first pass.

### **A.16.11.1 First-pass Tier-1 objective**

The first Tier-1 pass should aim at **directional falsification** of the CDT's monotone-drift claim in the two domains where the bridge variables are already explicit: accessible dissipative mode count $N(m)$ in the Prigogine reduction and frozen component fraction $f(t)$ in the Kauffman reduction. The goal of the first pass is not full domain realism. It is to build the cheapest simulation object that still contains the specific self-reinforcing mechanism identified in A.14.5 or A.15.5 and then ask whether the ACP-predicted monotone drift appears.

### **A.16.11.2 Prediction 9: minimal computational pipeline**

For Prediction 9, the bridge variable is already operational in a standard evolutionary Boolean-network model, so the first pass can be close to the appendix protocol:

(i) **Model class.** Use an ensemble of random Boolean networks evolved under a fixed target Boolean function, with network size $N$ and connectivity $K$ held fixed within a run and initial bias chosen near the critical surface so that the starting ensemble lies inside the productive interval rather than already deep in the ordered regime.

(ii) **Selection rule.** Evolve each population until the target function is achieved to a high threshold (e.g. fitness at or above the appendix's 0.99 benchmark), then continue selection with the target and fitness rule unchanged for a long post-optimality window. This isolates crystallization drift after overt optimization has effectively saturated.

(iii) **Primary observables.** Record $f(t)$ each generation, together with $\lambda(t)$ and a simple attractor-diversity statistic as secondary readouts. The ACP's primary prediction is positive post-optimal drift in $f(t)$; the expected companion signal is non-increasing $\lambda(t)$.

(iv) **Primary statistic.** For each replicate, fit the slope of $f(t)$ over the post-optimality window. The main test is whether the median slope is positive and whether the fraction of positive-slope runs is substantially above a matched null.

(v) **Null controls.** The minimal null is a post-threshold control where retention is neutral among fitness-equivalent networks, so that function is preserved but continued selection for dynamical stability is removed. A second useful null is mutation-only drift with no selective retention.

(vi) **Pass/fail criterion.** The Tier-1 pass counts as supportive if post-optimal $f(t)$ continues to rise in a clear majority of runs and the effect exceeds the null controls. It counts as a directional failure if $f(t)$ plateaus immediately after threshold in both the selected and null ensembles.

### **A.16.11.3 Prediction 8: minimal computational pipeline**

Prediction 8 needs one modeling caution. A bare fixed-coefficient Bénard or reaction-diffusion solver with no slow state variable for pathway reinforcement would test only transient mode selection, not the A.14.5 claim that *successful dissipative pathways rigidify under continued operation*. The minimal Tier-1 object should therefore be an ACP-informed reduced simulator rather than a full laboratory-fidelity fluid code.

(i) **Model class.** Use a reduced mode-competition system with amplitudes for a finite family of candidate dissipative modes under constant drive, together with a slow reinforcement variable that increases when a mode remains active and feeds back by stabilizing the occupied pathway relative to its competitors. This slow reinforcement field is the computational proxy for the pathway accumulation described in Proposition A.14.5.

(ii) **Operational observable.** Define the accessible mode count not as an abstract theoretical $N(m)$ but as a probe-based quantity $N_\epsilon(t)$: the number of distinct post-perturbation modes reachable from the current state at age $t$ under a fixed library of equal-magnitude kicks.

(iii) **Protocol.** Run the system under constant boundary conditions. At probe ages $t_1 < \cdots < t_J$, clone the state into many replicas, apply the same perturbation library to the replicas, relax each replica, cluster the resulting macroscopic patterns, and count the number of distinct recovered modes. In parallel, estimate $\epsilon^*(t_j)$ by finding the smallest perturbation magnitude that reliably ejects the system from its incumbent mode.

(iv) **Primary statistics.** The ACP predicts that $N_\epsilon(t)$ is non-increasing with age and typically strictly decreasing, while $\epsilon^*(t)$ is non-decreasing. The first is the direct test of dissipative aging; the second is the perturbation-threshold companion predicted in A.14.5(d).

(v) **Null control.** Freeze or remove the slow reinforcement update while leaving the fast mode dynamics unchanged. Under that null, the post-transient accessible-mode count should be stationary up to sampling noise. This creates the cleanest same-codebase falsification test.

(vi) **Pass/fail criterion.** The Tier-1 pass counts as supportive if the reinforced model shows declining $N_\epsilon(t)$ and rising $\epsilon^*(t)$ relative to the no-reinforcement null. It counts as a directional failure if both quantities remain stationary once initial transients are excluded.

In implementation order, Prediction 9 should be built first because its simulator is the most direct transcription of A.15. Prediction 8 should follow immediately after, but its first computational pass should be treated as an ACP-informed reduced model of pathway rigidification rather than as a surrogate for the full Tier-3 Bénard experiment.

A negative result on any single prediction would not falsify the ACP framework as a whole, since each prediction draws on different aspects of the theory. However, a systematic failure across multiple predictions—especially Predictions 1 and 5, which follow most directly from the core theorem—would constitute strong evidence against the framework. The most decisive test is Prediction 10: if normalized drift rates across domains differ by many orders of magnitude, the ACP's broader recurring-law claim would need to be narrowed to a more local or qualitative statement.

**Relationship to OP2. **Resolution of OP2 (non-Gaussian bounds) would enable quantitative predictions of drift rates, perturbation thresholds, and early warning signal lead times that are currently stated only qualitatively or in terms of scaling relations. The predictions stated here are deliberately structured to be testable even without OP2—using scaling relations, rank orderings, and qualitative trends rather than absolute magnitudes. OP2 resolution would upgrade each prediction from ‘directional’ to ‘quantitative.’

## **A.16.12 Falsification Criteria**

We state explicitly the conditions under which the ACP framework would be falsified:

**Strong falsification: **If, across multiple independent domains, crystallization failures are negligibly rare (Prediction 1 rejected with NC/ND < 0.05) *and* historical success does not predict subsequent crystallization (Prediction 5 rejected), the core claim that self-reinforcing mechanisms drive conditional entropy toward zero would be refuted.

**Moderate falsification: **If the dual critical slowing down effect (Prediction 2) is absent near C—i.e., highly ordered systems recover equally fast from novel and familiar perturbations—the distinction between the two boundaries, which is central to the ACP, would be undermined.

**Weak falsification: **If the Prigogine and Kauffman domain-specific predictions (8 and 9) fail in controlled simulations, the claim that these frameworks are special cases of the ACP would require revision, though the core theorem could survive with a narrower domain of applicability.

The framework explicitly acknowledges these falsification criteria. A theory that cannot specify the conditions for its own refutation is not a scientific theory. The ACP meets this standard.

## **References**

Bergstrom, C. T. & Lachmann, M. (2004). Shannon information and biological fitness. IEEE Workshop on Information Theory.

Derrida, B. & Pomeau, Y. (1986). Random networks of automata: a simple annealed approximation. Europhysics Letters, 1(2), 45–49.

DeLong, E. R., DeLong, D. M. & Clarke-Pearson, D. L. (1988). Comparing the areas under two or more correlated receiver operating characteristic curves. Biometrics, 44(3), 837–845.

Donaldson-Matasci, M. C., Bergstrom, C. T. & Lachmann, M. (2010). The fitness value of information. Oikos, 119(2), 219–230.

Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Reviews Neuroscience, 11, 127–138.

Holling, C. S. (1973). Resilience and stability of ecological systems. Annual Review of Ecology and Systematics, 4, 1–23.

Kauffman, S. A. (1993). The Origins of Order. Oxford University Press.

Kelly, J. L. (1956). A new interpretation of information rate. Bell System Technical Journal, 35(4), 917–926.

Levitt, B. & March, J. G. (1988). Organizational learning. Annual Review of Sociology, 14, 319–340.

Prigogine, I. & Stengers, I. (1984). Order Out of Chaos. Bantam Books.

Scheffer, M. et al. (2009). Early-warning signals for critical transitions. Nature, 461, 53–59.

Zurek, W. H. (2009). Quantum Darwinism. Nature Physics, 5, 181–188.
