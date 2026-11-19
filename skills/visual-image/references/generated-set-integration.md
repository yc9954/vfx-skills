# Integrate generated sets with the action

Use for image-based backgrounds, image-to-3D assets and a scene whose objects look
like separate layers. This is a production diagnostic, not a promise that an image
or a provider creates watertight geometry, matched parts or physical water.

## Keep the current view and physical layout

- Recover the active project's camera, frame dimensions, crop and plate/actor
  anchors before editing. Define elevation above the floor separately from tilt
  away from vertical. A 60° elevation in one film and 75° in a later series are
  different contracts; do not apply either to unrelated projects by default.
- Bind the plate, characters, props and environment to the same view. Repairing a
  camera mismatch by rotating every prop 60° creates a different spatial problem.
  Inspect top/side silhouettes and contact in the actual output.
- For a physical projection brief, distinguish screen millimetres from world
  dimensions and pixels. Map anchors through the registered camera/canvas; a
  210 mm projected plate is not established by setting an oblique mesh to 210 mm.
  Specify whether a bottom margin is measured to the plate rim or its centre and
  whether minimum actor height is a projected silhouette or model dimension.
- Preserve calibrated sizes over time. Do not shrink the plate to fit food, add
  thickness to hide the water boundary or stretch a background nonuniformly to
  fill a new aspect ratio. Use the requested crop with extension outside it.

## Separate source beauty from 3D evidence

Record `source image/version | generation method/job | actual inputs | downloaded
asset/hash | textures | dimensions | repairs`. A turntable of one generated mesh
is not evidence that multi-view references were supplied. Label single-image
generation accurately; inspect front, side, underside and silhouette for flattened
relief, missing volume, fused water, floating decorations and distorted borders.

Split by how the scene must move: a removable roof/lid, opening shell, held tool or
edible interior needs independent useful geometry. Generating a hull and roof
separately does not make their rims fit. Establish one shared mating profile in
the DCC, adjust both parts to it, and test closed contact plus the full opening path.
Inspect existing duplicated appendages and remove only confirmed unwanted geometry;
do not keep extra bow oars merely because they are baked into an asset.

When the user selects a flat background and crop, keep that method. Match extra
rocks/flowers to its light, scale, texture frequency and perspective; fill outside
the action area without covering grips or inventing obstructing 3D terrain.
Do not replace this choice with another paid set generation by default.

## Diagnose the layer boundary

| Symptom | Inspect before adding detail |
|---|---|
| Objects sit above water like stickers | Actual water elevation/intersection, depth ordering, refraction/absorption, shadow and wet contact band |
| Rocks/coral look plastic or flat | Geometry relief and silhouette, texture scale/UV, roughness variation, depth attenuation; not only a higher-resolution color map |
| Plate looks thick or disconnected | Rim/profile/underside, immersion and waterline, true scale, contact shadow; avoid adding a solid slab underneath |
| Everything is equally shiny | Material-specific highlights, roughness, scattering/transmission distances in scene units |
| Water is dark, static or syrupy | Reference palette/exposure, visible bottom/depth, ripple wavelength/speed, moving reflections and local disturbance |
| Fire is only a bright spot | Visible source-connected flame body, silhouette/variation/occlusion; emitted light illuminates nearby forms but cannot replace the flame |

For water, align submerged/above-water parts with the actual surface and intended
depth. Use depth-dependent color/visibility rather than tinting the whole object
blue. Foam, wake and ripples start where contact/displacement occurs and persist
plausibly after it; white dots scattered uniformly do not establish immersion.
Do not claim buoyancy or fluid simulation from a water shader alone.

## Compare the real candidate

Lock exposure/color management for comparisons. Preserve a bright reference's
highlight detail, warm wood and water/flower color separation without clipping
the whites or assigning the same orange/teal grade to all materials. Confirm image
textures are actually connected and mapped; test roughness/normal separately.

Inspect at delivery scale and through motion: waterline, shadows, reflection,
geometry and effect timing must agree. A beauty still supports look only. Hand
ingredient identity/transformations to `food-vfx-director`, contact to
`blender-contact-animation`, and actual candidate verdicts to the review skill.
