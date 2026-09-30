# Choreography and performance brief

Use when designing dance, rhythmic action, an ensemble or varied character
performance. This is direction, not a claim that a model can execute a precise
beat, hand grip or full-body pose. Preserve the production adapter's scope.

- Define what the actor is doing and why, then the movement quality. Prefer an
  observable phrase to “natural, varied, realistic dancing.” Let action settle;
  constant motion is not required to keep a character alive.
- Separate movement reference, character/look reference and music/tempo source.
  Use the actual music segment and offset if supplied. If none exists, label a
  proposed meter/BPM as a design assumption, not something extracted from audio.
- Choose motif, variation, contrast and resolution as useful; do not impose an
  eight-count, conflict or fixed number of moves on every style. For court dance,
  distinguish reference-based reconstruction from an original court-inspired dance.
- Brief each meaningful phrase with:
  `time/beat interval | actor/purpose | action/energy | support and path |
  prop/grip | accent/pause | ending state and next transition`.
  Phrase boundaries are not necessarily camera cuts or separate generation calls.
- Make rhythmic intent specific: an accent can be a landing, torso hit, gaze,
  turn completion or prop opening. Not every beat needs an accent. Free-rhythm,
  swing, syncopation and local musical traditions need their own timing map.
- Specify variation with purpose: restrained vs expansive, preparation length,
  gaze lead, amplitude, facing, phrase order and tempo feel. Do not request
  independent random motion of all joints or break planned group unison.
- For ensembles specify who leads, who responds, shared accents, lanes and any
  hand-off event. Prop carriers, guards, dancers and musicians need different
  action responsibilities, not one dance loop with different costumes.
- Preserve intended side/back steps, pivots and slides; mark them for contact
  construction. Do not use “feet never slide” as a universal dance negative prompt.
- Keep each generator prompt within its verified action/duration capacity. A
  precise timing brief is not proof of precise model timing. Hand over full state
  at clip boundaries; video dissolves cannot replace missing transition movement.

Example direction (original, not an authenticated traditional choreography):
“The dancer acknowledges the guests, transfers weight before opening an arm arc,
turns with a visible replant, lets the sleeve follow, settles facing the audience,
then makes space for the tray bearer. The bearer keeps both hands under the tray
and uses small, deliberate steps; the guard remains still through the solo.”
Assign beat timings only after the music is known or an explicit draft clock is chosen.

For authorized Blender construction, the installed `blender-contact-animation`
skill's natural-motion-and-dance reference covers motion sources, transitions and
contact modes. For an actual candidate, `animation-causality-review` covers dance
quality. No model installation or paid generation is implied by writing this brief.
