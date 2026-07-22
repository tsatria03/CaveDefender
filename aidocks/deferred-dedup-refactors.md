---
name: deferred-dedup-refactors
description: Deferred-as-too-risky refactors — /promote↔/demote merge, client preset menus, and splitting the two giant netloop dispatch functions
metadata: 
  node_type: memory
  type: project
  originSessionId: 08cf857d-410c-46d7-a1c0-4e573399708d
---

From the 3.0 code evaluation, several refactors were **deliberately left undone** because they're risky (twins that hide real behavioral differences, or huge functions) and best done in their own focused sessions. The safe parts of item 7 ("heavy duplication") were already done: `reply_target_not_found()` (11 not-found sites) and `resolve_mute_target()` (the shared /mute↔/unmute preamble), both in `src/server/includes/main/globals/net.nvgt`.

**Timing:** the user wants all of these (especially the big netloop split) held until **3.0 is completely finished** — don't start them mid-3.0, so a large risky refactor never tangles with in-flight feature work.

**Still deferred — fix carefully when revisited:**

1. **`/promote` ↔ `/demote`** (server `net.nvgt`, the two command handlers). They look like twins but genuinely diverge: different valid-rank sets (promote: moderator/administrator/developer; demote: player/moderator/administrator), **opposite direction checks** (promote requires new rank *above* target's current, demote *below*), and `/demote` has an extra `is_owner()` guard that `/promote` lacks. Don't fully merge — extract only the common pieces (target lookup already uses `reply_target_not_found`; the grant-cap "above your own rank" check and the set_rank+broadcast+audit tail are the mergeable parts). Keep the direction/rank-set logic per-command.

2. **Client server-preset vs account-preset menu machinery** (`src/client/includes/main/menus/menu.nvgt`). Parallel copies: `addserver`/`addaccount`, `editserverdetails`/`editaccountdetails`, and the `loadserver`/`loadaccount`, `removeserver`/`removeaccount`, `editserver`/`editaccount`, `serverstorage`/`accountstorage` submenu families — hundreds of lines. Differ in fields (server: name/address/port; account: username/password), password masking, and the sound-device index off-by-one convention nearby. Largest single duplication surface. A generic "prefs list CRUD + form" helper would collapse it, but it's the riskiest merge — do it as its own focused session with careful diffing.

3. **The two giant `netloop` dispatch functions** (evaluation item 6 — a maintainability, not-duplication, deferral). Server `netloop()` in `src/server/includes/main/globals/net.nvgt` is ~1,450 lines and the client `netloop_impl()` in `src/client/includes/main/globals/net.nvgt` is ~700 — each one enormous if/else-if chain dispatching the space-delimited protocol on `parsed[0]`. Split each into a **dispatch table / per-command handler functions** (the client already has a `dispatch_modal` pattern to mirror). Do the two sides in **separate focused sessions**, one command group at a time, keeping behavior identical — this is the biggest and riskiest single refactor, which is why it's deferred. NOTE: the protocol is a client/server contract, so a handler rename/move on one side must keep the wire strings identical to the other (see the CLAUDE.md networking rule).

See [[command-parser-conventions]] and [[formatting-deferred]].
