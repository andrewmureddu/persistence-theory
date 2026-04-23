# Proof Debt Audit v11

**Date:** 2026-04-21
**Scope:** The theorem chain supporting the Crystallization Drift Theorem (CDT) and the universal ACP claim.

## Executive summary

The review's strongest mathematical criticism lands on a real issue, but the issue is narrower than "the whole program is only analogy."

The current proof chain is strongest in three places:

- the Gaussian compounding calculation in `proofs/compounding_lemma_proof.md`
- the interventional reformulation of Claim A.3 in `proofs/claim_a3_interventional_proof.md`
- the channel-erosion route from stable coexistence to Coherent Steering in `proofs/coherent_steering_derivation.md`

The current proof debt is concentrated in four joints:

- upgrading local entropy reduction to monotone global drift without hiding a replenishment assumption
- upgrading "the fraction of self-reinforcing patterns rises" to "the total active load rises"
- extending the two-mechanism story to a fully closed generic k-mechanism theorem
- turning several strong structural arguments in the non-Gaussian and discrete cases into explicit estimates rather than proof sketches

This means the project does not need a weaker ambition. It needs a sharper theorem architecture.

## Main discrepancy to fix

The public-facing paper and `STATUS.md` currently speak as if the CDT proof chain is fully closed. The support documents are more mixed:

- `paper/acp_main_v10.md` and `STATUS.md` present the core proof chain as established.
- `proofs/crystallization_drift_theorem.md` still flags the compounding step and the Schur-complement connection as open or heuristic.
- `proofs/claim_a3_interventional_proof.md`, `proofs/induction_step_k_mechanisms.md`, and `bridges/non_gaussian_bounds.md` often mark the hard step as resolved in the section summary while still carrying a proof sketch or unclosed derivative/bound step inside the body.

This is not fatal, but it is exactly the kind of mismatch a skeptical reviewer will attack.

## Dependency ledger for Theorem 4.19

| Node | Role in CDT | Current status | Main debt |
|---|---|---|---|
| Lemma 4.13 | One active self-reinforcing mechanism lowers conditional macrostate entropy | Qualitatively solid; quantitative bound still open | The direction is argued correctly, but the explicit lower bound depends on basin geometry and is not fully stated |
| Lemma 4.14 | Selection pressure enriches the repertoire for self-reinforcing patterns | Partial | Proves fraction monotonicity, not total load monotonicity |
| Lemma 4.16 / Appendix A | Two interacting mechanisms compound superadditively | Gaussian case closed; generic case conditional | The interaction-information identity is exact, but sign control outside the Gaussian case still depends on Coherent Steering machinery and unresolved discrete/non-Gaussian details |
| Theorem A.8.9 | Interaction information is non-negative under Coherent Steering, generically strictly positive | Conditional | The Gaussian branch is strongest; the finite discrete perturbation step still says the derivative argument needs explicit computation |
| Theorem A.10.9 | Stable coexistence implies Coherent Steering | Strong structural result; not fully quantitative | Depends on the channel-reinforcement inequality and an erosion ODE whose constant is only qualitatively controlled |
| Theorem A.9.9 | k-mechanism extension and acceleration | Conditional | Closure of self-reinforcement under intersection and strict monotonic acceleration both still rely on nontrivial genericity and monotonicity steps |
| Lemma 4.17 | No endogenous reversal | Heuristic but plausible | Needs a cleaner operator, Lyapunov, or Markov-kernel formulation |
| Theorem 4.19(a) | Conditional entropy is monotone non-increasing | Conditional core | Needs a precise net-pressure or maintenance lemma to pass from local entropy reduction to global monotone drift |
| Theorem 4.19(b) | Reinforcement load is monotone non-decreasing | Open | Not implied by Lemma 4.14 as currently stated |
| Theorem 4.19(c) | Compound basin shrinks monotonically | Conditional | Immediate once (b) is actually proved |
| Theorem 4.19(d) | Default trajectory is toward crystallization | Conditional | Needs (a), Lemma 4.17, and a clean statement about exclusion or resolution of coherence crisis |

## What is actually closed now

These are the strongest pieces that can already carry real weight:

- The Gaussian compounding identity and Schur-complement picture are the cleanest hard proof currently in the chain.
- The observation/intervention split is a real upgrade. It gives a principled reason why the relevant sign question is not the naive observational interaction-information problem.
- The stable-coexistence to Coherent-Steering move is a good strategic result because it turns a static genericity claim into a dynamical-selection claim.
- The Heisenberg layer is not "proved from ACP alone," but the repo now does distinguish the closed structural statement from the stronger still-open operator-algebra derivation.

## Where the CDT proof currently overreaches

### 1. The jump from fraction monotonicity to load monotonicity

This is the single sharpest hidden inference in the current Theorem 4.19 proof.

Lemma 4.14 gives:

- the share of active patterns that are self-reinforcing rises

The proof of Theorem 4.19(b) uses:

- the total number of active self-reinforcing mechanisms rises

That is not the same claim. A system could lose mechanisms overall while becoming more dominated by the self-reinforcing ones that remain.

### 2. The core entropy-drift claim is packaged too late

The deepest content of the CDT is part (a): conditional macrostate entropy drifts downward under accumulated self-reinforcement.

Right now the theorem proves part (a) by routing through part (b). That makes the whole theorem depend on the weakest link. The architecture should be reversed:

- first prove a core entropy-drift theorem under a net reinforcement-pressure hypothesis
- then prove a separate dynamical accumulation theorem that justifies that hypothesis

### 3. The k-mechanism extension is more conditional than the summaries suggest

The induction file says the chain is complete, but its own body still relies on:

- a strong closure claim for intersections
- a generic smooth-map argument
- a strict acceleration step that is only exact in the Gaussian case

This is not a collapse. It is a packaging issue. The result should currently be presented as "closed in Gaussian, structurally argued generically, with strict acceleration still open in full generality."

### 4. The non-Gaussian quantitative story is not yet fully audit-clean

`bridges/non_gaussian_bounds.md` contains real progress, but still includes:

- a corrected false start in the entropy argument
- a conservative-linear-model claim that is explicitly marked as not fully proven

That means A.17 should currently be treated as a strong quantitative program with partial closures, not as a universally settled rate theorem.

## Recommended theorem split

To keep the universal claim and make it mathematically harder to dismiss, the CDT should be reorganized into three layers.

### Layer 1: Core universal theorem

Prove the entropy statement only:

- if a system's active self-reinforcing repertoire exerts non-decreasing net entropy-reducing pressure, then conditional macrostate entropy is monotone non-increasing

This is the theorem that should bear the universal claim.

### Layer 2: Dynamical accumulation theorem

Separately prove that in ACP systems:

- stable coexistence selects for coherence
- self-reinforcing patterns outcompete non-self-reinforcing ones
- the net entropy-reducing pressure is maintained or increases

This is where the missing replenishment or birth-death lemma belongs.

### Layer 3: Geometric and asymptotic corollaries

Then derive:

- reinforcement-load monotonicity, if actually established
- compound-basin shrinkage
- approach to crystallization absent coherence crisis or external reset

This keeps the strong claims, but stops the whole theorem from standing or falling on the weakest subclaim.

## Priority proof obligations

1. Write the missing maintenance lemma.
State exactly what dynamical assumption upgrades Lemma 4.14 to the claim needed for Theorem 4.19(b), then either prove it or restate the theorem in terms of net reinforcement pressure instead of raw load.

2. Recast Lemma 4.17 in kernel or Lyapunov form.
It should say something like: under the induced unperturbed transition kernel, there is no internal operator that increases the relevant entropy functional.

3. Mark the Gaussian/generic distinction everywhere.
When a claim is exact in Gaussian systems and structural elsewhere, say so explicitly rather than flattening them together.

4. Audit every "resolved" summary sentence against the body below it.
No section summary should say "resolved" if the body still contains a proof-sketch placeholder.

5. Pick one flagship reduction and overprove it.
The universal claim gets stronger when one reduction becomes undeniable. Kauffman or Price/Fisher are the best candidates.

## Bottom line

The universal claim is not the problem.

The problem is that the current theorem packaging lets a reviewer attack one or two still-open dynamical closure steps and then treat that as a refutation of the entire universal program.

The fix is to isolate the core theorem, name the exact remaining closure lemmas, and then close them one by one.
