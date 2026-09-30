# Full-body rig and coordination review

Use on an existing rig/action candidate, especially when an auto-rig or successful
joint-angle test is being presented as ready for many actions. Review the affected
kinematic chains; do not demand unrelated motions from every background actor.
This is animation qualification, not a medical assessment of a performer.

## Separate four claims

1. **Joint model/calibration:** anatomical region, rest/bind frame, pivot, axis and
   sign are identified on both sides. State which motions are approximated and
   which are independently controllable. A bone named Knee is not a calibration.
2. **Deformation:** evaluated skin maintains a plausible silhouette across the
   intended range and combined poses; skin, clothing and neighboring limbs do not
   intersect unacceptably. Good bone targets can coexist with collapsed skin.
3. **Contact/coordination:** actual support patches, body adjustments and prop
   relationships agree through the whole action, including transitions.
4. **Performance:** intent, effort, rhythm and recovery are readable at normal
   speed. Still poses, smooth splines and anatomical limits cannot establish this.

Keep these verdicts separate. A successful simple hinge audit does not certify
coupled knee motion, multi-axis hips/shoulders, feet, balance or skin. Missing
calibration is unverified, not a license to use universal default human angles.

## Inspect the linked body, not a target list

- Feet: compare heel/forefoot/toe patches with the real support surface. Distinguish
  support roll, intentional pivot, swing clearance and slip; on a moving support,
  measure relative to it. An ankle marker at ground height proves little.
- Knees/hips: inspect bending direction and pole continuity near extension, leg
  reach without hidden stretch, pelvic response and skin during deep/combined poses.
  A declared hinge approximation may be appropriate; do not equate it with a full
  anatomical knee or apply its off-axis failure rule to a deliberately coupled knee.
- Spine/neck: look for regional participation, not all motion at one waist/neck
  pivot. Gaze should not demand unlimited head rotation while the torso stays fixed.
- Shoulder/arm: inspect clavicle/scapular contribution as needed for the task,
  armpit shape, elbow continuity, forearm twist and wrist orientation. A hand target
  reached by stretching the arm or twisting only the wrist is not successful reach.
- Hands: use [hand-grasp-review.md](hand-grasp-review.md) for articulated grasping.
  Successful grasping must not invalidate shoulder, trunk or foot support.
- State changes: inspect before/at/after IK/FK and parent-space switches, support
  changes, stopping and turning. Sample subframes for fast changes; unchanged
  endpoints do not exclude mid-transition pops or collisions.
- Balance: identify actual supports and the status of any mass model. Pelvis/root
  is not measured whole-body CoM; estimated CoM is not measured contact force or CoP.
  Static support-region reasoning cannot automatically reject running or flight.
- Wearables/props: check the final clothing/footwear and carried objects. Diagnostic
  visibility changes are not repairs. Ragdoll/physics assets do not prove controlled
  balance, nonpenetration or natural performance in the delivered animation.

## Behavior-level qualification

Select the planned role's complete actions: weight shift, walk/start/stop/turn,
low reach/squat or sitting, step-up/down, front/overhead reach, carrying/placing,
and jump/landing or instrument handling only if used. Preserve intentional styles,
body differences, assistive supports and task-specific sideways/backward motion.

Record per action: scene/rig/output identity; interval/FPS; anatomy calibration;
surface/prop and any load assumption; evaluated measurements with tolerances;
front/side close inspection; normal-speed viewing; failures and exclusions.
Use **verified for stated scope**, **failed**, **unverified**. A tray carry may pass
while kneeling remains unverified. Do not convert that to “all joints approved.”
When transferring the rig to different proportions, clothes or footwear, recheck
the affected actions rather than inheriting the first character's approval.

## Counterexamples for validators and review

Use suitable cases to challenge a claimed check. These are expected distinctions,
not tests that have already been executed on the production rig.

| Candidate | Required distinction |
|---|---|
| Zero foot drift; pelvis dragged ahead on stretched legs | Foot drift may pass; reach/coordination fails |
| All angles inside separate ranges; combined shoulder pose collapses the armpit | Angle checks cannot approve skin/combined pose |
| Knee endpoint poses correct; pole flips between them | Endpoint-only evidence is insufficient; temporal defect fails |
| Ankle marker on floor; toes visibly buried | Point target passes; sole geometry fails |
| Both hands touch tray; support foot loses ground when pelvis solves | Hand-only approval cannot approve full action |
| Smooth intentional jump with feet airborne | Do not require grounding or static support in flight |
| Character on a moving platform with stable relative contact | World-space motion alone is not foot sliding |
| Correct crouch bones; thigh cuts through the final skirt | Skeleton-only approval cannot approve the dressed character |

The shared [joint/coordination reference](../../human-motion-biomechanics/references/joint-rom-and-coordination.md)
owns working-range and compensation vocabulary. The installed construction skill's
[full-body design reference](../../blender-contact-animation/references/full-body-biomechanics.md)
owns Blender implementation choices. Consult both at their boundary when a joint
interpretation is uncertain; this review does not authorize rebuilding the rig.
