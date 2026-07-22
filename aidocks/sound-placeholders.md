---
name: sound-placeholders
description: "When the user requests a sound, wire up the playback CODE referencing the intended filename now; the user adds the actual .ogg later. Don't create dummy files or wait for the asset."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

When the user asks for a feature to play a sound, **add the sound-playing code immediately, referencing the intended filename in the correct sounds subfolder**, even though the `.ogg` file does not exist yet. The user will add the real sound later ("when I find the perfect sound"). The code reference *is* the placeholder.

- **Do NOT** create a dummy/empty/copied `.ogg` file. A "placeholder" here means the code, not a stand-in asset.
- **Do NOT** withhold or comment out the playback code waiting for the file — wire it up as if the sound exists.
- After wiring it, **remind the user which file to add and where** (e.g. "add `notify.ogg` to `client/sounds/ui/misc/`"), since it'll be silent until then.

How sounds are played in this codebase (match these patterns):
- **Client, directly:** `p.play_stationary("sounds/ui/misc/<name>.ogg", false);` (or the relevant pool). UI sounds live under `client/sounds/ui/misc/`.
- **Server-driven:** the server sends `"play <name>.ogg"` on channel 0, and the client's `play` handler plays `sounds/ui/misc/<name>.ogg`. Use this when the server decides a client should hear something.

**Why:** the user designs features first and sources the "perfect" sound later; blocking on the asset (or faking one) just slows iteration. Wiring the real path now means the feature is complete the moment they drop the file in.

**How to apply:** any "it should play <name>.ogg" request → add the playback call with that exact path, then note the file to add. Pair with [[list-modified-files]] / [[relaunch-notice]] when reporting.
