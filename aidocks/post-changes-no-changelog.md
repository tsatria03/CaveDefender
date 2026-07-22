---
name: post-changes-no-changelog
description: "A \"post change\" is a quiet final touch-up before release — readme yes, changelog no"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
  modified: 2026-07-19T19:17:42.875Z
---

When the dev calls something a **"post change"** (e.g. "now for the post 4.2 changes"), it means a final touch-up folded in right before releasing that version — a fix or behavior a player only notices if they go looking for that exact action. These do **NOT** get a changelog entry (the changelog is for player-visible headline changes), and they do **NOT** start a new version block or bump the version. They ride out with the version being released.

**Why:** the dev batches versions and, when a version's changelog is "full enough" (~10 entries), starts wrapping it for release; post changes are the invisible polish on top, not release highlights.

**How to apply:** for a post change, update the **readme** (or other behavior docs) if there's a detail worth documenting, but leave `docks/changelog.txt` alone and don't touch `version.txt`. If you're unsure whether a change is "post" or headline-worthy, ask. Relates to [[changelog-rules]], [[release-cadence-batches-versions]], [[dont-touch-version-txt]].
