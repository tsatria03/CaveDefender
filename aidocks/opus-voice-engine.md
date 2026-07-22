---
name: opus-voice-engine
description: The pinned nvgt2 engine now has the opus codec + live mic capture for real-time voice chat
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

The pinned legacy engine (C:\nvgt2, built from tsatria03/misc/Legacy-NVGT) now has everything needed for **live** voice chat, added 2026-06-19:

- **opus plugin** (codec-only: `opus_encoder`, `opus_decoder`, packet utils, plus the `opus_application_type`/`opus_signal_type`/`opus_bandwidth` enums it registers itself) ships as a **shared DLL** (`opus.dll`). Scripts load it with **`#pragma plugin opus`**. The DLL must live in the engine's lib (`C:\nvgt2\lib\opus.dll` for interpreted dev; `cf/client/lib/opus.dll` for compiled bundles, which `cfcm.py` copies in). `static_plugin(opus)` in src/nvgt_config.h is commented out (we tried static first, then switched to shared per the dev's preference — re-enable that line + rebuild to go back). The file reader/writer were stripped (they needed libopusfile/libopusenc, absent from windev).
- **microphone live-capture API** added to the engine's built-in `microphone` object (no pragma needed): `read_data(uint max_frames=0)` drains buffered PCM in capture format (float32/int16 LE), `available_frames` property, `flush_capture()` to drop buffered audio without stopping.
- **Playback** of decoded PCM uses the existing `sound.push_memory(string data, bool end_stream, int pcm_rate, int pcm_channels)` (BASS push stream, expects **float** PCM).

Live-voice pipeline: `mic.start_recording(-1,48000,1,true,false,false)` → poll `available_frames`/`read_data(480)` (10ms) → `opus_encoder.encode_float` → send → `opus_decoder.decode_float` → `sound.push_memory(pcm,false,48000,1)` (3D-positioned). `flush_capture()` on talk→idle.

This lets CaveDefender replace the current record-clip + `oggenc2.exe` voice path (task [[game-vision-wallbreaker]] #45). Reference impl: kalahami/games/Vengeance-of-the-mocking-jay client/includes/sound/voicechat.nvgt (but that runs on miniaudio NVGT: uses `mic.read()`/`stream_pcm`, not our BASS `read_data`/`push_memory`). Test: Legacy-NVGT/test/quick/opus_microphone.nvgt.
