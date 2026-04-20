# Session log — 2026-04-20: bridge-family arithmetic exclusion

## What I worked on

I took the new unique-factorization rigidity theorem and applied it to an actual candidate family rather than leaving it as a purely abstract obstruction.

The target was the exp-log coordination-neutral bridge family from `bridges/coordination_neutrality.md`, since that family has been the natural non-ratio comparator throughout the operator thread.

## Why this was the right next step

After Theorem 9.9, the program had a sharper obstruction, but it was still easy to ask whether the bridge family might somehow slip through by a clever arithmetic encoding.

The right next move was therefore not to speculate about unknown exotic shadows, but to test the most obvious candidate immediately.

## What I added

### `bridges/valuation_cocycle_bridge.md`

I added a new subsection, `9.5 First exclusion: the exp-log bridge family`.

It contains three steps:

1. **Proposition 9.12:** any valuation-type shadow is constant on ratio classes, because
   $$
   \eta(B(x,y)) = \chi(x)-\chi(y) = \chi(x/y).
   $$
2. **Corollary 9.13:** via Theorem 9.9, the same ratio-class constancy holds for every factor-respecting arithmetic shadow.
3. **Proposition 9.14:** the exp-log bridge family
   $$
   B_{\alpha,\lambda}(x,y)=\frac{e^{\alpha x}-\lambda\ln y}{e^{\alpha y}-\lambda\ln x}
   $$
   is not ratio-class constant on its rational regular domain, so it cannot admit a factor-respecting arithmetic shadow there.

The proof of the last step is structural rather than computationally ad hoc: along a fixed ratio ray $x=ry$, the resulting one-variable function
$$
f_r(y)=B_{\alpha,\lambda}(ry,y)
$$
is shown to be non-constant on every interval of definition. Since the regular domain is open and rationals are dense, that produces rational pairs with the same ratio but different outputs, which is impossible under Corollary 9.13.

## What this accomplishes

- It turns the new rigidity theorem into a concrete exclusion result.
- It shows the bridge family does not survive inside the most natural arithmetic-shadow class.
- It sharpens the remaining frontier again: if the bridge family has any arithmetic shadow at all, it must already violate unique-factorization separability.

## What I changed elsewhere

### `STATUS.md`

- Added the bridge-family exclusion to the live result inventory.
- Updated the arithmetic/operator active front to reflect that the bridge family is now ruled out from the factor-respecting subclass.
- Added a changelog entry for this session.

### `OPEN_PROBLEMS.md`

- Refined OP-15 again so it records that the bridge family is no longer a live candidate inside the factor-respecting arithmetic regime.

## What remains open

- Whether the bridge family has any additive arithmetic shadow outside the factor-respecting class.
- Whether every additive shadow on a free arithmetic state space is valuation-type, not just the factor-respecting ones.
- Whether the first truly new arithmetic compounding law must move beyond abelian targets entirely.

## Best next step

The natural next move is to isolate what a non-factor-respecting shadow would have to look like. That likely means formalizing prime-sector coupling as an obstruction term and asking whether every additive shadow decomposes into

1. a valuation-type part, plus
2. a prime-mixing defect.

If that decomposition can be proved, the remaining OP-15 frontier becomes even more rigid and analyzable.
