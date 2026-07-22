---
name: release-cadence-batches-versions
description: "The dev batches several versions into one public release. 4.2 shipped publicly on 2026-07-19 (bundling 4.1); the next in-flight version is 4.3. While a version is unreleased, log every player-facing change (features AND fixes) in the changelog under the active version block — no README-only routing."
metadata: 
  node_type: memory
  type: project
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
  modified: 2026-07-20T02:40:59.917Z
---

The dev doesn't release at every version bump — they batch. **4.2 was released to the public on 2026-07-19** (with 4.1 bundled in). The next in-flight version is **4.3**, again unreleased until the dev decides to ship. The first player-facing change of a new version needs a fresh `New in X.Y.` block at the TOP of the changelog. "Post changes" (see [[post-changes-no-changelog]]) are the quiet pre-release touch-ups made just before shipping a version — those don't get changelog entries.

**Why it matters:** it resolves the recurring changelog-vs-README question. Earlier in this project a "post-4.0 audio/behavior fixes go to the README, not the changelog" idea floated around — that only applies to changes made AFTER a version has actually shipped to players. Since the game stays unreleased through 4.1 and 4.2 development, **all** player-facing changes (features and bug fixes alike) go in `cf/client/docks/changelog.txt` under the active `New in X.Y.` block, following [[changelog-rules]]. Don't divert fixes to the README while a version is still unreleased.

**How to apply:** when a version is in active development (unreleased), add player-facing changes to the changelog normally. Only consider README-only routing once that build has been released to players — and even then, confirm with the dev. Never hand-edit [[dont-touch-version-txt]]; flag when a new changelog block needs a version bump.
