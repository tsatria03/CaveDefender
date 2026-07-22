---
name: input-prompt-form-vs-dialog
description: One input field -> virtual dialog; more than one field -> a real audio form with tabbable fields
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

Rule for ANY input prompt, going forward:
- Exactly ONE field -> use a virtual dialog (`vd.input_box` / `vd.password_box`).
- MORE THAN ONE field -> use a real `audio_form` with all fields on one screen, tabbable, like the new-account form in client `menus/menu.nvgt` (a `form.create_input_box` per field plus create/cancel buttons and a validate loop), NOT a chain of sequential blocking dialogs.

**Why:** entering several values one blocking dialog at a time is clumsy and gives no chance to review or fix an earlier field; a single form lets the player tab between fields and see them together before submitting.

**How to apply:** build multi-field prompts as one form. Flows converted for this rule: private-room set-password (password + confirm), `/changepass` self (current + new + confirm), `/changepass` admin reset (new + confirm). A password field masks with `"*"` and disallows spaces. Related: [[virtual-dialogs-form-backend]], [[use-dlgmessage]], [[menus-say-canceled]].
