---
name: nvgt-key-pressed-oneshot
description: NVGT key_pressed() is one-shot — never read the same key twice in one frame
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

In the pinned nvgt2 engine, `key_pressed(KEY_X)` is **consumed on the first read** each frame. Reading the SAME key in two separate `if` checks in one loop iteration means the second check always sees false.

**Why:** the auto-running feature added `if(key_pressed(KEY_R) and alt_is_down())` right before the existing `else if(key_pressed(KEY_R) and !in_game)` room-list check. With Alt up, the first read ate the R press, so plain R in the lobby silently did nothing.

**How to apply:** when one physical key drives multiple behaviors (modifier combos, mode branches), read it **once** into the `if` and branch inside:
`if(key_pressed(KEY_R)) { if(alt_is_down()) ...; else if(!in_game) ...; }` — not two sibling `if`s that each call `key_pressed(KEY_R)`. Different keys per check are fine. See [[angelscript-reserved-out]] for other engine gotchas.
