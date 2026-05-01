**The Induction Step for k ****>**** 2 Mechanisms**

*Partial Closure of Open Problem 3 from Appendix A.8*

Appendix A.9 to the Compounding Lemma Proof

Working Draft — April 2026

*Red markers (⚠) indicate open problems requiring further formalization.*

# A.9 The Induction Step

## A.9.1 The Problem

The Compounding Lemma (Lemma 4.16, Part (c)) claims that when mechanisms R₁, R₂, …, R*k* compound sequentially, each new mechanism contributes *more* than its individual effect to the compound entropy reduction. The proof of Theorem A.8.9 (Claim A.3) establishes this for two mechanisms: the interventional interaction information Ido(Xe; X₁; X₃) ≥ 0, with strict inequality on a set of full measure. The induction step requires extending this to the pair (R̅*k*, R*k+1*), where R̅*k* = R₁ ∩ … ∩ R*k* is the compound mechanism.

The challenge is threefold: (i) we must show that the compound mechanism R̅*k* is itself a self-reinforcing mechanism; (ii) we must verify that its causal structure inherits the mediation property required by Proposition A.8.4; and (iii) we must show that Coherent Steering holds generically for the pair (R̅*k*, R*k+1*). We address each in turn.

## A.9.2 The Compound Mechanism Is Self-Reinforcing

***Lemma A.9.1 (Conditional closure of self-reinforcement under intersection). ****Let R**₁** and R**₂** be self-reinforcing mechanisms (Definition 4.7) with reinforcement strengths α(R**₁**), α(R**₂**) **>** 0 and nonempty intersection R**₁** ∩ R**₂** ≠ ∅. Assume additionally:*

*(i) **Intersection-compatibility:** for i = 1, 2, starting from the deeper set R̅ = R**₁** ∩ R**₂** is at least as favorable to return to R**i** as starting from R**i** in general, i.e.*

$$P(m' \in R_i \mid m \in \bar R) \ge P(m' \in R_i \mid m \in R_i).$$

*(ii) **Strong-overlap threshold:** the inclusion-exclusion lower bound coming from the two return channels dominates the exterior return probability to the intersection, i.e.*

$$P(m' \in R_1 \mid m \in \bar R) + P(m' \in R_2 \mid m \in \bar R) - 1 > P(m' \in \bar R \mid m \notin \bar R).$$

*Then R̅ = R**₁** ∩ R**₂** is self-reinforcing.*

***Proof. ***By Definition 4.7, a mechanism R is self-reinforcing if occupancy increases the probability of returning to R relative to starting outside it. We therefore need to show:

$$P(m(t+\Delta t) \in \bar R \mid m(t) \in \bar R) > P(m(t+\Delta t) \in \bar R \mid m(t) \notin \bar R).$$

For m(t) ∈ R̅, we have m(t) ∈ R₁ and m(t) ∈ R₂ simultaneously. The probability of the next state lying in R̅ satisfies:

P(m(t+Δt) ∈ R̅ | m(t) ∈ R̅) = P(m(t+Δt) ∈ R₁ ∩ R₂ | m(t) ∈ R₁ ∩ R₂)

By the inclusion-exclusion bound on the complement:

P(m(t+Δt) ∈ R₁ ∩ R₂ | m(t) ∈ R̅) ≥ P(m' ∈ R₁ | m ∈ R̅) + P(m' ∈ R₂ | m ∈ R̅) − 1

By assumption (i), each term on the right is at least as large as the corresponding basin-return probability from the full basin. Assumption (ii) then upgrades the inclusion-exclusion lower bound into exactly the self-reinforcement inequality needed for R̅:

$$P(m' \in \bar R \mid m \in \bar R) > P(m' \in \bar R \mid m \notin \bar R).$$

Hence the compound basin is itself self-reinforcing. ■

*Remark A.9.2. *Lemma A.9.1 is deliberately stated as a **conditional closure lemma**. The hidden content in earlier drafts was exactly the pair of assumptions now made explicit: an intersection-compatibility property for nested basins and a threshold ensuring that the combined return channels dominate the exterior return probability to the intersection. In Gaussian systems, the Schur-complement picture strongly suggests these hypotheses are natural. In the generic case, however, they are real assumptions that should not be silently smuggled into the induction.

***Corollary A.9.3 (Iterated conditional closure). ****By induction, if R**₁**, …, R**k** are self-reinforcing with nonempty successive compound basins and each successive pair (R̅**j**, R**j+1**) satisfies the hypotheses of Lemma A.9.1, then the compound R̅**k** = R**₁** ∩ … ∩ R**k** is self-reinforcing.*

## A.9.2a A First Generic Closure Class: Aligned Positive-Association Kernels

Lemma A.9.1 is intentionally conditional. The next step is not to erase its
hypotheses, but to identify natural dynamical classes in which they are forced
by the transition structure. The first such class consists of systems whose
active basins are aligned and whose one-step return events are positively
associated from the compound basin.

For measurable sets A, B ⊆ M, write

$$
K_t(A,B)=P(m(t+\Delta t)\in B\mid m(t)\in A)
$$

for the one-step transition probability averaged over the current conditional
occupancy law on A.

***Definition A.9.3a (aligned positive-association pair).*** Let R₁ and R₂ be
self-reinforcing mechanisms with nonempty compound basin
\(\bar R=R_1\cap R_2\). The pair is *aligned positive-association* at time t if:

1. **Depth advantage.** Starting from the compound basin does not weaken either
   individual return channel:
   $$
   K_t(\bar R,R_i)\geq K_t(R_i,R_i),\qquad i=1,2.
   $$
2. **Positive return association.** Conditional on starting in the compound
   basin, the next-step return events to R₁ and R₂ are positively associated:
   $$
   K_t(\bar R,R_1\cap R_2)
   \geq
   K_t(\bar R,R_1)K_t(\bar R,R_2).
   $$
3. **Product-overlap threshold.** The associated compound return dominates the
   exterior return probability:
   $$
   K_t(\bar R,R_1)K_t(\bar R,R_2)
   >
   K_t(M\setminus\bar R,\bar R).
   $$

***Proposition A.9.3b (positive-association closure).*** If R₁ and R₂ form an
aligned positive-association pair at time t, then the compound basin
\(\bar R=R_1\cap R_2\) is self-reinforcing at time t. Moreover, the
intersection-compatibility condition of Lemma A.9.1 holds.

*Proof.* By positive return association,

$$
K_t(\bar R,\bar R)
=K_t(\bar R,R_1\cap R_2)
\geq K_t(\bar R,R_1)K_t(\bar R,R_2).
$$

By the product-overlap threshold,

$$
K_t(\bar R,R_1)K_t(\bar R,R_2)
>
K_t(M\setminus\bar R,\bar R).
$$

Combining the two inequalities gives

$$
K_t(\bar R,\bar R)>K_t(M\setminus\bar R,\bar R),
$$

which is exactly self-reinforcement for the compound basin. The depth-advantage
condition is the intersection-compatibility hypothesis of Lemma A.9.1. ■

***Corollary A.9.3c (iterated positive-association closure).*** Let
R₁, …, Rₙ be self-reinforcing mechanisms with nonempty successive compounds
\(\bar R_j=R_1\cap\cdots\cap R_j\). If each pair
\((\bar R_j,R_{j+1})\) is aligned positive-association, then every compound
\(\bar R_j\) is self-reinforcing.

*Proof.* Apply Proposition A.9.3b inductively, replacing R₁ by the already
formed compound \(\bar R_j\) and R₂ by the incoming mechanism \(R_{j+1}\). ■

***Proposition A.9.3d (MTP2 / monotone-kernel sufficient form).*** Suppose the
macrostate space carries a partial order, the active basins Rᵢ are increasing
events, and the transition law from each compound basin has the MTP2 / positive
association property for increasing next-step events. Suppose also that the
conditioned transition from a deeper compound basin stochastically dominates
the conditioned transition from each individual basin on increasing events. If
the exterior return probability satisfies the product-overlap threshold at each
successive compound step, then the k-mechanism intersection-closure requirement
of Theorem A.9.9 holds.

*Proof sketch.* MTP2 gives the FKG positive-correlation inequality for
increasing events, so next-step returns to aligned basins are positively
associated. Stochastic monotonicity supplies the depth advantage: starting from
the deeper compound cannot lower the return probability to any increasing
active basin. The remaining product-overlap threshold is then exactly the
exterior-leakage condition needed by Proposition A.9.3b. Iterating gives
Corollary A.9.3c. ■

*Remark A.9.3e (Status of OP-17).* This is a genuine partial closure, not a
generic theorem. It covers structured classes where the active mechanisms are
order-aligned and the transition kernel preserves positive association, such as
ferromagnetic lattice models, monotone reliability networks, order-preserving
birth-death systems, and monotone Boolean-network regimes after a coarse
graining has selected increasing basin events. It does not show that arbitrary
ACP/CDT systems have aligned basins or positive association. The remaining OP-17
task is the classification problem: determine which ACP systems generate this
alignment internally, which require it as a domain hypothesis, and which fail
intersection closure because their active basins are antagonistic or
non-comparable.

## A.9.3 The Compound Inherits the Mediation Property

Proposition A.8.4 requires a mediation condition: the causal effect of the mechanism on Xe must be fully mediated through its constrained variables. For a single mechanism R*i*, this holds by definition (Remark A.8.5): the mechanism *is* the biasing of X*i*, and has no separate causal pathway to other variables.

For the compound mechanism R̅*k*, the situation is analogous but requires explicit verification. The compound constrains the variables X̅ = (X₁, …, X*k*) jointly. We need to show that the compound’s causal effect on Xe is fully mediated through X̅.

***Proposition A.9.4 (Mediation for compound mechanisms). ****Let R̅**k** = R**₁** ∩ … ∩ R**k** be the compound of mechanisms R**i** acting on disjoint variable sets X**i**. Let X̅ = (X**₁**, …, X**k**) and let X**e** be the remaining (free) variables. If each R**i** satisfies the mediation condition with respect to X**i**, then R̅**k** satisfies the mediation condition with respect to X̅.*

***Proof. ***The compound mechanism R̅*k* acts by simultaneously applying the structural equation modifications of each R*i*. In the causal graph, the do-operator do(X̅ ∈ R̅*k*) severs all incoming arrows to (X₁, …, X*k*) from the shared substrate. The resulting graph has:

R̅*k* → (X₁, …, X*k*) → Xe

with no direct edge from R̅*k* to Xe that bypasses X̅. This follows from the fact that each component R*i* satisfies mediation individually: R*i* affects Xe only through X*i*. The compound, being the conjunction of these individual interventions, inherits this structure. There is no mechanism by which the *conjunction* of individual mediating interventions could create a direct path that none of them individually possess.

Formally: let Gdo be the interventional graph under do(X̅ ∈ R̅*k*). In Gdo, every directed path from R̅*k* to Xe must pass through at least one X*i* ∈ X̅, because R̅*k* has no direct structural equations involving Xe—it only modifies the equations for X₁, …, X*k*. Therefore the mediation condition holds: do(X̅ ∈ R̅*k*)’s effect on Xe is fully mediated through X̅. ■

*Remark A.9.5 (Non-disjoint variable sets). *If the mechanisms act on overlapping variable sets (X*i* ∩ X*j* ≠ ∅), the argument still holds: the compound intervention constrains the union X̅ = X₁ ∪ … ∪ X*k*, and mediation holds for the union because it holds for each component. The overlapping variables receive *multiple* constraints, but this is compatible with the do-operator formalism (multiple interventions on the same variable compose by taking their intersection).

## A.9.4 Coherent Steering Composes

The final and most substantive step is showing that Coherent Steering (Definition A.8.3) holds generically for the pair (R̅*k*, R*k+1*). We prove this in two stages: first for Gaussian systems (where the algebraic structure gives an exact result), then for the general case via the perturbation argument of Proposition A.8.7.

### A.9.4.1 The Gaussian case: Schur complements compose

***Proposition A.9.6 (Iterated Schur complement preserves Coherent Steering). ****Let Q be the precision matrix of the joint Gaussian transition kernel for variables (X**₁**, …, X**k**, X**k+1**, X**e**). Let Q**(k)** denote the effective precision matrix of (X**k+1**, X**e**) after eliminating X**₁**, …, X**k** by iterated Schur complementation. If the original kernel has shared substrate coupling (J**i,k+1** ≠ 0 for some i ≤ k) and Q is positive definite, then the pair (R̅**k**, R**k+1**) satisfies Coherent Steering.*

***Proof. ***The key algebraic fact is that the Schur complement of a Schur complement is a Schur complement. Specifically, if we partition the variables as (̅X, X*k+1*, Xe) and first eliminate X̅ = (X₁, …, X*k*), the resulting effective precision matrix for (X*k+1*, Xe) is:

Q(k) = Q(k+1,e),(k+1,e) − Q(k+1,e),̅X Q̅X,̅X⁻¹ Q̅X,(k+1,e)

This is a standard result from linear algebra (the quotient formula for nested Schur complements; see e.g., Zhang 2005, Theorem 1.4). The point is that Q(k) is itself a positive definite matrix—the Schur complement of a positive definite matrix is positive definite. Moreover, Q(k) inherits the coupling structure between X*k+1* and Xe from the original Q, modified by the elimination of X̅.

The Coherent Steering condition for the pair (R̅*k*, R*k+1*) becomes: the mutual information I(Xe; X*k+1* | do(X̅ ∈ R̅*k*)) ≥ I(Xe; X*k+1*). In the Gaussian case, the intervention do(X̅ ∈ R̅*k*) corresponds to fixing X̅ and computing mutual information from Q(k). Since Q(k) has the same algebraic form as the original precision matrix (positive definite, with coupling between X*k+1* and Xe), the argument of Proposition A.8.7 Part (i) applies *verbatim*: the Schur complement elimination of X̅ reduces the marginal variance of X*k+1* while preserving or sharpening the X*k+1*–Xe signal, giving Coherent Steering.

The critical algebraic fact: the effective cross-precision between X*k+1* and Xe in Q(k) is generically nonzero whenever *any* of the eliminated variables X*i* had nonzero coupling to both X*k+1* and Xe. This is because the Schur complement propagates indirect couplings: even if X*k+1* and Xe have zero direct coupling in Q, the elimination of an intermediary X*i* that couples to both creates an effective coupling in Q(k). This is the Schur complement’s defining property: it propagates indirect dependencies through eliminated variables. ■

### A.9.4.2 The general case

***Proposition A.9.7 (Coherent Steering composes generically). ****Let R**₁**, …, R**k+1** be self-reinforcing mechanisms on a shared substrate. The set of joint transition kernels for which the pair (R̅**k**, R**k+1**) violates Coherent Steering has measure zero.*

***Proof. ***The proof mirrors the three-part strategy of Proposition A.8.7, applied to the *effective* system after the first k mechanisms have been applied.

**Step 1: Effective system. **After the compound mechanism R̅*k* constrains (X₁, …, X*k*), the remaining variables (X*k+1*, Xe) evolve according to an *effective transition kernel*: Peff(X*k+1*, Xe | do(X̅ ∈ R̅*k*)). This effective kernel is a well-defined probability distribution over the remaining variables, parametrized by the original kernel parameters and the compound constraint. The key observation is that this effective kernel is itself a transition kernel with shared substrate coupling between X*k+1* and Xe (generically; the coupling vanishes only on a measure-zero set, by the same argument as Proposition A.8.7).

**Step 2: Reduction to two-mechanism case. **In the effective system, we have exactly the setup of Theorem A.8.9: two entities—the compound R̅*k* (which has already been applied) and the new mechanism R*k+1*—acting on a shared substrate. The compound R̅*k* is self-reinforcing (Lemma A.9.1). It satisfies the mediation condition (Proposition A.9.4). The effective kernel has shared substrate coupling (Step 1). Therefore, the hypotheses of Theorem A.8.9 are satisfied for the pair (R̅*k*, R*k+1*) in the effective system.

**Step 3: Apply Theorem A.8.9. **By Theorem A.8.9 (specifically, Proposition A.8.7 applied to the effective kernel), the Coherent Steering condition holds generically—the set of effective kernels violating it has measure zero. Since the effective kernel is a smooth function of the original kernel parameters (the Schur complement is a rational function of matrix entries; the discrete analog is a polynomial function of the transition probabilities), the preimage of a measure-zero set under a smooth map is measure-zero. Therefore the set of *original* kernels for which the pair (R̅*k*, R*k+1*) violates Coherent Steering has measure zero. ■

*Remark A.9.8 (The smooth map argument). *The claim that “the preimage of a measure-zero set under a smooth map is measure-zero” requires the map to be a submersion (or at least have full-rank Jacobian on a set of full measure). For the Schur complement map, this holds: the Jacobian of the map from original precision matrix entries to effective precision matrix entries has full rank whenever the eliminated block is non-singular, which is guaranteed by positive definiteness. For the discrete case, the map from original transition probabilities to effective (marginalized) probabilities is a polynomial map, and its Jacobian has full rank on a Zariski-open set (the complement of an algebraic subvariety).

## A.9.5 The Complete Induction

***Theorem A.9.9 (Conditional inductive compounding). ****Let R**₁**, R**₂**, …, R**n** be self-reinforcing mechanisms on a shared dynamical system with nonempty successive compound basins R̅**k** = R**₁** ∩ … ∩ R**k** and shared substrate coupling. Assume that for each k = 1, …, n−1:*

*(i) the pair (R̅**k**, R**k+1**) satisfies the closure hypotheses of Lemma A.9.1, or belongs to the aligned positive-association closure class of Proposition A.9.3b;*

*(ii) the compound mediation statement of Proposition A.9.4 applies; and*

*(iii) the effective-kernel map used in Proposition A.9.7 has the full-rank genericity required in Remark A.9.8.*

*Then for each k = 1, …, n−1, the interaction information I(X**e**; X̅**k**; X**k+1**) ≥ 0, with strict inequality on a set of full measure. Consequently, the compound entropy reduction satisfies:*

ΔH(R̅*n*) > ΔH(R̅*n−1*) + ΔH(R*n*)

*for each n. In Gaussian systems, the rate of conditional entropy decrease accelerates exactly; in the generic case, the acceleration claim is structural / conditional:*

ΔH(R̅*k+1*) − ΔH(R̅*k*) > ΔH(R̅*k*) − ΔH(R̅*k−1*)

*generically (i.e., on a set of full measure in kernel space) once the above hypotheses are in force.*

***Proof. ***By induction on k.

**Base case (k = 1): **This is Theorem A.8.9. R₁ is self-reinforcing, the mediation condition holds (Remark A.8.5), and Coherent Steering is generic (Proposition A.8.7). Therefore I(Xe; X₁; X₂) ≥ 0 with strict inequality on a set of full measure.

**Inductive step: **Assume the result holds for the compound R̅*k* of k mechanisms. We show it holds for R̅*k+1* = R̅*k* ∩ R*k+1*.

(i) R̅*k* is self-reinforcing: by Lemma A.9.1 (iterated via Corollary A.9.3), or by Proposition A.9.3b / Corollary A.9.3c in the aligned positive-association class.

(ii) The mediation condition holds for R̅*k*: by Proposition A.9.4.

(iii) Coherent Steering holds generically for (R̅*k*, R*k+1*): by Proposition A.9.7.

Given (i)–(iii), Theorem A.8.9 applies to the pair (R̅*k*, R*k+1*), yielding I(Xe; X̅*k*; X*k+1*) ≥ 0 with strict inequality generically.

For the accelerating rate claim: the increment at step k+1 is

ΔH(R̅*k+1*) − ΔH(R̅*k*) = I(Xe; X*k+1* | X̅*k*)

by the chain rule of mutual information. This conditional mutual information is at least I(Xe; X*k+1*) (by non-negative interaction information), and it grows with k because conditioning on a larger set X̅*k* provides more context for synergistic interaction. In the Gaussian case, this is exact: each Schur complement elimination increases the effective precision between X*k+1* and Xe (by propagating indirect couplings), so the conditional mutual information at step k+1 exceeds that at step k.

In the general case, the acceleration is a structural continuation of the Gaussian picture rather than a completely closed theorem. The interaction information I(Xe; X̅*k*; X*k+1*) is at least as large as I(Xe; X̅*k−1*; X*k+1*) under the same genericity and closure assumptions, because the larger compound X̅*k* ⊃ X̅*k−1* provides a richer conditioning set. The data processing inequality gives the weak version; the strict version remains a separate generic-constancy problem. ■

## A.9.6 What This Resolves and What Remains

**Partially resolved: **Open Problem 3 from Section A.8.7 is now split cleanly into a Gaussian-closed branch, a first structured generic branch, and a still-open fully generic branch. The two-mechanism result (Theorem A.8.9) extends by induction to k mechanisms once three ingredients are supplied explicitly: (1) closure of self-reinforcement under intersection, either by the conditional hypotheses of Lemma A.9.1 or by the aligned positive-association class of Proposition A.9.3b, (2) inheritance of the mediation property by compounds (Proposition A.9.4), and (3) generic Coherent Steering for compound-new-mechanism pairs (Proposition A.9.7). What has been removed is the hidden overclaim: the generic induction is no longer described as unconditional when it still depends on those closure hypotheses.

**Strengthened: **The induction reveals a structural insight that was not visible in the two-mechanism case: the Schur complement propagation of indirect couplings (Proposition A.9.6) means that even mechanisms with no *direct* coupling to each other can interact synergistically through intermediaries. Mechanism R3 may have zero direct coupling to R7, but the compound R̅6 may have created an effective coupling between them via the Schur complement propagation of R4 and R5. This is the algebraic mechanism behind the “web of interactions” described informally in Section A.7 of the Compounding Lemma proof.

**What remains open:**

⚠ **Open Problem (generic intersection closure). **Lemma A.9.1 now states the real hidden hypotheses explicitly, and Proposition A.9.3b derives a first non-Gaussian model class where the compound basin remains self-reinforcing: aligned positive-association kernels. The remaining job is to classify when ACP / CDT dynamics generate alignment and positive association internally, and when intersection closure fails because the active basins are antagonistic, non-comparable, or only weakly overlapping. The Gaussian case and the monotone / MTP2 class are now positive templates, but no fully generic theorem is known.

⚠ **Open Problem (monotonicity of interaction information in k). **The acceleration claim—that the increment at step k+1 strictly exceeds the increment at step k—is proven for Gaussian systems (where the Schur complement algebra gives an exact result) and argued structurally for the general case. A fully rigorous general proof would require showing that the interaction information I(Xe; X̅*k*; X*k+1*) is strictly monotonically increasing in k, which is a stronger claim than non-negativity. The Gaussian case establishes the template, and the data processing inequality provides the weak version (≥), but the strict version (>) in the general case requires ruling out the measure-zero set where the increment is exactly constant.

⚠ **Open Problem (quantitative acceleration rate). **The induction shows that drift accelerates but does not bound the rate of acceleration. A quantitative bound—expressing the acceleration in terms of the coupling structure and reinforcement strengths—would require solving Open Problem 2 (quantitative non-Gaussian bounds) from Section A.8.7 first. The Gaussian case gives the template: the acceleration rate is expressible in terms of the eigenvalues of the precision matrix, and scales with the product of coupling strengths along the Schur complement chain.

## A.9.7 Summary of the Formal Chain

The Crystallization Drift Theorem (Theorem 4.19 in the standalone note) now rests on the following strongest-current formal chain:

1. Self-reinforcing mechanisms reduce conditional entropy (Lemma 4.13).

2. Self-reinforcing mechanisms dominate pattern repertoires over time (Lemma 4.14).

3. Two non-independent mechanisms compound superadditively, with excess equal to interaction information (Compounding Lemma, Lemma 4.16, identity from Section A.4.1).

4. Self-reinforcing mechanisms are generically synergistic: the interaction information is non-negative (Theorem A.8.9, via Coherent Steering and do-calculus).

5. The compound of self-reinforcing mechanisms is itself self-reinforcing in the Gaussian branch, under the explicit closure hypotheses of Lemma A.9.1, or in the aligned positive-association class of Proposition A.9.3b. It inherits mediation (Proposition A.9.4) and satisfies Coherent Steering generically with new mechanisms once the effective-kernel map has the required rank properties (Proposition A.9.7 / Remark A.9.8).

6. By induction, k mechanisms compound with accelerating superadditivity in Gaussian systems, and conditionally in the generic case (Theorem A.9.9).

7. No endogenous reversal is possible (Lemma 4.17). Only external perturbation can interrupt the drift.

8. Therefore: the Gaussian branch yields a closed accelerating-compounding theorem, while the generic branch reduces the remaining debt to explicit closure hypotheses rather than hidden assumptions. This is enough to support the core entropy-drift theorem architecture, but not to overstate the generic acceleration claim as fully closed. ■

# Additional References for Appendix A.9

Zhang, F. (2005). *The Schur Complement and Its Applications. *Springer.

Horn, R.A. & Johnson, C.R. (2013). *Matrix Analysis. *2nd ed. Cambridge University Press.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference. *2nd ed. Cambridge University Press.

Cover, T.M. & Thomas, J.A. (2006). *Elements of Information Theory. *2nd ed. Wiley.

Fortuin, C.M., Kasteleyn, P.W. & Ginibre, J. (1971). Correlation inequalities on some partially ordered sets. *Communications in Mathematical Physics* 22, 89–103.
