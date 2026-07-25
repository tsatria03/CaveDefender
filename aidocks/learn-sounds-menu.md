---
name: learn-sounds-menu
description: Design spec for the 5.0 Learn Sounds menu — a main-menu, offline sound-preview browser built on form_menu.nvgt's learn_game_sounds_menu helper, organized by sound-folder categories with per-entry "used in <mode>" context clauses. Read before building learn-sounds.
metadata:
  type: project
---

The **Learn Sounds menu** is a committed 5.0 todo item ("Add a learn sounds option for the EVP and PVE game modes so players can have an idea on how the modes work when being played"). It's onboarding for an audio-only game: newcomers preview the game's audio cues before playing. **BUILT in 5.0 (awaiting dev test)** — the design below was agreed 2026-07 with the dev, then implemented.

## As built (5.0)
All in **`src/client/includes/main/menus/menu.nvgt`**: a new **`learnsoundsmenu()`** placed right after `docsmenu()`, plus a `"learn sounds menu"` item (id `"learn"`) in `mainmenu()` that fades music and calls it. Also reachable **in-session via Alt+L** (mirrors Alt+K docs): the L-key handler in `game.nvgt` reads L once and branches — `alt_is_down()` → `mute_pools(); learnsoundsmenu(); unmute_pools();`, else the plain-L lobby list. Alt+L is unreachable while paused/frozen (those branches `continue` past the handler). **Silence the game by MUTING, not pausing** — this was iterated: `pause_pools()` only freezes sounds already PLAYING, but the menu keeps pumping the network (`net_keepalive_cb`), so incoming spawn messages start NEW sounds mid-menu (items, and especially rapid bot footsteps — `botstep` → `botpool.play_3d`, net.nvgt:1117) that a one-time pause misses; even re-pausing each tick left a window (a botstep plays during `netloop`'s drain, before the post-netloop pause). The fix: **`mute_pools`/`unmute_pools`** (decpool.nvgt) set each `pool.mixer.volume = -100`, which the engine's `set_volume_alt` maps to linear amplitude 0 (fully silent; 0 = full). Every pool sound routes through `pool.mixer` via `set_mixer` (sound_pool.nvgt:303-305) and so do new ones, so they're born silent — no timing gap. `unmute_pools` restores the saved volumes (`saved_pool_volumes`). Preview sounds (plain `sound`) and menu clicks (`menupool`) aren't in `all_pools`, so they stay audible. Engine ref: `misc/Legacy-NVGT/src/sound.cpp` (mixer `set_volume`/`set_volume_alt`), which lives in the **parent** `tsatria03/` dir, not the CaveDefender repo. Two file-scope helpers build the dictionaries: **`ls_add(dictionary@ d, label, path)`** (single file) and **`ls_addv(dictionary@ d, label, dir, base, count)`** (numbered-variant for-loop, appends ". This sound has multiple variants."). Both write with **`d.set(...)`** — the client's convention for writing a `dictionary@` (opIndex reads like `dict[key]` and `cast<dictionary@>(dict[key])` are fine, but writes use `.set()`; see form_menu.nvgt). Categories assembled into a `learnCategories` dictionary via `.set()`, keys sorted `sort_ascending()`, a `while(true)` category picker (`setupmenu(false)` → `m.run()`), then for a chosen category: `setupmenu(false)` (fresh list so the helper's `selected_item >= sfx.size()` = Go-back logic holds), `m.automatic_intro=false` (helper calls `intro()` itself), then `learn_game_sounds_menu(cast<dictionary@>(learnCategories[sel]), "sounds/", m)`. Offline-safe (main menu; `net_keepalive_cb` background callback is a no-op pre-login). Label wording (after dev polish): melee "swing", ranged "fire", loop = "<gun> bullet" for guns / "<weapon> projectile" for archery+explosive, ping = "<weapon> reloaded" (e.g. "Machine gun reloaded"), "ricochet" (rico), "shell casing" (shell). Wood = "<kind> <action>" with loop just "loop"; ammo = "<kind> ammo <action>" (e.g. "Gas ammo drop"). Walls: "hit"/"break"/"ignite"/"burning"/"extinguish". Surfaces: "<surface> step: used when you walk on …". Interface: "Wave begin"/"Wave end" (begin sorts before end, so order is right), "Player turn", "Build phase", "Game paused/resumed", "Player beacon", "Join game", "Leaderboard climb/update". The sound-list intro is just "<category> sounds." — NO key-navigation instructions (navigation is configurable in the client menu settings, so don't hard-describe arrow keys).

## The engine already exists — reuse it, don't rebuild

`src/client/includes/main/deps/form_menu.nvgt` already ships **`learn_game_sounds_menu(dictionary@ sfx, const string&in audio_prefix = "", form_menu@ m = null)`** (lines ~519-556). It:
- takes a `dictionary` mapping a **description** (the menu label) to either a **filename** (`string`) or a **list of filenames** (`string[]` — plays a RANDOM one each press);
- sorts the descriptions ascending, lists them + a "Go back" item;
- loops: arrowing to a new item **stops** the current sound, Enter **loads `audio_prefix + filename` and plays it**, "Go back"/Escape exits; a missing file speaks "Unable to play …".

So the browsing machinery is done. We only build the **category structure**, the **content dictionaries**, and the **main-menu entry point**.

## Reference: how ToyMania did it (a DIFFERENT repo, for pattern only)

`C:\Users\tonys\OneDrive\Documents\github\tsatria03\games\ToyMania` used this exact helper before it moved to a custom menu object. Key commits (ToyMania repo, not CaveDefender):
- **`64129f4`** — first version: ONE flat `dictionary sfx` of every sound, bare Title-Case labels ("Bat Draw", "Boss Alert"), `@m.pack_file = @sound_default_pack;` then `learn_game_sounds_menu(sfx, "", m)`.
- **`c8da4b1`** — added **categorization**: a `dictionary learnCategories` (category name → its own sub-`dictionary` of sounds), sort the category keys, show a **category picker** menu + "Back", and on select call `learn_game_sounds_menu(cast<dictionary@>(learnCategories[sel]), "", m)`. Two-step drill-down. Also a `variant_descriptions` bool that appends `". This sound has multiple variants."` (`vdesc`) to any list-valued entry's label.
- **`747f545` / `5b45566`** — added a **mode-context clause** to each description: `"<Description>: used in <mode> mode"` (e.g. "Dart fire: used in endless mode", "Alarm: used in normal mode"), the clause BEFORE the `+ vdesc` variant note.

## Agreed design for CaveDefender (dev-confirmed 2026-07)

1. **Entry point: the main menu.** New item in `mainmenu()` (`src/client/includes/main/menus/menu.nvgt`) → a `learnsoundsmenu()` function. It's offline/local (pure sound playback, no server), so it belongs before sign-in.
2. **Organized by SOUND CATEGORY, not game mode.** CaveDefender's sounds are filed by TYPE (`cf/client/sounds/`), and the modes SHARE them (wood → PVE+free play; ammo/weapons → EVP+free play; walls/platforms/ambience → all), so a type split falls straight out of the folders while a mode split would force arbitrary "which mode owns this shared sound" calls. Use the **categorized two-step drill-down** (category picker → per-category list) like ToyMania's `c8da4b1`.
3. **Categories mirror the folders.** The sound tree: `ambience/`, `music/`, `equipment/items/wood/{oak,maple,birch,pine}`, `equipment/items/ammo/{arrow,gas,grenade,normal,powder}`, `equipment/weapons/{archery/crossbow, artillery/{pistol,machinegun}, explosive/{cannon,firebomb,grenade}, melee/{axe,bat,crowbar,feet,fist,hammer}}`, `objects/walls/{wallbuilding,wallcrate,wallgeneric,wallwood,wallwoodpile}`, `objects/platforms/{carpet,concrete,gravel,marble,woodpile}`, `ui/{buffer,dlg,keyboard,menu,misc}` (misc has ~51 files, needs CURATING not dumping). Final categories (dev-decided, see Final scope below): **Wood, Ammo, Weapons, Walls, Surfaces, Interface**.
4. **Descriptions = short Title-Case "<Subject> <Action>" identity labels PLUS a mode-context clause**, following ToyMania's later style: `"<Description>: used in <modes> mode"`, spelling out the SPECIFIC modes a cue appears in (PVE / EVP / free play / all). Examples the dev approved: `"Oak pickup: used in PVE and free play"`, `"Pistol fire: used in EVP and free play"`, `"Wall wood hit: used in all modes"`, `"Wave warning: used in PVE"`. Loops labeled with "Loop".
5. **NO sound packs** (deliberate CaveDefender choice — see [[no-sound-pack-support]]). Do NOT set `m.pack_file`; instead pass the helper's `audio_prefix` (point at `sounds/` and give each value its sub-path, e.g. `"equipment/weapons/artillery/pistol/fire.ogg"`), or `audio_prefix=""` with full relative paths in the values. Multi-variant sounds → `array<string>` value (helper randomizes).

## Mode mapping for the context clauses (shared-sound reality)
- **Wood** (oak/maple/birch/pine pickups, placements, bumps): PVE + free play (defenders).
- **Ammo** (arrow/gas/grenade/normal/powder): EVP + free play (attackers).
- **Weapons** (all kinds, melee + ranged): EVP + free play (attackers).
- **Walls** (wallwood/wallcrate/etc. hits, breaks, rebuilds): all modes.
- **Surfaces/platforms** (footsteps): all modes.
- **Ambience / Music / Interface (ui)**: all modes / menus.

## Final scope (dev-decided 2026-07) — "game-specific sounds only"
The throughline: teach sounds you hear INSIDE a round/arena (or that shape gameplay/navigation), NOT the shared social/server layer.

**IN:**
- **Equipment — all.** *Wood* (oak, maple, birch, pine), *Ammo* (arrow, gas, grenade, normal, powder), *Weapons* (ALL, one FLAT Weapons category — archery/crossbow, artillery/pistol+machinegun, explosive/cannon+firebomb+grenade, melee/axe+bat+crowbar+feet+fist+hammer).
- **Objects — partial.** *Surfaces* category = platforms **concrete, gravel, woodpile**. *Walls* category = **wallcrate, wallwood, wallwoodpile**.
- **Interface (from ui/misc only) — 10 curated cues:** buildprep, wavestart, wavestop, pause, resume, turn, beacon, joingame, lbrank, lbupdate.

**OUT (deliberately):** `ambience/`, `music/`, platforms carpet + marble, walls wallbuilding + wallgeneric, and the other 41 `ui/misc` files (chat, moderation, AFK, account/presence, voice, room-social, ping, toggles/flags, and the developer world-freeze cues — those two were **renamed `gamestart`→`worldstart` / `gamestop`→`worldstop`** to stop reading like round start/stop; `net.nvgt` refs updated). They're all "you're on a server with other people" sounds, not "what's happening in the cave."

**Working category list (6):** Wood, Ammo, Weapons, Walls, Surfaces, Interface. Wood and Ammo kept SEPARATE (opposite sides) rather than merged into one "Items" (dev didn't object). Each category = one flat list reached via a category picker → `learn_game_sounds_menu(sub-dictionary, prefix, m)`.

## Decided
- **Everything alphabetized — BOTH levels** (dev 2026-07). Category picker AND the sound names within each category sort ascending, so insertion order in code is irrelevant. Free from the design: `learn_game_sounds_menu` already `sort_ascending()`s the descriptions; the category picker sorts its keys `sort_ascending()` like ToyMania's `sortedKeys`. (Category display names are SINGULAR per dev polish — Ammo, Interface, Surface, Wall, Weapon, Wood — in that alphabetical order.)
- **Flat Weapons category** — every weapon's sounds in one list, no per-kind drill-down (matches ToyMania c8da4b1).
- **Multi-variant sounds:** build the `string[]` with a FOR-LOOP over the numbered files (like ToyMania's toyloop: `for(i=1..N) list.insert_last("name"+i+".ogg")`), and append `". This sound has multiple variants."` to the label AFTER the "used in … mode" clause. Requires each sound's variant count + consistent numbered naming (`name1.ogg`, `name2.ogg`, …).
- **Interface label phrasing (dev-decided 2026-07):** EVERY label carries a "used in …" clause (ToyMania style — the dev likes it). True game cues name the MODE: buildprep/wavestart/wavestop → "used in PVE and EVP", pause/resume → "used in any game". The five mode-AGNOSTIC cues name their CONTEXT instead, mirroring ToyMania's "Complete: used in speaker tests and various other menus". Draft clauses: **Turn** → "used when you turn to face a direction in place"; **Player beacon** → "used to locate other players around you"; **Join game** → "used when you join a game"; **Leaderboard climb** (lbrank) → "used when you move up a leaderboard"; **Leaderboard update** (lbupdate) → "used when another player moves up a leaderboard". (Bare-label option rejected — dev prefers the informative clause.)

## Sound inventory (enumerated 2026-07 — prep DONE, ready to build)
Paths relative to `cf/client/sounds/`. `audio_prefix = "sounds/"`, each dictionary VALUE carries its sub-path from there (e.g. `"equipment/weapons/artillery/pistol/fire.ogg"`). Every label gets a "used in …" clause (mode for gameplay, context for agnostic). Append ". This sound has multiple variants." ONLY to the numbered-variant entries (built by for-loop).

**Wood category** — `equipment/items/wood/{oak,maple,birch,pine}`, each kind identical: `take.ogg` (pick up), `place.ogg` (reinforce onto a wall), `drop.ogg` (piece drops onto the floor), `loop.ogg` (piece lying on the ground). All single, no variants. Clause: "used in PVE and free play".

**Ammo category** — `equipment/items/ammo/{arrow,gas,grenade,normal,powder}`, each: `take.ogg`, `drop.ogg`, `loop.ogg`. Single. Clause: "used in EVP and free play".

**Weapons category** (FLAT, ALL actions — dev 2026-07). Clause for all: "used in EVP and free play". Action → label word: draw="draw"; **fire = "fire" for ranged but "swing" for MELEE** (they swing, not fire); hit="hit" (strikes a wall); empty="empty" (dry fire, out of ammo); reload="reload"; ping="ping"/"reload ready" (the ready chime); loop="in flight"/projectile whizzing (bullets whizzing, arrows & shells flying); rico="ricochet" (shot/​swing didn't count — build or rest window); shell="shell casing" (hits the ground, GUNS ONLY).
  - **Melee** (`melee/{axe,bat,crowbar,feet,fist,hammer}`): `draw` (1), `fire1–3` (swing, 3 variants), `hit1–3` (3), `rico` (single).
  - **Explosive** (`explosive/{cannon,firebomb,grenade}`): `draw, empty, fire, hit, loop, ping, reload, rico` — all single.
  - **Archery** (`archery/crossbow`): same set as explosive, but `rico1–2` (2 variants).
  - **Artillery** (`artillery/{pistol,machinegun}`): `draw, empty, fire, hit, loop, ping, reload` + `rico1–12` (12) + `shell1–2` (2). The two guns are identical twins.
  - **RICO IS INCONSISTENT — branch per weapon:** melee & explosive = single `rico.ogg` (no variant note); crossbow = `rico1–2`; pistol/mg = `rico1–12` (for-loop). Don't blindly for-loop rico.

**Walls category** — `objects/walls/`: `wallcrate/bump.ogg` (single), `wallwoodpile/bump.ogg` (single), and `wallwood/` = `bump, death, burnstart, burning, burnstop` (single) + `hurt1–3` (3). Actions: bump (walking into it), hurt (struck/damaged), death (destroyed), burnstart (catches fire), burning (fire loop), burnstop (fire goes out). Clause: "used in all modes".

**Surfaces category** — `objects/platforms/{concrete,gravel,woodpile}`, each `step1–5.ogg` (5 variants). Footsteps — surface-based not mode-based, so a CONTEXT clause: "used when you walk on <surface>".

**Interface category** — `ui/misc/` 10 curated, all single: `buildprep, wavestart, wavestop, pause, resume` (mode clause) + `turn, beacon, joingame, lbrank, lbupdate` (context clauses — see the phrasing decision above for the exact drafts).

**Numbered-variant entries (for-loop + "multiple variants" note):** melee `fire1–3` & `hit1–3`, wallwood `hurt1–3`, surfaces `step1–5`, crossbow `rico1–2`, pistol/mg `rico1–12` & `shell1–2`. Everything else is a single file.

Related: [[game-mode-free.md]] name-drops this as the "future home" of learn-sounds; [[audio-and-sounds]] has the folder layout; [[no-sound-pack-support]]; [[launchers-and-running]] (cwd = `cf/client`, so `sounds/…` paths resolve there).
