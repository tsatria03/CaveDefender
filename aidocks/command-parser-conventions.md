---
name: command-parser-conventions
description: "How CaveDefender's client slash-command parser works and the rule for adding new commands"
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

CaveDefender's slash commands are handled by `comparse(string)` in `client/includes/main/parsers/command_parser.nvgt`, called from the in-chat slash dialog in `game.nvgt` (press `/`). Because the game is **online**, this parser is a **router, not a local executor** — unlike SimpleFighter's offline `comparse()`. Plain text → public chat on channel 1; recognised slash commands are forwarded to the server on the channel its handler expects (0 = control, 1 = chat); unknown commands → `add_buffer_item("misc", "Unknown command: ...")`.

**Rule for every new command:** validate its own argument count first, and on bad syntax call `syntax_error("usage text")` — a shared helper that speaks and logs `Invalid command syntax. Usage: <usage>.` to the misc buffer (the SimpleFighter style). Only after the check passes, route the command to the correct channel. All command feedback (usage errors, unknown command, plus the ping/uptime results) goes to the **misc** buffer via `add_buffer_item`, which both speaks and logs.

**For commands with optional arguments, show BOTH forms in the usage text** (the helper appends the trailing period). Example: `/mute` takes an optional seconds → `syntax_error("/mute username, or /mute username seconds")` → "Invalid command syntax. Usage: /mute username, or /mute username seconds." Do this for any command where an argument can be omitted, so the player sees both the short and long form.

Commands route on channel 0 (`/who`, `/uptime`/`/serveruptime`, `/getmotd`, `/staff`, `/restart`/`/rt`, `/fastrestart`/`/ft`) or channel 1 (`/pm`, `/motd`, `/kick`, `/promote`, `/demote`, `/mute`, `/unmute`, `/notify`, `/notifyplayer`/`/notplayer`). The server enforces rank gating (`/exit` was removed). When adding a command, remember the server side must understand it too — see the protocol contract in [[path-conventions]].
