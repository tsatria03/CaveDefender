---
name: data-repointing
description: "OPEN — point the server at the renamed data/equipments folder (was data/equipment, renamed by the dev 2026-11-23). Four sections + one optional; until section 1 lands, the server silently plays on code-default weapon/item values."
metadata:
  type: project
---

**Context:** the dev renamed `cf/server/data/equipment` to `cf/server/data/equipments` (21 files, contents unchanged, committed in c76e74d "Major server data enhancements."). `gamedata.nvgt`'s `read_kv()` returns false on a missing file and each loader just returns, so callers fall back to code defaults (damage 1, wood reinforce 10-20, ammo starter 5-10...). Nothing crashes and no files are written. Every other data path (players, preffs, client data/scriptkeys.srk, docks) was checked and still matches.

**Section 1 — the loader (the actual fix). DONE 2026-11-24** (all 21 roster paths verified to exist under cf/server/data/equipments; awaiting the dev's in-game check). `src/server/includes/main/globals/gamedata.nvgt`: line 122 `data/equipment/weapons/` → `data/equipments/weapons/`; line 159 `data/equipment/items/wood/` → `data/equipments/items/wood/`; line 174 `data/equipment/items/ammo/` → `data/equipments/items/ammo/`. Relaunch the server. Verify: no `"data/equipment/"` left in src/server; in game, melee damage, wood reinforce and starting ammo match the data files.

**Section 2 — comments only. DONE 2026-11-24** (0 `data/equipment` mentions left anywhere in src). gamedata.nvgt lines 3-4 (header), `cfs.nvgt` line 110, `game/enemy.nvgt` line 123, `game/item.nvgt` lines 125, 147, 175, 199.

**Section 3 — server docs (final section per [[final-section-dock-updates]]).** `cf/server/docks/help/player.txt` lines 51 ("under data/equipment"), 61 (`data/equipment/weapons`), 63 (`data/equipment/items`); `cf/server/docks/help/staff.txt` line 77 ("in the equipment folder" → "equipments folder"). Line 75's "the equipment data files" describes files, leave it. Rules pages need nothing. Stay under 1024 chars per line ([[dock-line-length-1024]]).

**Section 4 — memories. DONE 2026-11-24** (game-data-file-layout now has a CURRENT PATHS line + history; ranged-weapon-architecture and the index line corrected; also fixed the stale "4 ammo types" to 5). [[game-data-file-layout]] (3 mentions), [[ranged-weapon-architecture]] (1), and the MEMORY.md index line.

**Optional — missing-file warning.** Print one console line at boot for each data file not found, so a future rename can't silently fall back to defaults. New behavior; only if the dev wants it.

Line numbers were checked 2026-11-24; re-locate by text if files moved ([[verify-code-while-fixing]]). Commit style: [[commit-style]].
