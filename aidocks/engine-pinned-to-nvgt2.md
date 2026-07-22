---
name: engine-pinned-to-nvgt2
description: "CaveDefender runs on a pinned legacy NVGT fork at C:\\nvgt2; current upstream NVGT is incompatible — don't suggest upgrading"
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

CaveDefender (and all of tsatria03's games) target a **pinned legacy NVGT fork**, the runtime installed at **`C:\nvgt2\nvgt.exe`**. The launcher/build scripts in `game/cf/` hard-code this path. A *newer* stock NVGT (with miniaudio) is also installed as plain `nvgt` on the machine — that one is for testing other people's games, NOT for this project.

**Do not suggest upgrading to current/upstream NVGT, and don't treat upstream NVGT docs/source as authoritative here.** Migration is impossible without rewriting the games, because upstream diverged incompatibly in two ways:
1. **The `library` (DLL-call) object was rewritten differently.** The fork's `library.call()` returns a **`dictionary@`** (keys `"0"`=return, `"1".."N"`=output params) and `library.load()` resolves relative paths against the CWD so `lib/GameEngine64.dll` loads past Windows SafeDllSearchMode. Upstream now returns a single **`var@`** (libffi) with stock `SDL_LoadObject` (no CWD resolution). CaveDefender's `GameEngine.nvgt` wrapper depends entirely on the `dictionary@` + CWD contract (see [[path-conventions]]).
2. **Upstream switched audio to miniaudio**; the fork stays on **BASS**. The game's `sound_pool`/HRTF code is written against the BASS-backed sound object.

The fork is itself tsatria03's own work, not a stale upstream copy — it adds engine objects upstream lacks/removed (microphone, bassmidi, tone_synth, input_bind, joystick, combination, uuid), crypto (AES/ChaCha via monocypher), and more. The fork source lives at **`C:\Users\tonys\OneDrive\Documents\github\tsatria03\misc\Legacy-NVGT`**, whose own `CLAUDE.md` has a full catalog of how it diverges from the `320e9ce` upstream baseline. This is why the engine is named `nvgt2` and kept separate.
