---
name: privacy-cleanup
description: "COMPLETE (2026-11-24) — removing player account data from the public repo: untracked + gitignored, history rewritten with git-filter-repo and force-pushed, old release archives deleted, GitHub Support contacted by the dev about purging cached commits. No other clones exist."
metadata:
  type: project
---

**Why:** the GitHub repo is PUBLIC and had tracked `cf/server/data/players` since 2026-06-18: 104 accounts with Argon2id password hashes, real email addresses, nicknames, pronouns, stats, moderation files and 9 players' custom online/offline .ogg clips. No IP addresses were ever stored. Older history also held accounts under `server/data/players/`, `play/server/data/players/` and `src/server/data/players/`, plus player feedback in `feedback.svr` and a report in `reports.svr`.

**Done:**
- Release archives: the server .7z of V2.50, V3.00, V3.50, V4.10, V4.20 and V4.50 held accounts (V4.50: 17); V4.00 held reports.svr. The build's `sanitize_server_bundle` only exists since commit 8f84df0 (2026-07-23), so every release before V4.70 was dirty. The dev deleted all releases except V5.10 and V5.20 (both scanned clean).
- `.gitignore` gained `cf/server/data/players/`, then `user/`, then `feedback.svr` / `reports.svr`; the players folder was untracked (`git rm -r --cached`) and committed.
- History rewrite: `git-filter-repo --invert-paths` on the four player paths + the three .svr paths, run in a fresh clone; verified 0 matches in any commit or tag, all 521 commits and 20 tags kept, every kept file byte-identical. Claude force-pushed at the dev's request (`--force-with-lease`), then reset the dev's working copy onto the new history and purged old objects (reflog expire + gc). New main after the rewrite: 2c59502. The 7 old commit hashes quoted in aidocks were remapped via filter-repo's commit-map (4ff4bb4).
- Lesson recorded: `git commit -- <path>` takes disk contents, so it can't commit an untracking; commit staged removals with no pathspec.

**Left:**
1. ~~Ask GitHub Support to purge cached old commits~~ — DONE: the dev contacted GitHub Support about the player data (2026-11-24).
2. ~~Re-clone other copies~~ — NOT NEEDED (dev, 2026-11-24: there is no separate clone of this repo; the VPS has none). The only copy is the dev's working folder, already reset onto the new history.
3. Optional (the dev's call; don't raise it unless they ask, see [[dont-mention-optional-items]]): tell players their email may have been visible and suggest a password change. Longer term, consider whether email needs storing at all.

**Tools:** git-filter-repo 2.47.0 is installed for Python 3.12 at `C:\Users\tonys\AppData\Roaming\Python\Python312\Scripts\git-filter-repo.exe` (not on PATH; call by full path). See [[commit-style]] (Claude never pushes, the force push was a one-off).
