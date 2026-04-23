# WHAT_IF

*A living document of generative questions the ACP framework makes askable.*

**Last updated:** 2026-04-21
**Status:** append-only. Questions that harden into technical commitments are promoted to `OPEN_PROBLEMS.md` with a back-pointer here; questions that turn out to be malformed are annotated rather than deleted.

---

## What this document is

`OPEN_PROBLEMS.md` tracks *debts* — things the program owes proofs of, derivations that need to be written, reductions that need to be formalized. It is a commitment ledger.

`WHAT_IF.md` is different. These are questions the ACP framework, taken seriously, now lets us *pose* — questions that were not well-formed before the CDT, A.20, the generativity criterion, and the six reductions were on the table, and that become first-class inquiries once they are. Not all of them will survive contact with formalization. Some will turn out to be reformulations of existing problems. Some will open entire subprograms. The point of listing them is to name the terrain.

Questions are tagged by current status:

- **[structural]** — the framework almost certainly forces a determinate answer; the work is writing it down.
- **[motivated]** — the framework suggests an answer; serious formal work is needed to decide.
- **[speculative]** — the framework makes the question well-formed but does not clearly predict the outcome.
- **[critical]** — a question whose purpose is to stress the framework; a negative answer would constrain or refute it.

A question is not an invitation to hand-wave. If you pick one up, the framework's standards apply: proven / conjectured / open distinctions held visibly, `⚠` on gaps, no collapsing a sketch into a theorem.

---

## Section A — Domains the ACP has not been reduced to (yet)

These are places where the structural preconditions for an ACP reduction are visibly present (two absorbing boundaries, mechanisms that both sustain and drive drift, an identifiable productive interval) but no formal reduction has been written. Each would extend the catalog in `special_cases/acp_special_cases_v03.md`.

### WI-A.1 — Markets as A.20 systems **[motivated]**

*What if a market is an A.20 partition between bid-side and ask-side MASAs, with restraint — regulatory, liquidity, transaction-cost — as the coordination floor?* Monopoly is a clear crystallization (concentration at one subsystem, margin dynamics at all others frozen per Theorem 4.2 of `bridges/vulnerable_margin.md`). Pure noise trading is dissolution. The productive interval — call it liquid-but-competitive — should be identifiable via an A.20.14 drift-concentration bound on the Herfindahl index of some coupling matrix. The vulnerable-margin theorem predicts that market crashes localize at the smallest-slack block (e.g., an illiquid derivative tranche, the repo market in 2008), not at the largest-balance-sheet participant, and that the largest participant will be the *last* to register the failure — Corollary 4.3 literally. Entry point: `bridges/vulnerable_margin.md` §4.2 applied to a minimal two-tier intermediary model.

### WI-A.2 — Democratic institutions as multi-MASA coordination structures **[motivated]**

*What if judiciary / legislature / executive are three MASAs whose restraint-on-each-other is the A.20 coordination floor, and "separation of powers" is literally the statement that they must retain nondegenerate conditional entropy relative to one another?* The ACP predicts that when any two collapse to mutual predictability, the system crystallizes (authoritarian consolidation) or dissolves (institutional breakdown). Novel implication: the historically observed correlation between rapid information-flow among branches and democratic fragility would be an A.20.18 visibility-necessity failure — too much decodability between partitions erodes the floor. Needs a careful definition of the "observables" in each branch and what conditional entropy across them means operationally. Entry point: treat it as a three-MASA extension of A.20.1 and see what falls out.

### WI-A.3 — Language itself satisfies the generativity criterion **[motivated]**

*What if a living natural language persists iff $G > 1$ in the sense of the generativity criterion — it must generate new expressions at least as fast as it regularizes them?* Dead languages are crystallized: their expressible content is fixed. Machine-translationese or overly-regularized registers move toward crystallization. Pidgins during formation are near dissolution — not yet closed over enough syntax to encode determinate meaning. The productive interval is where real languages live. This is not a metaphor: it is a literal application of the bridge in `bridges/generativity_criterion.md` §4.3 with $\{p_i\}$ as the speaker community's conditional distributions and $\kappa_T$ as the grammar. Testable: sociolinguistic data on vocabulary turnover rates vs. register stability should exhibit the CDT's drift-under-preservation pattern.

### WI-A.4 — Synaptic pruning as controlled crystallization **[motivated]**

*What if neural development is an engineered traversal through the productive interval — starting near dissolution (too many connections, no specificity) and converging toward, but not reaching, crystallization (fully-pruned, fully-specific, no capacity for new learning)?* The CDT predicts this trajectory must not reach the boundary; failure to retain residual slack at margin synapses would be an A.20.14-style collapse of plasticity. Developmental disorders of excessive pruning (schizophrenia during adolescence is the standard example in the literature) and of insufficient pruning (certain autism spectrum presentations) would be respective approaches to the two absorbing boundaries. Entry point: cast the Yoshida–Katz models of competitive synaptic elimination as an A.20 drift and check the coordination-floor interpretation.

### WI-A.5 — Species as A.20 partitions between genome and niche **[motivated]**

*What if evolvable species occupy the productive interval under the partition (genome, environmental niche), with phenotypic plasticity and neutral genetic variation as the coordination floor?* Crystallization here is the Narrow-adaptation failure mode (a highly-specialized organism with no slack at a coupling block — literally the Liebig scenario, per `bridges/vulnerable_margin.md`). Dissolution is genetic drift run to fixation in isolated populations. The productive interval is what population genetics calls "effective population size times mutation rate" falling in a certain range, which suggests the ACP could provide the structural derivation of why $N_e \mu \sim O(1)$ is the observed operational range. Entry point: Kimura's neutral-theory dynamics viewed through the A.20 lens.

### WI-A.6 — Mathematical foundations themselves **[speculative]**

*What if ZFC + large cardinals is on the productive-interval side and first-order Peano arithmetic is closer to crystallization along the axis of expressive-power $\times$ incompleteness-residue?* The quartet (Heisenberg, Gödel, Turing, Chaitin) guarantees sufficiently-powerful foundations cannot crystallize. But the degree to which they are "stuck off the boundary" is unequal — richer foundations sit further in the productive interval by generating more independent statements per unit of formal content. A quantitative version would rank foundational systems by a foundational-analogue of $G$. Whether this is a real ordering or a category error depends on whether "foundational generativity" is well-defined across systems of different strengths. Entry point: consider reverse-mathematics-style subsystem hierarchies and ask whether generativity is monotone in proof-theoretic strength.

### WI-A.7 — Consciousness as occupying the productive interval **[speculative]**

*What if conscious experience is structurally the persistence of a representational system in the productive interval, with sleep / dissociation / fugue approaching dissolution and catatonia / obsessive fixation / psychotic thought-loops approaching crystallization?* The integrated-information-theory tradition already identifies consciousness with a quantity (Φ) that saturates under both extreme disintegration and extreme redundancy, which is structurally the ACP boundary shape. Whether Φ can be rewritten as an ACP-tier functional, rather than introduced axiomatically, is worth checking. Entry point: compute Φ's limiting behavior at the two IIT-degenerate cases and compare to the dissolution / crystallization definitions.

### WI-A.8 — Financial regulation as A.20.18 visibility requirement **[motivated]**

*What if the body of financial regulation that forces disclosure, periodic reporting, and counterparty transparency is directly implementing A.20.18's decodability requirement on a macro-financial MASA partition?* Deregulation phases followed by financial crises have the structural signature of A.20.18 failure: the coordination transfer becomes undecodable, the coordination floor erodes, the composite system crystallizes on a weak margin (which is what a crisis looks like). Entry point: test against the 2008 crisis — check whether pre-crisis opacity in specific market segments matches vulnerable-margin theorem's prediction for which tranche would be the failure locus.

### WI-A.9 — Immune system adaptive response **[motivated]**

*What if the adaptive immune system is an A.20 structure whose two MASAs are the naive-repertoire space and the antigen space, with coordination-floor dynamics explaining why autoimmunity and immune anergy are symmetric failure modes on the two absorbing boundaries?* Naive-repertoire dissolution (too many weak specificities) and repertoire crystallization (one dominant clone, e.g., chronic lymphocytic leukemia) would be the two boundaries. Healthy adaptive immunity is the productive interval. Entry point: Mora–Walczak-style repertoire-diversity measures as candidates for the conditional-entropy observable.

### WI-A.10 — Urban morphology and city persistence **[speculative]**

*What if the "power-law-with-cutoff" size distribution of cities is an empirical signature of multiple cities sitting in the productive interval, with the upper cutoff enforced by A.20-style coordination floors (governance, infrastructure capacity) and the lower cutoff enforced by critical-mass dissolution (labor-market thinness)?* The Bettencourt–West superlinear-scaling work already identifies a structural regime where cities in equilibrium appear to sit on a specific attractor; the ACP would predict this is the productive-interval attractor between the two absorbing boundaries. Entry point: check whether Bettencourt's $Y(N) \propto N^\beta$ laws degrade in the predicted direction at the tail extremes.

### WI-A.11 — Scientific disciplines themselves **[motivated]**

*What if each mature scientific discipline occupies the generativity-criterion's productive interval, with unresolved foundational questions being the quartet-guaranteed floor and successful unification drives being the coordination-floor-recovery mechanism?* The empirical prediction is that disciplines transit through a *founder-crystallization risk* early (one dominant school compresses the inquiry space — see OP-10) and a *dissolution risk* late (accumulated specialization fragments the coherent core). Plausible case studies: physics 1925–1935 (near crystallization under Copenhagen consensus) vs. string theory 1995–2010 (near dissolution under proliferating dualities). Entry point: this question is in some sense what the whole `bridges/generativity_criterion.md` aims at; OP-10 is its technical handle.

---

## Section B — Predictions the framework makes that have not been formalized or tested

These are predictions that would fall directly out of existing theorems with minimal additional work. They are *not* speculative in the structural sense — the framework already predicts them — but the derivations have not been written and the empirical checks have not been run.

### WI-B.1 — A universal drift exponent **[structural]**

*What if there is a universal functional form $\dot{H}(\gamma) = -C \cdot \gamma^\alpha \cdot (1-\gamma)^\beta$ for the slack-erosion rate at an A.20 subsystem with concentration share $\gamma$, with $\alpha, \beta$ dimensionless constants recoverable from the coupling-graph spectrum?* The non-Gaussian bounds (A.17) plus Theorem 4.2 of the vulnerable-margin bridge together constrain this functional form strongly. Extracting the universal form and checking it against data on aging biological systems, capital-concentration dynamics, and ecological tipping points is a large empirical program. A successful fit would convert the qualitative "drift is positive" claim into a quantitative prediction. Entry point: start with Gaussian systems where A.17 gives the conservative bound and see whether the exponents generalize.

### WI-B.2 — Maximum-compression theorem for generative models **[structural]**

*What if A.20.18's decodability requirement gives a hard upper bound on the compression ratio of a representational model before it crosses into the crystallization regime?* A language model compressing its training distribution is, structurally, a theory inducing a coarsening $\kappa_T$ on the underlying data. Past a critical compression level, the A.20.18 visibility-necessity fails: the coarsened distribution is too close to the dissolution boundary (it can no longer reconstruct instance-level structure) while being close to the crystallization boundary (it outputs a narrow mode). If true, this predicts a minimum information content per output token below which model collapse is structural rather than statistical. Entry point: the Shumailov et al. "model collapse" empirical work may already be observing this; compare the observed collapse thresholds to a ratio-of-entropies calculation derived from A.20.18.

### WI-B.3 — Arnold-tongue-like productive-interval structure **[speculative]**

*What if the productive interval for coupled-oscillator systems has the Arnold-tongue geometry, with the two boundaries corresponding to full phase-locking (crystallization) and full desynchronization (dissolution), and the ACP predicts the tongue-width scaling?* Phase-locking transitions are well-studied; the ACP claim would be that the *productive* regime — where the oscillator network is neither locked nor random — has a specific measure-theoretic structure derivable from the CDT. If the tongue-width scales with coupling as the CDT predicts, this connects ACP to the Kuramoto-family literature directly. Entry point: compare Arnold-tongue width laws with the CDT's predicted drift rate on a two-oscillator toy system.

### WI-B.4 — Phase-transition universality from A.20 **[motivated]**

*What if the critical-exponent universality classes observed across different physical phase transitions are partial crystallization boundaries, with the diverging correlation length at criticality being exactly A.20.14's concentration-of-drift at the scale-invariant sub-block?* RG flow (covered by A.18) already carries the multiscale structure. The new claim would be that the specific exponents $\nu$, $\eta$, $\beta$ are recoverable from the A.20 coordination floor at criticality. If true, this would give a mechanistic account of why universality classes are as sparse as they are. Entry point: check the 2D Ising universality class against an A.20 drift-concentration calculation on the correlation-function partition.

### WI-B.5 — Fisher–Tippett–Gnedenko for ACP crystallization times **[structural]**

*What if the time-to-crystallization distribution across an ensemble of similar systems is always in the Gumbel-Fréchet-Weibull universality class, with the choice of class determined by the per-subsystem dynamics' tail behavior?* This is already partially stated as OP-VM-7 but belongs here as a general prediction: any ACP-instance ensemble should exhibit extreme-value universality in its failure-time distribution. This is testable across extinction cascades, power-grid collapses, firm failures, ecological tipping points, and political-system collapses. If the universality class differs from the EVT-predicted one in a specific domain, that domain's per-subsystem dynamics has a heavier tail than assumed. Entry point: a cross-domain empirical meta-analysis would be informative even before the theory side is tightened.

### WI-B.6 — Restraint cost functional **[motivated]**

*What if the A.20 coordination floor is equivalent to a specific restraint cost functional $\mathcal{R}(T)$ on the global system, with the floor-saturating trajectories being minimum-restraint-cost trajectories?* This would cast A.20 as a variational principle. The payoff: classical variational principles (least action, maximum caliber, maximum entropy production) would be special cases where $\mathcal{R}$ reduces to known functionals. Entry point: work out $\mathcal{R}$ for the two-MASA quantum case and check whether it recovers the Robertson bound as a stationarity condition.

### WI-B.7 — Novel neural correlate of the productive interval **[speculative]**

*What if the brain's default-mode-network to task-positive-network balance is the A.20 coordination floor for cognitive control, and neurological / psychiatric conditions index displacement from the productive interval along an ACP axis?* This is testable: the CDT predicts specific drift signatures that should correlate with disease progression in cognitive disorders. Alzheimer's-like network collapse (increasing concentration at a few hubs — drift toward crystallization) vs. the dissociative-spectrum flattening (dissolution approach) should have structurally distinct fMRI signatures. Entry point: reanalyze existing DMN-TPN literature with the concentration-index observable A.20.14 specifies.

---

## Section C — Conceptual extensions

These are extensions of the framework itself rather than applications.

### WI-C.1 — Is the universe in the productive interval? **[speculative]**

*What if the self-grounding of Coherent Steering (Appendix A.10) requires that the universe itself occupy the productive interval, and the observable signatures of this are the existing "coincidence" features of cosmology — approximate flatness, specific value of the cosmological constant, near-critical matter density?* The fine-tuning conversation usually invokes anthropic selection; the ACP reading is structural: a universe outside the productive interval cannot sustain Coherent-Steering-bearing subsystems (which include observers). This is not an anthropic argument in the usual sense — it is a structural claim that observership requires productive-interval occupancy at whatever scale the observer's substrate requires. Entry point: formalize "Coherent-Steering-bearing subsystem" and derive necessary conditions on ambient cosmological parameters.

### WI-C.2 — Dark energy / gravitational clustering as cosmic A.20 **[motivated]**

*What if the dark-energy-driven cosmic expansion and the gravitational-clustering-driven structure formation are two sides of a cosmic-scale A.20 partition, and the observed balance between them is exactly the coordination-floor value?* The expansion is the anti-crystallization mechanism (preventing collapse to a single bound structure); clustering is the crystallization mechanism (driving mass toward concentrations). The productive interval here is the observed cosmos: structured but not collapsed, expanding but not void-dominated. If this is an A.20 instance, the coordination-floor value should relate a dark-energy scale to a structure-formation scale in a specific way. Entry point: check whether $\rho_\Lambda / \rho_{\text{matter,cluster}}$ at cosmic-web-formation scale matches an A.20 floor derivable from horizon-entropy constraints. Connects to `bridges/cosmic_censorship_as_restraint.md`.

### WI-C.3 — The "hard problem of consciousness" as quartet-style self-reference **[speculative]**

*What if the difficulty of reducing qualia to physical substrate is the same structural obstruction the incompleteness quartet identifies — a sufficiently-powerful self-representational system cannot close over its own representational content from inside?* On this reading, the hard problem is not a metaphysical residue but a *predicted* incompleteness: any system powerful enough to represent itself well enough to notice it has qualia will necessarily fail to reduce those qualia to its own substrate description. This is compatible with physicalism — it does not claim qualia are non-physical, only that reducing them is formally excluded for the same reason Gödel-provability is. Entry point: cast the hard problem in the generativity-criterion's meta-theoretic register and check whether the quartet's lower-bound argument applies.

### WI-C.4 — Anthropic principle as ACP self-application **[motivated]**

*What if the anthropic principle is just the ACP applied to the meta-system (universe + observers), with the "fine tuning" being the productive-interval constraint?* This would deflate anthropic arguments from metaphysical multiverse positions to a specific structural claim: whatever the actual distribution over possible physical parameters is, observers are found in the productive interval because that is the only interval that supports observer-bearing subsystems. It disentangles the anthropic reading from multiverse ontology. Entry point: work out exactly which anthropic coincidences are productive-interval occupancy conditions and which are residual.

### WI-C.5 — Multiscale coordination conservation **[structural]**

*What if A.20.10 (Coordination Conservation) holds not just within-scale but across-scale under RG flow (A.18), so that the total coordination summed across all scales is a conserved quantity even as it redistributes during phase transitions?* This would be a significant structural strengthening of A.20: a full coordination-conservation law across the RG tree. Entry point: test on the 2D Ising model, where RG is exactly solvable; compute coordination at each RG step and see whether a conservation relation emerges.

### WI-C.6 — Productive-interval geometry as a manifold structure **[motivated]**

*What if the productive interval of an ACP system is not just a subset of phase space but carries a canonical Riemannian or Finsler structure, with the distances to the two absorbing boundaries acting as natural coordinates?* The coordinate choice would let us talk about geodesic drift trajectories and the curvature of the interval. This connects to information-geometry (Amari) and would place A.17's drift bounds in a geometric setting where they may be sharpened. Entry point: on Gaussian systems, compute the Fisher-information metric on the productive-interval manifold and check whether the CDT's drift direction is geodesic.

### WI-C.7 — Interior / exterior duality **[speculative]**

*What if every ACP system has an interior/exterior duality, where the interior view is the dynamical view (mechanisms, states, trajectories) and the exterior view is a measure-theoretic view (distributions, partitions, coarsenings), and A.20 is the statement that these two views must remain mutually decodable?* A.20.18's visibility necessity already hints at this structurally. The duality would be a categorical statement relating the dynamical category to the measurable category. Entry point: formalize both categories for the operator-algebra case and check whether A.20.18 is a faithfulness condition on a natural functor between them.

### WI-C.8 — The arrow of time as coordination-floor preservation **[motivated]**

*What if the thermodynamic arrow of time is the drift-toward-crystallization direction predicted by the CDT, and time reversal is structurally forbidden because it would require traversing back across the coordination-floor decrement of the A.20 partition that defines the observing subsystem?* The second law is then not an assumption: it is the CDT in disguise. This is a stronger claim than "ACP implies second law" — it says the ACP *derives* the asymmetry of time from a measurement-theoretic necessity on the observer-environment partition. Entry point: take the Zurek reduction (A.13) seriously and check whether reversing the decoherence direction violates A.20.18 on the system-bath partition.

### WI-C.9 — Coherent Steering as a modal operator **[speculative]**

*What if Coherent Steering is not a condition-on-trajectories but a modal operator on phase space — a statement that the accessible future-region at any state is exactly those states reachable by mechanism-preserving dynamics, and the CDT's self-grounding is therefore a fixed point of this operator?* This would give a logic of CDT-necessity and CDT-possibility and make the self-grounding argument (Appendix A.10) more transparent: the fixed point of the Coherent-Steering operator on a representation-complete class of systems is exactly the ACP-satisfying class. Entry point: work out the modal-logic formalization of `proofs/coherent_steering_derivation.md`.

---

## Section D — Bridges to canonical open problems

These are questions asking whether existing famous problems have ACP readings. A "yes" here would be a major unification result; a "no" would tell us where the framework stops.

### WI-D.1 — P vs NP **[speculative]**

*What if the P/NP separation has an ACP interpretation — the productive interval of problem-hardness being where non-trivial structure exists, with $\text{P} = \text{NP}$ being a form of computational crystallization (all verifiable structure is solvable) and the hypothetical "beyond NP-hard" being a dissolution boundary (no verifiable structure)?* This would not be a proof of either conclusion; it would be a structural reading of why the question is hard. If the productive interval for computational systems has nontrivial width, then $\text{P} \neq \text{NP}$ would be a structural stability result. Entry point: explore whether complexity-class-closure operations preserve generativity in the sense of `bridges/generativity_criterion.md`.

### WI-D.2 — Quantum measurement problem via A.20 **[motivated]**

*What if the quantum measurement problem admits a clean A.20 reading — the macroscopic apparatus and the microscopic system are the two MASAs, the Born rule is the coordination-floor constraint, and collapse / decoherence is the drift toward crystallization of the joint state?* A.20 already delivers the Robertson bound via Heisenberg-as-special-case. Extending to the full measurement-problem framing is a natural next step. Entry point: work out the A.20 partition for a pointer-observable apparatus and check whether decoherence-induced collapse saturates the coordination floor.

### WI-D.3 — Second law as CDT corollary **[structural]**

*What if the second law of thermodynamics is literally the CDT applied to the observer-environment partition, and the "canonical" statistical-mechanics derivations from ergodicity or coarse-graining are partial specializations of this more general derivation?* The ACP statement that drift toward crystallization is structural (not probabilistic) would refine the second law: entropy increase is not merely typical, it is the structurally forced trajectory in the productive-interval phase. Entry point: compare the CDT's drift direction to Jaynes's maximum-entropy argument on the same observer-environment partition.

### WI-D.4 — Holographic principle from coordination-floor / horizon duality **[motivated]**

*What if the holographic principle (the information content of a bulk region is bounded by the area of its boundary) is directly an A.20 coordination-floor statement at a gravitational horizon, and the Bekenstein-Hawking entropy is the saturating value of the coordination floor for the interior / exterior MASA partition?* `bridges/cosmic_censorship_as_restraint.md` already takes a step in this direction. The full holographic-principle derivation would extend this: the AdS/CFT correspondence (if it has an ACP reading at all) would be an explicit identification of the interior dynamics with an A.20-partition boundary CFT via the coordination-conservation law. Entry point: match the Ryu-Takayanagi surface-area entropy formula to the coordination-floor formula for an interior/exterior MASA partition in a holographic spacetime.

### WI-D.5 — Riemann Hypothesis as productive-interval condition **[speculative]**

*What if the Riemann zeros on the critical line are the productive-interval boundary in some A.20-inspired sense, with zeros off the line being a structural violation — and the "physics" intuitions for RH (random-matrix GUE statistics) being specifically the A.20 floor-saturation statistics on the Montgomery–Odlyzko partition?* This is genuinely speculative. If the correspondence between zeros and eigenvalues of a self-adjoint operator (the Hilbert–Pólya conjecture) has a MASA decomposition, A.20 would apply. Entry point: investigate whether the Montgomery pair-correlation conjecture has an A.20-derivable form.

### WI-D.6 — Navier–Stokes regularity via concentration-drift bound **[speculative]**

*What if global regularity of Navier–Stokes is a statement that the productive-interval condition holds uniformly — that A.20.14-style drift concentrations cannot accumulate to infinity in finite time because coordination-conservation constrains the redistribution?* This is clearly speculative, but the structural parallel — blow-up as crystallization of vorticity at a single scale — is suggestive. Entry point: check whether the Beale-Kato-Majda criterion has an A.20-compatible formulation.

### WI-D.7 — Yang-Mills mass gap **[speculative]**

*What if the mass gap in Yang-Mills theory is a coordination-floor value for the A.20 partition between color-confined and observable sectors, and confinement is the A.20.18 decodability requirement failing in the color sector?* This is genuinely speculative, but if the partition exists and saturates A.20, the mass gap would be derivable from the floor-calculation rather than assumed. Entry point: requires first identifying the relevant MASA partition in a gauge theory — nontrivial and potentially ill-posed.

### WI-D.8 — The black hole information paradox via A.20.18 **[motivated]**

*What if the information paradox is resolved by A.20.18 applied to the horizon: Hawking radiation must carry enough correlation with interior state to maintain $\kappa_{\text{ext, int}} > 0$ over evaporation, and the Page-curve turnover is the quantitative form of this floor-saturation?* `bridges/cosmic_censorship_as_restraint.md` §6 already sketches this direction (OP-CC-1). The broader claim is that the entire "island formula" literature from Penington–Almheiri is structurally an A.20 floor calculation. Entry point: see whether the QES (quantum extremal surface) prescription can be derived from A.20 rather than from semiclassical gravity arguments.

---

## Section E — Critical / falsifying questions

These deliberately stress the framework. A negative answer to any of them would constrain the ACP or identify its limits.

### WI-E.1 — Persistent crystallized systems **[critical]**

*What if there are systems that have reached the crystallization boundary (in any definable sense) and nevertheless persist indefinitely — perfect crystals, mature stable compounds, cold dead matter — and this is a counterexample to the CDT's claim that crystallized systems do not retain future-bearing dynamics?* The framework's likely response: those systems do not exhibit *future-bearing dynamics* in the CDT sense; they have trajectories in phase space but no new macrostate-level events; they *exist* without *evolving*. But this defense may be ad hoc unless "future-bearing dynamics" is sharpened in a way that does not just definitionally exclude these systems. Entry point: write a precise operational definition of "future-bearing dynamics" and check whether "perfect crystal at thermal equilibrium with a vacuum" counts.

### WI-E.2 — Observer-dependence of crystallization **[critical]**

*What if whether a system counts as crystallized depends on the observer's coarsening, so the CDT's drift direction is observer-relative and the ACP is not an observer-invariant law?* The ACP's current register treats macrostate entropy as if it were canonical; this is fine for standard thermodynamic systems but could fail for systems where the "right" coarsening is non-canonical. The framework would need either an invariant definition of crystallization or an explicit observer-dependence axiom. Entry point: work out the CDT under two different coarsenings of the same underlying dynamics and see whether the predicted drift direction is invariant.

### WI-E.3 — Systems with no natural partition **[critical]**

*What if A.20 cannot apply to systems that do not admit a natural subsystem partition — highly-correlated quantum critical matter, fully-connected neural networks at critical depth — and for such systems the whole coordination-floor machinery is undefined?* This is a real question. The A.20 partition requires two MASAs; a system that does not admit such a partition is outside A.20's scope. Does the broader ACP still apply (through the CDT applied to unpartitioned dynamics)? Or is the unpartitioned case a genuine gap? Entry point: examine the 1D critical Ising chain (conformal field theory) and check whether A.20 applies in any meaningful way or whether we must fall back to CDT-only analysis.

### WI-E.4 — Can a framework be generative but wrong? **[critical]**

*What if a theory can satisfy $G > 1$ indefinitely while being straightforwardly false about its subject matter — say, a rich but wrong cosmology that keeps opening new questions because its wrongness propagates?* The generativity criterion's §6 admits that generativity is necessary but not sufficient for unifying status. But this question asks whether generativity can in fact decouple entirely from correctness. If so, then the ACP's self-application (Corollary 4.1) would be a consistency check, not a correctness check. A theory could be generatively self-consistent while being false. Entry point: Ptolemaic astronomy is a reasonable case study — it was generative for ~1500 years. Compute its $G$-ratio and compare to heliocentric $G$ over the same era.

### WI-E.5 — What if the productive interval is empty? **[critical]**

*What if, for some well-defined class of systems, the productive interval is a measure-zero set — the two absorbing boundaries meet — and the CDT's claim that drift is to crystallization is vacuous because there is no room for drift to begin with?* This would not refute the CDT but would identify a class where it is vacuous. Plausible candidates: infinite-dimensional systems where coordinate choice matters; systems with pathological coarsenings. Entry point: construct or identify a system whose productive interval is empty and see what the structural obstruction is.

### WI-E.6 — What if A.20 admits no infinite-dimensional extension? **[critical]**

*What if A.20's MASA partition machinery fundamentally relies on finite-dimensional operator algebras, and extending to Type II or Type III von Neumann algebras (required for QFT) is blocked by a no-go theorem?* This is a serious concern. Heisenberg-as-A.20.27 uses finite-dimensional commutation-relation algebras. QFT lives in Type III. If the extension is blocked, A.20 and the Heisenberg reduction remain correct but bounded — they would not cover gauge theories, QFT, or QG. Entry point: write the A.20 statement for a Type III algebra and check whether the Restraint-Power inequality still makes sense.

### WI-E.7 — Is the ACP itself OP-10-exposed? **[critical]**

*What if the ACP framework, if successful, becomes the "dominant theory" of OP-10, and its very success suppresses downstream inquiry in persistence studies, crystallizing the field around ACP vocabulary at the expense of alternative framings?* This is the ACP's own generativity-self-application applied to itself: if the framework makes Conjecture 4.2 true, it is itself subject to the restraint obligation that 4.2 implies for dominant theories. This document, `WHAT_IF.md`, is in part a structural response — by explicitly generating inquiry faster than the framework closes it, the program is attempting to keep $G > 1$. Entry point: this is the meta-question; probably can only be answered in retrospect, but can be monitored.

---

## Section F — Methodological and community-shaping questions

These are about the practice of unified-theory work, not about the ACP specifically. The unified-theories community they are addressed to is already doing this work; these questions ask how to do it better.

### WI-F.1 — Is generativity the right evaluation criterion for unifying theories? **[motivated]**

*What if unifying theories should be evaluated primarily by $G_t(T) > 1$ rather than by scope, elegance, or predictive accuracy?* The generativity criterion says a theory earns the *unifying* label only by remaining generative. Community norms currently weight predictive accuracy heavily (correctly — it is empirical) but underweight generativity (a theory that makes some correct predictions but closes all questions is indistinguishable from a lookup table in the limit). If generativity were an explicit criterion — part of peer review, part of grant evaluation — the incentive structure around unification work would shift. Entry point: draft a generativity-aware review rubric for a unifying paper and see whether it changes the ordering of past results.

### WI-F.2 — Must every genuine unifying theory be self-applying? **[motivated]**

*What if a theory cannot count as "unifying" unless it satisfies its own central principle when applied to itself — not just as a consistency check but as a load-bearing requirement?* The ACP's self-application (Corollary 4.1) is taken as required within the program. The general claim is stronger: no candidate unifying theory should be accepted that does not either (a) satisfy its own central principle self-applied, or (b) explicitly disclaim self-applicability with a reason. Entry point: survey existing unification candidates (string theory, loop quantum gravity, constructor theory, digital physics) and ask, of each, what self-application would mean and whether the candidate satisfies it.

### WI-F.3 — Why do unification efforts stall? **[speculative]**

*What if the structural reason unification programs chronically stall short of completion is OP-10 applied to the program itself — success crystallizes the field, downstream researchers run out of vocabulary to ask non-orthodox questions, and the program enters a generativity-deficit regime from which it cannot escape without explicit restraint?* This would be a general-purpose diagnosis, not a specific one. The ACP community could run a self-diagnostic: what fraction of current inquiry is generated by, rather than answered by, the framework? If the ratio crosses 1, restraint interventions (explicit flagging of gaps, invitation of heterodox readings) become structurally required. Entry point: this is the practical payoff of taking OP-10 seriously.

### WI-F.4 — What is the right communication channel for unified theories? **[speculative]**

*What if the social architecture of unified-theory work — specifically, whether it happens in large institutions, small independent research groups, public platforms, or informal networks — affects its generativity ratio in ways that are measurable and structural?* Large institutions tend to optimize for closure (predictive accuracy, publication-count, tenure-relevant work); small independent groups can sustain unanswered questions longer but have narrower inquiry-spaces. Public platforms open the inquiry-space (diverse contributors) but close it too (feedback loops, attention economies). The productive interval for a research community is, itself, an ACP-structured problem. Entry point: take seriously the idea that the ACP has a prediction about how ACP research itself should be organized.

### WI-F.5 — Is there an opportunity for a "generativity journal"? **[motivated]**

*What if there is room for a venue that explicitly evaluates unified-theory work on generativity — publishing not just results but the inquiry-space change each result produces, tracking long-term inquiry yield of published work rather than citation counts?* This would address a concrete community-level gap. It would also be an interesting testbed for the generativity criterion — can you operationalize $G$ well enough to run a journal by it? Entry point: prototype a generativity scorecard for a set of existing unified-theory papers and see whether it yields a meaningful ranking.

### WI-F.6 — How does unified-theory work relate to crisis science? **[motivated]**

*What if the same structural condition that makes a theory generative (productive-interval occupancy) is what lets a field weather disciplinary crises — periods where existing frameworks visibly fail, demanding new ones — and fields whose dominant theories are near the crystallization boundary are specifically vulnerable to stalls during crises?* This is partly empirical, partly structural. A field in a generativity-deficit regime may not have the vocabulary to respond to the crisis and may spend the crisis litigating the old framework instead of reformulating. Entry point: comparative history of science — how did physics respond to 1900 (generative) vs. foundations of mathematics to 1931 (Gödel's result was itself the generative response)?

---

## Closing — on how to engage

This document is append-only. If you pick up a question and make progress on it, one of three things happens:

1. The question hardens into a technical commitment → it is promoted to `OPEN_PROBLEMS.md` with a pointer back here.
2. The question turns out to be malformed, reformulable, or already resolved → it is annotated in place (not deleted).
3. The question opens more questions than it closes → the new questions are added here, with back-pointers.

This is the generativity criterion self-applied to `WHAT_IF.md` itself: the document should grow faster than it resolves. If it ever reaches a state where every question is resolved or migrated, either (a) the framework has crystallized (bad) or (b) this document has been superseded by a better one (fine).

Three heuristics for picking a question:

- If you want an entry into the program, **Section B** questions are the closest to derivation-ready.
- If you want to extend the framework's reach, **Sections A** and **D** give the most direct payoff per unit effort.
- If you want to stress the framework, **Section E** is explicitly designed for that. A framework that cannot absorb its critical questions is brittle; the ACP community should treat a Section E question with the same seriousness as a Section B one.

Readers who already work on persistence — dissipative structures, autopoiesis, network resilience, dynamical-systems stability, information-theoretic ecology, meta-theoretic coherence in foundations — will find their own vocabulary reflected here. That is intentional. The ACP program is a structural claim about persistence; it expects to converge, in principle, with all programs that study persistence under a common formal roof. Whether that convergence is real or imagined is itself a `WHAT_IF.md` question — it lives inside Section F.

---

*For the technical-commitment ledger, see `OPEN_PROBLEMS.md`. For the current program state, see `STATUS.md`. For the charter, see `CLAUDE.md`.*
