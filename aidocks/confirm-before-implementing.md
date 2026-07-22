---
name: confirm-before-implementing
description: "User has repeatedly experienced Claude over-implementing — treat every design discussion as a question, never a commission. Carried over from the SimpleFighter project (same dev)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

Treat every design discussion as a question requiring explicit go-ahead — never a commission. "I really wish X" / "what if we did Y" / "could we extend Z" / "I have an idea" are explorations, not instructions. Lay out the design, call out tradeoffs, ask for go-ahead. Stop and wait.

**Why:** The user has repeatedly observed Claude over-implementing despite explicit guardrails (this was a recurring frustration on the SimpleFighter project). They tried `permissions.defaultMode: "plan"` as system-level enforcement but turned it off — the approval friction was too high for routine work. So the rule rests **entirely on instruction-following**; there is no permission-layer backstop, which makes vigilance more important, not less.

**How to apply:**
- Default to asking "want me to proceed?" before any Edit/Write/destructive Bash, even when the design feels obvious or small.
- Never bundle implementation into the same turn as a proposal — split the proposal turn from the implementation turn so the user can redirect.
- Never fan out into adjacent files unprompted (help topics, changelog entries, memory files alongside the main change) — each side-effect deserves its own go-ahead.
- **Hard rule: a message ending in `?` is a question, full stop.** No exceptions. Even when it reads like a polite imperative ("Could you fix the bug in X?"), respond with info or a plan and *wait* for "yes" / "go ahead" / "do it."
- **Treat information-seeking imperatives as questions too**, even without a `?`: "explain X", "tell me about X", "describe X", "walk me through X", "summarize X", "what is X", "what does X do".
- **Question shapes to recognize:** WH-questions (what/why/how/when/where/who/which); polarity (is/are/do/does/have/will); modal (can/could/would/should/might); idea framings (what if, wouldn't it be cool if, I was thinking); preference solicitations (I wish X, what do you think); comparisons; status checks.
- **Exceptions** (imperatives, proceed without re-asking): direct unambiguous commands without `?` ("rename X to Y", "install it", "go ahead", "do it", "yes please", "delete this"), follow-ups within an already-approved task, or bug fixes the user explicitly asked for in the same message.

Related: [[list-modified-files]].
