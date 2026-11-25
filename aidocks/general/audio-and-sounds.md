---
name: audio-and-sounds
description: "CaveDefender's sound_pool/HRTF audio model and the cf/client/sounds/ folder map since the 2026-11 reorg (sounds/main for UI + alerts, sounds/game for equipments + objects/audio + objects/construction). The ONE place that describes the sound folders; read when wiring a sound or referencing a sound path. No swappable sound packs."
metadata:
  node_type: memory
  type: reference
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

NVGT `sound_pool` with HRTF. Player position is the vector `me`; pools advance per frame and every pool's listener is re-anchored to `me` each frame by `update_sound_pools()`. Code references sounds cwd-relative as `sounds/...` (the launcher's cwd is `cf/client`, see [[path-conventions]]).

**Folder map (current, since 2026-11-23/24):**
- `main/ui/` — `buffer/` (choose, switch), `dialog/` (open, close, scroll, coppy — the dev's spelling), `keyboard/` (type, space, cap, delete, return), `menu/` (click, close, edge, enter, open, wrap, music, speaker — speaker.ogg was deliberately replaced 2026-11; it is what the main menu's "test speakers" option plays).
- `main/misc/` — the game's alerts and cues (52 files: online/offline, chat cues, von/voff, ping, welcome, newmotd, kick, ban, promote/demote, notify, toggleon/off, beacon, turn, wave/build/pause cues, afk, invites, leaderboard...). `gameover.ogg` and `roundcleared.ogg` are referenced in code but don't exist yet: sound placeholders for the dev ([[sound-placeholders]]).
- `game/equipments/items/wood/<oak|maple|birch|pine>/` (drop, loop, place, take) and `game/equipments/items/ammo/<arrow|gas|grenade|normal|powder>/` (drop, loop, take).
- `game/equipments/weapons/<class>/<name>/` — melee (axe, bat, crowbar, feet, fist, hammer: draw, fire1-3, hit1-3, rico), archery (crossbow: draw, empty, fire, hit, loop, ping, reload, rico1-2), explosive (cannon, firebomb, grenade: draw, empty, fire, hit, loop, ping, reload, rico), artillery (machinegun, pistol: same set plus rico1-12 and shell1-2). Enemy bots play the `hit` clips when they strike a wall.
- `game/objects/audio/ambience/` and `game/objects/audio/music/` — cavern_ext, cavern_int, lobby, room (one bed/track per area).
- `game/objects/construction/platforms/<tile>/step1-5` — carpet (lobby), marble (office room), concrete (cave floor), gravel (EVP outdoor exterior), woodpile (the breach left by a destroyed wall).
- `game/objects/construction/walls/<wall>/` — wallwood (bump, death, hurt1-3, burnstart/burning/burnstop for the firebomb), wallbuilding (lobby), wallgeneric (office room), wallcrate (inside/PVE spectator deck border, bump only), wallwoodpile (EVP outside watcher deck border).

**Paths travel over the wire.** The client sends `step <subpath> <x> <y>` (e.g. `step game/equipments/weapons/melee/axe/draw`, `step main/misc/turn`), the server relays it as `footstep <subpath> <x> <y>` to the same room, and the receiver plays `sounds/<subpath>.ogg`. The server also originates `footstep game/equipments/items/{wood,ammo}/<type>/take` for pickups, and the client's net.nvgt sorts incoming paths containing `game/equipments/items/ammo/` / `game/equipments/items/` into the ammo/wood pools. So renaming a sound folder is a PROTOCOL change: client and server must change together and ship under a new version ([[sound-path-repointing]], [[networking-protocol]]).

**Pools:** `p` (general) = UI/local sounds, other players' footsteps and wall bumps, wall death/hurt; `beaconpool` = player locator beacons; separate pools for items (woodpool, ammopool), weapons, bots (botpool), burning walls (burnpool), ambience (ambpool), music (musicpool), and `crosspool` for PVP cross-wall sounds. The cave interior carries reverb and the exterior/through-wall gets a lowpass muffle, applied via pool mixers (and, for voice, directly on the sound) in `globals/effect_space.nvgt` — see [[include-tree]].

**Rules:** no swappable sound packs ([[no-sound-pack-support]]) — paths point directly at the fixed folders. When a sound is requested, wire the playback to the intended filename now and let the dev add the `.ogg` later ([[sound-placeholders]]). Sounds ship as an ordinary loose folder since boxing was removed (2026-11-24, [[build-tools-remove-boxing]]), so `file_exists()` on a sound works again. After any reorg, run a checker over every quoted sound path and grep both src trees for old folder names (the method is in [[sound-path-repointing]]).
