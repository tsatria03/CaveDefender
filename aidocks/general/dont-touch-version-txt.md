---
name: dont-touch-version-txt
description: "Bump build/version.txt to match each new changelog version block; the dev only overrides it to test against someone else's server, and it's their call whether to change it back."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

**Updated rule (2026-07, supersedes the old "never touch it"):** when you open a new `New in X.Y.` changelog block, **bump `build/version.txt` to that same X.Y** as part of the change. Keep the two in lockstep — a new changelog version should always be reflected in version.txt.

The ONE reason the dev sets version.txt to something else is to **test connecting to another server someone else hosts** (the login version check must match, so the version string decides which servers the game will join). That's their manual override, and it's their call whether to change it back — don't undo it or re-bump on top of it.

**Why:** the dev asked for the version to track the changelog automatically so they don't have to bump it by hand each release; the only exception is their deliberate cross-server test.

**How to apply:** new changelog block → set version.txt to match, mention it in the Files changed list. If version.txt already holds a value that looks like a deliberate mismatch (e.g. it's LOWER than the latest changelog block, suggesting a cross-server test in progress), flag it and ask before changing rather than assuming. See [[changelog-rules]].

**RELATED — `rulesver` in `data/preffs/main/conf.svr` is ALSO dev-owned; do NOT bump it yourself (confirmed 2026-08).** It gates the rules re-agreement (raising it forces everyone to re-read + re-agree once). The dev keeps it **in step with the MAJOR game version** — game 5.0 → `rulesver=5` — so edits to the rules text within a version are NOT a reason to bump it; the current version's rules just change in place. When a rules change might warrant re-agreement, FLAG it and let the dev decide (they may prefer to keep re-agreement tied to the major-version bump). I bumped 5→6 for a rules edit and the dev reverted it to 5. See [[docks-and-help]].
