---
name: angelscript-reserved-out
description: "Never use \"out\" as a variable name in NVGT/AngelScript — it's a reserved keyword"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

`out` is a reserved keyword in AngelScript (parameter direction, like `in`/`inout`), so it cannot be used as a variable, parameter, or member name in any `.nvgt` code. Using it causes a compile error.

**Why:** the user compiles the build themselves (see [[dont-compile-yourself]]) and hit this when I named a local `string out`.

**How to apply:** pick a different name (e.g. `result`, `serialized`, `output`, `buf`) for any variable that would otherwise be `out`. Watch for other AngelScript reserved words too (`in`, `inout`, `shared`, `final`, `from`, etc.).
