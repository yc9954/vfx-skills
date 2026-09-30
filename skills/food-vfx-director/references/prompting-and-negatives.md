# Generative food-VFX prompting

Write an observable contract, not a menu of physics terms. The current provider,
model, attachment roles and parameters must be confirmed by the execution workflow.

## Prompt block

Use only applicable lines:

```text
SUBSTANCE / STATE: [exact material and comparison; temperature/process if visible]
SCALE: [anchors and relative ingredient/effect size]
SOURCE / TRIGGER: [container opening and event that starts flow or vapor]
MOTION: [onset, established flow, breakup, impact, response, shutoff]
SINK / END STATE: [where the material finishes and what residue remains]
SURFACE RESPONSE: [opacity/transmission, wetness, highlight, scattering]
FIXED: [camera, vessel geometry, actor/prop identity, registration, timing]
AVOID: [short targeted failure classes]
```

Put the desired behavior before the negative list. Negative constraints are a
backstop, not a replacement for source, motion and end-state instructions.

## Failure-class corrections

### Milk reads as cream

Use a relative material statement and visible consequences:

```text
Fresh milk, clearly freer-flowing than cream: a narrow gravity-driven stream leaves
the jug lip only after tilt, tapers slightly during the fall, makes small local
ripples on impact, levels promptly, then thins to a few residual drops as the jug
returns upright.
```

Targeted rejects: no cream/yogurt/icing consistency; no rope-like ribbon; no mound
that holds its shape; no stream continuing after the jug is upright. Do not ban
thickness globally when the requested substance is actually a glaze or cream.

### Rice grains read too large

```text
Fine cooked rice grains remain small relative to the spoon and bowl, partially
embedded in the porridge and visible as subtle texture rather than dominant pellets.
Their identity and size remain constant through the shot.
```

Targeted rejects: no boba-sized beads, beans, pebbles, dumplings, swelling grains,
uniform cloned pellets or free-floating particles moving independently of the food.

### Detached or causally impossible effects

Pair the correction with the actual event:

- no pre-tilt leak or stream from the vessel wall;
- no receiver response before impact;
- no splash, foam or ripple away from the contact point;
- no steam before a credible hot source is revealed;
- no unexplained volume gain/loss, teleporting residue or particles crossing walls;
- no generic looping effect after the causing action has settled.

## AI-video constraints

- Bind every reference to one role and exclusions. A Blender guide can own camera,
  layout and timing without making its gray material the final look.
- Preserve fixed geometry with explicit anchors and an actual supported reference
  path. Text such as “exactly preserve” is not a guarantee; review the output.
- For a projection master, repeat only the critical lock: no camera travel, rotation,
  zoom, crop/reframe, focus breathing or cut; preserve plate and vessel anchors.
- Separate prompt prose from real mode/duration/resolution/reference/audio settings.
  Recheck current schema; provider examples are not interchangeable API syntax.
- Keep one material hypothesis per A/B test. With input, action and camera fixed,
  change only the food-behavior block and compare the same temporal phases.
- Do not claim PBR, FLIP, Mantaflow, ray tracing, SSS or a render pass was used
  merely because the prompt contains the term. Describe the visible target instead.
