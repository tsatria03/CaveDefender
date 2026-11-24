---
name: reorg-docs-and-version
description: "OPEN — the final docs/version section for the late-2026 reorganization (code into includes/game, sounds into main/ + game/, data/equipments, no more Enigma boxing): bump to 5.3, decide the changelog line, update the stale memories and CLAUDE.md. Runs LAST, after data-repointing, sound-path-repointing and build-tools-remove-boxing."
metadata:
  type: project
---

**Version:** bump `build/version.txt` to 5.3 with the changelog block ([[dont-touch-version-txt]]). Required, not cosmetic: [[sound-path-repointing]] changes network message paths, so a 5.2 client must be refused by the 5.3 server (the login version check does that).

**Changelog (OPEN QUESTION to the dev):** most of the reorg is invisible to players. The likely single entry: game sounds now ship as an ordinary folder beside the game instead of packed inside it. Server hosts can also now edit the help and rules pages, since server docks ship loose. Dev decides wording and whether each earns a line ([[changelog-rules]], [[post-changes-no-changelog]]).

**Server docks** are in [[data-repointing]] section 3 (help/player.txt 51, 61, 63; help/staff.txt 77).

**Memories to update:**
- [[path-conventions]]: sounds main/ + game/ layout, data/equipments, includes/game, no boxing.
- [[include-tree]]: includes.nvgt now globs `game/*` FIRST, then main's deps/functions/globals(/menus/parsers on the client); the 10 moved files (client bot, burn, item, platform, wall; server burn, enemy, heal, item, wall) now live in includes/game.
- [[audio-and-sounds]]: new sound folder map.
- [[game-data-file-layout]]: data/equipments (also in data-repointing section 4).
- [[launchers-and-running]]: drop boxing, tools.py CLI is 4 flags, menu 1-10.
- Retire [[enigma-boxing]] and [[file-exists-boxed-sound-trap]] (boxing is gone; keep as short history notes or delete, dev's call), and fix CLAUDE.md's "Distribution boxing" line.

**Commit:** "Major dock enhancements." for the memory sweep ([[commit-style]]); the changelog/version as its own commit using the changelog entry text.
