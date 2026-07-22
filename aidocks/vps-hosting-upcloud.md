---
name: vps-hosting-upcloud
description: "The dev hosts the CaveDefender server on an UpCloud Windows Server VPS; firewall needs one inbound UDP 25562 rule in Windows Defender Firewall (UpCloud's panel firewall left disabled)"
metadata: 
  node_type: memory
  type: project
  originSessionId: e1f5da55-9f97-4238-93af-1b847784dab5
---

As of July 16, 2026 the dev runs the public CaveDefender server on a **Windows Server VPS at UpCloud** (upcloud.com). Setup facts confirmed working:

- The game's ENet networking is **UDP**; the server listens on port **25562** (conf.svr `port=`, see [[accounts-system]] / [[networking-protocol]]).
- Only ONE firewall rule was needed: an **inbound UDP 25562 allow** in Windows Defender Firewall inside the VM (`New-NetFirewallRule -DisplayName "CaveDefender Server" -Direction Inbound -Protocol UDP -LocalPort 25562 -Action Allow`).
- UpCloud's control-panel network firewall ships disabled and the dev left it off — no rule needed there.
- Clients connect to the VPS public IPv4; the game already forces IPv4 ([[nvgt-ipv6-networking]]).
