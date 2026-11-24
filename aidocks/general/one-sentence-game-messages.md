---
name: one-sentence-game-messages
description: In-game feedback messages must be exactly one sentence — no second sentence with extra advice/instructions
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

In-game feedback messages (the short notices sent to a player, e.g. reinforce errors, command results) must be **exactly one sentence** — at least one, but never more. Don't tack on a second sentence with advice or instructions.

**Why:** the dev wants concise, single-statement feedback; trailing "do X instead" / "wait for Y" sentences are clutter when spoken by a screen reader.

**How to apply:** state the fact and stop. E.g. "You can't reinforce while the enemies are attacking." NOT "...attacking. Wait for them to pull back." This is distinct from the [[changelog-rules]] (which govern changelog prose, not in-game messages).
