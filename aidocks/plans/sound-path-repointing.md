---
name: sound-path-repointing
description: "OPEN — repoint all client sound paths (and the server's footstep wire strings) to the reorganized cf/client/sounds/main + sounds/game layout. Until done the client is mostly silent. Waiting on the dev's approach choice: rewrite paths in place (recommended) vs shared folder-name constants."
metadata:
  type: project
---

**The move (dev, 2026-11-23, committed "Major sound enhancements."):** all 270 files kept, mapping:
- `ui/misc/` → `main/misc/`; `ui/dlg/` → `main/ui/dialog/`; `ui/buffer|keyboard|menu/` → `main/ui/buffer|keyboard|menu/`
- `equipment/` → `game/equipments/`; `objects/walls|platforms/` → `game/objects/walls|platforms/`
- `ambience/` → `game/objects/ambience/`; `music/` → `game/objects/music/`
- `main/ui/menu/speaker.ogg` was deliberately REPLACED with a new sound (dev confirmed).
The server's own `cf/server/sounds/` (soundboard clips) did NOT move; its 4 "sounds/" refs stay.

**Stage 3 — full literal paths.** ~136 `"sounds/..."` strings in 18 client files (net.nvgt 74, form.nvgt 12, wall.nvgt 10, weapon.nvgt 8, game.nvgt 8, buffer.nvgt 7, setupmenu.nvgt 7, dlg.nvgt 6, recfuncts.nvgt 6, plus menu, map, player, music, item, command_parser, burn, bullet, ambience). Prefix builders: `ambience.nvgt` line 16 `"sounds/ambience/"`, `music.nvgt` line 16 `"sounds/music/"`; also map.nvgt comments lines 51-59. Verify with a scratchpad checker that extracts every literal path and confirms the file exists.

**Stage 4 — pieced paths + wire protocol (client AND server together).** Paths without the "sounds/" prefix (the prefix is added later, so a "sounds/" grep misses them):
- client local: wall.nvgt 102 (`equipment/weapons/`), weapon.nvgt 190, recfuncts.nvgt 218 (`ui/misc/von|voff`) and 228 (`ui/keyboard/`), map.nvgt 121 (`objects/walls/`) and 130 (`objects/platforms/`)
- Learn Sounds menu, menu.nvgt ~266-366 (~25 folder/file strings)
- client sends: weapon.nvgt 86, 146, 212, 275 (`step equipment/weapons/...`), map.nvgt 162 (`step ui/misc/turn`)
- client sorts incoming: net.nvgt 1357/1359 substring checks `equipment/items/ammo/` / `equipment/items/` must become `equipments/...` (else ammo/wood play through the wrong pool, not silence)
- server sends: builder.nvgt 231, net.nvgt 1191 and 1233 (`footstep equipment/items/...`); the server's step relay (net.nvgt ~1826) passes paths verbatim, no change
**Wire change** → a 5.2 client would hear silence from a new server, so this ships as 5.3 (the login version check then refuses mismatches). See [[networking-protocol]].

**Approach (OPEN QUESTION to the dev):** (A, recommended) rewrite strings in place, smallest and easiest to verify; (B) introduce shared folder constants (e.g. SND_UI, SND_EQUIP) so a future reorg is one-line changes, but a bigger refactor over the same ~180 lines.

**Verify after:** 0 old-folder strings in any .nvgt on either side; in game: Learn Sounds plays every category, pick up wood and ammo, draw/fire each weapon, walls, footsteps, ambience, music, dialogs and typing sounds.

Noted side issue (out of scope): the server relays any client-supplied step path verbatim, so a modified client could make others try to play arbitrary local paths. Low risk. Line numbers checked 2026-11-23/24; re-locate by text. Related: [[audio-and-sounds]], [[data-repointing]].
