---
name: map-helpers-location
description: "Map helper functions live in client functions/mapfuncts.nvgt, not extrafuncts.nvgt"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

Map-related helper functions go in `client/includes/main/functions/mapfuncts.nvgt`, NOT `extrafuncts.nvgt` (which is for general utilities). So far it holds `facing_name()` (facing int -> spoken word) and `gmt()` (the tile the player is standing on).

**Why:** the dev is organizing helpers by domain — `extrafuncts` (general), `savefuncts` (save/load), `mapfuncts` (map). They explicitly moved the facing helper out of extrafuncts into mapfuncts and asked that any map helper go there.

**How to apply:** when writing a new map-related helper, put it in `mapfuncts.nvgt`. Map STATE and the per-frame core (the `me` vector, facing/timer globals, the direction consts, `draw_map`/`playstep`/`bounce`) stay in `globals/map.nvgt`. `distance()` stayed in extrafuncts (it's general coordinate math, not map-specific). Relates to [[path-conventions]].
