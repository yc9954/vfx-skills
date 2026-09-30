# SURA 타락죽 항아리 붓기 — human-motion regression

This is a project regression case, not a universal jug recipe. Reuse the failure
classes and contract structure; replace hand roles, dimensions, timing, character
capacity and camera facts with the current approved scene.

## Provenance and limits

The referenced project conversation reports that hand/handle penetration was reduced
from about **0.61 mm to 0.006 mm** in an earlier Blender pass. Those values are useful
as version-bound project history but were not independently remeasured in this skill
update. They are not a global contact tolerance. At miniature scale, judge error
relative to hand/handle geometry, deformation, sampling and visible contact.

The reusable lesson is narrower: reducing penetration matters, but the motion still
needs correct-facing contact, a secure two-hand load path, plausible joint use, body
weight response and a complete pickup-to-return sequence.

## Scene motion contract

| Field | Tarakjuk regression expectation |
|---|---|
| Task | Maid lifts a ceramic milk jug, tilts it to pour, returns it upright and replaces it |
| Start support | Jug is visibly supported before either hand owns its load; both feet have clear support |
| Grip | Two hands occupy the guide's established regions; one controls handle/rotation and the other supports/stabilizes the vessel according to actual geometry |
| Acquisition | Hands approach open, contact patches align, fingers/thumb establish opposition/support, then load transfers |
| Working range | Wrists remain near neutral under load; forearm, elbow, shoulder girdle and trunk share orientation; no stretched arm or abrupt elbow flip |
| Balance | A small preparatory shift occurs before lift; stance and pelvis/trunk respond as the jug moves away and its moment arm grows |
| Pour | Both contacts remain continuous through lift and tilt; body reacts to the jug and jug motion follows the hands without independent float |
| Upright/return | Controlled deceleration, stream shutoff handled by the food contract, jug returns over its support before fingers release |
| Settle | Hands withdraw after support transfer; shoulders/trunk/feet make a brief motivated recovery and stop |
| Readability | Grip acquisition, maximum tilt and re-support remain legible in the locked projection view; diagnostic close views verify hidden contact |

Do not assume the handle/control hand or support hand from prose alone. Preserve the
actual approved Blender guide and record the roles against its left/right geometry.

## Blender blocking delta

Previous shorthand such as `hands follow jug` is replaced with:

1. Block feet, pelvis/trunk and jug support before solving wrist targets.
2. Give each hand a named contact patch and load/control role.
3. Establish both grips while the jug is still supported.
4. Animate the support transfer; reject any jug motion before acquisition.
5. Lift close to the body, then add counterbalance as the jug moves outward.
6. Tilt through forearm/elbow/shoulder/trunk coordination, preserving wrist margin.
7. Maintain relative contact through tilt/upright; inspect subframes for handle sweep.
8. Re-support the jug, release fingers, withdraw hands and settle.

The prior penetration improvement remains a regression check, but it cannot be the
sole objective. A zero-intersection hand with nails facing the handle still fails.

## Provider-neutral prompt delta

```text
Preserve the Blender guide's exact two-handed grip regions, foot support and jug
geometry. The jug begins fully supported. The maid first settles both hands: thumb
and finger pads oppose the handle while the other hand bears and steadies the vessel.
Only after both contacts are secure does the jug leave its support.

She shifts weight toward the jug before lifting. Her wrists stay near neutral while
forearms, softly flexed elbows, shoulders and torso share the motion. She keeps the
jug close at first, then visibly counterbalances as it moves outward and tilts. Both
hands remain continuously attached; the jug never floats or moves ahead of the body.

After the pour, she rotates the jug upright with controlled deceleration, returns it
over its original support, sets it down before opening the fingers, withdraws both
hands and briefly settles through shoulders, torso and feet.
```

The food/material prompt owns milk onset, stream, impact and shutoff. Camera and
projection invariants remain with `visual-video`; this block adds human action only.

## QA regression gates

- Grip before load: does the jug remain on its original support until both required contacts exist?
- Contact quality: do thumb/finger/support surfaces face the right regions without visible penetration or gap?
- Continuous ownership: do both grips survive lift, tilt and upright without sliding or morphing?
- ROM/path: are wrists, elbows, shoulders and trunk plausible through the path, including subframes?
- Weight shift/support: does preparation precede lift, and do feet/pelvis respond to the changing load distance?
- Reciprocal reaction: does body motion cause jug motion, and does jug load visibly affect the body?
- Return/release: is new support established before fingers open?
- Follow-through: does the chain decelerate and settle rather than snap, float or keep swaying?
- Miniature read: are the enabling contacts and weight change legible at delivery scale, with close diagnostics for approval?

## Negative controls

The regression suite should reject: penetration reduced but contact surfaces wrong;
perfect wrist targets with open fingers; jug moving one frame before grip; both hands
attached while feet/pelvis ignore the outward load; legal endpoint poses with an elbow
flip between; upright jug still floating after release; visually smooth motion with
no re-support or settle.

Generalize these failure classes to trays, lids, baskets and tools. Do not generalize
the jug's exact grip, timing, stance or tolerance to every object-handling scene.
