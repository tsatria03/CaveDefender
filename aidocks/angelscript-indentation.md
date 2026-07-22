---
name: angelscript-indentation
description: "AngelScript/NVGT ignores indentation entirely; don't flag uneven whitespace as a concern"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

AngelScript (the `.nvgt` language) is brace-delimited, so indentation is purely cosmetic and never affects compilation — unlike Python, where it's syntactically required.

**Why:** I kept apologizing for or flagging "uneven indentation" after edits, which is noise — it has zero effect on the code.

**How to apply:** After an edit leaves whitespace slightly off, don't call it out or spend extra tool calls fixing it for compilation's sake. Only adjust indentation if the dev explicitly asks for tidy formatting. Relates to [[no-crlf-normalization]].
