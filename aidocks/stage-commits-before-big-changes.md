---
name: stage-commits-before-big-changes
description: "Proactively flag natural commit break points before a large or risky change, so work stays in small isolated commits rather than one big lump. The dev commits by hand between stages."
metadata:
  node_type: memory
  type: feedback
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
---

When a multi-stage feature has small/safe pieces followed by a large or risky one, **proactively tell the dev to commit the safe pieces before starting the big change** — don't wait to be asked. Call out the break point explicitly: which finished stages to commit now, and which upcoming stage is the "much bigger change" that deserves its own isolated commit. Example (2026-07-15): after #6 (data loader) + #7 (weapon damage) — both small, additive, behavior-neutral — I flagged that #8 (the wood small/medium/large -> block/drift/plank/shaft rename, which touches persisted counts + reconnect) is the big one and should be committed separately. The dev confirmed and asked me to keep doing this.

**Why:** the dev commits by hand and wants each risky change isolated in its own commit, so if something breaks it's easy to bisect/revert without untangling it from unrelated small edits. A big change lumped in with little ones is hard to review by screen reader and hard to roll back cleanly.

**How to apply:** at the end of a stage that completes the safe/additive work, before diving into the risky next stage, say plainly "commit now — the next part (X) is the big change and should be its own commit." Pair this with the standing [[list-modified-files]] + [[relaunch-notice]] close-out, and with [[confirm-before-implementing]] for the risky stage's plan (get sign-off on the migration approach first). Relevant to staged/multi-task features like the weapon/item data-driven reorg (see [[game-data-file-layout]], [[changelog-rules]] on multi-entry features).
