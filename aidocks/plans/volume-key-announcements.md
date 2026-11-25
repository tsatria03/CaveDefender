---
name: volume-key-announcements
description: "BUILT 2026-11-24 (code + docks; awaiting the dev's in-game test) — speak + log the in-game volume keys exactly like StrideRush: Page up/down = 'track <dB>', Home/End = 'source <dB>', logged to the misc buffer, silent at either end, keys stay fixed (not bindable), 1 dB per step on Windows key repeat (key_repeating). Menu music stays silent, as in StrideRush."
metadata:
  type: project
---

**Idea (dev, 2026-11-24):** "add spoken announcements for increasing/decreasing volumes with the keyboard keys. It should say source volume, track volume, etc."

**Today:** client `globals/game.nvgt` ~434-444 (the live world-volume block): Page up/down call `set_music_volume(musvolume±2)`, Home/End call `set_ambience_volume(ambvolume±2)`, on a 50 ms `worldvoltimer` repeat, clamped -100..0, `writepreffs()` only when it changed. Nothing is spoken. The menu's Page up/down (shared `deps/form_menu.nvgt` `check_volume_keys`) adjusts menu music, also silently.

**StrideRush reference (read 2026-11-24):** `change_music_volume` / `change_ambience_volume` in its globals/game.nvgt speak `"track " + music_volume` and `"source " + ambience_volume` (the raw dB value, e.g. "track -10", "source -25") through `speak_buffer`, which logs to the misc buffer and interrupts; at either end the press does nothing and says nothing; saved on every change. Its keys are rebindable via keyboard.ini (with F3-F6 alternates); its menu music is silent.

**Q&A log:**
- Q: Which name for which control? A: (dev confirmed by "match exactly") music = "track", ambience = "source", as StrideRush.
- Q: Percent ("84 percent", "maximum/minimum") or StrideRush's raw dB and silence at the ends? A (dev): "I want it to match exactly if possible, and logged to the misc buffer."
- Q: Rebindable like StrideRush? A (dev): "Also not bindable of course." Keys stay fixed in code; no F3-F6 alternates (F5/F6 are already beacons/player list here).
- Q: Keep CaveDefender's 2 dB steps on its own 50 ms hold timer? A (dev): "I want it to use the windows keyboard repeat behavior, aka key_repeating. Also make it go by 1db, not 2." So: key_repeating() (one step on press, then the OS key-repeat delay and rate while held), 1 dB per step, as StrideRush.

**Build (one small section, client only):** rewrite the world-volume block in game.nvgt: drop the `worldvoltimer.elapsed>=50` gate and `key_down`, and read each key ONCE with `key_repeating()` in an if/else-if chain ([[nvgt-key-pressed-oneshot]]); step by 1 dB (`musvolume±1`, `ambvolume±1`), clamped -100..0; after a change actually happens, `add_buffer_item("misc", "track " + musvolume)` for Page up/down and `add_buffer_item("misc", "source " + ambvolume)` for Home/End, then `writepreffs()`. No speech when clamped at -100 or 0 (the existing guards already skip the change). Remove the now-unused `timer worldvoltimer` from client `globals/dec.nvgt` (its only user was this block). Update the block's comment to match. `add_buffer_item` speaks with interrupt, so holding a key speaks only the newest level; a muted misc buffer stays silent, as with every misc line. Menu music unchanged (silent, as in StrideRush). Note: holding a key adds one misc line per step, exactly as StrideRush does.

**Built 2026-11-24:** code as specified (game.nvgt volume block on key_repeating, 1 dB, `add_buffer_item("misc", "track "/"source " + int(level))`; `worldvoltimer` removed from dec.nvgt; no other code reads these four keys). Docs: the 5.3 changelog's newest entry and one readme line under Volume. Line endings verified in all four files. Spotted, not fixed (pre-existing): readme lines 78, 110 and 140 exceed the 1024-char limit ([[dock-line-length-1024]]).

**Docs (final section, [[final-section-dock-updates]]):** one 5.3 changelog line (5.3 is unreleased) and a sentence in the readme's Volume section saying the keys announce "track" and "source" with the level. See [[changelog-rules]], [[dock-line-length-1024]].
