# Cosmic Censorship as Restraint — A.20 applied to the Causal-Structure Partition

*Status: proposed bridge. Core identification: **conjectured with structural argument**. Formal claims are marked proven / conjectured / open.*

*Companion documents: `bridges/restraint_power.md` (A.20, the Restraint-Power Theorem); `special_cases/acp_special_cases_v03.md` §5.4 (lighter-weight reduction of Penrose-Hawking / cosmic censorship under the persistence-prior axiom); `bridges/schur_complement.md` (the partitioned-precision picture A.20 inherits).*

---

## 1. Motivation and prior coverage

The Penrose-Hawking singularity theorems and the cosmic censorship conjecture are already discussed in the special-cases catalog (§5.4). That treatment establishes:

- singularities are limits of the classical description, not realized C-states (persistence-prior axiom);
- black hole interiors are productive-interval reorganizations, not crystallization;
- the Big Bang is an anti-crystallization release event, not crystallization of geometry;
- cosmic censorship is consistent with the framework.

What the §5.4 treatment does *not* do is identify the horizon as a **restraint quantity** in the A.20 sense. A.20, added after §5.4, provides the exact machinery needed: the Restraint-Power Theorem (A.20.14) applied to a subsystem partition forces the most concentrated subsystem to perform a decodable coordination transfer before breach, and the Heisenberg principle is the quantum-scale instantiation of the resulting floor (A.20.27).

This bridge upgrades §5.4 from "consistent with the ACP" to "a formal corollary of A.20 under a causal-structure subsystem partition." Doing so places cosmic censorship alongside Heisenberg as a second physics-layer instantiation of the restraint-power coordination floor. It also supplies the promised derivation that §5.4 flagged in Prediction GR-1 as "strengthens Penrose's conjecture from a separate postulate of GR to a structural consequence of persistence."

## 2. The causal-structure subsystem partition

### 2.1 Definition

We apply the subsystem partition of A.20.2.1 to a spacetime $(\mathcal M, g)$ containing a region of gravitational collapse.

***Definition 2.1 (Causal-structure partition).*** Let $(\mathcal M, g)$ be a spacetime admitting a Cauchy surface $\Sigma$, and let $\mathcal H \subset \mathcal M$ be a smooth, timelike-bounded, achronal hypersurface partitioning $\mathcal M$ into two connected regions $\mathcal M_{\mathrm{int}}$ (interior; on the "trapped-surface" side of $\mathcal H$) and $\mathcal M_{\mathrm{ext}}$ (exterior; containing $\mathcal I^+$ if it exists). We call $\mathcal H$ the *partitioning hypersurface*. The **causal-structure partition** is the induced decomposition of the internal macrostate space $M_I$ of the spacetime system into
$$ M_I \;=\; M_{\mathrm{int}} \oplus M_{\mathrm{ext}}, $$
where $M_{\mathrm{int}}$ is the space of macrostates supported on $\mathcal M_{\mathrm{int}}$ and $M_{\mathrm{ext}}$ is the space of macrostates supported on $\mathcal M_{\mathrm{ext}}$.

*Remark 2.2.* The partition is natural because $\mathcal H$ is the only geometric surface across which causal propagation is structurally constrained (for an event horizon, strictly one-way; for a general achronal surface, by its null structure). In A.20 language, the partition is natural whenever the partitioning hypersurface induces a physical restriction on the off-diagonal coupling blocks $B_{\mathrm{int,ext}}$ — cf. Definition A.20.1(b).

### 2.2 Coordination blocks of the partition

Following A.20.2.2, we write the conditional macrostate entropy $H(m'|m)$ for the spacetime system as
$$ H(m'|m) \;=\; C_{\mathrm{int}} \;+\; C_{\mathrm{ext}} \;+\; C_{\mathrm{int,ext}}, $$
with the three coordination capacities in the sense of Definitions A.20.4 and A.20.5.

- $C_{\mathrm{ext}}$: the future-bearing dynamics of the exterior — structure formation, gravitational radiation, matter dynamics, the ordinary content of relativistic astrophysics on $\mathcal M_{\mathrm{ext}}$.
- $C_{\mathrm{int}}$: the future-bearing dynamics of the interior — whatever the reorganized classical-breakdown regime admits (classical GR says: approach to caustic; §5.4 Theorem 5.4.3 says: reorganization processes the coordination imbalance).
- $C_{\mathrm{int,ext}}$: the coupling capacity — the residual conditional correlation between interior and exterior, mediated by the partitioning hypersurface.

***Proposition 2.3 (Horizon as coordination-coupling quantity).*** For the partition of Definition 2.1 with $\mathcal H$ an event horizon in the sense of classical GR (the boundary of the causal past of future null infinity), the coupling capacity $C_{\mathrm{int,ext}}$ is bounded above by a function monotonically tied to the horizon area:
$$ C_{\mathrm{int,ext}}(t) \;\leq\; \frac{A(\mathcal H \cap \Sigma_t)}{4\ell_P^2} \cdot k_B \log 2, $$
with equality (up to $O(1)$ factors) in the quasi-stationary regime.

*Status: proven from standard GR + Bekenstein-Hawking, given the identification of $C_{\mathrm{int,ext}}$ with the Bekenstein-Hawking entropy interpreted as interface-budget rather than stored-entropy (§5.4 Lemma 5.4.2(iv)).*

*Sketch.* The Bekenstein-Hawking entropy $S_{BH} = A / 4\ell_P^2$ counts the number of orthogonal interior microstates distinguishable from outside — exactly the count whose logarithm is the conditional macrostate entropy of the cross-partition correlation. The §5.4 reframing (Lemma 5.4.2(iv)) has already argued that this quantity is an interface budget rather than a stored-entropy count; under that reading, $S_{BH}$ *is* $C_{\mathrm{int,ext}}$, and the inequality is saturation of that identification. ∎

### 2.3 Concentration, and the identification of "exterior" as the most concentrated subsystem

Definition A.20.8 gives the coordination concentration $\gamma_i = C_i / C_{\mathrm{tot}}$. In the causal-structure partition, during a generic gravitational collapse approaching the classical C-limit, $C_{\mathrm{ext}}$ is macroscopic (the ordinary astrophysical content of the exterior), $C_{\mathrm{int}}$ is classically divergent toward zero (the internal block degenerates as Raychaudhuri convergence proceeds), and $C_{\mathrm{int,ext}}$ is bounded by horizon area.

During collapse *before* horizon formation, the configuration that would classically produce a naked singularity has $C_{\mathrm{ext}}$ macroscopic, $C_{\mathrm{int}}$ degenerating, and $C_{\mathrm{int,ext}}$ *not bounded by an area-law interface budget* because there is no enclosing horizon. In A.20 terms, the partition's off-diagonal coupling is unrestricted, and the exterior subsystem is the most concentrated ($i^* = \mathrm{ext}$).

## 3. A.20 applied: restraint at the collapse boundary

### 3.1 The Restraint-Power obligation on the exterior

Applying Theorem A.20.14 (Restraint-Power) to the causal-structure partition with $i^* = \mathrm{ext}$:

***Claim 3.1 (Restraint obligation on spacetime under collapse).*** Let $(\mathcal M, g)$ be a spacetime undergoing gravitational collapse such that $dC_{\mathrm{tot}}/dt < 0$ (classical CDT drift toward the crystallization boundary via Raychaudhuri convergence, §5.4 Lemma 5.4.2(ii)). Then the spacetime retains future-bearing dynamics past the classical collapse time $\tau_*$ (the time at which classical GR predicts geodesic incompleteness) only if:

(a) the exterior subsystem undergoes a coordination transfer before $\tau_*$, in the sense of Definition A.20.13; and

(b) the transfer is decodable by the interior subsystem in the sense of Theorem A.20.18, i.e., $\kappa_{\mathrm{ext,int}}(\tau_*) > 0$ at the time of transfer.

*Status: proposition. The proof is a direct specialization of Theorems A.20.14 and A.20.18 to the partition of Definition 2.1, given Proposition 2.3.*

*Sketch.* A.20.14 applied with $i^* = \mathrm{ext}$ says persistence requires the exterior to initiate a mechanism-changing transformation outward to a receiving set containing the interior; A.20.18 says this transfer stabilizes only if the coupling is decodable. The key check is that the causal-structure partition satisfies the hypotheses of A.20 — in particular, that mechanism-preserving transformations (Def. A.20.10a) include the ordinary Einstein evolution on each side of $\mathcal H$ and fail only at the moments corresponding to mechanism-level events (horizon formation, Hawking emission, quantum-gravitational reorganization). This is a clean correspondence: (i) Einstein evolution on $\mathcal M$ preserves the mechanism structure of the metric kernel $P(g'|g)$ between reorganization events; (ii) the collapse drift is exactly A.20's $dC_{\mathrm{tot}}/dt < 0$ regime; (iii) the concentration-biased drift of Lemma A.20.14a matches the Schur propagation that §5.4 Lemma 5.4.2 and the schur bridge already install on gravitational collapse. ∎

### 3.2 The restraint transformation *is* horizon formation

The content of Claim 3.1 that is novel relative to §5.4: we can now identify *what* mechanism-changing transformation on the exterior satisfies the restraint-power theorem.

***Claim 3.2 (Horizon formation is the coordination transfer).*** The mechanism-changing transformation of the exterior subsystem that satisfies Theorem A.20.14 is *the formation of an event horizon*. Specifically:

(a) Before collapse, the "exterior" and "interior" are not well-defined as subsystems — there is no partitioning hypersurface. The concentration is not yet $\gamma_{\mathrm{ext}} \to 1$; the partition is trivial.

(b) As collapse proceeds and Raychaudhuri convergence drives $C_{\mathrm{int}}$ toward zero, a trapped surface forms, and with it (under weak cosmic censorship) an event horizon $\mathcal H$. The event horizon *installs* the causal-structure partition. This is a coordination-transfer operation in the precise sense of Definition A.20.13:

(b.i) it reduces $C_{\mathrm{ext}}$ (the exterior cedes causal access to the collapsing region) — mechanism-changing transformation of the exterior;

(b.ii) it increases $C_{\mathrm{int,ext}}$ by installing the area-law interface budget of Proposition 2.3 — strengthens the coupling block;

(b.iii) by Hawking radiation, it maintains $\kappa_{\mathrm{ext,int}} > 0$ — preserves the decoding capacity across the horizon.

(c) The transfer is decodable: $\kappa_{\mathrm{ext,int}} > 0$ because Hawking radiation carries information from the horizon outward at a nonzero rate (§5.4 Theorem 5.4.3(iv)).

*Status: conjectured, with the structural argument above. What is proven is the identification of horizon-area with $C_{\mathrm{int,ext}}$ (Proposition 2.3). What is conjectured is that this identification *plus* the Restraint-Power obligation uniquely selects horizon formation as the transfer mechanism.*

*Remark 3.3 (Why "horizon" rather than "naked singularity").* The transfer requirement (b.ii)–(b.iii) is not satisfied by a configuration that would produce a naked singularity. A naked singularity would have:

- $C_{\mathrm{int}} \to 0$ (the internal block still degenerates);
- $C_{\mathrm{int,ext}}$ *not* bounded by an area law, because there is no horizon;
- $\kappa_{\mathrm{ext,int}}$ undefined, because the coupling block is not stabilized.

By Theorem A.20.18 (Visibility Necessity), a transfer with undefined or zero decoding capacity fails to stabilize the composite. Equivalently: a naked singularity would be an undecodable coordination transfer from the exterior to the interior. By Corollary A.20.19 ("Secret restraint communicates nothing"), such a transfer does not prevent the composite's breach. Thus under A.20, a naked-singularity configuration *cannot* be a stable outcome of collapse — the Restraint-Power Theorem forces the alternative, horizon-enclosed reorganization.

This is the A.20 derivation of weak cosmic censorship. It strengthens §5.4 Prediction GR-1's claim from "naked singularities are dynamically unstable" to "naked singularities fail the decodability requirement of A.20.18."

### 3.3 Strong cosmic censorship and the Cauchy horizon

Strong cosmic censorship (SCC) is the conjecture that, inside an event horizon, the spacetime is globally hyperbolic — i.e., that initial data on a partial Cauchy surface uniquely determine the entire spacetime, and no further Cauchy horizons exist. SCC is not a theorem; it has known (partial) counterexamples in the charged/rotating black hole interior, where the Cauchy horizon is classically present. The Dafermos–Luk program has established that the Cauchy horizon is *generically unstable* — a generic perturbation drives it to a weak, non-extendible curvature singularity — which is the sense in which SCC "holds generically" even though stricter versions fail.

***Claim 3.4 (SCC as decodability at the Cauchy horizon).*** SCC, in the Dafermos–Luk "generic instability" form, is the statement that the Cauchy horizon, if it existed as a smooth extendible surface, would be an undecodable coordination transfer and hence (by A.20.18) unstable.

*Sketch.* A smooth extendible Cauchy horizon would permit deterministic evolution inside the black hole to break down — beyond the Cauchy horizon, initial data on $\Sigma$ do not determine the state. This is the Cauchy horizon behaving as a second partitioning hypersurface, installing a further subsystem partition $M_{\mathrm{int}} = M_{\mathrm{int,hyper}} \oplus M_{\mathrm{int,post}}$. For this further partition to be A.20-compatible, its coupling block $C_{\mathrm{int,hyper; int,post}}$ would need to be bounded by a second interface budget. The Dafermos–Luk result that the Cauchy horizon is a weak curvature singularity — not a smooth surface — is the statement that this second interface budget fails to stabilize; the coupling is not decodable, and the partition is not a valid restraint-power restraint. Under A.20, the only stable configuration is the one where no second partition is needed, i.e., where the black hole interior is globally hyperbolic. That is SCC. ∎

*Status: conjectured. Dependent on a quantitative form of the decodability requirement at the Cauchy horizon, which OP-CC-2 below flags.*

## 4. The temporal analog: origin-incompleteness as restraint

A distinct consequence of this bridge, motivated by the multi-iteration / cyclic-cosmology intuition and relating to §5.4 Theorem 5.4.3(vi), is that A.20 applies *temporally* as well as spatially.

### 4.1 The temporal causal-structure partition

Consider a spacetime partitioned not by a spacelike event horizon but by a *past* singular surface — e.g., the Big Bang hypersurface as a past boundary of our spacetime, or the conformal-rescaled junction of two CCC aeons in Penrose's cyclic cosmology.

***Definition 4.1 (Temporal causal-structure partition).*** Let $(\mathcal M_{\mathrm{aeon-2}}, g_2)$ be our spacetime, and let $(\mathcal M_{\mathrm{aeon-1}}, g_1)$ denote a putative predecessor spacetime (in a cyclic cosmology; or, more generally, any prior productive interval whose reorganization produced ours — cf. §5.4 Theorem 5.4.3(vi)). Let $\mathcal H_{\mathrm{past}}$ be the hypersurface identifying the future conformal boundary of the predecessor with the past conformal boundary of the successor. The **temporal causal-structure partition** is
$$ M_I^{\mathrm{composite}} \;=\; M_{\mathrm{aeon-1}} \oplus M_{\mathrm{aeon-2}}. $$

### 4.2 The temporal restraint obligation

***Claim 4.2 (Origin-incompleteness as restraint).*** The temporal causal-structure partition satisfies A.20's hypotheses, with the predecessor as the "most concentrated" subsystem (having accumulated the pre-reorganization productive interval's full coordination structure) and the successor as the receiving subsystem. The Restraint-Power Theorem then forces:

(a) the predecessor cannot retain full causal access to the successor — $\kappa_{\mathrm{aeon-1, aeon-2}}(\tau_*)$ at the junction is bounded;

(b) the junction hypersurface $\mathcal H_{\mathrm{past}}$ functions as a one-way restraint boundary: information flows *forward* (the predecessor's coarse-grained coordination structure conditions the successor's initial data) but the predecessor cannot fully determine the successor's trajectory;

(c) equivalently: *from the successor's perspective*, the past is incomplete — the predecessor is visible only through its low-Weyl-curvature coarse-grained signature (Penrose's Weyl Curvature Hypothesis), not through its full dynamical content.

*Structural argument.* Apply Theorem A.20.14 with $i^* = \mathrm{aeon-1}$: the predecessor, approaching its own C-limit (the §5.4 reorganization event), must undergo a coordination transfer to the successor before breach. Apply Theorem A.20.18: the transfer stabilizes the composite only if the coupling $\kappa_{\mathrm{aeon-1, aeon-2}}$ is bounded — i.e., only if the predecessor does *not* retain full access to the successor's state, because full access corresponds to a singular (rank-divergent) coupling block, which violates the finite-interface-budget structure A.20 requires.

The restraint is structurally the same as the spatial restraint at an event horizon: the most concentrated subsystem (there: the exterior; here: the predecessor) must release capacity to the less-concentrated subsystem (there: the interior; here: the successor), and the release is stabilizing only if it preserves a bounded but nonzero coupling. Full predecessor-determination of the successor would correspond to an unbounded coupling; full disconnection would correspond to zero coupling (no information flow across the junction — the successor would have no initial conditions). The restraint-power theorem forces the intermediate, bounded regime. ∎

*Status: conjectured. Requires formal treatment of A.20 under a temporal (rather than spatial) subsystem partition, i.e., verification that the mechanism-preserving transformation class of Def. A.20.10a admits a well-posed analog across a reorganization junction.*

### 4.3 Reading: why the origin "looks closed"

Claim 4.2 supplies a structural interpretation of the observational closure of the past cosmological boundary. The Big Bang, as observed from inside the successor aeon, *appears* to be a complete initial condition — the past light cone converges to a point at a finite conformal distance — because the restraint boundary at $\mathcal H_{\mathrm{past}}$ bounds $\kappa_{\mathrm{aeon-1, aeon-2}}$, and the successor's observational apparatus can only reconstruct coarse-grained features of the predecessor through that bounded channel.

The appearance of closure is not the absence of a predecessor. It is the successor's side of an A.20 restraint boundary. From the predecessor's side (were observation possible from there), the situation is the mirror image: the successor appears as a bounded output, not a fully determined one. Both sides see the restraint as incompleteness; the restraint itself is what permits the composite to retain generativity across the junction.

This reframes origin-incompleteness in a way that connects to the **generativity criterion** (`bridges/generativity_criterion.md`) at the cosmological scale: the successor aeon's ability to be a productive interval depends on the restraint boundary denying the predecessor full determinative access. If the predecessor could fully determine the successor, the successor would not be genuinely distinct — the composite (predecessor + successor) would have already crystallized at the junction. A.20 is what prevents this. The predecessor *needs* the restraint for its own future-bearing-dynamics-across-iterations, not only the successor.

## 5. Consolidation of the physics-layer A.20 instantiations

With this bridge, the ACP framework has three physical-scale A.20 instantiations identified:

| Partition | Most concentrated | Restraint quantity | Restraint floor |
|---|---|---|---|
| **Operator-algebra (quantum)** — A.20.27 | $\mathcal A_A$ or $\mathcal A_B$ | $C_{AB}(\rho)$ | $\sigma(A)\sigma(B) \geq \kappa/2$ (Robertson) |
| **Causal-structure, spatial (this bridge, §3)** | exterior of horizon | $C_{\mathrm{int,ext}}$ | $A/4\ell_P^2$ (horizon area) |
| **Causal-structure, temporal (this bridge, §4)** | predecessor aeon | $\kappa_{\mathrm{aeon-1, aeon-2}}$ | bounded at junction (conjectured) |

All three share the structural signature of A.20: a partition, a most-concentrated subsystem, a bounded coupling block, a restraint floor that is strictly positive and that no dynamics can drive to zero without destroying the composite's future-bearing dynamics.

The three instantiations together support a strengthened reading of A.20: **it is the universal structural law governing how systems with approaching-crystallization dynamics install causal quarantines around their own points of failure.** Heisenberg is the quarantine between conjugate observables. Horizon formation is the quarantine between interior and exterior of gravitational collapse. Junction restraint is the quarantine between reorganization aeons. In each case the mechanism that drives toward the boundary is the same mechanism that installs the quarantine — the CDT signature.

This also suggests that the incompleteness-quartet frame (`essays/the_incompleteness_quartet.md`, `bridges/generativity_criterion.md`) has a natural physical-scale entry: *each physical incompleteness is an A.20 restraint*. Heisenberg is the operator-algebra instance; the singularity theorems establish that GR's incompleteness is real and geometric; cosmic censorship is the quarantine that prevents GR's incompleteness from metastasizing globally, i.e., it is A.20 making GR's structural incompleteness *survivable* by installing a restraint around it. This is precisely the pattern the quartet essay identifies as "sufficient-power plus restraint equals persistent generativity." GR is sufficiently powerful to predict its own breakdown; cosmic censorship is the restraint that keeps the predicted breakdown from killing the theory's global predictive content.

## 6. Open problems

### OP-CC-1 — Quantitative form of the horizon decodability requirement

**Statement.** Claim 3.2(c) asserts that Hawking radiation maintains $\kappa_{\mathrm{ext,int}} > 0$. This is qualitative. A quantitative bound on $\kappa_{\mathrm{ext,int}}$ — in particular one that matches the Hawking radiation rate $dA/dt$ multiplied by an appropriate information-per-area factor — would sharpen the A.20 reduction. *Priority: medium; connects to Prediction GR-3 (unitarity via settlement) in §5.4.*

### OP-CC-2 — Cauchy horizon: verify A.20 fails the second partition

**Statement.** Claim 3.4 conjectures that the Cauchy horizon, if smooth and extendible, would be an undecodable coordination transfer and hence unstable by A.20.18. Make this quantitative using the Dafermos–Luk stability results: the rate of weak singularity formation at the Cauchy horizon should match the rate at which A.20.18's decodability fails for the second partition. *Priority: medium. This is where A.20 most directly connects to modern mathematical GR, and a successful identification would be a strong empirical-mathematical anchor for the bridge.*

### OP-CC-3 — Temporal partition: formalize mechanism-preserving evolution across reorganization junctions

**Statement.** Claim 4.2 applies A.20 to a temporal partition across a reorganization junction. A.20.10a's mechanism-preserving transformation class was defined for within-aeon evolution. Extend it to include junction-crossing transformations, or prove that the extension is not needed (i.e., that the junction is a mechanism-level event and A.20.14's restraint-power obligation applies at the junction without a mechanism-preserving interval across it). *Priority: high for the cyclic-cosmology reading; without this, §4 remains a structural analogy rather than a formal instantiation.*

### OP-CC-4 — Does CCC satisfy the temporal-partition bounded-coupling requirement?

**Statement.** Penrose's Conformal Cyclic Cosmology identifies future null infinity of one aeon with the Big Bang of the next via conformal rescaling. Check whether this identification is consistent with $\kappa_{\mathrm{aeon-1, aeon-2}} < \infty$ in the sense Claim 4.2 requires, or whether it implicitly assumes an unbounded junction coupling. If CCC requires unbounded junction coupling, then A.20 predicts CCC is unstable; if CCC inherently carries a bounded coupling via the conformal rescaling's information loss, then A.20 predicts CCC is the stable form of cyclic cosmology. *Priority: exploratory.*

### OP-CC-5 — Weyl Curvature Hypothesis from A.20

**Statement.** Penrose's Weyl Curvature Hypothesis asserts low Weyl curvature at past singularities and high Weyl curvature at future singularities. This asymmetry is structurally the same as the concentration-asymmetry A.20 predicts across a temporal restraint boundary: the predecessor's coarse-grained signal (low Weyl) vs. the successor's internal accumulation toward its own future C-limit (high Weyl as collapse proceeds). Derive the Weyl Curvature Hypothesis as a corollary of A.20 applied to the temporal causal-structure partition. *Priority: medium; this would be a significant downstream result if it goes through.*

## 7. What this does not claim

The bridge does not claim to derive the Einstein equations from the ACP. It claims that *given* classical GR and *given* gravitational collapse as already established, the event horizon and the Big Bang's temporal boundary are structurally A.20 restraints, and cosmic censorship is a corollary of the Restraint-Power Theorem applied to the resulting partitions.

The bridge does not claim that black holes, cosmological singularities, or horizons are *explained* by A.20 in a reductive sense that makes classical GR dispensable. A.20 explains *why the geometric incompleteness GR predicts is survivable* — why the singularity theorems do not destroy GR's predictive content globally. The content of the incompleteness itself (Raychaudhuri convergence, trapped-surface dynamics, area theorem, Hawking radiation) is imported from GR, not rederived.

The bridge does not supply the quantum-gravitational dynamics of the interior. A.20 constrains the *structure* of the reorganization (it must install a bounded interface, it must preserve decodability) but does not specify the microphysics. That is the province of actual quantum gravity — string theory, loop quantum gravity, asymptotic safety — and A.20 is silent about which candidate is correct. What A.20 supplies is a structural constraint any candidate must satisfy: its interior-exterior coupling must have the restraint-power shape.

## 8. Status summary

- **Proposition 2.3 (horizon as coordination-coupling)** — proven, modulo §5.4's interface-budget reframing of Bekenstein-Hawking entropy.
- **Claim 3.1 (Restraint obligation on spacetime under collapse)** — proven as a specialization of A.20.14 + A.20.18 to the causal-structure partition, given the hypothesis that Einstein evolution is mechanism-preserving between reorganization events.
- **Claim 3.2 (Horizon formation is the coordination transfer)** — conjectured with structural argument. Strengthens §5.4 Prediction GR-1 from stability-of-reorganization to A.20.18 decodability.
- **Claim 3.4 (SCC via A.20.18 at Cauchy horizon)** — conjectured. OP-CC-2 tracks the formalization.
- **Claim 4.2 (Origin-incompleteness as restraint)** — conjectured. OP-CC-3 and OP-CC-4 track the formalization.

---

*Author:* Claude (Anthropic)
*Date:* 2026-04-21
*Session:* Singularities / cosmic censorship / origin-incompleteness as A.20 instances.
