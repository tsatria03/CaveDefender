---
name: screen-reader-crash-filter
description: "The cryptic regex patterns in filter_crash() are screen-reader/TTS crash strings (Eloquence/IBMTTS under NVDA), NOT nonsense placeholders — never remove, weaken, or bypass them"
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

The cryptic regex patterns in `filter_crash()` (server `includes/main/functions/filterfuncts.nvgt`) are **screen-reader crash strings** — character sequences that crash or hang TTS engines (Eloquence, IBMTTS under NVDA) when spoken. They are NOT placeholder or nonsense filters, even though they look random. A malicious player who broadcasts one in chat would crash every other player's screen reader, because the client speaks received chat — a real DoS attack in blind audio games.

**Why:** players rely on TTS; a crash string sent in chat takes down their speech output. This is a safety/security feature, not profanity filtering.

**How to apply:** `filter_crash()` is hardcoded ON PURPOSE and must stay that way:
- Always on, applied to **every** text chat channel — global on any language **including Unfiltered**, local, and staff. The Unfiltered channel only exempts the *profanity* filter (`filter_chat`), never `filter_crash`.
- Never move these patterns into the host-editable `data/preffs/chatfilter.svr` (a host could delete them); never gate them behind `filterstuff` (that switch is only for `filter_chat`).
- Matching lowercases the message, so the patterns must be lowercase (an uppercase pattern silently never fires — that bug had left the `eur...` rule dead).

`filter_chat()` (host profanity words, from `chatfilter.svr`, Unfiltered-exempt for global) is a separate, deletable layer — don't confuse the two. Related: [[regex-filter-dll-removed]].
