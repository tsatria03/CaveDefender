---
name: data-reorg-repointing
description: "PLANNED (2026-11-25) — repoint the server and build tools and update docks after the dev's data reorg: server data/ split into host/ (server-only: players, main .svr settings) and config/ (game rules: equipments, modes.ini, effects.ini); the client gained a config/ copy of the game rules for offline play; ini comments switch from # to ; (reader accepts both). Client scriptkeys.srk stays at the data root. 3 sections: server, build, docks."
metadata:
  type: project
---

**Why:** the dev reorganized both data folders on 2026-11-25 ("I did a reorg of the entire client and server ... We'll also need to repoint paths again"), partly to prepare for the offline menu (see [[online-menu]]; offline design still being discussed). Every moved file was checked: identical content, only CRLF differs from git's stored copy. src/ and sounds/ were not touched. The dev committed the reorg as b85ae0b (verified: no player data in it).

**Path map (old -> new):**
Server (cf/server/data):
- `players/` -> `host/game/players/`
- `preffs/main/*.svr` (chatfilter, conf, languages, motd, peak, pronouns; plus the runtime-written feedback.svr, reports.svr) -> `host/main/*.svr`
- `preffs/game/conf.gvr` -> `config/main/modes.ini` (same content, new name)
- `preffs/game/effects.gvr` -> `config/main/effects.ini` (same content, new name)
- `equipments/` -> `config/game/equipments/`
Client (cf/client/data):
- `scriptkeys.srk` stays at the data root, unchanged. (The dev briefly moved it to `config/main/scriptkeys.ini`, then moved it back on 2026-11-25: "the script keys, which by the way I decided to move back to the root of the data folder". Same content. So no client code changes.)
- new: `config/game/equipments/`, `config/main/effects.ini`, `config/main/modes.ini`, byte-identical copies of the server's, for offline play. No client code reads them yet.

**Already done (2026-11-25):** .gitignore covers `cf/server/data/host/game/players/` and `host/main/feedback.svr` / `reports.svr` (the old-path rules are kept until section 2). Git saw 1183 player files before the fix and 0 after.

**Hazard until section 1 is done:** don't run the server. cfs.nvgt creates `data/players` and `data/preffs/main` on startup, so it would start with an empty account store and no owner (the real data is untouched, but the old folders come back).

**Sections:**

1. **Server code (server).** Repoint every data path string:
   - cfs.nvgt: the startup folder creation (lines 20-23: create `data/host`, `data/host/game`, `data/host/game/players`, `data/host/main`, and `data/config` as needed), conf.svr reads (25-27, 133), motd.svr (98-106).
   - account.nvgt (21, 24, 26, 175, 367, 372, 399), net.nvgt (players 250/779/817, peak 121-133, reports 166-181, feedback 210-225, motd 3472), menu.nvgt (players 1355/1383/1443, languages 830-836, pronouns 906-912), filterfuncts.nvgt (chatfilter 42-44): to `data/host/...`.
   - gamedata.nvgt: weapons 122, wood 159, ammo 174 to `data/config/game/equipments/...`; effects 303 to `data/config/main/effects.ini`; conf 324 to `data/config/main/modes.ini`.
   - gamedata.nvgt's reader (line 42 skips blank lines and lines starting with `#`; the header comment at line 9 states the format): skip lines starting with `;` OR `#` (dev: accept both), and update the header comment.
   - menu.nvgt `is_onoffs_path()` (1571): it matches `players/<user>/onoffs` by position under the data root, so it must now match `host/game/players/<user>/onoffs` (onoffs at segment index 4). Without this the editdata browser would open the binary .ogg clips. Its comment and push_data_nav's "only three levels deep" comment get updated.
   - The editdata/viewdata root stays `data/`, so staff now see `config` and `host` at the top.
   - Code comments naming the old paths (server dec.nvgt, game.nvgt, item.nvgt, enemy.nvgt, heal.nvgt, etc.), checked by a final grep for `preffs`, `data/players`, `data/equipments`, `.gvr`, which must come back with nothing.

2. **Build tools (build).** tools.py `sanitize_server_bundle()`: empty `data/host/game/players` (150-155), blank the owners in `data/host/main/conf.svr` (156-170), delete feedback/reports/peak from `data/host/main` (171-175), reset `data/host/main/motd.svr` (176-179), and update its comments. Until this is done, a release build would ship the real player accounts in the server archive. The client already ships its whole data/ folder (`CLIENT_ASSETS`), so config/ goes with it. Then remove the three old-path .gitignore rules.

3. **Docks (docks).**
   - The ini comments: change the leading `#` to `;` on every comment line of modes.ini and effects.ini, in both cf/server/data/config/main and cf/client/data/config/main (keep the two copies byte-identical). The equipment files have no comments.
   - Server help/player.txt lines 51-69 (the hosting/data-files section): new folder names, modes.ini and effects.ini instead of conf.gvr and effects.gvr. Check help/staff.txt's /editdata text (71, 80) for path wording.
   - Client readme: a new section explaining the server's ini files (data/config/main beside the server): what modes.ini and effects.ini each hold, and that `;` starts a comment. Not the script keys (dev, 2026-11-25: "minus the script keys"). The client's copy is described later, in the offline plan (see the Q&A log).
   - Client changelog: fold into the unreleased 5.3 block, rewording the existing "The server's weapon and item files now live in a folder called equipments inside the data folder." entry to describe the new layout ([[changelog-rules]]).
   - Memories: [[path-conventions]], [[game-data-file-layout]], [[accounts-system]], [[include-tree]] if it names paths, CLAUDE.md's accounts line, and the other memories the grep finds; mark this plan COMPLETE.
   - Recheck every edited dock line against [[dock-line-length-1024]].

Sections 1 and 3's ini comment change go in together before the server is run: the new reader accepts both `#` and `;`, so section 1 alone is safe, but the converted `;` comments need section 1's reader.

**Note for the offline plan:** the game rules now exist twice in the repo (cf/server/data/config and cf/client/data/config), so a balance change has to be made in both or they drift. The offline plan also owns the readme's description of the client's copy.

**Q&A log:**
- Q: The ini files' "number comments": the `#` lines? A (dev, 2026-11-25): "Yes exactly. I meant the number signs." They become `;`, the standard ini comment.
- Q: Should the reader accept only `;`, or both `;` and `#`? A (dev): both.
- Q: The readme's client-side ini section: the client's copies aren't read by anything until offline play exists. Describe them now, or only the server's copy now and the client's when offline ships? A (dev, 2026-11-25): "the server copy now, client copy later." So the readme section covers the server's modes.ini and effects.ini only; the client copy's description is a step for the offline plan.
