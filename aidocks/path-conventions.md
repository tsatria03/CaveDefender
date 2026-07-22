---
name: path-conventions
description: "Where things live in CaveDefender — the src/ (code) + cf/ (assets+launchers) + release/ split, appdata, sound folders, server data, the engine DLL"
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

**Major restructure 2026-06-18: source and assets are now SEPARATED into three top-level folders at the repo root.**
- **`src/`** = code only. `src/client/` (entry `cfc.nvgt`, `includes/`) and `src/server/` (entry `cfs.nvgt`, `includes/`). NO assets here.
- **`cf/`** = assets + launchers + compilers. `cf/client/` = `lib/` (GameEngine64.dll + oggenc2.exe), `sounds/`, `docks/`, `cfc.py` (launcher), `cfcm.py` (compiler). `cf/server/` = `data/`, `docks/`, `lib/`, `cfs.py` (launcher), `cfsm.py` (compiler). (Naming: `cfc.py`/`cfs.py` = launchers; `cfcm.py`/`cfsm.py` = compilers — all four in `cf/`, moved there 2026-06-18.)
- **`release/`** = compiled builds: `release/windows/CaveDefender/{client/cfc,server/cfs}` + `release/archives/`.

Both halves still use the **same glob-include layout**: `includes/includes.nvgt` pulls in `main/deps/*`, `main/functions/*`, `main/globals/*` (server has `menus/`/`parsers/` stubbed out).

**How source/assets connect (the key trick):** launchers run the `.nvgt` script from `src/<side>` but set **cwd = `cf/<side>`**, so every cwd-relative path in code (`lib/GameEngine64.dll`, `sounds/...`, `lib/oggenc2.exe`, `docks/...`, `data/...`) resolves against `cf/<side>`. At COMPILE time there are **NO `#pragma asset` lines** (a pragma approach was tried and dropped — this nvgt2 build resolves pragma asset paths relative to the OUTPUT dir, making the `..` depth brittle/timing-dependent). Instead the per-side compilers run `nvgt -c` to make a bundle folder (NVGT auto-copies its runtime DLLs into the bundle's `lib/`; global `C:\nvgt2\config.properties` sets `build.windows_bundle=1` = folder output), then **copy** that side's `cf/<side>` assets into the bundle next to the exe (client: `lib` merged → adds GameEngine64.dll + oggenc2.exe, plus `sounds`, `docks`; server: `data`, `docks`). **No in-code path needed changing for the move** — only the launcher cwd (runtime) and the compilers' copy step (build) know about the split. (Verified 2026-06-18: both sides compile + assemble cleanly; every path in src is cwd-relative or absolute appdata/temp.)

**Launchers (Python, in `cf/<side>`):** `cf/client/cfc.py` — `subprocess.Popen` + `CREATE_NO_WINDOW`, exits immediately (console only flashes, no persistent cmd window). `cf/server/cfs.py` — **blocking** `subprocess.run`, cmd window **stays open the whole session** (it's the server's UI; nvgt inherits it). Each shows its own NVGT window too. **Compilers (Python, in `cf/<side>`, per-side):** `cf/client/cfcm.py` → only the client (runs `nvgt -c` from `src/client`, copies `cf/client` assets in) → `release/windows/CaveDefender/client/cfc`; `cf/server/cfsm.py` → only the server (from `src/server`) → `.../server/cfs`. Each wipes only its own side's release subfolder and ends with an `input()` pause. All four scripts hard-code `C:\nvgt2\nvgt.exe`, need Python, and the console ones want `.py`→`python.exe`. The server's cmd window is its UI, so `cfs.nvgt` sets a `show_game_window` title (version/port/user-limit) then `if(!SCRIPT_COMPILED) hide_window();` — interpreted = headless; a compiled build keeps the NVGT window.

**Client appdata** (absolute, via `DIRECTORY_APPDATA` — unaffected by the code layout):
- Settings + saved account: `tsatria03/CaveDefender/preffs/settings.cvf` (the `st` savedata; the last-account name/password/gender are merged in here, NOT a separate `account.cvf`).
- Buffer export logs: `tsatria03/CaveDefender/logs`.

**Engine DLL:** `cf/client/lib/GameEngine64.dll`, loaded cwd-relative via `engine.load("lib/GameEngine64.dll")` (resolves under the launcher's cwd `cf/client`). Only works with the **patched NVGT** (the pinned `C:\nvgt2` fork, see [[engine-pinned-to-nvgt2]]) — `library::load()` resolves relative paths against the working directory (stock NVGT's SafeDllSearchMode excludes the CWD, so a subfolder DLL fails). `oggenc2.exe` (voice encoder) sits beside it in `cf/client/lib/`, run cwd-relative as `lib/oggenc2.exe`.

**Client sounds** (`cf/client/sounds/`, referenced cwd-relative as `sounds/...`), per-category with per-type subfolders. NOTE: `player/weapons/` was renamed to `weapons/` and `player/items/` to `objects/items/` (the UI tree stayed `ui/`):
- `ui/buffer/`, `ui/dlg/`, `ui/menu/`, `ui/misc/` (online, offline, playerchat, privchat, von, voff, pingstart/stop, welcome, newmotd, kick, ban, promote/demote, notify1-5, playermute/playerspeak, toggleon/off, beacon, staffchat, teamchat, mapchat, newchar).
- `objects/platforms/<tile>/step1-5.ogg` — footsteps per tile: `carpet` (lobby), `cave`, `cement` (office room).
- `objects/walls/<wall>/...` — `wallbuilding/bump`, `wallgeneric/bump` (office room), `wallwood/{bump,death,hurt1-3}`.
- `objects/items/<item>/{drop,loop,place,take}.ogg` (wood…).
- `weapons/<weapon>/...` — axe (draw/fire/hit), crowbar (draw/fire1-3/hit1-3), hammer (draw/fire/hit).
- No swappable sound packs (see [[no-sound-pack-support]]). `cement`/`wallgeneric` are reserved for the **office room** map (50x50), like the lobby's `carpet`/`wallbuilding`.

**Sound-pool assignments (LOCKED by the dev):** `p` (the general pool) = UI/local sounds, **other players' footsteps and wall bumps** (the `footstep` net message plays `sounds/<subpath>.ogg` 3D on `p`), and the **wall death/hurt** sounds when gameplay lands. `beaconpool` = player locator beacons. When the game is built: `objpool` = items (wood, etc.), `weaponpool` = weapons (axe/crowbar/hammer). All pools' listener is re-anchored to `me` every frame by `update_sound_pools()`. Remote footsteps work: the mover's `playstep()` sends `step <soundsubpath> <x> <y>` (for a wall bump, sent *before* `bounce()` so the position is the wall tile); the server relays it as `footstep <subpath> <x> <y>` to same-`room_id` peers only.

**Server data** (`cf/server/data/`, referenced cwd-relative as `data/...`):
- Config: `data/preffs/conf.svr`; MOTD: `data/preffs/motd.svr`.
- Accounts: a **folder per account** at `data/players/<username>/` (lowercase), one small file per field (`username.usr`, `password.usr` = `<salt>:<hash>`, `gender.usr`, `rank.usr`, `muted.usr`, `banned.usr`). The salt (plaintext, not secret) rides inside password.usr joined to the hash by a colon. muted/banned: empty=not, 0=indefinite/permanent, else epoch. (Replaced the old single `<username>.usr` key=value file.)

`map.nvgt` now builds the correct per-type subfolder paths — `objects/walls/<wall>/bump.ogg` and `objects/platforms/<tile>/step<n>.ogg` — matching the layout above (the old flat-path gap is resolved). `spawn_map()` lays a `wallwood` border around a `cave` interior and `me` starts at `(1,1)` on the interior. The offline wall-breaker reference lives at `C:\Users\tonys\OneDrive\Desktop\Sammy Center`.
