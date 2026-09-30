# Camera, lighting, color, sound vocabulary

Use precise production language. "Cinematic" is not a direction. "35mm, slow push-in, warm window key from frame-left" is.

**Local qualification (2026-09-30):** these are craft descriptions, not universal
model commands. Read `cinematic-cg-prompting.md` for term-to-visible-result examples
and projection-safe routing. A camera brand, focal length, LUT or renderer name
in prose does not certify optics, color space, bit depth or an actual simulation.

## Contents

1. Framing
2. Camera movement
3. Lens language
4. Light sources
5. Light direction
6. Light quality
7. Color discipline
8. Sound categories
9. Blocking language
10. Translating uncommon terms
11. Transition vocabulary

---

## 1. Framing

- extreme wide shot
- wide shot
- medium wide
- medium shot
- medium close-up
- close-up
- extreme close-up
- macro insert
- over-the-shoulder
- POV
- profile
- silhouette
- low angle
- high angle
- top-down
- dutch angle
- locked-off frame

## 2. Camera movement

- static camera
- slow push-in
- fast push-in
- pull-back
- tracking shot
- lateral tracking
- handheld micro-shake
- whip pan
- snap zoom
- rack focus
- tilt up
- tilt down
- orbit
- gimbal glide
- dolly-in
- dolly-out
- crane shot
- aerial shot
- Hitchcock zoom (dolly-zoom)
- dive (camera plunges downward)
- FPV (drone first-person flight)
- one-take shot
- bullet time
- bounce speed ramp (speed up - slow down - speed up)

Craft heuristic, not a universal rule: start with one dominant move per shot,
at most one motivated secondary move. A registered projection master may need
zero camera movement. The named move still needs a subject, start/end and pace.

## 3. Lens language

- 24mm. Wide, immersive, exaggerated proximity.
- 35mm. Natural documentary.
- 50mm. Intimate, human perspective.
- 85mm. Portrait, compressed background.
- 100mm macro. Texture, detail.
- anamorphic 40mm. Cinematic widescreen.
- shallow depth of field.
- deep focus.
- compressed telephoto background.
- distorted wide-angle proximity.

Focal length descriptions assume a sensor/framing convention. Perspective is
determined by viewpoint; do not imply that a lens number alone physically moves
the camera or compresses space. For generated video, pair lens language with
observable framing and foreground/background relationships.

## 4. Light sources

- cold refrigerator light
- harsh overhead kitchen LED
- moonlight through window
- neon sign spill
- phone screen glow
- car headlights
- streetlamp backlight
- fluorescent office light
- practical lamp
- candlelight
- monitor glow
- emergency red light
- sodium vapor street light
- police strobe
- theater house lights
- stage spotlight
- campfire flicker
- sunset through blinds
- under-counter kitchen LED

## 5. Light direction

- top light
- side light
- backlight
- underlight
- frontal soft light
- rim light
- bounce fill
- window key light
- motivated practical (the light source is visible in frame)

## 6. Light quality

- hard shadow
- soft diffused
- low-key lighting
- high contrast
- silhouette
- specular highlights
- volumetric haze
- steam catching backlight
- wet reflections
- desaturated palette
- cold blue-gray grade
- teal shadows
- clean commercial lighting
- gritty naturalistic
- blown-out overexposure
- crushed blacks

## 7. Color discipline

Define palette with concrete colors. Never write "cinematic colors."

Bad. "cinematic colors."
Good. "Cold blue-gray shadows, desaturated skin tones, greenish fridge spill, black negative space, no warm yellow tones."

If the user bans a color, obey it strictly. Repeat the ban in every clip of a multi-clip sequence.

Common palettes.

- Fincher cold. Cold blue-gray shadows, desaturated skin, black negative space.
- Deakins natural. Warm amber interiors, cool blue exteriors, clean contrast.
- Wong Kar-wai. Saturated warm reds, deep greens, hazy practicals.
- Glazer neon. Black, one dominant neon hue (magenta or teal), hard edges.
- Commercial creamy. Warm creams, soft pastels, clean whites, no harsh blacks.
- Safdie chaotic. Mixed sources, overlapping color temperatures, urban neon spill.

## 8. Sound categories

Even if the model does not generate audio, sound description helps structure rhythm.

Ambient.

- room tone
- distant city ambience
- rain on tin roof
- wind through leaves
- fridge hum
- fluorescent buzz
- traffic wash

Body and action.

- breath
- footsteps
- fabric rustle
- fork clink
- door hinge
- key in lock
- zipper
- stomach growl

Dramatic events.

- sudden silence
- low bass hit
- wet thud
- glass break
- distant thunder
- car door slam
- final sound cue before cut to black

Keep audio as a separate brief. Verify audio support and actual controls for the
selected provider/model/mode; old family-wide claims are not reliable. Labels
such as `Audio:` or `SFX:` organize prose, not an assumed API parser. In a silent
workflow, keep these cues for local editing rather than claiming generated audio.

## 9. Blocking language

Describe physical movement with six inputs.

- Who moves.
- Where they start.
- Where they end.
- What object they touch.
- What they look at.
- What their body reveals emotionally.

Example.

```text
The man stands in the kitchen doorway, shoulders collapsed. He slowly approaches the refrigerator, opens it with hesitation, leans into the cold light, then freezes when he sees the empty shelves.
```

This beats "a sad man goes to the fridge" because it is playable by the model frame by frame.

## 10. Translating uncommon terms

Common terms (section 2) work by name. For rarer cinematography terms, keep the term **and** translate it into observable change, or the model guesses:

```text
Term + target subject + visual change + foreground/background relationship + direction or speed
```

Example.

```text
Rack focus: shift focus smoothly from the leaves in the foreground to the person
in the background. The leaves gradually blur while the person's face changes
from soft to sharp.
```

Same pattern for snorricam, contra-zoom variants, tilt-shift, split diopter, speed ramps with specific curves. Numeric aperture and focal-length values are allowed, but the intended visible result phrased in words is what actually steers the model.

## 11. Transition vocabulary

Editing vocabulary to describe in visible terms and test on the selected model:

- **natural cut** — plain edit point, model picks the framing change
- **fade in / fade out** — to or from black
- **dissolve** — cross-fade, 1-2 seconds of overlap
- **white flash / black flash** — one-frame blast, impact punctuation
- **wipe** — new frame pushes the old one off
- **occlusion mask** — a foreground object covers the lens, the new scene is revealed behind it
- **match cut** — similar shape or motion bridges two scenes (moon → latte)
- **action cut / whip pan** — cut hidden inside fast motion with motion blur
- **motion relay** — subject exits frame A mid-move and lands in frame B continuing it
- **zoom-through** — camera dives through a pupil, keyhole or window into the next scene
- **ink-wash dissolve** — stylized bleed, common in guofeng / animation work

Rules of use. Name the transition and the exact moment it fires. One transition type per cut. When the choice is open, delegate: "choose the most suitable from [natural cut / occlusion mask / match cut] for the style of this film."

---

*Author: Serge Shima ([t.me/aimastersme](https://t.me/aimastersme) · [sergeshima.com](https://sergeshima.com) · [aimasters.me](https://aimasters.me)) · License: CC BY 4.0 — attribution required · Source: [smixs/visual-skills](https://github.com/smixs/visual-skills)*
