---
name: command-full-name-before-alias
description: In player-facing docks, write a command's full name before its short alias (e.g. /playerlist, or /prl)
metadata:
  type: feedback
---

When a slash command has both a full name and a short alias, in the DOCKS (changelog, readme, help pages) always write the **full name first, then the alias** — e.g. "/playerlist, or /prl", not "/prl, or /playerlist".

**Why (dev, 2026-09):** the dev consistently refers to commands full-name-first and wants the docks to match; they had me swap `/prl`/`/playerlist` mentions in the changelog and todo to lead with `/playerlist`.

**How to apply:** default to full-name-first for every command's dock references. Note existing docks are inconsistent (e.g. the readme's leaderboard line opens with "/lb"); don't mass-rewrite old entries unprompted, but write NEW dock text this way and fix a command's ordering when the dev flags it. Relates to [[changelog-rules]], [[new-command-checklist]].
