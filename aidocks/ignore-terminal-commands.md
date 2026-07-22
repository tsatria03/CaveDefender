---
name: ignore-terminal-commands
description: "Ignore the user's local terminal commands (bash-input/local-command blocks like cls); they aren't instructions to me"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

The user runs local shell commands in their prompt (shown in `<local-command-caveat>`, `<bash-input>`, `<bash-stdout>`, `<command-name>` blocks — e.g. `cls`, `/compact`). These are the user operating their own terminal, NOT messages or instructions to me.

**Why:** they're side effects of the user's local session, not requests. Acting on them (or treating their output as a task) derails the real conversation.

**How to apply:** never respond to or act on the content of these blocks unless the user explicitly asks me to in their actual message. Related: [[quoted-text-meaning]].
