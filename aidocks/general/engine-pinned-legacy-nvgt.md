---
name: engine-pinned-legacy-nvgt
description: "CaveDefender runs on the pinned legacy NVGT fork at C:\\nvgt (source: misc\\Legacy-NVGT); C:\\nvgt2 is the unused miniaudio build; upstream NVGT is incompatible — don't suggest upgrading"
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

CaveDefender (and all of tsatria03's games) target a **pinned legacy NVGT fork**, the runtime installed at **`C:\nvgt\nvgt.exe`**. The launchers in `cf/<side>/` and `downcheck.nvgt` hard-code this path, and `build/tools.py` reads it from `~/.game_tools/tools.ini` (`nvgt = C:\nvgt\nvgt.exe`). Its C++ source is **`C:\Users\tonys\OneDrive\Documents\github\tsatria03\misc\Legacy-NVGT`** (see [[nvgt-engine-source-location]]).

**`C:\nvgt2` is NOT this game's engine.** It holds the newer miniaudio-based NVGT build, kept for testing other people's games; CaveDefender never uses it. Don't let the "2" mislead: legacy = `C:\nvgt`, miniaudio = `C:\nvgt2`. (This memory was once misleadingly named `engine-pinned-to-nvgt2`; renamed 2026-11-23.)

**Do not suggest upgrading to current/upstream NVGT, and don't treat upstream NVGT docs/source as authoritative here.** Migration is impossible without rewriting the games, because upstream diverged incompatibly in two ways:
1. **The `library` (DLL-call) object was rewritten differently.** The fork's `library.call()` returns a **`dictionary@`** (keys `"0"`=return, `"1".."N"`=output params) and `library.load()` resolves relative paths against the CWD so `lib/GameEngine64.dll` loads past Windows SafeDllSearchMode. Upstream now returns a single **`var@`** (libffi) with stock `SDL_LoadObject` (no CWD resolution). **CaveDefender itself no longer uses the `library` object** — its only user was the `GameEngine.nvgt` wrapper, deleted 2026-07-14 when the DLL was replaced by the native tile store (see [[game-engine-dll]]). This point still matters for the dev's other legacy-engine games and for any future native DLL, so the pin stands; for CaveDefender today the binding reason is #2.
2. **Upstream switched audio to miniaudio**; the fork stays on **BASS**. The game's `sound_pool`/HRTF code is written against the BASS-backed sound object.

The fork is itself tsatria03's own work, not a stale upstream copy — it adds engine objects upstream lacks/removed (microphone, bassmidi, tone_synth, input_bind, joystick, combination, uuid), crypto (AES/ChaCha via monocypher), and more. The fork source lives at **`C:\Users\tonys\OneDrive\Documents\github\tsatria03\misc\Legacy-NVGT`**, whose own `CLAUDE.md` has a full catalog of how it diverges from the `320e9ce` upstream baseline. This is why the engine is named `nvgt` and kept separate.
