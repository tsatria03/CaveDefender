---
name: final-section-dock-updates
description: When building a feature in sections, reserve the FINAL section for dock updates (changelog/readme/help); earlier sections are code only
metadata:
  type: feedback
---

When a feature is built in SECTIONS, the LAST section is always reserved for client/server **dock updates** — the changelog entry, readme, and `/help` pages (if any). Earlier sections are code/behavior only; don't write player-facing docs mid-build. Applies to all features.

**Why (dev, 2026-09):** docs describe the finished behavior, so writing them before the feature is complete risks documenting a half-built state (e.g. `/prl`'s offline card wasn't done until section 3, so its changelog/readme/help waited for section 4).

**How to apply:** plan the section list with a final "dock updates" section. In each code section's wrap-up, note that docs are deferred to the last section. The dock work still follows [[new-command-checklist]] (client router, server handler, both help pages, changelog, identical wire strings) and [[changelog-rules]] / [[bump-version-with-changelog]] — just batched at the end. If a feature touches no docks, the final section is a no-op (say so). Relates to [[check-git-log-for-commits]] (verify each section's commit).
