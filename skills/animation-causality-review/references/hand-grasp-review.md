# Anatomically plausible hands are a separate release gate

Use for articulated hands and prop handling, not every render. A finger-bone count,
near-zero wrist IK error or fewer interpenetrating vertices cannot certify a grasp.
For anatomy/calibration detail, if the companion is installed, read
[hand-biomechanics](../../blender-contact-animation/references/hand-biomechanics.md).
Otherwise use authoritative anatomy and actual observed reference poses; keep unknown axes unverified.
Use the shared [grasp and tool-use contract](../../human-motion-biomechanics/references/grasp-and-tool-use.md)
for purpose, opposition, contact-patch and two-hand-role vocabulary. This review still
owns the candidate verdict and must inspect the actual evaluated result.

## Evidence before scores

Inspect the actual saved candidate at a clear hand scale, palm/back/side where needed.
Record time range and separate observations from suspected causes. Check:

- Which surfaces face the object: finger/thumb pads, palm, nails or the back of the hand?
- Does the thumb oppose/support the intended contact, or merely stick up?
- Are MCP/PIP/DIP and thumb CMC/MCP/IP centres, bend direction and segment order plausible?
- Does an apparent wrist turn actually twist the wrist joint while the forearm stays fixed?
- Is the skin collapsing, stretching, webbing adjacent digits, or moving the wrong finger?
- Can the described support plausibly resist the load? A tray resting on palms is a
  support grasp; do not demand a closed power grip. Exact force closure remains unverified
  without force/friction/load analysis, even when the pose looks convincing.
- In a two-hand grasp, does each hand perform its declared support/control/stabilizing
  role without one hand's correction pulling the other through the prop or breaking stance?

Use distinct verdicts: anatomy/DOF, skin deformation, contact/support, temporal performance.
Failed required anatomy blocks overall hand approval even if contact distances pass.
Scalar weighted scores must not allow prettier materials or smaller penetration to compensate.

## Measurements must correspond to the claim

Evaluate relative joint rotations in calibrated anatomical frames, not raw world Euler angles.
Compare pad regions, normals and multiple spatially distributed contact samples with the
intended support. One nearest vertex can be incidental contact or a wrong-facing surface.
Check finger–finger, finger–palm, hand–prop, sleeve–prop and relevant body/support pairs.
Inspect before first touch through release and withdrawal. Sample fast motion between frames;
an integer-frame no-hit result is not a swept-collision proof.

Confirm actual evaluated mesh behaviour in left-only, right-only and both-hand tests.
Numerical hinge checks do not certify thumb opposition, comfortable combined posture or acting.
Record normal-speed review separately from stills; unavailable playback remains unverified.

## Negative controls that should fail the relevant claim

| Deliberately bad input | Expected rejection |
|---|---|
| Wrist exactly at target, thumb points away from the intended opposition patch | Grasp orientation/support, not an IK success |
| No prop penetration, PIP rotates around its long axis | Anatomical DOF |
| Small gap to a handle but only nail/back surfaces face it | Contact pattern; do not approve from min distance |
| Right-hand-only control changes left-hand evaluated vertices | Skin/controller independence |
| Both endpoints legal, wrist flips or fingers sweep through a handle between them | Temporal/swept safety |
| Prop starts lifting while fingers have not acquired the required support | Causal transfer |
| Rig mapping/axis calibration omitted | Unverified, not passed |

Positive counterexample: a palm-supported tray with lightly stabilizing fingers must not fail
merely because it is not a fist. A character with intentionally nonhuman anatomy follows the
user's explicit design, not a human-clinical range table; still test its stated mechanics.

When a user rejects hands, reopen the hand and adjacent arm/support claims. Preserve old
candidate evidence, label it failed/unverified, and do not quietly reuse it as a generation guide.
