**Adaptive Coherence Principle**

*A General Theory of Persistence from Thermodynamic First Principles*

with Unification of Dissipative Structures, Edge-of-Chaos Dynamics,

Free Energy Minimization, Quantum Darwinism, the Bergstrom–Lachmann Information Bound,

and the Price Equation / Fisher's Fundamental Theorem

as Special Cases of a Single Structural Law

•  •  •

**WORKING DRAFT — v0.9**

April 2026

# **Abstract**

We derive from thermodynamic first principles a structural law governing the persistence of dynamical systems. The **Adaptive Coherence Principle** (ACP) states that a system retains future-bearing dynamics—macroscopic evolution that is neither fully determined nor fully random—only inside a nondegenerate interval between two absorbing boundaries: *dissolution* (maximum entropy or maximum conditional macrostate randomness) and *crystallization* (zero conditional macrostate entropy). We isolate the core entropy-drift content of the **Crystallization Drift Theorem** (CDT): if the active entropy-contracting self-reinforcing repertoire of a system exerts non-decreasing net entropy-reducing pressure, where that pressure lower-bounds the one-step contraction of conditional macrostate entropy, then conditional macrostate entropy is monotonically non-increasing. The mechanisms that prevent dissolution are therefore the same mechanisms that, once maintained in an entropy-contracting form, drive the system toward crystallization, establishing a formal organizational dual to the second law. The compounding argument separates an exact identity from its sign condition: the superadditive excess in joint entropy reduction is the interaction-information term, and it is non-negative under Coherent Steering or dynamically stable coexistence. The required Coherent Steering condition is not an additional free assumption but a consequence of stable coexistence in the channel-erosion model: anti-coherent mechanisms undergo channel erosion and are shed. The stronger repertoire-geometry claims often associated with the CDT—monotone reinforcement-load growth, compound-basin shrinkage, and default convergence to the crystallization boundary—are identified as depending on one remaining maintenance lemma. We provide full formal reductions showing that six major results from independent literatures—Prigogine’s dissipative structures, Kauffman’s edge-of-chaos dynamics, Friston’s free energy principle, Zurek’s quantum Darwinism, the Bergstrom–Lachmann information bound, and the Price equation / Fisher’s fundamental theorem—are derivable as special cases. We further formulate a **Restraint-Power Theorem** (Appendix A.20): given a subsystem partition of any persistent system and a kernel-preserving coordination-conservation law on that partition, the subsystem with the highest coordination concentration must undergo a decodable mechanism-changing transformation before any other subsystem, and before the global floor is breached. This identifies the Heisenberg uncertainty principle as the quantum-scale instantiation of the coordination floor for a two-MASA operator-algebra partition. Finally, we record a meta-theoretic coherence result (Appendix A.21): for productive theory evolution, generativity is exactly the local adaptive coherence steering condition, with new inquiry acting as the theory-level entropy-restoring mechanism, and any correct self-representing ACP must remain structurally unfinished. We state ten testable predictions with formalized experimental protocols and falsification criteria, including three novel predictions that emerge uniquely from the unification. Open problems are identified.

*Keywords:* adaptive coherence, adaptive coherence steering, persistence, crystallization drift, entropy restoration, dissipative structures, edge of chaos, free energy principle, quantum Darwinism, information bound, second law, absorbing states, interaction information, do-calculus, channel erosion, coherent steering, operational time, Price equation, Fisher’s fundamental theorem, restraint-power law, coordination conservation, Schur complement, Heisenberg uncertainty, generativity

# **1. Introduction**

A recurring observation across physics, biology, and information theory is that systems capable of sustained complex behavior occupy a narrow operating regime—neither maximally disordered (which would destroy coherent structure) nor maximally ordered (which would eliminate the capacity for novel state transitions). This observation appears independently in thermodynamics (Prigogine 1977), complex systems theory (Kauffman 1993), computational neuroscience (Friston 2010), quantum foundations (Zurek 2003, 2025), information-theoretic biology (Bergstrom & Lachmann 2004), and evolutionary theory (Fisher 1930; Price 1972). Despite this convergence, no unified derivation exists. Each result is presented within its own formalism, and the structural identity between them is noted informally at best.

The present paper provides that unification. We proceed in eight steps: (i) establish a minimal formal vocabulary for persistence in dynamical systems (Section 2); (ii) derive the Adaptive Coherence Principle from axioms grounded in the second law and information theory (Sections 3–4.3); (iii) isolate the core entropy-drift theorem underlying the CDT and identify the remaining closure step for its stronger repertoire-geometry consequences (Section 4.4); (iv) show that each of the six convergent results follows as a special case under domain-appropriate restrictions (Section 5, Appendices A.11–A.15, A.19); (v) state ten testable predictions with formalized protocols and falsification criteria (Section 6, Appendix A.16); (vi) develop a partial quantitative program for the drift rate in general systems, combining one unconditional maximal-correlation route with sharper but still partly conditional non-Gaussian refinements (Appendix A.17); (vii) formulate a Restraint-Power Theorem unifying the coordination conservation and restraint-power redistribution formulations of the subsystem coordination floor, with the Heisenberg uncertainty principle as a quantum-scale special case once the subsystem transformation preserves the transition kernel (Appendix A.20); and (viii) apply the same interval structure to theory evolution itself, proving that a productive unifying theory must remain generative rather than closed (Appendix A.21).

The Crystallization Drift Theorem is the paper’s principal novel contribution. The ACP itself might be characterized as a careful unification of existing results; the drift theorem is genuinely new. Its strongest closed component is the core entropy-drift statement: maintained self-reinforcement drives conditional entropy downward. A key structural result is that the coherence input needed for superadditive compounding is self-grounding: the Coherent Steering condition is not an additional assumption but a necessary consequence of the theorem’s own premise that self-reinforcing mechanisms coexist stably. Anti-coherent mechanisms are dynamically unstable and are shed through channel erosion (Appendix A.10). The proof chain therefore identifies two selection pressures driving crystallization: selection for self-reinforcement (mechanisms that persist outcompete those that do not) and selection for coherence (mechanisms that enhance each other’s information channels outcompete those that jam them). What remains open is not the coherence step but the maintenance lemma needed to promote this core drift statement to the full load/basin/asymptotic package often associated with the CDT.

The unification claim is supported by full formal reductions for all six special cases (Appendices A.11–A.15, A.19), each consisting of a variable identification, a bridge lemma, and a reduction theorem. These reductions show that the productive interval is not merely analogous across domains but structurally identical: the same mathematical object, instantiated through different physical variables.

The broader claim of the project should therefore be read in layers. The productive-interval geometry is the strongest closed layer because it is established by six explicit reductions. The CDT's core entropy-drift statement is the paper's principal new theorem, while its stronger load / basin / asymptotic consequences are separated cleanly as remaining closure work. The wider package suggested by the current research synthesis — including restraint-power and vulnerable-margin as recurrent companions of ACP/CDT — is best treated as a mapped comparative program and empirical test target, not as a claim that every adjacent literature has already proved the full theorem under another name. Appendix A.21 adds the corresponding methodological constraint on this manuscript: the theory does not seek total closure. If the ACP is correct, its own research program should remain generative, opening well-posed successors rather than terminating inquiry.

# **2. Formal Vocabulary**

We begin by fixing definitions. These are stipulative—chosen for precision within this framework—not claims about the only possible usage of these terms. Unless otherwise specified, the core statements are written for a finite macrostate space M. Continuous or countably infinite versions require replacing the uniform distribution U_M and H_max by a reference measure and a finite resolution scale; the domain reductions state those reference choices explicitly.

## **2.1 Systems and States**

***Definition 2.1 (System). ***A system S is a tuple (Ω, σ, T, μ) where Ω is a state space (the set of all microstates), σ: Ω → M is a coarse-graining function mapping microstates to macrostates in some macrostate space M, T: Ω × ℝ≥0 → Δ(Ω) is a (possibly stochastic) time-evolution operator mapping a microstate and elapsed time to a probability distribution over microstates, and μ ∈ Δ(Ω) is the current distribution over microstates.

***Definition 2.2 (Macrostate entropy). ***For a macrostate m ∈ M, the macrostate entropy is S(m) = k_B ln |σ⁻¹(m)|, the Boltzmann entropy counting the number of microstates compatible with m. More generally, for a distribution μ concentrated on σ⁻¹(m), we use the Gibbs entropy S(μ) = −k_B Σ μ(i) ln μ(i).

***Definition 2.3 (Conditional macrostate entropy). ***The conditional macrostate entropy at time t, given the current macrostate m(t), is H(m(t+Δt) | m(t))—the Shannon entropy of the distribution over future macrostates conditional on the present macrostate. This measures how much macroscopic uncertainty remains about the system’s future given complete knowledge of its current macroscopic description.

*Remark 2.4. *The conditional macrostate entropy H(m(t+Δt) | m(t)) is distinct from the Boltzmann/Gibbs entropy S(m). The former measures unpredictability of macroscopic transitions; the latter measures microscopic degeneracy. A system can have high Boltzmann entropy (many microstates compatible with a macrostate) but low conditional macrostate entropy (the macrostate transitions are highly predictable). It is the conditional macrostate entropy that is relevant to future-bearing dynamics.

## **2.2 Future-Bearing Dynamics**

***Definition 2.5 (Future-bearing dynamics). ***Fix a crystallization margin η > 0 and a structural resolution margin δ_H > 0 before observing the system, chosen so that η < H_max − δ_H. A system S exhibits future-bearing dynamics at time t if and only if, for some finite Δt > 0, its conditional macrostate distribution P(m(t+Δt) | m(t)) satisfies: (a) H(m(t+Δt) | m(t)) > η (nontrivial unpredictability—the future is not fully determined by the present macrostate), and (b) H(m(t+Δt) | m(t)) ≤ H_max − δ_H, where H_max is the entropy of the uniform distribution over M (nontrivial structure—the future is not maximally random). Equivalently, condition (b) may be written as D_KL(P(m(t+Δt) | m(t)) || U_M) ≥ δ_H, up to the conventional entropy units.

*Remark 2.6. *Future-bearing dynamics is the formal counterpart of “alive enough to do something new while structured enough to remain recognizable.” Condition (a) prevents crystallization; condition (b) prevents dissolution by requiring a fixed, observer-independent gap from uniform randomness. Any system satisfying both is, in the precise sense of this framework, persisting.

## **2.3 Absorbing Boundaries**

***Definition 2.7 (Absorbing macrostate). ***A macrostate m* ∈ M is absorbing if P(m(t+Δt) = m* | m(t) = m*) = 1 for all Δt **>** 0. Once the system reaches m*, it never leaves under its own dynamics.

***Definition 2.8 (Dissolution boundary). ***The dissolution boundary D ⊂ M is the set of macrostates for which S(m) ≥ S_max − δ for some small δ > 0. These are states of near-maximum entropy in which the system has lost coherent macroscopic identity. Operationally, in domains where system identity is represented directly by the transition law rather than by Boltzmann degeneracy, the same boundary is represented by conditional macrostate distributions within δ_H of H_max. The reduction appendices specify which coordinate carries the dissolution condition in each domain.

*Remark 2.8a (Boundary compatibility). *The main theorem uses the following compatibility convention: membership in D implies either an absorbing equilibrium macrostate in the thermodynamic coordinate S, or a near-uniform conditional transition law in the operational coordinate H(m′|m). Without this bridge, high Boltzmann/Gibbs entropy and high conditional macrostate entropy are distinct quantities and should not be identified.

***Definition 2.9 (Crystallization boundary). ***The crystallization boundary C ⊂ M is the set of macrostates for which H(m(t+Δt) | m(t)) ≤ η for some small η > 0 and all finite Δt. These are states in which the macroscopic future is (nearly) fully determined by the macroscopic present.

*Remark 2.10. *Crystallization as defined here is not the same as low Boltzmann entropy. A crystal in the physical sense has low entropy and may still undergo phase transitions, defect migration, etc. Our “crystallization” is a dynamical condition: the macrostate evolution has become deterministic. A physical crystal that retains stochastic macrostate transitions is not “crystallized” in our sense. The terminology is metaphorical but precisely defined.

# **3. Axioms**

We require three axioms, each grounded in established physics.

## **3.1 The Entropy Production Axiom**

***Axiom 1 (Second Law). ***For any isolated system S, the total entropy S(μ(t)) is non-decreasing in t. For any system in thermal contact with an environment at temperature T_env, the free energy F = E − T_env S is non-increasing. Equilibrium is the global attractor of isolated dynamics.

*Grounding. *This is the second law of thermodynamics. We take it as axiomatic. It is the most empirically confirmed law in physics. No known exception exists. (Fluctuation theorems refine it for small systems but preserve the statistical asymmetry.)

## **3.2 The Coarse-Graining Axiom**

***Axiom 2 (Macroscopic Lossy Compression). ***The coarse-graining map σ: Ω → M is many-to-one. Multiple microstates map to the same macrostate. Consequently, macrostate dynamics are inherently lossy—macroscopic observation destroys microscopic information. For any macrostate m with |σ⁻¹(m)| > 1, knowledge of m underdetermines the microstate.

*Grounding. *This is the definition of coarse-graining in statistical mechanics (Jaynes 1957, Zurek 2003). It is not an approximation or a limitation of current measurement. It is the structural relationship between levels of description.

## **3.3 The Coupling Axiom**

***Axiom 3 (Environment-System Coupling). ***No physical system is perfectly isolated. Every system S interacts with an environment E such that the joint system S ∪ E is closed but neither S nor E alone is closed. The interaction strength may vary but cannot be reduced to exactly zero for any finite system embedded in a physical universe.

*Grounding. *This follows from the universality of gravity and quantum entanglement. A perfectly isolated subsystem is an idealization that no finite physical system achieves. Zurek’s decoherence program (2003, 2025) is built on this observation: the environment continuously monitors every system.

# **4. The Anti-Crystallization Theorem**

## **4.1 Thermodynamic Absorbing States**

We first establish that both boundaries are absorbing in the technical sense.

***Lemma 4.1 (Dissolution is absorbing). ***Under Axiom 1, thermal equilibrium is an absorbing macrostate for an isolated system. Once S(m) = S_max, the second law prohibits transitions to any macrostate m′ with S(m′) < S_max with probability 1 in the thermodynamic limit.

*Proof sketch. *By Axiom 1, S(m(t)) is non-decreasing for isolated systems. If m(t) achieves S_max, then S(m(t+Δt)) ≥ S_max for all Δt > 0. But S_max is the maximum, so S(m(t+Δt)) = S_max for all Δt. Therefore the system remains at maximum entropy. In the thermodynamic limit (N → ∞), fluctuations away from equilibrium become measure-zero events. ■

***Lemma 4.2 (Crystallization is absorbing as a zero-entropy class). ***Under Axioms 1–3, if a system reaches a macrostate m* such that H(m(t+Δt) | m*) = 0 for all Δt, then its unperturbed trajectory remains inside the zero-conditional-entropy class C₀. If m* is also a fixed point of the macrostate transition, then m* is absorbing in the strict sense of Definition 2.7. More generally, a system whose macroscopic future is fully determined by its macroscopic present cannot spontaneously recover nontrivial conditional entropy under its own transition kernel.

*Proof sketch. *If H(m(t+Δt) | m*) = 0, then the macrostate transition is deterministic: there exists a unique m′ = f(m*, Δt) for each Δt. If f(m*, Δt) = m* for all Δt (fixed point), m* is absorbing. If not, the system follows a deterministic orbit. In either case, the trajectory remains in C₀ and the conditional entropy remains zero along the orbit. No internal mechanism restores conditional entropy once it reaches zero. External perturbation (Axiom 3) may eventually disrupt the orbit, but the system itself cannot. ■

*Open problem (macroscopic determinism). *Lemma 4.2 requires a more careful treatment of the relationship between macroscopic determinism and microscopic stochasticity. A macroscopically deterministic system may still have microscopic fluctuations that eventually accumulate into macroscopic effects. The timescale separation between microscopic fluctuation and macroscopic determinism needs to be formalized. The claim holds in the limit of strong coarse-graining (high degeneracy) but needs qualification for weakly coarse-grained descriptions.

## **4.2 The Main Result**

***Theorem 4.3 (Adaptive Coherence Principle). ***Let S = (Ω, σ, T, μ) be a system satisfying Axioms 1–3 and the boundary-compatibility convention of Remark 2.8a. S exhibits future-bearing dynamics at time t only if its macroscopic state lies strictly between the dissolution boundary D and the crystallization boundary C. Formally: if m(t) ∈ D or m(t) ∈ C, then S does not exhibit future-bearing dynamics at t. In the conditional-entropy coordinate, future-bearing dynamics requires η < H(m(t+Δt) | m(t)) ≤ H_max − δ_H, where η and δ_H are the fixed margins from Definition 2.5.

*Proof.*

Case 1 (Dissolution): If m(t) ∈ D, then by Lemma 4.1, m(t) is absorbing (in the thermodynamic limit). Therefore H(m(t+Δt) | m(t)) = 0, violating condition (a) of Definition 2.5. Alternatively, if the system is at maximum entropy but still transitions stochastically among equilibrium-equivalent macrostates, condition (b) fails: the conditional distribution is uniform or near-uniform, so D_KL(P(m(t+Δt) | m(t)) || U_M) < δ_H.

Case 2 (Crystallization): If m(t) ∈ C, then by definition H(m(t+Δt) | m(t)) ≤ η, violating condition (a) of Definition 2.5 directly.

Therefore future-bearing dynamics requires m(t) ∉ D and m(t) ∉ C. By the definitions of D and C together with Definition 2.5, this means η < H(m(t+Δt) | m(t)) ≤ H_max − δ_H and S(m) < S_max − δ, jointly: the system maintains nontrivial conditional entropy (not crystallized) while remaining bounded away from maximum randomness (not dissolved). ■

*Remark 4.3a (Scope of the crystallization case). *Case 1 (dissolution) is unconditional in the thermodynamic limit. Case 2 (crystallization) inherits the qualification noted after Lemma 4.2: the absorbing character of C is rigorous for strongly coarse-grained systems (high degeneracy of the map σ) and requires the timescale separation assumption for weakly coarse-grained descriptions. The theorem therefore holds without qualification for the dissolution boundary and under the strong coarse-graining condition for the crystallization boundary.

## **4.3 The Persistence Corollary**

***Corollary 4.4 (Persistence requires active maintenance). ***Under Axiom 1, the dissolution boundary is the thermodynamic attractor for isolated systems. Therefore, any system exhibiting future-bearing dynamics must be actively maintained away from equilibrium by continuous thermodynamic work. Persistence is not a default state but a sustained achievement against the second law.

*Proof sketch. *By Axiom 1, an isolated system monotonically approaches equilibrium (D). By Theorem 4.3, future-bearing dynamics requires m(t) ∉ D. Therefore the system must not be isolated—it must exchange energy and entropy with its environment to resist the thermodynamic drift toward D. This is Prigogine’s dissipative structure condition (1977) derived as a corollary rather than an independent result. ■

***Corollary 4.5 (The crystallization trap). ***Total internal closure—a condition in which a system’s current macrostate uniquely determines all future macrostates—is a terminal event equivalent in finality to thermodynamic equilibrium. Both are absorbing conditions from which the system cannot spontaneously recover future-bearing dynamics: dissolution as an absorbing equilibrium state, crystallization as an absorbing zero-entropy state or orbit. The first kills by stasis; the second by dissipation. Both terminate future-bearing dynamics.

*Remark 4.6 (The asymmetry). *The second law provides a natural drift toward dissolution. The question of whether there is a corresponding drift toward crystallization—a formal dual to the second law for organizational systems—is answered affirmatively by the Crystallization Drift Theorem (Section 4.4). Crystallization occurs through entropy-contracting self-reinforcing mechanisms: excessive positive feedback, lock-in effects, overfitting, institutional rigidity. The drift theorem shows that these mechanisms are not accidental pathologies but necessary consequences of the very strategies that enable persistence when those strategies reduce the accessible future repertoire. While dissolution is the default thermodynamic fate, crystallization is the default organizational fate of systems that successfully resist dissolution by entropy-contracting reinforcement. Both must be actively avoided. This is the core structural insight of the ACP.

## **4.4 The Crystallization Drift Theorem**

The Adaptive Coherence Principle (Theorem 4.3) establishes that future-bearing dynamics requires a system to remain strictly between the dissolution boundary D and the crystallization boundary C. Corollary 4.4 shows that the second law provides a thermodynamic drift toward D. This section provides the organizational dual: a formal core showing that maintained entropy-contracting self-reinforcing mechanisms drive systems toward C when their net entropy-reducing pressure is sustained.

The central result is the Crystallization Drift Theorem: any system that maintains itself away from dissolution through entropy-contracting self-reinforcing mechanisms undergoes monotonic non-increase of conditional macrostate entropy, in the absence of external perturbation of sufficient magnitude, provided the active repertoire's entropy-reducing pressure does not weaken. The mechanisms that prevent dissolution are therefore the same mechanisms that drive the system toward crystallization once maintained in this entropy-contracting regime.

### **4.4.1 Self-Reinforcing Mechanisms**

***Definition 4.7 (Self-reinforcing mechanism). ***A self-reinforcing mechanism in a system S is a proper subset R ⊂ M of macrostates (the reinforcement basin) together with a transition bias: for all m ∈ R and all Δt in a characteristic time window [τ_min, τ_max], P(m(t+Δt) ∈ R | m(t) ∈ R) > P(m(t+Δt) ∈ R | m(t) ∉ R). That is: once the system occupies a macrostate within the reinforcement basin, the probability of remaining within the basin exceeds the probability of entering it from outside. A self-reinforcing mechanism is **entropy-contracting** at time t if its active conditional law also satisfies H(m(t+Δt) | m(t) ∈ R) < H(m(t+Δt) | m(t) unconstrained). Residence bias alone is a stabilizing tendency; entropy contraction is the additional bridge condition that makes the mechanism contribute to the CDT pressure functional.

*Remark 4.8. *This definition encompasses increasing returns to adoption (Arthur 1989), competency traps (Levitt & March 1988), institutional path dependence (Pierson 2000), precision-weighting of confirmed priors (Friston 2010), and the ordered-regime attractors in Boolean networks (Kauffman 1993). The common structure is: a pattern whose presence increases the probability of its own persistence.

***Definition 4.9 (Reinforcement strength). ***The reinforcement strength of a mechanism R at time t is α(R, t) = P(m(t+Δt) ∈ R | m(t) ∈ R) − P(m(t+Δt) ∈ R | m(t) ∉ R). By Definition 4.7, α(R, t) > 0 for all self-reinforcing mechanisms. When α = 1, the mechanism is maximally self-reinforcing and the basin is absorbing in the sense of Definition 2.7.

### **4.4.2 The Pattern Repertoire and Its Evolution**

***Definition 4.10 (Active pattern family and self-reinforcing repertoire). ***Let A(t) denote the family of organizational patterns currently active in system S at time t, whether or not they are self-reinforcing. The self-reinforcing repertoire, denoted Ρ(t), is the subset of A(t) consisting of the active patterns that satisfy Definition 4.7 at time t. The reinforcement load is |Ρ(t)|, the number of simultaneously active self-reinforcing mechanisms. When |A(t)| > 0, write

f_SR(t) = |Ρ(t)| / |A(t)|

for the self-reinforcing fraction.

***Definition 4.11 (Compound reinforcement basin). ***For a pattern repertoire Ρ(t) = {R₁, R₂, …, Rₖ}, the compound reinforcement basin is the intersection R̅ = R₁ ∩ R₂ ∩ ⋯ ∩ Rₖ ⊆ M. This is the set of macrostates simultaneously consistent with all active self-reinforcing mechanisms. As k increases, R̅ can only shrink or remain the same.

***Definition 4.11a (Net entropy-reducing pressure). ***Let H_t = H(m(t+Δt) | m(t)). Let Π(t) denote the coarse-grained total entropy-reducing pressure exerted by the active self-reinforcing repertoire, measured as a lower bound on the unperturbed one-step contraction of H_t. Write

Π(t) = Σ_{R ∈ Ρ(t)} π(R, t) + Ξ(t),

where π(R, t) ≥ 0 is the one-step entropy-reduction contribution attributed to an entropy-contracting mechanism R, and Ξ(t) ≥ 0 is the coherent superadditive excess contributed by the active interactions when the sign conditions from Appendices A.8-A.10 hold. The pressure functional is tied to the entropy process by the drift inequality

H_{t+Δt} − H_t ≤ −Π(t)Δt

for the unperturbed transition kernel at the chosen coarse-graining scale. The exact numerical decomposition of Π into π and Ξ is model-dependent; the CDT core requires only the drift inequality and non-weakening of Π(t). OP-16 asks for domain-native dynamical conditions guaranteeing that Π(t) is maintained or increases along unperturbed trajectories.

*Remark 4.12. *The compound reinforcement basin R̅ may be empty, in which case the system cannot simultaneously satisfy all active mechanisms. This is a coherence crisis—the system’s accumulated commitments are mutually incompatible. In practice, the system resolves this by abandoning one or more mechanisms, which is the organizational equivalent of a phase transition. See Section 4.4.5.

### **4.4.3 Preparatory Lemmas**

***Lemma 4.13 (Entropy-contracting self-reinforcement reduces conditional entropy). ***Let S be a system at macrostate m(t) ∈ R for some entropy-contracting self-reinforcing mechanism R with reinforcement strength α(R, t) > 0. Then H(m(t+Δt) | m(t) ∈ R) < H(m(t+Δt) | m(t) is unconstrained). That is: the presence of an active entropy-contracting self-reinforcing mechanism strictly reduces the conditional entropy of the system’s macroscopic future.

*Proof sketch. *By the entropy-contracting clause of Definition 4.7, the active transition law is more concentrated, in Shannon entropy, than the unconstrained law. In concrete reductions this condition is usually proved by a domain-native majorization or mode-count argument: probability mass is shifted toward a proper repertoire without introducing compensating within-basin dispersion. Under that majorization condition, Schur concavity of Shannon entropy gives the strict inequality. The magnitude of the reduction is bounded below by a domain-dependent function of the reinforcement strength α and the geometry of R. ■

***Lemma 4.14 (Survivorship selection for self-reinforcement). ***In a system maintained away from the dissolution boundary D, self-reinforcing patterns have a survivorship advantage over non-self-reinforcing patterns at the same coarse-graining scale. If the active pattern family evolves by a fixed-composition or birth-death process in which self-reinforcing patterns have uniformly lower exit hazards than non-self-reinforcing patterns, and no influx term reverses that ordering, then the expected self-reinforcing fraction f_SR(t) = |Ρ(t)| / |A(t)| is monotonically non-decreasing in t. Without those population-dynamical assumptions, the lemma supplies an enrichment pressure rather than literal monotonicity.

*Proof sketch. *Consider the population A(t) of organizational patterns active in S at time t. Non-self-reinforcing patterns (those with α ≤ 0) have no occupancy advantage and decay at a rate determined by the noise level. Self-reinforcing patterns resist decay: their occupancy advantage α > 0 means perturbations are counteracted by the bias toward re-entry. In a fixed-composition or suitably ordered birth-death model, the exit hazard for the self-reinforcing subpopulation is therefore lower than the exit hazard for the non-self-reinforcing subpopulation. Standard comparison for two-type survival processes then gives monotone increase of the expected self-reinforcing fraction. If new active patterns enter, or if hazards vary so that the ordering is not preserved, the conclusion weakens to a directional selection pressure toward Ρ(t). This is a selection argument formally analogous to natural selection (cf. Price equation), but the population-dynamical hypotheses must be stated explicitly. ■

***Lemma 4.14a (Maintenance balance, partial OP-16). ***Over one operational step, let L_t be the active entropy-contracting self-reinforcing mechanisms lost from Ρ(t), let B_t be the newly stabilized entropy-contracting self-reinforcing mechanisms, and let S_t = Ρ(t) \ L_t be the survivors. Then |Ρ(t+Δt)| − |Ρ(t)| = |B_t| − |L_t|. Hence the active reinforcement load is non-decreasing whenever |B_t| ≥ |L_t|, and is non-decreasing in conditional expectation whenever E[|B_t| − |L_t| | 𝔽_t] ≥ 0, where 𝔽_t is the history available at time t. Likewise, the net pressure Π(t) is non-decreasing whenever the incoming pressure from B_t, survivor strengthening inside S_t, and change in coherent excess Ξ(t) together dominate the pressure lost through L_t. The full bookkeeping identity and proof are recorded in `proofs/maintenance_lemma.md`.

*Status. *This is a sufficient maintenance lemma, not a universal derivation. It converts the hidden step in Theorem 4.17(b) into an explicit gain-loss condition. The companion proof note now derives that condition for deficit-responsive renewal systems, where loss-triggered replacement pressure plus survivor/coherent increment dominates expected shed pressure. OP-16 remains open in the generic form: classify renewal-dominant ACP systems and derive analogous balance conditions in broader target classes.

***Lemma 4.15 (Compounding identity and conditional superadditivity). ***Let R₁ and R₂ be two non-independent entropy-contracting self-reinforcing mechanisms active simultaneously in system S. The excess in their compound entropy reduction is exactly the interaction-information term:

ΔH(R₁ ∩ R₂) − ΔH(R₁) − ΔH(R₂) = I(Xₑ; X₁; X₃),

where Xₑ is the shared substrate, X₁ the constrained variables, and X₃ the free variables. Consequently, the compounding is strictly superadditive exactly when I(Xₑ; X₁; X₃) > 0, additive when this term is zero, and subadditive when it is negative. Under Coherent Steering, or under dynamically stable coexistence as formalized in Appendix A.10, the sign is non-negative and is strictly positive away from the redundant/degenerate cases.

The full proof is given in Appendix A, proceeding through three stages: (i) Gaussian systems, where the interaction information has an exact formula in terms of precision matrix entries and the Schur complement provides the algebraic mechanism; (ii) discrete systems, via the Partial Information Decomposition (Williams & Beer 2010); and (iii) general systems, via the chain rule of mutual information. The key identity—excess = interaction information—holds exactly in all three cases; the superadditive reading requires the sign condition stated above.

The sign of the interaction information is established in Appendix A.8 via an interventional argument using Pearl’s do-calculus. The result (Theorem A.8.9): for self-reinforcing mechanisms satisfying a Coherent Steering condition, the interaction information is non-negative, with strict positivity on a set of full measure. The Coherent Steering condition (Definition A.8.3)—that intervention on a mechanism’s constrained variables does not decrease the mutual information between shared substrate and free variables—is shown to be generic: its violation set is measure-zero in the space of mechanism parameters (Proposition A.8.7).

Moreover, Appendix A.10 establishes that Coherent Steering is not merely generic but *necessary* for dynamically stable coexistence of self-reinforcing mechanisms. The argument proceeds by contraposition: if Coherent Steering is violated (anti-coherence), the antagonistic mechanism’s constraint jams the other mechanism’s information channel, degrading its reinforcement strength through a self-amplifying feedback loop (channel erosion). The weaker mechanism’s reinforcement strength decays exponentially (Theorem A.10.7), and the mechanism is shed from the pattern repertoire. Stable coexistence therefore implies Coherent Steering (Theorem A.10.9), and the coherence input to the CDT is self-grounding: the theorem’s coexistence premise implies its own technical requirement without additional assumptions. This identifies a second selection pressure beyond survivorship selection (Lemma 4.14): not only are self-reinforcing mechanisms favored for persistence, but *coherent* self-reinforcing mechanisms are favored for compatibility. Under the maintenance hypotheses of Theorem 4.17, these pressures contribute to crystallization: survivorship selection enriches the repertoire for constraint-preserving mechanisms, and coherence selection ensures those constraints are mutually reinforcing.

The key insight connecting the algebraic and causal programs: the do-operator on X₁ corresponds to computing the Schur complement Q/X₁ of the joint precision matrix. Observation introduces confounding; intervention removes it. The Schur complement is causal denoising.

Appendix A.9 extends the two-mechanism result to k mechanisms in three layers. In Gaussian systems, Schur complement propagation gives an exact induction step. In aligned positive-association systems, positive return association plus a product-overlap threshold makes compound basins self-reinforcing, with monotone / MTP2 kernels as a checkable sufficient form. In the remaining generic case, the extension is obtained under an explicit intersection-compatibility hypothesis on compound basins together with a full-rank smooth-map argument for generic Coherent Steering. A new structural insight emerges: Schur complement propagation creates indirect couplings between mechanisms that have no direct coupling, providing the algebraic mechanism for superadditive acceleration (Theorem A.9.9 in its Gaussian-strongest / aligned-positive-association / generic-conditional form).

Part (c): the compounding accelerates. Each new mechanism Rₖ₊₁ compounds with the entire accumulated structure R̅ₖ rather than with individual mechanisms. In Gaussian systems, the induction step shows exactly that the pairwise interaction information I(Xₑ⁽ₖ⁾; X̅ₖ; Xₖ₊₁) is non-negative and that the effective couplings sharpen under Schur complementation. In the general case, the weak monotonicity claim is structural and the strict-generic acceleration claim remains conditional on the explicit k-mechanism closure assumptions recorded in Appendix A.9.

*Open problem (strict monotonicity). *The strict monotonicity of the interaction information in k (i.e., that the increment at step k+1 strictly exceeds the increment at step k) is proven for Gaussian systems and argued structurally for the general case, but ruling out the measure-zero constancy set for general systems remains open. Quantitative acceleration rates for general (non-Gaussian) systems are available only in the present partial sense of Appendix A.17: the maximal-correlation route supplies a rate template, while the sharper copula/cumulant refinements remain partly conditional. The explicit acceleration formula—bounding dκ̄/dk—remains open. See Section 7.

***Lemma 4.16 (No endogenous reversal). ***A system whose active pattern family A(t) coincides with its entropy-contracting self-reinforcing repertoire has no endogenous mechanism to increase its conditional macrostate entropy. That is: if every active pattern is self-reinforcing and entropy-contracting at the chosen coarse-graining scale, then H(m(t+Δt) | m(t)) ≤ H(m(t) | m(t−Δt)) under the system’s own dynamics alone.

*Proof sketch. *Increasing conditional entropy requires that the conditional distribution P(m(t+Δt) | m(t)) become less concentrated. For this to happen, one or more entropy-contracting self-reinforcing mechanisms must weaken (α or its entropy-contraction contribution must decrease) or the system must exit some reinforcement basin R. But by Definition 4.7, the system is biased toward remaining in each active basin. If all active patterns are entropy-contracting and self-reinforcing, every perturbation is resisted by the collective reinforcement. The only source of perturbation strong enough to overcome this resistance is external (Axiom 3). This is the formal sense in which the crystallization boundary is absorbing for self-organizing systems. ■

### **4.4.4 The Crystallization Drift Theorem**

***Theorem 4.17 (Crystallization Drift). ***Let S = (Ω, σ, T, μ) be a system satisfying Axioms 1–3 that maintains itself away from the dissolution boundary D through entropy-contracting self-reinforcing mechanisms. Then the CDT splits into a closed core and stronger conditional extensions:

(a) **Core entropy-drift claim.** If the net entropy-reducing pressure Π(t) of Definition 4.11a is non-decreasing along the unperturbed trajectory, then the conditional macrostate entropy H(m(t+Δt) | m(t)) is monotonically non-increasing in t.

(b) **Conditional repertoire-geometry extension.** If, in addition, the active reinforcement load |Ρ(t)| is monotonically non-decreasing, then the compound reinforcement basin R̅(t) is monotonically non-increasing (in the set-inclusion sense). Together with Lemma 4.16, this yields the familiar asymptotic formulation: absent sufficiently large external perturbation or a coherence crisis, the default organizational trajectory is toward the crystallization boundary C.

*Proof.* For part (a), Definition 4.11a packages the single-mechanism entropy-reduction contributions from Lemma 4.13 together with the non-negative coherent excess supplied by Lemma 4.15 and Appendices A.8-A.10. By the drift inequality in Definition 4.11a,

H_{t+Δt} − H_t ≤ −Π(t)Δt.

Since Π(t) ≥ 0, every unperturbed step is non-increasing in conditional entropy. If Π(t) is non-decreasing, the one-step contraction cannot weaken along the trajectory. Since conditional entropy is bounded below by zero, H_t is monotonically non-increasing and converges to a lower limit, with strict decrease on intervals where Π(t) > 0.

For part (b), Definition 4.11 gives R̅(t) = ∩{R : R ∈ Ρ(t)}. If the active reinforcement load is monotonically non-decreasing and each newly stabilized mechanism contributes an additional intersection constraint, then R̅(t) is monotonically non-increasing in the set-inclusion ordering. Lemma 4.16 then rules out endogenous reversal of the entropy contraction, so the unperturbed trajectory is toward C unless a sufficiently large external perturbation intervenes or the repertoire enters a coherence crisis and reorganizes. The remaining dynamical step is therefore clear: Lemma 4.14 gives a conditional enrichment result for f_SR(t), not a general monotonicity theorem for either f_SR(t) or |Ρ(t)|. Lemma 4.14a supplies a sufficient maintenance-balance condition, but the full four-part CDT package still depends on deriving that balance from lower-level ACP dynamics in the target class. ■

### **4.4.5 Corollaries**

***Corollary 4.18 (The Double Bind). ***The second law (Axiom 1) establishes D as the thermodynamic attractor. Theorem 4.17 identifies an opposing organizational drift toward C: maintained self-reinforcement contracts conditional entropy. Therefore, any system exhibiting future-bearing dynamics is subject to two simultaneous drifts in opposite directions. Persistence requires active management of both boundaries: continuous thermodynamic work to resist D, and continuous self-disruption to resist C.

*Remark 4.19. *The double bind explains why Holling’s adaptive cycle (1973) requires a release phase (Ω). The system cannot remain indefinitely in the conservation phase (K) because the accumulation of self-reinforcing mechanisms during K drives it toward C. Release—the deliberate or catastrophic dissolution of accumulated structure—is not a failure of the system but the mechanism by which it avoids crystallization.

***Corollary 4.20 (The organizational dual of the second law). ***Under the same maintained-pressure hypothesis as Theorem 4.17(a), there is a formal dual to the second law for organizational systems. The second law states: the Boltzmann entropy S(m) of an isolated system is monotonically non-decreasing. The organizational dual states: the conditional macrostate entropy H(m(t+Δt) | m(t)) of a self-maintaining system is monotonically non-increasing. The first is driven by the thermodynamic arrow (toward equilibrium). The second is driven by the selection arrow (toward lock-in). Together they define the two absorbing boundaries between which all future-bearing dynamics must navigate.

***Corollary 4.21 (The critical perturbation threshold). ***If the maintenance step in Theorem 4.17(b) is supplied so that self-reinforcing mechanisms accumulate without net loss, then the minimum external perturbation magnitude ε*(t) required to reverse the crystallization drift is monotonically non-decreasing in t. The more self-reinforcing mechanisms have accumulated, the larger the perturbation required to disrupt them. Systems deep in the crystallization drift therefore require increasingly violent disruptions to escape.

*Remark 4.22 (Connection to Schur complement structure). *In the algebraic framework developed in companion work, the productive interval corresponds to the regime where the Schur complement M/D of the internal block D is well-defined and non-degenerate. Crystallization drift corresponds to progressive degeneration of D: as self-reinforcing mechanisms accumulate, internal degrees of freedom are progressively eliminated, and D approaches singularity. When D becomes singular, the Schur complement is undefined—the system can no longer be decomposed into effective boundary behavior and eliminated internal structure. This is crystallization stated algebraically: the system has become its own boundary, with no interior.

*Open problem (Schur complement formalization). *The Schur complement connection (Remark 4.22) is stated heuristically. Formalizing it requires defining the internal block D in terms of the system’s macrostate transition matrix and showing that self-reinforcement corresponds to rank reduction of D. This is tractable for Gaussian systems but requires additional machinery for nonlinear systems.

### **4.4.6 Relationship to Existing Results**

The current literature positioning is narrower and therefore stronger than "the CDT was already known under another name." The nearest external matches split across three clusters. First, cascade and resilience work captures the productive-interval geometry and the fact that a stabilizing coupling can become destabilizing when over-accumulated. Second, lock-in, competency-trap, and robust-yet-fragile work captures the directional claim that successful adaptation narrows future options. Third, adaptive-cycle work captures the need for periodic release to avoid overclosure.

The recent cross-domain research notes sharpen the proof sketch by supplying domain-native examples of the maintained-pressure hypothesis rather than treating it as a free abstraction. Ashby's requisite-variety tradition and Bode-style robustness limits frame stabilization as variety attenuation with conserved fragility elsewhere; Hannan and Freeman's structural-inertia models show organizational survival selecting for reliability by reducing flexibility; March's exploration/exploitation simulations show learning reinforcing local competence until exploration becomes unattractive; Waddington-style canalization shows developmental stabilization narrowing accessible cell fates; and Kauffman's fitness-landscape / NK models show optimization trapping populations at local peaks. Across these notes, the common theorem skeleton is: a state space, a reachable-set or entropy/rank/variance metric, a stabilizing operator that lowers local uncertainty, and a reinforcement rule that increases the future weight of successful stabilizers. These examples do not prove the universal maintenance lemma, but they show that the missing hypothesis has repeatedly been isolated in independent mathematical or computational settings: stabilization is often implemented by mechanisms whose continued success deepens the same constraint that later limits adaptation.

The newest standalone control-theory reduction makes one member of this cluster explicit rather than merely suggestive. In that register, the entropy proxy is the information-conditioned viable continuation count \(N_h(m_t)\): the number of distinguishable closed-loop futures still reachable under bounded actuation, admissible disturbances, and a nondegenerate task neighborhood. Data-rate-limited stabilization supplies the dissolution floor, saturation-locked regulation supplies the crystallization boundary, Bode sensitivity gives the conserved-fragility geometry, and anti-windup is a local adaptive coherence steering device that preserves actuator and controller headroom. This note is not yet counted among the six fully integrated appendix reductions, but it sharpens the control-theoretic interpretation of the maintained-pressure problem: successful regulation suppresses dangerous variety, and repeated success can consume the very maneuver authority needed for future adaptation.

Kauffman and Friston have a different status here: in this project they are not left as analogies, but are handled by explicit reductions in Appendices A.15 and A.11. What remains distinctive about the CDT is the composition of these pieces into one theorem: maintained self-reinforcement, when coherent and non-weakening, drives monotone contraction of conditional macrostate entropy.

### **4.4.7 Additional Testable Predictions from the Drift Theorem**

**Prediction 5 (Crystallization drift rate scales with system success). **Systems that are more successful at resisting dissolution should, other things equal, crystallize faster whenever that success is mediated by increasing maintained reinforcement pressure. This predicts a negative correlation between historical resilience and current adaptability—the competency trap of Levitt & March (1988) promoted from observation to structural expectation once the maintenance step is specified.

**Prediction 6 (Early warning signals for crystallization). **The early warning signals for crystallization should include increasing autocorrelation of organizational patterns, decreasing variance in the system’s response to perturbation, and increasing recovery time from novel (as opposed to familiar) disruptions.

**Prediction 7 (Optimal institutional lifespan). **If the conditional accumulation step behind Corollary 4.21 holds so that ε*(t) is monotonically non-decreasing, then there exists a time T* at which ε*(T*) exceeds the maximum perturbation available from the system’s environment. Beyond T*, the system can no longer self-correct. This predicts a characteristic timescale beyond which organizational reformation becomes increasingly rare relative to organizational replacement.

# **5. Unification: Six Results as Special Cases**

We now show that six independently derived results from separate literatures are each special cases of Theorem 4.3 under domain-specific constraints. All six mappings are supported by full formal reductions in Appendices A.11–A.15 and A.19.

## **5.1 Prigogine’s Dissipative Structures (1977)**

**Result: **Systems far from thermodynamic equilibrium can spontaneously develop and maintain ordered structures by continuously dissipating energy and exporting entropy to their environment.

**Derivation from ACP: **Corollary 4.4 states that persistence requires active maintenance against the thermodynamic drift toward dissolution. A dissipative structure achieves exactly this: it maintains m(t) ∉ D by continuous energy throughput. Prigogine’s condition (“far from equilibrium”) is the ACP’s condition (m(t) ∉ D) stated for thermodynamic systems. The ACP additionally specifies the other boundary: the dissipative structure must also avoid crystallization (m(t) ∉ C).

**What the ACP adds: **The crystallization boundary is the ACP’s novel contribution—the recognition that a dissipative structure can fail not only by collapsing toward equilibrium but also by becoming locked into a single dynamical mode. Section 4.4 shows that this second failure mode is structurally driven by the same reinforcement mechanisms that keep the structure away from equilibrium, with the strongest default-trajectory reading supplied by the conditional repertoire-geometry extension of the CDT.

**Formal reduction: **Appendix A.14 provides the full formal reduction. The variable identification (Definition A.14.1) maps the system’s extensive thermodynamic variables to the ACP’s macrostate, with nonlinear kinetic evolution as the dynamics. The entropy production–macrostate entropy bridge (Lemma A.14.3) establishes that the conditional macrostate entropy H(m′ | m) is controlled by the number of accessible dissipative modes N(m)—not by the entropy production rate σ_P directly. Theorem A.14.4 proves: (i) thermodynamic equilibrium is the dissolution boundary; (ii) a frozen dissipative mode—thermodynamically active but macroscopically rigid—is the crystallization boundary; (iii) dissipative structures with multiple accessible modes occupy the productive interval. Proposition A.14.5 identifies crystallization drift as dissipative pathway rigidification under the maintained-pressure / load-growth caveats isolated in Section 4.4, and thereby motivates dissipative aging as the relevant conditional prediction. A novel insight: bifurcation is the thermodynamic system’s built-in adaptive coherence steering mechanism.

## **5.2 Kauffman’s Edge of Chaos (1993)**

**Result: **In random Boolean networks, networks in the ordered regime converge rapidly to fixed points. Networks in the chaotic regime exhibit exponentially divergent trajectories. Networks near the critical transition exhibit maximal computational capability (see also Bertschinger & Natschläger 2004 for recurrent neural networks).

**Derivation from ACP: **The ordered regime corresponds to C: highly predictable macroscopic dynamics, H(m(t+Δt) | m(t)) near zero. The chaotic regime corresponds to D: trajectories fill state space ergodically. Kauffman’s edge of chaos is the ACP’s productive interval (m ∉ D and m ∉ C), restricted to Boolean networks.

**What the ACP adds: **The ACP derives the same structural conclusion from thermodynamic first principles, showing why the edge-of-chaos regime exists. The Crystallization Drift Theorem additionally explains why networks under selection pressure drift toward the ordered regime: the frozen component’s expansion is precisely the compound reinforcement basin R̅ shrinking as self-reinforcing mechanisms accumulate.

**Formal reduction: **Appendix A.15 provides the full formal reduction. The variable identification (Definition A.15.1) maps the network’s dynamical profile (frozen/unfrozen partition plus attractor structure) to the ACP’s macrostate, with the joint action of Boolean dynamics and selection as the dynamics. The frozen component–macrostate entropy bridge (Lemma A.15.3) establishes that the frozen component fraction f(t) is the Kauffman-specific analog of the compound reinforcement basin occupancy, and that the Derrida parameter λ is a conditional entropy proxy. Theorem A.15.4 proves: (i) the chaotic regime is the dissolution boundary; (ii) the deep ordered regime is the crystallization boundary; (iii) the edge of chaos is the productive interval; (iv) frozen component expansion under selection is the Boolean-network signature of crystallization drift once the maintained-pressure / load-growth layer is invoked. Proposition A.15.5 identifies freezing cascades as superadditive compounding and treats acceleration as the strongest current conditional consequence rather than an unconditional closure. A novel insight: selection for function is selection for rigidity—any fitness criterion rewarding dynamical stability simultaneously selects for crystallization.

## **5.3 Friston’s Free Energy Principle (2010)**

**Result: **All living systems minimize variational free energy—an upper bound on the surprise of sensory observations given an internal generative model.

**Derivation from ACP: **Minimizing F pulls the system away from D (maintaining an accurate model prevents dissolution of coherent prediction) while the complexity penalty prevents overfitting to current data—which is precisely the crystallization boundary C (a model so tightly fit that it cannot accommodate novel observations).

**What the ACP adds: **The ACP provides a physical grounding for the FEP: the reason living systems minimize free energy is that the alternative leads to one of two absorbing states. The Crystallization Drift Theorem clarifies why the FEP includes both perception and action: perception manages the dissolution boundary, while action risks crystallization.

**Formal reduction: **Appendix A.11 provides the full formal reduction. The variable identification (Definition A.11.1) maps the agent’s internal and sensory states to the ACP’s macrostate. The model–macrostate entropy bridge (Lemma A.11.3) establishes that H(m′ | m) ≤ ⟨surprisal⟩ for deterministic recognition dynamics. Theorem A.11.5 proves: (i) perception manages the dissolution boundary; (ii) unchecked action (maximizing P(s|μ) without complexity penalty) drives crystallization drift; (iii) the complexity penalty D_KL(q || P(ψ)) is exactly the adaptive coherence steering constraint. Proposition A.11.6 identifies crystallization drift as precision accumulation and Friston’s epistemic value as the corresponding entropy-restoring perturbation mechanism.

## **5.4 Zurek’s Quantum Darwinism (2003, 2025)**

**Result: **When a quantum system interacts with its environment, decoherence selects preferred “pointer states” that are stable under environmental monitoring.

**Derivation from ACP: **Pointer states are the quantum-level instantiation of the productive interval. Superposition states that interact too strongly with the environment are dissolved. States completely decoupled from the environment are crystallized—they retain coherence but cannot be observed or interact. Pointer states maintain a nondegenerate interval: enough coupling to be real, enough stability to persist.

**What the ACP adds: **The ACP places quantum Darwinism inside the productive-interval architecture and turns pointer-state selection into one explicit reduction of the same geometry. The broader conjecture is not that every monitored system has already proved a Zurek-style theorem, but that environmental monitoring often creates an analogous stabilization-window / overclosure tradeoff in domain-native variables.

**Formal reduction: **Appendix A.12 provides the full formal reduction. The variable identification (Definition A.12.1) maps the reduced density matrix ρ_S to the ACP’s macrostate, with the partial trace as the coarse-graining map. The decoherence–entropy bridge (Lemma A.12.3) establishes that the Lindblad dissipator drives H(ρ_S′ | ρ_S) toward H_max (dissolution) while unitary evolution drives it toward zero (crystallization). Theorem A.12.4 proves pointer states occupy the productive interval. Proposition A.12.5 establishes Zurek’s redundancy Rδ as a quantitative indicator of position within the productive interval (Rδ = 0 ↔ C; Rδ → ∞ ↔ D; finite Rδ ≫ 1 ↔ productive interval). A novel insight emerges: classicality is a productive interval phenomenon.

## **5.5 Bergstrom–Lachmann Information Bound (2004)**

**Result: **The fitness value of environmental information to a biological agent is bounded above by the Shannon entropy H(E) of the environment.

**Derivation from ACP: **Zero environmental entropy corresponds to crystallization: no adaptive benefit to continued information processing. Maximum environmental entropy corresponds to dissolution: no learnable structure exists. The productive interval—where information has adaptive value—is bounded by H(E) > 0 and H(E) < H_max.

**What the ACP adds: **This reduction shows that the information-value bound is one explicit biological instantiation of a wider productive-interval constraint. That motivates parallel tests in engineered and social systems that use information to persist, but those out-of-domain extensions should be read as structural hypotheses unless and until they are reduced with the same explicit bridge.

**Formal reduction: **Appendix A.13 provides the full formal reduction. The variable identification (Definition A.13.1) maps the organism’s phenotypic strategy (the probability distribution over phenotypes) to the ACP’s macrostate, with natural selection as the dynamics. The strategy–entropy bridge (Lemma A.13.3) establishes that the optimal strategy entropy H(x) is bounded above by H(E)—the Bergstrom–Lachmann bound reinterpreted as a productive interval width constraint. Theorem A.13.4 proves: (i) H(E) = 0 corresponds to the crystallization boundary (full specialization); (ii) H(E) = H_max corresponds to dissolution (strategic incoherence); (iii) intermediate H(E) is the productive interval (diversified bet-hedging). Proposition A.13.5 identifies crystallization drift as specialization pressure: selection for the currently best phenotype is a self-reinforcing mechanism that progressively narrows phenotypic diversity, predicting that lineages with longer histories of environmental stability exhibit narrower phenotypic plasticity.

## **5.6 Price’s Equation and Fisher’s Fundamental Theorem (1930, 1972)**

**Result: **The Price equation (Price 1972) is the most general statement of selection dynamics: w̄ Δz̄ = Cov(w, z) + E(w Δz), partitioning the total change in a population trait into a selection component and a transmission component. Fisher’s fundamental theorem (Fisher 1930) states that the partial rate of increase in mean fitness due to natural selection equals the additive genetic variance in fitness: ∂_NS w̄/∂t = V_A(w) ≥ 0. Fisher drew an explicit analogy to the second law of thermodynamics.

**Derivation from ACP: **Under a fixed fitness landscape and the selection-entropy bridge of Appendix A.19, the selection term Cov(w, z) acts as a crystallization operator: it concentrates reproductive success on a subset of trait values and can reduce trait-distribution entropy. The transmission term E(w Δz) is the adaptive coherence steering operator: mutation, recombination, developmental noise, and environmental or developmental reindexing inject conditional entropy back into the trait distribution. Complete fixation (a delta-function trait distribution) is the crystallization boundary; strategic incoherence (a uniform trait distribution encoding no environmental information) is the dissolution boundary. Fisher’s guarantee that V_A(w) ≥ 0 is therefore a fitness-space ascent statement; it becomes a crystallization-drift statement only after the reduction identifies fitness ascent with entropy concentration in the chosen trait coordinate.

**What the ACP adds: **Fisher’s analogy between his theorem and the second law is made precise inside the restricted Price/Fisher reduction: thermodynamic relaxation and selection-mediated fitness ascent become dual monotonicity statements once the relevant entropy coordinate has been fixed. The two are the dual drives of the ACP—one toward dissolution, one toward crystallization—and persistence requires balanced resistance to both. The Crystallization Drift Theorem additionally predicts that populations under sustained directional selection require progressively larger mutational inputs to maintain standing variation (selection exhaustion), a quantitative prediction absent from population genetics.

**Formal reduction: **Appendix A.19 provides the full formal reduction. The variable identification (Definition A.19.1) maps the population’s trait distribution to the ACP’s macrostate, with one generation of reproduction as the dynamics. The selection–entropy bridge (Lemma A.19.3) states the conditions under which pure selection reduces trait entropy: H(z’) ≤ H(z). Theorem A.19.5 proves the Price equation is the ACP’s conditional entropy dynamics restricted to trait space; Theorem A.19.7 proves Fisher’s fundamental theorem is the CDT restricted to the fixed fitness-space coordinate. Corollary A.19.9 establishes the maintenance of genetic variation as the biological adaptive-coherence steering requirement. Proposition A.19.11 shows that the multi-level Price equation (Price 1972; Hamilton 1975) is the multi-scale ACP (Appendix A.18) restricted to nested biological populations, with within-group and between-group selection as crystallization at different scales.

# **6. Testable Predictions**

The ACP yields predictions that distinguish it from weaker claims. We state ten, of which Predictions 1–3 derive from the main theorem, Prediction 4 from the Restraint-Power Theorem (Appendix A.20), Predictions 5–7 from the Crystallization Drift Theorem, and Predictions 8–10 from the unification reductions (Appendices A.14–A.15). Each prediction is formalized with measurable quantities, null hypotheses, experimental protocols, and statistical tests in Appendix A.16. We state them here in summary form.

## **6.1 Symmetry of failure modes**

**Prediction 1: **In any empirical domain, the failure mode of excessive order should be as frequent and as catastrophic as the failure mode of excessive disorder, despite receiving less theoretical attention. In evolutionary biology, extinction by over-specialization (crystallization) should be comparable in frequency to extinction by environmental disruption (dissolution). In economic systems, firm death by rigidity should be comparable to firm death by disorganization.

## **6.2 Critical slowing near boundaries**

**Prediction 2: **Systems approaching either absorbing boundary should exhibit critical slowing down. This is well-established for the dissolution boundary (Scheffer et al. 2009). The ACP predicts the same early-warning signals near the crystallization boundary.

## **6.3 Optimal perturbation size**

**Prediction 3: **The optimal size of perturbation that a system can absorb while maintaining future-bearing dynamics should scale with its distance from the nearest boundary.

## **6.4 The restraint-power law**

**Prediction 4: **Among systems with the capacity to close their own productive interval, the successful systems—those that persist longest—will be those that exhibit maximal voluntary restraint relative to their capacity. This predicts a negative correlation between dominance concentration and system longevity across all domains. The formal anchor is the Restraint-Power Theorem (Appendix A.20.14): given a subsystem partition, the subsystem with the highest coordination concentration must undergo a decodable mechanism-changing transformation before any other subsystem, and before the composite’s global floor is breached. The Visibility Necessity Theorem (A.20.18) further establishes that secret restraint provides no stabilization—the transfer must be observable to the receiving subsystems to have functional effect. Adjacent literatures split cleanly across the theorem’s two clauses: strongest-goes-first results appear in self-binding, anti-saturation, and backoff settings, while visibility results appear in public-signal and common-knowledge settings. The theorem’s claim is that persistence near the coordination floor requires both clauses at once. Four novel quantitative predictions (RP-1 through RP-4, A.20.8.2) follow, including a concentration-lifespan hyperbola scaling and a cross-scale coordination-floor prediction connecting quantum (Heisenberg), gravitational (Bekenstein), and organizational floors.

## **6.5 Success-crystallization coupling**

**Prediction 5: **Systems that are more successful at resisting dissolution should crystallize faster when that success is mediated by maintained or increasing reinforcement pressure. This predicts a negative correlation between historical resilience and current adaptability in domains where reliability, local competence, or optimization success is implemented by narrowing the accessible repertoire.

## **6.6 Organizational early warning signals**

**Prediction 6: **Early warning signals for crystallization should include increasing autocorrelation of organizational patterns, decreasing variance in response to perturbation, and increasing recovery time from novel disruptions.

## **6.7 Institutional lifespan bound**

**Prediction 7: **There exists a time T* at which the critical perturbation threshold ε*(T*) exceeds the maximum perturbation available from the environment. This predicts a characteristic timescale beyond which organizational reformation becomes increasingly rare relative to organizational replacement.

*Formalization: Appendix A.16.8. Statistical test: competing risks survival analysis with Cox proportional hazards. Difficulty: Hard.*

## **6.8 Dissipative aging**

**Prediction 8: **A dissipative structure maintained under constant boundary conditions is expected to exhibit a monotonic decrease in the number of accessible dissipative modes N(m)(t) over time when the effective entropy-reducing pressure of its active pathways is maintained. The structure's pattern repertoire narrows even with no change in the driving force. This prediction follows from Proposition A.14.5 (crystallization drift as dissipative pathway rigidification) and is novel to the ACP—Prigogine's framework does not predict aging under constant boundary conditions.

*Formalization: Appendix A.16.9.1. Statistical test: Poisson regression of pattern count on time. Difficulty: Tractable (computational).*

## **6.9 Regulatory network aging**

**Prediction 9: **Under sustained selection for a fixed function, Boolean regulatory networks are expected to exhibit monotonic increase in frozen component fraction f(t) even after the target function is achieved whenever selection continues to stabilize the same self-reinforcing constraints. Selection for function is selection for rigidity: the drift continues as a consequence of self-reinforcing mechanism accumulation, not as optimization. This prediction follows from Proposition A.15.5 and is novel to the ACP—Kauffman's framework does not predict post-optimality drift.

*Formalization: Appendix A.16.9.2. Statistical test: linear regression of f(t) in the post-optimality phase. Difficulty: Tractable (computational).*

## **6.10 Drift rate universality**

**Prediction 10: **The normalized crystallization drift rate γ = |ΔH(m′ | m)| / (k · τ_char)—the rate of conditional entropy decrease per self-reinforcing mechanism per characteristic time—should be of the same order across the currently instrument-ready reduced domains, despite spanning >40 orders of magnitude in physical timescale. This is the most ambitious prediction because it asks whether the common ACP/CDT template recovered by the reductions constrains quantitative scaling and not only qualitative geometry. If confirmed, it would constitute the strongest evidence that the reduced cases instantiate one recurring law rather than merely a family of structural neighbors.

*Formalization: Appendix A.16.9.3. Statistical test: coefficient of variation of log(γ) across domains. Difficulty: Very hard (requires coordinated cross-domain measurement).*

## **6.11 Falsification criteria**

The ACP framework is falsifiable. **Strong falsification:** if crystallization failures are negligibly rare across domains (Prediction 1 fails with N_C/N_D < 0.05) *and* historical success does not predict crystallization (Prediction 5 fails), the core claim that maintained self-reinforcement drives conditional entropy downward would be refuted. **Moderate falsification:** if dual critical slowing down (Prediction 2) is absent near C—i.e., highly ordered systems recover equally fast from novel and familiar perturbations—the distinction between the two boundaries would be undermined. **Weak falsification:** if Predictions 8 and 9 fail in controlled simulation, the claim that Prigogine and Kauffman are special cases of the ACP would require revision. See Appendix A.16.12 for the full falsification protocol.

# **7. Open Problems and Limitations**

The following problems remain open. Several earlier problems have indeed advanced substantially: Coherent Steering is now derived from stable coexistence dynamics (Appendix A.10, Theorem A.10.9), all six reduction appendices are in place in structural form (Appendices A.11–A.15, A.19), and the multi-scale problem is resolved via the renormalization group embedding (Appendix A.18). The current proof debt is now sharper than in earlier drafts: the central remaining obligations are the maintenance lemma behind the full CDT package, the generic k-mechanism closure assumptions in Appendix A.9, the exact status of the non-Gaussian quantitative routes in Appendix A.17, and the kernel-preserving premise behind coordination conservation in Appendix A.20.

The single highest-priority gap is the **maintenance lemma** behind Theorem 4.17(b): Lemma 4.14 gives a survivorship-selection pressure, and monotone growth of the expected self-reinforcing fraction only under explicit fixed-composition or ordered birth-death assumptions. Lemma 4.14a and `proofs/maintenance_lemma.md` now give a precise sufficient balance condition: new stabilized pressure plus survivor strengthening plus coherent-excess change must compensate for pressure lost through shed mechanisms. The proof note also closes the first model class: in deficit-responsive renewal systems, explicit loss hazards, replacement probabilities, replacement pressures, and survivor/coherent increments imply the maintained-pressure condition whenever renewal dominance holds. The open problem is no longer the bookkeeping step; it is classifying which ACP systems are renewal-dominant and deriving analogous balance inequalities in broader target dynamics.

A second high-priority gap is the **generic k-mechanism closure problem** in Appendix A.9. The Gaussian induction is clean, and the first structured non-Gaussian branch is now explicit: aligned positive-association kernels close the compound-basin step when positive return association and a product-overlap threshold hold, with monotone / MTP2 systems giving a checkable sufficient form. The remaining generic induction still depends on an explicit intersection-compatibility hypothesis and a full-rank smooth-map argument. This is a localized problem, but it is mathematically real and should be named as such.

## **7.1 Non-Gaussian bounds: residual open questions**

Appendix A.17 now provides a **partial quantitative program** for general systems: an unconditional maximal-correlation / reinforcement-strength route (Theorem A.17.11, Proposition A.17.12), together with two sharper but still partly conditional refinements (the Gaussian-copula interventional bound, Theorem A.17.7, and the perturbative cumulant route, Theorem A.17.14 / Corollary A.17.15). The main qualitative insight is still that non-Gaussian structure should generically accelerate crystallization beyond the Gaussian baseline, but the sharpest statements remain conditional. Two central questions remain open: (a) the claim that linear structural equations provide the most conservative post-intervention bound (A.17, Step 5), argued structurally but not proven in full generality; and (b) the generic positivity of the non-Gaussian correction Δ_3 under Coherent Steering (Corollary A.17.15), similarly argued structurally. The present paper therefore relies only on the strongest currently defended quantitative route in each setting, not on the full conditional sharpening.

## **7.2 Strict monotonicity and quantitative acceleration**

Two related technical refinements from the k > 2 induction (Appendix A.9): (i) the strict monotonicity of interaction information in k—that the entropy reduction increment at step k+1 strictly exceeds the increment at step k—is proven for Gaussian systems and argued structurally for general systems, but the measure-zero constancy set has not been ruled out; and (ii) the strongest current quantitative acceleration template comes from the maximal-correlation route of A.17 (Corollary A.17.17), with sharper copula/cumulant readings remaining conditional. The explicit *acceleration formula*—bounding dκ̄/dk, the rate at which effective coupling strength grows as new mechanisms are incorporated—remains open. This is topology-dependent and may not admit a universal bound.

## **7.3 Erosion constant characterization**

The erosion rate constant c in the channel erosion theorem (Theorem A.10.7) depends on the coupling structure and basin geometry. The Gaussian case (Proposition A.10.14) gives an explicit form. For general systems, A.17's maximal-correlation route (Theorem A.17.11) provides a quantitative lower bound: c ≥ ρ²_m(coupling). The existence of c > 0 is established and a computable lower bound is available; the tight characterization of c in terms of basin geometry remains open but is no longer needed for the central results.

## **7.4 Rate of coherence crisis resolution**

The channel erosion theorem gives the time scale for shedding a single anti-coherent mechanism (τ = 1/(cδα₁₀)). The full coherence crisis dynamics—in which the system may shed multiple mechanisms and reorganize to a coherent subset—require a multi-mechanism version of the erosion ODEs (coupled differential inequalities). The k-mechanism extension (Theorem A.10.13) shows that stability implies coherence for each pair, but the transient dynamics of how a system with multiple anti-coherent mechanisms resolves remain to be characterized. This is a problem in dynamical selection theory and may connect to the phase transition structure discussed in Section 4.4.5.

## **7.5 The measure problem**

The ACP identifies the productive interval but does not specify a measure on it. How wide is the productive interval for a given system? Candidates for a metric on macrostate space include Fisher information metrics, Wasserstein distances, and order parameters from statistical mechanics.

## **7.6 The boundary dynamics problem**

The current formulation treats C and D as fixed boundaries. In reality, both may shift as the system evolves. A system that develops new internal degrees of freedom expands its state space, potentially moving the crystallization boundary. A dynamic treatment of the boundaries is needed.

## **7.7 Residual multi-scale open problems**

Appendix A.18 resolves the main single-scale-to-multiscale extension by embedding the ACP within the renormalization group framework. The key results are: (1) the *scale tower theorem* (Theorem A.18.7), which establishes that the productive interval at scale ℓ+1 is contained within the image of the productive interval at scale ℓ under the coarse-graining map, and that crystallization propagates upward through the hierarchy under a coherence condition; (2) *boundary covariance* (Theorem A.18.9), which shows that C→D and D→C transitions are forbidden under a single coarse-graining step; (3) the *critical productive interval* (Theorem A.18.12), which proves that at RG fixed points the productive interval is self-similar across scales—critical systems are the paradigmatic multi-scale persistors; (4) *upward crystallization propagation* (Theorem A.18.14), extending the CDT to hierarchical systems; and (5) *multi-scale adaptive coherence steering necessity* (Corollary A.18.16), which shows that single-scale perturbation is generically insufficient for hierarchical persistence. The residual open problems are the continuous scale limit (connecting to the Wetterich exact flow equation), downward propagation, emergent scales, and inter-scale interaction information.

## **7.8 The origins problem**

The ACP describes conditions for persistence, not origination. How does a system enter the productive interval in the first place? A complete theory would need to address the transition from non-future-bearing to future-bearing dynamics—the genesis problem.

## **7.9 Meta-theoretic generativity**

Appendix A.21 applies the ACP to theory evolution itself. It models a theory at research-time t by an inquiry-space coordinate I_t(T) and an uncertainty-space coordinate U_t(T), then shows that for productive research steps the generativity ratio G_t(T) > 1 is exactly the condition that explanatory progress move away from the crystallization boundary. The quartet inquiry floor (Gödel, Turing, Chaitin, and the Heisenberg/A.20 register) gives a positive lower bound on inquiry-space for self-representing theories. This supplies a self-consistency condition for the present program: if the ACP is correct and self-representing, it cannot be a terminal closed theory.

The result is intentionally limited. It does not prove the downstream semantic-field claim that dominant theories can crystallize the inquiry-space of researchers who think through them, nor does it give a quantitative lower bound for G_t(T). Those remain OP-10 through OP-12. What is closed is the local formal core: a unifying theory survives as a research program only by continuing to generate well-posed inquiry faster than it exhausts it.

## **7.10 Control-theory continuation variety**

The standalone control-theory reduction identifies viable continuation variety as the control-native proxy for conditional macrostate entropy, but several pieces remain outside the present manuscript's closed theorem layer. A fully quantitative version should relate \(H(m_{t+h}\mid m_t)\) to viable-tube volume, covering numbers, empirical controllability-Gramian spectra, or topological entropy for nonlinear and continuous-time plants. A sharper criterion is also needed to distinguish ordinary exact tracking from genuine crystallization: the task-neighborhood clause prevents the theory from misclassifying every successful setpoint regulator as overclosed, but the size and regularity of that neighborhood still have to be characterized.

The same note opens two further frontiers. First, decentralized control should be treated separately, because Witsenhausen-style action-as-signal problems may provide the cleanest control-theoretic version of the visibility clause in Appendix A.20. Second, the CDT-style claim for adaptive, gain-scheduled, or learned controllers remains conditional: repeated envelope-specific success plausibly contracts continuation variety, but promoting that statement to a theorem requires a control-native maintenance result rather than a structural analogy.

# **8. Discussion**

The Adaptive Coherence Principle, as derived here, makes a precise claim: the persistence of future-bearing dynamics in any system requires that system to maintain a nondegenerate interval between two absorbing boundaries, and both boundaries are genuine threats—the second law drives toward one; organizational dynamics drive toward the other.

The principal novel contribution is the Crystallization Drift Theorem program (Section 4.4). While the ACP itself might be characterized as a careful unification of existing results, the drift theorem is genuinely new. Its strongest closed component establishes that the organizational tendency toward rigidity is not merely an empirical regularity but a formal consequence of the same mechanisms that enable persistence once the maintained-pressure hypothesis is satisfied. The proof chain from axioms through the compounding identity (interaction information = compounding excess), the interventional proof of non-negativity under Coherent Steering, and the dynamical derivation of Coherent Steering from stable coexistence is now explicit in the appendices. The remaining debt is localized rather than diffuse: the maintenance lemma behind the full load/basin/asymptotic version of the CDT, and the generic closure assumptions in the k-mechanism induction.

The most surprising element of the proof is the exact identity between the compounding excess in joint self-reinforcement and the interaction information from information theory. The sign is supplied separately by Coherent Steering or stable coexistence; the identity itself was not assumed or constructed—it fell out of the algebra. The further insight that the Schur complement (the central algebraic object in the companion paper on categorical structure) is the causal denoising operator in the interventional framework connects two apparently separate mathematical programs.

The resolution of the Coherent Steering problem (Appendix A.10) closes the most important conceptual gap in the proof chain. The CDT no longer relies on Coherent Steering as a merely generic assumption; it derives that coherence input from stable coexistence via channel erosion, making this part of the theorem self-grounding. The subsequent non-Gaussian work (Appendix A.17) advances the most important *quantitative* gap but does not yet close it in full. Three complementary techniques—the Gaussian-copula interventional route, the maximal-correlation route via strong data processing inequalities, and the perturbative cumulant expansion—show that a quantitative program exists, but the sharpest copula/cumulant claims remain partly conditional. The strongest current generic quantitative template is therefore the maximal-correlation / reinforcement-strength route, while the sharper non-Gaussian acceleration story remains an active problem rather than a finished theorem.

The empirical predictions (Section 6, Appendix A.16) are structured in four tiers of tractability. Tier 1 predictions (8, 9, and 5 in the Kauffman domain) are testable immediately via computational simulation. Tier 2 predictions (1 and 6) require analysis of existing empirical databases. A first Tier-2 social-insect reanalysis track now targets existing ant and honey-bee datasets in which colony-level perturbation response, interaction-network entropy, spatial entropy, waggle-dance communication diversity, and recruitment concentration can be measured directly. This track is not a new formal reduction; it is an observational empirical program asking whether ACP-derived observables predict social homeostasis, communication-repertoire narrowing, and productive partitioning in independently collected collective-behavior data. Tier 3 predictions (2 and 3) require controlled laboratory experiments in nonlinear dynamics. Tier 4 predictions (4, 7, and 10) require extensive cross-domain data collection. This tiered structure is deliberate: it provides a research program that can generate initial evidence rapidly while building toward the most decisive tests. With the present partial quantitative program of Appendix A.17, predictions 8–10 can now be parameterized by explicit coupling- and reinforcement-based bounds, but the sharpest numerical thresholds remain route-dependent and, in the copula/cumulant formulations, partly conditional.

The formal reductions of all six special cases (Appendices A.11–A.15, A.19) strengthen the unification claim from loose structural analogy to mathematical theorem in six explicit cases. Each reduction follows the same pattern: a variable identification mapping domain-specific quantities onto the ACP framework, a bridge lemma connecting the domain’s characteristic entropy measure to H(m′ | m), and a reduction theorem establishing the domain result as a special case. That the same pattern works across thermodynamic systems (Prigogine), Boolean networks (Kauffman), Markov-blanketed agents (Friston), quantum subsystems (Zurek), evolving organisms (Bergstrom–Lachmann), and evolving populations (Price/Fisher)—six settings with radically different physics—is the paper's strongest evidence that the productive interval is a recurring cross-domain structure rather than a domain-specific convenience. The current literature scan sharpens how far that conclusion should be carried: for the productive interval itself the evidence is strongest, while for the larger ACP + CDT + restraint-power + vulnerable-margin package the more accurate claim is compositional. No single prior theorem found in the scan already combines workable-interval geometry, drift-to-rigidity, strongest-goes-first restraint, visibility, and margin-first failure into one argument. The distinctiveness of the project is therefore not that every piece is unprecedented in isolation, but that part of the package is now under explicit reduction, part under new theorem, and the rest organized as a disciplined test map rather than a free analogy. The completion of these reductions also reveals structural connections between the domains: the frozen component fraction f in Kauffman’s framework corresponds to the inverse of the accessible mode count 1/N(m) in Prigogine’s, and both measure the fraction of degrees of freedom captured by self-reinforcing mechanisms. The bridge variables are projections of the same underlying quantity—the ACP’s conditional macrostate entropy—onto different physical substrates.

A newer control-theory note extends this reduction pattern as a standalone bridge rather than as a numbered appendix. It identifies \(N_h(m_t)\), the viable continuation count, as the control-side analog of conditional macrostate entropy; data-rate theorems and saturation lock provide the two boundaries; Bode's sensitivity integral explains why the productive interval cannot be eliminated by stronger design; and anti-windup becomes the clearest engineered adaptive coherence steering mechanism. The note is therefore useful evidence that the productive-interval architecture is not confined to the six already integrated reductions, while also preserving the project's current honesty line: adaptive-controller crystallization drift remains an open CDT extension until the maintenance condition is derived in control-native terms.

The sixth reduction—the Price equation and Fisher’s fundamental theorem (Appendix A.19)—is structurally distinct from the other five in that it operates at the level of population dynamics rather than individual-system dynamics. Yet it yields the most direct validation of the ACP’s central metaphor. Fisher (1930) explicitly compared his fundamental theorem to the second law of thermodynamics; the ACP makes this comparison precise in the restricted fitness-space coordinate supplied by the reduction. The second law drives toward dissolution; the selection component of the Price/Fisher dynamics drives toward crystallization when fitness ascent is identified with entropy concentration in the chosen trait coordinate. These are the two absorbing boundaries of the ACP, and Fisher’s analogy becomes a structural identity after the reduction has fixed its bridge assumptions. The reduction also closes a loop opened in the proof of Lemma 4.14, where survivorship selection among self-reinforcing mechanisms was noted as formally analogous to natural selection. The Price equation reduction shows that the analogy is literal at the level of the shared selection operator, while leaving the population-genetic qualifications in place: transmission, balancing selection, and changing environments can reopen variation. The connection to the multi-scale extension (Appendix A.18) is immediate: the multi-level Price equation is a two-level scale tower, and the tension between within-group and between-group selection is the inter-scale crystallization tension of Theorem A.18.14.

The Restraint-Power Theorem (Appendix A.20) establishes a unification at a different level. Where the six reductions (Appendices A.11–A.15, A.19) show that major results from independent literatures are special cases of the ACP, the restraint-power theorem unifies two *formulations* of the coordination floor that had previously appeared to be distinct structural claims. The first formulation is conservation: under kernel-preserving mechanism-preserving transformations, the total coordination uncertainty H(m′|m) is exactly invariant (Theorem A.20.10). The second is the restraint-power redistribution dynamics: when the system approaches its crystallization boundary, the subsystem with the highest coordination concentration must undergo a decodable mechanism-changing transformation before any other subsystem and before the global floor is breached (Theorem A.20.14). These two statements turn out to be logically equivalent given the CDT (Theorem A.20.22); the CDT is the connecting premise that turns algebraic invariance into forced dynamical pattern. A visibility lemma (Theorem A.20.18) sharpens the result: the transfer stabilizes only if decodable by at least one receiving subsystem—secret restraint communicates nothing. A broader review of adjacent literatures suggests that strong neighbors of the theorem’s two halves already exist, but usually in separate domains: some results capture strongest-goes-first restraint, others capture visibility or common-knowledge requirements. What remains comparatively uncommon is their conjunction under a single coordination-floor argument. The most consequential special case of the restraint-power theorem is at the quantum scale (Theorem A.20.27): applied to a two-MASA partition of a quantum operator algebra, the coordination floor coincides with the Robertson uncertainty bound σ(A)σ(B) ≥ |⟨[A,B]⟩|/2, placing the Heisenberg uncertainty principle on the same structural footing as ecological restraint, market structure, and organizational delegation. The framework does not rederive the numerical value ℏ/2 from ACP axioms alone—that value is supplied by the commutator structure of the quantum partition and is imported from standard quantum mechanics (Cauchy-Schwarz). What the framework establishes is the *existence* and *location* of the floor: the two-MASA partition of a non-commutative operator algebra is the quantum instantiation of the subsystem partition of Definition A.20.1, and the coordination floor is strictly positive precisely because the algebras do not commute. The Bekenstein bound and weak cosmic censorship are stated as further physical-scale instantiations (Corollaries A.20.32, A.20.33), though formal derivations of both remain open problems (OP-RP-3, OP-RP-4).

Appendix A.21 gives the framework its internal methodological check. A theory that tries to explain persistence is itself a persistent representational system. The program therefore cannot be healthy if it aims at total closure. In the theory-evolution register, dissolution is the null theory that says nothing determinate, while crystallization is the closed theory whose own vocabulary leaves no live questions. For productive steps, the generativity criterion G_t(T) > 1 is exactly the condition that the research trajectory move away from crystallization. This is the formal reason the project may legitimately draw inspiration from unexpected domains without treating every analogy as a completed reduction: a living unification must keep generating disciplined questions at its boundary. The current manuscript reflects that constraint by separating theorem-level reductions, conditional extensions, bridge programs, and open problems rather than forcing them into one premature closure.

The symmetry between the two boundaries—that crystallization is as dangerous as dissolution—is the prediction most likely to have practical consequences. If confirmed empirically, it would provide a cross-domain early-warning framework for both failure modes using the same mathematical signature. The prediction that historical success at resisting dissolution accelerates crystallization (Prediction 5) is particularly testable and, if confirmed, would have immediate implications for institutional design.

## **8.1 Operational Time and the Verification Loop**

The ACP framework yields a natural account of time that deserves explicit statement, because it distinguishes the present framework from approaches that treat time as a background parameter.

***Definition 8.1 (Operational time). ***The operational time of a system S is the cumulative count of distinguishable macrostate transitions:

τ_op(t) = |{t_i ∈ [0, t] : m(t_i + Δt) ≠ m(t_i)}|

where distinguishability is defined by the coarse-graining map σ. Operational time advances by one unit each time the system's macrostate undergoes a transition resolvable at the macroscopic level.

*Remark 8.2 (Time loses operational content at both boundaries). *At the dissolution boundary D, the system has lost coherent macroscopic identity; macrostate transitions may still occur, but they are indistinguishable from noise relative to the system-level coarse-graining, so τ_op no longer functions as a clock for a persisting system. At the crystallization boundary C, H(m′|m) → 0 and the unperturbed macrostate evolution is fixed or periodic with no unresolved alternatives; τ_op may count deterministic cycle steps, but it no longer measures future-bearing dynamics. Thus future-bearing dynamics implies a nondegenerate operational-time regime, while the stronger equivalence requires the convention that only transitions resolving nonzero conditional entropy count as operational renewal.

This yields a tripartite temporal structure:

**Past (verified constraints).** Macrostate transitions that have already occurred and whose outcomes are shared across the system's internal degrees of freedom. These constitute the system's accumulated structural commitments—the compound reinforcement basin R̅(t) of Definition 4.11. In the language of Section 4.4, verified constraints are the self-reinforcing mechanisms that have survived selection. They are "crystallized" in the sense that their informational content has been compressed into the system's current boundary conditions. For physical systems, verified constraints reduce to geometry: the spatial and topological structure that encodes the outcomes of prior interactions at minimal thermodynamic cost.

**Future (unverified possibilities).** The set of macrostates accessible from the current state—the support of P(m(t+Δt) | m(t)). The cardinality of this set is the system's possibility space. The conditional macrostate entropy H(m′|m) measures the informational content of this space: how much remains to be determined. The system's current structure implicitly encodes a distribution over future states, and in this precise sense *every persistent system predicts ahead*—its transition kernel T is a conditional model of its own future.

**Present (the verification buffer).** The active process by which unverified possibilities are resolved into verified constraints. This is where H(m′|m) is expended: the system's conditional entropy decreases by one bit for each binary distinction that is resolved. The present is not an instant but a process with nonzero duration—the *verification latency* τ_v, defined as the characteristic timescale of the transition kernel T.

***Proposition 8.3 (Persistence as sustained verification, under renewal counting). ***Under the renewal-counting convention of Remark 8.2, the persistence condition of Theorem 4.3 is equivalent to the requirement that the verification loop

Predict → Verify → Crystallize → Re-predict from updated constraints → ⋯

continues indefinitely. The loop halts when the system reaches an absorbing boundary in the entropy-renewal sense.

*Proof sketch. *The loop advances operational time by one renewal unit per cycle. Each renewal cycle converts conditional entropy (unverified possibilities) into structural constraint (verified past). The loop halts when either (a) H(m′|m) → 0, i.e., there are no remaining alternatives to verify (crystallization), or (b) the structural constraints dissolve and there is no coherent system-level distribution whose transitions can count as verification (dissolution). These are exactly the two absorbing boundaries of Definition 2.8–2.9 once deterministic cycling is treated as repetition rather than renewal. ■

***Proposition 8.4 (Adaptive coherence steering as time renewal). ***The entropy-restoring mechanisms identified in Section 4.4.5—external perturbation exceeding ε*(t), coherence crises inducing phase transitions, and deliberate self-disruption—are mechanisms of adaptive coherence steering. They function as time-renewal operators: they inject new conditional entropy into the system, reopening the possibility space and enabling the verification loop to continue. Without entropy-restoring steering, Theorem 4.17 predicts monotone entropy contraction under the maintained-pressure hypothesis; a finite-time halt of operational time requires additional bounded-rate assumptions beyond the present paper.

*Remark 8.5 (Self-excitation and pattern expansion). *The verification loop has the structure of a self-excited circuit: the output of each verification cycle (newly crystallized constraint) modifies the boundary conditions for the next prediction, which modifies what must be verified next. The Crystallization Drift Theorem shows that this loop is not self-sustaining in a closed system—each cycle reduces H(m′|m), and the loop converges to a fixed point. Sustained operation requires that the loop *expand its pattern space*: each cycle must generate new unverified possibilities at a rate sufficient to offset the loss from verification. This is the informational analogue of the dissipative structure's requirement for continuous entropy export (Prigogine 1977): the system must create internal disorder faster than it crystallizes internal order.

***Remark 8.6 (Relationship to existing programs). ***The concept of operational time connects to several established research programs:

(a) *Connes–Rovelli thermal time hypothesis* (1994): Time flow emerges from the modular automorphism group of the system's thermal state. The ACP account differs in a fundamental respect: Connes–Rovelli extracts time from an equilibrium state, while operational time is generated by the *non-equilibrium* process of persistence. At equilibrium—the dissolution boundary—both frameworks agree that macroscopic time flow is trivial, but for different reasons: Connes–Rovelli because the modular flow becomes geometric; ACP because the verification loop has no coherent substrate.

(b) *Entropic time* (Martyushev 2025; various 2026): Entropy as an internal clock, with τ(ΔS) parametrizing change via entropy production. ACP's operational time is richer because it recognizes *two* stopping conditions: entropy maximization (ΔS → 0 at equilibrium) *and* conditional entropy minimization (H(m′|m) → 0 at crystallization). Entropic time has one boundary; operational time has two.

(c) *Page–Wootters relational time*: Time as entanglement between a "clock" subsystem and the rest of the universe. ACP's verification loop provides a specific physical mechanism for what the clock subsystem *does*: it verifies predictions by resolving conditional entropy into structural constraint.

(d) *Predictive processing / Active inference* (Friston 2010): The brain as a prediction engine that minimizes prediction error. ACP's verification loop is the abstract structure of which predictive processing is a neural special case: the predict-verify-update cycle is the universal temporal engine, not a property specific to brains.

***Remark 8.7 (Empirical consequences). ***The operational time framework sharpens the empirical content of several existing predictions:

(a) *Dissipative aging (Prediction 8)* becomes the claim that aging systems undergo monotonic deceleration of operational time: fewer distinguishable macrostate transitions per unit of clock time. The accessible mode count N(m) decreasing under drift is literally the system's clock slowing down.

(b) *Regulatory network aging (Prediction 9)* becomes the claim that the frozen component fraction f(t) increasing under selection is the fraction of the system's degrees of freedom for which verification has permanently halted—time has stopped for those variables.

(c) *Drift rate universality (Prediction 10)* becomes the claim that the deceleration profile of operational time—the function dτ_op/dt versus t—exhibits universal scaling behavior across systems, because it is governed by the same compounding dynamics (Lemma 4.15) regardless of physical substrate.

The multi-scale extension (Appendix A.18) embeds the ACP within the renormalization group framework. The most consequential result is the asymmetry between the two boundaries under coarse-graining: crystallization propagates upward through a hierarchy of scales (fine-grained rigidity induces coarse-grained rigidity), while dissolution does not (fine-grained randomness can produce coarse-grained order through self-averaging). This asymmetry is not imposed—it falls out of the many-to-one structure of the coarse-graining map. The implication for hierarchical systems is that crystallization is the more dangerous boundary at macroscopic scales: it accumulates from below, while dissolution is self-limiting. The connection to the information-theoretic RG program (Koch-Janusz & Ringel 2018; Lenggenhager et al. 2020) provides the bridge: the optimal RG transformation—the one that maximizes real-space mutual information—is precisely the coarse-graining that best preserves the productive interval structure across scales. The information bottleneck (Tishby et al. 1999) traces a one-dimensional cross-section of the productive interval, trading compression (crystallization) against predictive value (anti-dissolution). At RG fixed points, the productive interval becomes self-similar, and the ACP provides a thermodynamic account of why critical systems exhibit the richest dynamics: they are the systems that maintain the productive interval at every scale simultaneously.

Except for the limited self-application result in Appendix A.21, we have deliberately avoided philosophical and theological extensions in this paper. The ACP has implications for metaphysics, theology, and philosophy of mind. These extensions are pursued in companion work. The purpose here was to establish the physics—to show that the principle stands on thermodynamic ground before asking what else it might support.

# **References**

*Bibliography policy.* This reference list is intentionally shared across the main paper and the externally stored appendix documents cited throughout the manuscript; it is not a paper-only bibliography. Some entries are used only in appendix documents that are referenced here but not reproduced in full in this file.

Ahlswede, R. & Gács, P. (1976). Spreading of sets in product spaces and hypercontraction of the Markov operator. Annals of Probability 4(6), 925–939.

Amari, S. & Nagaoka, H. (2000). Methods of Information Geometry. Translations of Mathematical Monographs 191. American Mathematical Society.

Arthur, W.B. (1989). Competing Technologies, Increasing Returns, and Lock-In by Historical Events. Economic Journal 99, 116–131.

Ashby, W.R. (1956). An Introduction to Cybernetics. Chapman & Hall.

Bekenstein, J.D. (1973). Black holes and entropy. Physical Review D 7(8), 2333–2346.

Bergstrom, C.T. & Lachmann, M. (2004). Shannon information and biological fitness. In: IEEE Workshop on Information Theory.

Bertschinger, N. & Natschläger, T. (2004). Real-time computation at the edge of chaos in recurrent neural networks. Neural Computation 16(7), 1413–1436.

Bode, H.W. (1945). Network Analysis and Feedback Amplifier Design. Van Nostrand.

Breuer, H.P. & Petruccione, F. (2007). The Theory of Open Quantum Systems. Oxford University Press.

Calsaverini, R.S. & Vicente, R. (2009). An information-theoretic approach to statistical dependence: Copula information. Europhysics Letters 88(6), 68003.

Chaitin, G.J. (1975). A theory of program size formally identical to information theory. Journal of the ACM 22(3), 329–340.

Connes, A. & Rovelli, C. (1994). Von Neumann algebra automorphisms and time-thermodynamics relation in generally covariant quantum theories. Classical and Quantum Gravity 11, 2899–2917.

Cover, T.M. & Thomas, J.A. (2006). Elements of Information Theory, 2nd ed. Wiley.

Crow, J.F. (1958). Some possibilities for measuring selection intensities in man. Human Biology 30, 1–13.

DeLong, E.R., DeLong, D.M. & Clarke-Pearson, D.L. (1988). Comparing the areas under two or more correlated receiver operating characteristic curves. Biometrics 44(3), 837–845.

Donaldson-Matasci, M.C., Bergstrom, C.T. & Lachmann, M. (2010). The fitness value of information. Oikos 119, 219–230.

Ewens, W.J. (1989). An interpretation and proof of the fundamental theorem of natural selection. Theoretical Population Biology 36, 167–180.

Fisher, R.A. (1930). The Genetical Theory of Natural Selection. Clarendon Press, Oxford.

Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Reviews Neuroscience 11, 127–138.

Friston, K. (2019). A free energy principle for a particular physics. arXiv:1906.10184.

Friston, K., Rigoli, F., Ognibene, D., Mathys, C., Fitzgerald, T. & Pezzulo, G. (2015). Active inference and epistemic value. Cognitive Neuroscience 6(4), 187–214.

Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., Dolan, R.J. & Pezzulo, G. (2017). Active inference and learning. Neuroscience and Biobehavioral Reviews 68, 862–879.

Frank, S.A. (1997). The Price equation, Fisher’s fundamental theorem, kin selection, and causal analysis. Evolution 51, 1712–1729.

Gardner, A. (2020). Price’s equation made clear. Philosophical Transactions of the Royal Society B 375, 20190361.

Holling, C.S. (1973). Resilience and Stability of Ecological Systems. Annual Review of Ecology and Systematics 4, 1–23.

Holling, C.S. & Gunderson, L.H. (2002). Panarchy: Understanding Transformations in Human and Natural Systems. Island Press.

Derrida, B. & Pomeau, Y. (1986). Random networks of automata: a simple annealed approximation. Europhysics Letters 1(2), 45–49.

Glansdorff, P. & Prigogine, I. (1971). Thermodynamic Theory of Structure, Stability and Fluctuations. Wiley.

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. Monatshefte für Mathematik und Physik 38, 173–198.

Haldane, J.B.S. (1957). The cost of natural selection. Journal of Genetics 55, 511–524.

Hamilton, W.D. (1975). Innate social aptitudes of man: an approach from evolutionary genetics. In: Biosocial Anthropology (R. Fox, ed.), 133–155. Malaby Press.

Hannan, M.T. & Freeman, J. (1984). Structural inertia and organizational change. American Sociological Review 49(2), 149–164.

Heisenberg, W. (1927). Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik. Zeitschrift für Physik 43, 172–198.

Jaynes, E.T. (1957). Information theory and statistical mechanics. Physical Review 106(4), 620–630.

Kauffman, S.A. (1969). Metabolic stability and epigenesis in randomly constructed genetic nets. Journal of Theoretical Biology 22(3), 437–467.

Kauffman, S.A. (1993). The Origins of Order: Self-Organization and Selection in Evolution. Oxford University Press.

Kauffman, S.A. (2000). Investigations. Oxford University Press.

Kadanoff, L.P. (1966). Scaling laws for Ising models near T(c). Physics 2, 263–272.

Kelly, J.L. (1956). A new interpretation of information rate. Bell System Technical Journal 35, 917–926.

Kubo, R. (1966). The fluctuation-dissipation theorem. Reports on Progress in Physics 29(1), 255–284.

Koch-Janusz, M. & Ringel, Z. (2018). Mutual information, neural networks and the renormalization group. Nature Physics 14, 578–582.

Kline, A.G. & Hughes, D.L. (2022). Gaussian information bottleneck and the non-perturbative renormalization group. New Journal of Physics 24, 033007.

Langton, C.G. (1990). Computation at the edge of chaos: phase transitions and emergent computation. Physica D 42, 12–37.

Levitt, B. & March, J.G. (1988). Organizational Learning. Annual Review of Sociology 14, 319–340.

Martyushev, L.M. (2025). The Significance of the Entropic Measure of Time in Natural Sciences. Entropy 27(4), 425.

March, J.G. (1991). Exploration and exploitation in organizational learning. Organization Science 2(1), 71–87.

Muller, H.J. (1932). Some genetic aspects of sex. American Naturalist 66, 118–138.

Lewontin, R.C. (1978). Adaptation. Scientific American 239(3), 212–230.

Lenggenhager, P.M., Gökmen, D.E., Ringel, Z., Huber, S.D. & Koch-Janusz, M. (2020). Optimal renormalization group transformation from information theory. Physical Review X 10, 011037.

Lindblad, G. (1976). On the generators of quantum dynamical semigroups. Communications in Mathematical Physics 48(2), 119–130.

Maassen, H. & Uffink, J.B.M. (1988). Generalized entropic uncertainty relations. Physical Review Letters 60(12), 1103–1106.

Nicolis, G. & Prigogine, I. (1977). Self-Organization in Nonequilibrium Systems. Wiley.

Onsager, L. (1931). Reciprocal relations in irreversible processes. I. Physical Review 37(4), 405–426.

Ostrom, E. (1990). Governing the Commons. Cambridge University Press.

Page, D.N. & Wootters, W.K. (1983). Evolution without evolution: Dynamics described by stationary observables. Physical Review D 27(12), 2885–2892.

Pearl, J. (2009). Causality: Models, Reasoning, and Inference, 2nd ed. Cambridge University Press.

Penrose, R. (1969). Gravitational collapse: The role of general relativity. Rivista del Nuovo Cimento (Numero Speziale) 1, 252–276.

Penrose, R. (1996). On gravity’s role in quantum state reduction. General Relativity and Gravitation 28(5), 581–600.

Pierson, P. (2000). Increasing Returns, Path Dependence, and the Study of Politics. American Political Science Review 94(2), 251–267.

Polyanskiy, Y. & Wu, Y. (2017). Strong data processing inequalities for channels and Bayesian networks. In: Convexity and Concentration, IMA Volumes in Mathematics and Its Applications 161, 211–249. Springer.

Price, G.R. (1970). Selection and covariance. Nature 227, 520–521.

Price, G.R. (1972). Fisher’s ‘fundamental theorem’ made clear. Annals of Human Genetics 36, 129–140.

Pinsker, M.S. (1964). Information and Information Stability of Random Variables and Processes. Holden-Day.

Prigogine, I. (1945). Modération et transformations irréversibles des systèmes ouverts. Bulletin de la Classe des Sciences, Académie Royale de Belgique 31, 600–606.

Prigogine, I. (1967). Introduction to Thermodynamics of Irreversible Processes, 3rd ed. Wiley.

Prigogine, I. (1977). Time, Structure, and Fluctuations. Nobel Lecture, December 8, 1977.

Prigogine, I. & Wiame, J.M. (1946). Biologie et thermodynamique des phénomènes irréversibles. Experientia 2, 451–453.

Prigogine, I. & Stengers, I. (1984). Order Out of Chaos: Man’s New Dialogue with Nature. Bantam Books.

Robertson, H.P. (1929). The uncertainty principle. Physical Review 34(1), 163–164.

Rosas, F.E., Mediano, P.A.M., Gastpar, M. & Jensen, H.J. (2019). Quantifying high-order interdependencies via multivariate extensions of the mutual information. Physical Review A 100(3), 032310.

Sarmanov, O.V. (1958). Maximum correlation coefficient (nonsymmetric case). Doklady Akademii Nauk SSSR 121(1), 52–55.
Scheffer, M. et al. (2009). Early-warning signals for critical transitions. Nature 461, 53–59.

Schrödinger, E. (1930). Zum Heisenbergschen Unschärfeprinzip. Sitzungsberichte der Preussischen Akademie der Wissenschaften, Physikalisch-mathematische Klasse 14, 296–303.

Schrödinger, E. (1944). What is Life? Cambridge University Press.

Shannon, C.E. (1948). A Mathematical Theory of Communication. Bell System Technical Journal 27, 379–423.

Stein, D., Zanasi, F., Piedeleu, R. & Samuelson, J. (2025). Gaussian Processes as Quadratic Relations. Preprint.

Stone, M.H. (1930). Linear transformations in Hilbert space. III. Operational methods and group theory. Proceedings of the National Academy of Sciences 16(2), 172–175.

Tishby, N., Pereira, F.C. & Bialek, W. (1999). The information bottleneck method. In: Proc. 37th Allerton Conference on Communication, Control and Computation, 368–377.

Turing, A.M. (1936). On computable numbers, with an application to the Entscheidungsproblem. Proceedings of the London Mathematical Society, Series 2, 42, 230–265.

Tsybakov, A.B. (2009). Introduction to Nonparametric Estimation. Springer.

Waddington, C.H. (1953). Genetic assimilation of an acquired character. Evolution 7(2), 118–126.

Williams, P.L. & Beer, R.D. (2010). Nonnegative decomposition of multivariate information. arXiv:1004.2515.

Wetterich, C. (1993). Exact evolution equation for the effective potential. Physics Letters B 301, 90–94.

Wilson, K.G. (1975). The renormalization group: Critical phenomena and the Kondo problem. Reviews of Modern Physics 47, 773–840.

Wilson, K.G. & Kogut, J. (1974). The renormalization group and the ε expansion. Physics Reports 12, 75–200.

Zhang, F. (2005). The Schur Complement and Its Applications. Springer.

Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. Reviews of Modern Physics 75(3), 715–775.

Zurek, W.H. (2025). Decoherence and Quantum Darwinism. Cambridge University Press.

# **Appendix A: Notation Summary**

| ****Symbol**** | ****Meaning**** |
| --- | --- |
| Ω | State space (set of all microstates) |
| M | Macrostate space |
| σ: Ω → M | Coarse-graining function |
| T | Time-evolution operator |
| μ | Distribution over microstates |
| S(m) | Boltzmann/Gibbs entropy of macrostate m |
| H(m′│m) | Conditional macrostate entropy |
| D | Dissolution boundary (near-maximum entropy) |
| C | Crystallization boundary (near-zero conditional macrostate entropy) |
| α(R) | Reinforcement strength of mechanism R |
| Ρ(t) | Pattern repertoire at time t |
| R̅ | Compound reinforcement basin |
| I(Xₑ; X₁; X₃) | Interaction information (= compounding excess; superadditive when positive) |
| ε*(t) | Critical perturbation threshold (Corollary 4.21) |
| F | Variational free energy (Friston) / thermodynamic free energy (Prigogine) |
| ε, η | Small positive parameters defining boundary regions |
| δ | Erosion deficit (anti-coherence measure) |
| c | Erosion rate constant (coupling- and geometry-dependent) |
| τ | Channel erosion time constant: 1/(c·δ·α₁₀) |
| g(·,·) | Channel–reinforcement bound function (Prop A.10.6) |
| Φ | Proper subset of M capturing structured dynamics |
| Δt | Finite time increment |
| ρ_S | Reduced density matrix (Zurek, A.12) |
| Γ | Decoherence rate (Zurek, A.12) |
| Rδ | Redundancy measure (Zurek, A.12) |
| q(ψ) | Variational (recognition) density (Friston, A.11) |
| π | Precision (inverse variance) in generative model (Friston, A.11) |
| H(E) | Shannon entropy of the environment (Bergstrom–Lachmann, A.13) |
| x = (x₁,…,xₙ) | Phenotypic strategy (Bergstrom–Lachmann, A.13) |
| V(X) | Fitness value of information (Bergstrom–Lachmann, A.13) |
| W = (wᵢⱼ) | Fitness matrix (Bergstrom–Lachmann, A.13) |
| σ_P | Entropy production rate dᵢS/dt (Prigogine, A.14) |
| Jₑ | Entropy flux rate dₑS/dt (Prigogine, A.14) |
| N(m) | Accessible dissipative mode count (Prigogine, A.14) |
| f(t) | Frozen component fraction (Kauffman, A.15) |
| λ | Derrida parameter / perturbation sensitivity (Kauffman, A.15) |
| K | Node connectivity in Boolean networks (Kauffman, A.15) |
| p | Bias parameter of Boolean functions (Kauffman, A.15) |
| w, w̄ | Individual fitness, mean fitness (Price/Fisher, A.19) |
| z, z̄ | Trait value, mean trait value (Price/Fisher, A.19) |
| V_A(w) | Additive genetic variance in fitness (Fisher, A.19) |
| p(z) | Population-level trait distribution (Price/Fisher, A.19) |
| CEWI(t) | Crystallization early warning index (A.16) |
| ε_max(m) | Maximum absorbable perturbation at macrostate m (A.16) |
| R(S) | Voluntary restraint ratio: (dH/dt)_potential / (dH/dt)_actual (A.16) |
| γ | Normalized crystallization drift rate: \|ΔH\| / (k · τ_char) (A.16) |
| τ_novel | Recovery time from novel (non-repertoire) perturbations (A.16) |
| T* | Characteristic reformation timescale: age at which ε*(T*) = ε_env (A.16) |
| P_G | Gaussian reference distribution N(μ, Σ) with same mean and covariance as P (A.17) |
| ρ_m(X;Y) | Maximal correlation: sup_{f,g} Corr(f(X),g(Y)) (A.17) |
| κ, κ̄ | Coupling strength (cross-precision); mean coupling strength across mechanism pairs (A.17) |
| ᾱ | Mean reinforcement strength across mechanisms (A.17) |
| Δ₃ | Non-Gaussian correction to interaction information: I_P − I_G (A.17) |
| τ_op | Operational time: cumulative count of distinguishable macrostate transitions (8.1) |
| τ_v | Verification latency: characteristic timescale of the transition kernel T (8.1) |
| I_t(T) | Inquiry-space of theory T at research-time t (A.21) |
| U_t(T) | Uncertainty-space of theory T at research-time t (A.21) |
| G_t(T) | Generativity ratio: inquiry opened per uncertainty closed (A.21) |
| \mathcal P_T | Theory-evolution productive interval (A.21) |

# **Appendix B: Relationship Between ACP and Special Cases**

| ****ACP Term**** | ****Prigogine**** | ****Kauffman**** | ****Friston**** | ****Zurek**** | ****Bergstrom–Lachmann**** | ****Price / Fisher**** |
| --- | --- | --- | --- | --- | --- | --- |
| Dissolution (D) | Thermal equilibrium | Chaotic regime | High surprise | Full decoherence | Unlearnable environment (H(E)=H_max) | Strategic incoherence (uniform trait distribution) |
| Crystallization (C) | Static crystal | Ordered regime | Overfitting | Perfect isolation | Full specialization (xᵢ=1) | Complete fixation (δ-function trait distribution) |
| Productive interval | Far-from-equilibrium | Edge of chaos | Free energy minimum | Pointer states | Diversified bet-hedging | Maintained polymorphism |
| Future-bearing dynamics | Dissipative structure | Long transients | Active inference | Classicality | Adaptive phenotypic plasticity | Evolvability |
| Maintenance mechanism | Energy throughput | Selection pressure | Perception + action | Environmental monitoring | Bet-hedging (Kelly criterion) | Mutation + recombination + drift |
| Crystallization drift | Rigidification | Frozen component growth | Precision accumulation | Decoherence saturation | Specialization pressure | Selection (Cov(w,z) ≥ 0) |

# **Appendix C: The Proof Chain (Summary)**

The following summarizes the strongest current formal chain from axioms to the core entropy-drift theorem and its conditional extensions. Full proofs are in Appendices A–A.10.

**Step 1. **Self-reinforcing mechanisms reduce conditional entropy (Lemma 4.13).

**Step 2. **Self-reinforcing mechanisms are favored in pattern repertoires by survivorship selection; literal monotone enrichment requires the population-dynamical assumptions stated in Lemma 4.14.

**Step 3. **Two non-independent mechanisms have a compounding excess exactly equal to the interaction information: ΔH(R₁ ∩ R₂) − ΔH(R₁) − ΔH(R₂) = I(Xₑ; X₁; X₃). The compounding is superadditive when this term is positive, which is supplied under Coherent Steering or stable coexistence. Proven in Appendix A via Gaussian, discrete, and general arguments (Lemma 4.15).

**Step 4. **Self-reinforcing mechanisms are generically synergistic: I(Xₑ; X₁; X₃) ≥ 0 with strict inequality on a set of full measure. Proven via interventional do-calculus under the Coherent Steering condition, which is shown to be generic (Theorem A.8.9, Appendix A.8).

**Step 4.5. **Coherent Steering is a necessary consequence of dynamically stable coexistence. Anti-coherent mechanisms undergo channel erosion: the antagonistic mechanism’s constraint degrades the other’s information channel, causing decay of reinforcement strength (dα₂/dt ≤ −c·δ·α₁·α₂). Stable coexistence therefore implies Coherent Steering (Theorem A.10.9, Appendix A.10). This makes the coherence input to the drift theorem self-grounding and identifies a second selection pressure: selection for coherence among mechanisms.

**Step 5. **The k > 2 induction step: in Gaussian systems, the compound mechanism R̅_k inherits the needed structure exactly; in the generic case, the induction presently depends on an explicit intersection-compatibility hypothesis together with a smooth-map genericity argument for Coherent Steering. Schur complement propagation creates indirect couplings (Theorem A.9.9, Appendix A.9).

**Step 6. **No endogenous reversal: a system whose active pattern family is entirely self-reinforcing cannot increase its conditional entropy under its own dynamics (Lemma 4.16).

**Step 7. **Crystallization Drift Theorem (Theorem 4.17): combining Steps 1–6 yields the core entropy statement that maintained net entropy-reducing pressure drives monotone non-increase of H(m'|m). The stronger load / basin / asymptotic package requires one further maintenance lemma upgrading survivorship-selection enrichment to sustained reinforcement pressure or monotone load growth.

*Status: Core theorem isolated; full package still conditional. *The formal chain from axioms to the core entropy form of Theorem 4.17 is strongest in the Gaussian case and structurally argued more generally. The Coherent Steering condition is derived from stable coexistence (Appendix A.10), so the theorem’s coherence input is self-grounding. The remaining load-bearing open steps are the maintenance lemma behind the repertoire-geometry extension and the generic closure assumptions in Appendix A.9.

**Formal reductions (Appendices A.11–A.15, A.19): **The unification claim in Section 5 is supported by six formal reductions, each following the pattern: variable identification → bridge lemma → reduction theorem. Appendix A.11 reduces the Free Energy Principle (Friston 2010, 2019) to the ACP via the model–macrostate entropy bridge (Lemma A.11.3, Theorem A.11.5). Appendix A.12 reduces quantum Darwinism (Zurek 2003, 2025) to the ACP via the decoherence–entropy bridge (Lemma A.12.3, Theorem A.12.4). Appendix A.13 reduces the Bergstrom–Lachmann information bound (2004) to the ACP via the strategy–entropy bridge (Lemma A.13.3, Theorem A.13.4). Appendix A.14 reduces Prigogine’s dissipative structures (1945, 1977) to the ACP via the entropy production–mode count bridge (Lemma A.14.3, Theorem A.14.4). Appendix A.15 reduces Kauffman’s edge-of-chaos dynamics (1969, 1993) to the ACP via the frozen component–macrostate entropy bridge (Lemma A.15.3, Theorem A.15.4). Appendix A.19 reduces the Price equation (Price 1972) and Fisher’s fundamental theorem (Fisher 1930) to the ACP via the selection–entropy bridge (Lemma A.19.3, Theorems A.19.5 and A.19.7), establishing selection as a crystallization operator under the bridge assumptions and the maintenance of genetic variation as an adaptive-coherence steering requirement. All six special cases are now established by full formal reduction at the structural level; the stronger CDT-style monotonicity extensions inside several reductions inherit the maintenance caveat from Section 4.4.

**Standalone reduction notes: **The control-theory note in `reductions/control_theory.md` follows the same pattern at the working-note level: it identifies regulation profiles and viable continuation sets as the macrostate proxy, proves the support-size entropy bridge \(0 \le H(m_{t+h}\mid m_t) \le \log N_h(m_t)\), and locates dissolution in data-rate-limited loss of regulation and crystallization in saturation-locked single-continuation behavior. It is not yet part of the appendix numbering, and its adaptive-controller CDT extension remains open.

**Empirical formalization (Appendix A.16): **Appendix A.16 provides experimental protocols and statistical tests for ten predictions derived from the proof chain and the unification reductions. Three predictions (8–10) are novel to the ACP, emerging from the formal reductions in A.14–A.15 and not present in any of the six parent frameworks. The predictions are structured in four tiers of tractability, from immediately testable computational simulations (Tier 1) to the cross-domain drift rate universality test (Tier 4). Explicit falsification criteria are stated.

**Non-Gaussian bounds (Appendix A.17): **Appendix A.17 advances the quantitative non-Gaussian problem via three complementary techniques. The sharp Gaussian-copula interventional route (Theorem A.17.7) is partly conditional, because its linear-conservatism step is not yet fully proved. The maximal-correlation bound (Theorem A.17.11) provides the strongest current generic lower-bound template, and the perturbative cumulant expansion (Theorem A.17.14) supplies an explicit near-Gaussian correction program. Together, these motivate a quantitative drift-rate template (Corollary A.17.17): dH/dt ≤ −k · ½ · κ̄² · (1 − e^{−2ᾱ}) / (2 − e^{−2ᾱ}), depending only on the number of mechanisms k, mean coupling κ̄, and mean reinforcement ᾱ, while still leaving two genuine open questions: the conservatism of the linear structural equation bound and the generic positivity of the non-Gaussian correction Δ_3.

**Restraint-power and meta-theoretic closure checks (Appendices A.20-A.21): **Appendix A.20 states the restraint-power theorem for subsystem partitions under kernel-preserving coordination conservation, including strongest-goes-first, visibility, and the Heisenberg two-MASA specialization. Appendix A.21 applies the same interval structure to theory evolution: for productive research steps, G_t(T) > 1 iff explanatory progress moves the theory away from crystallization, while the quartet inquiry floor prevents self-representing theories from collapsing inquiry-space to zero. The ACP self-application corollary follows: if the ACP is correct and self-representing, it is structurally unfinished rather than a totalizing closed theory. The downstream semantic-field extension and a quantitative lower bound for G_t(T) remain open.
