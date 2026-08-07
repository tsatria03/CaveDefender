---
name: scriptkeys
description: Script keys — Alt/Alt+Shift number-row hotkeys that run lines from cf/client/scriptkeys.txt as chat commands, with %prompt placeholders. Plus the /gl /lc /st /tm channel-routing commands (DONE). Read before building the key loader/executor or touching the channel commands.
metadata:
  type: project
---

**Feature (dev, 2026-08, 5.0):** client-side "script keys" — user-defined keyboard shortcuts that run a slash command (or plain chat) from anywhere. Config file `cf/client/scriptkeys.txt`, one command per line, line N → key N by position.

**Keys (28 total):** Alt + `` ` `` 1 2 3 4 5 6 7 8 9 0 - = Backspace = keys 1–14; Alt+Shift + those same keys = keys 15–28. Fire anywhere you have normal control (NOT while a menu or the chat box is already open — those capture input). Blank/missing line = that key unbound.

**Grammar (dev-locked):**
- A line is interpreted exactly like text typed into a chat box: leading `/` = command, otherwise = GLOBAL chat (a script key has no channel context, so slash-less text always goes global).
- `%` starts a PROMPT: text after it (until the next `%`) is the question shown in a single-field input box; the player's typed answer is substituted at that spot. Prompts are asked in order, left to right.
- No `%` at all → runs instantly (e.g. `/lb`).
- Cancel any prompt → the whole command cancels ("canceled"), nothing sent.
- NO reserved tokens: the original sample's `%user` (= last person who messaged you) was CUT to keep one consistent rule.
- No comment syntax (every line maps to a key by position, so a comment would consume a key slot).
- Execution = resolve all `%prompts` into the final text, then call `comparse(text)` (the normal client router), so rank gating and validation apply.

**Channel-routing commands — BUILT (client-only, in command_parser.nvgt, after the /channel block):** `/gl` global, `/lc` local, `/st` staff (staff only: `my_rank_level()<1` → unknown_command; hidden like other staff commands), `/tm` team where possible. Each re-runs the remainder of the line via `comparse(rest, <channel>)`, so plain text → that channel's chat and `/me` → that channel's emote, reusing the existing `localchat`/`staffchat`/`teamchat` + `localme`/`staffme`/`teamme` wire messages — NO new server code. Bare command (no text) → `syntax_error(base + " message")`. They solve the "which channel does /me use from a hotkey?" problem AND let you cross-post from any chat box (e.g. `/gl hi` from the local box). Docs done: player help (/gl,/lc,/tm), staff help (/st), changelog entry. See [[new-command-checklist]], [[command-parser-conventions]].

**STILL TO BUILD:** the scriptkeys.txt loader (read at client startup into an array of 28 slots), the `%prompt` executor (sequential single-field dialogs per [[input-prompt-form-vs-dialog]] — one field each, so a virtual dialog; cancel aborts), and the Alt / Alt+Shift key bindings wired into the client's global key handling (see game.nvgt input loop). Then its own changelog entry + readme section + player-help note + todo Finished. Discussed as sections: Section 1 = channel commands (DONE), Section 2 = loader+executor+bindings, Section 3 = docs.
