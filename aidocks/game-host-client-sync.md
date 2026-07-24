---
name: game-host-client-sync
description: The client gates a game's host controls on current_game_host==name, kept in sync with the server's host_peer via a gamehost broadcast on every host migration — read before touching host migration, the round menu, or host hotkeys.
metadata:
  type: reference
---

A game has TWO independent notions of "who's the host", and they must be kept in sync by hand:

- **Server:** `games[].host_peer` (peer id) + `games[].host` (name). Every host-only action gate checks `host_peer == event.peer_id` (begin round, skip build, stop, kick, invite, wall damage, etc., in server `net.nvgt`/`game.nvgt`).
- **Client:** `current_game_host` (a plain username string, set from the `gamejoined` message's plain-name field). The client gates whether it even OFFERS host controls on `current_game_host == name` (the local username): opening the round menu on Enter (`client game.nvgt` `openmenu`), and the host hotkeys Ctrl+B begin / Ctrl+S skip.

The gotcha: if the server migrates the host but never tells the clients, the new host's `current_game_host` still holds the OLD host's name, so their client never lets them open the menu or fire the hotkeys — they're locked out even though the server would accept their commands. (Bug fixed in 4.8: "can't do anything after a host leaves".)

The fix / the rule to keep: **every host migration must call `announce_game_host(gi)`** (server `game.nvgt`), which broadcasts `gamehost <plainname>\n<displayname>` to the game's live members; the client `gamehost` handler (`net.nvgt`) sets `current_game_host` and posts a one-sentence "You are now the host of the game." / "<name> is now the host of the game." notice. There are FOUR migration sites — THREE in `game.nvgt` (become_watcher, leave_game, the disconnect-removal path) and ONE in `net.nvgt` `begin_hold` (see below) — all four call it. If you add a fifth way the host can change, call `announce_game_host` there too.

Reconnect-hold interaction ([[reconnect-persistence]]): a game host's role does NOT survive the hold. When a host drops, `begin_hold` swaps their peer to a negative sentinel and then **immediately migrates the game host to a live member** (first_live_member) + announces — so the game isn't frozen for the 45s (an idle game can still be started, a running one paused/stopped). If the dropped host reconnects, `restore_scope` re-sends `gamejoined` with the current host, so their client's current_game_host updates and they come back as a regular member (no reclaim). A solo/all-held game has no live member to hand to, so it stays parked. (Room host status IS still held across a reconnect — only the GAME host migrates.)
