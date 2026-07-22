---
name: nicknames
description: "Nicknames = display name (nickname.usr); username stays the identity. display_name* helpers return the nickname; commands target username (Option 1). /nick set/default, staff /nick username altname"
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

Player nicknames (built 2.2, task #24). **Username = identity** (login, account folder, ALL command targeting); **nickname = display**, shown in place of the username everywhere a name is spoken.

Storage: `nickname.usr` in the account folder. `get_nickname(name)` (defaults to the username) / `set_nickname(name, nick)` in account.nvgt; `create_account` writes it = username. The in-memory roster has `players[].nickname`, loaded at spawn (net.nvgt spawn handler). ALL `display_name` / `display_name_for` / `display_name_flagged` / `display_name_flagged_for` return the nickname instead of `.name`, so every server-built display (chat, /me, PM, R/L/G, lifecycle, host labels, afkannounce, flag announce) shows the nickname automatically.

Client-built displays needed nickname plumbing: `pos` gained a trailing nickname token (`pos <username> x y vrank afk nickname`) — roster keyed by **username** (parsed[1]), tracker shows nickname; `online`/`offline` gained a nickname token (`<username> <rank> <nickname>`) — display nickname, remove_player by username. roomjoined/gamejoined already used a trailing flag-aware display line for the announcement and kept the username for host comparison.

Command: `/nickname`/`/nick <name>` sets your own (or `default` to revert); `/nick <username> <altname>` is the staff form — **all staff** (rank_level ≥ 1), targets an ONLINE player by username (like /afk). `apply_nickname(ti, requested, issuer_peer, byself)` (net.nvgt): validates format (3-24 chars — shorter min than usernames so "tony" works — plus filterchar's letters/numbers/-/_) unless "default"; **uniqueness** = rejects if any other online player's nickname OR username matches (anti-impersonation); persists; `broadcast_pos` to refresh the tracker; alerts EVERYONE via `alert <text>` ("<old afk+flag-aware display> has changed their nickname to <new>" for self, "...'s nickname has been changed to..." for staff).

**Command targeting** (evolved past the original Option 1): `get_player_index_from` now resolves a typed name to an ONLINE player by **username first, then nickname** (exact-case), so commands accept either. Per the dev, player-targeting commands now require the target to be **ONLINE**: `/promote`, `/demote`, `/ban`, `/warn`, `/mute`, `/unmute` were converted from offline-capable (`account_exists_exact`) to online-only — they now use `get_player_index_from`, operate on `players[ti]`, and persist via `players[ti].name` (NOT the typed name, which may be a nickname). `/kick`, `/afk`, `/pm`, `/nick`, `/notifyplayer` already required online. The ONLY offline-capable holdout is **`/unban`** (banned players are always offline, so online-only is impossible) — it takes the username. (`/unmute` was briefly kept offline-capable then made online-only too, since a mute doesn't remove the player.) Not-found feedback is context-aware: `account_exists_exact(name)` true → "This player is not online.", else "This player does not exist." (all "not found"/feedback messages now carry the `misc ` prefix → misc buffer). `kickannounce`/`banannounce` gained a nickname token (`<username> <rank> <nickname>`) — display nickname, remove_player by username. `/who` and `build_staff_list` append `(username)` when it differs from the nickname. Nicknames are space-free (protocol is space-delimited). See [[path-conventions]], [[command-parser-conventions]].

Related sound changes (same task): `alert.ogg` now plays for generic alerts-buffer items that lack a dedicated cue (the `alert` prefix handler + `restartnotice`); notify sounds reduced to 2 (`notify1`/`notify2`), client picks `random(1,2)`.
