---
name: networking-protocol
description: "CaveDefender's client/server wire protocol — enet network class, the 4 channels (0 control / 1 chat / 2 PM / 3 voice), the rscs123 encryption, and the space-delimited message contract. Read before changing any message string on either side."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

Built on NVGT's built-in `network` class (enet). The client uses `setup_client` + `net.connect`; the server uses `setup_server`. Both poll `net.request()` each frame and branch on `event.type` (`event_connect` / `event_disconnect` / `event_receive`). (Note: NVGT defaults to IPv6/dual-stack, which breaks IPv4 VPN hosting — both sides set `net.IPV6enabled=false` before setup; see [[nvgt-ipv6-networking]].)

- **Channels:** 0 = control/system, 1 = public chat, 2 = private messages, 3 = voice. Channels 0–2 carry the space-delimited text protocol; **channel 3 carries raw voice bytes** — with the live opus voice system the client sends only the audio, the server prepends a `name x y\n` header before relaying to everyone else, and drops anything larger than `maxvoicebytes`. Received clips play per-speaker positioned at the speaker's map spot (see [[cavedefender-voice-chat-mode]], [[opus-voice-engine]]).
- **Encryption:** every packet is run through `string_encrypt` / `string_decrypt` with the key `"rscs123"`, shared by both sides in `send()` / `get_event_message()`.
- **The protocol is the contract.** Both sides agree on a set of **space-delimited** message strings (`login`, `register`, `spawn_player`, `who`, `welcome`, `disconnect`, `ping_request`/`ping_response`, `online`/`offline`, `move`/`pos` (player position: client sends `move <x> <y>`, server broadcasts `pos <username> <x> <y> <visible-rank> <afk> <nickname>`, where visible-rank is the flag-filtered rank — the rank only when staff with their flag on, else `player` — afk is 1/0, and nickname is the display name, all for the P player-tracker; the roster is keyed by the **username**), `play`, `terminate`, `/motd`, `/pm`, …). `online`/`offline` carry `<username> <rank> <nickname>` (display uses the nickname, the username keys the roster). Because messages are space-delimited, usernames / passwords / **nicknames** must contain **no spaces**. **When you change a message on one side, update the matching handler on the other** — a silent client/server mismatch is the classic bug here. Each side has its own `net.nvgt` (`src/client/includes/main/globals/net.nvgt` and `src/server/.../net.nvgt`): near-identical `send()`/`get_event_message()` but mirror-image `netloop()`s (client presents; server dispatches).

Also relevant: client menus/dialogs must pump `net_keepalive()` while blocking or enet drops the connection — see [[blocking-ui-network-keepalive]].
