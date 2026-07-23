---
name: internal-code-improvements
description: Internal (player-invisible) backlog from the 4.5 full-game review — remaining correctness/robustness bugs plus structural refactors/dedup (god-functions, ring-geometry copy-paste, taxonomy twins, duplicated helpers)
metadata:
  type: project
---

Player-invisible work from the full 360 review at v4.5 — nothing here changes what a normal player sees in the game, so none of it earns a changelog line (per [[changelog-rules]]). Two groups, numbered continuously so any item is unambiguous to pick. Fix one at a time and delete each entry as it lands (per [[delete-completed-tasks]]). Player-visible bugs (all cleared) live in [[user-facing-improvements]]. Line numbers were accurate at review time — re-locate by symbol if the file has shifted. Related: [[deferred-dedup-refactors]], [[include-tree]], [[command-parser-conventions]], [[networking-protocol]].

**Cleared in 4.6 (quick-wins pass):** copy_buffer_item bounds guard, the three result-handler token guards (roundover/pvpresult/evpover), the unchecked MOTD write, and the filterchar signed/unsigned compare. Removed below.

## Correctness & robustness (invisible in normal play)

**1. Menu-result branches with weak bounds-checking.** ~10 branches check only `choice < 0` (not the upper bound) then index by fixed literal / fall through ternaries; a malformed `menuresult` with a large positive `choice` isn't rejected. Low exploitability (client authoritative on its own menu) but a modified client could trip unexpected paths. — `server/menu.nvgt:1218, 1313, 1328, 1354, 1359, 1377, 1384, 1390, 1400, 1410`

**2. `enemy_attacks()` forward iteration with mid-loop removal.** When a bot's hit downs a wall, `remove_bots_on_wall` removes multiple `enemies[]` entries (possibly at indices ≤ `i`) inside a forward loop, so some bots are skipped that tick. Not a crash and imperceptible; convert to back-to-front if precise per-tick behavior ever matters. — `server/enemy.nvgt:153-177`

## Structural / refactors & dedup

**3. Server `netloop()` god-function, ~2,500 lines** (~114 `else if` branches, two coding dialects at a visible seam). Tracked baseline was ~1,450 → grown ~1.7×. Plan the dispatch-table split; freeze new commands into the old chain until then. — `server/net.nvgt:1035-3537`

**4. `on_menu_result` (~349 lines)** — one `if/else if` chain over ~35 menu ids, string-coupled to senders scattered file-wide; a typo in either half silently dead-ends a menu with no compile error. Extract per-menu handlers; hoist menu-id literals to shared consts. — `server/menu.nvgt:1100-1449`

**5. `gametick` (~161 lines)** concentrates the whole round state machine, including three near-copy PVE/EVP/PVP end-condition passes. Merge those into one mode-parameterized helper; split drop logic out. — `server/game.nvgt:812-973` (passes at `953-972`)

**6. Ring-wall geometry copy-pasted ~12×** across both binaries (`wmin=size/4; wmax=size-wmin` + four direction branches). Highest drift risk in the codebase — change the inset and audio silently desyncs from geometry. Extract one `wall_span(dir, …)` helper per side. — `server/wall.nvgt:62-67,117-123,131-138,144-151,158-163`; `client/wall.nvgt:49-63,78-91,124-138,158-172,199-212,236-249,276-280`; `client/bullet.nvgt:33-47`; `client/effect_space.nvgt:113`

**7. Cross-binary taxonomy twins.** Weapon id→name (server `enemy.nvgt:128-149` vs client `wall.nvgt:96-101` and `139-145`) and ammo types (server `item.nvgt:178-187` vs client `item.nvgt:12`) are parallel hard-coded literals; reorder one side and hits play the wrong sound / ammo routes to wood, with no error.

**8. Internal twin functions in server `game.nvgt`:** `pause_game`(671-686)≈`freeze_world`(726-736); `resume_game`(689-703)≈`unfreeze_world`(753-763); `leave_game`(303-348)≈`handle_disconnect_games`(435-474) (same removal cascade + host migration + play-again reset).

**9. Language/pronoun loader twins in `menu.nvgt`** are line-for-line: `load_language_channels`(660-685)≈`load_pronoun_options`(736-761); `is_valid_language`≈`is_valid_pronoun`; `language_bare`≈`pronoun_bare`. Collapse into one `load_svr_list(...)`.

**10. `rename_account`(271-280) ≈ `delete_account`(293-301)** share the ignore-list rescan loop. — `server/account.nvgt`

**11. Already-tracked debt, still unpaid** (in [[deferred-dedup-refactors]]): promote/demote twins (`server/net.nvgt:3062-3103` vs `3104-3145`) and client preset menus `addserver`/`addaccount`, `loadservermenu`/`loadaccountmenu` (`client/menus/menu.nvgt:318-680`). Decide pay-down vs. keep-deferring.

**12. Name the player-cap constant.** Bare `4` is repeated as the game player cap across `server/menu.nvgt:232,248,303,390,414` and `server/game.nvgt:390,414,777`; add `const int game_capacity = 4;` beside the existing `spectator_cap` and use it everywhere. Quick win.

**13. Hoist mode/phase/side string literals to named consts.** `"pve"/"evp"/"pvp"/"free"`, `"idle"/"build"/"wave"/"over"`, `"attack"/"defend"` are compared as raw strings dozens of times in `game.nvgt`; a typo silently misroutes. Change the *comparisons* only — emitted wire strings must stay identical across sides per [[networking-protocol]]. Quick win.
