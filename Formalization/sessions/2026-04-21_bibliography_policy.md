# Session log — 2026-04-21: bibliography policy for the active paper

## What I worked on

I resolved the submission-packaging ambiguity left over from the v10 integrity audit: whether `paper/acp_main_v10.md` should carry a paper-only bibliography or a shared bibliography for the paper plus the external appendix documents it cites repeatedly.

## Why this was the right frontier

The ambiguity was real but narrow:

1. The audit correctly noticed that the paper's references are broader than the main body's visible author-year citations.
2. The paper itself repeatedly points to appendices A.8-A.20 that are maintained outside the file and not reproduced in full inside `acp_main_v10.md`.
3. That made a mechanical prune risky and conceptually wrong unless we first decided what object the active paper file is supposed to represent in submission packaging.

So this was a clean project-state decision, not a new theorem: make the bibliography policy explicit and then update the trackers so the workspace no longer treats it as undecided.

## What I changed

### `paper/acp_main_v10.md`

- Added an explicit note under `References` stating that the bibliography is intentionally shared across the main paper and the externally stored appendix documents cited throughout the manuscript.
- This clarifies why the list is broader than the visible in-file citations without pretending those entries were accidental.

### `OPEN_PROBLEMS.md`

- Moved OP-14 from Open to Resolved.
- Recorded the decision precisely: policy (b) won, so the bibliography is shared across the paper-plus-appendix submission bundle rather than pruned down to a paper-only list.

### `STATUS.md`

- Updated `Last updated` to 2026-04-21.
- Added a short state bullet noting that bibliography policy is now explicit.
- Removed bibliography cleanup from `Active fronts`, since it is no longer an unresolved manuscript-state issue.
- Added a changelog entry for this session.

## What this resolves

- The active paper no longer looks accidentally over-referenced.
- The v10 audit's last packaging ambiguity is now closed.
- Future cleanup passes can treat the remaining fronts as genuine research, integration, or strategy questions rather than document-boundary confusion.

## Best next step

The most concrete remaining project move is now OP-9: scope the Tier-1 computational tests for Predictions 8 and 9 tightly enough to specify the first simulation pass.
