---
name: include-tree
description: "CaveDefender's include model (includes.nvgt globs includes/game/* FIRST, then each includes/main/ subfolder) plus the file-by-file map of what lives in each client and server .nvgt. Read to find which file owns a feature."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

`cfc.nvgt` includes only `includes/includes.nvgt`, which (after `#pragma plugin opus` and `version.nvgt`) glob-includes **`game/*` first**, then `main/deps/*`, `main/functions/*`, `main/globals/*`, `main/menus/*`, `main/parsers/*`, then a `typedef` line. The **server** mirrors this: `cfs.nvgt` → `includes/includes.nvgt` → `version.nvgt`, then `game/*`, `main/deps/*`, `main/functions/*`, `main/globals/*` (no menus/parsers on the server). This layout dates from the dev's 2026-11-23 reorg, which moved the gameplay modules out of `main/globals/` into `includes/game/`; the dev chose game-first order. Globbing makes every symbol visible everywhere and picks up new files automatically, but a glob does NOT reach subfolders, so a new folder needs its own line. Include order only matters for the starting values of globals (AngelScript initializes them in read order); every global in `game/` starts from a plain literal, so game-first is safe. `version.nvgt` is mirrored from `build/version.txt` by the launchers and the build (see [[dont-touch-version-txt]]).

**Gameplay modules in `includes/game/`:**
- client: `bot.nvgt` (EVP builder-bot roster: `clientbots`, fed by `botspawn`/`botstep`/`botclear`, so the B key locates them), `burn.nvgt` (firebomb wall-fire audio), `item.nvgt` (ground item sounds, wood vs ammo category), `platform.nvgt` (the native tile store: handle-based `spawn_platform`/`get_tile_at`/`remove_platform`/`clear_map`, see [[game-engine-dll]]), `wall.nvgt` (wall event sounds: strikes, hurt, death, ricochets, shell casings).
- server: `burn.nvgt` (firebomb burn ticks), `enemy.nvgt` (the PVE wall-smasher bots: `enemy_damage`, `enemy_attacks`, redistribute on wall fall), `heal.nvgt` (free-play self-healing walls), `item.nvgt` (ground wood/ammo, reinforce and starter amounts from data files), `wall.nvgt` (server-authoritative walls: health, `damage_wall`/`repair_wall`, `border_wall`).

**Key client files** (under `src/client/includes/main/`):
- `globals/dec.nvgt` — central client state: player identity (`name`, `password`), prefs, sound pools, timers, the `st` savedata. The cached last account is stored inside the same `settings.cvf` as prefs. (Version lives in `includes/version.nvgt`, not here.)
- `globals/net.nvgt` — the connect / login / register flow and the `netloop()` that handles incoming server messages.
- `globals/game.nvgt` — the in-chat loop: movement (reports position via `move`), voice-chat keys, F1–F4 server keys, F5 beacons toggle, escape-to-leave, buffer navigation. Each frame calls `update_sound_pools()` then `beaconloop()`.
- `globals/map.nvgt` — the map (`spawn_map()` via the native tile store in `game/platform.nvgt`), stepping / wall-bounce, and the `me`/`cam` vectors and bounds.
- `globals/effect_space.nvgt` — audio effect zones (cave reverb / through-wall lowpass): `apply_all_effects`/`set_cave_source_fx` on pool mixers, the PVP cross-wall geometry (`pvp_inside_ring`/`pvp_crosswall`), and `apply_voice_fx` (voice bypasses the pools, so effects go on the sound directly, in every mode).
- `globals/weapon.nvgt` — **EVP/PVP attacker**: the local weapon (number row 1-4 = axe/bat/crowbar/hammer) and the held-Space swing (`swingloop`).
- `globals/player.nvgt` — the client-side roster (`players`, the `player` class) of **other** players, for 3D sound; the local player stays `me` + identity globals. Also the beacon system (`beaconloop()`, F5).
- `globals/decpool.nvgt` — the `all_pools` `sound_pool` array (`p`, `beaconpool`, `vpool`, `ambpool`, `musicpool`, `objpool`) + `initialize`/`update`/`pause`/`resume`. `update_sound_pools()` positions the 3D listener at `me` each frame.
- `deps/buffer.nvgt` — the message-buffer system: categories (`alerts`, `global chats`, `connections`, `private chats`, `misc`, `player events`) navigated by comma/period + brackets. Exported logs go under appdata `.../CaveDefender/logs`.
- `deps/` — vendored libs shared with SimpleFighter: `form.nvgt`, `form_menu.nvgt`, `setupmenu.nvgt`, `dlg.nvgt`/`dlgplayer.nvgt`, `sound_pool.nvgt`, `savedata.nvgt`, `speech.nvgt`, `voicechat.nvgt`, `virtual_dialogs.nvgt`, etc. (`GameEngine.nvgt` was deleted 2026-07-14 — see [[game-engine-dll]].) Use `dlgmessage()` for player-facing dialogs (see [[use-dlgmessage]]).
- `menus/menu.nvgt` — `mainmenu()`, the connection menu + account forms, and the preferences menu (`settingsmenu()`). (`dockread()` is a utility in `extrafuncts.nvgt`.)
- `functions/` — `extrafuncts.nvgt` (helpers), `savefuncts.nvgt` (`readpreffs`/`writepreffs`, `save_last_account`/`load_last_account`), `mapfuncts.nvgt` (map/spatial helpers — see [[map-helpers-location]]), `recfuncts.nvgt` (all voice chat: `recordcheck`, `voice_init`, `play_remote_voice`, `voiceloop`).
- `parsers/command_parser.nvgt` — `comparse()`, the in-chat slash-command **router** (not a local executor — see [[command-parser-conventions]] and [[new-command-checklist]]).
- `parsers/menu_parser.nvgt` — `show_server_menu()`, renders a **server-pushed** menu (`showmenu`/`menuresult`/`on_menu_result`).

**Server files** (under `src/server/`; the gameplay modules are listed under `includes/game/` above):
- `cfs.nvgt` — entry, config/MOTD load, ensure-dirs, main loop.
- `globals/net.nvgt` — send/receive, message dispatch, `login`/`register_account`, chat broadcast, the word `filter`, and the staff/moderation commands gated by `rank_level`.
- `globals/player.nvgt` — the **in-memory** connected-player roster (the `player` class: `name`/`peer_id`/`rank`/`version`/`x`/`y`), distinct from the on-disk accounts (renamed from the old `user`/`user.nvgt`).
- `globals/account.nvgt` — the on-disk account store (see [[accounts-system]]).
- `globals/game.nvgt` — the cavern spaces and round lifecycle for **all three modes** (`games[].mode` = `pve`/`evp`/`pvp`): phases (idle → build → wave), wood drops, the host-only shared pause. PVE = defend; EVP = attack (see [[game-mode-evp]]); PVP = humans both sides (see [[game-mode-pvp]]).
- `globals/builder.nvgt` — the EVP builder bots (roam, gather wood, `repair_wall`, `builder_tick`; broadcast `botspawn`/`botstep`/`botclear`).
- `globals/gamedata.nvgt` — the boot-time loader for the weapon/item data files under `data/equipments/` (see [[game-data-file-layout]]).
- `globals/menu.nvgt` — the server-pushed menus (`broadcast_menu`/`send_menu`, `on_menu_result`).
- `functions/filterfuncts.nvgt` — chat filters via NVGT's native `regexp`: `filter_crash()` (the always-on TTS crash-string filter — see [[screen-reader-crash-filter]]), `filter_chat()` (the host word filter in `chatfilter.svr`, also on NVGT's own `regexp`; it no longer needs the old 32-bit BGT filter.dll), `filterchar()` (username/nickname character filter).
