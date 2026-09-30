---
name: human-motion-biomechanics
description: "Specify shared human-motion biomechanics contracts for animation, blocking and generative-video direction: joint use, load path, balance, grasp, locomotion and readable effort. Use when a human or humanlike character handles weight, reaches, walks, pushes, pulls or uses a tool; this is not medical diagnosis, performer safety advice, rig implementation or final candidate approval."
---

# Human motion biomechanics

Convert an action into a common motion contract that Blender construction,
video prompting and animation review can interpret consistently. Keep the
contract observable and task-specific. Do not prescribe clinical joint limits,
diagnose a performer or claim force/dynamic validation from a plausible pose.

## Responsibility boundary

- Own the shared meaning of joint use, comfortable working range, kinetic chain,
  support, load, balance, grasp and compensatory motion.
- Do not design personality, emotional beats, key poses, gaze, facial acting or
  appeal; `character-performance-animation` owns those choices. Constrain its
  performance contract without erasing the intended thought or rhythm when a
  plausible alternative exists.
- Do not build or repair a rig; `blender-contact-animation` owns implementation.
- Do not choose camera, lens or edit grammar; `visual-video` owns presentation.
- Do not accept a generated clip; `animation-causality-review` owns candidate QA.
- Do not execute or price generation; `blender-seedance-handoff` owns that stage.

## Build one motion contract

Record only what the action needs:

`task | character/body assumptions | prop/load assumption | start support |
grip/contact roles | working joints | kinetic chain | balance/weight transfer |
compensation near limits | action phases | end support | readability | unknowns`

Prefer visible evidence such as “right foot accepts more load before lift” over
abstract commands such as “obey biomechanics.” Treat a load as light, moderate,
heavy-for-this-character or unknown unless production evidence supports more.
When a versioned performance contract exists, cite it and flag any key pose, timing
or exaggeration that must change to preserve support, contact or working range.

## Read only the needed reference

| Need | Reference |
|---|---|
| Joint functions, working range and compensation | [joint-rom-and-coordination.md](references/joint-rom-and-coordination.md) |
| CoM/BoS, moment arm, lifting, carrying, push/pull and locomotion | [load-balance-and-handling.md](references/load-balance-and-handling.md) |
| Grasp taxonomy, thumb/finger opposition, grip security and tools | [grasp-and-tool-use.md](references/grasp-and-tool-use.md) |
| Blender/prompt/review translation and templates | [motion-language.md](references/motion-language.md) |
| Evidence provenance and application limits | [sources-and-limits.md](references/sources-and-limits.md) |
| SURA 타락죽 항아리 회귀 사례 | [tarakjuk-jug-regression.md](references/tarakjuk-jug-regression.md) |

Do not load the project regression for unrelated work. It is one challenge case,
not a universal jug recipe or a tolerance standard.

## Operating rules

- Distinguish anatomical possibility from a comfortable repeated working range.
  Near a distal limit, redistribute the task through grip/prop placement, elbow,
  shoulder girdle, trunk, pelvis and feet rather than silently clamping or stretching.
- Establish contact and grip security before transferring load; establish the new
  support before release. Preserve continuous contact through the supported phase.
- Treat pelvis/root and simple joint-angle checks as proxies. Without a mass model,
  forces, friction and contact solution, keep dynamic and safety claims unverified.
- Preserve character design, disability, assistive supports and stylized intent.
  Human defaults do not override explicit nonhuman anatomy or the user's reference.
- Treat physical plausibility as a floor rather than the whole performance. Allow
  bounded pose/timing exaggeration and design-supported squash/stretch after support,
  load, contact and working-range requirements remain credible.
- At miniature scale, improve readability with clear silhouette, phase separation
  and brief holds; do not fake weight by introducing impossible anatomy or slow motion
  that changes the requested timing.

Return the compact contract plus target-specific notes, not a medical report. When
a produced candidate exists, route the same contract and version to review.
