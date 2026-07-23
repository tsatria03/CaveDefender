---
name: yes-no-menu-labels
description: For a yes/no menu, label the two items simply "Yes" and "No" — do not tack on descriptive clauses
metadata:
  type: feedback
---

When a menu is a yes/no choice, make the two menu items say exactly **"Yes"** and **"No"** — nothing more. Don't append explanatory clauses like "Yes, respawn them each time the wall recovers" / "No, they leave when the wall falls".

**Why:** the question line above the menu already carries the meaning; verbose option labels are redundant and slower to read by screen reader. Confirmed by the dev 2026-07 on the free-play "spawn upon wall recovery?" prompt ([[free-play-planned-enhancements]] item 4).

**How to apply:** put the full context in the menu's question/prompt text; keep the options themselves to bare "Yes" and "No" (Yes first, so `choice==0` is Yes). Related menu conventions: [[menus-say-canceled]].
