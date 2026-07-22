---
name: relaunch-notice
description: "When reporting changed files, also tell the dev whether the server and/or client must be relaunched to pick up the change."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

When ending a turn that edited files, in addition to the "Files changed:" list (see [[list-modified-files]]), tell the dev **whether they need to relaunch the server and/or the client** for the change to take effect.

The rule for CaveDefender (no hot-reload — both halves are NVGT scripts loaded at startup):

- **`.nvgt` code files** (client or server) — **relaunch that side.** Code is compiled/loaded once at startup, so a running instance won't see edits until restarted. Editing a server `.nvgt` = relaunch the server; editing a client `.nvgt` = relaunch the client.
- **Data files read at runtime** — usually **no relaunch needed.** Account files (`data/players/*.usr`), `motd.svr`, `conf.svr` are read fresh by the server when needed (e.g. `load_account`/`get_rank` on login), so a new value applies on the next login/read. Caveat: a player already in-session won't see a change to their own loaded state until they reconnect.
- **`docks/*.txt`** (changelog, todo, readme, credits) — **don't mention relaunch at all.** The dev already knows these are outside the running game, so omit the relaunch note entirely when only docks changed.

**Why:** the dev runs the server and client as separate processes and needs to know, per change, whether a restart is required before testing — especially since a server `.nvgt` edit silently has no effect on a still-running server.

**How to apply:** after the Files changed list, add a one-line relaunch note, e.g. "Relaunch: server (code change); client not affected." If only data/docks changed, say so ("No relaunch needed — data read at runtime").
