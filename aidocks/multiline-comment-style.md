---
name: multiline-comment-style
description: "Multi-line code comments must use /* */ block style, not stacked // lines"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
---

When a code comment spans more than one line, write it as a single `/* ... */` block comment, not a stack of consecutive `//` lines. Single-line comments still use `//` (inline or on their own line).

**Why:** the dev's preferred house style; stacked `//` blocks read as clutter and are harder to reflow.

**How to apply:** any new multi-line comment I author uses `/* */`; when I edit an existing stacked-`//` block, convert it while I'm there. Example: the client `net.nvgt` reconnect doc and `netfuncts.nvgt` [[is_hoster]] doc were converted during the netfuncts extraction.
