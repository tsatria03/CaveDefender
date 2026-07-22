---
name: blocking-ui-network-keepalive
description: Client blocking UI (menus/dialogs/input boxes) must pump net_keepalive() or enet drops the connection (10-35s timeout); how the keepalive + reentrancy guard work
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
  modified: 2026-07-19T18:42:11.354Z
---

The engine hardcodes the enet peer timeout at `enet_peer_timeout(peer, 128, 10000, 35000)` (network.cpp, on connect) — a 10s minimum / 35s maximum unresponsive window, NOT exposed to script. So if `net.request()` stops being called for >10-35s the server drops the client. Any **blocking modal loop** that suspends the main `game()` loop (which is what normally calls `netloop()` each frame) will trip this. The classic repro was the after-round results `dlgmessage` + "Play again?" menu — players linger there and get dropped (fixed in 2.1).

The fix (client `net.nvgt`): blocking UI pumps `net_keepalive()` every tick, which runs `netloop()` so ACKs/pings keep flowing and messages are handled live. Wired at the central spots:
- `setupmenu()` sets `@m.background_callback = @net_keepalive_cb;` (form_menu's run loop calls background_callback every monitor() tick) — covers every menu.
- `dlg()`'s while loop calls `net_keepalive()` — covers dlgmessage.
- `virtual_dialogs::monitor()` calls `net_keepalive()` — covers input_box/password_box/message_box/info_box.
- The F6 player info card's own `while` loop (`net.nvgt`) calls `net_keepalive()`.
- `dockread()`'s `while` loop (client `extrafuncts.nvgt`) calls `net_keepalive()` — added in 4.2. This bespoke read-only viewer is the SINGLE reader for server /help & /rules, the staff /warnings /bans /mutes /reports views, AND the client docks (changelog/credits/readme/todo). It was the one blocking loop that got missed, so sitting in any of those views timed the connection out and it "freaked out and reconnected" the moment you closed the view — because nothing polled the network while it was open, the drop was only detected when the main loop resumed. Chat inputs never showed it (they pump keepalive). Lesson: bespoke `while(true){ form.monitor(); }` loops are easy to miss — grep for them, not just the three central helpers.

`net_keepalive()` is gated `if(connected or reconnecting)` so it does nothing during the pre-connect menus (mainmenu/settings) and the connect/login handshake (those have their own request loops and must not have events stolen).

Re-entrancy guard: `netloop()` is now a thin wrapper around `netloop_impl()` that tracks `netloop_depth`. Because a pumped `netloop()` can itself receive a message that opens ANOTHER blocking UI, the four blocking-UI branches (`showmenu`, `roundover`, `helptext`, `askinput`) check `if(netloop_depth>1)` and, if so, push the raw message onto `net_deferred` instead of opening. When the outermost call (`netloop_depth==1`) finishes, the wrapper drains `net_deferred` via `dispatch_modal()`. This prevents two modals from using the shared globals (`m`, the dlg pools) at once — the real corruption risk was the global `m` being reset while a menu using it was still on the stack (e.g. play-again arriving while another menu is open). The round-over/help/askinput handlers were extracted into `handle_roundover/handle_helptext/handle_askinput` so both the live branch and the deferred-drain path call the same code.

Rule going forward: any NEW client blocking loop must pump `net_keepalive()`, and any NEW incoming message that opens blocking UI must go through the `netloop_depth>1 ? defer : handle` pattern. See [[path-conventions]].
