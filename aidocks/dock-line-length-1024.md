---
name: dock-line-length-1024
description: "Keep every line in the player-facing docks (server rules, server help, client docks) at or under 1024 characters, because the user's screen reader splits any longer line"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

Each line in a player-facing doc must stay **at or under 1024 characters**. The user's screen reader splits any line longer than that into multiple lines, which reads awkwardly.

This applies to **all player-facing docs where possible**:
- Server rules: `cf/server/docks/rules/{player,staff}.txt`
- Server help: `cf/server/docks/help/{player,staff}.txt`
- Client docks: `cf/client/docks/{changelog,readme,todo list,credits}.txt`

**Why:** these docs are written one logical entry per physical line — a numbered rule's body, a help command's description, a changelog entry — with no wrapping inside the file. So a single long paragraph is one long line, and once it passes 1024 chars the reader chops it mid-thought.

**How to apply:** after editing or adding any dock text, check the length of the edited line(s) (e.g. `awk 'NR==N {print length($0)}' file`). If a line is over 1024, tighten the wording first (preferred — trim examples/redundancy, keep the substance), or split it into two entries/sentences-on-their-own-lines if the content genuinely needs the room. When writing new dock prose, keep entries lean so they don't creep over on the next edit. Relates to [[changelog-rules]] (entry caps/prose style) and [[docks-and-help]] (which docs exist and how they're read); the [[one-sentence-game-messages]] rule is separate — that's for in-game feedback, not docs.
