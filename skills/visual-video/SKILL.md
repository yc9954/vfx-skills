---
name: visual-video
description: Design or improve video treatments, storyboards and generation prompts using precise cinematography, editing, lighting and CG/VFX language, including Higgsfield/Seedance and tabletop projection. Use for shot, effect or prompt direction; does not replace Blender implementation, paid generation, candidate review or render-status checks.
license: CC-BY-4.0 (adapted from Serge Shima, github.com/smixs/visual-skills; see SOURCE.md)
---

# Visual video direction

Turn a story into readable action, staging, rhythm and a usable generation brief.
Preserve the user's chosen medium, camera and deliverable. A finished prompt is
not a finished video. For production requests, pass the brief to the available
production workflow and continue within authorization; do not stop at prose.

## Local contract — read first

Read [production-adapter.md](references/production-adapter.md) before upstream
references. It governs how their craft guidance is applied here: project-specific
choices override examples, and model documentation is a pinned, unverified
snapshot, not a live API or a guarantee of physics.

For new direction read [dramaturgy.md](references/dramaturgy.md) and
[universal-rules.md](references/universal-rules.md). For a small prompt repair,
reuse the existing creative brief and read the relevant specialist below.
Use intention → playable action → visible consequence, not adjective stacking.
Do not invent conflict, forced details, cuts or fixed numbers of anchors merely
to fill a template. Beat timing is not necessarily a camera cut.

## Read only what changes this task

| Need | Reference |
|---|---|
| Story shape, including quiet discoveries and causal journeys | [patterns-and-genres.md](references/patterns-and-genres.md) |
| Treatment, beat sheet, or editing rhythm | [role-modes.md](references/role-modes.md) |
| Precise framing, light, sound and spatial vocabulary | [camera-lighting-vocabulary.md](references/camera-lighting-vocabulary.md) |
| Professional shot/cut/CG prompting, including Higgsfield prompt research | [cinematic-cg-prompting.md](references/cinematic-cg-prompting.md) |
| Character thought, emotional beats, key poses, gaze/face, timing texture or layered acting | Read the relevant [character-performance-animation](../character-performance-animation/SKILL.md) reference and preserve its performance contract/version |
| Human reach, lifting, carrying, pouring, push/pull or tool-use prompting | Read the shared [human-motion prompt language](../human-motion-biomechanics/references/motion-language.md); use only the action's needed joint/load cues |
| Food/fluid behavior, particulate scale or culinary-effect QA | Use installed `food-vfx-director`; keep only shot, visibility and lighting intent here |
| Prompt continuity or failure repair | [fixes-and-skeletons.md](references/fixes-and-skeletons.md) |
| Unmotivated appearances, arbitrary effects, or unclear scene transitions | [animation-causal-staging](../animation-causal-staging/SKILL.md) for entity sources, triggers, visible consequences and before/coverage/reveal/result boards |
| Choreography, dance, musical rhythm or varied character performance | [choreography-brief.md](references/choreography-brief.md) |
| Still keyframes for an animatic | [animatic-keyframes.md](references/animatic-keyframes.md); its faceless/cold racing examples are not universal rules |
| A requested race/speed spot | [race-and-speed.md](references/race-and-speed.md), after animatic-keyframes |
| Higgsfield/Seedance capability claims or prompt construction | [higgsfield-prompting-evidence.md](references/higgsfield-prompting-evidence.md) and [cinematic-cg-prompting.md](references/cinematic-cg-prompting.md). Archived [seedance.md](references/seedance.md) and [seedance-25.md](references/seedance-25.md) are optional craft examples, not current schemas or mandatory recipes. |
| Kling or Veo prompt syntax | [kling.md](references/kling.md) or [veo.md](references/veo.md), only the selected provider |

For model-specific output, verify the actual provider/version/mode first. If
unavailable, give a provider-neutral brief with capability questions marked
unverified; do not invent executable flags. No provider lookup is needed for a
Blender-only beat sheet. Read the complete selected reference, not just its header.

## A compact production handoff

First classify the deliverable: `projection_master`, `cinematic_footage`, or
`look_motion_pilot`. Do not silently move between them. Build a prompt packet
with [this template](assets/director-prompt-packet.md) when the task needs more
than a short prompt. Separate the director's prose, actual provider settings and
deterministic Blender/compositing work. For every specialist term specify the
subject, visible change, timing and what stays fixed. Choose useful terms, not
as many terms as possible. Treat better results as a hypothesis until compared
on actual outputs; terminology alone is not a quality guarantee.

For **PROJECTION MASTER**, preserve the registered camera transform, crop, anchors,
focus behavior and plate geometry: no travel, rotation, zoom, reframing, lens
breathing, stabilization drift or unrequested cuts. Move attention with blocking,
timed action and local light/material contrast. For **CINEMATIC/PROMO**, motivated
coverage, camera movement, lens/focus changes and edits are available; specify their
start, end, pace and visible purpose. Never use promo freedom in a projection master.

A fixed projection camera does not forbid an explicitly requested scene cut.
For a full-screen fan wipe, cover the entire raster, including corners, before
the hidden edit; do not reinterpret it as plate-local effects. Draw the coverage
and reveal states when the user requests images, and inspect those actual images.
Follow the user's selected preparation method and
[production loop](../miniature-film-director/references/collaborative-production-loop.md).
The current tabletop path uses Nano Banana plate/character images and Kling action
direction, then per-plate background removal/review before four-seat foreground placement
and selected-background composition. Do not add a full-duration Blender previs or its
approval as a prerequisite.
For explicitly selected mesh previs work, use the
[previs handoff](../animation-causal-staging/references/storyboard-previs.md).

Use the smallest useful artifact: one prompt, a timed beat sheet, or a treatment.
For contact stories retain actor/prop IDs, start/end support states, the event
that permits each transfer, viewer attention, and constraints that must survive.
Bind each supplied asset to its role and exclusions. Preserve camera/layout and
critical contact constraints before decorative detail when compressing prompts.
For handling beats, specify the intended support/grip (for example palm-supported tray versus
wrapped pole), what the thumb/finger pads do, and when weight transfers. Avoid a generic
"natural hands" instruction as the whole contract. A beautiful AI reference with twisted
digits is not approved motion; actual hand quality belongs to candidate review.
For loaded human action, translate the shared motion contract into visible order:
`grip/contact → anticipatory weight shift → load transfer → kinetic-chain response →
primary action → deceleration/new support → release → settle`. Do not paste anatomy
jargon or a universal angle table into the prompt. Describe only cues that will read
in this framing, especially support foot, hand roles and body response at miniature scale.
For character acting, translate the performance contract in the same observable way:
name the trigger and gaze target, which body part leads, which follows, the readable
pose/hold, facial change, partner reaction and staggered settle. Never submit a list
such as “overlap, moving hold, appeal, Pixar-like.” For overlap say what stops first,
what continues and what contact/camera fact remains fixed; for a moving hold say which
pose stays stable and how breath, eyes, fingers or sleeves remain alive.

If available, `visual-image` handles still look development; `miniature-film-director`
coordinates a requested full film; `blender-seedance-handoff` executes an authorized
image-based or hybrid job; `animation-causality-review` inspects the resulting candidate. Load
companions only at their actual stage. Do not install missing companions silently.

Answer in the user's language. Choose prompt language for the current tool and
user preference; do not assert universal English superiority. Mark inferred
creative choices and verified versus unknown generation parameters. Keep the
explanation brief unless the user asks for the reasoning.

Original craft library: Serge Shima, [smixs/visual-skills](https://github.com/smixs/visual-skills),
CC BY 4.0. Local changes and pinned revision: [SOURCE.md](SOURCE.md).
