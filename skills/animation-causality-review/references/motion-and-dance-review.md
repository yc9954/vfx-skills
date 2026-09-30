# Motion variety, dance and transitions

Review a produced candidate, not a promise in a prompt. Identify motion source,
retarget version, music version/offset and whether contact modes are authored or
inferred. This review does not require installing a new model or generating video.

## Keep verdicts separate

- **Body/contact:** use full-body and hand references where relevant. Ordinary
  posture and zero penetration are not evidence of performance quality.
- **Temporal continuity:** inspect a window around boundaries, not just endpoint
  pose similarity. Compare root/limb velocities, support mode, grip, object pose,
  intended direction and actual accumulated rotations. Check loops' root advance.
- **Music:** compare selected movement accents with actual beat/phrase markers.
  Preserve intended syncopation and pauses. A declared BPM or nearest-beat score
  does not establish musicality, especially with changing tempo or unreviewed audio.
- **Performance/variety:** ask whether intent, preparation, effort, contrast,
  recovery and character-specific choices read at normal speed. Random jitter,
  speed changes and many seeds are not automatically distinct, appealing actions.
- **Style/role:** distinguish original choreography, reference-inspired work and
  faithful reconstruction. Generic dancing in historical costume is not evidence
  of a specific traditional dance. Check dress/prop effects on the choreography.

Use verified for stated scope / failed / unverified per category. No single jerk,
foot-skate, beat-alignment or diversity score can approve all categories.

## Dance-specific contact and facing

Distinguish planted, pivoting, intentionally sliding, airborne and unknown
intervals. Verify the intended slide/pivot against choreography and support;
do not relabel an accidental failure after observing a bad metric.
A toe pivot can move the heel legitimately. A moonwalk-like action can slide on
purpose. A jump has no foot support during flight. Forward alignment is not
mandatory in every dance or backward/sideways task.
Check support geometry, load plausibility and upper-body compensation even when
the direction/slide is intentional. Do not excuse penetrating floors as a style.

## Transitions and ensembles

Inspect before, through and after the bridge. Matching root position with opposite
support feet, losing a held prop, or changing speed instantly is not a good join.
Check time warps and IK/parent switches at subframes when necessary. NLA blending
or an AI extension receipt does not establish actual continuity.

For groups, inspect the shared clock, formations, paths and space for limbs/props.
Canon/time offsets are appropriate only where intended. Hand-offs and shared
loads must still coincide. Identical clones can look mechanical, but intentional
unison should not be randomly desynchronized to satisfy a diversity metric.
Fixed tabletop framing should reveal readable movement, not conceal defects
behind cuts, zooms or excessive cloth/effects.

## Negative and positive controls

These are proposed review cases, not claims of tests run on a production rig.

| Case | Expected distinction |
|---|---|
| Matching end poses but root velocity reverses instantly | Pose metric may pass; join fails |
| Smooth quaternion interpolation deletes a planned full spin | Smoothness is insufficient; choreography fails |
| Foot lock removes an intended pivot/slide | Lower skate score does not mean better motion |
| Forward correction rotates a deliberate side-step | Reject the correction, not the intended direction |
| High beat score but every limb pulses identically throughout | Rhythm score does not approve acting/variety |
| Pop/stop accent has high jerk but supported, intended timing | Do not blindly smooth away the style |
| Phase-shifted dancers miss a two-person prop exchange | Individual dance timing cannot approve shared contact |
| Repeated phrase has expressive variation but matching unison accents | Preserve variation and group intent together |

Inspect actual saved/evaluated candidates. If only stills can be seen, retain
unverified normal-speed performance; if audio cannot be heard, retain unverified
musical expression even when event times are numerically aligned.
