---
name: menus-say-canceled
description: "Every menu/input-box back, escape, or cancel path should speak \"canceled\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

When building any menu or input box, every way of backing out without choosing an action must `speak("canceled")`: pressing Escape (a menu's `m.run()` returns < 0; an input box / `vd.input_box` / `vd.password_box` returns ""), choosing a **Back** item (even in a "single"/leaf menu — Back closes the menu, it doesn't open a sub-menu), and choosing **No** on a yes/no confirmation.

**Why:** the dev wants consistent audible feedback when canceling out; silent menus leave a screen-reader player unsure whether anything happened.

**How to apply:** in every new menu/input flow, wire `speak("canceled")` on the escape path, the Back item, and the No/decline path. Match the existing room menus (`lobby_menu.nvgt`, `room_menu.nvgt`, `join_menu.nvgt`) which already do this. Relates to [[use-dlgmessage]].
