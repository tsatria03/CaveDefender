---
name: quoted-text-meaning
description: "How to interpret quoted text in the user's messages"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

When the user puts text in quotes, the quote is a **reference**, not literal new content to insert. It is one of:
- something I (Claude) said, that they're pointing back at, or
- something they **do** want, or something they **don't** want.

**Why:** I once read a quoted phrase as "add this text" when the user was actually quoting the phrase they wanted *removed*.

**How to apply:** read the surrounding sentence to decide whether the quote marks a thing to keep/add or a thing to drop/avoid. Don't assume a quoted string is verbatim text to paste in. If genuinely ambiguous, ask.
