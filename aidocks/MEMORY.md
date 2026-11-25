# CaveDefender memory index

The [[name]] links across these memories resolve to aidocks/general/<name>.md or aidocks/plans/<name>.md. Add a one-line pointer here for every new memory, under the heading that fits. "Memory" always means this folder (see [[memory-folder-layout]]).

## Working style
- [Memory folder layout](general/memory-folder-layout.md) — memories live in aidocks/: general/ for topics, rules and references, plans/ for feature plans both open AND completed (a finished plan stays in plans/ as the record); MEMORY.md indexes both
- [Confirm before implementing](general/confirm-before-implementing.md) — treat design discussion as a question, never a green light; a `?` means respond and wait, don't edit
- [Ask one question at a time](general/ask-one-question-at-a-time.md) — when clarifying a plan, surface ONE question per turn and wait; don't batch a numbered list of questions
- [Verify code while fixing](general/verify-code-while-fixing.md) — when fixing, read the surrounding code carefully, confirm the finding's line numbers/claims are actually true (they drift), and catch/flag adjacent errors; don't blindly patch the reported spot
- [Check git log for commits](general/check-git-log-for-commits.md) — the user commits their own work between turns; check git log/status before asking about or assuming commit state; for section-built features verify each section's commit before the next
- [Commit style](general/commit-style.md) — "Major/Minor <area> enhancements." subjects, or a feature's changelog entry word for word (several entries go in the body); one commit per area; memory/aidocks commits are "Major/Minor dock enhancements." by file count and size of the change; Claude's own commits MAY carry a Co-Authored-By line here (unlike StrideRush); the dev makes their own commits (Claude commits only when asked, e.g. to split a large pile); Claude NEVER pushes
- [Stage commits before big changes](general/stage-commits-before-big-changes.md) — proactively flag a commit break point before a large/risky stage, so safe pieces get committed on their own and the big change stays isolated
- [Final section: dock updates](general/final-section-dock-updates.md) — when building a feature in sections, reserve the LAST section for changelog/readme/help; earlier sections are code only
- [List modified files](general/list-modified-files.md) — end every editing turn with a "Files changed:" list, bare filenames tagged with client or server (dev reviews via screen reader)
- [Relaunch notice](general/relaunch-notice.md) — after the Files changed list, say whether the server and/or client must be relaunched (.nvgt code = relaunch that side; data/docks = usually none)
- [Don't compile yourself](general/dont-compile-yourself.md) — never run cfcm.py/cfsm.py/nvgt -c; the user compiles and verifies builds themselves; just edit and report
- [Quoted text meaning](general/quoted-text-meaning.md) — when the user quotes text it's a reference (something said, wanted, or NOT wanted), not literal content to paste
- [No CRLF normalization](general/no-crlf-normalization.md) — don't run post-edit CRLF normalizer passes; git handles line endings at commit
- [CLAUDE.md length limit](general/claudemd-length.md) — keep CLAUDE.md under 40,000 chars; move detail to memory files
- [Sound placeholders](general/sound-placeholders.md) — when a sound is requested, wire up the playback code referencing the intended filename now; user adds the .ogg later. No dummy files
- [Formatting deferred](general/formatting-deferred.md) — consistent indentation (spaces/tabs) cleanup is wanted eventually for readability, but stays parked; no formatting passes unless the dev asks

## Player-facing text, docks and versions
- [One-sentence game messages](general/one-sentence-game-messages.md) — in-game feedback messages must be exactly one sentence; no trailing advice/instruction sentence
- [Yes/no menu labels](general/yes-no-menu-labels.md) — for a yes/no menu, label the two items just "Yes" and "No" (Yes first); put the context in the question line, not the option labels
- [Menus say canceled](general/menus-say-canceled.md) — every menu/input back, escape, or No path must speak("canceled")
- [Use dlgmessage](general/use-dlgmessage.md) — use dlgmessage() for all dismissable alerts and dialogs, never alert() or raw dlg()
- [Input prompt: form vs dialog](general/input-prompt-form-vs-dialog.md) — one field uses a virtual dialog; more than one field uses a real tabbable audio form, not a chain of sequential dialogs
- [Command full name before alias](general/command-full-name-before-alias.md) — in docks, write a command's full name before its short alias (e.g. /playerlist, or /prl)
- [Docks and help](general/docks-and-help.md) — client docks/ (changelog/credits/readme/todo) + server-authoritative /help and /rules pages; read when updating docs, help, or rules
- [Changelog rules](general/changelog-rules.md) — docks/changelog.txt: player-facing prose, sentence/entry caps, reverse-chronological, a record of what changed not a manual
- [Dock line length limit](general/dock-line-length-1024.md) — keep every line in the player-facing docks (server rules, server help, client docks) at or under 1024 chars; the user's screen reader splits longer lines
- [Todo list one sentence](general/todo-list-one-sentence.md) — every entry in docks/todo list.txt (finished or unfinished) must be ONE short sentence, not a run-on
- [Post changes: no changelog](general/post-changes-no-changelog.md) — a "post change" is a quiet pre-release touch-up; document in readme if needed, but no changelog entry and no version bump
- [Bump version.txt with each changelog block](general/dont-touch-version-txt.md) — bump build/version.txt to match each new "New in X.Y." changelog block; the dev's only override is temporarily setting it to another server's version for cross-server connection testing (their call to change back)
- [Release cadence batches versions](general/release-cadence-batches-versions.md) — dev batches versions; 4.1 done but won't ship until end of 4.2. While unreleased, ALL player-facing changes (features + fixes) go in the changelog, not the README

## Code conventions
- [Multi-line comment style](general/multiline-comment-style.md) — multi-line code comments use /* */ block style, not stacked // lines; single-line stays //
- [New command checklist](general/new-command-checklist.md) — adding/changing a slash command = update all 5 together: client router, server handler, both /help pages, changelog, identical wire strings
- [Command parser conventions](general/command-parser-conventions.md) — client comparse() is a router not a local executor; new commands validate args + call syntax_error(), feedback goes to misc buffer
- [Map helpers location](general/map-helpers-location.md) — map helper functions go in client functions/mapfuncts.nvgt, not extrafuncts; map state/core stays in globals/map.nvgt
- [No sound pack support](general/no-sound-pack-support.md) — CaveDefender will not have swappable sound packs (unlike SimpleFighter); sounds folder reorg was just for layout

## Project structure, build and hosting
- [Path conventions](general/path-conventions.md) — src/ (code: includes/game + includes/main) + cf/ (assets+launchers) + build/ + release/ + user/; the cwd trick; sounds/main + sounds/game; server data/equipments; players git-ignored; appdata; no boxing, no engine DLL
- [Include tree](general/include-tree.md) — includes.nvgt globs game/* FIRST, then each main/ subfolder (a glob doesn't reach subfolders); the 10 gameplay modules in includes/game; file-by-file map of what each client/server .nvgt owns
- [Launchers and running](general/launchers-and-running.md) — cf/<side> Python launchers (cwd trick, client errors.txt compile-watch, server under the downcheck supervisor with only its console visible), no test suite/linter, build/tools.py = compile, package, release (no boxing; 4-flag CLI; menu 1-10; tools.bat via py -3.12)
- [Enigma boxing (removed)](general/enigma-boxing.md) — HISTORY: release exes were packed with Enigma Virtual Box until the dev dropped it 2026-11-23; tools.py's box stage removed 2026-11-24; all assets ship loose now; don't reintroduce it
- [file_exists boxed-sound trap](general/file-exists-boxed-sound-trap.md) — HISTORY (boxing is gone, trap no longer applies) + the lasting rule: never gate sound playback on file_exists; detect optional sounds with a data/class flag
- [Game engine DLL (removed)](general/game-engine-dll.md) — HISTORY: GameEngine64.dll is GONE since 2026-07-14 (commit c26ac21), replaced by the native tile store in client game/platform.nvgt (handle-based spawn_platform/get_tile_at/remove_platform/clear_map); no DLL is loaded via library any more
- [VPS hosting on UpCloud](general/vps-hosting-upcloud.md) — the public server runs on an UpCloud Windows VPS; one inbound UDP 25562 rule in Windows Firewall is the whole network setup

## Engine, NVGT and AngelScript
- [Engine pinned to legacy NVGT](general/engine-pinned-legacy-nvgt.md) — game runs on the pinned legacy NVGT fork at C:\nvgt (source misc\Legacy-NVGT); C:\nvgt2 is the UNUSED miniaudio build; upstream NVGT is incompatible (miniaudio vs BASS); don't suggest upgrading
- [NVGT engine source location](general/nvgt-engine-source-location.md) — Legacy-NVGT C++ source is at misc/Legacy-NVGT; grep src/*.cpp Register* lines for authoritative API signatures (functions.txt can be stale); has file_get_date_modified/size
- [AngelScript indentation](general/angelscript-indentation.md) — NVGT ignores indentation entirely; don't flag uneven whitespace after edits
- [AngelScript brace-less if](general/angelscript-braceless-if.md) — a brace-less if/else governs one statement; adding a 2nd (e.g. m.fade_music) into a menu dispatch chain orphans the else → compile error → client won't launch
- [AngelScript reserved out](general/angelscript-reserved-out.md) — never name a variable "out" (reserved keyword); also watch in/inout/shared/final/from
- [NVGT key_pressed one-shot](general/nvgt-key-pressed-oneshot.md) — key_pressed() is consumed on first read each frame; read a key once and branch inside, never two sibling ifs reading the same key
- [NVGT sound preload cache](general/nvgt-sound-preload-cache.md) — sound.load caches decoded audio by filename; reusing a name for changing audio (voice clips) replays the old one. Use unique names or allow_preloads=false
- [NVGT sound device indexing](general/nvgt-sound-device-indexing.md) — get_sound_output_devices() index 0 = "No sound" (stripped via remove_at(0)), index 1 = "Default"; the trimmed list already starts with Default, so never add your own Default item
- [NVGT IPv6 networking gotcha](general/nvgt-ipv6-networking.md) — NVGT defaults to IPv6/dual-stack which breaks IPv4 VPN (Radmin) hosting; CaveDefender sets net.IPV6enabled=false before setup_client/setup_server
- [Opus voice engine](general/opus-voice-engine.md) — nvgt has the opus codec as a shared opus.dll plugin (needs #pragma plugin opus; dll in C:\nvgt\lib + cf/client/lib) + live mic capture (read_data/available_frames/flush_capture) + sound.push_memory playback for live voice
- [Virtual dialogs form backend](general/virtual-dialogs-form-backend.md) — vd class is a front-end over form.nvgt's audio_form; keyboard typing sounds live only in form.nvgt and play in every input box, so gating/toggling them there covers the whole game

## Networking, accounts and chat
- [Networking protocol](general/networking-protocol.md) — enet network class, 4 channels (0 control/1 chat/2 PM/3 voice), rscs123 encryption, space-delimited message contract; read before changing any wire message on either side
- [Blocking UI network keepalive](general/blocking-ui-network-keepalive.md) — client menus/dialogs/input boxes must pump net_keepalive() or enet drops the connection (10-35s); netloop_depth reentrancy guard defers nested modals
- [Reconnect persistence](general/reconnect-persistence.md) — the 45s disconnect hold-and-restore (server-side session hold, negative sentinel peer ids, restore_scope); read before touching disconnect/reconnect/held-player code
- [Accounts system](general/accounts-system.md) — server-side data/players/<username>/ folder-per-account, one .usr per field, Argon2id passwords, ranks & command gating, owner aliases, nicknames, command targeting; read before touching accounts/ranks/moderation/login
- [Nicknames](general/nicknames.md) — nickname.usr = display name; username stays identity; display_name* helpers return nickname; commands target username (Option 1, /who & /staff show it); /nick set/default + staff /nick username altname
- [Ban tiers and HWID limits](general/ban-tiers-and-hwid-limits.md) — account/IP/machine ban tiers, how ipbans.svr & compbans.svr would be shaped; hard finding that a true hardware id isn't achievable (NVGT can't read hardware; a real HWID would need a new native DLL) — install-ID is the ceiling
- [Screen-reader crash filter](general/screen-reader-crash-filter.md) — filter_crash()'s cryptic regexes are TTS crash strings (Eloquence/IBMTTS), not nonsense; hardcoded, all channels, never remove or bypass
- [Player-events lifecycle](general/player-events-lifecycle.md) — lifecycle notices split: actor → first-person misc, everyone else → third-person player-events via broadcast_event(); server-wide, flag-aware, no AFK-prefix
- [Commands usable while AFK](general/commands-usable-while-afk.md) — players can run slash commands while still AFK; command broadcasts about the actor must be AFK-aware (afk_prefix), unlike lifecycle notices

## Gameplay and audio
- [Game vision: Wallbreaker](general/game-vision-wallbreaker.md) — CaveDefender's gameplay is a multiplayer, server-authoritative remake of Sammy Center's "Wallbreaker" (defend 4 walls, gather wood, repair vs. enemies)
- [EVP game mode](general/game-mode-evp.md) — as-built reference for EVP (Environment versus Player), the reverse of PVE Wallbreaker (players smash walls from outside, bots build); BUILT and feature-complete
- [Free Play game mode](general/game-mode-free.md) — AS-BUILT reference for the 4th mode, a solo/open sandbox shipped whole in 4.4: empty cavern you stock via Cavern controls (Tab), Enter arena menu with Begin arena + one-way Enable wall damage ricochet lock, self-healing walls, both toolkits live; BUILT and feature-complete 4.4a-e, tested end to end
- [Game host client sync](general/game-host-client-sync.md) — client gates host controls on current_game_host==name, kept in sync with server host_peer via the gamehost broadcast (announce_game_host at every migration site); read before touching host migration, the round menu, or host hotkeys
- [Ranged weapon architecture](general/ranged-weapon-architecture.md) — as-built ranged weapons: ammo+reload, a server-authoritative bullet that hits WALLS ONLY (never players), synced via the resolve-on-fire A-plus model; BUILT (server bullet.nvgt)
- [Game data-file layout](general/game-data-file-layout.md) — the data-driven file tree for weapons/items (cf/server/data/equipments/{weapons,items} since the 2026-11 reorg), extensions (.mel/.exp/.arc/.art, .mtr material, .amt ammunition), the 4 wood types + 5 ammo types, and what each file configures; read before building the data loader
- [Audio and sounds](general/audio-and-sounds.md) — sound_pool/HRTF model and THE current cf/client/sounds/ folder map (main/ui, main/misc, game/equipments, game/objects/audio, game/objects/construction); sound paths travel in network messages, so a folder rename is a protocol change; read when wiring a sound or referencing a sound path

## Open backlogs
- [Feature ideas backlog](general/feature-ideas.md) — living list of candidate FEATURE ideas to fill the PVP gap + general enhancements (achievements, difficulty selector, enemy variety, defender traps, power-ups, co-op scaling; leaderboard + learn-sounds already on the todo); MAINTAIN it: update whenever the dev promotes an idea to the todo or asks me to brainstorm. Includes the fleshed-out leaderboard design
- [Internal code improvements](general/internal-code-improvements.md) — player-INVISIBLE backlog from the 4.5 review: 10 structural refactors/dedup remain (god-functions, ring-geometry copy-paste, taxonomy twins, helper twins, quick-win consts). ALL correctness items cleared in 4.6 (buffer/token guards, MOTD write, filter cast, player-cap const, enemy_attacks deferred-removal); menu-result bounds verified not-a-bug.
- [Deferred dedup refactors](general/deferred-dedup-refactors.md) — risky refactors left undone for their own sessions: /promote↔/demote merge, client preset menu machinery in menu.nvgt, and splitting the two giant netloop dispatch functions (server ~1450 / client ~700 lines)

## Plans (aidocks/plans/)
Feature plans, open and completed; a finished plan stays here as the record.

Open (the late-2026 reorganization; suggested order: data, sounds, build, docs):
- [Data repointing](plans/data-repointing.md) — sections 1-4 DONE (loader, comments, server help docs, memories); optional missing-file warning skipped; left: the dev's in-game check
- [Sound path repointing](plans/sound-path-repointing.md) — DONE IN CODE (client + server; awaiting in-game test + 5.3): ~136 literal client sound paths + pieced paths + the footstep wire strings to the new sounds/main + sounds/game layout; ships as 5.3; approach decided: rewrite in place
- [Build tools: remove boxing](plans/build-tools-remove-boxing.md) — DONE: the Enigma stage is gone from tools.py (menu 1-10, CLI 4 flags); awaiting the dev's first real Compile only run
- [Reorg docs and version](plans/reorg-docs-and-version.md) — DONE: 5.3 changelog block (4 entries), version.txt 5.3, memory sweep (path-conventions, include-tree, audio-and-sounds, launchers-and-running, changelog-rules), boxing memories retired
- [Privacy cleanup](plans/privacy-cleanup.md) — MOSTLY DONE: player data untracked, history rewritten + force-pushed, dirty releases deleted; left: GitHub Support purge, optional player notice (no other clones exist)

Completed:
- [Chat channels](plans/chat-channels.md) — COMPLETE: Global (/), Local (\ current map instance, covers lobby/room/game), Staff (' all staff), Team (; PVP-only, your side); all four built
- [Voice chat mode feature](plans/cavedefender-voice-chat-mode.md) — COMPLETE: live-streaming vs record-then-send voice messages: prefs "Voice chat mode" list + tagged channel-3 wire format (l=live, m=message); confirmed working in-game 2026-07-06
- [PVP game mode design](plans/game-mode-pvp.md) — COMPLETE: full design spec + as-built reference for PVP (humans on both sides, real inside/outside, team chat, muffled cross-wall audio); built 3.1-3.2, hidden in 4.7, rebuilt and back in the start-game menu since 5.0
- [PVP recode rationale](plans/pvp-recode-rationale.md) — COMPLETE: why PVP was pulled in 4.7 and what the recode had to fix (the uneven inset-ring map split); recode done and PVP revived in 5.0 with equal inside/outside space
- [User-facing improvements](plans/user-facing-improvements.md) — COMPLETE: player-visible bug backlog from the 4.5 review, ALL CLEARED in 4.6 (case-match fix, ban/kick enforcement, movement bounds-clamp); full anti-teleport consciously deferred as disproportionate
- [Free Play planned enhancements](plans/free-play-planned-enhancements.md) — COMPLETE: all six free-play items built in 4.6 (open-start needs 2+ players, pause, builder bots, bots on wall recovery, continuous items, guest cavern access), with the exact cavern prompt wording; refill rate adjustable since 5.1
- [EVP build-phase wall % bug](plans/evp-build-phase-wall-percent-bug.md) — COMPLETE: fixed in 4.7 and confirmed in-game; EVP walls ramp visibly to the round's fortify target across the build phase (evp_fortify_from + evp_build_fortify_tick), the wave-start top-up stays as the skipped-build safety net
- [Learn Sounds menu design](plans/learn-sounds-menu.md) — COMPLETE (built in 5.0, Alt+L anywhere): main-menu sound-preview browser on form_menu.nvgt's learn_game_sounds_menu helper, categories mirroring the sound folders, "<Subject> <Action>: used in <modes> mode" descriptions
- [Onoff sounds](plans/onoff-sounds.md) — COMPLETE (shipped 5.0, fixes 5.1): per-account custom online/offline connect sounds, base64 over the protocol (getonoff/onoffdata) + client-side cache-and-reuse
- [Script keys](plans/scriptkeys.md) — COMPLETE (shipped 5.0, pronoun codes 5.2): Alt/Alt+Shift number-row hotkeys running cf/client/data/scriptkeys.srk lines as chat commands with %prompt placeholders, plus the /gl /lc /sc /tm channel commands
- [Soundboard](plans/soundboard.md) — COMPLETE (shipped 5.0): /playsound (/pls) plays a server-hosted clip to everyone, base64 stream + per-session client cache, path-safe + rank-scoped (players → player/, staff → +staff/), menu picker reusing the editdata browser
