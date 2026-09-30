---
name: character-performance-animation
description: "Design character acting for animation: intention, emotional beats, key poses, timing, gaze, facial transitions and layered secondary motion. Use when motion is mechanically correct but feels segmented, generic or emotionally unreadable; biomechanics, rig implementation, camera direction and final candidate approval remain separate responsibilities."
---

# Character Performance Animation

Turn a scene objective into an observable acting contract that another stage can
constrain, implement, prompt and review. Aim for clear thought and personality,
not imitation of a named studio, film, character or proprietary style.

## Responsibility boundary

- Own **why and how the character performs**: thought beats, emotional changes,
  key poses, line of action, timing texture, gaze, facial transitions, gesture
  hierarchy, moving holds, overlap and performance readability.
- `human-motion-biomechanics` owns whether the action is plausible: working range,
  load path, balance, base of support, grip and contact. Treat that contract as a
  floor, then stylize above it without breaking its required support or phase order.
- `blender-contact-animation` owns rig, keyframe, constraint and contact implementation.
- `visual-video` owns camera/edit/lighting language and converts the acting contract
  into provider-appropriate observable prose.
- `blender-seedance-handoff` owns actual guide/reference binding and generation.
- `animation-causality-review` owns verdicts on an existing candidate. It must score
  physical and performance quality separately.

## Build one performance contract

Start from `scene objective | character want | obstacle/attention target | personality
and current emotion | relationship/partner | start and end states | camera/readability`.
Then design:

1. A short sequence of thought/emotional beats. The character notices, decides,
   anticipates, acts, registers the result and recovers; omit beats the scene does
   not need.
2. Storytelling key poses with readable silhouette, line of action, asymmetry and
   prop relationship. Each pose must answer what changed in thought or action.
3. Timing phrases and accents: holds, moving holds, contrast, acceleration,
   deceleration, overshoot and settle. Avoid uniform easing and equal beat lengths.
4. Attention and face: gaze target, eye/head lead, blink purpose, brows/lids/cheeks/
   mouth/jaw transition and the smallest readable micro-reaction.
5. Layered motion: primary action, supporting gesture and tertiary cloth/finger/
   breath detail. Secondary motion may enrich the action but must not compete with it.
6. A handoff using [performance-beat-packet.md](assets/performance-beat-packet.md).
   Keep unknown rig abilities and hidden facial detail explicitly unverified.

Choose pose-to-pose for planned acting and contact landmarks; use straight-ahead
exploration for loose arcs, cloth, tails or spontaneous connective motion when it
will not drift the required state. Refine splines only after stepped/blocking poses
read. Smooth curves are not a substitute for decisions.

## Read only what the task needs

| Need | Reference |
|---|---|
| Core acting workflow, animation principles and stylization floor | [performance-principles.md](references/performance-principles.md) |
| Spacing, easing, holds, rhythm, phrasing and comedic timing | [timing-spacing-rhythm.md](references/timing-spacing-rhythm.md) |
| Key poses, silhouette, line of action, asymmetry and staging | [pose-silhouette-line-of-action.md](references/pose-silhouette-line-of-action.md) |
| Follow-through, drag, successive joints and gesture hierarchy | [overlap-secondary-action.md](references/overlap-secondary-action.md) |
| Gaze, blinks, head-eye coordination and facial transitions | [facial-acting-and-gaze.md](references/facial-acting-and-gaze.md) |
| Personality, thought beats, emotional mapping and ensemble reactions | [personality-emotional-beats.md](references/personality-emotional-beats.md) |
| Miniature readability, restrained cuteness, projection master and Tarakjuk regression | [cute-miniature-performance.md](references/cute-miniature-performance.md) |
| Design review or candidate performance QA | [performance-qa.md](references/performance-qa.md) |
| Evidence, source limits and provenance | [research-sources.md](references/research-sources.md) |

Do not load the Tarakjuk example for unrelated work. When the request is only a
physical feasibility check, use biomechanics directly. When an actual candidate
exists, pass the contract and candidate version to review rather than declaring
the designed performance successful.

## Observable handoff language

Translate craft terms into body parts, order and visible change. Write “the eyes
find the bowl, the head follows a fraction later, then the torso turns” rather than
“good eye lead.” Write “the forearm stops, fingers and sleeve continue briefly,
then settle on different beats” rather than “add overlap.” A moving hold names what
stays fixed and what remains alive: breath, eyes, fingers, cloth or weight.

Return the smallest useful artifact: a performance contract, timed beat sheet,
key-pose list, observable generation block or scoped QA rubric. Preserve the user’s
duration, character design, culture, medium and current tool constraints.
