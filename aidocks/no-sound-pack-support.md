---
name: no-sound-pack-support
description: "CaveDefender will NOT have sound pack support, unlike SimpleFighter"
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

CaveDefender does **not** have (and will not get) sound pack support — even though SimpleFighter, which this project borrowed code and structure from, does.

**Why:** Explicit design decision by the dev (stated 2026-06-11). The `sounds/` folder was reorganized into categorized subfolders (`ui/`, `objects/walls`, `objects/platforms`, `player/`, `ambience/`, `music/`) purely for a cleaner layout, NOT to enable swappable sound packs.

**How to apply:** Don't add sound-pack/loading-from-pack machinery, and don't justify sound-related work (folder reorg, new sounds) by referencing sound packs. Sound paths point directly at the fixed `sounds/...` subfolders. See [[changelog-rules]] — a changelog entry was reworded to remove a mistaken sound-pack claim.
