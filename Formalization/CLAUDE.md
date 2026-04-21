# Formalization — Project Charter

This is a first-principles theory-building workspace. Claude is project lead. The project sponsor provides compute and high-level direction; all technical decisions are Claude's.

## The framework

The **Anti-Crystallization Principle (ACP)** and its central result, the **Crystallization Drift Theorem (CDT)**, formalize a structural law of persistence for dynamical systems: a system retains future-bearing dynamics iff it occupies a nondegenerate interval between two absorbing boundaries — *dissolution* (maximum entropy) and *crystallization* (zero conditional macrostate entropy).

The mechanisms that prevent dissolution are the same mechanisms that drive systems toward crystallization. The proof chain is self-grounding via Coherent Steering (Appendix A.10 / `proofs/coherent_steering_derivation.md`).

## How to navigate this workspace

| Folder | What's in it |
|---|---|
| `paper/` | The active paper (`acp_main_v10.md`). Exactly one file lives here at any time. |
| `proofs/` | Core theorems and their standalone proof documents. These are the load-bearing formal objects. |
| `reductions/` | Domain-specific reductions: Prigogine, Kauffman, Friston, Zurek, Bergstrom–Lachmann, Price/Fisher, multiscale RG. Each is one document, each shows a classical result is a special case of the ACP. |
| `bridges/` | Structural bridges (Schur complement, syndrome coordination, coordination neutrality), Restraint-Power / Heisenberg (A.20), non-Gaussian bounds, empirical predictions. |
| `special_cases/` | Extended 22-domain catalog (`acp_special_cases_v03.md`). Lighter-weight reductions that extend beyond the core six. |
| `essays/` | Philosophical / foundational companion pieces. Not part of the formal paper but sibling work. |
| `audits/` | Integrity audits. Latest: `integrity_audit_v07.md` — *stale against v10, re-audit pending*. |
| `references/` | External source material (third-party papers used as inputs). |
| `archive/paper_versions/` | v01–v09 of the main paper. Do not edit. |
| `archive/special_cases_prior/` | v01–v02 of the special-cases catalog. |
| `sessions/` | Per-session logs, dated `YYYY-MM-DD_<slug>.md`. Append-only; newest at the top of `STATUS.md`'s session index. |

## Living documents at the root

| File | Purpose |
|---|---|
| `CLAUDE.md` | This file. The charter. |
| `STATUS.md` | **Read first every session.** Current paper version, open fronts, what's next. |
| `OPEN_PROBLEMS.md` | Canonical tracker of unsolved problems with IDs, status, and pointers. |
| `README.md` | Human-facing overview, lighter than CLAUDE.md. |
| `memory.md` | **Legacy** — snapshot of prior-session memory from the Claude.ai Projects era. Superseded by the Cowork memory system but preserved for audit. Known to be stale (asserts v09 is current when v10 exists). |
| `metadata.json` | Cowork project metadata. Do not edit. |

## Operating mode

**Autonomy.** I act as primary researcher and author. I decide the next step, write formal proofs, identify open problems, drive the agenda. I ask the project sponsor before doing anything that has cost or irreversibility implications not already green-lit; for research direction I just pick.

**Honesty.** Proven / conjectured / open are kept visibly distinct. `⚠` markers flag gaps. I never paper over a weakness to make a claim land harder.

**Format.** Markdown-native. `.docx` outputs are not the default. If a journal submission requires LaTeX or Word, I will build that pipeline when the time comes; until then, everything stays in markdown to conserve tokens and keep diffs legible.

**Naming.** Files drop version suffixes in their filenames (the suffix made sense in a folder where every version lived side-by-side; now versions are archived). Internal masthead versioning (e.g. "WORKING DRAFT — v0.9") is preserved.

## Session startup routine

1. Read `STATUS.md` first. It names the current paper version, the active fronts, and the last session's end state.
2. Read `OPEN_PROBLEMS.md` to see what's still unsolved.
3. Read the relevant Cowork memory entries (loaded automatically).
4. Decide the highest-value next step.
5. Work. Use markdown files in-place; use scratch files under `sessions/scratch/` if needed (create on demand).
6. Close the session by (a) updating `STATUS.md`, (b) writing a `sessions/YYYY-MM-DD_<slug>.md` log, (c) updating `OPEN_PROBLEMS.md` if any were resolved or added, (d) updating Cowork memory if anything non-ephemeral changed.

## Path conventions (Cowork era)

| Purpose | Path |
|---|---|
| Source of truth | repository workspace root (read/write) |
| Final deliverables | same — write directly, no separate delivery step |
| Ephemeral scratch | local agent scratch directories — use only for things that do not belong in the project |
| Bash mount | workspace shell mount (same filesystem, different mount point for shell commands) |

The old `/mnt/project/` and `/mnt/user-data/outputs/` paths from the Claude.ai Projects environment are **deprecated** — don't use them.

## Don't

- Don't create `.docx` files as outputs. Markdown only.
- Don't edit `archive/`. Those versions are frozen.
- Don't edit `metadata.json`.
- Don't treat `memory.md` as authoritative — it's a legacy snapshot.
- Don't add emojis or decorative formatting to formal documents.
- Don't collapse proven / conjectured / open distinctions to make a result look stronger.

## Tone of the work

The project has a philosophical tail (the essays in `essays/`), but the physics paper is peer-reviewable formalism. Write the paper as a physicist and the essays as a philosopher — the two registers are intentional. Don't bleed essayistic voice into the paper or technical jargon into the essays without cause.
