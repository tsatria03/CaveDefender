---
name: dont-touch-version-txt
description: "Never edit build/version.txt unless the dev explicitly says so — they set the version number by hand, sometimes to match another server for connection testing."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

Do NOT edit `build/version.txt` on your own — **not even when opening a new changelog version block** (the [[changelog-rules]] used to imply a bump was required; it isn't your call).

The dev sets the version number by hand and sometimes changes it for reasons unrelated to the changelog — e.g. temporarily setting it to **another server's version to test connecting to a server someone else hosts** (the login version check must match, so the version string decides which servers the game will join).

**Why:** an unasked-for bump silently changes which servers the game can connect to, breaking the dev's live testing.

**How to apply:** when a new `New in X.Y.` changelog block needs a version, or you think `version.txt` looks stale/wrong, **flag it and let the dev set it** — never write the file yourself unless they explicitly ask. (Learned 2026-07 after I bumped 3.5→3.7 while the dev had deliberately set 3.5 to test against someone's 3.5 server.)
