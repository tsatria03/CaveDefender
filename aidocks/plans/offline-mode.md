---
name: offline-mode
description: "PLANNED (2026-11-25) — the full offline game: a game menu option that plays with no sign-in, no server program and no networking, by running the unchanged server code as a second script module inside the client (Option A, proven by [[offline-module-poc]]). Both sides swap their network object for a same-named wrapper; online play is untouched. 8 sections; design questions open."
metadata:
  type: project
---

**Goal (dev, 2026-11-25):** "a mode where you do not need to sign in at all, and all of the networking that goes into it can be disabled", like StrideRush, without a second copy of the game rules ("that would mean basically creating a clone of the game"). The server program stays exactly as it is for local-online testing and the VPS. Players get only the client; no cfs.exe, no hosting.

**Approach:** the client loads the server's own code as a second script module ([[offline-module-poc]] proved it, script and compiled) and connects to it through an in-memory bridge instead of enet. The server code still thinks a client connected; the client still thinks it reached a server. So the lobby, rooms, games, bots, walls and menus all run from the same code as online.

**Key finding (2026-11-25):** both sides touch the network only through `network net;` and `network_event event;`:
- server: `net.setup_server`, `net.request` (3 places), `net.send_reliable` / `net.send_unreliable` (netfuncts.nvgt), `net.disconnect_peer_forcefully` / `net.disconnect_peer_softly`, `net.IPV6enabled`.
- client: `net.setup_client`, `net.connect` (2), `net.request` (6), the two sends (netfuncts.nvgt), `net.disconnect_peer_forcefully` (11), `net.IPV6enabled`.
- The engine's `network_event` fields are `const` (network.cpp 277-280), so script can't build a fake one. Hence a script wrapper class with the same field names.
- The engine also has `setup_local_server`, but that is still networking; not used.

**Requirements from the PoC:** join the server's include tree into one text with its own deps; `set_access_mask(0xFFFFFFFF)`; `reset_globals()` after build (and again to reset); messages as the same text strings; data paths resolve against the client's cwd (cf/client), where data/config already mirrors the server's.

**Sections (draft; order and details depend on the Q&A below):**

1. **Network wrapper (client and server).** Each side gets a small script class with the same method names (`setup_server`/`setup_client`, `connect`, `request`, `send_reliable`, `send_unreliable`, `disconnect_peer_forcefully`/`softly`, `IPV6enabled`) and an event class with the same field names (`type`, `peer_id`, `channel`, `message`). `network net;` becomes the wrapper; `network_event event;` becomes the wrapper's event type. Online, every call forwards to the real enet object, so behavior is identical; offline, calls go to the bridge. Encryption stays as it is (both ends still encrypt/decrypt the same strings). Test: online play unchanged, client and server.

2. **Server startup split (server).** cfs.nvgt's main() becomes `server_init()` (the current setup) + `server_tick()` (one pass of the netloop/gametick loop), with main() calling them as today. Offline, the client calls init once and tick every frame. Guard anything that only makes sense as a real program: the single-instance check, the server window (`show_game_window`/`hide_window`), `exit()` and relaunch in /restart and /shutdown, so an offline game can never close or restart the client.

3. **Offline loader and bridge (client).** New client file: join the server's include tree (`src/server/cfs.nvgt` and its `includes/` globs) into one text, build it as a module with the PoC's three requirements, bind the bridge functions, call server_init, then pump server_tick + deliver queued messages each frame while offline. Shut the module down (discard) when leaving offline play. Where the server source comes from: the dev run reads `../../src/server` from cf/client; a release build reads what section 7 ships.

4. **Offline sign-in (client and server).** No sign-in screen: the client logs into the offline module automatically with a local profile. Where that profile and its stats live, and whether they're kept between sessions, is a Q&A item.

5. **What offline leaves out (server and client).** Agreed list in the Q&A: chat, voice, other-player features, the soundboard, server-host features, account commands, script keys, and PVP.

6. **Menus (client).** Main menu loses "learn sounds menu"; game menu becomes play game, learn sounds, back; play game opens online / offline / back; online opens the existing online menu; offline runs the name prompt (first time) and then the offline start. See the Q&A's final layout.

7. **Build tools (build).** Ship the server's game code inside the client release, as a text constant compiled into cfc.exe (Q&A), plus nothing else of the server (no data/host, no docks).

8. **Docks (docks).** Readme: offline play, and the client's own data/config copy (deferred here from [[data-reorg-repointing]]); 5.3 (or later) changelog entry; memories ([[path-conventions]], [[include-tree]], [[launchers-and-running]], [[networking-protocol]]).

**Q&A log:** (questions asked one at a time in chat, [[ask-questions-in-chat]])
- Q: Where does offline play start: the lobby alone, StrideRush-style straight into the start-game menus, or a new client menu? (The dev first asked what StrideRush's play-game menu looks like: main menu > game menu > play game > a mode menu with descriptions > difficulty or per-mode options > the run.) A (dev, 2026-11-25): StrideRush-style, "That is exactly how I like it." The agreed flow, reusing the server's own start-game menus and wording, no new menus:
  - **FINAL menu layout (dev, 2026-11-25, "the final menu correction in full"; supersedes the earlier "online menu / offline menu" draft):**
    - Main menu: documentation menu, game menu, preferences menu, test speakers, restart game, exit game. The main menu's "learn sounds menu" item is REMOVED (dev: "Remove the learn sounds item off the main menu").
    - Game menu: **play game**, **learn sounds** (the existing `learnsoundsmenu()` browser), back. The "online menu" item that [[online-menu]] put here moves down a level.
    - Play game: a menu with the intro "Choose how you'd like to play.", with **online** and **offline** (plain words, dev: "Simply online, offline"), back.
    - Online: opens the existing online menu (`onlinemenu()`: sign in, accounts, server address, storage), unchanged.
    - Offline: asks for the name (first time only), then the game mode (step 1 below).
    - Alt+L ([[learn-sounds-menu]]) stays as it is. The readme's main-menu description (line 7, which also says "Choose the game menu, then the online menu"), its Learn sounds section ("The main menu also has a learn sounds menu"), and the unreleased 5.3 online-menu changelog entry must all describe the new path (docks section).
  - Offline > step 1 "Choose a game mode to play.": EVP (Environment versus player), PVE (Player versus environment), Free play (Sandbox), back. No PVP (needs humans).
  - Step 2 "Choose the map size": Small 25 by 25, Medium 50 by 50, Big 75 by 75, Large 100 by 100.
  - PVE only: step 3 "Choose a wall reinforce limit" (200, 400, 800 percent, No limit), step 4 the bot pile-up Yes/No. EVP and free play start right after the size; free play keeps its in-arena reinforce menu.
  - The online "Choose who can play" (solo/open) and player-limit steps are skipped: offline is always solo (pending_maxplayers 1, menu_pending "solo"), the same way PVP already skips the solo/open step.
  - The offline module quietly gives the player a private room behind the scenes, so the lobby and rooms never appear; when a game ends the player returns to step 1, as a StrideRush run returns to its menus.
- Q: Keep offline progress between sessions? Claude recommended saving it in the client's appdata (where settings.cvf already lives), not the game folder, so it survives updates and never reaches git or a release. The dev agreed on appdata and named the folder (2026-11-25): "I'd say call it saves". It plays the role of the offline server's `data/host` folder, same layout, so the server code only changes where its host path starts (a variable, `data/host/` online, the saves folder offline):
  - `%APPDATA%\tsatria03\CaveDefender\saves\main\` — conf.svr, motd.svr, peak.svr (written by the server code at startup; offline-only copies).
  - `%APPDATA%\tsatria03\CaveDefender\saves\game\players\<name>\info\*.usr` — the offline profile, the same fields an online account uses: username, created, seen, rank, nickname, pronoun, language, and, once played, pvebestround/pvebestrounddate, evpbestround/evpbestrounddate, totalwood, totalammo (plus privroom for the hidden room).
  - Nothing else: no chat filter, reports, feedback, moderation or onoff sound files offline.
- Q: What is the profile called? Claude suggested a fixed name (Player, or Guest, which is 5 characters but would skip registration anyway), then a list of 6+ character names. A (dev, 2026-11-25): "I'd rather a person type what their name is. This will be saved so they do not have to enter it again." Agreed details ("Exactly right"):
  - **When:** choosing **offline** under play game (final layout above; dev: "The offline mode will ask for the name, then the game mode"), only while no name is saved; afterwards offline goes straight to step 1.
  - **How:** one virtual dialog ([[input-prompt-form-vs-dialog]]), e.g. "Enter a name for your offline profile.", with the online username rules: 6 to 24 characters, no spaces (names ride space-delimited messages even offline). A broken rule is explained and the box asked again; Escape or empty says "canceled" ([[menus-say-canceled]]) and returns to the play game menu.
  - **Saved (unchanged by the final layout):** the name in the client's settings.cvf (preffs, beside the saved account); the profile in `saves\game\players\<name>\info`. If settings.cvf is reset but a profile folder exists, the client adopts that profile instead of asking again, so a settings reset never loses offline progress.
- Q: What does offline leave out? A (dev, 2026-11-25): "I believe so yes. Script keys cannot work in offline mode." Left out: chat (global, local, staff, team, private messages and replies), voice chat, other-player features (F1 player list, F6 players menu, F5 beacons, online/offline sounds and messages), the soundboard, server-host features (rules agreement, message of the day, reports, feedback, all staff and moderation commands), account commands (rename, delete, change password, nickname, pronouns), script keys (they only run chat commands), and PVP. Kept: everything inside a game (movement, walls, wood, weapons, ammo, bots, round status, alerts), the message buffers, the volume keys, the documentation reader (Alt+K) and learn sounds.
- Q: The play game menu intro (online / offline)? A (dev, 2026-11-25): "Choose how you'd like to play." (mirrors StrideRush's "Choose the game you'd like to play.").
- Q: Ship the server code in the client release as joined source text or precompiled bytecode? A (dev, 2026-11-25): "I'll do option 1", joined source text. The build joins src/server's include tree into one text file in the client bundle; offline start reads and compiles it (expected around a second for ~16,000 lines). Readable, but the repo is public anyway. Bytecode (faster, unreadable, but tied to the exact engine build, so an engine update would break it until rebuilt) stays a possible later upgrade if the startup compile is slow.
- Q: Where does the joined server file go in the client? Claude first suggested data/offline/server.nvgt. The dev asked whether the build deletes it after compiling (no: unlike cfc.nvgt it is compiled on the player's computer every time offline starts, so the release must ship it; a built-in text-constant alternative was described and not chosen), then created **cf/client/scripts/** for it (dev, 2026-11-25: "What about a scripts folder? I just created it."). So: **scripts/server.nvgt** in the client bundle.
  - The folder is empty in the repo, and git does not track empty folders, so a fresh clone would not have it. tools.py must therefore NOT list scripts in CLIENT_ASSETS (compile_side stops with "missing asset folder" when one is absent); instead it creates scripts/ in the client bundle and writes the joined server.nvgt straight into it.
  - Running from source, the client ignores scripts/ and joins src/server live (../../src/server from cwd cf/client), so offline always runs the current server code and nothing generated is ever committed.
  - Not the repo-root scripts/ folder, which holds the dev's own tools (block_comments.py).
- Q (superseding the scripts-folder answer above): the dev then moved scripts/ to %APPDATA%\tsatria03\CaveDefender\scripts; Claude explained a portable 7z can't put files in appdata and a stale copy there would mismatch an updated client. The dev's real concern (2026-11-25): "I was hoping players did not see the code at all because it risks them deleting it, and then the offline menu would be broken." Two built-in routes were checked in the engine source: a generated text constant, or `#pragma embed` of a pack (nvgt_angelscript.cpp 852, pack.cpp 636). A (dev): "I like the text constant better." So:
  - The server code travels INSIDE cfc.exe; no loose file anywhere, so neither cf/client/scripts nor appdata/scripts is needed.
  - Committed placeholder: **src/client/includes/scripts/server.nvgt**, holding `const string offline_server_code = "";`, included by a new `#include"scripts/*"` line in includes.nvgt (the client's glob style).
  - tools.py, before compiling the client: join src/server's include tree, escape it onto one line (backslash, quote, CR, LF, tab), and write it into that file as the constant; compile; then ALWAYS restore the empty placeholder (in a finally block, so a failed or interrupted build never leaves a half-megabyte change in git).
  - Offline start: if offline_server_code is empty (running from source), join ../../src/server live; otherwise build the module from the constant.
  - Cost: every client build carries roughly an extra half megabyte of text and compiles a little slower.
