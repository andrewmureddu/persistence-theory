# ACP Workflow Guardrails

*Status: operating protocol. Use with `STATUS.md`, `OPEN_PROBLEMS.md`, `bridges/generativity_criterion.md`, and `bridges/cross_domain_generativity_protocol.md`. This file does not add theory content; it turns A.21 into session bookkeeping.*

---

## 1. Purpose

ACP says a living theory should remain inside the productive interval: coherent enough to make progress, open enough not to crystallize. For project workflow, that means every theory-building session should ask:

- What did this session close or strengthen?
- What did it make newly askable?
- What new observable, falsifier, simulator, bridge variable, or scope boundary became visible?

The practical target is:

$$
G_{\mathrm{session}} =
\frac{
|Q_{\mathrm{new}}| + |O_{\mathrm{new}}| + |P_{\mathrm{new}}|
}{
\max(1, |C_{\mathrm{closed}}|)
}
> 1.
$$

Where:

- `C_closed`: claims, open problems, ambiguities, or methodological choices closed or materially strengthened.
- `Q_new`: new or sharpened well-posed questions.
- `O_new`: new observables, bridge variables, proxy measures, or scope distinctions.
- `P_new`: new falsification paths, simulation routes, empirical protocols, or review tests.

This is a workflow diagnostic, not a mathematical proof of correctness. A session can be useful maintenance without being theory-generative, but it should be labelled as such.

## 2. Session Closeout Gate

Before closing a research session:

1. Record the closure side.
   - Which claim, OP, ambiguity, naming issue, or implementation question was closed or strengthened?
   - Was it theorem-level, conditional, bridge-level, empirical, or only editorial?

2. Record the opening side.
   - Which successor questions were created or sharpened?
   - Are they tracked in `OPEN_PROBLEMS.md`, `WHAT_IF.md`, a bridge note, a simulation TODO, or the session log?

3. Record new measurement pressure.
   - Did the work expose a new observable, null model, simulator, falsifier, or stress test?
   - If not, is the output still too rhetorical?

4. Run the generativity check.
   - If `G_session > 1`, the session passes the A.21 workflow test.
   - If `G_session <= 1`, choose one: downgrade the closure claim, add or sharpen an open problem, move the material back to `WHAT_IF.md`, or mark the session as maintenance rather than theory progress.

5. Check boundary pressure.
   - Too many closures with too few successors means crystallization pressure; next step should diversify or stress-test.
   - Too many probes with no observables means dissolution pressure; next step should ground, quantify, or falsify.

## 3. Promotion And Demotion Rules

- A smooth analogy with no failure set is not yet generative. It may be decorative closure.
- A resolved OP should keep its resolution trail and, when appropriate, leave a narrower successor problem.
- A candidate bridge should not become a reduction until it names its failure set and at least one falsification path.
- A positive simulation result should not become evidentially load-bearing until it survives a discriminating null or a proxy-refinement pass.
- A rename, website pass, or packaging fix is maintenance unless it exposes a new claim boundary or research front.

## 4. Default Next-Step Selector

When no user direction overrides it, prefer the next move that best satisfies one of these:

- attacks live proof debt (`OP-16`, `OP-17`, `OP-18`);
- turns a bridge into a falsifiable protocol or simulator (`OP-20`, `OP-21`);
- makes a scope boundary measurable (`OP-19`, `OP-10`, `OP-11`);
- improves empirical discrimination for Predictions 8, 9, or 10;
- clarifies claim status without erasing the newly opened questions.

## 5. Session Log Template

Add this section to future session logs when the session changes theory content:

```markdown
## Generativity ledger

- Closed / strengthened (`C_closed`):
- New questions (`Q_new`):
- New observables or bridge variables (`O_new`):
- New tests, falsifiers, or simulations (`P_new`):
- Workflow check: `G_session = (...) / max(1, ...) = ...`
- Boundary assessment:
```

The ledger should be short. Its job is to keep the project honest, not to turn every session into an audit.
