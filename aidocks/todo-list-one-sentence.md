---
name: todo-list-one-sentence
description: "Every entry in cf/client/docks/todo list.txt must be ONE short sentence, both finished and unfinished items"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

Each item in `cf/client/docks/todo list.txt` (the `**Finished.` / `**Unfinished.` entries) must be **one short sentence**, not a long multi-clause run-on. The whole finished list was rewritten this way — trim to the gist.

**Why:** the dev reviews the list by screen reader; long run-on entries with several clauses are hard to scan and hold in your head. A one-line gist per item is far easier to browse.

**How to apply:** when adding a new todo item (finished or unfinished), write a single concise sentence — the headline of what it does, not the full spec. Save the detail for the changelog ([[changelog-rules]]) and the code, which are the durable record. When an unfinished item is completed, move it to the top of the finished section and keep it one sentence. Don't confuse this with changelog entries, which may run 1-3 sentences.

**Ordering — NEWEST FIRST in BOTH sections (dev's convention, confirmed 2026-07-15).** Like the changelog, the todo list is reverse-chronological: a NEW unfinished entry goes at the TOP of the Unfinished section, and a just-completed item goes at the TOP of the Finished section. The dev reordered the existing entries this way, so always prepend, never append.

**Dev's own convention (don't flag it as odd):** the dev deliberately adds a changelog line like "Updated the todo list file with the latest bug fix and feature improvements" when the todo list has been refreshed but that refresh was never logged. It's intentional bookkeeping, not a mistake — leave it be.
