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

**Empty slot (dev-locked):** pressing a key whose line is blank/missing speaks exactly `"scriptkey N not found"` (N = the key's 1–28 number) and does nothing else.

**Live update (dev-locked):** NO persistent in-memory copy — RE-READ scriptkeys.txt fresh on every script-key press (the `file` object; presses are user-initiated + the file is tiny, so cost is nil), so a hand-edit is live on the next press with no restart/reload/watcher. This means `scriptkeys.txt` MUST stay a LOOSE editable file next to the game and be EXCLUDED from the Enigma box AND any pack (dev-confirmed) — otherwise players can't edit it.

**Boxing/build — DONE & verified:** the box already excludes it structurally — `src/client/cfc.evb` never references it, and `scripts/gen_cfc_evb.py` only embeds `EMBED_FOLDERS = ["sounds","docks"]` + fixed lib DLLs, so a `cf/client/` ROOT file is never boxed (and the post-box strip only removes embedded sounds/docks/DLLs, never root files). The gap was that `build/tools.py compile_side` copied only `["lib","sounds","docks"]`, so the root file wouldn't ship — fixed by adding a `loose_files` param + `CLIENT_LOOSE = ["scriptkeys.txt"]` (SERVER_LOOSE = []), copied into the bundle root next to the exe. So it ships loose, editable, unboxed. See [[enigma-boxing]], [[path-conventions]].

**Loader/executor/bindings — BUILT (client, `includes/main/globals/scriptkeys.nvgt`):**
- `read_scriptkeys()` — reads `scriptkeys.txt` fresh each call (missing/unreadable → empty array), reusing `split_lines()` (extrafuncts) which CRLF-normalizes and keeps blank lines so line N stays mapped to key N. Path is cwd-relative `"scriptkeys.txt"` (cwd = `cf/client/` in dev, bundle root in release).
- `resolve_scriptkey(line)` — splits on `%`; head is literal; each following segment's prompt text runs to the next `%` with TRAILING whitespace peeled off and kept as a literal arg-separator (so `/pm %who? %what?` → `/pm <a> <b>` with the space preserved); asks each via `vd.input_box("Script key", prompt, "")`; returns "" if any prompt is cancelled/blank (→ abort). Final text goes through `comparse()`.
- `run_scriptkey(n)` — empty/missing slot → `speak("scriptkey N not found")`; else resolve → comparse.
- `scriptkey_loop()` — returns bool (fired?). Guards: `!connected or reconnecting` → false; requires `alt_is_down() and !control_is_down()`. Local `uint[] row = { KEY_GRAVE, KEY_1..KEY_0, KEY_MINUS, KEY_EQUALS, KEY_BACK }` (14; built AFTER the alt guard so it's free when Alt is up). `key_pressed(row[i])` → `n = i+1 (+14 if shift)` → run. KEY_BACK = backspace (engine: SDL_SCANCODE_BACKSPACE); keys are `uint` and `key_pressed(uint)` per the codebase idiom (afk_wake_key_pressed).
- Wired in `game.nvgt` main loop right after the AFK/auto-afk block (`else activity_timer.restart();`) as `if(scriptkey_loop()) continue;` — only reached in the ACTIVE state (frozen/paused branches `continue` earlier), so it works in lobby/room/game/watching. Plain number row is weapon quick-equip (`weapon_hotkey_loop`), so requiring Alt keeps them clear; scriptkey_loop runs before it and continues, so Alt+number never leaks to weapon-equip.
- Docs: changelog entry + readme "Script keys." section (NOT the player help — help is slash-commands-only). Todo Finished. Sample `cf/client/scriptkeys.txt` shipped loose. Build copies it loose via `CLIENT_LOOSE` (see above).

**Design notes for future:** while AFK, a script key press wakes you (any non-modifier key does) rather than firing — acceptable. Prompts are single-line (chat is single-line); empty answer == cancel (vd.input_box returns "" for both). The whole feature is BUILT & awaiting dev test.
