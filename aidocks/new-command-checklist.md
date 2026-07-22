---
name: new-command-checklist
description: "When adding or changing a slash command, update all five places together so code and docs never drift"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

The user agreed (2026-07-01): any time we add or change a slash command going forward, do all of these in the same change so nothing drifts:

1. **Client** `src/client/includes/main/parsers/command_parser.nvgt` — the router: arg-count validation via `syntax_error()`, the client-side rank gate (`my_rank_level()`), and forward on the right channel. It's a router, not an executor (see [[command-parser-conventions]]).
2. **Server** `src/server/includes/main/globals/net.nvgt` — the authoritative handler with the real rank check (`rank_level`/`is_staff`), at-or-below-target and grant-cap rules, and online-target requirement (except `/unban`). Use `reply_target_not_found()` for the not-found reply.
3. **Both `/help` pages** — `cf/server/docks/help/player.txt` and/or `staff.txt`, documenting the command at its correct rank. (As of the 3.0 audit these matched the code exactly — keep it that way.)
4. **Changelog** — a player-facing entry per [[changelog-rules]].
5. **Keep the wire strings identical on both sides** — the space-delimited protocol is a client/server contract; a rename on one side must match the other.

**Why:** the client gate is UX-only (hides staff commands as "unknown"); the server is the real authority. Docs drifting from code is the classic bug here. **How to apply:** treat these five as one unit for every command add/change.
