# Three-Stroke Persistence Engine: Operator-Level Adaptive Coherence

*Status: standalone bridge note. Integrated 2026-04-30 as an operator-level ACP front. This note refines `bridges/coordination_neutrality.md` by showing that coordination-neutral composition naturally lifts to hierarchical wreath symmetry, and that persistence requires a third entropy-restoring stroke.*

*April 2026. CC0.*

---

## Abstract

We introduce an operator-level implementation of the Adaptive Coherence Principle (ACP), which states that persistent systems must remain between dissolution, where structure is lost to noise, and crystallization, where future-bearing uncertainty collapses. The question is what primitive operator algebra can maintain this interval under recursive composition.

Starting from a coordination-neutral (CN) operator \(C\) satisfying \(C(y,x)=C(x,y)^{-1}\), we show that positive coordination-neutrality forces endogenous self-seeding: \(C(x,x)=1\). Coupling this with an EML-class generator \(G(x,y)=e^x-\ln y\) yields a natural two-stroke engine in which coordination produces the seed and generation re-expands it. Linear stability analysis and simulation indicate, however, that this engine does not persist: the ensemble either leaves the positive domain or converges toward a fixed point, eliminating entropy and coordination gradient.

The required third stroke is a CN-invariant antisymmetric perturbation

\[
N_\varepsilon(x,y)=\left(xe^{\varepsilon \xi}, ye^{-\varepsilon \xi}\right),
\]

which preserves the geometric-mean coordination center while restoring antisymmetric log-lift variance. In the renamed ACP vocabulary, this is not the principle itself. It is the entropy-restoring mechanism of **adaptive coherence steering**: a local move that keeps the system readable, coherent, and not over-closed.

The three-stroke cycle gives a minimal constructive operator algebra for persistence:

\[
C \to G \to N_\varepsilon \to C \to G \to N_\varepsilon \to \cdots
\]

---

## 1. The Operator-Level Persistence Problem

A system persists when its future is neither fully determined nor fully random. The ACP formalizes this condition: a system maintains a productive interval when conditional macrostate entropy \(H(m' \mid m)\) remains bounded away from both zero and its maximum.

That is a dynamical-systems statement. The question here is more primitive:

**What operator algebra, under recursive composition, can maintain the productive interval?**

Odrzywolek (2026) demonstrated that the operator

\[
\operatorname{eml}(x,y)=e^x-\ln y,
\]

together with the constant \(1\), generates the complete elementary-function repertoire via the grammar \(S \to 1 \mid \operatorname{eml}(S,S)\). EML is therefore a Sheffer-like primitive for continuous elementary functions.

But generativity is not persistence. EML can make structure; it does not guarantee that recursive composition preserves future-bearing uncertainty. The present note asks what structural properties an operator must have to preserve the productive interval, uses EML as one component, and shows that the complete answer requires coordination, generation, and entropy-restoring steering.

---

## 2. Coordination Without Capture

### 2.1 Definition

A binary operator \(C:D \to \mathbb{R}_{>0}\) on a swap-stable domain \(D \subseteq \mathbb{R}_{>0}^2\) is **coordination-neutral** (CN) if

\[
C(y,x)=\frac{1}{C(x,y)}
\]

for all \((x,y) \in D\). The log-lift \(L(x,y)=\log C(x,y)\) is then swap-antisymmetric:

\[
L(y,x)=-L(x,y).
\]

**Theorem 1 (Endogenous self-seeding).** Every positive CN operator satisfies \(C(x,x)=1\) for all diagonal points in its domain.

*Proof.* From \(C(x,x)=1/C(x,x)\), we get \(C(x,x)^2=1\). Since \(C>0\), \(C(x,x)=1\). \(\square\)

This is the first distinction from EML: EML requires the constant \(1\) as an exogenous seed, while a positive CN operator generates \(1\) endogenously through any diagonal application. The seed is forced by symmetry.

### 2.2 The bridge family

The parametric family

\[
B_{\alpha,\lambda}(x,y)=
\frac{e^{\alpha x}-\lambda \ln y}{e^{\alpha y}-\lambda \ln x}
\]

is CN by construction: swapping \(x\) and \(y\) inverts the ratio. The special case \(B_{1,1}\), the **EML bridge**, preserves the exp-log structure of EML while enforcing reciprocal restraint.

**Lemma 1 (Thin-locus singularity).** For \(B_{\alpha,\lambda}\), singular closure occurs only on the curves \(e^{\alpha x}=\lambda \ln y\) and \(e^{\alpha y}=\lambda \ln x\). These are codimension-one sets, so singularities occupy a measure-zero subset of the positive regular domain.

### 2.3 Composition and wreath symmetry

CN survives tree-compositional block swaps at every depth. For

\[
T(a,b,c,d)=C(C(a,b), C(c,d)),
\]

let \(u=C(a,b)\) and \(v=C(c,d)\). Under the block swap \((a,b,c,d)\mapsto(c,d,a,b)\),

\[
T(c,d,a,b)=C(v,u)=\frac{1}{C(u,v)}=\frac{1}{T(a,b,c,d)}.
\]

So the composition is CN under block swaps. Full leaf reversal requires the additional condition

\[
C(1/v,1/u)=\frac{1}{C(u,v)},
\]

which is independent of CN and is exactly the joint-inversion issue isolated in `bridges/coordination_neutrality.md`. The symmetry that survives composition is therefore not plain global CN, but the iterated wreath product

\[
\mathbb{Z}_2 \wr \mathbb{Z}_2 \wr \cdots \wr \mathbb{Z}_2,
\]

the natural symmetry of hierarchical coordination.

---

## 3. The Two-Stroke Engine and Its Failure

### 3.1 Construction

The natural two-stroke engine combines CN coordination with EML-class generation:

\[
C \to G \to C \to G \to \cdots
\]

where \(C=B_{\alpha,\lambda}\) and \(G(x,y)=e^x-\ln y\). CN produces the seed \(C(z,z)=1\); EML re-expands it:

\[
G(1,z)=e-\ln z.
\]

The system appears to implement constraint, alignment, and persistence at the operator level. The next two results show why it does not.

### 3.2 Scalar seed basin

On the diagonal, the two-stroke cycle reduces to

\[
f(z)=e-\ln z.
\]

**Lemma 2 (Scalar seed basin).** The map \(f(z)=e-\ln z\) has a unique fixed point

\[
z_*=W(e^e)\approx 2.01678
\]

in the forward-invariant interval \(I=[1,e]\), where \(f(I)=[e-1,e]\subseteq I\). The fixed point is attracting with \(f'(z_*)=-1/z_*\approx -0.496\), so convergence is an oscillatory contraction.

The diagonal seed basin breathes, but it still contracts.

### 3.3 Antisymmetric instability

The full pair map

\[
F(x,y)=\left(e^{C(x,y)}-\ln x,\; e^{1/C(x,y)}-\ln y\right)
\]

has unstable off-diagonal modes. At \((z_*,z_*)\), define

\[
M=e^{\alpha z_*}-\lambda \ln z_*,
\qquad
K_{\alpha,\lambda}=
\frac{\alpha e^{\alpha z_*}+\lambda/z_*}{M}.
\]

The Jacobian is

\[
J=
\begin{pmatrix}
eK-1/z_* & -eK \\
-eK & eK-1/z_*
\end{pmatrix}.
\]

The symmetric and antisymmetric eigenvalues are

\[
\lambda_s=-\frac{1}{z_*}\approx -0.496,
\qquad
\lambda_a=2eK_{\alpha,\lambda}-\frac{1}{z_*}.
\]

For \(B_{1,1}\), \(K\approx 1.175\), giving \(\lambda_a\approx 5.90\).

**Theorem 2 (Antisymmetric instability).** For \(B_{1,1}\), the raw two-stroke pair map has stable symmetric eigenvalue \(|\lambda_s|<1\) and unstable antisymmetric eigenvalue \(|\lambda_a|\approx 5.90>1\). Any small antisymmetric perturbation from the diagonal grows by a factor of about \(5.9\) per step, so the naive invariant-band conjecture \(D_\rho=\{(x,y):|\log C(x,y)|<\rho\}\) is false for the unmodified pair map.

### 3.4 Phase diagram and gating

The antisymmetric eigenvalue varies over the bridge family:

\[
\lambda_a(\alpha,\lambda)=2eK_{\alpha,\lambda}-\frac{1}{z_*}.
\]

The boundary \(|\lambda_a|=1\) separates naturally stable operators from unstable ones. But natural stability is not persistence: simulations in the supplied draft indicate that naturally stable two-stroke operators still show monotonically decaying entropy. Stability prevents fast escape; it does not replenish the productive interval.

For unstable operators, define the partial CN-manifold projection

\[
P_\delta(u,v)=\left(u^{1-\delta}v^\delta,\;u^\delta v^{1-\delta}\right),
\qquad
0<\delta<\frac{1}{2}.
\]

In log coordinates, the antisymmetric component is multiplied by \(|1-2\delta|\). The gated map \(F_\delta=P_\delta\circ F\) has antisymmetric eigenvalue

\[
\lambda_a^{(\delta)}=(1-2\delta)\lambda_a.
\]

**Lemma 3 (Gate threshold).** The gated map is locally stable in the antisymmetric direction if and only if

\[
\delta>\delta_*=\frac{1-1/|\lambda_a|}{2}.
\]

For \(B_{1,1}\), \(\delta_*\approx 0.415\).

The productive gate window is \(\delta_*<\delta<1/2\). At \(\delta=1/2\), full symmetrization erases the antisymmetric mode: the system becomes stable but unable to read coordination gradients.

**Lemma 4 (Operator-level coherent steering).** The gated map satisfies operator-level Coherent Steering, in the sense that the antisymmetric Lyapunov exponent is negative, if and only if

\[
\chi_a(\delta)=\log|\lambda_a|+\log|1-2\delta|<0.
\]

Equivalently, \(\delta>\delta_*\).

---

## 4. The Third Stroke: Adaptive Coherence Steering

### 4.1 Why two strokes are insufficient

Gating removes fast antisymmetric blowup, but the symmetric mode still contracts toward the fixed point \(z_*\). Every surviving two-stroke chain therefore drifts toward a low-entropy attractor. In ACP terms, two strokes slow crystallization but do not arrest it.

### 4.2 The unique local steering stroke

In log coordinates \(a=\log x\), \(b=\log y\), decompose into symmetric and antisymmetric modes:

\[
s=\frac{a+b}{2},
\qquad
r=\frac{a-b}{2}.
\]

A local stroke that restores the productive interval while preserving the CN coordination center must satisfy:

\[
\Delta s=0,
\qquad
\operatorname{Var}(\Delta r)>0.
\]

The first condition requires \(\Delta a=-\Delta b\). The second requires a stochastic perturbation. Together they force, up to amplitude and noise distribution,

\[
N_\varepsilon(x,y)=\left(xe^{\varepsilon \xi},\;ye^{-\varepsilon \xi}\right),
\qquad
\xi\sim\mathcal{N}(0,1).
\]

**Theorem 3 (Uniqueness of the local steering stroke).** Within multiplicative log-space perturbations, \(N_\varepsilon\) is the unique local perturbation direction that (i) preserves the geometric-mean coordination center \(\sqrt{xy}\) and (ii) restores antisymmetric log-lift variance. Symmetric perturbation preserves the ratio but displaces the center; generic perturbation restores variance but breaks the CN invariant unless constrained to \(\xi_x+\xi_y=0\).

This is the operator-level place where the old phrase "anti-crystallization" should now be read as a mechanism, not the project name. \(N_\varepsilon\) is the entropy-restoring move inside adaptive coherence steering.

### 4.3 Linear steady-state prediction

The antisymmetric channel obeys, to first order,

\[
r_{t+1}\approx (1-2\delta)\lambda_a r_t+\varepsilon \xi_t.
\]

When \((1-2\delta)|\lambda_a|<1\), the linearized steady-state variance is

\[
\sigma_r^2=
\frac{\varepsilon^2}{1-(1-2\delta)^2\lambda_a^2}.
\]

Near the diagonal,

\[
\log C(x,y)\approx 2z_*K_{\alpha,\lambda}r,
\]

so the log-lift prediction is

\[
\left\langle |\log C(x,y)| \right\rangle_\infty
\approx
2z_*K_{\alpha,\lambda}
\sqrt{\frac{2}{\pi}}\sigma_r.
\]

The symmetric channel receives no direct first-order noise from \(N_\varepsilon\), since \(\Delta s=0\). Any symmetric plateau width must therefore come from nonlinear coupling, finite-bin measurement, selection effects near the domain boundary, or an intentionally added symmetric noise channel. This correction is important: the third stroke restores coordination-gradient variance without wandering the geometric center.

---

## 5. Simulation Summary

The supplied draft reports simulations initialized near \((z_*,z_*)\), tracking:

- ensemble entropy in log-space,
- mean absolute log-lift \(\langle|\log C(x,y)|\rangle\),
- positive-domain survival rate,
- antisymmetric variance \(\operatorname{Var}(\log x-\log y)\).

The qualitative findings are:

**Two-stroke failure.** Without injection (\(\varepsilon=0\)), all surviving chains show decreasing entropy, regardless of whether the operator is naturally stable or externally gated.

**Three-stroke persistence.** Adding CN-symmetric injection produces entropy plateaus across stable configurations. The plateau level scales with \(\varepsilon\), while domain survival decreases with \(\varepsilon\).

**Coordination-maintained entropy matters.** A plateau is ACP-relevant only if the log-lift remains nonzero. Noise-maintained entropy without coordination signal is spread without legibility; tuned steering preserves both variance and coordination gradient.

**Best reported configuration.** The draft identifies \(B_{0,0.3934}\) with \(\varepsilon=0.005\) as a strong naturally stable case: no external gating, full domain survival to depth 120, nonzero entropy plateau, and nonzero coordination gradient.

**Repository note.** The numerical claims should be treated as bridge evidence until the simulator is added under `Formalization/simulations/` with config snapshots, matching the repository's Prediction 8 and Prediction 9 simulation practice.

---

## 6. The Three-Stroke Engine

The minimal operator algebra consists of three strokes:

| Stroke | Operator | Function | Failure if isolated |
|---|---|---|---|
| Coordination | \(B_{\alpha,\lambda}\), with gating when needed | Reciprocal restraint, endogenous seed | Diagonal flattening, crystallization |
| Generation | \(G(x,y)=e^x-\ln y\) | Re-expansion from seed | Domain escape, dissolution |
| Steering | \(N_\varepsilon(x,y)=(xe^{\varepsilon\xi},ye^{-\varepsilon\xi})\) | Antisymmetric entropy restoration | Noise without coherence if ungated |

The productive engine is the closed cycle:

\[
C \to G \to N_\varepsilon \to C \to G \to N_\varepsilon \to \cdots
\]

### Mapping to adaptive coherence

- **Constraint.** CN forces \(C(x,x)=1\), creating a reciprocal reference point that neither input can unilaterally escape.
- **Alignment.** EML expands the seed \(G(1,z)=e-\ln z\), opening new degrees of freedom from the shared reference.
- **Persistence.** The steering stroke \(N_\varepsilon\) restores the coordination gradient that CN/EML bleeds away, keeping the system off the crystallizing attractor.

The deepest result is not which individual operators persist, but why persistence requires alternation. A single stroke cannot simultaneously coordinate and restore variance. Two strokes coordinate and generate, but still converge. The third stroke breaks the attractor's claim on the ensemble in exactly the dimension the attractor consumes.

---

## 7. Relation to Existing ACP Fronts

### 7.1 Relation to EML

EML establishes generative completeness for elementary functions. The three-stroke engine optimizes for a different property: bounded antisymmetric variance under recursive depth. EML and CN/EML/\(N_\varepsilon\) solve different problems in the space of mathematical primitives.

### 7.2 Relation to the CDT

The antisymmetric Lyapunov exponent \(\chi_a\) is the operator-level analog of the CDT's self-reinforcing drift rate. Gating implements the local Coherent Steering condition: it keeps antisymmetric growth below runaway. The \(N_\varepsilon\) stroke implements the entropy-restoring mechanism that prevents even coherently steered systems from slowly crystallizing.

### 7.3 Relation to OP-7

`OPEN_PROBLEMS.md` currently asks whether coordination-neutral operators preserve CN under tree composition. This note gives a partial answer:

- CN survives under hierarchical block swaps, producing wreath symmetry.
- Full leaf-reversal CN requires the independent joint-inversion condition already isolated in `bridges/coordination_neutrality.md`.
- Persistence is not solved by symmetry alone; it requires a stable/gated CN generator plus an entropy-restoring steering stroke.

This suggests OP-7 should be downgraded from "open" to "partial" and sharpened toward the classification of operator cycles rather than isolated CN operators.

---

## 8. Open Questions

**Ternary compression.** Can the three-stroke cycle be compressed into a single ternary operator satisfying cyclic triple-product neutrality,

\[
T(x,y,z)T(y,z,x)T(z,x,y)=1?
\]

Such an operator would have a variable partial diagonal and could implement coordinated but non-flat self-seeding.

**Global wreath coherence.** Local CN lifts into hierarchical tree symmetry. Does imposing global tree symmetry downward constrain admissible local operators? Operators that violate global wreath coherence may accumulate symmetry residual and lose compositional stability.

**Universality within persistence.** EML is universal for elementary functions. Is there a CN operator, or a finite CN-centered cycle, that is universal for elementary functions while remaining naturally stable?

**Simulation reproducibility.** The reported plateau and survival claims should be reproduced in a dependency-light simulator with explicit config snapshots before the note is promoted from bridge evidence to paper-level result.

---

## References

Odrzywolek, A. (2026). *All elementary functions from a single binary operator*. arXiv:2603.21852 [cs.SC], v2, April 4, 2026.

Project workspace. (2026). *Adaptive Coherence Principle: main framework document v10*. CC0.

Lambert W function: \(W(e^e)\approx 2.01678\), the unique positive solution to \(z+\ln z=e\).
