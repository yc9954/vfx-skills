# Director-grade prompts: terms that produce an observable brief

## Contents

1. Choose the output and allocate control
2. Build the shot/state specification
3. Cinematography and editing lexicon
4. Lighting, material and CG lexicon
5. Projection-safe staging and compositing
6. Reference strength, extensions and prompt tests

## 1. Choose the output and allocate control

Classify `projection_master`, `cinematic_footage`, or `look_motion_pilot` first.
For a master, hold its registered raster and anchor geometry; an actual filmed
commercial may use coverage and moving cameras. Do not make a camera move merely
because the request says cinematic. A pilot is not a calibrated final master.

Assign each requirement an owner:

| Owner | What belongs there |
|---|---|
| Generation prose | Appearance, readable acting, shot intent, light, broad effect behavior |
| Verified provider settings | Actual mode, duration, resolution, reference fields, audio toggle, supported preset IDs |
| Blender / deterministic post | Exact plate circles, millimetre geometry, four-seat transforms, masks, typography, retiming, color matching, alpha handling |

Name the **generation unit** as well as the delivery surface: one seat asset,
central-stage asset, full-table raster, or filmed shot. If local post instances
one seat four times, the generation prompt requests one seat, not four repeats.
Assign each effect one owner: if a fan wipe or rim ring is made in post, do not
also ask the video model to perform that wipe or draw that ring. Generate a
settled outgoing state and separately request an effect asset only if needed.
For full-table generation, fixed anchors remain a request to verify, not an
alternative to registration; choose it deliberately and state that risk.

Terms such as PBR, ray tracing, ACES, FLIP, Cryptomatte, 16-bit EXR and 180°
shutter have technical meanings. A text request can evoke their appearance but
does not establish that the generated file used those algorithms or contains
those data. Keep implementation specifications separate from visual intent.

Use **term + subject + visible change + time/direction + invariant**.
Bad: “epic anamorphic cinematic match cut, fluid simulation, amazing CG.”
Better: “A motivated soft key from the diner's edge makes the ceramic highlight
roll across the jar as she tilts it; the plate centre and exposure remain fixed.”

The same rule applies to character craft. Replace “overlapping action” with “her
forearms stop the jug first; shoulders recover next; sleeve folds and fingertips
settle last while both grip regions stay fixed.” Replace “moving hold” with “the
pour pose, eye target and support feet remain stable while a small breath, finger
pressure and the final sleeve fold keep the character alive.” Use the installed
`character-performance-animation` contract when thought, face or personality matters.

## 2. Build the shot/state specification

Use only the fields needed for the task, in this order:

1. Delivery mode, intended duration, single take or number of actual cuts.
2. Typed reference roles and which decisions remain free.
3. Start blocking: actor/prop identity, position, facing, support and attention.
4. Timed action: preparation → contact → load transfer → result → recovery.
5. Framing/optics/move OR explicit fixed-raster contract.
6. Light direction, shadow receiver, material response and palette.
7. Effects: source, trigger, travel, collision/occlusion, dissipation and end state.
8. End state + continuation handle; audio intent if applicable.
9. Short task-specific exclusions. Keep detailed QA outside the generation prose.

Time labels organize intent; they are not frame-accurate execution guarantees.
Beat boundaries are not automatically edits. Fit complete actions into the
verified duration rather than accelerating several interactions into one second.
Choose a master take when contact continuity is important; choose coverage only
when alternate views improve the intended story and are compatible with output.

## 3. Cinematography and editing lexicon

Translate terms into the visible result. Do not list incompatible camera moves.

| Term | Observable instruction | Boundary / test |
|---|---|---|
| Locked-off master / oner | One unchanged view contains approach, grasp, pour and release | Check corner/plate anchors; no zoom or unrequested cuts |
| Mise-en-scène / blocking | Name where each actor stands, faces and moves; route attention | Distinct roles, no prop or actor swaps |
| Motivated push-in | Camera approaches the face after a visible discovery | Footage/pilot only; not registered table geometry |
| Dolly / truck / tracking | Specify camera translation direction or who it follows | Dolly is not an optical zoom; track path must be stated |
| Pan / tilt | Camera rotates horizontally/vertically to reveal the named subject | Do not use as shorthand for moving the subject |
| Rack focus | Focus transfers from foreground spoon to face; first softens as second sharpens | Needs readable depth; do not request deep focus simultaneously |
| Deep focus | Hands, vessel opening and receiving bowl all stay readable | Useful for contact review and projection; avoid excessive blur |
| Macro insert / coverage | Separate close shot shows the fingers or liquid contact | Can be a diagnostic deliverable, not a master camera change |
| Dolly zoom | Subject stays similar size while background expands/compresses | Deliberate disorientation; usually wrong for tabletop registration |
| Match on action | Cut during the same movement, continuing pose, direction and velocity | Specify outgoing and incoming motion phases; reject repeated pickup |
| Graphic match | Align a named shape/position across two images | Doesn't guarantee scale registration; align locally when exact |
| Eyeline match / 180° continuity | Keep gaze target and screen direction legible across coverage | Opposite physical diners are a separate projection problem |
| Occlusion wipe | A visible fan crosses a defined mask, revealing the next state | Define coverage and retained objects; do not excuse teleportation |
| Dissolve | Overlap two pictures for an intentional time/mood shift | Avoid double hands/props; not a repair for bad contact or white-balance drift |
| J-cut / L-cut | Next audio begins before the picture / old audio continues after it | Audio edit only; it doesn't repair visual continuity |
| Hold / settle / handles | Reserve stable material before or after a completed action | Useful for editing/extensions; duration is a creative choice, not model law |

Camera/lens brand names are optional style cues, never a substitute for these
instructions. Focal length needs sensor/framing context for physical work; a
generated “85mm” look is not measured lens metadata. For miniature CG describe
scale, proportions and material response instead of automatically adding heavy
tilt-shift, grain, lens distortion or exaggerated bokeh.

## 4. Lighting, material and CG lexicon

Choose a few discriminative cues. For cute crafted miniatures, preserve clear
silhouettes and restrained surface detail rather than requesting pore-heavy
hyperrealism. These are look-development options, not a mandatory preset.

| Term | Say what should be visible | Owner / failure to reject |
|---|---|---|
| Motivated key, fill, rim | Identify the visible/implied light source; key direction; softer fill | Generation look / Blender lighting; no unexplained light flips |
| Contact shadow / ambient occlusion | Tight darkening only where soles or jar meet support; broader shadow falls inward | Receiver and light are explicit; no floating black halo |
| Soft highlight roll-off | Bright ceramic remains bright but retains rim and surface detail | Color/lighting; do not claim an HDR deliverable from this phrase |
| Roughness / specular breakup | Uneven, restrained highlight width on glaze; avoid uniformly plastic surfaces | Appearance cue, not a supplied roughness map |
| Coat / glaze | A thin glossy layer above the colored ceramic base | Distinguish vessel glaze from metallic gold trim |
| Subsurface scattering | Gentle light diffusion through skin, wax or a named translucent material, not waxy translucency everywhere | Generative look vs actual shader are separate |
| Fabric sheen / anisotropy | Soft edge sheen or directional highlights aligned with woven fabric | Pick the relevant material response, not glossy rubber cloth |
| Normal/bump vs displacement | Fine surface relief affects highlights; geometry relief affects silhouette | Real displacement requires collision/registration rechecks |
| Secondary motion / follow-through | Sleeve and ribbon lag the arm then settle after it stops | Must not pull a held handle away from fingers |
| Viscosity / surface tension | A named material has observable stream/sheet, breakup and leveling behavior | Food/liquid specifics belong to `food-vfx-director`; naming physics isn't simulation |
| Ripple / splash / mist | Effects begin at the named trigger/contact, expand and fade | Food/liquid scale and rejects belong to `food-vfx-director` |
| Volumetric light / atmospheric depth | Light becomes visible in a small amount of vapor, with controlled falloff | Do not veil the contact or make the whole table foggy |
| Emission / bloom / light spill | Gold practical glows with a small halo and lights adjacent surfaces | Bloom not white wash; preserve plate edge visibility |
| Beauty / shadow / holdout / matte passes | Separate visible color, received shadow and occlusion masks in actual render/post | Do not imply a generated RGB MP4 supplies these passes |
| Cryptomatte | Use rendered object/material IDs to isolate the plate or cast | Blender/compositor feature; not a magic video-prompt keyword |
| Straight/premultiplied alpha | Match input alpha interpretation when compositing | Verify actual alpha; prevent dark/bright fringes |
| Linear-light compositing / color transform | Combine and grade using a defined real color pipeline | Don't stamp “ACES” onto an unknown encoded RGB output |

For generic effects state emitter → onset condition → transport → receiver/occlusion
→ decay → final location. When food/fluid identity, rheology, wetness, steam or
particulate scale matters, use the installed `food-vfx-director` rather than growing
a second material rulebook here. Keep precise simulation methods in the Blender
implementation brief, not as a claimed provider guarantee.

## 5. Projection-safe staging and compositing

- Keep the calibrated anchors, table aspect and floor coordinates outside the
  model's free choices. Direct “cinematic” attention through lighting, timed
  reveals, actor blocking and material contrast, not a random drone move.
- A four-quadrant composition means four content regions, not a filmed shot of
  four guests. Rotate each approved seat content and its light/shadow together.
- For the shared centre, use plan-view-readable motifs and deliberate staged
  reveals. Do not promise one perspective illusion valid from all seats.
- Prefer matte/occlusion reveals for transitions inside the content plane when
  anchors must survive. Preserve support and held-object ownership across them.
- Generate expressive materials/acting where allowed; keep plate-bound circles,
  exact gold paths, typography and registration-sensitive masks in local post.
- In a Projection Master, route attention with key pose, gaze, stillness, partner
  reaction and local contrast while the registered camera remains locked. Promo-style
  camera moves or coverage belong to a separately named cinematic deliverable.
- “Transparent background,” “shadow pass” and “fixed camera” in a prompt are
  requests, not proof of alpha, separable shadows or geometric registration.

## 6. Reference strength, extensions and prompt tests

For each reference assign exactly which properties it controls. The correct
package may be image-only, sparse blockout + look image, motion-only guide + look
image, or a near-final source. Do not always add more inputs. A bad hand guide
must be repaired; a gray preview must not become a material mandate. When asking
for creative freedom, state the free properties (fabric, microacting, vapor)
and fixed ones (actor identity, prop inventory, camera, plate layout, supports).

For extension, carry actual last poses, hand ownership, support, velocity,
lighting and palette. The last image does not encode velocity. Inherit a usable
video tail only if the selected mode supports it. Confirm whether the returned
file includes the source or only new footage; don't assume duration semantics.

Before paid work, lint for: fixed camera + orbit; deep focus + extreme bokeh;
exact circular registration + whole-frame tilt; one take + hard-cut commands;
silent output + required music; unsupported reference mode; exact CG passes from
RGB generation; a release before support. Fix the contradiction, not with extra
adjectives. Keep prompt QA distinct from actual candidate QA.

To test whether terminology helps, keep the same approved inputs/mode/action and
change only the direction block. Compare identity, action completion, contact,
camera/anchor drift, material consistency and cut boundaries. Use an explicit
small paid-test budget if generation is requested; offline drafting alone spends
nothing and does not establish that the new wording improves generated quality.

Sources and current tool boundary: [dated evidence](higgsfield-prompting-evidence.md).
This reference is local synthesis; it does not adopt provider marketing promises.
