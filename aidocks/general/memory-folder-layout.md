---
name: memory-folder-layout
description: "CaveDefender memories live in aidocks/, split into general/ (topics, rules, references) and plans/ (feature plans, finished or in progress); aidocks/MEMORY.md indexes both. Set up by the dev 2026-11-24, matching their other NVGT games."
metadata:
  type: feedback
---

Save every memory for this project in the repo's own aidocks/ folder, never the harness's ~/.claude memory store. Topics (conventions, feedback rules, engine notes, project facts, as-built references, backlogs) go in aidocks/general/. Feature plans go in aidocks/plans/, and that includes COMPLETED plans, not just open ones: when a plan is finished it stays in plans/ as the record of what was decided and built (mark it done; don't delete it or move it to general/). aidocks/MEMORY.md is the index for both, grouped under headings, with every link written as general/<name>.md or plans/<name>.md.

**Why:** the dev reorganized the flat aidocks/ folder into general/ and plans/ on 2026-11-24 so CaveDefender matches the layout of their other NVGT games (the StrideRush repo's aidocks is the model).

**How to apply:** write the file into the right subfolder, add a one-line pointer under the fitting MEMORY.md heading, and keep [[name]] links as bare names (they resolve to either folder, so moving a memory between folders never breaks a link). Keep CaveDefender's plain kebab-case file names; no type prefixes. When a memory is deleted, remove its index line and rewrite any sentence that linked to it. See [[claudemd-length]] for keeping CLAUDE.md a dispatcher.
