# Shared motion contract and translation language

Use this file to express the same action consistently in Blender blocking,
generative-video prompts and candidate QA. It is a specification, not proof that
any implementation or generated clip obeys it.

## Compact contract card

```text
TASK / INTENT:
CHARACTER / BODY ASSUMPTIONS:
PROP / LOAD: light | moderate | heavy-for-character | unknown; why
START SUPPORT: prop support; body support; feet/contact patches
GRIP ROLES: left/right contact regions; support/control/opposition
WORKING RANGE: neutral/task range/near-limit/unknown by affected chain
KINETIC CHAIN: support -> body -> arm -> hand -> prop
BALANCE: preparatory shift; stance/replant; load distance consequence
PHASES: prepare -> contact -> acquire -> transfer -> act -> decelerate -> new support -> release -> settle
END SUPPORT / VELOCITY:
READABILITY: silhouette/hold/diagnostic view needed at miniature scale
UNKNOWN / EXCLUSION:
```

## Blender blocking translation

| Contract field | Blocking/contact decision |
|---|---|
| Start support | Parent/constraint/dynamic owner before pickup; prop must not move early |
| Grip roles | Hand targets plus finger/thumb contact patches and handle/body regions |
| Working range | Calibrated joint frames, elbow/pole continuity, no hidden stretch/clamp |
| Kinetic chain | Pose feet/pelvis/trunk/shoulder before solving hand precision |
| Balance | Support foot/patch and visible weight shift; preserve contact when pelvis changes |
| Load distance | Keep close or author corresponding counterbalance/effort when extended |
| Phases | Key support/constraint influence changes only after the enabling contact |
| Settle | Match position and velocity through IK/FK/parent switches; add bounded recovery |
| Readability | Delivery silhouette plus close contact/side diagnostic views |

Pose/IK order for a loaded interaction:

1. Place the prop, receiver and actual support surfaces.
2. Establish feet/base of support and pelvis/trunk relation to the task.
3. Block shoulder girdle, elbows and forearm orientation with joint margin.
4. Align hands and choose contact patches; then articulate fingers/thumb.
5. Author support transfer and maintain continuous relative contact.
6. Add effort, follow-through and secondary motion after the causal chain works.

Do not optimize penetration alone. First preserve plausible posture and contact
orientation, then reduce gaps/intersections within a scale-appropriate tolerance.

## Human-motion prompt vocabulary

Translate abstract mechanics into visible verbs:

| Instead of | Prompt observable behavior |
|---|---|
| “realistic biomechanics” | establishes a two-handed grip; elbows remain softly flexed; shoulders and torso join the lift |
| “shift center of mass” | shifts weight onto the nearer foot before lifting; pelvis moves toward the support side |
| “use kinetic chain” | feet brace, knees/hips yield slightly, torso and shoulders rise with the hands |
| “heavy object” only | slower pickup, load kept near torso, stance widens, brief stabilizing correction after lift |
| “natural hands” | thumb pads oppose the handle; finger pads close around it before load transfers |
| “good ROM” | wrist stays near neutral; forearm rotation and elbow position orient the hand; no arm stretch |
| “follow-through” | jug decelerates upright, shoulders and torso make a small delayed recovery, then settle |

Use the minimum cues that distinguish this task. Prompts become brittle when every
possible joint is commanded. State the action order, fixed contacts and visible
consequences before decorative acting.

## Provider-neutral handling template

```text
Start with [prop] supported by [surface] and the character balanced on [support].
[Hand roles and contact patches] approach and establish contact before the prop moves.
The character [visible preparatory weight shift / stance change], keeping [joint]
within a comfortable working posture by sharing the reach through [upstream joints/body].
Only after the grip is secure, [load transfer and primary action]. As [load distance
or resistance] changes, [body/feet response] remains visible and contact stays continuous.
[Deceleration/new support]. The new support takes the load before the hands release;
[brief motivated follow-through] settles into [end pose/velocity]. Preserve [fixed
guide pose/contact/support facts].
```

## Heavy jug template

```text
The ceramic jug begins fully supported. She approaches with both hands open and
settles them on the established handle and support regions. Her thumb and finger
pads oppose the handle while the other hand bears and steadies the jug body.

Before lifting, she widens and organizes her stance and shifts weight toward the
vessel. Her wrists stay near neutral; forearm rotation, softly flexed elbows,
shoulders and torso share the reach. Only after both grips are secure does the jug
leave its support. She keeps it close while lifting, then visibly counterbalances
as she moves it outward and tilts it. Both hands remain continuously attached.

She rotates the jug upright with controlled deceleration, brings it back over its
support, sets it down before easing the fingers open, withdraws both hands, and
settles through shoulders, torso and feet. Preserve the guide's exact grip regions,
foot support, vessel geometry and phase order.
```

Use “heavy” only relative to the character and performance. If load is unknown,
request deliberate supported handling without inventing strain.

## Candidate-review translation

Review the same contract as independent claims:

- grip before load;
- correct contact surfaces and thumb/opposition role;
- continuous contact while the hand owns the prop;
- plausible joint path and working-range margin, not just legal endpoints;
- preparatory weight shift and appropriate feet/base support;
- body reacts to prop/load and prop reacts to body input;
- support/parent/constraint transitions follow their enabling event;
- controlled deceleration, new support, release and settling;
- action remains readable at delivery scale and normal speed.

Record `verified for stated scope`, `failed`, or `unverified` for each material
claim. A prompt, solver target or guide is design evidence; the actual evaluated
candidate is required for acceptance.
