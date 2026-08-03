---
name: onoff-sounds
description: Per-account custom online/offline connect sounds (V1, host-managed) — the onoffs/ folder feature, base64-over-the-protocol + client cache-and-reuse. Read before touching the online/offline cue path or the account onoffs/ folder.
metadata:
  type: project
---

**Feature (dev, 2026-08):** each account can have its OWN custom connect (`online.ogg`) and disconnect (`offline.ogg`) sound, stored server-side in `data/players/<user>/onoffs/`. When player X connects/disconnects, EVERYONE hears X's custom sound (not a generic one, and not a listener preference). If X has no custom file, clients play their builtin `sounds/ui/misc/online.ogg` / `offline.ogg` (the existing behavior). **V1 is HOST-MANAGED** (host drops the .ogg into the account's onoffs/ folder); in-game player self-upload is a SEPARATE later feature. The reorg that created info/ + onoffs/ per account is done (see [[accounts-system]]).

**Rejected alternative (Daily Life BGT game's approach):** a fixed library of predefined sounds (online1..24) shipped in every client, selected by NAME, only the name sent over the wire — no audio transfer at all. Dev knows about it but WANTS the arbitrary-per-account model (richer, truly custom), accepting the transfer cost.

**Delivery: base64 over the text protocol + client cache-and-reuse.** NVGT confirmed capable: `sound.load(string& data, uint size, ...)` loads from memory, and `string_base64_encode`/`string_base64_decode` (with `STRING_BASE64_DEFAULT`) exist (already used for privroom passwords in account.nvgt). The .ogg is binary (has space/newline/null bytes) so it can't be a raw token in the space-delimited, encrypted protocol -> base64 makes it safe text (~33% bigger, negligible here). Cache-and-reuse means a player's sound is fetched ONCE per session per client, then replayed from a client-side cache FILE via the existing sound pool -- so rapid connect/disconnect never re-sends (the dev's concern).

**Protocol:**
- The `online` broadcast gained TWO trailing flags: `online <user> <rank> <nick> <hasCustomOnline> <hasCustomOffline>` (1/0 each). Offline broadcast UNCHANGED (7 sites left alone; the client warms the offline cache from the online flags, and does an on-demand fetch-discover only for players who were already online before this client joined).
- Client -> server: `getonoff <user> <online|offline>`.
- Server -> client: `onoffdata <user> <which>\n<base64 audio>` or `...\nnone` (no custom file). Everything after the first `\n` is the payload, so the audio's own bytes never disturb parsing.

**Playback (dev-approved):** decode base64 -> write to a client cache FILE (e.g. `DIRECTORY_APPDATA + "tsatria03/CaveDefender/onoffcache/<user>_<which>.ogg"`) -> play via the existing sound pool `p.play_stationary(path)`, exactly like the builtin cue (reuses pool overlap/volume). Per-SESSION cache: a host swapping a sound shows next session (a version/hash check can make it live later -- not V1).

**Prefetch (dev-approved):** when a player comes online, the client uses the flags to fully populate its cache for BOTH sounds (fetch each custom one, or cache a "none" marker), so the departure cue is instant too. First encounter of a player plays a beat late (one round-trip); every time after is instant from cache.

## BUILD STATUS (2026-08)
- **SERVER: DONE.** account.nvgt: `has_onoff_sound(name, which)` (file_exists onoffs/<which>.ogg) + `onoff_flags(name)` (the "1 0" suffix). net.nvgt: appended `onoff_flags` to the 2 ONLINE broadcasts (~1310 restore-reannounce, ~1356 fresh login); new `getonoff` handler (~2183, before getreports) reads the file, base64-encodes, replies `onoffdata`, or `\nnone`. Safe to ship alone (flags trailing, getonoff uncalled by old clients).
- **CLIENT: DONE (awaiting dev test).** client net.nvgt (before netloop_impl): `onoff_cache` + `onoff_pending` dictionaries; helpers `onoff_key`, `onoff_cachefile` (`DIRECTORY_APPDATA + "tsatria03/CaveDefender/onoffcache/<user>_<which>.ogg"`), `play_builtin_onoff`, `play_cached_onoff`, `request_onoff` (one getonoff in flight per cue; a play request beats a warm), `do_onoff(user,which,hascustom,play)` (cached->play/skip; "0"->cache none+builtin; "1"/"?"->fetch). Online handler: parse flags parsed[4]/[5], `do_onoff(...,"online",hason,true)` + `do_onoff(...,"offline",hasoff,false)` prefetch, staffin.ogg + connections buffer unchanged. Offline handler: `do_onoff(...,"offline","?",true)`. New `onoffdata` handler: split payload after first `\n`, base64_decode -> write cache file (or "none"), cache the answer, play if pending=="1". Playback via `p.play_stationary(cachefile)` -- OK because the client uses loose files, NO pack (see [[no-sound-pack-support]]), so an absolute APPDATA path loads fine.
- **DOCS: held** (no changelog/readme until dev tests, same as PVP).
- **TEST NOTES:** first encounter of a player plays a beat late (round-trip); after that instant from cache. Base64 may wrap lines (Poco) -- harmless: payload is everything after the header's first `\n`, and base64_decode ignores embedded newlines. Cache files persist across sessions but the in-memory dict is per-session, so a host swapping a sound shows next session (re-fetch overwrites the file).
