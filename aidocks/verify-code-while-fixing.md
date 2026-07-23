---
name: verify-code-while-fixing
description: When fixing anything, read the surrounding code carefully, verify the reported detail is actually true, and catch/flag adjacent errors found along the way — don't blindly trust a finding's line numbers or claims
metadata:
  type: feedback
---

When fixing a bug or applying a change, don't just patch the reported spot — **read the code carefully around it, confirm the report is accurate, and surface any errors you notice while you're in there.**

**Why:** review findings and remembered line numbers drift and can be wrong. Blindly following them ships broken or incomplete fixes (the user compiles builds themselves, so a wrong edit ships — see [[dont-compile-yourself]]).

**How to apply:**
- Re-locate the target by symbol, not the stored line number (line numbers drift after edits).
- Read enough surrounding code to understand intent before changing it.
- Verify the finding's claim is actually true; correct it if not.
- Fix or flag adjacent problems you trip over — but keep the fix scoped, don't silently balloon it.

Confirmed working in the 4.6 quick-wins pass: on the player-cap constant ([[internal-code-improvements]]) the review had mislabeled `game.nvgt:777` (that `4` is the four *walls*, not the player cap) and had missed a real cap site at `net.nvgt:2479`; verifying each site caught both before editing. Related: [[confirm-before-implementing]], [[check-git-log-for-commits]].
