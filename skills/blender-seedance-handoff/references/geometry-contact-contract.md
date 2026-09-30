# Blender geometry/contact preservation contract

Generation receives a bounded reference contract, not permission to reinterpret
all Blender decisions. Record immutable inputs by version/hash and name what remains creative.

## Freeze before handoff

| Class | Freeze and record | Evidence / candidate test |
|---|---|---|
| Camera/projection | Camera transform, aspect/crop, plate/registration anchors, approved mapping, focus state | Overlay first/middle/last candidate frames on anchors; reject drift, reframe, zoom, breathing or cut |
| Geometry | Actor/prop IDs, scale, silhouettes, vessel openings, handle/contact regions, receiver boundaries | Compare landmarks and openings; reject topology morphs, sealed mouths, duplicate/missing props |
| Contact/support | Hand/finger regions, support owner, foot contacts, pickup/release events, collision-critical intervals | Inspect before contact through release; reject early motion, sliding grip, penetration or floating |
| Human motion/load | Motion-contract version, load assumption, left/right grip roles, calibrated working-range status, support feet/patches, preparatory weight shift, kinetic-chain poses, end support/velocity | Compare guide phases and pose landmarks; reject grip redesign, distal-limit rescue, frozen body under load, support-foot drift or missing settle |
| Character performance | Performance-contract version, thought/emotional beats, key poses, gaze/face targets, moving hold, partner reaction and lead/follow/settle order | Compare delivery-scale read and timed landmarks; reject generic re-acting, simultaneous body-part starts/stops, lost eye lead, frozen/noisy hold or erased personality |
| Timing/continuity | FPS/timebase, action phases, screen direction, start/end pose and velocity | Compare guide phase order and clip boundary; reject repeated/skipped actions or direction reversal |
| Food/effect interface | Emitter opening, trigger, receiver, occluders, intended final sink | Use `food-vfx-director` for behavior; reject a stream/effect that bypasses these interfaces |

Do not rely on filenames alone. Preserve the source scene/camera/guide version and
the exact exported media used by the job. A diagnostic oblique camera or gray material
does not become final truth unless its role says so.

## Allocate freedom

State each property as `fixed`, `bounded`, or `free`:

- Fixed examples: plate anchors, camera, jug mouth/handle, grip regions, actor IDs,
  prop count, action order, source and receiver. For an approved loaded-human guide,
  also fix grip roles, support ownership/feet, load-transfer event and required phase order.
- Bounded examples: facial microacting, cloth follow-through, small local steam,
  food surface breakup within the material contract. Small torso/shoulder recovery may
  be bounded only when it preserves the approved contact, working range and end support.
- A versioned performance contract can make selected facial transitions, gaze targets,
  partner offsets, key silhouettes or settle order fixed rather than generically free.
  State which performance details are exact landmarks and which may vary in amplitude.
- Free examples: only properties the user/brief genuinely leaves open. Do not call
  a critical material, identity or contact detail “creative freedom” to avoid failure.

## Reference binding

For every supported input record:

`artifact/version | provider field/label | controls | interval | inherit | exclude`

For a human-motion guide also bind:

`motion-contract/version | prop/load assumption | grip roles/contact patches |
support feet/patches | key pose/phase intervals | working-range/compensation facts |
fixed versus bounded body motion | end support/velocity`

For character acting also bind:

`performance-contract/version | thought/emotional beats | key-pose/hold intervals |
gaze/face/partner cues | primary-secondary-tertiary hierarchy | fixed versus bounded
microacting | lead/follow/settle order | end attention/emotional residue`

Use the current schema's actual role/label. If the mode cannot carry the required
guide, do not pretend prose provides the same strength; keep the result a pilot or
choose an authorized deterministic path. Start/end images lock frames, not hidden
velocity or 3D geometry.

## Acceptance

1. Confirm the submitted input versions and returned candidate/job identity.
2. Compare anchors and silhouettes before judging polish.
3. Inspect each critical contact from separated state through settle.
4. Compare grip-before-load, continuous contact, weight shift, support feet, body/prop
   reciprocal response, joint path and re-support/release against the motion contract.
5. Inspect source/receiver openings and food/effect interfaces.
6. Check normal-speed acting and boundary continuity separately.
7. Compare thought/action read, key poses, gaze/face, partner timing, moving hold and
   staggered settle against the performance contract; do not infer them from contact.
8. Record fixed-property survival, bounded variation and unverified hidden areas.

Prompt compliance is not acceptance. A candidate that looks attractive but changes
the camera, seals the jug, moves a grip, resizes rice or redirects the receiver fails
the relevant contract and must not be promoted as a projection master.
