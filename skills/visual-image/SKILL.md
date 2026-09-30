---
name: visual-image
description: Develop reference-grounded visual direction, style comparisons, character sheets, storyboard keyframes and image prompts. Supports image generation with concrete materials and preservation rules; does not substitute a prompt for a requested image or claim an image is a rigged 3D asset.
license: CC-BY-4.0 (adapted from Serge Shima, github.com/smixs/visual-skills; see SOURCE.md)
---

# Visual image direction

Build the smallest clear art brief that preserves the user's target. Read
[style-contract.md](references/style-contract.md) first. A request for an actual
image goes through the available image-generation skill/tool, using this brief;
do not deliver only a prompt. A prompt-only or analysis-only request stops there.
Do not let planning become an unnecessary approval round before generation.

## Select the relevant guidance

Read [golden-rules.md](references/golden-rules.md) for prompt composition, subject
roles and iterative preservation. Treat its model limits as unverified snapshot
claims. Current tool schemas and official provider documentation govern execution.
Keep explicit user exclusions even when rephrasing positively.

| Need | Read |
|---|---|
| Match a supplied style/reference | [vision-decomposer.md](references/vision-decomposer.md); separate observation from inference, not mandatory keyword-only output |
| Lighting, palette and material vocabulary | [creative-direction.md](references/creative-direction.md) |
| Cinematic miniature look without changing projection geometry | [projection-look-gate.md](references/projection-look-gate.md) |
| Complex prompt organization | [prompt-framework.md](references/prompt-framework.md) |
| Character identity / turnarounds / expressions | [characters.md](references/characters.md) and, when needed, [character-design.md](references/patterns/character-design.md) |
| Story sequence / keyframes | [storyboards.md](references/storyboards.md) |
| A multi-panel sheet in one image | [multi-panel.md](references/multi-panel.md); count panels for actual changes, not mandatory cuts |
| Existing-image edit | [editing.md](references/editing.md) |
| Layout/sketch control or a dimensional visualization | [structural.md](references/structural.md) or [dimensional.md](references/dimensional.md) |
| Text, diagram, or raster slide art | [text-rendering.md](references/text-rendering.md) or [slides.md](references/slides.md); editable documents require their own tools |
| A photograph specifically, with unwanted beautification | [de-slop.md](references/de-slop.md); not the cure for stylized CG |
| Domain-specific stills | The matching [food](references/patterns/food-beverage.md), [product](references/patterns/ecommerce.md), [fashion](references/patterns/fashion-editorial.md), [portrait](references/patterns/portrait-cinema.md), [poster](references/patterns/poster-illustration.md), or [UI/social](references/patterns/ui-social.md) library |

The upstream [model comparison](references/models.md), [GPT Image notes](references/gpt-image.md)
and [Nano Banana notes](references/nano-banana.md) are historical prompt references,
not a supported-model registry. Read only when relevant to the verified selected
tool. Do not pass their model IDs, quality tiers, reference limits, prices or JSON
fields to a different tool. The built-in image tool has its own schema and rules.

## Deliver the requested thing

For a prompt: state its purpose, reference roles, change/preserve/constraints and
only verified generation settings; requested-but-unverified specs stay labelled.
For style analysis: cite the viewed frame/image and describe visible differences.
For generation: call the actual tool and return its result, then assess the image
against the style contract. A still cannot establish motion/contact correctness.
For characters intended for articulated handling, inspect separate digits, thumb placement,
palm/nail orientation and plausible joint silhouettes at useful resolution. Keep props separate
when the intended rig needs pickup/release. A neutral pose or five visible fingers is only a
design input, not proof of usable topology, skinning or a physically plausible grasp. Reject
twisted hands in style images instead of passing them downstream as anatomical truth.
For video planning, hand keyframes to the installed `visual-video` or film workflow.
For a food still, this skill owns composition and look-reference quality. It may show
ingredient scale and surface cues, but a still cannot verify viscosity, stream breakup,
source-sink causality or settling; route those video requirements to the installed
`food-vfx-director` when available.

Original craft library: Serge Shima, [smixs/visual-skills](https://github.com/smixs/visual-skills),
CC BY 4.0. Local changes and pinned revision: [SOURCE.md](SOURCE.md).
