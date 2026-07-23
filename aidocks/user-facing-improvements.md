---
name: user-facing-improvements
description: Player-visible bug backlog from the 4.5 full-game review — ALL CLEARED in 4.6 (case-match, ban/kick enforcement, movement bounds-clamp); kept as a record + the consciously-deferred full anti-teleport option
metadata:
  type: project
---

Player-visible bugs from the full 360 review at v4.5 (the [[changelog-rules]] "player-observable effect" test). **All three were addressed in 4.6 — this backlog is now empty.** Kept as a record and to note the one piece deliberately deferred. Related: [[accounts-system]], [[ban-tiers-and-hwid-limits]], [[reconnect-persistence]].

## Cleared in 4.6
- **Case-sensitive session match** (showed a player twice) — fixed by canonicalizing the login name to on-disk casing (`login()` in `server/net.nvgt`).
- **Ban & kick not enforced** — fixed with a central `force_logout(peer)` (revoke `verified_logins` + `disconnect_peer_softly`) applied to ban/kick/kickall/changepass/delchar/rename, plus a ban re-check in the `spawn_player` `existing<0` branch (`server/net.nvgt`).
- **No server-side movement validation (anti-cheat)** — partially addressed via **option B (bounds-clamp only)**: the `move` handler now clamps x/y to `[0, game size]` when the player is in a game (`server/net.nvgt`, the `parsed[0]=="move"` branch). Invisible to honest players, so no changelog entry.

## Consciously deferred (not a bug — a decision)
**Full anti-teleport (option C) was deliberately NOT done.** Placement is client-authoritative by design — the client teleports itself to spawn points and informs the server via a big-delta `move` (e.g. PVP side-spawn at `client/net.nvgt` `yourside`). Rejecting in-map teleports would require flipping to server-driven placement across every mode's start/entry — a large refactor with real regression risk, judged disproportionate for a small trusted community. Revisit only if teleport-cheating becomes an observed problem in competitive PVP/EVP. The cheap bounds-clamp (option B, above) is the accepted "good enough."
