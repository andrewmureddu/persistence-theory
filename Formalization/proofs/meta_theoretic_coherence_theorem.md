**Meta-Theoretic Coherence and the Generativity Theorem**

*Draft Appendix A.21 for: The Adaptive Coherence Principle*

WORKING DRAFT — April 2026

*This document formalizes the self-application program proposed in `bridges/generativity_criterion.md`. It promotes the core claim from structural bridge language into a proof document. Red markers (⚠) indicate what remains open after the present pass.*

# **A.21 Overview and Result Inventory**

The generativity bridge proposes that the Adaptive Coherence Principle (ACP) applies not only to physical, biological, and institutional systems, but also to *theory evolution itself*. A theory persists as a research program only if it remains in a nondegenerate interval between two absorbing boundaries:

- **dissolution:** the theory says nothing determinate and closes no uncertainty;
- **crystallization:** the theory closes its domain so completely that it opens no further inquiry.

The missing step has been a formal statement connecting the bridge's generativity ratio

$$
G_t(T) = \frac{\max(0,\Delta I_t)}{\max(\varepsilon,-\Delta U_t)}
$$

to the ACP's nondegenerate-interval condition. This appendix supplies that step in a form strong enough for the proof chain, while keeping the more ambitious semantic-field extensions explicitly outside the proved core.

The main results are:

- **Proposition A.21.4 (Theory-evolution productive interval):** the theory-evolution state space admits exact analogues of the ACP's two absorbing boundaries and productive interval.
- **Lemma A.21.7 (Distance-to-crystallization identity):** for any productive research step, $G_t(T) > 1$ iff the step increases the theory's distance from the crystallization boundary.
- **Theorem A.21.8 (Generativity as adaptive coherence steering condition):** for productive research trajectories, persistent generativity is exactly the local condition that explanatory progress not collapse the theory into closure.
- **Theorem A.21.11 (Quartet inquiry floor):** any self-representing theory satisfying at least one standard richness condition (Gödel, Turing, Chaitin, or Heisenberg/A.20 register) has inquiry-space bounded below by a positive constant.
- **Corollary A.21.12 (Crystallization boundary unreachable):** any self-representing theory satisfying a quartet richness condition cannot reach the crystallization endpoint.
- **Corollary A.21.13 (Meta-theoretic coherence):** a productive self-representing theory cannot crystallize; if its substantive steps are generative, it remains in the productive interval.
- **Corollary A.21.14 (ACP self-application):** if the ACP is correct and continues to satisfy the richness condition it attributes to sufficiently-powerful theories, then the ACP is itself structurally unfinished.

What this appendix does **not** prove is the downstream semantic-field program of `bridges/generativity_criterion.md` §4.2–4.3. Those claims remain open and are tracked in `OPEN_PROBLEMS.md` as OP-10 through OP-12.

# **A.21.1 Setup**

We model theory evolution at research-time $t$ by a two-coordinate state:

$$
x_t(T) = (I_t(T), U_t(T)).
$$

Here:

- $I_t(T) \ge 0$ is the **inquiry-space** of theory $T$: the cardinality, measure, or effective size of the well-posed questions that remain open in $T$'s own vocabulary.
- $U_t(T) \in [0, U_{\max}]$ is the **uncertainty-space** of $T$: the amount of unresolved explanatory uncertainty over the intended domain $D$, restricted to distinctions $T$ can pose.

We assume throughout that $U_{\max} < \infty$ on the restricted domain actually representable by $T$. This is not a substantive loss: if the intended domain is too large to normalize, we simply work on the bounded subdomain on which the theory presently claims explanatory authority.

## **A.21.1.1 Research Steps**

***Definition A.21.1 (Research step).*** A research step is a map

$$
x_t(T) \mapsto x_{t+\Delta t}(T) = (I_t + \Delta I_t,\; U_t + \Delta U_t)
$$

induced by a new theorem, extension, application, reduction, measurement protocol, or correction internal to the research program.

***Definition A.21.2 (Productive step).*** A research step is **productive** if it reduces uncertainty:

$$
\Delta U_t < 0.
$$

That is: the step actually closes some explanatory uncertainty rather than merely restating the theory.

***Definition A.21.3 (Generative step).*** A productive step is **generative** if

$$
G_t(T) > 1,
$$

where on productive steps the regularized denominator reduces to $-\Delta U_t > 0$, so

$$
G_t(T) = \frac{\Delta I_t}{-\Delta U_t}.
$$

Thus a productive step is generative exactly when it opens inquiry faster than it closes uncertainty.

# **A.21.2 The Theory-Evolution Interval**

We now define the ACP boundaries in theory space.

***Definition A.21.4 (Theory-evolution dissolution boundary).*** The dissolution boundary is

$$
\mathcal D_T := \{(I,U) : I = 0,\; U = U_{\max}\}.
$$

This is the null-theory endpoint: the theory poses no live questions because it does not organize the domain enough to formulate or close them.

***Definition A.21.5 (Theory-evolution crystallization boundary).*** The crystallization boundary is

$$
\mathcal C_T := \{(I,U) : I = 0,\; U = 0\}.
$$

This is the complete-closure endpoint: the theory has no residual uncertainty *and* no residual inquiry.

***Definition A.21.6 (Productive interval).*** The theory-evolution productive interval is

$$
\mathcal P_T := \{(I,U) : I > 0,\; 0 < U < U_{\max}\}.
$$

This is the exact analogue of the ACP's nondegenerate interval.

***Proposition A.21.4 (Theory-evolution productive interval).*** The pair $(T,D)$ occupies the theory-evolution productive interval iff it is strictly separated from both $\mathcal D_T$ and $\mathcal C_T$.

*Proof.* By Definition A.21.6, $(I,U) \in \mathcal P_T$ iff both conditions hold simultaneously:

1. $I > 0$, which excludes both absorbing boundaries, since each has $I=0$;
2. $0 < U < U_{\max}$, which excludes the crystallization endpoint $U=0$ and the dissolution endpoint $U=U_{\max}$.

Hence $\mathcal P_T$ is exactly the open interval between the two absorbing endpoints in the $(I,U)$ state space. ■

## **A.21.2.1 Distance Coordinates**

To make the directional statement precise we introduce the obvious affine distance coordinates.

***Definition A.21.5a (Distance to crystallization).*** Define

$$
d_C(t) := I_t(T) + U_t(T).
$$

Since $\mathcal C_T = (0,0)$, this is the natural one-norm distance to the crystallization endpoint in theory space.

***Definition A.21.5b (Distance to dissolution).*** Define

$$
d_D(t) := I_t(T) + (U_{\max} - U_t(T)).
$$

Since $\mathcal D_T = (0,U_{\max})$, this is the corresponding one-norm distance to the dissolution endpoint.

Both coordinates are nonnegative on the normalized theory domain, and both vanish exactly at their respective boundary points.

# **A.21.3 Generativity as the Anti-Crystallization Condition**

The bridge's central structural claim is that $G_t(T) > 1$ is not merely a suggestive heuristic but the exact condition that productive explanatory progress move *away* from the crystallization endpoint.

***Lemma A.21.7 (Distance-to-crystallization identity).*** Let $x_t(T)$ undergo a productive research step. Then

$$
G_t(T) > 1 \;\Longleftrightarrow\; d_C(t+\Delta t) > d_C(t).
$$

Equivalently:

- $G_t(T) = 1$ iff the step is neutral with respect to crystallization distance;
- $G_t(T) < 1$ iff the step moves the theory toward the crystallization boundary.

*Proof.* On a productive step, $\Delta U_t < 0$, so

$$
G_t(T) > 1
\Longleftrightarrow
\frac{\Delta I_t}{-\Delta U_t} > 1
\Longleftrightarrow
\Delta I_t > -\Delta U_t
\Longleftrightarrow
\Delta I_t + \Delta U_t > 0.
$$

But by Definition A.21.5a,

$$
d_C(t+\Delta t) - d_C(t) = \Delta I_t + \Delta U_t.
$$

Therefore

$$
G_t(T) > 1 \Longleftrightarrow d_C(t+\Delta t) - d_C(t) > 0,
$$

which is the claim. The equality and strict-inequality cases follow identically. ■

***Lemma A.21.7a (Productive steps move away from dissolution).*** If a research step is productive and non-anti-generative in the weak sense $\Delta I_t \ge 0$, then

$$
d_D(t+\Delta t) > d_D(t).
$$

*Proof.* By Definition A.21.5b,

$$
d_D(t+\Delta t) - d_D(t)
= \Delta I_t - \Delta U_t.
$$

Since $\Delta U_t < 0$ on productive steps and $\Delta I_t \ge 0$, the right-hand side is strictly positive. ■

***Theorem A.21.8 (Generativity as adaptive coherence steering condition).*** Let $\{x_t(T)\}_{t \ge 0}$ be a productive research trajectory for a theory $T$, with $x_0(T) \in \mathcal P_T$. Then the following are equivalent:

1. Every substantive step is generative: $G_t(T) > 1$ whenever $\Delta U_t < 0$.
2. Every substantive step increases the theory's distance from crystallization: $d_C(t+\Delta t) > d_C(t)$ whenever $\Delta U_t < 0$.

Moreover, if either condition holds and the trajectory satisfies the weak openness condition $\Delta I_t \ge 0$ on productive steps, then the trajectory remains in $\mathcal P_T$ and moves strictly away from both absorbing boundaries.

*Proof.* The equivalence of (1) and (2) is exactly Lemma A.21.7 applied at each productive step.

For the second claim: by Lemma A.21.7, generativity implies $d_C$ increases strictly at each productive step, so the trajectory cannot move toward $\mathcal C_T$. By Lemma A.21.7a, the same step increases $d_D$ whenever $\Delta I_t \ge 0$, so it also moves away from $\mathcal D_T$. Since $x_0(T)$ already lies in the open interval $\mathcal P_T$, and every productive step increases both boundary distances, the trajectory remains in the interval. ■

*Remark A.21.9.* This is the precise technical content of the bridge claim. The result does **not** say that every generative theory is correct. It says that, among productive theories, generativity is exactly the local adaptive coherence steering condition in theory space.

# **A.21.4 The Quartet Inquiry Floor**

The previous subsection shows what generativity *does* geometrically. We now show why sufficiently-powerful theories can sustain nonzero inquiry at all.

***Definition A.21.10 (Self-representing theory).*** A theory $T$ is **self-representing** at time $t$ if it is rich enough to encode nontrivial statements about its own inference, prediction, or descriptive procedures. Concretely, we will use any one of the following sufficient richness conditions:

1. **Gödel register:** $T$ is consistent and arithmetically expressive enough to encode elementary arithmetic.
2. **Turing register:** $T$ hosts a Turing-universal substrate or an equivalent universal procedure class.
3. **Chaitin register:** $T$ can describe strings or descriptions of unbounded length relative to a fixed universal coding scheme.
4. **Heisenberg/A.20 register:** $T$ admits a nontrivial two-subsystem partition of its observable algebra with noncommuting conjugate observables, so A.20 applies.

***Theorem A.21.11 (Quartet inquiry floor).*** Let $T$ be self-representing at research-time $t$ in the sense of Definition A.21.10. Then its inquiry-space is bounded below by a positive constant:

$$
I_t(T) \ge I_{\min} > 0.
$$

For counting measure, one may take $I_{\min} = 1$.

*Proof.* We prove the statement by cases, one for each standard richness register. In each case we show that at least one well-posed question remains open inside $T$.

**Case 1: Gödel register.** If $T$ is consistent and expressive enough to encode elementary arithmetic, Gödel's first incompleteness theorem guarantees the existence of a sentence $G_T$ expressible in the language of $T$ that is true in the intended model but unprovable in $T$. Therefore the question "is $G_T$ derivable from the present axioms of $T$?" is well-posed internally and unresolved. Hence $I_t(T) \ge 1$.

**Case 2: Turing register.** If $T$ hosts a universal procedure class, Turing's halting theorem guarantees that there exists at least one program-input pair $(p,x)$ for which no total decision procedure internal to that class determines whether $p(x)$ halts. Therefore the question "does $p(x)$ halt?" remains open for at least one well-posed instance. Hence $I_t(T) \ge 1$.

**Case 3: Chaitin register.** If $T$ can describe strings of unbounded length relative to a universal coding scheme, Chaitin's incompleteness theorem implies that beyond a finite complexity threshold set by the axiomatic description length of $T$, there exist bits of $\Omega$ (equivalently, incompressibility claims of sufficiently long strings) that cannot be derived inside $T$. Therefore at least one description-theoretic question remains open. Hence $I_t(T) \ge 1$.

**Case 4: Heisenberg/A.20 register.** If $T$ admits a nontrivial two-subsystem partition of its observable algebra with conjugate observables, Theorem A.20.27 gives a strictly positive coordination floor coinciding with the Robertson uncertainty bound in the quantum specialization. Therefore the theory cannot jointly sharpen both observables to zero residual uncertainty. The question "which admissible state saturates or further resolves the joint sharpening limit?" remains structurally open from inside the theory. Hence $I_t(T) \ge 1$.

In every richness register at least one open question is forced by the theory's own expressive power. Therefore $I_t(T)$ is bounded below by a positive constant. ■

*Remark A.21.11a.* The theorem is deliberately weak in its lower bound and strong in its structural meaning. For present purposes the important statement is not the exact size of $I_{\min}$ but the impossibility of $I_t(T)$ collapsing to zero for self-representing theories.

***Corollary A.21.12 (Crystallization boundary unreachable for self-representing theories).*** Let $T$ satisfy Theorem A.21.11 at all times along its research trajectory. Then $x_t(T)$ cannot reach the crystallization boundary $\mathcal C_T$.

*Proof.* By Theorem A.21.11, $I_t(T) \ge I_{\min} > 0$ for all such $t$. But every point of $\mathcal C_T$ has $I=0$. Therefore the trajectory cannot intersect $\mathcal C_T$. ■

# **A.21.5 Meta-Theoretic Coherence**

We can now state the self-application result cleanly.

***Corollary A.21.13 (Meta-theoretic coherence).*** Let $T$ be a self-representing theory with $x_0(T) \in \mathcal P_T$. Suppose:

1. $T$ remains productive on its substantive research steps ($\Delta U_t < 0$);
2. $T$ remains self-representing in at least one quartet register along the trajectory;
3. those substantive steps are generative ($G_t(T) > 1$).

Then the trajectory of $T$ remains in the productive interval $\mathcal P_T$ and cannot crystallize.

*Proof.* By Corollary A.21.12, self-representation prevents intersection with $\mathcal C_T$. By Theorem A.21.8, generativity on productive steps strictly increases the trajectory's distance from crystallization and, under the weak openness condition already built into generativity ($\Delta I_t > 0$), also increases the distance from dissolution. Since the initial state lies in $\mathcal P_T$, the trajectory remains there. ■

***Corollary A.21.14 (ACP self-application).*** If the ACP is correct and is itself a self-representing theory in the sense of Definition A.21.10, then the ACP is structurally forbidden from being finished: there is no terminal research state in which both its residual uncertainty and inquiry-space collapse to zero.

*Proof.* Apply Corollary A.21.13 to $T=\mathrm{ACP}$. The framework already treats representational systems as dynamical systems, so the ACP falls under its own domain if correct. The quartet inquiry floor prevents $I_t(\mathrm{ACP})$ from vanishing, and generative productive steps keep the trajectory off the crystallization boundary. Hence there is no terminal closed state with $I=U=0$. ■

*Remark A.21.15.* This does not imply that every future ACP extension will be good. It implies only that a *correct* ACP cannot terminate as a closed monument. Its success condition is the continued production of well-posed successors.

# **A.21.6 What Remains Open**

The present appendix resolves the minimal formal core of the generativity program, but three important extensions remain open.

**⚠ Open extension 1: quantitative lower bound for $G_t(T)$.** Theorem A.21.8 is threshold-based. It identifies the sign of the adaptive coherence steering condition but does not give a conservative lower bound analogous to A.17's non-Gaussian drift-rate bound. This is OP-12.

**⚠ Open extension 2: downstream semantic field.** The present proof concerns the internal theory-evolution state $(I_t,U_t)$ of the dominant theory itself. It does not yet prove the stronger claim that downstream researchers thinking through the theory inherit a reduced inquiry-space as compressive ratio rises. This is OP-10.

**⚠ Open extension 3: measure-theoretic meaning-space.** The meaning-space proposal of `bridges/generativity_criterion.md` §4.3 remains only sketched. This is OP-11.

# **A.21.7 Consequence for the Workspace**

The bridge `bridges/generativity_criterion.md` should now be read in two layers:

1. the **proved core** in this appendix: generativity as the adaptive coherence steering condition for productive research steps, plus the quartet inquiry floor and ACP self-application;
2. the **open outer program** in the bridge: downstream semantic-field restraint, meaning-space measure theory, and quantitative generativity bounds.

That split is exactly the right one for the workspace at this stage. The formal self-consistency story is now load-bearing; the social-semantic generalization remains frontier work.
