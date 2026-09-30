# SURA 타락죽 — milk pour example

This is a project example, not a universal recipe. Replace actor names, anchors,
duration and provider settings with the current approved scene data.

## Responsibility flow

1. `visual-video` declares **PROJECTION MASTER** and locks shot/camera/focus/light intent.
2. `character-performance-animation` supplies the scene-specific intent, attention,
   phrase timing and overlap contract. Match the real actor count; partner exchange,
   recoil and facial controls are conditional, not ingredients of every pour.
3. `human-motion-biomechanics` supplies the shared grip/load/kinetic-chain/weight-shift
   contract; see the [jug regression](../../human-motion-biomechanics/references/tarakjuk-jug-regression.md).
4. `blender-contact-animation` supplies the jug opening, two-hand grip, tilt path,
   bowl receiver, support transfer and timing.
5. `food-vfx-director` supplies milk/porridge/rice behavior and specialized QA.
6. `blender-seedance-handoff` binds exact guide/look roles and freezes geometry/contact.
7. `animation-causality-review` judges the whole generated action and release state.
8. `film-render-delivery` verifies the approved file and technical output.

## Behavior contract

| Field | 타락죽 scene |
|---|---|
| Substance | Fresh milk, opaque and freer-flowing than cream |
| Source/trigger | Milk reaches the real jug lip only after the maid establishes grip and tilts |
| Travel | Narrow continuous gravity-driven stream; slight taper; small breakup only near shutoff |
| Receiver | Inside the porridge bowl, at the visible impact point |
| Response | Small local concentric ripples and a brief pale mixing trace; surface levels promptly |
| Porridge/rice | Soft porridge body; fine cooked grains subordinate to spoon/bowl scale and partially embedded |
| Shutoff | Jug rotates upright; stream thins; a few residual drops; no continued flow |
| Fixed | Plate centre/diameter, bowl and jug geometry, character scale, grip regions, camera and crop |

## Provider-neutral generation prompt

```text
PROJECTION MASTER — one continuous locked-off medium-wide view. Preserve the exact
plate centre and circular geometry, bowl and jug positions, character scale, camera
transform, crop, exposure and established two-handed grip from the Blender guide.
No cuts, camera travel, rotation, zoom, reframing, focus breathing or stabilization drift.

The maid first settles both hands on the established jug contact regions, shifts
her body weight toward the vessel, and only then transfers the jug's load into her
grip. She tilts the jug gradually with both contacts continuous. Fresh milk reaches the real mouth and begins
only after the tilt: a narrow gravity-driven stream, clearly freer-flowing than cream,
tapering slightly during the fall. It lands inside the porridge bowl at one visible
impact point, producing small local ripples and a brief pale mixing trace that levels
promptly. Fine cooked rice grains stay small relative to the spoon and bowl, partially
embedded as subtle texture; their size and identity remain constant.

She rotates the jug upright. The stream thins naturally into a few residual drops,
then stops. She returns the jug to its established support and settles.
Preserve vessel openings, hand placement, prop ownership and all fixed geometry.

Avoid cream, yogurt, icing or rope-like milk; no mound that holds shape; no oversized
boba/bean/pebble grains; no pre-tilt leak; no stream from the jug wall; no splash away
from impact; no continuing flow after upright; no teleporting residue or new props.
```

The prompt does not choose executable model settings. `blender-seedance-handoff`
must translate the actual guide/look inputs into the selected provider's current
attachment roles and preserve the authorized cost boundary.

## Review flow

1. Compare first frame/anchors to the approved projection guide.
2. Inspect grip and jug support before any liquid appears.
3. Step through pre-tilt -> onset at lip -> connected fall -> impact -> ripples.
4. At normal speed, ask whether the liquid reads as milk rather than cream.
5. Compare grain size against spoon/bowl in several frames; reject species/size drift.
6. Inspect upright/shutoff and final residue; reject a looping or detached stream.
7. Record food-material, causal-contact and projection verdicts separately, then
   pass the same candidate ID to whole-scene review and technical delivery.
