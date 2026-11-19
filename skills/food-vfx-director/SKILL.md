---
name: food-vfx-director
description: Direct food, liquid and culinary VFX behavior for CG and generative video, including ingredient identity, shellfish anatomy, raw-to-cooked transformations, pours, sauces, porridge, grains, steam, material response, source-sink causality and candidate QA. Use when food behavior or scale materially affects the shot; ordinary cinematography, rigging, generic contact review and rendering belong to their specialists.
---

# Food VFX direction

Make food read as the intended material at the intended scene scale. Convert the
reference and action into observable behavior, a bounded prompt block and tests.
A prompt that names physics is design evidence, not proof of a simulation.

## Responsibility boundary

- Own fluid/food class, relative viscosity, stream breakup, impact response,
  particulate scale, wetness/specular/SSS cues, steam and source-to-sink behavior.
- Do not redesign shot grammar, lens or lighting except to state what must remain
  visible. Use `visual-video` for those choices.
- Do not replace vessel openings, collision geometry, grips or controls. Use
  `blender-contact-animation` for implementation and record the required emitter,
  receiver and contact surfaces for it.
- Review the actual food/effect candidate when one exists. Overall scene approval
  remains with `animation-causality-review`; encoding and delivery remain with
  `film-render-delivery`.

## Build the behavior contract

1. Identify the exact substance, state and reference: water is not milk; milk is
   not cream; a thin sauce is not glaze; rice porridge is not a bowl of oversized grains.
2. Establish scale anchors visible in the shot: vessel mouth, bowl diameter,
   utensil, hand and known ingredient size. Prefer ratios to invented millimetres.
3. Write the event chain: source and trigger -> emergence -> travel/breakup ->
   impact/occlusion -> spreading or retention -> residual drops/vapor -> final sink.
4. Separate motion from appearance. A correct white color does not prove milk;
   a plausible stream does not prove the grains, wetness or steam are in scale.
5. State fixed geometry/camera and the few properties open to generation. Keep
   provider parameters outside the prose until the current tool/schema confirms them.
6. If a candidate exists, inspect it at normal speed and around onset, impact and
   shutoff. Report `verified for stated scope`, `failed`, or `unverified` with evidence.

## Read only the needed detail

| Need | Reference |
|---|---|
| Material class, scale, optics and motion cues | [material-behavior.md](references/material-behavior.md) |
| Shellfish anatomy, edible parts, episodic entrances or raw-to-cooked transformations | [ingredient-identity-and-transformations.md](references/ingredient-identity-and-transformations.md) |
| Generative prompt block and targeted negatives | [prompting-and-negatives.md](references/prompting-and-negatives.md) |
| Candidate inspection and verdict gates | [qa-checklist.md](references/qa-checklist.md) |
| SURA 타락죽 milk-pour example | [tarakjuk-example.md](references/tarakjuk-example.md) |
| Research provenance and current-tool caveats | [sources.md](references/sources.md) |

Use the smallest useful output: a material contract, one prompt block, or scoped
findings. Do not load the project example for unrelated food. Do not turn one failed
clip into a universal ban: generalize only the observable failure class, and keep
the correction conditional on the requested material.

## Handoff

Pass `substance/state | scale anchors | source/trigger | receiver | motion phases |
surface response | fixed geometry/camera | targeted rejects | candidate/version |
QA verdict/open issue`. Preserve the user's story and chosen production path.
