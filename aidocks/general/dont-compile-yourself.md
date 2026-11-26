---
name: dont-compile-yourself
description: "Don't run the client/server compilers or nvgt -c — the user compiles and verifies builds themselves"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

Do NOT compile the game yourself — don't run `cfcm.py`/`cfsm.py`, `nvgt -c`, or otherwise invoke the NVGT compiler to build the client or server. Make the code edits and stop; the user compiles and verifies builds on their own machine.

**Why:** the user prefers to control the build/verify step themselves (and compiling spawns the pinned `C:\nvgt` runtime, see [[engine-pinned-legacy-nvgt]]).

**How to apply:** after editing `.nvgt` (or build) files, just report the change and the Files changed / Relaunch list. It's fine to read code, reason about correctness, and note "this should compile," but never actually run a compile to check. (Running other read-only diagnostics is still fine.)

**Exception: only when the dev explicitly asks.** On 2026-11-25 the dev asked Claude to compile the offline proof-of-concept test in user/poc ("Please try to compile it using this. C:\nvgt\nvgt.exe"), and Claude ran `C:\nvgt\nvgt.exe -c poc_host.nvgt` once. That was a one-off for a standalone test, not a standing permission: never compile the game (client or server) unless asked again, and don't run the resulting exe if it would block on a dialog; let the dev run it.
