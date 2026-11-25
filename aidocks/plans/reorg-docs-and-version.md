---
name: reorg-docs-and-version
description: "OPEN — the final docs/version section for the late-2026 reorganization (code into includes/game, sounds into main/ + game/, data/equipments, no more Enigma boxing): bump to 5.3, decide the changelog line, update the stale memories and CLAUDE.md. Runs LAST, after data-repointing, sound-path-repointing and build-tools-remove-boxing."
metadata:
  type: project
---

**Version:** bump `build/version.txt` to 5.3 with the changelog block ([[dont-touch-version-txt]]). Required, not cosmetic: [[sound-path-repointing]] changes network message paths, so a 5.2 client must be refused by the 5.3 server (the login version check does that).

**Changelog — 5.3 BLOCK WRITTEN 2026-11-24** (dev: "Please write it now. The build tools can wait untill after"): `New in 5.3.` at the top of cf/client/docks/changelog.txt with two entries, the merged sound-reorg + speaker line and the host-facing equipments line. The dev had already bumped build/version.txt to 5.3 themselves. The two boxing-removal lines were ADDED at the top of the block on 2026-11-24 once [[build-tools-remove-boxing]] landed, so the 5.3 block is now COMPLETE with 4 entries. Original decision: a 5.3 block, written at the END (dev: "update the change log at the end"), once every plan has landed, so it describes what actually shipped. The dev wants the sound reorg changelogged, as they did in StrideRush (its line 32: "Made it so the sounds folder is now split into a game folder, for the environments, weapons and items, and a main folder, for the game's own events, your own sounds and the menus."). Draft entries to finalize with the dev then ([[changelog-rules]]: 1 sentence default, player-facing, newest first, "New in 5.3." header, up to 10 lines):
- Sound reorg, MERGED with the new speaker sound (dev, 2026-11-24: "for the speaker sound, that can be merged with the sound reorg entry"; the dev deliberately replaced main/ui/menu/speaker.ogg): "The sounds folder is now split into a main folder, for the menus, dialogs, typing and the game's alerts, and a game folder, for weapons, items, walls, floors, ambience and music. The test speakers option in the main menu also plays a new sound."
- Candidate, host-facing: "The server's weapon and item files now live in a folder called equipments inside the data folder."
- After [[build-tools-remove-boxing]] lands: game sounds now ship as an ordinary folder beside the game instead of packed inside it; server hosts can now edit the help and rules pages (server docks ship loose).

**Stale rule to fix here:** [[changelog-rules]] still says never to edit version.txt; [[dont-touch-version-txt]] (2026-07, newer) supersedes it: bump version.txt with each new changelog block. Correct the changelog-rules line.

**Server docks** are in [[data-repointing]] section 3 (help/player.txt 51, 61, 63; help/staff.txt 77).

**Memories to update:**
- [[path-conventions]]: sounds main/ + game/ layout, data/equipments, includes/game, no boxing.
- [[include-tree]]: includes.nvgt now globs `game/*` FIRST, then main's deps/functions/globals(/menus/parsers on the client); the 10 moved files (client bot, burn, item, platform, wall; server burn, enemy, heal, item, wall) now live in includes/game.
- [[audio-and-sounds]]: new sound folder map.
- [[game-data-file-layout]]: data/equipments (also in data-repointing section 4).
- [[launchers-and-running]]: drop boxing, tools.py CLI is 4 flags, menu 1-10.
- Retire [[enigma-boxing]] and [[file-exists-boxed-sound-trap]] (boxing is gone; keep as short history notes or delete, dev's call), and fix CLAUDE.md's "Distribution boxing" line.

**Commit:** "Major dock enhancements." for the memory sweep ([[commit-style]]); the changelog/version as its own commit using the changelog entry text.
