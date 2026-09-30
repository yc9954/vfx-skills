# Tools, containers, rigging and effects

Read for object handling or contact effects. Review the whole interaction from
a demonstrably separated state through approach, contact, transport, release,
settling and withdrawal. Each phase needs its own evidence.

## Persistent support

- Where was the prop before pickup? What supports it? Establish grip before it
  leaves its support, and new support before the hand releases it.
- Trace visibility, parenting, constraints and dynamic/kinematic states. Bodies
  animated through each other do not become valid because dynamics starts later.
  Hidden initialization needs a justified precondition, not a teleportation excuse.
- Compare collision proxies with actual object extent and openings. A root point
  clearing a rim does not mean the carried item fits through it.

## Capture, retention and release

- For a net/scoop, the catch must pass through the open mouth in the right direction
  with room for its size. Lowering a closed underside through food or attaching
  food at a scheduled time is not capture. Check relative swept bag/rim/food geometry.
- Start before the first possible touch: include underside, sides, rim and handle
  during approach and immersion. A later legal mouth crossing does not cancel an
  earlier wall crossing. “No capture” does not mean “no collision”.
- Include container depth, gravity, tilt and item size in retention. Parenting alone
  must not keep food stuck to a nearly inverted basket.
- Pouring requires a receiver under the exit, motion to the downhill lip, clearance,
  plausible release position/velocity, falling and settling. Lowering the carrier
  alone does not transfer contents. A good landing does not prove a good pickup.

## Load paths and materials

- Trace what pulls, supports, pivots, tips and stops a hoist: attachment, rope payout,
  pulley ratio, tension/slack and tip actuation. A decorative rope redrawn along a
  keyframed basket is not a demonstrated mechanism. Test controller inputs against
  motion; do not invent an unseen motor solely to justify the result.
- Water displacement, drainage, splashes and wakes should follow actual crossings.
  Foam, bubbles, steam and sound need event locations/timing, not unrelated clocks.
  State which effects approximate rather than simulate fluid/body dynamics.
- Judge material and scale perception, contact shadows and occlusion. Does water
  read as liquid and does the miniature's weight match its timing? Keep this visual
  verdict separate from collision measurements.
- When food/fluid class, rheology, grain scale, wetness or steam is material to the
  decision, apply the installed `food-vfx-director` checklist and import its scoped
  findings. Keep this file responsible for the whole interaction and release verdict,
  not a competing culinary material rulebook.
- Audition noise, clipping, sync and contact sounds when tools allow it. Audio-track
  presence or duration does not establish sound quality. Keep unavailable audition
  unverified, including when silent output is a known technical property.
