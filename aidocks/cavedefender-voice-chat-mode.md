---
name: cavedefender-voice-chat-mode
description: Voice chat mode — live streaming vs record-then-send voice messages; prefs list + tagged opus channel-3 wire format, implemented and confirmed working in-game (2026-07-06)
metadata:
  node_type: memory
  type: project
---

CaveDefender's **"Voice chat mode"** preference (Live streaming vs Voice messages) is **fully implemented and confirmed working in-game** as of 2026-07-06 (two-machine test passed). Design: Design A (reliable framed messages), 3D playback for all room listeners. Builds on [[opus-voice-engine]].

**Wire format (channel 3):** payload is `<tag><data>`. `"l"` + one opus packet = live frame (unreliable). `"m"` + framed blob = voice message (reliable); blob = back-to-back `[uint16 big-endian length][opus packet]` per frame. Server (`src/server/includes/main/globals/net.nvgt` ~2033) prepends `"name x y\n"`, relays verbatim, picks reliability from the tag. Both modes interoperate per-sender (the listener handles whatever tag arrives regardless of their own mode).

**Client (`src/client/includes/main/functions/recfuncts.nvgt`):**
- Framing helpers `voice_frame_pack()` / `voice_blob_split()` (use engine `ascii_to_character`/`character_to_ascii`).
- `recordcheck()` branches on `voicemode`: mode 0 streams `"l"` frames live (unchanged); mode 1 buffers frames + raw pcm, sends one reliable `"m"` blob on release/cap, plays own clip back locally if `hearvoice`. Resets the encoder at message start (self-contained stream). 300ms min-length floor silently discards an accidental tap (no announcement), `rectime` (10s) cap, mute discards partial.
- Receive: `play_remote_voice()` branches on tag; `play_remote_message()` splits+decodes the blob with a fresh decoder and plays a fixed-position 3D clip. `playing_voice_message` class + `voice_msgs[]` container; `voiceloop()` re-pans clips against the listener and drops them when finished; `voice_msgs_clear()` on shutdown + on space change (`map.nvgt` draw_map).

**Prefs UI:** `voicemode` global (0=stream default) in `dec.nvgt`; list on General tab in `menu.nvgt` settingsmenu(); the "hear your voice" checkbox relabels in place via `form.set_caption()` ("while speaking" vs "after recording"); saved/loaded in `savefuncts.nvgt`, defaulted in `cfc.nvgt`.

**Changelog:** DONE — two entries at the top of the 3.6 block in `cf/client/docks/changelog.txt` (send capability + the mode setting). No version bump (3.6 is the in-dev block; version generated from `build/version.txt`, never hand-edited). Follows [[changelog-rules]].

**Deploy note:** tagged wire format is a coordinated client+server change; the user always uploads both together, and the 3.5→3.6 version-mismatch check fences off old clients.
