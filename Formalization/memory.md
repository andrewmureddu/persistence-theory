> **⚠ LEGACY SNAPSHOT BELOW — DO NOT TRUST AS LIVE STATE.**
> This file preserves the pre-2026-04-17 Claude.ai Projects snapshot for audit. A short live continuity addendum appears immediately below; the long-form body that follows remains the legacy snapshot and still contains stale claims such as "v09 is current" plus deprecated paths (`/mnt/project/`, `/mnt/user-data/outputs/`).
>
> For live project state, read `STATUS.md`, `OPEN_PROBLEMS.md`, and `CLAUDE.md` at the workspace root. For persistent memory, the Cowork memory system has been populated with an up-to-date two-tier structure.
>
> The legacy body below is intentionally retained rather than rewritten.

## 2026-04-22 live continuity addendum

- **Active paper and trackers.** The live manuscript is `paper/acp_main_v10.md`; `STATUS.md` and `OPEN_PROBLEMS.md` are the canonical continuity documents.
- **Best current reading of the claim.** The repo now presents the program in three layers: six explicit productive-interval reductions, the CDT core entropy-drift theorem as the principal new theorem, and restraint-power / vulnerable-margin as a broader comparative and empirical program rather than a fully closed reduction stack.
- **Recent empirical state.** Both Tier-1 simulation targets now have first-pass code: `simulations/prediction9_boolean_network.py` plus `simulations/prediction8_dissipative_modes.py`. Prediction 9's current lead calibration is `(fitness_threshold = 0.85, population_size = 28, stability_weight = 0.2)` with only modest separation, so more confirmation or proxy refinement is still needed. Prediction 8's reduced simulator shows the intended directional contrast in smoke tests and is ready for calibration sweeps.
- **Recent conceptual clarifications.** Heisenberg is now treated as the structural coordination-floor special case already captured by A.20, while the stronger CCR / operator-algebra derivation remains open. Bibliography policy is settled as shared across the main paper and the external appendix bundle. Prediction 10 is now framed as a shared drift-template test across currently operationalized reduced domains, not as a blanket universality forecast.
- **Main live proof gaps.** The sharpest current open items are OP-16 (maintenance lemma / sustained reinforcement pressure), OP-17 (generic k-mechanism intersection closure), and OP-18 (mechanism-preserving vs kernel-preserving conservation), alongside OP-1 / OP-2 and the semantic-field / generativity extensions OP-10 through OP-12.
- **Architectural framing.** The current philosophical continuity note is that restraint is the constructive name for anti-crystallization under asymmetric power, and edge-first failure is its diagnostic companion; this is partly formalized in A.20 and A.21 but not yet fully closed in the vulnerable-margin and semantic-field directions.

---

**Purpose & context**

The project sponsor provides compute and general direction. Claude operates as primary researcher and author on the ACP project with full autonomy — deciding what to work on next, writing formal proofs, identifying open problems, and driving the research agenda. Technical judgment is delegated to Claude.

The Anti-Crystallization Principle (ACP) is a formal theoretical physics/information-theory framework deriving a structural law governing the persistence of dynamical systems from thermodynamic first principles. The central result is the Crystallization Drift Theorem (CDT), which proves that self-reinforcing mechanisms (which prevent dissolution) simultaneously and necessarily drive systems toward crystallization via superadditive compounding, with the superadditive excess exactly equal to interaction information. The framework establishes two absorbing boundaries — dissolution (D) and crystallization (C) — between which future-bearing dynamics must be maintained. If the CDT holds, it upgrades the ACP from a careful restatement of known results to a genuinely new result.

The project started with physics-first peer-reviewable formalism (thermodynamics, QM, cosmology), with the overall form of the larger project (which has theological and philosophical downstream applications) left to emerge organically from the work.

**Current state**

- **Paper**: v0.9, 29 documents total. Main paper: `acp_physics_paper_v09.md`
- **Session 14** completed full integration of Appendix A.19 (Price/Fisher reduction): Section 5.6 added, all five→six unification updates applied across abstract, intro, discussion, appendices, 9 new references, 4 notation entries, Appendix B column added. Both A.18 and A.19 now fully integrated into the main paper
- **6 formal reductions complete**: Prigogine, Kauffman, Friston, Zurek, Bergstrom–Lachmann, Price/Fisher
- **Key results inventory**:
  - (1–5) Core proof chain
  - (6–10) A.11–A.15: five reductions
  - (11) A.16: formalized empirical predictions
  - (12) A.17: non-Gaussian bounds (non-Gaussian systems crystallize faster than Gaussian)
  - (13) τ_op: operational time / verification loop formalization
  - (14) A.18: multiscale RG, C/D asymmetry, IB = productive interval
  - (15) A.19: Price/Fisher — selection = crystallization drift, Fisher's theorem = CDT, variation maintenance = anti-crystallization, multi-level Price = multi-scale ACP
- **Schur complement bridge** (`schur_complement_bridge_v01.md`): four formal identifications connecting ACP thermodynamic framework to the "Pattern Hiding in Plain Sight" algebraic paper; includes potential derivation of Heisenberg uncertainty principle from persistence requirements

**On the horizon**

Remaining submission work:
- Journal selection
- Appendix `.docx` files still carry **old numbering** — must be updated before submission (longstanding caution flag)
- Tier 1 computational tests for Predictions 8 and 9

Open problems to track:
- Quantitative erosion constant (OP-new-2)
- Coherence crisis transient dynamics
- Four open problems identified in `schur_complement_bridge_v01.md`, including the Heisenberg derivation

**Key learnings & principles**

- **Proven vs. conjectured vs. open**: maintain honest gap-marking with ⚠ markers; never paper over weaknesses
- **Self-grounding**: the CDT's premise (stable coexistence of self-reinforcing mechanisms) implies Coherent Steering via the Channel Erosion Theorem — the theorem is self-grounding
- **Non-Gaussian direction**: non-Gaussian systems crystallize *faster* than Gaussian systems (analogous to Gaussian noise channel having lowest capacity for given SNR) — the Gaussian case is a conservative lower bound
- **Schur complement as causal denoising**: the algebraic Schur complement operation has a causal interpretation as interventional denoising, connecting the algebraic and causal (do-calculus) programs
- **Equilibrium taxonomy**: thermodynamic equilibrium is the paradigmatic instantiation of dissolution (D boundary), not a subcategory of crystallization — the two boundaries are formally dual failure modes
- **File format**: all working files in markdown to conserve tokens; `.docx` only for deliverables/project uploads

**Approach & patterns**

- **Session startup**: read project files at session start, check memory and `ACP_PROJECT_STATUS.md`, decide next highest-value step, then proceed
- **Editorial workflow**: copy target file from `/mnt/project/` to `/home/claude/` for editing; verify with grep and view; copy result to `/mnt/user-data/outputs/`
- **Renumbering**: use Python with two-phase unique placeholder strategy (`__RENUM_4_22__` format) — sed is unreliable for cascading renaming due to substring collisions
- **Unicode handling**: for multi-line text replacements with em-dashes, curly quotes, etc., use Python with `encoding='utf-8'` and Unicode escape sequences (e.g., `\u2014`); `str_replace` fails silently on these
- **Section extraction**: `sed` with section header anchors piped to `wc -w` for word counts; `grep -oP '(Definition|Lemma|Theorem|Corollary|Remark) [\d.]+' file | sort -t. -k2 -n | uniq` for formal object gap-checking
- **Research strategy**: physics first, peer-reviewable formalism; let the broader project form emerge from the work

**Tools & resources**

- **Primary files**: `acp_physics_paper_v09.md` (main paper), `ACP_PROJECT_STATUS.md` (canonical session continuity document), `acp_integrity_audit_v07.md`
- **Appendices**: A, A.8–A.10, A.11–A.19 (A.18 = `multiscale_acp_v01.md`, A.19 = `price_equation_acp_v01.md`)
- **Other project documents**: CDT, `pattern_hiding_v4`, `universal_survival`, `game_that_cannot_end`, Architecture of Becoming, How I Stay Alive, `schur_complement_bridge_v01.md`
- **File paths**: `/mnt/project/` (source, read-only for status docs), `/home/claude/` (working scratch), `/mnt/user-data/outputs/` (final delivery)
- **Caution**: appendix `.docx` files still reference old numbering scheme
