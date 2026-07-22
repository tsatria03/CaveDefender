---
name: claudemd-length
description: "Keep CLAUDE.md under 40,000 characters — move detailed content to memory files rather than expanding inline. Carried over from SimpleFighter (same dev)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

Keep CLAUDE.md under 40,000 characters. Do not add large blocks of content inline — move detailed rules and guidance to memory files instead and reference them with a short pointer line.

**Why:** On the SimpleFighter project, CLAUDE.md was deliberately shortened from ~43,000 down to ~33,000 chars by extracting detailed rules into memory files. The dev wants the same discipline applied to keep the file scannable.

**How to apply:** Before adding new content to CLAUDE.md, check the current character count. If an addition would push it toward or past 40,000 characters, put the content in a new memory file instead and add a brief pointer in CLAUDE.md.
