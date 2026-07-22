---
name: no-crlf-normalization
description: Do NOT run python CRLF-normalization passes after edits; git handles line endings on commit. Carried over from SimpleFighter (same dev).
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

Do not run a post-edit python CRLF normalizer (`d.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n')`) after file edits. The dev's git setup (`.gitattributes` eol=crlf + commit-time normalization) converts line endings automatically when they commit.

**Why:** The normalization step adds noise to every turn and is redundant. Guidance to author new file CONTENT with CRLF still applies (don't deliberately write LF-only files), but no post-edit fixup pass is wanted.

**How to apply:** After Edit/Write calls, just stop — no Bash normalization step. Related: [[list-modified-files]].
