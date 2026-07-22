---
name: game-mode-free
description: "As-built reference for Free Play, the 4th game mode (solo/open sandbox) — BUILT and feature-complete across 4.4a-e, shipped whole in the 4.4 batch"
metadata: 
  node_type: memory
  type: project
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
  modified: 2026-07-21T00:37:00.898Z
---

**Free Play** is CaveDefender's 4th game mode, a **solo/open sandbox** — shipped whole in version **4.4** (its flagship). **BUILT and feature-complete across 4.4a-e** (mode plumbing, dual toolkit, cavern controls, open version, docs); this file is now the as-built reference, like [[game-mode-evp]] / [[game-mode-pvp]]. Mode string is **`"free"`** (4th value beside `pve`/`evp`/`pvp`). Tested end to end 2026-07. Key server pieces: `free_wall_down`/`schedule_wall_heal`/`heal_tick` (self-heal, heal.nvgt), `add_free_bots`/`spread_free_bots` (enemy.nvgt), `add_free_items`/`clear_items_broadcast` (item.nvgt), `reset_free_cavern` + `game_joinable` (game.nvgt), the cavern menu cascade (menu.nvgt), and the `enablewalldamage`/`cavernbotcount`/`cavernitemcount`/`cavernbots` handlers (net.nvgt); client `rebuild_wall_client` + the `cavernreset`/`wallrebuilt` handlers.

**Identity / what it deliberately lacks:** no round timer, no score, no win/loss, no wave escalation, **no persistence** (never touches wins.usr / best-round). Solo-only in v1; an **Open** version is a separate later section (4.4d). It's also the natural future home for the learn-sounds idea ([[form-menu]]'s `learn_game_sounds_menu`) and a practice space for new players.

**The one big risk (from the code map):** an unrecognized `mode` string **silently falls into the PVE `else` branches** everywhere (`set_game_phase` build/wave, `gametick` cycle-flip + resolution passes, `gather_wood` which only early-returns for EVP). And the client gates roles off **`game_outside`** (a binary EVP "attacker/outdoor" flag), NOT off mode — weapons on when `game_outside`, wood on when `!game_outside`. Free is NEITHER, so both sides need explicit `mode=="free"` handling, and 4.4b must re-express those client gates as `can_attack`/`can_defend` derived from mode (PVE=defend, EVP=attack, PVP=by side, FREE=both).

## Naming & placement (LOCKED)
Player-facing label is **"Free play" (two words)** everywhere (menu item + all text); the internal mode id/token is the single word **`"free"`** (wire messages, `mode=="free"` checks). It's listed **LAST** in the game-mode menu — after EVP, PVE, PVP — since it's the sandbox/practice mode, not a competitive one (keeps the three core modes together at the top).

## Build workflow (LOCKED)
Each of the five sections (4.4a-e) is built in **sub-sections reviewed one at a time** — build one slice, report it, wait for the dev's review before the next. Don't dump a whole section at once.
- **Free Play changelog: HELD to the very END (the 4.4e docs pass), then written as SEVERAL entries covering the whole finished mode** — NOT per section as we go. Reason (dev's call): the mode is one feature spread across sections; a per-section entry would announce half-built plumbing (e.g. an empty cavern with nothing to do). At 4.4e, write a few player-facing entries organized by what a player experiences — e.g. "Free play mode added" (what it is + how to start it), the arena (Begin arena / Enable wall damage / ricochet-until-live), cavern controls (spawn bots, add wood/ammo, clear/reset), and self-healing walls. Tune the split to what's actually built. (Independent, self-contained fixes still get their own immediate entries — that's unchanged; only the Free Play feature is deferred.) 4.4 is unreleased, so all of it goes in the changelog per [[release-cadence-batches-versions]].
- **README is saved for the very END,** after every section is built — so 4.4e's docs pass is really "readme (+ help/todo) last," since the changelog is already done incrementally by then.
- Sub-section split for 4.4a: **4.4a.1** mode entry + empty cavern (DONE), **4.4a.2** arena lifecycle (arena menu / Begin arena / free idle→active phase machine + mode guards) (DONE). **4.4a.3 was FOLDED FORWARD** (both pieces are untestable until walls can be destroyed): the **ricochet-lock flag → start of 4.4b** (weapons honor it), **self-healing walls → 4.4c** (built with the wall-destruction paths so it can actually be watched healing). So **4.4a is COMPLETE at .1 + .2.**
- Sub-section split for 4.4c (5 slices): **4.4c.1** Enable wall damage (arena-menu one-way item flips `free_wall_damage`; unify the wall-DOWN path via a `free_wall_down(gi,dir)` helper called by BOTH the swing branch and `resolve_bullets`; send `walldestroyed` + the "gone down" alert; permanent debris for now). **4.4c.2** Self-healing walls (rebuild ~10s later at fresh random 50-100% + client re-tile-back-to-wallwood message + the "come back up" alert). **4.4c.3** Cavern controls: bots (Tab menu framework replacing the "coming soon" stub; Add cavern bots count→wall→spread, Clear cavern bots, B locator for free bots). **4.4c.4** Cavern controls: items (Add cavern items type→kind→count vs the per-category ground budget, Clear cavern items). **4.4c.5** Clear cavern map (wipe bots+items, reset walls to a fresh roll, re-lock damage, weapon→axe).
- Implementation notes discovered: the free active phase is the string **"active"** (set by `set_game_phase(gi,"active")`); it falls through every `gametick` guard, so no `mode=="free"` guards were needed there. Client walls are NOT tracked objects — `destroy_wall_client(dir)` re-tiles a breach span to `woodpile` (PVE/EVP) / `wallwoodpile` (PVP); so self-heal's client side must re-tile the span back to the `wallwood` tile via a new "wall rebuilt" message + resync health. Server wall rebuild = set `walls[wi].health = wall_start_health(...)` (random 50-100%) after a ~10s timer, broadcast wallstr + the "come up" alert; broadcast the "gone down" alert on destruction.

**4.4b.3 done (free swing/fire ricochet):** the server "attack" swing handler (net.nvgt ~1508) has a `mode=="free"` branch, the "fire" handler + `resolve_bullets` (bullet.nvgt) include free via `game_active_play` + attacker-OR-free, and the fire `window` = `free_wall_damage` for free. While `free_wall_damage` is false (all of 4.4b), every free swing/shot RICOCHETS. **4.4c FOLLOW-UP when Enable wall damage flips `free_wall_damage` true:** the wall-DOWN path differs by weapon — the swing free branch sends `walldestroyed <dir>` directly, but the damaging BULLET path (`resolve_bullets` ~line 52-53) falls into the `else on_wall_destroyed(...)` (the PVE/EVP bot-redistribute+announce). 4.4c must give BOTH paths a unified free wall-down handler that triggers the self-heal timer + the "gone down" alert (and decides what free's attacker bots do when their wall drops — likely just re-target, since it heals back).

## Start flow
Free play → **Choose who can play** (Solo works / **Open says "coming soon"** and backs out — the menu shows Open as a stub so wiring real Open later just swaps the stub) → **map size** (25/50/75/100) → placed in the cavern, arena NOT started.

## Arena (map)
Reuses the PVE interior verbatim: `draw_map("cavern")`, `game_outside=false`, four `wallwood` **border** walls (`spawn_border_walls`, keep the hardcoded 4-wall model — never touch WALL_DIRS/geometry), interior reverb. Walls roll **random 50–100%** on load AND again each time one **self-heals** (see below). Reinforce is **uncapped**.

**Self-healing walls (dev decision):** a wall destroyed to 0 **auto-rebuilds ~10 seconds later** (fresh random 50–100%), never permanent debris — so a solo player is never left with nothing to smash. Re-tiles back via the same `spawn_platform` overwrite the death re-tile uses. **Alert everyone in the game on both transitions,** naming the direction (LOCKED wording): on destruction "**The `<dir>` wall has just gone down.**" and on rebuild "**The `<dir>` wall has just come back up.**" ("back" signals the same wall rebuilding, not a new one). Broadcast to all members (and watchers) of that free game.

**Always INSIDE the cave — Free sits on the PVE side of every inside/outside fork (verified client net.nvgt):** `game_outside=false` always. Line 1417 shows only EVP flips outside (`game_outside = (parsed[4]=="evp")`) — EVP is the outdoor-gravel mode; Free is indoor like PVE. **Watching Free Play = watching PVE:** the spectate deck flag (line 1501, `game_outside = (parsed[4]=="out")`, "PVE/EVP fixed by mode") — the server sends **"in"** for Free, so watchers get the **indoor concrete overhead deck** (cavern2 + spectate_height), NOT EVP's outdoor gravel deck. So 4.4a's gamejoined/spectate branches must treat `mode=="free"` as indoor (`game_outside=false`, deck flag "in").

## Two keys: Enter = arena lifecycle, Tab = populate/clear
**The dev's rule: "Enter = the state of the arena, Tab = the stuff in it."** Enter mirrors the existing round menu (`push_game_menu`), which is already the host's live-game control surface (Begin round / Invite / Kick — confirmed menu.nvgt:350-386).

**Enter — Arena menu (renamed from "round menu"):**
- Before Begin arena: **Begin arena** (solo). Open (later): host options.
- After Begin arena: **Enable wall damage** is the FIRST item (the slot Begin round used to fill), → reads **"Wall damage enabled"** (informational) once used. In Open, kick/invite list BELOW it.

**Tab — Cavern controls (populate/clear console):**
- Before Begin arena: says **"The arena hasn't started yet."** (gated — populate only after the arena is live).
- After Begin arena, the list (order matters):
  1. **Add cavern bots**
  2. **Add cavern items**
  3. **Clear cavern bots**
  4. **Clear cavern items**
  5. **Clear cavern map**

## The ricochet lock (reuses EVP build→wave machinery)
Weapons ricochet off walls (the `wallrico` feedback via `play_wall_rico`, NO damage) — like EVP's build phase — until the player opts in. Flow:
- **Begin arena ENGAGES the lock** (weapons ricochet; this is your setup window — gather ammo/wood, spawn bots/items, position). Bots you spawn attack the walls; only the PLAYER's own weapons are locked to ricochet.
- **Enable wall damage** (Enter menu) LIFTS it — your weapons now damage walls (`play_wall_hit`). **One-way: can't be turned off** once on (a flip-flop toggle would make it ambiguous whether hits are landing). Reads "Wall damage enabled" afterward.
- **Clear cavern map RE-LOCKS** damage (fresh safe slate).

So the lifecycle end-to-end: enter free play (not started) → Enter → **Begin arena** (armed, ricochet, Tab unlocks) → gather/spawn/set up → Enter → **Enable wall damage** (weapons damage) → **Clear cavern map** re-locks + resets everything.

## Both toolkits live at once
The defining feature: every weapon (melee + ranged) AND the wood/reinforce kit are enabled together (first mode where attack + defend keys both work). Ranged weapons feed on **gathered ammo** — NO unlimited ammo (the dev + I agreed the gathering loop, homing on drops by their audio, moving between ammo pile and wall, IS the fun in an audio game; unlimited flattens it to standing still). A later controller toggle for unlimited-ammo aim-drills was floated but not planned.

## Cavern controls — the two picker cascades
**Add cavern bots** (attacker bots only — dev cut builder bots to de-clutter; they're the only positional bot, the wood-competition source, and redundant in a solo practice space where you're the defender):
1. input box **"How many attacker bots?"** (UNLIMITED — enemies are abstract/positionless, no map cost; a quiet sanity ceiling only)
2. wall target menu: **North wall / East wall / South wall / West wall / All walls**
3. IF All walls → spread menu with DYNAMIC numbers in the labels: **"Spread all N across the walls"** (N total, even-spread) / **"Put N on each wall"** (N×4 total)
Bots always roll one of the **4 melee weapons** (axe/bat/crowbar/hammer) — reuse PVE `spawn_enemy` + `fill_walls_to` even-spread. No ranged/fist bots.

**Add cavern items:**
1. **What item?** → Ammo / Wood / **Both**
2. kind picker: Ammo → **Arrow / Gas / Grenade / Normal / Powder / All ammo**; Wood → **Birch / Maple / Oak / Pine / All wood**; **Both skips the kind picker** straight to the count (drops a mix of random wood + random ammo)
3. input box **"How many?"**
NO third spread menu (unlike bots) — items scatter to random floor tiles against ONE shared per-category budget, so "per target" is meaningless. The number is ALWAYS a **total against the category budget, spread across kinds** (e.g. "All ammo, 30" = 30 ammo total, mixed kinds; "Arrow, 30" = 30 arrows against the same shared ammo budget), clamped to the map-size ceiling.

**Cap facts (verified in code, item.nvgt / gamedata.nvgt / conf.gvr — external config matches built-in defaults):** the ground cap is **per CATEGORY, not per kind** — `wood_count_in` counts all 4 wood kinds vs one ceiling, `ammo_count_in` counts all 5 ammo kinds vs another. Caps by size: **6 / 18 / 28 / 40** at 25 / 50 / 75 / 100, one wood budget + one ammo budget each. (Wood kinds matter: oak reinforces most, pine least — so a kind picker isn't purely cosmetic. Ammo kinds are weapon-specific: arrow=crossbow, powder=cannon, gas=firebomb, grenade=grenade, normal=pistol+machinegun.)

**Clear cavern bots / Clear cavern items** — immediate, split (wipe attackers to breathe while keeping items, or vice versa).
**Clear cavern map** — wipes bots + items, resets walls to a fresh random roll, re-locks wall damage, and sets your weapon back to the **axe** — as if freshly started.

## Build order (dev commits each slice as we go; changelog per [[changelog-rules]])
- **4.4a** — mode plumbing: register `"free"` through the menu cascade + validated mode set (net.nvgt startgame) + `mode_tag` + client labels (net.nvgt gamejoined/mode-label spots); who-can-play menu with Open stubbed; arena menu + Begin arena; the idle-ricochet→active-damage lock; empty cavern; full-wall readouts; self-heal. Explicit `mode=="free"` guards in every `set_game_phase`/`gametick` fork so it doesn't inherit PVE defaults.
- **4.4b** — dual toolkit: the `can_attack`/`can_defend` client refactor; ungate `gather_wood`/`gather_ammo`/`reinforce` for free; arming. **PLUS the ricochet-lock state flag** (folded from 4.4a.3): a game field (e.g. `free_wall_damage`, default false = locked) that the weapon-damage code honors so free weapons only ricochet until it's lifted; 4.4c adds the control that lifts it.
- **4.4c** — Cavern controls: bots + items pickers, clears, reset; the Tab gate. **PLUS self-healing walls** (folded from 4.4a.3): a destroyed free wall rebuilds **~10s** later at a fresh random 50-100% (server timer + a client re-tile-to-wallwood message), built here because this is where walls can first be destroyed (Enable wall damage + attacker bots) and thus tested. Broadcast an alert to everyone in the game on both transitions: "The `<dir>` wall has just gone down." / "The `<dir>` wall has just come back up."
- **4.4d** — the **Open version**: host-controlled — ONLY the host spawns/clears (guests just play in the sandbox the host sets up); real Open replaces the 4.4a stub; kick/invite in the arena menu.
- **4.4e** — dock/doc changes: readme, help, changelog, todo.
