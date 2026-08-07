---
name: soundboard
description: The /playsound (/pls) soundboard — play a server-hosted clip to everyone, base64-streamed with client cache, path-safe + rank-scoped, with a menu picker reusing the editdata/viewdata browser pattern. Read before touching /playsound, the sound browser, or the sounds/player and sounds/staff trees.
metadata:
  type: project
---

**Feature (dev, 2026-08):** `/playsound <path>` (alias `/pls`) plays a short server-side clip to EVERYONE connected. Clips live on the server under `cf/server/sounds/player/{common,misc}/` (shared, any player may play) and `cf/server/sounds/staff/{common,misc}/` (staff only). `player` and `staff` are the only roots; `common` and `misc` the only categories. New clips can be dropped into those folders anytime — no client reship, because the bytes are streamed. Clip filenames CONTAIN SPACES (e.g. `staff/common/a good waste of fiddling jerks.ogg`), which drove the wire design.

**Locked design decisions (all confirmed by dev):** playback is STATIONARY (everyone hears it identically, an announcement not spatial); scope is the WHOLE server (not room-scoped); SILENT to players (no public "X played a sound" line) but a quiet STAFF AUDIT note records who played what; NO cooldown; the actor gets a one-line confirmation. Permissions: players → `player/` only; staff → `player/` AND `staff/`, enforced entirely server-side so a modified client can't reach `staff/`.

**Delivery = base64 stream + per-session client cache** (mirrors [[onoff-sounds]]). Pull-on-miss: the server broadcasts only the path, each client plays from cache or fetches the bytes once. `getsound` has NO rank gate on purpose — any listener (incl. a regular player) must be able to fetch a staff clip a staffer just played to everyone. The rank gate is only on WHO can trigger a play.

**Wire protocol (all channel 0):**
- Client→server: `playsound` (open picker) · `playsound <path>` (play/browse; path is the whole remainder after `"playsound "`, kept whole since names have spaces — so `parsed[0]=="playsound"` works because a SPACE, not a newline, follows the verb) · `getsound <path>`.
- Server→all: `soundplay\n<relpath>` (relpath on line 2 — has slashes+spaces but no newline).
- Server→one: `soundpush\n<relpath>\n<base64>` (base64 has no newlines under STRING_BASE64_DEFAULT, so it's the whole 3rd line).
- Client reads `firstline[1]`/`firstline[2]` for the path/payload, NOT `parsed`.

**Server code (all reuse the editdata/viewdata browser machinery — see [[new-command-checklist]], [[command-parser-conventions]]):**
- `menu.nvgt`: the picker sorts folders+files with `dirs.sort(natural_number_sort)` (natural-number order — misc2 before misc10; dev request, NOT the plain `sort_names_ci` the editdata browser uses). `natural_number_sort(const string&in, const string&in)` IS a registered global in the pinned legacy engine (confirmed in `misc/Legacy-NVGT/src/misc_functions.cpp`), and `array<T>::sort(const less&in, ...)` matches its signature (`ASAddon/src/scriptarray.cpp`), so this is the same call SimpleFighter uses — no hand-rolled comparator needed. Plus `safe_sound_path()` (twin of `safe_data_path`, confines to `sounds/`), `sound_floor(index)` (player→`"player"`, staff→`""`), `sound_path_reject(index, relpath)` (whitelist + rank gate, re-applied every step), `broadcast_sound(index, relpath)` (validate → `send(0,"soundplay\n"+relpath)` → actor confirm → `notify_staff_audit(..., peer)` with actor excluded), `push_sound_nav(index, relpath)` (picker; folders drill, files play), and the `soundnav` branch in `on_menu_result` (Escape walks up one level, stops/closes at your floor, sends `datacancel`).
- `net.nvgt`: `playsound` handler (menu vs play, via `string_contains(message," ")`) and `getsound` handler (path-confined + whitelisted, no rank gate, replies `soundpush`).
- `player.nvgt`: `sound_nav_path` field (the picker's current folder, for Escape walk-up).

**Client code:**
- `net.nvgt`: globals `sound_cache` (dict relpath→cache file path, per session) + `sound_cachefile()` (slashes/spaces→underscores under `DIRECTORY_APPDATA + "tsatria03/CaveDefender/soundcache/"`); `play_soundboard(path)` keeps `soundboard_slot` and calls `p.destroy_sound(soundboard_slot)` before `p.play_stationary` so a new clip CUTS OFF the previous one still ringing (dev request; same pattern as the weapon-draw slot); handlers `soundplay` (cache hit → `play_soundboard`, miss → `getsound`) and `soundpush` (decode → cache file → set dict → `play_soundboard`).
- `command_parser.nvgt`: `/playsound`/`/pls` router — NO rank gate (server scopes folders); no-arg sends `playsound`, arg sends `"playsound "+remainder`.
- `menu_parser.nvgt`: `soundnav` added to the Escape-suppression (like `datanav:`) so the picker's own walk-up doesn't auto-say "canceled"; the server's `datacancel` speaks it when it actually closes.

**Note:** this is a genuine soundboard, unrelated to [[no-sound-pack-support]] (which rejects per-listener notification-sound packs). Docs: player help + staff help entries, changelog, readme "Soundboard." section, todo Finished.
