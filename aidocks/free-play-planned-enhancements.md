---
name: free-play-planned-enhancements
description: Agreed design decisions for the UNBUILT Free Play / cavern-controls todo items (parity fixes + cavern-control spawn prompts) — not yet implemented; delete each note as it ships
metadata:
  type: project
---

Design decisions agreed with the dev for the unfinished Free Play todo items (`cf/client/docks/todo list.txt`), captured before implementation. The as-built Free Play reference is [[game-mode-free]]; delete each note here as it ships. Companion to that mode's cavern-controls cascade (`menu.nvgt`) and the `add_free_bots`/`add_free_items` server pieces.

**BUILT in 4.6 — item 1 (open free-play needs 2+ to start).** Added the `!games[gi].solo and games[gi].members.length() < 2` guard to the `beginarena` handler (`server/net.nvgt`), message "You can't begin an arena with yourself." Changelog'd. Done.

**BUILT in 4.6 — item 2 (pause free play).** Extended the `openpausemenu` gate (`server/net.nvgt`) to include free's `"active"` phase, and added heal-clock freeze/thaw to `pause_game`/`resume_game` (`game.nvgt`) so a breached wall's self-heal doesn't complete during a pause (the clock kept running before — pause_game didn't touch it). Client already sends `openpausemenu` + handles `gamepaused` mode-agnostically, so server-only. Changelog'd. Done.

**Add builder bots to cavern controls (todo).** Reuse `spawn_builders(gameid, count)` (`builder.nvgt:40`) — builders roam and auto-target the weakest standing wall, so NO wall picker; the menu just asks **"how many builder bots?"**.
- **Count cap: 100** (match the free-play attacker-bot ceiling at `net.nvgt:2171`).
- **Gated on ground wood:** builders carry *ground* wood to walls, so they can't be added until there's wood on the ground to pick up. Let the host type a count, but refuse to spawn if no ground wood exists, with a message like **"You need wood on the ground before builder bots can be added."**
- **Reinforce cap: 400%** (`wall_overbuild_cap = 4.0`, `wall.nvgt:91`) — pass that as the `repair_wall` capmult so free-play builders keep building instead of stalling at EVP's round-0 150%. Confirmed by dev.
- **B key:** once builders exist in free play, **B locates the builder bots in 3D** (reuse EVP's `track_bots` path), REPLACING the current free-play B behavior (`client/game.nvgt:288`) which sends `cavernbots` for a per-wall attacker-bot tally. B ONLY reports builder positions.
- **Attacker-bot tally moves into the "Clear attacker bots" option:** invoking Clear attacker bots (from cavern controls) **appends the per-wall attacker-bot summary at the end** (e.g. north/east/south/west counts, the old `cavernbots` output). Applies to both host (clear-all) and guest (clear-N) paths, so everyone can still read the per-wall bot spread — just from the clear option now, not the B key.

**Cavern-controls spawn prompts — exact wording (todo: continuous item spawning + bots on wall recovery).** The cavern-controls menu should ask these two questions verbatim:
- Continuous item spawning: **"Do you want these items to spawn continuously?"**

**Item 5 full spec — continuous item spawning (the toggle above).** Asked after the add-items flow (category → kind → count → this Yes/No). Uses `add_free_items` (`item.nvgt`), which already clamps to the per-category ground cap (`wood_cap`/`ammo_cap` by size).
- **Yes (maintain a level — option A, confirmed):** keep the typed count of that category/kind on the ground; as players pick items up, respawn to top back toward that count, bounded by the ground cap. Multiple continuous rules can be active at once, tracked per category/kind (e.g. continuous arrows AND continuous oak). Needs per-game storage of the active rules + a maintenance check on a tick.
- **No:** one-time drop (today's behavior).
- **Stopping:** the EXISTING "Clear cavern items" action (`menu.nvgt:438` → `clear_items_broadcast`, `item.nvgt:267`) must ALSO cancel all active continuous-spawn rules for the arena, not just despawn the ground items — otherwise a clear would instantly respawn. Dev's call: clear = despawn everything + stop all continuous spawning. No separate "stop continuous" menu entry.
- Attacker bots re-spawning when a downed wall is rebuilt: **"Do you want these bots to spawn upon wall recovery?"**

**Item 4 full spec — bots on wall recovery (the toggle above).** Asked at the END of the add-attacker-bots flow (pick wall or all → count → this Yes/No). Remembered **per wall** with that wall's count. This makes the assault perpetual-or-one-time and CHANGES today's default (free-play bots are currently always kept and resume after a recovery = effectively always "Yes"):
- **Yes:** the wall gets a standing rule — every recovery, respawn it back up to its count and keep attacking. During the breach itself, keep the current behavior (bots idle while the wall is down, then resume on recovery, topped back up to the count) rather than despawn/respawn — same visible result, less churn.
- **No:** when the wall falls, its bots leave and do NOT return when it recovers (one-time assault).
- "Same count for that wall or walls" — if applied to All, each of the four walls remembers its own count and the toggle.

**Item 6 full spec — guests can access cavern controls (add freely; clear only bots, and only partially).** Today `do_cavern_action` (`menu.nvgt:445`) gates EVERY action host-only (line 449). Relax to per-action. What each existing clear does (for reference): `clear_enemies` wipes ALL attacker bots; `clear_items_broadcast` wipes ALL ground items; `reset_free_cavern` (Clear map) is a full arena reset — wipes bots+items, cancels self-heals, drops in-flight bullets, stops wall fires, rolls all four walls to a fresh 50-100%, resets the host's ammo, and disables wall damage.

Guest vs host access:
- **Add attacker bots / builder bots / items:** guest-accessible (the additive actions).
- **Clear attacker bots / clear builder bots:** guest-accessible but with a **"how many?" count prompt** — indiscriminate (remove the first N found), **capped at 100** per action (the same ceiling as spawning them). The **host** clears these fully with **no prompt** (clear-all, today's behavior). Builders use `clear_builders`; attackers use `clear_enemies` — both need a "remove up to N" variant for the guest path.
- **Clear items:** **HOST-ONLY, no guest option.** (The ground cap is only 6-40 by size, so a guest "clear N items" would just be clear-all anyway — not worth a guest entry.)
- **Clear map (full reset) + Enable wall damage:** **HOST-ONLY** (destructive/global; a full reset is all-or-nothing so no count prompt).
- **UX:** the cavern menu shows guests only their allowed entries (add ×3, clear attacker bots, clear builder bots); host-only entries appear only for the host (same conditional-option pattern the room/game menus use).

All six Free Play todo items (1 open-start guard, 2 pause, 3 builder bots, 4 bots-on-recovery, 5 continuous items, 6 guest cavern access) are now SPEC'D above and agreed — awaiting a build pass, built one by one. The two broader todo items — **server-wide leaderboard and learn-sounds mode for EVP/PVE — are SKIPPED** for now (dev's call 2026-07; don't re-raise them as open). Build order note: items 3, 4, and 6 all touch the cavern-controls menu (item 6 + 3 add a new "Clear builder bots" action), so doing those together is cleanest.
