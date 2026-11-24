---
name: game-engine-dll
description: "HISTORY ONLY: the PureBasic GameEngine64.dll is GONE (removed 2026-07-14, commit c26ac21) and replaced by the in-script native tile store in client game/platform.nvgt. Nothing in CaveDefender loads a DLL through NVGT's library object any more. Read when touching map tiles or if old notes mention the DLL."
metadata: 
  node_type: memory
  type: project
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

**The DLL is no longer used.** CaveDefender once spawned map tiles through a third-party PureBasic `GameEngine64.dll` (wrapper `src/client/includes/main/deps/GameEngine.nvgt`, `load_engine()` at startup, loaded cwd-relative from `cf/client/lib/`). It was dropped in two steps:
- **2026-06-18, commit f4b28b4** — the DLL files left git (`client/lib`, `server/lib`); `lib/` has been git-ignored since, so later DLL changes never show in history.
- **2026-07-14, commit c26ac21 ("Major map enhancements.")** — the real switch: the 351-line wrapper was deleted, its include removed from `cfc.nvgt`, and the map functions reimplemented natively in `platform.nvgt` (wall.nvgt lost ~78 lines of DLL workarounds). Use this date as "when the DLL stopped being used".

**What replaced it: the native tile store** — client `src/client/includes/game/platform.nvgt` (moved from `main/globals/` in the late-2026 folder reorg). `platform@[] platforms`; `spawn_platform(minx,maxx,miny,maxy,tile)` returns an index handle; `get_tile_at(x,y)` scans newest-first and skips nulls (latest paint wins); `remove_platform(id)` nulls one slot; `clear_map()` empties the list. No z, zones, volume or pitch. It mirrors SimpleFighter's platform.nvgt, rebuilt lean. The server never used the DLL (its wall logic was always native).

**Why it was replaced:** the DLL's only removal call was `clear_map()` (wipe everything) and `spawn_platform` returned nothing, so one wall/tile could never be destroyed — `destroy_wall_client` had to paint a floor tile over a broken wall and leave dead tiles underneath. The handle-based store fixes that.

**What is now stale elsewhere:** there is no `load_engine()`, no "DLL missing" startup alert, no `GameEngine64.dll` in `cf/client/lib/` or in release builds, and no third-party code the dev "can't modify" in the map path. `cf/client/lib/` now holds only the audio DLLs (bass, bassmix, bass_fx, opus, phonon) and screen-reader DLLs. The patched `library::load()` in the pinned NVGT fork ([[engine-pinned-legacy-nvgt]]) was made for this DLL; nothing in the game calls the `library` object now, so that patch no longer matters to CaveDefender (the fork is still pinned for other reasons). (The last code mention, a comment above `restart()` in `src/client/cfc.nvgt`, was corrected 2026-11-23.)
