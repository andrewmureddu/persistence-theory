# Session log — 2026-04-24: partition-generating functors

## Goal

Respond to the mathematician's first move: stop treating the ACP as a whole framework and test the smallest load-bearing typing problem. The selected target was WI-E.3, systems with no natural partition, because A.20 requires a subsystem / MASA-like partition while CDT can be stated at the unpartitioned level.

## What changed

### `bridges/partition_generating_functors.md`

- Added a candidate bridge for A.20 typing in no-partition systems.
- Defined an **A.20-untyped system**: a system where ACP/CDT objects are available but no domain-native subsystem partition has been selected.
- Defined a **partition-generating functor** $\Pi : \mathsf{C} \to \mathsf{Part}$ with four requirements:
  - typing;
  - equivariance under isomorphism;
  - A.20 admissibility;
  - nontriviality.
- Proved Theorem 4.1, the **symmetry obstruction**: if the automorphism group acts primitively on the candidate internal degrees of freedom, no nontrivial invariant partition exists.
- Derived Corollary 4.2: no universal nontrivial canonical partition selector can exist for all finite ACP systems.
- Defined selector data $S_X$ and stable selectors.
- Proved Proposition 5.3: a self-adjoint selector with a simple isolated eigenvalue canonically generates an equivariant eigenspace, and under a sign-separation condition generates a two-block spectral partition.
- Stated Conjecture 6.1: RG-generated A.20 typing may arise from the relevant/irrelevant decomposition of the RG linearization near a fixed point.
- Added three minimal test cases:
  - fully symmetric finite system;
  - two-community weighted graph;
  - scale-free Gaussian field.
- Linked the two finite cases to the new toy checker in `simulations/partition_selector_toy.py`.

### `simulations/partition_selector_toy.py`

- Added a dependency-free finite spectral-selector checker.
- Implements a Jacobi eigensolver for symmetric matrices.
- Builds two examples:
  - a fully symmetric graph, where the Fiedler selector is degenerate and no partition is selected;
  - a two-community weighted graph, where the Fiedler selector recovers the two blocks.
- Smoke run result:
  - fully symmetric: no selected partition;
  - two-community: `[0, 1, 2, 3] | [4, 5, 6, 7]`.

### `OPEN_PROBLEMS.md`

- Added OP-19, "Partition-generating functors for A.20."
- Recorded the state as open / partial: obstruction and first construction are written, but selector classification and invariance across selector families remain open.

### `WHAT_IF.md`

- Annotated WI-E.3 with the first bridge result.
- Reframed no-partition systems as a typing split: CDT may apply to $X$, while A.20 applies only to $(X,\Pi(X))$.

### `STATUS.md`

- Added partition-generating functors to the result inventory.
- Updated the A.21 / blind-spot active front to say the WI-E.3 consequence has been cashed out as a candidate bridge.
- Added OP-19 to the headline open-problem list.
- Added a changelog entry.

### `simulations/README.md`

- Documented the partition selector toy and its default smoke check.

### `research/blind_spot_atlas_2026-04-24.md`

- Updated the WI-E.3 row from "draft a bridge" to using the new bridge for selector classification and obstruction cases.

## Status split

**Now established:**

- A universal nontrivial canonical A.20 partition selector cannot exist in full generality.
- Generated partitions are possible only when the system supplies stable selector data.
- The no-partition problem is now a precise typing question rather than a loose analogy.
- The first finite toy check behaves as predicted: symmetry blocks selection, two-community structure generates a partition.

**Still open:**

- Formalize the concrete category $\mathsf{Sys}_{\mathrm{fin}}$ of finite ACP Markov systems.
- Decide which selector data are canonical enough for ACP: symmetrized transition kernels, mutual-information matrices, covariance/precision operators, RG maps, or correlation graphs.
- Test whether A.20 conclusions are invariant across distinct admissible selectors.
- Work out the RG-generated case in a minimal critical system.

## Recommended next move

Build the finite toy model:

1. Define $\mathsf{Sys}_{\mathrm{fin}}$ and its kernel-preserving isomorphisms.
2. Implement two test kernels: fully symmetric and two-community.
3. Compute the spectral selector and verify when the generated partition appears / disappears.
4. Use this as the first empirical-mathematical check of OP-19.
