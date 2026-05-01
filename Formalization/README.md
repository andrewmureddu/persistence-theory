# Formalization

This workspace holds the formal theory program known as the **Adaptive Coherence Principle (ACP)** and its central theorem, the **Crystallization Drift Theorem (CDT)**. The working thesis: a system retains future-bearing dynamics iff it occupies a nondegenerate interval between two absorbing boundaries — dissolution (maximum entropy) and crystallization (zero conditional macrostate entropy). The mechanisms that prevent dissolution are the same mechanisms that can drive toward crystallization, so persistence requires **adaptive coherence steering**: structured mechanisms that preserve coherence while reopening future-bearing uncertainty.

## Where to start

- **`STATUS.md`** — current state of the paper, active fronts, what's next.
- **`paper/acp_main_v10.md`** — the working paper itself.
- **`CLAUDE.md`** — the operating charter (Claude as project lead, conventions, path layout).
- **`WORKFLOW.md`** — A.21-derived workflow guardrails: every theory-building session should open more disciplined questions than it closes.
- **`OPEN_PROBLEMS.md`** — canonical tracker of unsolved problems.

## Layout

```
paper/           the active paper (one file)
proofs/          core theorems + standalone proof documents
reductions/      six integrated reductions plus standalone bridge notes
bridges/         structural bridges, supporting appendices, A.20 Restraint-Power + Heisenberg
empirical/       Tier-2 observational tracks and dataset reanalysis scaffolds
special_cases/   extended 22-domain catalog
essays/          philosophical / foundational companion pieces
audits/          integrity audits
references/      external source material
sessions/        per-session logs
archive/         frozen prior versions
```

## How this workspace is run

The project sponsor provides high-level direction; Claude acts as primary researcher and author with full autonomy over technical decisions and next-step selection. Everything lives in markdown. Claude reads `STATUS.md` at session start and updates it at session end.
