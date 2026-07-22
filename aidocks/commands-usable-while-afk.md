---
name: commands-usable-while-afk
description: Players can run slash commands while AFK; command broadcasts must be AFK-aware (afk_prefix)
metadata: 
  node_type: memory
  type: project
  originSessionId: c482c7b1-1d44-40e1-bdc5-885ee6305ae7
---

A player can issue `/` commands **while still AFK** — running a command does not first un-AFK them. So any third-person notice a command broadcasts about its actor must be AFK-aware: prefix the actor's display name with `afk_prefix(index)` (alongside `display_name_flagged(index)` for rank/nickname), e.g. the `/motd` change notice `afk_prefix(index)+display_name_flagged(index)+" has changed the Message of the Day to: "+motd`.

**Why:** an earlier assumption that "the actor can't be AFK while typing a command" was wrong and the user corrected it.

**How to apply:** when adding a command that announces its actor in third person, include `afk_prefix`. Note [[player-events-lifecycle]] says lifecycle player-events notices are flag-aware but carry *no* AFK prefix — that's a separate convention for lifecycle events, not command-response broadcasts.
