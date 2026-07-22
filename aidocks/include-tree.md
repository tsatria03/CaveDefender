---
name: include-tree
description: "CaveDefender's include model (cfc.nvgt/cfs.nvgt glob-include everything under includes/main/) plus the file-by-file map of what lives in each client and server .nvgt. Read to find which file owns a feature."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

`cfc.nvgt` includes only `includes/includes.nvgt`, which pulls in three NVGT stdlib files (`bgt_compat`, `instance`, `token_gen` — resolved from the NVGT install, not the repo, so don't flag them as missing) then glob-includes every directory under `includes/main/`: `deps/`, `functions/`, `globals/`, `menus/`, `parsers/`. Globbing means every symbol is visible everywhere, and renamed files are picked up automatically (no explicit include to update). The **server** mirrors this: `cfs.nvgt` includes `includes/includes.nvgt`, which glob-includes `main/deps/*`, `main/functions/*`, `main/globals/*` (with `menus/` and `parsers/` stubbed for later). Each side's `includes.nvgt` also includes `version.nvgt` before the globs (see the version note in [[changelog-rules]]).

**Key client files** (under `src/client/includes/main/`):
- `globals/dec.nvgt` — central client state: player identity (`name`, `password`), prefs, sound pools, timers, the `st` savedata. The cached last account is stored inside the same `settings.cvf` as prefs. (Version lives in `includes/version.nvgt`, not here.)
- `globals/net.nvgt` — the connect / login / register flow and the `netloop()` that handles incoming server messages.
- `globals/game.nvgt` — the in-chat loop: movement (reports position via `move`), voice-chat keys, F1–F4 server keys, F5 beacons toggle, escape-to-leave, buffer navigation. Each frame calls `update_sound_pools()` then `beaconloop()`.
- `globals/map.nvgt` — the map (`spawn_map()` via the engine), stepping / wall-bounce, and the `me`/`cam` vectors and bounds.
- `globals/effect_space.nvgt` — audio effect zones (cave reverb / through-wall lowpass): `apply_all_effects`/`set_cave_source_fx` on pool mixers, the PVP cross-wall geometry (`pvp_inside_ring`/`pvp_crosswall`), and `apply_voice_fx` (voice bypasses the pools, so effects go on the sound directly, in every mode).
- `globals/weapon.nvgt` — **EVP/PVP attacker**: the local weapon (number row 1-4 = axe/bat/crowbar/hammer) and the held-Space swing (`swingloop`).
- `globals/bot.nvgt` — **EVP only**: client roster of builder bots (`clientbots`, fed by `botspawn`/`botstep`/`botclear`) so the B key locates them.
- `globals/player.nvgt` — the client-side roster (`players`, the `player` class) of **other** players, for 3D sound; the local player stays `me` + identity globals. Also the beacon system (`beaconloop()`, F5).
- `globals/decpool.nvgt` — the `all_pools` `sound_pool` array (`p`, `beaconpool`, `vpool`, `ambpool`, `musicpool`, `objpool`) + `initialize`/`update`/`pause`/`resume`. `update_sound_pools()` positions the 3D listener at `me` each frame.
- `deps/buffer.nvgt` — the message-buffer system: categories (`alerts`, `global chats`, `connections`, `private chats`, `misc`, `player events`) navigated by comma/period + brackets. Exported logs go under appdata `.../CaveDefender/logs`.
- `deps/` — vendored libs shared with SimpleFighter: `form.nvgt`, `form_menu.nvgt`, `setupmenu.nvgt`, `dlg.nvgt`/`dlgplayer.nvgt`, `sound_pool.nvgt`, `savedata.nvgt`, `speech.nvgt`, `voicechat.nvgt`, `GameEngine.nvgt`, `virtual_dialogs.nvgt`, etc. Use `dlgmessage()` for player-facing dialogs (see [[use-dlgmessage]]).
- `menus/menu.nvgt` — `mainmenu()`, the connection menu + account forms, and the preferences menu (`settingsmenu()`). (`dockread()` is a utility in `extrafuncts.nvgt`.)
- `functions/` — `extrafuncts.nvgt` (helpers), `savefuncts.nvgt` (`readpreffs`/`writepreffs`, `save_last_account`/`load_last_account`), `mapfuncts.nvgt` (map/spatial helpers — see [[map-helpers-location]]), `recfuncts.nvgt` (all voice chat: `recordcheck`, `voice_init`, `play_remote_voice`, `voiceloop`).
- `parsers/command_parser.nvgt` — `comparse()`, the in-chat slash-command **router** (not a local executor — see [[command-parser-conventions]] and [[new-command-checklist]]).
- `parsers/menu_parser.nvgt` — `show_server_menu()`, renders a **server-pushed** menu (`showmenu`/`menuresult`/`on_menu_result`).

**Server files** (under `src/server/`, same `includes/main/{deps,functions,globals}` glob layout):
- `cfs.nvgt` — entry, config/MOTD load, ensure-dirs, main loop.
- `globals/net.nvgt` — send/receive, message dispatch, `login`/`register_account`, chat broadcast, the word `filter`, and the staff/moderation commands gated by `rank_level`.
- `globals/player.nvgt` — the **in-memory** connected-player roster (the `player` class: `name`/`peer_id`/`rank`/`version`/`x`/`y`), distinct from the on-disk accounts (renamed from the old `user`/`user.nvgt`).
- `globals/account.nvgt` — the on-disk account store (see [[accounts-system]]).
- `globals/game.nvgt` — the cavern spaces and round lifecycle for **all three modes** (`games[].mode` = `pve`/`evp`/`pvp`): phases (idle → build → wave), wood drops, the host-only shared pause. PVE = defend; EVP = attack (see [[game-mode-evp]]); PVP = humans both sides (see [[game-mode-pvp]]).
- `globals/enemy.nvgt` — the PVE wall-smasher bots (`enemy_damage`, `enemy_attacks`, redistribute on wall fall).
- `globals/builder.nvgt` — the EVP builder bots (roam, gather wood, `repair_wall`, `builder_tick`; broadcast `botspawn`/`botstep`/`botclear`).
- `globals/wall.nvgt` + `globals/item.nvgt` — server-authoritative walls (health, `damage_wall`/`repair_wall`, `border_wall`) and ground wood.
- `globals/menu.nvgt` — the server-pushed menus (`broadcast_menu`/`send_menu`, `on_menu_result`).
- `functions/filterfuncts.nvgt` — chat filters via NVGT's native `regexp`: `filter_crash()` (the always-on TTS crash-string filter — see [[screen-reader-crash-filter]]), `filter_chat()` (the host word filter in `chatfilter.svr` — see [[regex-filter-dll-removed]]), `filterchar()` (username/nickname character filter).
