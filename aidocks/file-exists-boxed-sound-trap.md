---
name: file-exists-boxed-sound-trap
description: "file_exists() reads FALSE for sounds embedded in the Enigma-boxed client, so gating sound playback behind file_exists silently kills that sound in release builds; bullet travel loop fixed, shell casings + item ground loops still pending"
metadata: 
  node_type: memory
  type: project
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
  modified: 2026-07-18T21:28:57.459Z
---

In the release client, sounds are embedded into the exe by Enigma Virtual Box ([[enigma-boxing]]). `play_3d`/the sound loader read those embedded files fine through the virtual filesystem, but **`file_exists("sounds/...")` returns FALSE** for them (it checks the real disk, where the file isn't present). So any `if(file_exists(soundpath)) play(...)` pattern **silently drops that sound in the boxed build** while unguarded sounds around it still play. This is why the ranged bullet travel loop "didn't play at all" — it was the only bullet sound behind a `file_exists` guard (fire/impact had none). Fixed 4.1 by removing the guard (client `globals/bullet.nvgt`, `add_client_bullet`), and moving the loop onto its own `bulletpool` ([[audio-and-sounds]]).

**Why:** SimpleFighter never hits this because it loads via sound packs (`get_pack_sound`); CaveDefender loads loose files ([[no-sound-pack-support]]) and someone added `file_exists` for placeholder tolerance ([[sound-placeholders]]) — which is exactly the boxed-FS trap.

**How to apply:** Never gate sound PLAYBACK behind `file_exists`. Play directly (a genuinely missing file just fails into an invalid slot the move/destroy calls ignore). For true feature-detection ("does this weapon/item have this optional sound?"), use a boxing-safe check — play then verify the slot actually loaded (handle non-null / `sound_is_active`), or a data-driven flag from the weapon/item data — NOT `file_exists`. (`file_exists` is still fine for real on-disk files like settings.cvf / save files.)

All three known sound victims were fixed in 4.1:
- Bullet travel loop — guard removed, plays directly, moved to its own `bulletpool`.
- Item ground loops (client `globals/item.nvgt`, `clientitem` ctor) — every item type (4 wood species + 5 ammo kinds) now has a `loop.ogg`, so the guard was dropped and it plays directly.
- Shell casings (client `globals/wall.nvgt`, bullet hit + ricochet) — only the guns eject shells, so this is real feature detection; swapped `file_exists(shell1.ogg)` for a boxing-safe CLASS check, `weapon_class(wname)=="artillery"` (true for pistol/machinegun exactly). This is the pattern to reuse for "does this weapon/item have this optional sound?" — a data/class flag, never file_exists.

**One unresolved file_exists worth verifying:** client `functions/extrafuncts.nvgt` ~line 280 guards OPENING a dock file with `if(!file_exists(filename))` -> "Could not find" alert. Docks are ALSO boxed, so if this trap applied uniformly docks would fail to open in release. They apparently DON'T fail, which hints file_exists may behave differently for docks than sounds (or the dev tests unboxed) -- not yet confirmed. Left as-is (it has a legit error fallback); flag if a dock ever errors "Could not find" in a release build.
