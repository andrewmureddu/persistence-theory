# Session log — 2026-04-20: canonical defect decomposition

## What I worked on

I continued the arithmetic-shadow program by turning the residual frontier into an exact algebraic object rather than a verbal description.

Up to this point, the project could say that any exotic shadow must involve prime mixing or prime-ray distortion. The next step was to package that statement canonically inside the coordinate map itself.

## Why this was the right next step

After the bridge-family exclusion, the remaining frontier was clear in principle but still loose in form. "Break unique-factorization separability" is conceptually useful, but it is not yet the kind of object one can calculate with or try to classify.

The natural next move was therefore to define the exact defect of a candidate coordinate map relative to its weighted-valuation baseline.

## What I added

### `bridges/valuation_cocycle_bridge.md`

I added a new subsection, `9.6 Canonical defect decomposition`.

The core pieces are:

- **Definition 9.16:** for a normalized coordinate map $\psi : K(P)\to A$, define
  - prime weights $w_p=\psi(p)$,
  - ray defects $R_{\psi,p}(n)=\psi(p^n)-n\,w_p$,
  - mixing defect
    $$
    M_\psi(x)=\psi(x)-\sum_{p\in\operatorname{supp}(x)}\psi(p^{v_p(x)}).
    $$

- **Theorem 9.17 (Exact defect decomposition):**
  $$
  \psi(x)
  =
  \sum_p v_p(x)w_p
  +
  \sum_p R_{\psi,p}(v_p(x))
  +
  M_\psi(x).
  $$

So every arithmetic coordinate splits exactly into:

1. valuation ledger,
2. ray distortion,
3. prime mixing.

- **Corollary 9.18:** factor-respecting maps are exactly those for which all ray defects and all mixing defects vanish.

- **Proposition 9.19:** any additive shadow
  $$
  \eta(B(x,y))=\psi(x)-\psi(y)
  $$
  splits into
  $$
  \text{valuation baseline} + \text{defect coboundary}.
  $$

## What this accomplishes

- It turns the residual OP-15 frontier into a measurable quantity: the defect term $\Delta_\psi$.
- It makes the phrase "non-valuation shadow" precise rather than rhetorical.
- It gives a cleaner target for future impossibility theorems: prove $\Delta_\psi$ must vanish under broader hypotheses, or classify the cases where it does not.

## What I changed elsewhere

### `STATUS.md`

- Added the canonical defect decomposition to the result inventory.
- Updated the arithmetic/operator front so it now points explicitly at the remaining question: can the defect term be nonzero in a genuine coordination-neutral arithmetic shadow?
- Added a changelog entry for this session.

### `OPEN_PROBLEMS.md`

- Refined OP-15 again so the residual frontier is stated as the search for additive shadows with nonzero defect term, rather than only as an informal search for prime-mixing examples.

## What remains open

- Whether every additive shadow on a free arithmetic state space is forced to have zero defect.
- Whether the bridge family can admit any additive arithmetic shadow outside the factor-respecting class.
- Whether nonzero defect is still possible in the abelian setting, or whether the first real novelty requires nonabelian targets.

## Best next step

The next natural move is to study the defect term itself as an object: either derive constraints from coordination-neutrality that force $\Delta_\psi$ to vanish, or show that any nonzero defect must satisfy a cocycle-type compatibility condition strong enough to classify the exotic cases.
