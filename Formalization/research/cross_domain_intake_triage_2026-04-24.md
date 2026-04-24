# Cross-Domain Intake Triage — 2026-04-24

*Status: first application of `bridges/cross_domain_generativity_protocol.md`. Scores are heuristic, not evidence. The purpose is to identify which unexpected domains most improve the ACP research program by producing new questions, observables, and falsification paths.*

---

## 1. Candidates

This pass applies the protocol to three existing `WHAT_IF.md` entries:

1. **Language as generativity system** (WI-A.3)
2. **Model collapse as compression-bound phenomenon** (WI-B.2)
3. **Systems with no natural partition** (WI-E.3)

These were chosen because they stress different parts of the theory:

- language probes OP-11, the measure-theoretic meaning-space;
- model collapse probes OP-12, the quantitative generativity bound;
- no-partition systems probe the scope boundary of A.20.

## 2. Intake Table

| Candidate | $B_X$ boundary pair | $M_X$ mechanisms | $O_X$ observable candidates | Primary $F_X$ gap | First $Q_X$ questions | Score sketch |
|---|---|---|---|---|---|---|
| Language | dissolution = no shared syntax / unstable meaning; crystallization = fixed dead register | innovation, regularization, mutual intelligibility pressure, institutional standardization | lexical turnover, syntactic entropy, semantic-neighborhood spread, register diversity, mutual-information across speakers | observable gap + falsification gap | What measure of living-language inquiry-space survives across corpora? Does over-regularization reduce expression turnover before intelligibility fails? | high: $G_X \approx (4Q + 5O + 2P)/1C$ |
| Model collapse | dissolution = outputs lose instance-level reconstructability; crystallization = narrow-mode repetition | compression, distillation, synthetic-data feedback, mode selection | output entropy, support coverage, KL to source distribution, reconstruction fidelity, novelty-rate decay | conservation gap + quantitative-bound gap | Is there a minimum information-per-token floor? Does collapse begin when compression breaches an A.20-like visibility threshold? | high: $G_X \approx (4Q + 4O + 3P)/1C$ |
| No-partition systems | dissolution/crystallization may exist, but A.20 partition is undefined | critical correlations, all-to-all coupling, scale-free organization | correlation length, mutual-information spectrum, effective-rank flow, partition-dependence of entropy | partition gap + scope gap | Does CDT survive when A.20 fails? Can partitions be generated endogenously from spectrum or RG flow? | very high: 0 closed claims, denominator regularized to 1 |

Because $C_X$ is regularized by $\max(1, |C_X|)$, the no-partition candidate scores high not because it closes claims, but because it exposes a clean scope boundary. That is exactly the kind of incompleteness sensor the protocol is meant to preserve.

## 3. Candidate Notes

### 3.1 Language

Language is the most direct route into OP-11 because it already looks like a meaning-space object. The likely observer set $\{O_i\}$ is a speaker community, each with conditional distributions over intended meanings and utterance forms. A grammar or dominant register acts as a coarsening $\kappa_T$.

The strongest observable candidate is not vocabulary size alone. Vocabulary can grow while expressive use crystallizes. Better candidates are:

- semantic-neighborhood spread for words or constructions over time;
- syntactic entropy conditional on communicative function;
- mutual-information between speaker communities across registers;
- rate of productive construction formation relative to rate of standardization.

First testable conjecture: living languages retain a nonzero turnover floor in productive constructions even when core grammar stabilizes. Dead or over-standardized registers should show falling construction turnover before they show total communicative failure.

### 3.2 Model Collapse

Model collapse is a strong OP-12 probe because it is already quantitative. The candidate ACP reading is that repeated compression and synthetic-data feedback move a representational system toward a dual failure: narrowed output support (crystallization) and loss of reconstructable source distinctions (dissolution).

The immediate value is the possibility of a bound. If A.20.18-style decodability is the right lens, collapse should begin when the model's compressed distribution loses enough correlation with the source distribution that downstream samples no longer preserve the coordination floor.

Possible observables:

- support coverage over generations of synthetic-data retraining;
- output entropy conditional on prompt class;
- KL or Wasserstein distance from the original data distribution;
- reconstruction fidelity for rare or tail modes;
- novelty-rate decay under repeated generation.

First testable conjecture: collapse onset is better predicted by tail-mode reconstruction loss than by global entropy alone, because the vulnerable margin should fail first.

### 3.3 Systems With No Natural Partition

This is the most theoretically valuable failure case. If a system has no stable subsystem partition, then A.20 may be undefined even while CDT remains meaningful. That would sharpen the theory by separating:

- ACP/CDT as the broad interval-and-drift layer;
- A.20 as the partitioned coordination-transfer layer.

The key question is whether partitions must be supplied externally, or whether they can be generated endogenously from the system's spectrum, RG flow, or correlation structure.

Possible observables:

- effective rank of the correlation matrix;
- mutual-information spectrum across candidate cuts;
- stability of partitions under RG coarse-graining;
- conditional entropy under competing coarsenings.

First testable conjecture: for strongly critical systems, A.20 becomes meaningful only after choosing a scale or coarse-graining, while CDT-level drift statements remain invariant across a larger class of coarsenings. If true, this gives a scope theorem shape: A.20 is not false in no-partition systems; it is not yet typed.

## 4. Recommendation

The best next protocol-driven move is the no-partition candidate (WI-E.3). It produces the sharpest improvement to the theory because it can delimit A.20 without weakening ACP/CDT. It asks a precise structural question:

> Can the CDT be formulated for unpartitioned systems while A.20 requires an additional partition-generating functor?

If yes, the project gains a cleaner layer separation. If no, the project learns that partition structure is more primitive than currently stated. Either outcome improves the theory.

The second-best candidate is model collapse, because it may give OP-12 an empirical and computational handle quickly.

## 5. Historical Blind-Spot Addendum

The next meta-level use of the protocol is historical rather than domain-analogical. History gives a before/after structure for ignorance: a later state of a field can reveal which observables, partitions, scales, or explanatory norms were unavailable earlier. This can help ACP avoid overfitting its current vocabulary to the domains it already understands.

Candidate audit episodes:

| Episode | Later-visible blind spot | Likely gap type | ACP use |
|---|---|---|---|
| Thermodynamics before statistical mechanics | entropy existed operationally before microstate-counting made its substrate visible | conceptual + scale blind spot | tests whether ACP observables are macro-only or require hidden microstate structure |
| Heredity before DNA | inheritance was measurable before the storage / copying partition was identified | partition + instrumental blind spot | probes how ACP should handle mechanisms that are empirically present before their carrier is known |
| Critical phenomena before renormalization | universality was observed before scale-flow became the explanatory object | scale + conceptual blind spot | informs WI-E.3 by asking whether partitions can be generated from RG flow rather than supplied externally |

This does not replace the no-partition recommendation. It supports it: the renormalization example is a historical case where a missing scale vocabulary later made a previously confusing cross-domain regularity askable.

First-pass audit completed in `research/historical_blind_spot_audit_2026-04-24.md`. Its reusable signature is: a field can have a stable regularity before it has the carrier, partition, or transformation vocabulary for that regularity. The strongest immediate consequence is to sharpen WI-E.3 into a candidate bridge about partition-generating functors for no-partition systems.

## 6. Promotion Suggestions

- Promote WI-E.3 into a candidate bridge note if a minimal example can be chosen: 1D critical Ising chain, fully-connected critical neural network, or Gaussian field with scale-free covariance.
- Convert WI-B.2 into a small simulation plan only after deciding which source-distribution metric represents the decodability floor.
- Keep WI-A.3 in `WHAT_IF.md` until an observable for meaning-space is selected; otherwise it risks becoming too elastic.
- Use `research/historical_blind_spot_audit_2026-04-24.md` as the input for a candidate bridge on partition-generating functors; the historical audit extracted a reusable blind-spot signature without claiming a new ACP reduction.
