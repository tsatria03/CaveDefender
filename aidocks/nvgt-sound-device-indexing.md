---
name: nvgt-sound-device-indexing
description: "BASS/NVGT sound device list indexing — index 0 is \"No sound\", index 1 is \"Default\"; don't add your own Default entry"
metadata: 
  node_type: memory
  type: reference
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
---

NVGT's `get_sound_output_devices()` is BASS's `list_output_devices()` (see [[nvgt-engine-source-location]], `src/sound.cpp` ~2088), which enumerates `BASS_GetDeviceInfo(0,1,2,…)`. In BASS the returned array is: **index 0 = "No sound"** (a virtual no-audio device), **index 1 = "Default"** (the actual system default output, literally named "Default"), then **2+ = the named devices**.

CaveDefender's device choosers (`client/includes/main/menus/menu.nvgt`, the sound `sdm` button and `savefuncts.nvgt` load) call `devices.remove_at(0)` to drop "No sound", so the trimmed list **already starts with "Default"** at trimmed index 0. `sound_output_device = trimmed_index + 1`, i.e. the original BASS device index. The startup default is `soundcard="Default"` / `sound_output_device=1` (`cfc.nvgt`), which is exactly trimmed-index-0 "Default".

**Do NOT add your own synthetic "Default" menu item** — it duplicates the real one. This bit us once: an added Default item made "Default" appear twice. The "Currently active" marker (`devices[i]==soundcard`) already tags Default correctly because it's a real list entry. Recording input devices (`get_sound_input_devices`) similarly include a real "Default" at index 0 and are NOT trimmed.
