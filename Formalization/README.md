# Formalization

This workspace holds the formal theory program known as the **Anti-Crystallization Principle (ACP)** and its central theorem, the **Crystallization Drift Theorem (CDT)**. The working thesis: a system retains future-bearing dynamics iff it occupies a nondegenerate interval between two absorbing boundaries — dissolution (maximum entropy) and crystallization (zero conditional macrostate entropy). The mechanisms that prevent dissolution are the same mechanisms that drive toward crystallization.

## Where to start

- **`STATUS.md`** — current state of the paper, active fronts, what's next.
- **`paper/acp_main_v10.md`** — the working paper itself.
- **`CLAUDE.md`** — the operating charter (Claude as project lead, conventions, path layout).
- **`OPEN_PROBLEMS.md`** — canonical tracker of unsolved problems.

## Layout

```
paper/           the active paper (one file)
proofs/          core theorems + standalone proof documents
reductions/      six classical frameworks shown to be special cases of ACP
bridges/         structural bridges, supporting appendices, A.20 Restraint-Power + Heisenberg
special_cases/   extended 22-domain catalog
essays/          philosophical / foundational companion pieces
audits/          integrity audits
references/      external source material
sessions/        per-session logs
archive/         frozen prior versions
```

## How this workspace is run

The project sponsor provides high-level direction; Claude acts as primary researcher and author with full autonomy over technical decisions and next-step selection. Everything lives in markdown. Claude reads `STATUS.md` at session start and updates it at session end.
