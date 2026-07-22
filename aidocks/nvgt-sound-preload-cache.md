---
name: nvgt-sound-preload-cache
description: NVGT sound.load caches decoded audio by FILENAME (preload cache); reusing a filename for changing audio replays the old clip. Use unique names or allow_preloads=false.
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

NVGT's `sound::load(filename, pack@, bool allow_preloads = !system_is_mobile)` consults a global **filename-keyed preload cache** (`get_sound_preload(filename)` in sound.cpp). On a hit it builds the stream from the CACHED bytes and ignores the file's current contents on disk. So if you write new bytes to the SAME filename and load it again, you get the PREVIOUS clip back.

This bit voice chat (the "plays the last clip, not the new one" bug, fixed in 2.1): the local "hear yourself" path reused `convert.ogg` and the remote path reused `cvf_voice_<name>.ogg`, so after the first clip every reload replayed the cached audio. `sound.close()` does NOT clear the cache (it's a separate global map).

Two fixes, both used:
- **Direct sound object** (the global `playback`): load with preloads off — `playback.load(outfile, sound_default_pack, false)`. `sound_default_pack` is a registered global; the third arg is `allow_preloads`.
- **Through a sound_pool** (e.g. `vpool.play_3d(file, ...)`): the bundled sound_pool always loads with default preloads and exposes no flag, so give each clip a **unique filename** instead (`cvf_voice_<name>_<counter>.ogg`, counter = `voiceclip_id++`). Delete the previous temp file (`file_delete`, after `destroy_sound` frees it) to avoid temp churn; track it per remote player (`player.voicefile`).

Rule: any time you regenerate audio into a reused path (voice, TTS-to-file, downloaded clips), either use a fresh filename each time or pass `allow_preloads=false`. See [[path-conventions]].
