---
name: player-events-lifecycle
description: "Lifecycle notices (room/game create/delete/leave/stop, kick, AFK) split: actor gets first-person misc, everyone else gets third-person player-events via broadcast_event(); server-wide, flag-aware, no AFK-prefix"
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

The actor/bystander split for game & room lifecycle notices (built 2.1, task #36). Every lifecycle action produces TWO different messages and nobody gets both:
- **Actor** (who did it) → a **first-person** line in their own **misc** buffer ("You are now in your public room", "You kicked bob", "You stopped the game"). Many already existed (roomjoined/roomleft/gamejoined/gameleft).
- **Everyone else, server-wide** → a **third-person** line in their **player events** buffer ("bob just created a public room. You can join it…").

Server: `broadcast_event(text, skip1 = -1, skip2 = -1)` (net.nvgt) sends `event <text>` to all players except the skipped peer(s); the client appends `message.substr(6)` to the **player events** buffer. Names use `display_name_flagged` / `display_name_flagged_for` (flag-aware) — **NOT** `afk_prefix` (dropped per the dev: you can't do most things while AFK anyway). Audience is the WHOLE server (dev's choice), not just the local room/lobby. Private rooms ARE announced too. Only OPEN games announce "started… you can join" (solo games are unjoinable, so silent).

Wired at: do_create_room and do_join_room (room.nvgt), and net.nvgt handlers leaveroom, startgame (if !solo), leavegame, both stopgame handlers, kickfromroom, deleteroom. (do_join_room was added in 2.2 — joining a room was initially missed; it's the complement of leaveroom.) Multi-recipient cases that can't use the 2-skip helper: **kick** skips kicker+kicked (kicked gets `roomkicked` misc, kicker gets "misc You kicked X"); **deleteroom** loops players manually and sends `event` only to non-members (members get `roomdeleted` misc + map reset). The old `roomkickannounce` message was removed (replaced by `event`). `playerjoinedgame` (game-scoped, has joingame sound) was left as-is — joining a game wasn't in scope.

AFK is part of this pattern — see [[commands-usable-while-afk]]: `afkself` (actor, misc) + `afkannounce` (others, player events), both with the cue.
