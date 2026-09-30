# Character performance QA

Use this rubric to review a design or an existing candidate. A design review can
find missing intent; only playback of the identified candidate can verify performed
timing and acting. Keep this verdict separate from physical/contact QA.

## Evidence views

For a candidate, review:

1. normal-speed delivery framing, including neighboring actors and sound if present;
2. silhouette/thumbnail playback for pose and attention hierarchy;
3. frame or stepped inspection around thought changes, contact, accents and settles;
4. a readable face/hand diagnostic when the delivery view hides required detail;
5. comparison with the versioned performance and biomechanics contracts.

Diagnostic views do not replace the audience view. If playback, face resolution or
audio is unavailable, mark the affected claim unverified.

## Separate verdict axes

Use `verified_for_scope`, `failed` or `unverified` for each required claim. Do not
average them into one naturalness score.

| Performance axis | Review question | Frequent false green |
|---|---|---|
| Objective/read | Can a viewer tell what the character wants and monitors? | Correct action list with no readable intention |
| Thought → action | Does attention/decision prepare each meaningful action or change? | Face reacts after the body for no reason; decorative anticipation |
| Key poses | Do key moments have specific, readable silhouettes and prop relations? | Smooth motion with weak or duplicate poses |
| Line/asymmetry | Do line of action and purposeful asymmetry support role/emotion? | Random offsets, broken balance or generic S-curves |
| Timing/rhythm | Do pauses, accents, spacing and phrase contrast fit thought and effort? | Uniform easing and equal beat durations |
| Gaze/head | Are targets, eye/head lead, shared glances and release motivated? | Eyes drift, stare, or snap on a loop |
| Facial transition | Do lids/brows/cheeks/mouth/jaw change coherently and specifically? | Instant emotion icon; mouth-only smile; all regions mirror |
| Gesture hierarchy | Is one primary idea clear, with secondary/tertiary support? | Every limb, cloth piece and face control competes |
| Overlap/settle | Do followers start/stop in a material- and action-specific sequence? | Same frame offset/damping everywhere; endless sway |
| Moving hold | Does the pose stay readable while sparse signs of life remain? | Frozen frame or random channel noise |
| Personality | Are choices specific to this character and scene? | Generic “cute,” “confident” or “sad” cycle |
| Partner/ensemble | Do reactions and shared attention reveal relationship and cause? | Everyone moves simultaneously or secondary actors ignore events |
| Prop as acting | Do gaze, hand shape, effort and recovery express treatment of the prop? | Contact passes but prop is emotionally invisible |
| Appeal/readability | Is the performance engaging and legible without design clichés? | Large eyes/bounce substitute for intention |
| End state | Is support, velocity, attention and emotional residue usable for the next beat? | Animation stops because the clip ends |

## Physical QA is a different gate

The performance pass does not approve ROM, balance, load, grip, foot contact,
penetration, support transfer or prop/fluid causality. Compare those against the
versioned `human-motion-biomechanics` and contact contracts. Conversely, a physical
pass does not approve thought, personality, timing, gaze or appeal.

If the same defect affects both—such as a weightless lift with no effort—record two
findings: the physical cause and the performance consequence. Repair causal/contact
failure first, then preserve or rebuild the acting intent.

## Projection Master gate

For a registered master also verify:

- camera/crop/anchors remain locked; performance, not camera drift, directs attention;
- key silhouette, head direction and major reaction read at delivery scale;
- partner offsets do not produce quadrant confusion;
- no promo cut, rack focus, zoom or reframing was introduced;
- microacting hidden by scale is not used as evidence of a passed audience read.

## Tarakjuk regression gates

Select gates from the current performance contract, actor inventory and rig capabilities.
Mark inapplicable beats `not_applicable` with a reason, not `failed` or a fabricated pass.
For example, a solo expert pour needs no partner glance, comic overshoot or visible relief.
Never add a character or a physical disturbance merely to satisfy this example.
In addition to the biomechanics/contact regression, check the applicable items:

- thought/eye preparation before the reach and before the return;
- a motivated shared glance only when a partner and exchange are specified;
- load-appropriate effort and controlled arrival without grip or support drift;
  require overshoot only when the approved performance calls for it;
- sleeve/body/finger overlap with named lead/follow order;
- partner stir/reaction rhythm when a partner task is actually present;
- moving-hold life during the pour without camera/contact drift;
- controlled upright/return; recoil, relief or smile only if motivated and designed;
- support-before-release and staggered final settle;
- no default big-eye, bounce or random hand-flutter shortcut.

Name missing controls separately from missing acting: a rig without eyeballs or
facial shapes cannot pass a gaze/blink test via head rotation. Use a readable head,
shoulder and timing alternative and keep ocular/facial implementation unverified.

## Report shape

Record `candidate/version | axis | interval | intended beat | observed evidence |
contract dependency | verdict | bounded repair`. Findings should name the earliest
broken beat and its downstream effect. A prompt or blocking plan is intent evidence,
not proof that the generated or rendered candidate performs it.
