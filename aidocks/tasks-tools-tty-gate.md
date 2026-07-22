---
name: tasks-tools-tty-gate
description: "Todos were renamed to Tasks (TaskCreate/TaskUpdate/TaskList/TaskGet); they vanish silently in this dev's sessions and CLAUDE_CODE_ENABLE_TASKS=1 alone did NOT fix it"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 2ea4e4c2-64df-4051-8fb3-7a3e41740da2
  modified: 2026-07-22T04:45:32.212Z
---

Claude Code v2.1.16 (2026-01-22) replaced **Todos** with **Tasks**: `TodoWrite` is gone,
replaced by `TaskCreate` / `TaskUpdate` / `TaskList` / `TaskGet`, persisted in
`~/.claude/tasks/<session-id>/`.

**Open problem as of 2026-07-21.** The task tools are missing entirely from this dev's
sessions (ToolSearch finds none) even though the installed 2.1.217 bundle defines them
in `sdk-tools.d.ts`. Tasks last worked on Jul 20 — `~/.claude/tasks/` has folders up to
that date and none since.

What has been ruled out, in order:
1. Not the rename — the tools ship in the installed bundle.
2. Not a policy override — no `managed-settings.json` or `policies.json` anywhere.
3. **`CLAUDE_CODE_ENABLE_TASKS=1` in settings.json `env` is NOT sufficient.** Added it,
   restarted, confirmed the var is live in the process env — tools still absent. So the
   binary's explicit-enable branch does not beat whatever is disabling them, matching
   the VSCode reports in https://github.com/anthropics/claude-code/issues/23874
   (closed as *not planned*).

4. Not `"todoFeatureEnabled": true` either — removed it, restarted, still absent.
5. Not the session ID — a fresh headless session (`claude -p`) with the env var live
   also reports no task tools.
6. Not a missing binary — `claude.exe` contains `TaskCreate` ×30, `TaskUpdate` ×24,
   `TaskList` ×21 and the `CLAUDE_CODE_ENABLE_TASKS` string. The tools are compiled in
   and being withheld, not absent.

**Leading hypothesis: a regression in 2.1.217.** Tasks demonstrably worked on Jul 20
(`~/.claude/tasks/e1f5da55…/.highwatermark` = 25, i.e. 25 tasks created). `claude.exe`
was replaced Jul 21 20:53, ~20 min before tasks were first noticed missing. The
documented `CLAUDE_CODE_ENABLE_TASKS=1` override does not work in this version.
Proposed fix if it recurs: `npm i -g @anthropic-ai/claude-code@2.1.216` (no local
version cache exists — `~/.claude/versions` and `downloads` are empty).

Likely remaining cause if that fails: the `process.stdout.isTTY` gate, which this dev
may trip via their screen-reader terminal setup. There is no upstream fix coming.
Fallback tracker is `cf/client/docks/todo list.txt` (see [[todo-list-one-sentence]]).

**Update 2026-07-21 (downgrade attempt).** Dev downgraded the CLI to an earlier version
to try to restore legacy todos; task tools are STILL absent (ToolSearch finds none).

**Version boundary (from changelog research):** `v2.1.141` is the last release where the
legacy `TodoWrite` (single rewrite-the-whole-array todo tool) was the *default*; starting
`v2.1.142`, Tasks became default and TodoWrite was deprecated. Tasks first appeared as
opt-in in `v2.1.16`. So a reliably-legacy build is **v2.1.141 or earlier**. Treat the
`.142` boundary as very-likely-but-not-certified (release wording on defaults is fuzzy).

**Flag polarity — likely inverted from what we assumed.** `CLAUDE_CODE_ENABLE_TASKS=1`
means "use new Tasks"; **`=0` / `=false` means "fall back to legacy TodoWrite."** That
explains why `=1` never helped — to get the old todo tool back on a Tasks-default build,
try **`CLAUDE_CODE_ENABLE_TASKS=0`**, not `1`. (Untested here yet.)

**Auto-updater probably reverts the downgrade.** npm-installed Claude Code auto-updates;
a manual `npm i -g …@<old>` gets bumped back to latest on next launch unless the updater
is disabled (`DISABLE_AUTOUPDATER=1`, or `autoUpdates: false` in config). Pin the version
AND disable the updater together, or the downgrade won't stick.

**Confirmed 2026-07-22: the auto-updater WAS clobbering the downgrade.**
`~/.claude/.last-update-result.json` showed a successful bump `2.1.216 → 2.1.217` at
04:43 UTC. So every manual `npm i -g …@<old>` was being auto-reverted to latest.

**Fix applied to `~/.claude/settings.json` `env`:** added `"DISABLE_AUTOUPDATER": "1"`;
kept `"CLAUDE_CODE_ENABLE_TASKS": "1"` (native-Tasks path).

**Rollback plan (pending dev action — do after fully quitting CC so env reloads):**
1. Primary: `npm i -g @anthropic-ai/claude-code@2.1.216` — the exact build from before
   the 2.1.217 install; Tasks worked on Jul 20, so this tests the "2.1.217 regression"
   hypothesis with the smallest rollback. Keep `CLAUDE_CODE_ENABLE_TASKS=1`.
2. Verify `claude --version` says 2.1.216 and STAYS (updater now disabled), then create
   a fake task to confirm.
3. If tasks STILL absent on 2.1.216 → it's the isTTY/terminal gate, not a regression.
   Fall back to `@2.1.141` (last legacy-default build) and flip
   `CLAUDE_CODE_ENABLE_TASKS` to `0` for legacy TodoWrite.
Unverified: that 2.1.216 / 2.1.141 are real published npm versions (not checked against
the registry from-session); if npm 404s, find the nearest real version.
