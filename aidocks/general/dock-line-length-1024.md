---
name: dock-line-length-1024
description: "Player-facing dock lines (server rules, server help, client docks): HARD CAP 1024 characters (the user's screen reader splits longer lines), RECOMMENDED limit 900 or less. Split long lines at a sentence boundary, no words changed."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

Two limits apply to every line in a player-facing doc:
- **Hard cap: 1024 characters.** Never exceed it. The user's screen reader splits any longer line into several, which reads awkwardly and can cut a thought in half.
- **Recommended limit: 900 characters or less** (dev, 2026-11-24: "The maximum cap is 1024, but the highly recommended limit is 900 characters or less."). Aim for this on every line you write or edit. A line between 900 and 1024 is technically allowed but should be split, because a few added words later would push it over the cap.

This applies to **all player-facing docs**:
- Server rules: `cf/server/docks/rules/{player,staff}.txt`
- Server help: `cf/server/docks/help/{player,staff}.txt`
- Client docks: `cf/client/docks/{changelog,readme,todo list,credits}.txt`

**Why:** these docs are written one logical entry per physical line (a numbered rule's body, a help command's description, a changelog entry, a readme paragraph), with no wrapping inside the file. So one long paragraph is one long line, and past 1024 characters the reader chops it mid-thought. The 900 margin keeps every line well clear of that.

**How to apply:**
- After editing or adding any dock text, measure the edited line(s) and confirm each is 900 or less.
- If a line is over 900, either tighten the wording (trim examples or redundancy, keep the substance) or split it. For a long readme paragraph the preferred split is at a sentence boundary where the topic shifts, into two paragraphs with a blank line between (the readme's own style), changing no words; verify by comparing the word list before and after. Changelog entries are one line each and capped at 1-3 sentences anyway ([[changelog-rules]]), so tighten those rather than split.
- When writing new dock prose, keep entries lean so they don't creep up on the next edit.
- Related: [[docks-and-help]] (which docs exist and how they're read). The [[one-sentence-game-messages]] rule is separate: that's for in-game feedback, not docs.

**History:** on 2026-11-24 the client docks were swept: three readme lines over 1024 (1328, 1091, 1156) and four close to it (965, 960, 912, 1016) were split at sentence boundaries; the longest client dock line is now 890. The server docks had not yet been swept against the 900 limit at that point (staff.txt had a 1003-character line).
