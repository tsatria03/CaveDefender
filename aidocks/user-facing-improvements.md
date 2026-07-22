---
name: user-facing-improvements
description: Player-visible bug backlog from the 4.5 full-game review — only defects a normal player sees/hears in the game (ban/kick enforcement, duplicate-roster from case mismatch); invisible robustness bugs live in internal-code-improvements
metadata:
  type: project
---

Outstanding bugs from the full 360 review at v4.5 that a **normal player actually sees, hears, or does in the game** — the test from [[changelog-rules]] (player-observable effect; if invisible it doesn't belong here). These are the ones that would earn a changelog line when fixed. Fix one at a time and delete each entry as it lands (per [[delete-completed-tasks]]). Invisible correctness/robustness bugs now live under "Correctness & robustness" in [[internal-code-improvements]]; item 2 below is an anti-cheat fix kept here because the exploit is very visible to players when someone abuses it. (The case-sensitive-session-match bug was fixed in 4.6 and removed from this list.) Line numbers were accurate at review time — re-locate by symbol if the file has shifted. Related: [[accounts-system]], [[ban-tiers-and-hwid-limits]], [[reconnect-persistence]].

**1. Ban & kick not enforced server-side.** A banned or kicked player keeps their connection and can keep playing — `perform_ban()` removes the roster entry and sends `"banned"` but never calls `disconnect_peer_forcefully(tpeer)` nor `verified_logins.delete(""+tpeer)`, so a modified client that ignores the message stays on and can re-send `spawn_player` (the `existing<0` branch re-seats it with no ban re-check at spawn). Weakens staff moderation directly. `/kick`, `/kickall`, `delchar`, `changepass`, `renamed` share the shape. Fix centrally: revoke `verified_logins` + force-disconnect (primitive already used by `do_restart`), and re-check the ban inside `spawn_player`. — `server/net.nvgt:446-470`, `1179-1215`, `2985-3028`

**2. No server-side movement validation (anti-cheat).** Position is fully client-authoritative; all gather/reinforce/attack reach logic trusts it, so a modified client can teleport adjacent to any wall — honest players never notice, but a cheater warping around is very visible to everyone. May be an accepted audio-game tradeoff, so decide consciously before touching. Fix if desired: clamp to `[0,size]` and reject implausible per-tick deltas. — `server/net.nvgt:1273-1278`
