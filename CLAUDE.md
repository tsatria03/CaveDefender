# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

CaveDefender is an **online**, audio-only game written in **NVGT** (Non-Visual Game Toolkit, an AngelScript-based engine). All code is `.nvgt`. There is no visual rendering — output is screen-reader speech plus HRTF spatial audio through NVGT's `sound_pool`.

It is a **client/server** game. The near-term goal is: connect to the server, log into an account, chat with other players, and walk around a shared map. Map objects (platforms, tiles, zones) are spawned through a custom game-engine DLL. Networked voice chat is planned but incomplete — voice currently records and plays back **locally only**, with no transmission to the server.

**Heritage note:** the folder layout and several conventions were borrowed from the **SimpleFighter** project (a separate, *offline* map-builder game), so the structure looks familiar. But CaveDefender is online and very different. Do **not** assume SimpleFighter mechanics exist here — there is no map builder, no `.sif` map format, no NPCs/weapons/shields, and no build pipeline.

## Running

There is **no test suite, no linter, and no build folder** — compiling and packaging are done manually outside this repo, on purpose. For development, run the two scripts with the NVGT runtime:

- **Client:** `cf.nvgt` — entry point. `main()` installs the keyhook, gates on `SCREEN_READER_AVAILABLE` / `SOUND_AVAILABLE`, blocks a second instance via `gamstence.is_already_running`, loads the game-engine DLL (`load_engine()`), creates the message buffers, reads prefs, sets up the network client, then loops `mainmenu()`.
- **Server:** `server/server.nvgt` — loads config from `data/preffs/conf.svr` and the MOTD from `data/preffs/motd.svr`, ensures the `data/` folders exist, calls `net.setup_server()`, then loops `netloop()`. **Run it from the `server/` folder** so its relative `data/` paths resolve.

## Client / server split

Two halves of the same game:
- **Client** — `cf.nvgt` plus everything under `includes/`. Presents the UI, plays sounds, manages the local player and the message buffers, and talks to the server.
- **Server** — everything under `server/`. Holds the connected-user roster and the account store, validates logins, broadcasts chat, and runs admin commands.

They are separate codebases that share only a message protocol and an encryption key. Each has its own networking file — `includes/main/globals/client_net.nvgt` and `server/includes/server_net.nvgt` — with near-identical `send()` / `get_event_message()` helpers but mirror-image `netloop()`s (the client *reacts to and presents* server messages; the server *dispatches* client requests).

## Networking

Built on NVGT's built-in `network` class (enet). The client uses `setup_client` + `net.connect`; the server uses `setup_server`. Both poll `net.request()` each frame and branch on `event.type` (`event_connect` / `event_disconnect` / `event_receive`).

- **Channels:** 0 = control/system, 1 = public chat, 2 = private messages.
- **Encryption:** every packet is run through `string_encrypt` / `string_decrypt` with the key `"rscs123"`, shared by both sides in `send()` / `get_event_message()`.
- **The protocol is the contract.** Both sides agree on a set of **space-delimited** message strings (`login`, `register`, `spawn_user`, `who`, `welcome`, `disconnect`, `ping_request`/`ping_response`, `/getmotd`, `/serveruptime`, `online`/`offline`, `play`, `terminate`, `kill`, `/motd`, `/pm`, …). Because messages are space-delimited, usernames / passwords / gender values must contain **no spaces**. **When you change a message on one side, update the matching handler on the other** — a silent client/server mismatch is the classic bug here.

## Accounts

Server-side. Each account is a key=value file at `server/data/players/<username>.svr`: `name`, `salt`, the **SHA-256 hash of salt+password**, `gender`, `admin`. Helpers live in `server/includes/account.nvgt` (`account_exists`, `create_account`, `load_account`, `verify_password`). Passwords are **never** stored in plaintext.

- `register <username> <password> <gender>` creates an account; `login <username> <password> <version>` verifies it. Gender is transmitted space-free (`male` / `female` / `nonbinary`) with friendly labels in the UI.
- The client **connection menu** (`includes/main/menus/menu.nvgt`) offers **sign in** (the last-used account, cached locally and encrypted in `account.cvf`), **sign in as** (any account, via a form), and **new account** (a form with username, masked password, and a gender list).

## The custom game engine

Map objects are spawned by a custom engine written in **PureBasic**, shipped as `lib/GameEngine64.dll` and wrapped in `includes/main/deps/GameEngine.nvgt` (`load_engine()`, `spawn_platform` / `spawn_zone` / `get_tile_at`, plus FTP/zip/download/recording helpers that are part of the engine's surface and not all used yet). The DLL must be present, or the wrapped calls throw `"library is not loaded"`; `load_engine()` checks the load result and shows a clean alert + exits if it fails.

## Non-stock NVGT engine change

This game depends on a **patched build** of NVGT (the Legacy-NVGT C++ source). `library::load()` in `src/library.cpp` was changed to resolve **any** relative path against the current working directory (not just bare filenames) before loading, so a DLL in a subfolder like `lib/GameEngine64.dll` loads correctly — Windows' `SafeDllSearchMode` otherwise excludes the CWD. This needs a `scons` rebuild of NVGT. With **stock** NVGT the engine won't load from `lib/`; if you must use stock NVGT, keep `GameEngine64.dll` in the project root and load it by bare name instead.

## Include tree

`cf.nvgt` includes only `includes/includes.nvgt`, which pulls in three NVGT stdlib files (`bgt_compat`, `instance`, `token_gen` — resolved from the NVGT install, not the repo, so don't flag them as missing) then glob-includes every directory under `includes/main/`: `deps/`, `functions/`, `globals/`, `menus/`, `parsers/`. Globbing means every symbol is visible everywhere.

Key client files:
- `globals/dec.nvgt` — central client state: player identity (`name`, `password`, `gender`), prefs, sound pools, timers, and the savedata stores (`st` for prefs, `accountdata` for the cached last account). The version string lives here too.
- `globals/client_net.nvgt` — the connect / login / register flow and the `netloop()` that handles incoming server messages.
- `globals/game.nvgt` — the in-chat loop: movement, voice-chat keys, F1–F4 server keys, buffer navigation.
- `globals/map.nvgt` — the map (`spawn_map()` via the engine), stepping / wall-bounce, and the `me` / `cam` vectors and bounds.
- `globals/decpool.nvgt` — the `sound_pool` array and `initialize` / `update` / `pause` / `resume` helpers. Note `update_sound_pools()` (positions the 3D listener) exists but is **not yet wired into the game loop** — a known gap, not dead code.
- `deps/buffer.nvgt` — the message-buffer system: categories (`alerts`, `chats`, `connections`, `pm's`, `misc`, `player events`) the player navigates (comma/period to move within a buffer, brackets to switch buffers) to review messages by type. Exported logs go under appdata `.../CaveDefender/logs`.
- `deps/` — vendored libraries shared with SimpleFighter: `form.nvgt` (audio form), `form_menu.nvgt`, `setupmenu.nvgt`, `dlg.nvgt` / `dlgplayer.nvgt`, `sound_pool.nvgt`, `savedata.nvgt`, `speech.nvgt`, `voicechat.nvgt`, `GameEngine.nvgt`, etc. **Use `dlgmessage()` for player-facing dialogs** (the nicer wrapper), not raw `dlg()`.
- `menus/menu.nvgt` — `mainmenu()`, the connection menu + account forms, and `docksmenu()`.
- `functions/` — `extrafuncts.nvgt` (helper library; `dockread()` lives here) and `savefuncts.nvgt` (`readpreffs` / `writepreffs`, `save_last_account` / `load_last_account`).

Server files (under `server/`):
- `server.nvgt` — entry, config/MOTD load, ensure-dirs, main loop.
- `includes/server_net.nvgt` — send/receive, message dispatch, `login` / `register_account`, chat broadcast, the word `filter`, admin commands (`/exit`, `/motd`, `/pm`).
- `includes/user.nvgt` — the **in-memory** connected-user roster (distinct from the on-disk accounts).
- `includes/account.nvgt` — the on-disk account store.
- `includes/regex.nvgt` — the chat word filter, using NVGT's **native `regexp`** (the old third-party `filter.dll` is gone — see memory).

## Version

The version string lives in **two** places that must stay in sync: `includes/main/globals/dec.nvgt` (client) and `server/server.nvgt` (server). Bump **both** together when opening a new changelog version block.

## Audio

NVGT `sound_pool` with HRTF. Player position is the vector `me`; pools advance per frame. `sounds/` is organized into categorized subfolders: `ui/` (`buffer`, `dlg`, `menu`, `misc`), `objects/` (`walls`, `platforms`), `player/`, `ambience/`, `music/`. Several `objects` / `ambience` / `music` / `player` folders are intentionally **empty**, to be filled later. This game does **not** support swappable sound packs (see memory) — paths point directly at the fixed `sounds/` subfolders.

## Player-facing docs (docks/)

Flat folder: `changelog.txt`, `credits.txt`, `readme.txt`, `todo list.txt`. Opened by `dockread()` / `docksmenu()` (note `dockread` strips the `docks/` prefix for the window title). `changelog.txt` is the source of truth for what shipped.

## Rules kept in memory (not inline, to keep this file lean)

Detailed conventions live in memory files — follow them:
- **confirm-before-implementing** — treat a design discussion or a question (anything ending in `?`, "what if", "I wish") as a request for a plan, **not** a green light to edit. Wait for explicit go-ahead.
- **list-modified-files** — end every turn that edited files with a bare-filename "Files changed:" list.
- **no-crlf-normalization** — don't run post-edit CRLF passes; author new file content with CRLF and let git handle it.
- **changelog-rules** — player-facing prose, sentence/entry caps, reverse-chronological, the two-file version bump above.
- **no-sound-pack-support** — don't add sound-pack machinery.

`New File.txt` in the repo root is the dev's personal scratch pad — don't read it as documentation or write to it.
