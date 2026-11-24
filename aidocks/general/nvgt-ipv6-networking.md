---
name: nvgt-ipv6-networking
description: "NVGT's network class defaults to IPv6/dual-stack, which breaks hosting over IPv4-only VPNs (Radmin); CaveDefender forces IPv4 with net.IPV6enabled=false"
metadata: 
  node_type: memory
  type: project
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

NVGT's built-in `network` class defaults to **IPv6/dual-stack** (`IPv6enabled = true` in Legacy-NVGT `src/network.cpp:35`). With it on, `setup_server` binds to IPv6 ANY (`::`) and `connect` resolves addresses as ANY. Symptom: **localhost works but a real IPv4 address does not** — including a host connecting to its *own* Radmin VPN IP. No firewall rule fixes it, because the IPv4 packets never land on the IPv6-bound socket. (BGT games work on Radmin because BGT is pure IPv4, binding 0.0.0.0.)

Discovered 2026-06-15 debugging why nobody (not even the host via its own Radmin IP 26.177.181.27) could connect, while BGT games and localhost worked.

**Fix (script-level, no NVGT rebuild):** set `net.IPV6enabled = false;` BEFORE `setup_client` / `setup_server`. The script-facing property name is `IPV6enabled` (capital V6), even though the C++ member is `IPv6enabled`. Applied in:
- client `cfc.nvgt` — right before `net.setup_client(5, 500)`
- server `cfs.nvgt` — right before `net.setup_server(port, 5, 500)`

Must be set on BOTH sides so the address family matches. This makes NVGT bind/resolve pure IPv4 like BGT, so VPN/LAN IPv4 hosting works. If IPv6 support is ever wanted later, this is the switch to revisit.
