---
name: nvgt-engine-source-location
description: The Legacy-NVGT C++ engine source is checked out locally — grep it to confirm exact registered API signatures instead of guessing
metadata: 
  node_type: memory
  type: reference
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
  modified: 2026-07-20T17:36:34.363Z
---

The C++ source for the pinned engine (see [[engine-pinned-to-nvgt2]]) is checked out at:
`C:\Users\tonys\OneDrive\Documents\github\tsatria03\misc\Legacy-NVGT`

**IMPORTANT: this is OUTSIDE the CaveDefender repo** — it's a sibling under the parent `tsatria03/` folder, NOT inside `tsatria03/games/CaveDefender/`. So repo-rooted searches (Glob/Grep/find from the project cwd) will NOT find it and a repo-scoped Explore agent will report "no misc/Legacy-NVGT". Always use the ABSOLUTE path above (e.g. `grep -rn "..." "C:/Users/tonys/OneDrive/Documents/github/tsatria03/misc/Legacy-NVGT/src"`).

Confirmed from `src/filesystem.cpp` (line ~413): `string[]@ find_directories(const string& in pattern)` and `string[]@ find_files(const string& in pattern)` — both take a glob (e.g. `"data/players/*"`) and return **bare names only** (not full paths). `find_files` returns FILES only (skips dirs); `find_directories` returns DIRECTORIES only (skips files) and **skips `.` and `..`**.

When unsure whether an NVGT function exists or what its exact signature is, **grep the source rather than guessing** (important because the user compiles builds themselves — see [[dont-compile-yourself]] — so a wrong API name ships broken):
- `src/*.cpp` `RegisterGlobalFunction(...)` / `RegisterObjectMethod(...)` lines are the authoritative AngelScript signatures (the `other/functions.txt` header list can be stale — e.g. it says `datetime file_get_date_modified` but the real registration in `src/filesystem.cpp` returns `timestamp`).

Confirmed via this source: `timestamp file_get_date_modified(const string& in path)` and `file_get_date_created` (both `Poco::File`-backed, **throw on a missing file** so guard with `file_exists` first), and `int64 file_get_size(const string& in path)`. A `timestamp` converts implicitly to `int64` microseconds since 1970 (same type `now_epoch()` uses in account.nvgt). Used these to give the pronoun/language `.svr` loaders an mtime-based cache.

**Audio volume scale (`src/sound.cpp`):** both `sound` and `mixer` expose a `float volume` property, but the registered getter/setter is `get_volume_alt`/`set_volume_alt`, which uses a **dB-like scale where the value is `(linear*100) - 100`**: `volume = 0` → linear amplitude **1.0** (full), `volume = -100` → linear **0.0** (fully silent). So `-100` is a true mute, not just "-100 dB". A `mixer` also has `set_fx`, `pan`, `slide_volume(target, ms)`. Every `sound_pool` routes its sounds through `pool.mixer` (`handle.set_mixer(pool.mixer)` in the deps' sound_pool.nvgt), so setting `pool.mixer.volume = -100` silences the WHOLE pool including sounds spawned afterward — used by `mute_pools`/`unmute_pools` (decpool.nvgt) for the learn-sounds menu.
