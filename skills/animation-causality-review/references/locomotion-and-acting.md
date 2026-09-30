# Locomotion and acting

Read when characters move, balance or handle objects. Contact and acting are
separate verdicts; inspect at normal speed and at a readable character scale.

For thought/emotional beats, key poses, timing texture, gaze/face, gesture hierarchy,
moving holds, personality and appeal, also read the shared
[character performance QA](../../character-performance-animation/references/performance-qa.md).
This file concentrates on locomotion, load and bodily/contact evidence; do not let
its physical checks stand in for the separate performance verdict.

For loaded actions or disputed joint use, compare the candidate against the shared
[human-motion contract](../../human-motion-biomechanics/references/motion-language.md),
[joint coordination](../../human-motion-biomechanics/references/joint-rom-and-coordination.md)
and [load/balance](../../human-motion-biomechanics/references/load-balance-and-handling.md).
Those references define the production vocabulary; this file owns review findings.

- Compare actual travel with calibrated forward direction, cadence and stride.
  Preserve intentional sideways/backward steps; stopped workers must not keep
  marching on a free-running clock.
- Inspect the sole, not only the ankle point, against the real support surface.
  Check knee bend and pelvis height against limb proportions and reach.
- Look for preparatory weight transfer, heel-to-toe roll, toe-off, landing,
  acceleration/deceleration, torso/pelvis counter-rotation and recovery.
  Zero foot drift can coexist with a pelvis dragged along like a puppet.
- Turns need pivots/replants instead of planted shoes twisting through the floor.
  Grounded walking needs support outside deliberate flight. Jumps need anticipation,
  takeoff, flight, landing absorption and recovery; grounding must not erase flight.
- Gaze, torso, shoulder and elbow motion should anticipate the task. Hand orientation
  and actual finger closure must establish a grip before load transfer. A wrist at
  the target with an open palm is not a verified grasp.
- Check effort and coordination under load, not only free-walking arm swing. Look
  for threshold catch-up steps, repeated identical swings, abrupt support changes,
  velocity discontinuities and a torso ignoring a tool's weight.
- A clamped IK target or stretched limb is not successful reach. Test independent
  corrective shapes/shared actions in left-only, right-only and combined grip
  states, checking evaluated fingers and the handle rather than just bone targets.
- Balance/centre-of-mass proxies and bounded IK errors do not prove full-body
  dynamics or humanlike performance. Still sheets cannot replace playback.

## Human-motion contract gate

Judge each required claim separately over the full action:

| Claim | Review question | Frequent false green |
|---|---|---|
| Grip before load | Are required contact/opposition/support patches established before the old support releases? | Wrist target reached while fingers remain open |
| Continuous contact | Do the same hand regions remain attached while they own load, including subframes? | Legal endpoints with handle sweep/slide between |
| Plausible ROM/path | Are joint axes calibrated and the whole path within task range or intentionally compensated? | Per-axis maxima pass while wrist/shoulder combination collapses |
| Weight shift | Does preparation precede the load change and match its direction/timing? | Torso reacts only after the prop is airborne |
| Feet/base support | Do support patches, pivots/replants and stance explain the body response? | Root proxy looks centered while soles slide or twist |
| Body reacts to prop | Does load distance/resistance affect trunk, pelvis, shoulders or timing as the story requires? | Heavy prop with free-walk arm/body behavior |
| Prop reacts to body | Does the prop start, tilt, stop and change support only from visible causes? | Prop leads hands, floats or ignores deceleration |
| Follow-through/settle | Do body and prop decelerate, gain new support, release and stabilize? | Smooth spline ends in drift, snap or endless sway |

Use `verified for stated scope`, `failed`, or `unverified` per claim. Do not average
them into a single naturalness score. At miniature delivery scale, confirm that the
enabling grip, support foot and weight change are readable; use close diagnostics
for geometry without substituting them for normal-speed performance.
