---
name: audio-and-sounds
description: "CaveDefender's sound_pool/HRTF audio model and the cf/client/sounds/ folder layout (ui, objects/walls, objects/platforms, objects/items, weapons). Read when wiring up a sound or referencing a sound path. No swappable sound packs."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

NVGT `sound_pool` with HRTF. Player position is the vector `me`; pools advance per frame. `cf/client/sounds/` (referenced cwd-relative in code as `sounds/...`) is organized by category, with a **per-type subfolder** holding named clips:
- `ui/` — `buffer/`, `dlg/`, `menu/`, `misc/` (online, offline, playerchat, privchat, von, voff, pingstart, pingstop, welcome, newmotd, kick, ban, promote/demote, notify, buildprep, wavestart, wavestop, gameover, pause, resume, etc.).
- `objects/walls/<wall>/` — e.g. `wallwood/{bump,death,hurt1-3}.ogg`; also `wallbuilding/bump.ogg` (lobby), `wallgeneric/bump.ogg` (office room), `wallcrate/bump.ogg` (the inside/PVE spectator deck's indestructible border — bump only, never breaks), and `wallwoodpile/bump.ogg` (the EVP outside watcher deck's border).
- `objects/platforms/<tile>/` — e.g. `caveground/step1-5.ogg`; also `carpet` (lobby), `marble` (office room), `gravel` (EVP outdoor exterior), and `woodpile` (the breach left when a wall is destroyed).
- `objects/items/<item>/` — e.g. `wood` (`drop`/`loop`/`place`/`take`).
- `weapons/<weapon>/` — `axe`, `bat`, `crowbar`, `hammer` (`draw`/`fire1-3`/`hit1-3`); the enemy bots play the `hit` clips when they strike a wall.

This game does **not** support swappable sound packs (see [[no-sound-pack-support]]) — paths point directly at the fixed subfolders. `map.nvgt` builds the per-type subfolder paths (`objects/walls/<wall>/bump.ogg`, `objects/platforms/<tile>/step<n>.ogg`); `spawn_map()` lays a `wallwood` border around a `caveground` interior, with `me` starting at `(1,1)` on the interior.

The cave interior carries reverb and the exterior/through-wall gets a lowpass muffle, applied via pool mixers (and, for voice, directly on the sound) in `globals/effect_space.nvgt` — see [[include-tree]]. When a new sound is requested, wire the playback code to the intended filename now and let the dev add the `.ogg` later (see [[sound-placeholders]]); if the build is boxed, the client `.evb` must be regenerated so the new file ships embedded (see [[enigma-boxing]]).
