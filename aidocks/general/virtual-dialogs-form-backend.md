---
name: virtual-dialogs-form-backend
description: "The virtual_dialogs (vd) class uses form.nvgt's audio_form as its backend, so form.nvgt's keyboard typing sounds play in EVERY input box game-wide"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

The client's `virtual_dialogs` class (the `vd` object — `vd.input_box`, `vd.password_box`, the chat prompts, etc.) is a front-end built on top of `form.nvgt`'s `audio_form` as its backend. It does NOT have its own separate text-entry path.

**Consequence:** the keyboard typing sounds live in ONE place — `form.nvgt`, as `formpool.play_stationary("sounds/ui/keyboard/<type|space|cap|delete|return>.ogg", ...)` (character sounds ~lines 2848-2850, delete ~3649-3667, return ~725/~3698). Because every input box in the game (chat input, account/server forms, password boxes) ultimately runs through that `audio_form` code, gating those play calls in `form.nvgt` covers the WHOLE game at once, and an F3 toggle placed in `form.nvgt`'s key loop applies everywhere. There is no second typing-sound path in `virtual_dialogs` to also patch.

The F3 `typingSounds` toggle (now built — gated in `form.nvgt`, persisted via `savefuncts.nvgt`) works exactly because of this: one gate in `form.nvgt` covers every input box. Relevant to any future change to text-entry feedback. See [[path-conventions]].
