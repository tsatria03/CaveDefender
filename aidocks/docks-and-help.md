---
name: docks-and-help
description: "CaveDefender's player-facing docs — the client cf/client/docks/ files (changelog/credits/readme/todo) and the server-authoritative cf/server/docks/help + rules served via /help and /rules. Read when updating docs, help pages, or rules."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

The client docks live under **`cf/client/docks/`**: `changelog.txt`, `credits.txt`, `readme.txt`, `todo list.txt`. There is no longer an in-game documentation viewer (the menu was removed), but **`changelog.txt` is still the source of truth for what shipped** and is maintained on every release (see [[changelog-rules]]; the todo list follows [[todo-list-one-sentence]]).

There is **also a server-side `cf/server/docks/`**, organized into subfolders: `help/` (`player.txt`, `staff.txt` — the help pages) and `rules/` (`player.txt`, `staff.txt` — the server rules players agree to). The whole `docks/` tree is copied into the server build by `build/tools.py` (no pragma), so new subfolders ship automatically.

Help is **server-authoritative**: `/help player` / `/help staff` (client) → server reads `docks/help/<which>.txt` (cwd-relative under `cf/server`) and sends `helptext <which>\n<content>` → the client shows it with `dockread(title, text)` (the text overload added so received content needs no temp file). **Keep the two help files updated when commands change** — they document every command and its rank (part of [[new-command-checklist]]). The rules pages work the same way via `/rules player` / `/rules staff`; the rules-agreement gate is version-tracked (`rulesver`, floored at 1) with an explicit `ruleswitch` off-switch in `conf.svr`.
