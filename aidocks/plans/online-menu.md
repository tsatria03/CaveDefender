---
name: online-menu
description: "PLANNED (2026-11-25) — main menu > game menu becomes a small submenu whose first item is a new online menu; the online menu holds everything the old connection menu had (sign in, accounts, server IP/port, storage). First step toward offline play; 'connection menu' wording becomes 'online menu' in code, spoken messages and docs."
metadata:
  type: project
---

**Idea (dev, 2026-11-25):** "put the options found in the game menu into a new online menu. So when you open game menu, you'll see online menu." It came out of a talk about offline play (LAN or localhost servers, no internet). The game menu is meant to have room for more items later, such as an offline option. Nothing offline is in scope here.

**Today:** client `src/client/includes/main/menus/menu.nvgt`. `mainmenu()` line 7 lists "game menu" (id "connect") and calls `connectionmenu()` (line 421). That holds: Sign in as <name> (only when an account is set), Set up an existing account, New account, Account storage, change server IP, change server port, Server storage, back. Its intro is "Game menu.". `login()` returns into that menu's loop when a session ends (exit, kick, drop), so the player lands back there. `connectionmenu()` has only the one caller. The server's in-game "Game menu" (`send_menu(peer, "leavemenu", "Game menu", ...)` in server menu.nvgt) is a different menu and is not touched.

**Sections:**

1. **Client menus (code).** In menu.nvgt add `gamemenu()`: items "online menu" and "back", intro "Game menu.", escape acts as back, built in the same `setupmenu(true)` / `while(true)` style as the other menus. Rename `connectionmenu()` to `onlinemenu()` and change its intro to "Online menu."; its items and behavior stay the same. `mainmenu()`'s "game menu" item now calls `gamemenu()`. When a session ends you still land in the online menu; back goes to the game menu, back again to the main menu.

2. **Spoken messages and code comments (client + server).** The client says "returned to the connection menu" in six messages (`globals/net.nvgt` ~1101, 1118, 1127, 1136, 1146, 1155). Change them to "online menu" so they name the menu the player actually lands in. Update the code comments that say "connection menu" (client menu.nvgt, net.nvgt, game.nvgt, savefuncts.nvgt, storage_presets.nvgt, cfc.nvgt; server net.nvgt) to "online menu". No wire strings change, so no protocol bump is needed beyond the existing 5.3.

3. **Docks (final section, [[final-section-dock-updates]]; merged from three at the dev's request, 2026-11-25).**
   - Server docs: change "connection menu" to "online menu" in `cf/server/docks/help/player.txt` (lines 25, 26, 28), `help/staff.txt` (34, 53, 54, 55) and `rules/player.txt` (5).
   - Client docs: readme.txt line 7, "Choose the game menu to open the connection menu, where you pick a server and sign in" becomes "Choose the game menu, then the online menu, where you pick a server and sign in". Line 404, "return to the connection menu" becomes "return to the online menu". One new entry at the top of the 5.3 changelog block (5.3 is unreleased; [[changelog-rules]]). Older changelog and todo-list lines stay as they are, because they record what was true then.
   - Memories: update [[include-tree]] (menu.nvgt now holds `gamemenu()` and `onlinemenu()`), [[accounts-system]] and [[feature-ideas]] where they say "connection menu"; mark this plan COMPLETE and update its MEMORY.md line.
   - Recheck every edited dock line against [[dock-line-length-1024]] (900 recommended).

**Q&A log:**
- (none yet)
