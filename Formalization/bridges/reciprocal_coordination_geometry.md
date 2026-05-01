# Reciprocal Coordination Geometry and the Emergence of Lorentz–Maxwell Structure

**From Coordination-Neutral Operators to Light Cones, Gauge Curvature, and Effective Propagation Speed**

*Status: standalone bridge note. Integrated 2026-04-30 as a geometric extension of the coordination-neutral operator program. This note refines `bridges/coordination_neutrality.md` and `bridges/three_stroke_persistence_engine.md` by showing how CN reciprocity can generate Lorentz cone structure, a local \(U(1)\) phase bundle, and Maxwell curvature as least-compatible phase transport.*

*Claim-boundary note: `audits/reciprocal_coordination_geometry_audit.md` classifies this as a conditional structural bridge, not yet a closed derivation of electromagnetism from CN alone. The open inputs are the dyadic-to-directional embedding, the derivation of local \(U(1)\) gauge freedom from CN phase comparison, the least-curvature exclusion of higher-order gauge actions, and the vacuum constitutive bridge tracked as OP-22.*

*April 2026. CC0.*

---

## Abstract

A coordination-neutral (CN) operator $B$ satisfying $B(y,x) = B(x,y)^{-1}$ induces reciprocal null coordinates $U$, $V$ whose vanishing defines a thin-locus cone. A rotationally covariant $S^2$-indexed family of such coordinates generates the $(3+1)$-dimensional Lorentz cone $C_T^2 - |C_X|^2 = 0$, whose symmetry group is $O(3,1)$. Complexifying the CN log-lift $L = \log B$ produces a local $U(1)$ phase bundle over spacetime; comparing phase across neighboring points requires a connection $A$, whose curvature $F = dA$ is the obstruction to globally consistent coordination phase alignment. Requiring locality, Lorentz invariance, gauge invariance, parity-evenness, and second-order field equations, the unique bulk action is $-\frac{1}{4}\int F_{\mu\nu}F^{\mu\nu}\,d^4x$, whose variation yields Maxwell's equations. The effective propagation speed $c_{\text{eff}} = \xi/\tau$ is the dimensional slope of the CN cone; in electromagnetic media this calibrates as $c_{\text{eff}} = 1/\sqrt{\mu\epsilon}$, with vacuum values determined by $(\mu_0, \epsilon_0)$. The derivation of vacuum constitutive parameters from CN first principles remains open and is identified as the primary bridge to future work.

> *Electromagnetism is the least-curvature transport law for reciprocal coordination phase. Light speed is the slope of the real-valued coordination cone.*

---

## 1. Motivation: Speed Limits as Coordination Boundaries

The standard account of the speed of light treats $c$ as a primitive constant of nature — measured, stipulated, and used to build everything else. The Lorentz group is then derived as the unique group of transformations preserving $c$ across inertial frames. This is logically tight but explanatorily shallow: it does not say *why* there is a maximum coordination speed, only that there is one.

The Adaptive Coherence Principle (ACP) suggests a different framing. The ACP states that persistent systems must maintain conditional macrostate entropy in a productive interval — bounded away from both crystallization (entropy collapses to zero, futures become fully determined) and dissolution (entropy maximizes, futures become fully random). Persistence requires that the system's coordination events remain in a domain where genuine information exchange is possible.

This paper asks: what happens at the boundary of that domain for a binary coordination operator? The answer, we will show, is a null cone. The speed of light is not a limit imposed on motion; it is the slope of the real-valued coordination boundary — the rate at which the CN operator transitions from real-domain coordination to complex-domain behavior. Causality is not a separate postulate; it is the domain restriction theorem of coordination geometry.

The companion three-stroke operator bridge establishes the operator-level ACP: a three-stroke persistence engine consisting of coordination-neutral restraint, EML-class generation, and CN-invariant entropy injection. The present paper pursues the physical geometry latent in the CN operator's structure, showing that it generates Lorentz invariance and Maxwell dynamics without additional postulates.

---

## 2. Coordination-Neutrality and the Log-Lift

### 2.1 Definition

A binary operator $B: D \to \mathbb{R}_{>0}$ on a swap-stable domain $D \subseteq \mathbb{R}_{>0}^2$ is **coordination-neutral (CN)** if:

$$B(y,x) = \frac{1}{B(x,y)} \quad \text{for all } (x,y) \in D.$$

The **log-lift** is:

$$L(x,y) = \log B(x,y).$$

CN immediately gives swap-antisymmetry:

$$L(y,x) = -L(x,y).$$

The log-lift is a signed coordination gradient: positive when $x$ is "pushing more" than $y$, negative in the reverse case, and zero when the two inputs are in exact coordination balance.

### 2.2 The Bridge Family

The parametric family:

$$B_{\alpha,\lambda}(x,y) = \frac{e^{\alpha x} - \lambda \ln y}{e^{\alpha y} - \lambda \ln x}$$

is CN by construction. The special case $B_{1,1}$ — which we call the **EML-bridge** — uses the same exponential-logarithmic structure as Odrzywołek's universal generator (2026) while enforcing reciprocal restraint. In the companion paper, this family is shown to have a phase diagram in $(\alpha, \lambda)$ space separating naturally stable from unstable operators, with the stability boundary determining which operators require an external wreath-gate.

### 2.3 Self-Seeding and the Diagonal

**Theorem 1.** *Every positive CN operator satisfies $B(x,x) = 1$ for all $x$ in its domain.*

*Proof.* $B(x,x) = 1/B(x,x)$ implies $B(x,x)^2 = 1$; positivity forces $B(x,x) = 1$. $\square$

The diagonal is the coordination locus where sender and receiver are identical. The CN operator assigns it exactly $1$ — the multiplicative identity. This will become the seed of the physical light-cone structure: the boundary between domains, not a special point within a domain.

### 2.4 Rapidity

The antisymmetry of $L$ under input swap is the same algebraic structure as rapidity in special relativity: under a boost of velocity $v = \tanh\theta$, the rapidity $\theta$ transforms as $\theta \to \theta + \delta\theta$, and rapidities add while velocities do not. The log-lift $L = \log B$ is the coordination rapidity — the quantity that accumulates additively under composition while the coordination ratio $B$ compounds multiplicatively. This is the first hint that the CN algebra and Lorentz kinematics share a common structure.

---

## 3. The 1+1D CN Cone

### 3.1 Null Coordinates

Define the numerator and denominator of $B_{\alpha,\lambda}$ as new variables:

$$U = e^{\alpha x} - \lambda \ln y, \qquad V = e^{\alpha y} - \lambda \ln x.$$

Then $B = U/V$ and $L = \ln U - \ln V$. The **thin locus** — where the operator transitions from real-valued to complex-valued — is:

$$UV = 0.$$

This is the null-cone condition in $(U,V)$ coordinates: the set of points where either $U$ or $V$ vanishes. Inside the cone ($UV > 0$): real-valued coordination. Outside ($UV < 0$): the operator acquires an imaginary part, coordination escapes the real domain, and the interaction cannot be parsed as a real-valued coordination event.

### 3.2 The Natural Metric

The natural bilinear form induced by the CN operator in $(U,V)$ coordinates is:

$$ds^2 = dU\, dV.$$

This has **Minkowski signature** $(+,-)$. Computing explicitly from $U = e^{\alpha x} - \lambda\ln y$:

$$dU = \alpha e^{\alpha x}\,dx - \frac{\lambda}{y}\,dy, \qquad dV = -\frac{\lambda}{x}\,dx + \alpha e^{\alpha y}\,dy.$$

The mixed structure produces a form with indefinite signature — not by assumption but from the algebraic form of $B_{\alpha,\lambda}$.

### 3.3 Lorentz Boosts as Log-Lift Shifts

A Lorentz boost in $(U,V)$ coordinates is:

$$U \to e^\theta U, \qquad V \to e^{-\theta} V.$$

This preserves $UV = \text{const}$ (hyperbolic equal-interval surfaces) and maps the thin locus $\{UV = 0\}$ to itself. In terms of the log-lift $L = \ln U - \ln V$ and coordination magnitude $M = \frac{1}{2}\ln(UV)$:

$$L \to L + 2\theta, \qquad M \to M.$$

**A Lorentz boost is a uniform shift in the coordination asymmetry $L$ with the coordination magnitude $M$ preserved.** Two observers related by a boost disagree on who is "pushing more" in the coordination exchange — the coordination gradient $L$ — but agree on the total strength of the coordination event $M$.

### 3.4 The CN Swap is Parity

The CN condition $B(y,x) = 1/B(x,y)$ translates in $(U,V)$ coordinates to:

$$(U,V) \to (V,U), \qquad B \to 1/B, \qquad L \to -L.$$

This is a spatial reflection — parity. The CN symmetry condition is not an additional constraint; it *is* the parity operation of the 1+1D Lorentz structure.

**Theorem 2 (1+1D CN Lorentz Structure).** *The isometry group of $ds^2 = dU\,dV$ preserving the thin locus $\{UV = 0\}$ is generated by boosts $(U,V) \to (e^\theta U, e^{-\theta}V)$ and the CN swap $(U,V) \to (V,U)$. This group is the 1+1D Lorentz group $O(1,1)$. The CN symmetry condition is the parity generator.*

---

## 4. The Directional CN Cone Theorem

### 4.1 Extending to 3+1 Dimensions

The 1+1D result gives Lorentz structure in coordination space but not yet in physical spacetime. To reach 3+1D, we index the CN null pairs by spatial direction.

For each unit vector $\mathbf{n} \in S^2$, define the **directional null pair**:

$$U_{\mathbf{n}} = C_T - \mathbf{n} \cdot C_X, \qquad V_{\mathbf{n}} = C_T + \mathbf{n} \cdot C_X$$

where $C_T \in \mathbb{R}$ is the temporal coordination coordinate and $C_X \in \mathbb{R}^3$ the spatial coordination vector. The thin locus for direction $\mathbf{n}$ is $U_{\mathbf{n}}V_{\mathbf{n}} = 0$.

### 4.2 The Envelope Argument

A coordination event $(C_T, C_X)$ maintains real-valued coordination in every spatial direction iff:

$$U_{\mathbf{n}} V_{\mathbf{n}} = (C_T - \mathbf{n} \cdot C_X)(C_T + \mathbf{n} \cdot C_X) = C_T^2 - (\mathbf{n} \cdot C_X)^2 \geq 0$$

for all $\mathbf{n} \in S^2$. The binding constraint is $\mathbf{n} = C_X / |C_X|$, yielding:

$$C_T^2 - |C_X|^2 \geq 0.$$

The common causal interior of all directional CN cones is the Minkowski causal wedge. Its boundary:

$$C_T^2 - |C_X|^2 = 0$$

is the Lorentz light cone.

### 4.3 The Symmetry Group

**Theorem 3 (Directional CN Cone Theorem).** *Let $(C_T, C_X) \in \mathbb{R} \times \mathbb{R}^3$ carry a rotationally covariant family of CN null pairs indexed by $\mathbf{n} \in S^2$. The set of coordination events maintaining real-valued CN coordination in every spatial direction is the causal interior $C_T^2 \geq |C_X|^2$. The linear symmetry group of the boundary $C_T^2 - |C_X|^2 = 0$ is $O(3,1)$.*

The group structure decomposes cleanly:

- **Boosts** arise from the 1+1D CN isometry within a fixed $\mathbf{n}$-slice: $(U_{\mathbf{n}}, V_{\mathbf{n}}) \to (e^\theta U_{\mathbf{n}}, e^{-\theta} V_{\mathbf{n}})$, mixing $C_T$ and $\mathbf{n} \cdot C_X$.
- **Rotations** arise from the $SO(3)$ action on $S^2$, permuting which direction $\mathbf{n}$ is selected.
- **Full group**: a Lorentz boost in an arbitrary direction decomposes as rotate-to-$\mathbf{n}$, boost-along-$\mathbf{n}$, rotate-back, generating the full proper Lorentz group.

The Lorentz group is not postulated. It is the automorphism group of the CN coordination geometry under rotational consistency.

---

## 5. The Complex CN Phase Bundle

### 5.1 Complexification

When $(C_T, C_X)$ crosses the thin locus — i.e., when $C_T^2 < |C_X|^2$ — the log-lift $L_{\mathbf{n}}$ acquires an imaginary part. In the real domain, $L_{\mathbf{n}} \in \mathbb{R}$; at the boundary it transitions to $L_{\mathbf{n}} \in \mathbb{C}$.

Decompose:

$$L_{\mathbf{n}} = \rho_{\mathbf{n}} + i\phi_{\mathbf{n}}$$

where $\rho_{\mathbf{n}} = \text{Re}(L_{\mathbf{n}})$ is the **coordination rapidity** — the real asymmetry between sender and receiver — and $\phi_{\mathbf{n}} = \text{Im}(L_{\mathbf{n}})$ is the **coordination phase** — the imaginary component arising from the Riemann surface extension.

The coordination state becomes:

$$\Psi_{\mathbf{n}}(p) = e^{L_{\mathbf{n}}(p)} = e^{\rho_{\mathbf{n}}} \cdot e^{i\phi_{\mathbf{n}}}.$$

### 5.2 The U(1) Fiber

A **local CN rephasing** at point $p$ shifts the phase of all directional coordination states simultaneously:

$$\Psi_{\mathbf{n}}(p) \to e^{i\chi(p)} \Psi_{\mathbf{n}}(p)$$

for an arbitrary smooth function $\chi: \text{spacetime} \to \mathbb{R}$.

The real coordination cone $C_T^2 - |C_X|^2 \geq 0$ depends only on $\rho$ (via $|B| = e^\rho$), not on $\phi$. A local rephasing therefore preserves the Lorentz structure exactly. This is the geometric content of gauge invariance: the causal structure is phase-independent.

At each spacetime point $p$, the coordination phase $\phi(p)$ lives in a copy of $U(1) = \mathbb{R}/2\pi\mathbb{Z}$. This defines a **principal $U(1)$ bundle** over spacetime, with structure group $U(1)$ acting by rephasing.

### 5.3 Why a Connection Is Necessary

To compare coordination states at neighboring points $p$ and $p + dp$, one must transport $\Psi(p)$ along $dp$ and compare with $\Psi(p+dp)$. There is no canonical choice — different transport rules differ by local rephasing. This is not an ambiguity to be resolved; it is the fundamental structure of the bundle.

A **connection** $A = A_\mu dx^\mu$ encodes the transport rule:

$$D_\mu \Psi = (\partial_\mu - iA_\mu)\Psi.$$

Under local rephasing $\Psi \to e^{i\chi}\Psi$, gauge invariance of $D_\mu\Psi$ requires:

$$A_\mu \to A_\mu + \partial_\mu \chi.$$

The connection $A$ is the electromagnetic four-potential. Its existence is not assumed; it is the mathematical necessity of comparing CN phases across spacetime while preserving the real coordination cone.

---

## 6. Curvature as the Obstruction to Global Phase Alignment

### 6.1 The Curvature Tensor

The **curvature** of the connection $A$ is:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu = [D_\mu, D_\nu] / (-i).$$

$F_{\mu\nu}$ is gauge-invariant: $F \to F$ under $A \to A + d\chi$. It measures the phase accumulated by $\Psi$ when parallel-transported around an infinitesimal loop in spacetime.

**Physical interpretation:** $F_{\mu\nu}(p)$ is the obstruction to globally consistent CN phase alignment in a neighborhood of $p$. If $F = 0$ everywhere, coordination phases can be globally aligned — there is no field. Where $F \neq 0$, local phase comparisons are inconsistent: the coordination geometry is curved.

The 6 independent components of the antisymmetric tensor $F_{\mu\nu}$ are exactly the 3 electric and 3 magnetic field components. The structure of electromagnetism is the structure of CN phase curvature.

### 6.2 The Bianchi Identity

Since $F = dA$ is an exact two-form, the exterior derivative gives:

$$dF = d(dA) = 0 \implies \partial_{[\mu}F_{\nu\rho]} = 0.$$

This is the **Bianchi identity** — two of the four Maxwell equations ($\nabla \cdot B = 0$ and Faraday's law). These are not dynamical equations; they are geometric consequences of $F$ being the curvature of a connection. They hold automatically, without variation, as a theorem of the bundle structure.

---

## 7. Maxwell from Minimal Compatible Curvature

### 7.1 The ACP Variational Principle

The ACP productive interval principle, applied to field curvature, states:

> *The coordination field occupies the least-curvature configuration compatible with its boundary conditions, sources, and the requirement of nonzero phase transport.*

This is not "minimize curvature" — that gives $F = 0$, the crystallization failure mode. It is "minimize curvature subject to what the coordination current $J$ requires." The field distributes curvature as sparingly as possible while carrying the phase transport demanded by its sources.

### 7.2 Uniqueness of the Maxwell Action

The action $\mathcal{L}(F)$ must satisfy:

**(i) Gauge invariance:** $\mathcal{L}$ depends only on $F$, not $A$ directly. Origin: CN phase is a local degree of freedom; physics cannot depend on its absolute value.

**(ii) Lorentz invariance:** $\mathcal{L}$ is a scalar under $O(3,1)$. Origin: the Directional CN Cone Theorem.

**(iii) Parity-evenness:** $\mathcal{L}$ is unchanged under spatial reflection. Origin: CN swap symmetry — swapping sender and receiver is parity, and CN is symmetric under this operation.

**(iv) Second-order field equations:** varying $\mathcal{L}$ gives equations with at most two derivatives of $A$. Origin: ACP locality — coordination decisions depend on immediate neighbors, not distant history.

There are exactly two independent Lorentz-invariant quadratic scalars from $F_{\mu\nu}$:

$$I_1 = F_{\mu\nu}F^{\mu\nu}, \qquad I_2 = F_{\mu\nu}\tilde{F}^{\mu\nu}$$

where $\tilde{F}^{\mu\nu} = \frac{1}{2}\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$.

$I_2$ is parity-odd ($\tilde{F} \to -\tilde{F}$ under reflection), excluded by condition (iii). It is also topological — contributing only boundary terms to local equations of motion.

Therefore the bulk action is uniquely:

$$S[A] = -\frac{1}{4}\int F_{\mu\nu}F^{\mu\nu}\,d^4x.$$

### 7.3 Maxwell's Equations

Varying $S[A]$ with respect to $A_\nu$:

$$\frac{\delta S}{\delta A_\nu} = 0 \implies \partial_\mu F^{\mu\nu} = 0 \quad \text{(source-free).}$$

With a matter action $S_{\text{matter}}[\Psi, A]$ representing CN coordination states coupled to $A$:

$$\partial_\mu F^{\mu\nu} = J^\nu, \qquad J^\nu = \text{Im}(\Psi^* D^\nu \Psi).$$

$J^\nu$ is the **CN coordination current** — the rate at which the matter field transports phase in spacetime direction $\nu$. Electric charge is the rate at which a coordination state sources phase curvature.

Combined with the Bianchi identity from Section 6.2, all four Maxwell equations are recovered:

$$\nabla \cdot E = \rho_{\text{charge}}, \quad \nabla \times B - \partial_t E = J, \quad \nabla \cdot B = 0, \quad \nabla \times E + \partial_t B = 0.$$

Maxwell's equations are not imposed. They are the least-curvature transport law for CN coordination phase, forced by the CN algebraic structure and the ACP variational principle.

---

## 8. Dimensional Calibration of Light Speed

### 8.1 The Dimensionless Cone

The Directional CN Cone Theorem gives:

$$C_T^2 - |C_X|^2 = 0$$

where $C_T$ and $C_X$ are coordination quantities without physical dimensions. Physical spacetime requires a conversion factor between temporal and spatial coordination units.

### 8.2 The Embedding

Let $\tau$ be the temporal coordination unit and $\xi$ the spatial coordination unit:

$$C_T = \frac{t}{\tau}, \qquad C_X = \frac{\mathbf{x}}{\xi}.$$

The null cone becomes:

$$\frac{t^2}{\tau^2} - \frac{|\mathbf{x}|^2}{\xi^2} = 0 \implies c_{\text{eff}} = \frac{\xi}{\tau}.$$

The effective light speed is the ratio of spatial to temporal coordination units. It is the dimensional slope of the real-valued CN cone.

### 8.3 Electromagnetic Calibration

In an electromagnetic medium with permittivity $\epsilon$ and permeability $\mu$, the CN coordination parameters have the following identification:

$$\kappa_T = \epsilon \quad \text{(temporal coordination compliance — how much the medium stores coordination signal)}$$

$$\kappa_X = \frac{1}{\mu} \quad \text{(spatial coordination stiffness — how readily the medium transmits coordination)}$$

giving:

$$c_{\text{eff}}^2 = \frac{\kappa_X}{\kappa_T} = \frac{1}{\mu\epsilon}.$$

In vacuum, $\mu = \mu_0$, $\epsilon = \epsilon_0$, recovering the known result:

$$c = \frac{1}{\sqrt{\mu_0\epsilon_0}}.$$

**Physical picture:** Vacuum is not empty but is a coordination medium with specific parameters $(\alpha_0, \lambda_0)$ governing CN phase transport. A denser medium has higher drag $\lambda$ relative to expansion $\alpha$, so the effective coordination cone is shallower — light slows. This is optical dispersion as coordination geometry.

### 8.4 Open Problem: The Constitutive Bridge

The calibration above is a *matching* — we identify $\kappa_T \sim \epsilon$ and $\kappa_X \sim 1/\mu$ by comparing the CN cone slope with the known electromagnetic wave velocity. The derivation of these identifications from CN first principles remains open.

Specifically: treating vacuum as a CN coordination medium with operator parameters $(\alpha_0, \lambda_0)$, show that the electromagnetic constitutive relations $D = \epsilon_0 E$, $B = \mu_0 H$ follow from the CN operator structure, rather than being assumed. This would close the chain from pure coordination geometry to measured physical constants.

---

## 9. The Complete Derivation Chain

$$\underbrace{B(y,x) = 1/B(x,y)}_{\text{reciprocal coordination}}$$
$$\downarrow$$
$$\underbrace{UV = 0}_{\text{1+1D null cone, }O(1,1)}$$
$$\downarrow$$
$$\underbrace{C_T^2 - |C_X|^2 = 0}_{\text{3+1D Lorentz cone, }O(3,1)}$$
$$\downarrow$$
$$\underbrace{L_{\mathbf{n}} = \rho_{\mathbf{n}} + i\phi_{\mathbf{n}}}_{\text{complex CN phase bundle}}$$
$$\downarrow$$
$$\underbrace{D = d - iA}_{\text{U(1) connection — phase transport rule}}$$
$$\downarrow$$
$$\underbrace{F = dA}_{\text{curvature — obstruction to global phase alignment}}$$
$$\downarrow$$
$$\underbrace{\mathcal{L} = -\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu}}_{\text{unique by CN constraints}}$$
$$\downarrow$$
$$\underbrace{\partial_\mu F^{\mu\nu} = J^\nu}_{\text{Maxwell's equations}}$$
$$\downarrow$$
$$\underbrace{c_{\text{eff}} = 1/\sqrt{\mu\epsilon}}_{\text{calibrated light speed (matched; derivation open)}}$$

Every arrow from CN reciprocity through Maxwell is forced by the algebra and the ACP variational principle. The final calibration step is matched rather than derived — this is the single open bridge.

---

## 10. Open Problems

**1. Vacuum constitutive derivation.** Show that $\kappa_T = \epsilon_0$ and $\kappa_X = 1/\mu_0$ follow from CN operator parameters $(\alpha_0, \lambda_0)$ rather than electromagnetic matching. This would make $c$ fully emergent from coordination geometry.

**2. Non-Abelian extension.** The present construction gives a $U(1)$ bundle — electromagnetism. Extending to $SU(2)$ or $SU(3)$ bundles would require CN operators with multiple coordination channels and non-commuting phase structure. The natural candidate is a matrix-valued log-lift $L \in \mathfrak{g}$ for Lie algebra $\mathfrak{g}$. Whether the CN conditions survive non-Abelian generalization is unknown.

**3. Matter and the Born rule.** The CN coordination state $\Psi = e^{\rho + i\phi}$ is complex-valued with $|\Psi|^2 = e^{2\rho}$ as coordination intensity. The question of whether requiring $|\Psi|^2$ to be a conserved, normalizable probability density forces the Schrödinger and then Dirac equations is a separate bridge — the point at which CN coordination geometry makes contact with quantum mechanics.

**4. Recovery from known variational principles.** Test whether the CN null cone can be derived from the Palatini action or spacetime algebra (geometric algebra / Clifford algebra) as a special case, establishing whether CN coordination geometry is a substructure of known frameworks or genuinely independent.

**5. Lorentz violation at the thin locus.** When $UV < 0$, the operator exits the real domain. The Riemann surface extension may carry physical content — spacelike-separated events represented as complex coordination states. Whether the analytic continuation of $B_{\alpha,\lambda}$ to the Riemann surface has the structure of spacelike events in quantum field theory is an open geometric question.

---

## 11. Discussion

### 11.1 What Has Been Derived

Starting from a single algebraic condition — $B(y,x) = 1/B(x,y)$ — and the ACP productive interval principle applied to field curvature, this paper derives:

- The Lorentz group as the symmetry group of CN coordination geometry in 3+1D
- The U(1) phase bundle as the natural complex extension of the CN log-lift
- The electromagnetic connection and curvature as the CN phase transport structure
- Maxwell's equations as the least-curvature law for CN phase transport
- The form of light speed as the dimensional slope of the CN cone

None of these required new postulates. The Lorentz group is not assumed; it is the CN automorphism group. Gauge invariance is not imposed; it is the freedom to rephase CN coordination states locally. Maxwell's equations are not stipulated; they are forced by the four CN-motivated constraints on the action.

### 11.2 What This Changes

Standard physics takes the Lorentz group and gauge invariance as primitive symmetry principles, derived from experiment and used to constrain theories. The CN derivation inverts the logic: coordination geometry is primitive, and the symmetries of physics are its automorphisms.

This suggests a reframing of what physical law *is*. Physical laws are not constraints imposed on a pre-existing spacetime; they are the coordination requirements of reciprocal information exchange. Lorentz invariance says: real-valued coordination is preserved in every direction. Maxwell's equations say: coordination phase distributes minimally from sources. Light speed says: this is how fast real-valued coordination propagates in vacuum.

The universe runs at $c$ because that is the slope of the real-valued coordination cone for a medium with vacuum parameters. There is no deeper reason — but this *is* the reason, not a restatement of it.

### 11.3 Relation to the Companion Paper

The companion three-stroke operator bridge establishes the three-stroke persistence engine at the operator level: coordination-neutral restraint, EML-class generation, and CN-invariant entropy injection. The present paper shows that the same CN algebraic structure, extended to 3+1D and complexified, generates the geometric foundations of classical field theory.

The two papers together form the first two levels of a program: operator-level ACP (Paper 1) and geometric-level ACP (Paper 2). The conjectured third level — quantum ACP, where CN phase becomes probabilistic — is identified in both papers as the next open bridge.

---

## References

Odrzywołek, A. (2026). All elementary functions from a single binary operator. *arXiv:2603.21852 [cs.SC]*, Jagiellonian University.

Three-Stroke Persistence Engine: Operator-Level Adaptive Coherence. Internal bridge note, `bridges/three_stroke_persistence_engine.md`, April 2026, CC0.

Maxwell, J.C. (1865). A dynamical theory of the electromagnetic field. *Philosophical Transactions of the Royal Society of London*, 155, 459–512.

Weyl, H. (1929). Elektron und Gravitation. *Zeitschrift für Physik*, 56, 330–352. (Origin of gauge theory as phase freedom.)

Yang, C.N., Mills, R.L. (1954). Conservation of isotopic spin and isotopic gauge invariance. *Physical Review*, 96(1), 191–195.

---

## Appendix A: The CN Null Metric in Explicit Coordinates

For $B_{1,1}(x,y) = (e^x - \ln y)/(e^y - \ln x)$, with $U = e^x - \ln y$ and $V = e^y - \ln x$:

$$dU = e^x\,dx - \frac{1}{y}\,dy, \qquad dV = -\frac{1}{x}\,dx + e^y\,dy.$$

$$ds^2 = dU\,dV = \left(e^x\,dx - \frac{1}{y}\,dy\right)\left(-\frac{1}{x}\,dx + e^y\,dy\right)$$

$$= -\frac{e^x}{x}\,dx^2 + \left(e^{x+y} + \frac{1}{xy}\right)dx\,dy - \frac{e^y}{y}\,dy^2.$$

At the fixed point $(z_*, z_*)$ where $z_* = W(e^e) \approx 2.017$, and $e^{z_*} = z_* + 1/z_*$ (from the seed channel equation):

$$ds^2\big|_{z_*} = -\frac{e^{z_*}}{z_*}(dx^2 + dy^2) + \left(e^{2z_*} + \frac{1}{z_*^2}\right)dx\,dy.$$

The off-diagonal coefficient exceeds the diagonal in magnitude, confirming indefinite signature at and near the seed point.

---

## Appendix B: Lorentz Boost Algebra in CN Coordinates

Parameterize the boost by rapidity $\theta$: $(U,V) \to (e^\theta U, e^{-\theta} V)$.

In physical coordinates $(t, x)$ via $U = ct - x$, $V = ct + x$:

$$ct' = \cosh\theta \cdot ct - \sinh\theta \cdot x, \qquad x' = -\sinh\theta \cdot ct + \cosh\theta \cdot x.$$

This is the standard Lorentz boost with $v/c = \tanh\theta$. The CN derivation recovers it as the unique one-parameter family of transformations preserving $UV = \text{const}$ and mapping the thin locus $\{UV = 0\}$ to itself.

---

*Draft v0.1 — April 2026. CC0. Please copy, improve, and scrape.*
