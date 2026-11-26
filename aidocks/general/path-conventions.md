---
name: path-conventions
description: "Where things live in CaveDefender: the src/ (code) + cf/ (assets+launchers) + build/ + release/ split, the cwd trick, includes/game + includes/main, sounds/main + sounds/game, server data host/ + config/, client data config/, appdata, lib/ DLLs. Updated for the 2026-11 reorgs (no boxing, no engine DLL, data split 2026-11-25)."
metadata:
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

**Top-level layout (split 2026-06-18, reorganized again 2026-11-23/24):**
- **`src/`** = code only. `src/client/` (entry `cfc.nvgt`) and `src/server/` (entry `cfs.nvgt`, plus the `downcheck.nvgt` supervisor), each with `includes/`. Inside `includes/`: **`game/`** (gameplay modules: client bot, burn, item, platform, wall; server burn, enemy, heal, item, wall) and **`main/`** (`deps/`, `functions/`, `globals/`, and on the client `menus/` + `parsers/`). `includes/includes.nvgt` globs `game/*` FIRST, then each main subfolder; a glob only reaches files directly in its folder. Details: [[include-tree]].
- **`cf/`** = runnable assets + launchers. `cf/client/` = `lib/` (audio DLLs bass/bassmix/bass_fx/opus/phonon + screen-reader DLLs; git-ignored), `sounds/` (see [[audio-and-sounds]]), `docks/`, `data/` (scriptkeys.srk + config/), `cfc.py`. `cf/server/` = `data/`, `docks/` (help + rules pages), `sounds/` (soundboard clips), `lib/` (git-ignored), `cfs.py`.
- **`build/`** = `tools.py` (the unified compile/package/release pipeline, plus commit helpers), `tools.bat` (runs it via `py -3.12`, with a fallback to `%LOCALAPPDATA%\Programs\Python\Launcher\py.exe`), `tools.ini`, `version.txt` (the single version source). See [[launchers-and-running]].
- **`release/`** (git-ignored) = `release/windows/CaveDefender{Client,Server}_password_is_<pw>/{cfc,cfs}` + `release/archives/` (two password-protected .7z).
- **`tests/`** (tracked) = standalone NVGT test scripts the dev runs by hand, outside the game, e.g. `tests/interact/poc_host/poc.nvgt`, the offline-module proof of concept ([[offline-module-poc]]). Their `.txt` output is git-ignored (`tests/**/*.txt`).
- **`user/`** (git-ignored) = the dev's private scratch area; only look inside where the dev points.

**The cwd trick:** each launcher runs the `src/<side>` script with **cwd = `cf/<side>`**, so every cwd-relative path in code (`sounds/...`, `docks/...`, `data/...`, `lib/...`) resolves against `cf/<side>`, while `#include` paths resolve against `src/<side>`. There are NO `#pragma asset` lines (tried and dropped: this nvgt build resolves pragma asset paths relative to the OUTPUT dir). At build time `tools.py` runs `nvgt -c` from `src/<side>` (bundle folder output; NVGT auto-copies its runtime DLLs into the bundle's `lib/`) and then COPIES that side's `cf/<side>` asset folders in next to the exe. Since 2026-11-24 nothing is packed into the exe (Enigma boxing removed, [[build-tools-remove-boxing]]): every asset folder ships loose and editable.

**Client sound paths** — the full folder map is in [[audio-and-sounds]]. In short: `sounds/main/ui/{buffer,dialog,keyboard,menu}`, `sounds/main/misc`, `sounds/game/equipments/{items,weapons}`, `sounds/game/objects/audio/{ambience,music}`, `sounds/game/objects/construction/{platforms,walls}`. Paths also travel inside network messages, so a folder rename is a protocol change ([[sound-path-repointing]]).

**Server data** (`cf/server/data/`, cwd-relative as `data/...`; split into host/ and config/ on 2026-11-25, [[data-reorg-repointing]]):
- `data/host/` = what only a server has.
  - `data/host/main/` — conf.svr, motd.svr, chatfilter.svr, languages.svr, pronouns.svr, peak.svr, plus the runtime-written feedback.svr / reports.svr (git-ignored, private).
  - `data/host/game/players/<username>/` — one folder per account, one small file per field. **Git-ignored and scrubbed from all history** because the repo is public ([[privacy-cleanup]]); the field format is in [[accounts-system]]. Never commit it.
- `data/config/` = the game rules (what an offline client would also need).
  - `data/config/main/modes.ini` (game tuning, was conf.gvr) and `effects.ini` (cave acoustics, was effects.gvr). Comment lines start with `;` (gamedata.nvgt's read_kv also still accepts `#`).
  - `data/config/game/equipments/weapons/<class>/<name>.<mel|arc|exp|art>` and `data/config/game/equipments/items/{wood/*.mtr, ammo/*.amt}` — read at boot by gamedata.nvgt; a missing file silently falls back to code defaults ([[game-data-file-layout]]).

**Client data** (`cf/client/data/`): `scriptkeys.srk` at the root, plus `config/` — byte-identical copies of the server's `config/main/{modes,effects}.ini` and `config/game/equipments/`, added for the planned offline mode. No client code reads them yet, and the two copies must be kept in sync by hand.

**Client appdata** (absolute, via `DIRECTORY_APPDATA`, under `tsatria03/CaveDefender/`, unaffected by the repo layout): `preffs/settings.cvf` (settings + the saved account), `logs/` (buffer exports), `onoffcache/` and `soundcache/` (downloaded online/offline and soundboard clips).

**No engine DLL.** `GameEngine64.dll` was replaced by the native tile store in client `game/platform.nvgt` on 2026-07-14 ([[game-engine-dll]]); `oggenc2.exe` went with the 2026-06-19 live-voice recode ([[opus-voice-engine]]).

The offline Wallbreaker reference lives at `C:\Users\tonys\OneDrive\Desktop\Sammy Center` ([[game-vision-wallbreaker]]).
