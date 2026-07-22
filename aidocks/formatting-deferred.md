---
name: formatting-deferred
description: "Consistent indentation (spaces/tabs) cleanup is wanted eventually for readability, but stays parked — don't run formatting passes unless the dev asks"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
---

The dev WANTS the code tidied into consistent indentation (spaces and/or tabs) at some point — NVGT ignores whitespace ([[angelscript-indentation]]), so it changes nothing functionally, but it reads much nicer in the long run. This is a real future goal, not a "never." It is NOT tied to any milestone (the old 2.0-server trigger is retired).

**Why:** During active feature work, reflowing whitespace is pure churn and bloats the diffs the dev reviews by screen reader, for zero functional gain. So the cleanup waits for a deliberate, dedicated pass.

**How to apply:** Keep making functional edits without fussing over consistent indentation, and don't propose or run formatting passes on your own. When the dev explicitly asks for a formatting/indentation cleanup, that's the time — treat it as its own isolated pass (see [[stage-commits-before-big-changes]]) so it doesn't mix into feature diffs.
