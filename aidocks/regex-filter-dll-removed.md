---
name: regex-filter-dll-removed
description: "Why CaveDefender's server no longer uses filter.dll/regex.dll and how the word filter works now"
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

The server's chat word-filter originally depended on an external `filter.dll` (a.k.a. `regex.dll`) loaded via `library`/`re.call(...)` in `server/includes/regex.nvgt`. That DLL was a **32-bit BGT (Blastbay Game Toolkit) community plugin** exposing a `regex_create`/`regex_compile`/`regex_match`/`result_ismatched` API. It cannot work in modern NVGT: NVGT is 64-bit and a 64-bit process can't load a 32-bit DLL, and no 64-bit build of that plugin exists. (Note: GnuWin32's `regex2.dll` is unrelated — it's 32-bit GNU/POSIX regex with `regcomp`/`regexec`, a different API entirely. Don't go down that path.)

**Why:** Hunting for the DLL is a dead end, and NVGT ships PCRE regex natively via the built-in `regexp` class — so the plugin's whole reason to exist is gone.

**How to apply:** `regex.nvgt` now just does `regexp re(pattern); return re.match(message);`, keeping the same `regex(string message, string pattern)` signature its only caller `filter()` (in `server/includes/net.nvgt`) uses. In `filter()`, rules prefixed `re=` are PCRE patterns (matched via `regex()`); rules without the prefix are literal case-insensitive substring matches. The existing `re=` patterns are already PCRE-compatible. If a binary BGT plugin is ever missing again, prefer a native NVGT equivalent over finding/porting the DLL — see also the broader rewrite work in [[cavedefender-overview]].
