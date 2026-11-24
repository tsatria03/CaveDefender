---
name: sound-path-repointing
description: "DONE IN CODE 2026-11-24 (awaiting the dev's in-game test and the 5.3 release) — repoint all client sound paths (and the server's footstep wire strings) to the reorganized cf/client/sounds/main + sounds/game layout. Until done the client is mostly silent. Approach decided 2026-11-24: rewrite paths in place."
metadata:
  type: project
---

**The move (dev, 2026-11-23, committed "Major sound enhancements."):** all 270 files kept, mapping:
- `ui/misc/` → `main/misc/`; `ui/dlg/` → `main/ui/dialog/`; `ui/buffer|keyboard|menu/` → `main/ui/buffer|keyboard|menu/`
- `equipment/` → `game/equipments/`; `objects/walls|platforms/` → `game/objects/walls|platforms/`
- `ambience/` → `game/objects/ambience/`; `music/` → `game/objects/music/`
- `main/ui/menu/speaker.ogg` was deliberately REPLACED with a new sound (dev confirmed).
- **Second objects split (dev, 2026-11-24):** `game/objects/ambience|music/` → `game/objects/audio/ambience|music/`; `game/objects/platforms|walls/` → `game/objects/construction/platforms|walls/` (45 files, contents unchanged). Repointed the same day: 15 code strings in 7 files + 9 comments; checker clean again.
The server's own `cf/server/sounds/` (soundboard clips) did NOT move; its 4 "sounds/" refs stay.

**Stage 3 — full literal paths.** ~136 `"sounds/..."` strings in 18 client files (net.nvgt 74, form.nvgt 12, wall.nvgt 10, weapon.nvgt 8, game.nvgt 8, buffer.nvgt 7, setupmenu.nvgt 7, dlg.nvgt 6, recfuncts.nvgt 6, plus menu, map, player, music, item, command_parser, burn, bullet, ambience). Prefix builders: `ambience.nvgt` line 16 `"sounds/ambience/"`, `music.nvgt` line 16 `"sounds/music/"`; also map.nvgt comments lines 51-59. Verify with a scratchpad checker that extracts every literal path and confirms the file exists.

**Stage 4 — pieced paths + wire protocol (client AND server together).** Paths without the "sounds/" prefix (the prefix is added later, so a "sounds/" grep misses them):
- client local: wall.nvgt 102 (`equipment/weapons/`), weapon.nvgt 190, recfuncts.nvgt 218 (`ui/misc/von|voff`) and 228 (`ui/keyboard/`), map.nvgt 121 (`objects/walls/`) and 130 (`objects/platforms/`)
- Learn Sounds menu, menu.nvgt ~266-366 (~25 folder/file strings)
- client sends: weapon.nvgt 86, 146, 212, 275 (`step equipment/weapons/...`), map.nvgt 162 (`step ui/misc/turn`)
- client sorts incoming: net.nvgt 1357/1359 substring checks `equipment/items/ammo/` / `equipment/items/` must become `equipments/...` (else ammo/wood play through the wrong pool, not silence)
- server sends: builder.nvgt 231, net.nvgt 1191 and 1233 (`footstep equipment/items/...`); the server's step relay (net.nvgt ~1826) passes paths verbatim, no change
**Wire change** → a 5.2 client would hear silence from a new server, so this ships as 5.3 (the login version check then refuses mismatches). See [[networking-protocol]].

**Approach — DECIDED 2026-11-24: (A) rewrite in place.** Every old path string is changed directly to its new location; no shared folder constants. Dev: "I'd say rewrite in place. I've done this reorg before, but on a much smaller scale." Rejected (B): shared folder constants (e.g. SND_UI, SND_EQUIP), which would make a future reorg one-line changes but reshape ~180 lines and hide the full path a screen-reader reviewer reads on each line.

**Progress (2026-11-24): CLIENT SIDE DONE.** Stage 3 plus every client part of stage 4 (local pieced paths, Learn Sounds, the step strings the client sends, net.nvgt's incoming equipments/items checks) — 173 strings across 18 files rewritten by a scratchpad script that only touched quoted sound strings (line endings verified unchanged), plus 12 stale comments by hand in 8 files. Checker: every client sound path resolves except sounds/main/misc/gameover.ogg (3 uses) and roundcleared.ogg (1), which never existed in git: they are sound placeholders ([[sound-placeholders]]) for the dev to add. 0 old folder names left anywhere in src/client. **SERVER SIDE DONE (2026-11-24) — PLAN COMPLETE in code:** the three footstep strings (builder.nvgt 231, net.nvgt 1191/1233) now send `footstep game/equipments/items/...`, matching the client's incoming checks; all 9 wood/ammo take.ogg files exist. A search of both src trees finds 0 old sound folder names. Remaining for release: the 5.3 bump + changelog in [[reorg-docs-and-version]], and the dev's in-game test (Verify after, below).

**Verify after:** 0 old-folder strings in any .nvgt on either side; in game: Learn Sounds plays every category, pick up wood and ammo, draw/fire each weapon, walls, footsteps, ambience, music, dialogs and typing sounds.

Noted side issue (out of scope): the server relays any client-supplied step path verbatim, so a modified client could make others try to play arbitrary local paths. Low risk. Line numbers checked 2026-11-23/24; re-locate by text. Related: [[audio-and-sounds]], [[data-repointing]].
