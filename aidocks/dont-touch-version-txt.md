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
