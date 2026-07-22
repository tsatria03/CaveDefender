---
name: ban-tiers-and-hwid-limits
description: "The three ban tiers (account/IP/machine), how ipbans.svr & compbans.svr would be shaped, and the hard engine finding that a TRUE hardware ID is not achievable in this project — pure NVGT can't read hardware and GameEngine64.dll can't be modified."
metadata: 
  node_type: memory
  type: reference
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
---

Design exploration (not built — recorded for later) of how banning could extend beyond the current account ban.

**Three ban tiers, escalating toughness to evade:**
1. **Account ban** — `banned.usr` on the account (BUILT). Checked after login. Evaded by making a new account.
2. **IP ban** — a hypothetical central `ipbans.svr`. Survives new accounts; evaded by changing IP (and near-useless over Radmin/VPN where addresses are shared/virtual — only meaningful on a real public VPS with distinct public IPs). See [[nvgt-ipv6-networking]].
3. **Machine / HWID ban** — a hypothetical central `compbans.svr`. Survives new account, IP change, OS reinstall, and VPN. **Correction to the intuitive framing:** a NEW computer DEFEATS it (different hardware = different id) — its strength is surviving everything short of new hardware, not being unbeatable.

**Why ipbans/compbans are central .svr files, not .usr:** an address or machine is not owned by any account (could belong to several or none), so it has no per-account home. They'd be delimited-record `.svr` files (like `reports.svr`), reusing `banned.usr`'s duration scheme: absent = not banned, `0` = permanent, `>0` = epoch expiry. Not an index/cache of account bans — a primary store of a different kind of ban. See [[accounts-system]].

**HARD ENGINE FINDING (checked against [[nvgt-engine-source-location]] functions export):**
- NVGT's `uuid_generate()` is **RANDOM (RFC 4122), NOT hardware-derived** — cannot fingerprint a machine.
- **No** disk-serial / MAC / motherboard / Windows `MachineGuid` API, **no** registry read, **no** command execution (no run/exec/system/popen). `PROCESSOR_COUNT`, `PROCESSOR_ARCHITECTURE`, `process_id` exist but aren't machine-unique.
- Therefore a TRUE hardware id is **not achievable in pure NVGT script.**

**Route B (add get_hwid to GameEngine64.dll) is OFF THE TABLE:** that DLL is external, third-party, written in PureBasic, and NOT the dev's to modify — its only job is spawning map objects. See [[game-engine-dll]].

**What's actually reachable today = Route A, the "install ID":** `uuid_generate()` once on first launch, stored in client appdata (see [[path-conventions]]), sent at login, banned in `compbans.svr`. Weak: it's an install fingerprint, not hardware — deleting the file, a fresh install, a different Windows user profile, or a new PC all mint a new id. A genuine HWID would need a brand-new separate native DLL loaded via `library` (a real project, outside the current toolset).

**Universal caveat:** any client-sent id (install-ID or true HWID) is client-reported, so a modified/patched client can spoof or randomize it. HWID bans are spoof-resistant, never spoof-proof.

**Bottom line:** account + IP bans are genuinely buildable and enforceable; the machine tier tops out at the weaker install-ID form unless new native code is introduced.
