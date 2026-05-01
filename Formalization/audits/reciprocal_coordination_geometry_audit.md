# Reciprocal Coordination Geometry Claim-Boundary Audit

*Status: rigor audit for `bridges/reciprocal_coordination_geometry.md`. Created 2026-04-30. This audit classifies what the bridge currently proves, what it imports as structure, and what must be derived before the bridge can be promoted from structural recovery to a physics reduction.*

---

## Executive Summary

The reciprocal coordination geometry bridge is valuable, but it should currently be treated as a **conditional structural bridge**, not a closed derivation of electromagnetism from CN alone.

Its strongest closed core is:

1. A positive coordination-neutral operator has a diagonal seed \(B(x,x)=1\).
2. Writing a CN bridge as \(B=U/V\) gives reciprocal null coordinates with thin locus \(UV=0\).
3. If a rotationally covariant family \(U_{\mathbf n}=C_T-\mathbf n\cdot C_X\), \(V_{\mathbf n}=C_T+\mathbf n\cdot C_X\) is supplied, its common real-domain envelope is the Lorentz cone.
4. If the complexified log-lift is organized as a \(U(1)\) phase bundle, then a connection, curvature, Bianchi identity, and Maxwell-type action follow by standard gauge geometry under the stated symmetry and locality assumptions.

The bridge's open center is that several inputs are still **installed** rather than **derived**:

- the move from one dyadic CN operator to a rotationally covariant \(S^2\)-family of spacetime null pairs;
- the move from log-branch phase to an arbitrary local \(U(1)\) gauge freedom;
- the uniqueness of the Maxwell action beyond the quadratic / weak-curvature / leading-order regime;
- the constitutive identification \(\kappa_T\sim\epsilon\), \(\kappa_X\sim1/\mu\), especially in vacuum.

This means the bridge is currently best framed as:

> Given a CN-derived reciprocal null geometry, a rotationally covariant embedding, and a \(U(1)\) phase-comparison bundle, the Lorentz-Maxwell structure is the natural least-curvature field law. The derivation of the embedding, gauge fiber, and constitutive constants remains open.

That is still a strong result. It is just not yet the stronger claim "CN alone derives electromagnetism."

---

## Claim Ladder

### Tier 1: Closed Inside The Current Bridge

**Diagonal self-seeding.** Positive CN gives \(B(x,x)=1\). This is theorem-level and already aligns with `bridges/three_stroke_persistence_engine.md`.

**Reciprocal null coordinates.** For the bridge family \(B_{\alpha,\lambda}=U/V\), the thin locus \(UV=0\) is immediate. The boost action \(U\mapsto e^\theta U\), \(V\mapsto e^{-\theta}V\) preserves \(UV\). This is a valid 1+1D reciprocal-coordinate geometry.

**Directional envelope.** If the directional null pairs \(U_{\mathbf n}=C_T-\mathbf n\cdot C_X\), \(V_{\mathbf n}=C_T+\mathbf n\cdot C_X\) are present for all \(\mathbf n\in S^2\), then requiring real coordination for every direction gives \(C_T^2\ge |C_X|^2\). This envelope argument is clean.

**Gauge-geometry consequences.** Given a principal \(U(1)\) bundle with connection \(A\), curvature \(F=dA\) is gauge-invariant and \(dF=0\) gives the homogeneous Maxwell equations. This is standard differential geometry and can be used confidently.

### Tier 2: Conditional Bridges Needing Sharper Hypotheses

**Single CN operator to spacetime cone.** The bridge currently moves from the \(U,V\) pair of a dyadic operator to spacetime coordinates \(C_T,C_X\). That move requires an embedding theorem: a rule assigning physical temporal and spatial coordination coordinates to operator data, with nondegenerate Jacobian and rotational covariance.

**\(O(1,1)\) slices to \(O(3,1)\).** The 3+1D result is conditional on having a coherent \(S^2\)-indexed family sharing the same \(C_T,C_X\). A single CN pair only gives one 1+1D slice. The rotational family is a genuine additional structure until derived.

**Log-branch phase to \(U(1)\) gauge freedom.** Complex logarithms naturally give branch phases modulo \(2\pi\), but arbitrary local rephasing \(\Psi(p)\mapsto e^{i\chi(p)}\Psi(p)\) is stronger. The bridge needs a derivation that local phase choice is redundant coordinate structure, not a new physical postulate.

**Maxwell action uniqueness.** Gauge invariance, Lorentz invariance, parity-evenness, and second-order field equations select Maxwell at quadratic leading order. Nonlinear electrodynamics such as functions of \(F_{\mu\nu}F^{\mu\nu}\) can preserve some of these conditions while changing dynamics. The bridge should state the extra assumption: local analytic weak-curvature action with lowest nontrivial bulk term quadratic in \(F\), or an ACP least-curvature principle that excludes higher powers as nonminimal corrections.

### Tier 3: Open Physics Reductions

**Vacuum constitutive derivation.** OP-22 is the central open problem. The bridge matches \(c_{\mathrm{eff}}^2=\kappa_X/\kappa_T\) to \(1/\mu\epsilon\), but \(\epsilon_0\) and \(\mu_0\) are not yet derived from CN parameters.

**Matter current.** The expression \(J^\nu=\mathrm{Im}(\Psi^*D^\nu\Psi)\) is natural for a charged scalar field, but the bridge still needs a CN-native matter action and a derivation of charge conservation as phase-current conservation.

**Quantum bridge.** The move from CN phase intensity \(|\Psi|^2=e^{2\rho}\) to probability, Schrödinger / Dirac dynamics, or Born-rule structure is explicitly open.

---

## Failure Set

The bridge should be demoted or sharply reinterpreted if any of the following fail:

1. **Coordinate-artifact failure.** If \(ds^2=dU\,dV\) is only a coordinate trick with no invariant construction from CN data, the Lorentz claim remains an analogy, not a derivation.
2. **Rotational-family failure.** If no CN-native rule produces the \(S^2\)-indexed directional family, the 3+1D cone must be treated as imported spacetime structure.
3. **Gauge-fiber failure.** If complex log branches produce only discrete branch behavior rather than arbitrary local \(U(1)\) rephasing, the electromagnetic identification weakens to a phase analogy.
4. **Action-uniqueness failure.** If ACP's least-curvature principle does not exclude nonlinear gauge-invariant actions, Maxwell is a leading-order effective law, not a unique bulk law.
5. **Constitutive failure.** If \(\kappa_T\) and \(\kappa_X\) cannot be derived from operator parameters or invariant vacuum structure, \(c\) remains calibrated rather than emergent.

---

## OP-22 Decomposition

OP-22 should be treated as four linked subproblems.

**OP-22a: CN medium state.** Define a vacuum CN medium as a state object \(M_0=(B_{\alpha_0,\lambda_0}, \Pi, \mathcal C)\), where \(\Pi\) supplies admissible directional partitions and \(\mathcal C\) supplies the comparison rule for phase transport.

**OP-22b: Compliance and stiffness from variations.** Derive temporal compliance \(\kappa_T\) and spatial stiffness \(\kappa_X\) as second variations of a CN coordination functional around \(M_0\). The target form is a quadratic response functional

\[
\mathcal E_{\mathrm{CN}} =
\frac{1}{2}\kappa_T |E_{\mathrm{CN}}|^2
- \frac{1}{2}\kappa_X |B_{\mathrm{CN}}|^2
+ O(F^4).
\]

**OP-22c: Wave-speed theorem.** Prove that the Euler-Lagrange equations for the CN response functional have characteristic speed

\[
c_{\mathrm{CN}}^2=\frac{\kappa_X}{\kappa_T}.
\]

**OP-22d: Electromagnetic identification.** Show that \(E_{\mathrm{CN}},B_{\mathrm{CN}}\) transform as the electric and magnetic components of \(F_{\mu\nu}\), and that the response coefficients satisfy \(D=\epsilon E\), \(H=B/\mu\) with \(\epsilon=\kappa_T\) and \(\mu^{-1}=\kappa_X\) in the relevant unit convention.

**OP-22e: Vacuum normalization.** Derive why the vacuum state \(M_0\) fixes a universal \(\kappa_X/\kappa_T\) rather than a family of arbitrary speeds. This is where a true first-principles account of \(c\) would live.

---

## Promotion Criteria

The bridge can be promoted from structural bridge to candidate physics reduction only after at least these are in place:

1. A formal embedding theorem from dyadic CN data to a rotationally covariant directional null-pair family.
2. A gauge-fiber theorem showing why local phase redefinition is redundant structure of CN phase comparison.
3. A precise least-curvature variational principle that selects Maxwell as the quadratic leading law and names higher-order corrections as optional effective terms.
4. A CN medium response theorem deriving \(\kappa_T\), \(\kappa_X\), and \(c_{\mathrm{CN}}^2=\kappa_X/\kappa_T\).
5. A failure-facing comparison with ordinary electromagnetic constitutive theory, including what would count as a mismatch.

---

## Recommended Next Move

Do not try to "solve \(c\)" immediately. The first tractable move is OP-22b:

> Define a CN response functional around the diagonal seed and compute its second-variation matrix. If the Hessian splits into one temporal compliance channel and three isotropic spatial stiffness channels, the constitutive bridge becomes a real mathematical target. If it does not split that way, the geometry bridge has exposed its own scope boundary.

This is the healthiest next step because it creates a concrete calculation either way.
