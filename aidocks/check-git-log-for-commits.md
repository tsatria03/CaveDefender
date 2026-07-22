---
name: check-git-log-for-commits
description: The user commits their own work; check git log before asking or assuming commit state
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
  modified: 2026-07-19T08:21:59.547Z
---

The user commits changes themselves, not me. Before asking "want me to commit?" or assuming something is uncommitted, check `git log --oneline` (and `git status`) — they often commit between turns without saying so.

**Why:** they were mildly annoyed at being asked about a commit they'd already made; the git log is the source of truth for what's landed.

**How to apply:** after an editing turn, run a quick `git log`/`git status` to see whether they've already committed before mentioning commits at all. Still never commit for them unless explicitly asked. Relates to [[list-modified-files]] and [[dont-compile-yourself]] (they own the commit/build/verify loop).
