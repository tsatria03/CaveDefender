---
name: use-dlgmessage
description: "Use dlgmessage() for all dismissable alerts and dialogs, never alert() or raw dlg()"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

For any dismissable, player-facing alert or dialog, use `dlgmessage(...)`. Don't use `alert(...)` or raw `dlg(...)`.

**Why:** dlgmessage is the nicer, consistent wrapper; the dev wants a single uniform style for all dialogs. (CLAUDE.md already preferred dlgmessage over raw dlg; this extends it to replace alert() too.)

**Scope:** This applies to normal in-game, player-facing dialogs (e.g. the connect-failure notice became `dlgmessage("Could not reach the server. Please try again.")`). Some alerts deliberately stay as `alert()` because they need the **visual** alert box, not a spoken dialog:
- The pre-initialization fatal alerts (audio/screen reader not up yet): "cannot load screen reader components", "cannot load soundsystem", the GameEngine DLL-missing alert, the voicechat DLL-load alert.
- The single-instance alert and the "Unable to restart …" failures in `cfc.nvgt`, and the same in `extrafuncts.nvgt`, plus the dockread "Could not find …" file-missing alert. (These were converted once and the dev reverted them — leave them as `alert()`.)

**How to apply:** Default to dlgmessage for new in-game dialogs. Don't blanket-convert existing `alert()` calls — ask first, since several are kept as visual alerts on purpose.
