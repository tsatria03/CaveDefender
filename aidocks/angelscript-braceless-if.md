---
name: angelscript-braceless-if
description: A brace-less if/else governs only ONE statement; adding a 2nd (e.g. m.fade_music) into a menu dispatch chain orphans the else and breaks compile
metadata: 
  node_type: memory
  type: project
  originSessionId: c482c7b1-1d44-40e1-bdc5-885ee6305ae7
---

A brace-less `if` / `else if` / `else` in AngelScript governs only the **single next statement**. The menu dispatch pattern in `menu.nvgt` is written brace-less (`if(sel=="x") action(); else if(sel=="y") ...`), so dropping a SECOND statement into a branch — e.g. `m.fade_music();` before the action — makes the action a separate unconditional statement that sits between the `if` body and the following `else`, orphaning the `else` ("else with no matching if"). That's a **compile error**, and an interpreted client/server that fails to compile **won't launch at all** (it looks like the game silently refusing to start).

**How to apply:** to fade music (or add any extra statement) inside a menu `if/else` chain, either brace the branch — `if(sel=="x") { m.fade_music(); action(); }` — or call `m.fade_music()` **once before the dispatch** (after the `if(sel=="back") return;`), the way `connectionmenu()` does it. Don't trust indentation to group statements — NVGT ignores whitespace entirely (see [[angelscript-indentation]]); only braces group.
