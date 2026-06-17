# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

CaveDefender is an **online**, audio-only game written in **NVGT** (Non-Visual Game Toolkit, an AngelScript-based engine). All code is `.nvgt`. There is no visual rendering — output is screen-reader speech plus HRTF spatial audio through NVGT's `sound_pool`.

It is a **client/server** game. The near-term goal is: connect to the server, log into an account, chat with other players, and walk around a shared map. Map objects (platforms, tiles, zones) are spawned through a custom game-engine DLL. The chat-center milestone is functionally complete: accounts, public/private chat, slash commands, networked player positions with locator beacons, and **spatial voice chat** (push-to-talk clips relayed through the server and played at the speaker's map position).

**Heritage note:** the folder layout and several conventions were borrowed from the **SimpleFighter** project (a separate, *offline* map-builder game), so the structure looks familiar. But CaveDefender is online and very different. Do **not** assume SimpleFighter mechanics exist here — there is no map builder, no `.sif` map format, and no build pipeline. (CaveDefender does have enemy bots and weapons, but they are its own Wallbreaker wave system, not SimpleFighter's NPCs/shields.)

## Layout

The repo root holds two self-contained halves:
- **`client/`** — entry `cfc.nvgt`, plus `includes/`, `lib/`, `sounds/`, `docks/`.
- **`server/`** — entry `cfs.nvgt`, plus `includes/`, `data/`.

Relative paths in code resolve against each side's working directory (client paths against `client/`, server paths against `server/`). Everything under each side moves together, so the relative paths "just work" as long as you run each from its own folder. `CLAUDE.md`, `.gitignore`, etc. sit at the repo root alongside `client/` and `server/`.

## Running

There is **no test suite, no linter, and no build folder** — compiling and packaging are done manually outside this repo, on purpose. For development, run the two scripts with the NVGT runtime:

- **Client:** `client/cfc.nvgt`. `main()` installs the keyhook, gates on `SCREEN_READER_AVAILABLE` / `SOUND_AVAILABLE`, blocks a second instance via `gamstence.is_already_running`, loads the game-engine DLL (`load_engine()`), creates the message buffers, reads prefs, sets up the network client, then loops `mainmenu()`.
- **Server:** `server/cfs.nvgt`. Loads config from `data/preffs/conf.svr` and the MOTD from `data/preffs/motd.svr`, ensures the `data/` folders exist, calls `net.setup_server()`, then loops `netloop()`. **Run it from `server/`** so its relative `data/` paths resolve.

## Client / server split

Two halves of the same game:
- **Client** (`client/`) — presents the UI, plays sounds, manages the local player and the message buffers, and talks to the server.
- **Server** (`server/`) — holds the connected-player roster and the account store, validates logins, broadcasts chat, and runs admin commands.

They are separate codebases that share only a message protocol and an encryption key. Each has its own networking file — both named **`net.nvgt`** (`client/includes/main/globals/net.nvgt` and `server/includes/main/globals/net.nvgt`) — with near-identical `send()` / `get_event_message()` helpers but mirror-image `netloop()`s (the client *reacts to and presents* server messages; the server *dispatches* client requests).

## Networking

Built on NVGT's built-in `network` class (enet). The client uses `setup_client` + `net.connect`; the server uses `setup_server`. Both poll `net.request()` each frame and branch on `event.type` (`event_connect` / `event_disconnect` / `event_receive`).

- **Channels:** 0 = control/system, 1 = public chat, 2 = private messages, 3 = voice. Channels 0–2 carry the space-delimited text protocol; **channel 3 carries raw ogg voice bytes** (the client sends only the audio; the server prepends a `name x y\n` header before relaying to everyone else, and drops anything larger than `maxvoicebytes`). Received clips play through `vpool` at the speaker's position.
- **Encryption:** every packet is run through `string_encrypt` / `string_decrypt` with the key `"rscs123"`, shared by both sides in `send()` / `get_event_message()`.
- **The protocol is the contract.** Both sides agree on a set of **space-delimited** message strings (`login`, `register`, `spawn_player`, `who`, `welcome`, `disconnect`, `ping_request`/`ping_response`, `/getmotd`, `/serveruptime`, `online`/`offline`, `move`/`pos` (player position: client sends `move <x> <y>`, server broadcasts `pos <username> <x> <y> <visible-rank> <afk> <nickname>`, where visible-rank is the flag-filtered rank — the rank only when staff with their flag on, else `player` — afk is 1/0, and nickname is the display name, all for the P player-tracker; the roster is keyed by the **username**), `play`, `terminate`, `/motd`, `/pm`, …). `online`/`offline` carry `<username> <rank> <nickname>` (display uses the nickname, the username keys the roster). Because messages are space-delimited, usernames / passwords / gender values / **nicknames** must contain **no spaces**. **When you change a message on one side, update the matching handler on the other** — a silent client/server mismatch is the classic bug here.

## Accounts

Server-side. Each account is a **folder** at `server/data/players/<username>/` (lowercase) holding one small file per field, so a server host can read or edit a single value by hand: `username.usr`, `nickname.usr` (the display name shown in place of the username **everywhere a name is spoken**; auto-created equal to the username, hand-editable, reverted with `/nick default`), `password.usr` (holds `<salt>:<hash>` — a random plaintext salt joined by a colon to the **SHA-256 hash of salt+password**; the salt is not secret), `gender.usr`, `rank.usr`, `muted.usr`, `banned.usr`, and the saved-room files `pubroom.usr` (`1` = has a public room, blank = none) and `privroom.usr` (the private room's password, blank = none). Saved rooms are **recreated when the host logs in** (and close on disconnect, but the files keep them for next time); a server host can hand-create `pubroom.usr`/`privroom.usr` to pre-make rooms. `muted.usr`/`banned.usr` each use one scheme: **empty = not muted/banned, `0` = indefinite/permanent, any other number = the absolute epoch it expires at** (so the old separate `muted`/`muteuntil` pair is now a single file). Field access goes through `read_field`/`write_field`; `account_exists` checks the folder; `/staff` enumerates accounts via `find_directories("data/players/*")`. `rank` is one of `player`, `moderator`, `administrator`, or `developer` (mutually exclusive, **full words only** — no short forms). `rank_level()` maps them to `0/1/2/3` and **commands are gated by minimum level** (`/promote`/`/demote`/`/mute`/`/unmute` ≥ moderator; `/kick`/`/ban`/`/unban`/`/motd`/`/restart`/`/fastrestart` ≥ administrator). `is_staff` (= level ≥ 1) is for **display only** (chat-name prefix, `/staff` listing, the "you are now…" notice). Both take an explicit target rank: `/promote <name> <rank>` and `/demote <name> <rank>`. You can act on anyone **at or below** your own level (yourself and peers included) but never someone above you, and a **grant cap** means you can never set a rank above your own (the anti-escalation guard). Each also enforces **direction**: `/promote`'s new rank must be *above* the target's current one, `/demote`'s must be *below* it — so the verb always matches and you can't accidentally over-drop someone (e.g. a dev demoting to `administrator` instead of all the way to `player`). Helpers live in `server/includes/main/globals/account.nvgt` (`account_exists`, `create_account`, `load_account`, `read_field`, `write_field`, `verify_password`, `get_rank`, `set_rank`, `rank_level`, `is_staff`, `get_mute_until`, `set_mute`, `clear_mute`, `get_ban_until`, `set_ban`, `clear_ban`, `now_epoch`). `/mute <name> [seconds]` (0/omitted = indefinite) silences a player's chat and voice — staff can mute **players only**, never each other; mutes persist in the account file (surviving reconnects and restarts) and timed ones auto-expire (polled in `netloop`). `/ban <name> [seconds]` (0/omitted = permanent) blocks a player entirely — enforced both in `login()` and by kicking the target off immediately; persists the same way, and timed bans are cleared at the next login attempt (no poll needed, since a banned player is offline). `/ban` is **administrator+** with **at-or-below target protection** (can't ban above your rank; also blocks self-ban). `/kick` is **administrator+** too but can remove **anyone** including a developer (it's only temporary). Both may target staff, unlike mute (players-only). `now_epoch()` returns whole Unix seconds via NVGT's Poco-backed `timestamp` (a default `timestamp` is "now"; its implicit `int64` is microseconds since 1970). Passwords are **never** stored in plaintext. The on-disk rank is loaded into the in-memory `player` roster at spawn; there is no longer a blanket `dev` backdoor (uncompiled builds used to auto-elevate — removed); instead a single configurable **owner** account (`conf.svr` `owner=`, default `tsatria03`) is always forced to `developer`, both on account creation and at login (`is_owner` in account.nvgt), and **cannot be demoted** (the `/demote` handler refuses the owner, so a self-demote can't strip the owner or get reverted confusingly on next login). **Nicknames:** the **username is the identity** (login, folder, all command targeting); the **nickname is the display** shown in its place everywhere a name is spoken (chat, `/who`, `/staff`, the R/L/G lists, the P tracker, lifecycle/AFK notices, connect notices). `get_nickname`/`set_nickname` back `nickname.usr`; the in-memory roster carries `players[].nickname` (loaded at spawn) and ALL the `display_name*` helpers return it instead of `.name`. `/nickname`/`/nick <name>` sets your own (or `default`), `/nick <username> <altname>` lets **any staff** set an online player's (targeted by username, like `/afk`); `apply_nickname` validates (username rules, must be unique among online players' nicknames AND usernames), persists, and **alerts everyone** (flag+AFK-aware old name). **Command targeting:** `get_player_index_from` resolves a typed name to an ONLINE player by **username first, then nickname** (both exact-case), so commands accept either. Player-targeting commands now require the target to be **online** — `/promote`, `/demote`, `/ban`, `/warn`, `/mute`, `/unmute` were converted from offline-capable (`account_exists_exact`) to online-only and operate on `players[ti]` (persisting via `players[ti].name`); `/kick`, `/afk`, `/pm`, `/nick`, `/notifyplayer` already were. The **only** offline-capable holdout is **`/unban`** (a banned player is always offline, so online-only is impossible); it takes the username. Not-found feedback is context-aware: "This player does not exist." vs "This player is not online." `/who` and `/staff` append `(username)` when it differs from the nickname.

- `register <username> <password> <gender>` creates an account; `login <username> <password> <version>` verifies it — and the server **rejects the login if `<version>` doesn't match its own version**, so client and server must be on the same version to connect. Gender is transmitted space-free (`male` / `female` / `nonbinary`) with friendly labels in the UI.
- The client **connection menu** (`menus/menu.nvgt`) offers **sign in** (the last-used account, cached locally inside the encrypted `settings.cvf`), **sign in as** (any account, via a form), and **new account** (a form with username, masked password, and a gender list).

## The custom game engine

Map objects are spawned by a custom engine written in **PureBasic**, shipped as `client/lib/GameEngine64.dll` and wrapped in `includes/main/deps/GameEngine.nvgt` (`load_engine()`, `spawn_platform` / `spawn_zone` / `get_tile_at`, plus FTP/zip/download/recording helpers that are part of the engine's surface and not all used yet). The DLL must be present, or the wrapped calls throw `"library is not loaded"`; `load_engine()` checks the load result and shows a clean alert + exits if it fails.

## Non-stock NVGT engine change

This game depends on a **patched build** of NVGT (the Legacy-NVGT C++ source). `library::load()` in `src/library.cpp` was changed to resolve **any** relative path against the current working directory (not just bare filenames) before loading, so a DLL in a subfolder like `lib/GameEngine64.dll` loads correctly — Windows' `SafeDllSearchMode` otherwise excludes the CWD. This needs a `scons` rebuild of NVGT. With **stock** NVGT the engine won't load from `lib/`; if you must use stock NVGT, keep `GameEngine64.dll` next to `cfc.nvgt` and load it by bare name instead.

## Include tree

`cfc.nvgt` includes only `includes/includes.nvgt`, which pulls in three NVGT stdlib files (`bgt_compat`, `instance`, `token_gen` — resolved from the NVGT install, not the repo, so don't flag them as missing) then glob-includes every directory under `includes/main/`: `deps/`, `functions/`, `globals/`, `menus/`, `parsers/`. Globbing means every symbol is visible everywhere, and renamed files are picked up automatically (no explicit include to update). The **server** now mirrors this exactly: `cfs.nvgt` includes `includes/includes.nvgt`, which glob-includes `main/deps/*`, `main/functions/*`, `main/globals/*` (with `menus/` and `parsers/` stubbed out for later).

Key client files (under `client/includes/main/`):
- `globals/dec.nvgt` — central client state: player identity (`name`, `password`, `gender`), prefs, sound pools, timers, and the `st` savedata. The cached last account (name/password/gender) is stored inside the same `settings.cvf` as prefs, not a separate file. The version string lives here too.
- `globals/net.nvgt` — the connect / login / register flow and the `netloop()` that handles incoming server messages.
- `globals/game.nvgt` — the in-chat loop: movement (which also reports position to the server via `move`), voice-chat keys, F1–F4 server keys, F5 to toggle player beacons, the escape-to-leave handler, buffer navigation. Each frame it calls `update_sound_pools()` then `beaconloop()`.
- `globals/map.nvgt` — the map (`spawn_map()` via the engine), stepping / wall-bounce, and the `me` / `cam` vectors and bounds.
- `globals/player.nvgt` — the client-side roster (`players`, an array of the `player` class: `name`, `x`, `y`, a `beacontimer` and `beaconsound` handle) of **other** players the server reports, for placing their sounds in 3D. The local player stays `me` + identity globals. `netloop()` keeps it current via `add_player` / `set_player_position` / `remove_player` (keyed by `get_player_index`), skipping your own name. Also holds the beacon system: `beaconloop()` pulses `beacon.ogg` at each player's spot every `beacontime` (500 ms) on the `beaconpool`, pitch jittered 80–120, gated by `beacons_enabled` (F5).
- `globals/decpool.nvgt` — the `all_pools` `sound_pool` array (`p`, `beaconpool`, `vpool`, `ambpool`, `musicpool`, `objpool`) and `initialize` / `update` / `pause` / `resume` helpers. `update_sound_pools()` positions the 3D listener at `me` and is now called every frame from `game()`'s loop (needed for the beacons to pan).
- `deps/buffer.nvgt` — the message-buffer system: categories (`alerts`, `global chats`, `connections`, `private chats`, `misc`, `player events`) the player navigates (comma/period to move within a buffer, brackets to switch buffers) to review messages by type. Exported logs go under appdata `.../CaveDefender/logs`.
- `deps/` — vendored libraries shared with SimpleFighter: `form.nvgt` (audio form), `form_menu.nvgt`, `setupmenu.nvgt`, `dlg.nvgt` / `dlgplayer.nvgt`, `sound_pool.nvgt`, `savedata.nvgt`, `speech.nvgt`, `voicechat.nvgt`, `GameEngine.nvgt`, etc. **Use `dlgmessage()` for player-facing dialogs** (the nicer wrapper), not raw `dlg()`.
- `menus/menu.nvgt` — `mainmenu()`, the connection menu + account forms, and the preferences menu (`settingsmenu()`). (The in-game documentation menu was removed; `dockread()` remains a utility in `extrafuncts.nvgt`.)
- `functions/` — `extrafuncts.nvgt` (helper library), `savefuncts.nvgt` (`readpreffs` / `writepreffs`, `save_last_account` / `load_last_account`), `mapfuncts.nvgt` (map/spatial helpers: `gmt`, `facing_name`, `facing_degrees`, `track_players`), and `recfuncts.nvgt` (all voice chat: `recordcheck` handles the O key like `buffercheck` handles the buffer keys, plus `prep_recording` / `prep_playback` / `transmit_voice` / `play_remote_voice` — own voice plays centered through `vpool`, others in 3D).
- `parsers/command_parser.nvgt` — `comparse()`, the in-chat slash-command **router** (called from `game.nvgt` on `/`). Because the game is online it does not execute commands locally (unlike SimpleFighter's `comparse()`) — it sends chat on channel 1 and forwards each recognized command on the channel the server expects. **Rule for new commands:** validate the argument count and call `syntax_error("usage")` on bad syntax (the "Invalid command syntax. Usage: …" style); route all command feedback to the `misc` buffer via `add_buffer_item`. See memory.
- `parsers/menu_parser.nvgt` — `show_server_menu()`, which renders a **server-pushed** menu. Server-initiated, client-rendered: the server (`server/.../globals/menu.nvgt`, `broadcast_menu()`) broadcasts `showmenu <id>\n<title>\n<option>…` on channel 0; the client builds it with `setupmenu`/`m`, runs it (modal), and replies `menuresult <id> <choice>` (0-based option index, -1 = cancelled), which the server hands to `on_menu_result()` (a hook feature code fills in). The server draws no player UI — it only describes the menu; only in-game clients receive it.

Server files (under `server/`, same `includes/main/{deps,functions,globals}` glob layout as the client):
- `cfs.nvgt` — entry, config/MOTD load, ensure-dirs, main loop.
- `includes/main/globals/net.nvgt` — send/receive, message dispatch, `login` / `register_account`, chat broadcast, the word `filter`, and the staff/moderation commands gated by `rank_level` (`/kick`, `/ban`, `/unban`, `/motd`, `/restart`, `/fastrestart`, `/promote`, `/demote`, `/mute`, `/unmute`, `/notify`, `/notifyplayer`; plus the public `/pm`, `/who`, `/staff`, `/help`).
- `includes/main/globals/player.nvgt` — the **in-memory** connected-player roster (the `player` class: `name` / `peer_id` / `rank` / `version` / `x` / `y`, plus `spawn_player` / `get_player_index`), distinct from the on-disk accounts. `rank` is set from the account file at spawn. Renamed from the old `user` / `user.nvgt`.
- `includes/main/globals/account.nvgt` — the on-disk account store.
- `includes/main/globals/game.nvgt` — the game (cavern) spaces and round lifecycle: phases (idle → build → wave), wood drops, bot spawning, the all-walls-down loss + reset (`end_round_loss`), and the **host-only shared pause** (`pause_game`/`resume_game`; `gametick` skips paused games, Open games auto-resume after 90s).
- `includes/main/globals/enemy.nvgt` — the wall-smasher bots: one weapon each (1 axe / 4 bat / 2 crowbar / 3 hammer, each its own attack speed and damage), spawned onto the least-attacked standing wall, swinging in `enemy_attacks`, and redistributing when a wall falls.
- `includes/main/globals/wall.nvgt` and `globals/item.nvgt` — server-authoritative walls (health, `damage_wall`/`repair_wall`, `border_wall`; cavern walls start at a random 20–80%) and ground wood (spawn/pickup, size-scaled cap).
- `includes/main/globals/menu.nvgt` — the server-pushed menus (`broadcast_menu`/`send_menu`, `on_menu_result`), including the host pause menu and the in-game leave menu.
- `includes/main/functions/regex.nvgt` — the chat word filter, using NVGT's **native `regexp`** (the old third-party `filter.dll` is gone — see memory).

## Version

The version string lives in **two** places that must stay in sync: `client/includes/main/globals/dec.nvgt` (client) and `server/includes/main/globals/dec.nvgt` (server). Bump **both** together when opening a new changelog version block.

## Audio

NVGT `sound_pool` with HRTF. Player position is the vector `me`; pools advance per frame. `client/sounds/` is organized by category, with a **per-type subfolder** holding named clips:
- `ui/` — `buffer/`, `dlg/`, `menu/`, `misc/` (online, offline, playerchat, privchat, von, voff, pingstart, pingstop, welcome, newmotd, kick, ban, promote/demote, notify1-3, buildstart, wavestart, gameover, pause, resume, etc.).
- `objects/walls/<wall>/` — e.g. `wallwood/{bump,death,hurt1-3}.ogg`; also `wallbuilding/bump.ogg` (lobby) and `wallgeneric/bump.ogg` (office room).
- `objects/platforms/<tile>/` — e.g. `cave/step1-5.ogg`; also `carpet` (lobby) and `marble` (office room).
- `objects/items/<item>/` — e.g. `wood` (`drop`/`loop`/`place`/`take`).
- `weapons/<weapon>/` — `axe`, `bat`, `crowbar`, `hammer` (`draw`/`fire1-3`/`hit1-3`); the enemy bots play the `hit` clips when they strike a wall.

This game does **not** support swappable sound packs (see memory) — paths point directly at the fixed subfolders. `map.nvgt` builds the per-type subfolder paths (`objects/walls/<wall>/bump.ogg`, `objects/platforms/<tile>/step<n>.ogg`); `spawn_map()` lays a `wallwood` border around a `cave` interior, with `me` starting at `(1,1)` on the interior.

## Player-facing docs (docks/)

`docks/` lives under **`client/`**: `changelog.txt`, `credits.txt`, `readme.txt`, `todo list.txt`. There is no longer an in-game documentation viewer (the menu was removed), but **`changelog.txt` is still the source of truth for what shipped** and is maintained on every release.

There is **also a server-side `server/docks/`** (`player help.txt`, `staff help.txt`), bundled into the server via `#pragma document docks`. Help is **server-authoritative**: `/help player` / `/help staff` (client) → server reads `docks/<which> help.txt` and sends `helptext <which>\n<content>` → the client shows it with `dockread(title, text)` (the text overload added so received content needs no temp file). Keep these two files updated when commands change, since they document every command and its rank.

## Rules kept in memory (not inline, to keep this file lean)

Detailed conventions live in memory files — follow them:
- **confirm-before-implementing** — treat a design discussion or a question (anything ending in `?`, "what if", "I wish") as a request for a plan, **not** a green light to edit. Wait for explicit go-ahead.
- **list-modified-files** — end every turn that edited files with a bare-filename "Files changed:" list.
- **no-crlf-normalization** — don't run post-edit CRLF passes; author new file content with CRLF and let git handle it.
- **changelog-rules** — player-facing prose, sentence/entry caps, reverse-chronological, the two-file version bump above.
- **no-sound-pack-support** — don't add sound-pack machinery.
- **path-conventions** — the full path map (appdata, sounds, server data, the DLL).

`New File.txt` in the repo root is the dev's personal scratch pad — don't read it as documentation or write to it.
