---
name: evp-build-phase-wall-percent-bug
description: 4.7 todo/bug — in EVP the wall % doesn't visibly escalate during the build phase on later rounds; root cause traced (escalation is a wave-start top-up, not a build-phase climb), NOT YET FIXED
metadata:
  type: project
---

**FIXED in 4.7 (Option A, the ramp) — CONFIRMED working in-game by the dev.** The build phase now visibly climbs to this round's target; no more confusing snap. Todo item moved to Finished. Implementation: (1) `double[] evp_fortify_from` snapshot on the game struct, filled at EVP build start (`set_game_phase`, build/evp branch) with each wall's health in WALL_DIRS order; (2) `evp_build_fortify_tick(gi)` called from `gametick` (right after `maintain_cavern_items`) ramps each standing wall from its snapshot up to `maxhealth * evp_fortify_mult(evp_rounds_cleared)` by `phasetimer.elapsed/buildduration`, raising health + floor only when below the ramp (so bot work on top is never pulled down) and broadcasting `wallstr` only on an integer-percent change; (3) the wave-start top-up (`game.nvgt` ~620) is KEPT as the safety net for a SKIPPED build (Ctrl+S) — a no-op after a normal full build since the ramp already reached target. Server-only, EVP-only. Changelog'd under 4.7 (version.txt still 4.6 — dev bumps it). The original investigation is retained below for reference.

---

**Original investigation (symptom + root cause).**

**Symptom (dev's report):** In EVP, during the build phase of round 2 and beyond, the wall-strength readout (N/E/S/W/D keys) does NOT reflect the higher fortification the later round is aiming for — it keeps showing roughly the round-1 build level (~150% or lower). The big numbers (e.g. ~700% on round 10) only appear later, so it looks like the "new goal" the bots are building toward never shows during build.

**Root cause (traced, believed correct — confirm before fixing):** This is NOT a stale/cached value. The client stores exactly what the server sends (`client/net.nvgt` wallstr handler ~1158), and the server recomputes `health/maxhealth*100` live and broadcasts on every builder placement (`builder.nvgt:173`). `maxhealth` is a constant 400 (`wall_base_health`); wall_percent can exceed 100. All accurate.

The escalation is delivered as a **one-shot guaranteed top-up at WAVE START**, not during the build phase:
- `game.nvgt:614-623` (phase becomes "wave"): loops the four walls and bumps each to `maxhealth * evp_fortify_mult(evp_rounds_cleared)`. THIS is the jump to 650-700%.
- `evp_fortify_mult` (`gamedata.nvgt:210`) = `evp_fortify_base(1.5) + rounds_cleared * evp_fortify_step(0.5)`. Round 1 (rounds_cleared 0)=150%, round 10=600%, round 11=650%.

During the **build phase** the bots fortify on their own toward that same cap (`builder.nvgt:162`), but are bottlenecked by two things that are IDENTICAL every round, so the wall % plateaus at ~the same build-phase level regardless of round:
1. Wood drop rate is constant per map size (fixed `woodtimer` cadence) — ~same total wood per build window.
2. Builder count caps at 8 (`evp_builders_for_round`, `builder.nvgt:30`), reached by round 5 — no extra building past then.

The code comment at `game.nvgt:611-613` already acknowledges the build "can't leave the round soft," which is exactly why the wave-start top-up exists — the build routinely falls short of the target.

**So: working as written, but the design hides the escalation during build.** The readout is correct; it just doesn't climb round-over-round DURING build, only jumps at wave start.

**Possible fixes (not chosen, not implemented):**
- Apply the fortify top-up (or a fraction) at BUILD start too, so the walls open the build phase already at/near this round's target and the escalation is visible immediately.
- Or scale the wood-drop budget / lift the builder cap per round so the bots actually reach the higher cap within the build window.
- Or, if it's really just a display expectation, announce this round's target on build start.

As-built EVP reference: [[game-mode-evp]]. Fortify/builder mechanics also touched by [[free-play-planned-enhancements]] (free builders share `builder_tick` but use the 400% overbuild cap, not the EVP per-round mult).
