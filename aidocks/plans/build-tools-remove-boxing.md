---
name: build-tools-remove-boxing
description: "DONE 2026-11-24 (all six sections; awaiting the dev's first real Compile only run) — remove the Enigma Virtual Box stage from build/tools.py (the dev dropped Enigma 2026-11-23 and deleted both .evb files and the gen_cf?_evb.py generators). Six sections, all in tools.py; reviewed, awaiting go-ahead."
metadata:
  type: project
---

**Why:** the dev no longer wants Enigma boxing. `src/client/cfc.evb`, `src/server/cfs.evb`, `scripts/gen_cfc_evb.py`, `scripts/gen_cfs_evb.py` are deleted (committed), but tools.py still references them, so its box step would fail. Effect on shipped builds: client `sounds/` ships as a loose folder and the 5 audio DLLs (bass, bassmix, bass_fx, opus, phonon) stay real in `lib/`; server `docks/` ships loose (already in SERVER_ASSETS), so hosts can edit help/rules. Compile, asset copy, `sanitize_server_bundle`, downcheck, 7z packaging and GitHub release are unchanged. tools.bat and tools.ini need nothing (since 2026-11-24 tools.bat runs `py -3.12 tools.py` through the py launcher, in all six of the dev's projects, so a Python reinstall or move can't break it again).

**Sections (line numbers as of 2026-11-23):**
1. Settings: rewrite comments on CLIENT_ASSETS / SERVER_ASSETS (~31-41); delete ENIGMA (~56-57) and the whole boxing block (~68-83: BOX_PROJECT, CLIENT_EVB, SERVER_EVB, *_EMBEDDED_DLLS, *_EMBEDDED_FOLDERS).
2. compile_downcheck comment (~204-207): drop "and before boxing; boxing only touches cfs.exe".
3. Delete `box_side()` and `box_project()` (~220-276).
4. `run_release` (~516): drop the `skip_box` parameter; delete the Box step (~580-593).
5. Menu: remove "8. Box only"; Package only → 8, Release only → 9, Exit → 10; update every run_release call to 4 flags; invalid-choice text "1-10".
6. CLI: usage text drops skip_box; arg count check 5 → 4 (nothing external passes 5; tools.bat passes none).

**Review notes:** sections 3-5 must land in one edit (positional flags: a 5-flag call into a 4-flag function would SHIFT silently, e.g. Compile only could trigger a release). Optional hardening: keyword arguments in the menu calls. Renumbering changes muscle memory (old 9 = Package, new 9 = Release); dev to confirm. ~/.game_tools/tools.ini may keep an `enigma=` line; leave it (shared with other games).

**Built 2026-11-24:** all six sections in one edit; tools.py went from 732 to 634 lines. Checks: py_compile clean; 0 references to Enigma/box/EVB/EMBEDDED left; no undefined names; every run_release call passes 4 positional flags (Full = SKIP x4; Compile = DO + 3 SILENT; Package = SILENT, DO, SILENT, SILENT; Release = SILENT, SILENT, DO, DO); the CLI refuses the old 5-flag form and a 4x SILENT_SKIP run exits cleanly doing nothing; the menu reads 1-10 (8 Package, 9 Release, 10 Exit). Line endings consistent (CRLF working copy). Not yet exercised: a real compile/package run (dev's job, [[dont-compile-yourself]]).

**Verify:** `python -m py_compile build/tools.py` (syntax only, not a game compile); dev opens the menu (1-10) and runs Compile only after the path plans land: cfc has `sounds/` + all audio DLLs in `lib/`, cfs has `docks/`. Memory follow-up is in [[reorg-docs-and-version]]. See [[launchers-and-running]], [[dont-compile-yourself]].
