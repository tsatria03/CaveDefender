---
name: file-exists-boxed-sound-trap
description: "HISTORY + one lasting rule: file_exists() used to read FALSE for Enigma-boxed sounds, silently killing guarded sounds in release builds (all victims fixed in 4.1). Boxing was removed 2026-11-24, so the trap is gone, but the rule stands: never gate sound playback on file_exists; detect optional sounds with a data/class flag."
metadata:
  type: project
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
---

**History:** while release clients were packed with Enigma Virtual Box ([[enigma-boxing]]), the sound loader could read embedded files but `file_exists("sounds/...")` checked the real disk and returned FALSE. Any `if(file_exists(path)) play(...)` therefore went silent only in release builds. Three victims were found and fixed in 4.1: the bullet travel loop (guard removed, moved to its own `bulletpool`), the item ground loops (every item type got a `loop.ogg`, guard dropped), and shell casings (replaced with the class check `weapon_class(wname)=="artillery"`). Since 2026-11-24 nothing is boxed and sounds ship loose ([[build-tools-remove-boxing]]), so `file_exists` on a sound now behaves the same in dev and release.

**The lasting rule (still follow it):** never gate sound PLAYBACK behind `file_exists`. Play directly; a genuinely missing file just fails into an invalid slot that the move/destroy calls ignore, which is also how the current placeholder sounds (`gameover.ogg`, `roundcleared.ogg`) behave until the dev adds them ([[sound-placeholders]]). For real feature detection ("does this weapon have shell casings?"), use a data or class flag like the shell-casing check, not a file probe. That keeps the code independent of how sounds are packaged, should packaging ever change again. `file_exists` remains fine for real on-disk files such as settings or save files ([[audio-and-sounds]]).
