---
name: list-modified-files
description: "Always end a turn that edited files with an explicit list of every file modified, bare filenames only. Carried over from SimpleFighter (same dev)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

After any turn that modifies files, explicitly tell the dev WHICH files were touched, using bare filenames only, so they can review the changes themselves.

**Why:** The dev is a screen reader user and reviews changes by opening the files; a summary that describes edits without naming every touched file makes those changes hard to find. They know the repo layout, so directory paths are noise — bare filenames are easier to read. (Requested/reaffirmed on the SimpleFighter project: bare names only, no paths.)

**How to apply:** End each response that performed edits with a short "Files changed:" list covering every file written, edited, or deleted that turn — including doc and config files, not just code. One line per file. Bare filenames only (e.g. `regex.nvgt`, `net.nvgt`) — never full directory paths; the dev knows where everything lives. **But note which half each file came from — client or server** (e.g. `net.nvgt (server)`, `game.nvgt (client)`). This matters because both halves have same-named files (notably `net.nvgt` exists in both `client/` and `server/`), so a bare name alone is ambiguous. Files outside both halves (CLAUDE.md, memory files) need no tag. Related: [[confirm-before-implementing]], [[no-crlf-normalization]].
