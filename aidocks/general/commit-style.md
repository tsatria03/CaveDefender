---
name: commit-style
description: "How CaveDefender commits are written: a general 'Major/Minor <area> enhancements.' subject, or a feature's changelog entry word for word; several entries go in the body under a general subject. When Claude makes a commit, a Co-Authored-By line IS allowed (unlike StrideRush)."
metadata:
  type: feedback
---

Commit messages follow the dev's own style, the same as their other NVGT games:
- Most commits use a one-line general subject: "Major <area> enhancements." or "Minor <area> enhancements." (for example "Major server enhancements.", "Minor dock enhancements.").
- A feature's main commit uses its changelog entry word for word as the message.
- When one commit covers several changelog entries, use a general subject with the entries in the body, newest first, one per line.
- Group commits by area (memory, code, sounds, build, server data), one commit per area, so each move or rename lands as its own readable block.
- **Memory (aidocks/ and CLAUDE.md) commits use the dock wording**, not a separate "memory" area: "Major dock enhancements." when many files change, "Minor dock enhancements." when only a few do (dev, 2026-11-24: "For memory files, you can just say major and or minor dock enhancements, depending on the file count."). The dev gave no exact cut-off, and it depends on the size of the changes as well as the file count (dev, 2026-11-24: "it can also depend on the file size as well, not just the count"): a reorganization, a sweep across many memories, or a big rewrite of even one or two files is Major; a small touch to a few files is Minor.

**Co-author lines:** when Claude makes a commit itself, adding a Co-Authored-By line is fine for CaveDefender. The dev said so on 2026-11-24 ("If you make commits yourself, you can add a co-author line"), noting StrideRush had some commits with it too. This deliberately differs from StrideRush's own memory, which asks for no attribution lines; follow this one in this repo.

**Who commits:** the dev makes their own commits by default (dev, 2026-11-24: "I'll start making the commits myself unless I need your help splitting large commits."). Claude only commits when the dev asks, typically to help split a large pile of changes into per-area commits; otherwise just report what changed and, for a big pile, suggest a split.

**Never push.** Claude may make commits when asked, but pushing is always the dev's job (dev, 2026-11-24: "Do not push any commits. I'll do that myself."). Don't push, don't offer to push, and don't push tags; just report that the commits are local and ready. The one exception is when the dev explicitly asks Claude to push a specific thing: on 2026-11-24 they asked Claude to do the history-rewrite FORCE push ("I can handle simple pushing, but I don't know much about force pushing"), which Claude did with --force-with-lease after confirming GitHub hadn't moved. That was a one-off, not a standing permission.

**How to apply:** only commit when the dev asks ([[check-git-log-for-commits]]). Before a big commit, tell the dev how many entries git shows and roughly what they are ([[stage-commits-before-big-changes]]). Never commit player account data from cf/server/data/players without the dev's explicit say, since the repo is public. Related: [[changelog-rules]].
