# Primary sources and tool boundary · checked 2026-09-30

This is a dated research snapshot, not a permanent API contract. Distinguish
provider advice, observed local tool schema, and our production decisions.

## Primary-source evidence

- [Higgsfield camera-control guide](https://higgsfield.ai/blog/ai-video-camera-control)
  says a camera move needs start/end position, speed/path and framing, and separates
  text prompts from explicit Cinema Studio settings. This supports observable move
  descriptions; it does not prove deterministic execution.
- [Higgsfield Academy camera examples](https://higgsfield.ai/academy) define a
  static shot as no drift, shake, breathing, reframing or end-frame change. Use
  those as projection-master reject criteria and verify the actual output.
- [BytePlus Seedance 2.0 tutorial](https://docs.byteplus.com/en/docs/ModelArk/seedance-2-0),
  [prompt guide](https://docs.byteplus.com/en/docs/modelark/seedance-2-0-prompt-guide)
  and [video-generation tutorial](https://docs.byteplus.com/en/docs/modelark/video-generation-tutorial)
  document typed/numbered assets, ordered reference instructions and concise
  subject/background/camera motion descriptions. Provider documentation does not
  establish which subset the current Higgsfield integration exposes.
- [Higgsfield Seedance prompting guide](https://higgsfield.ai/blog/seedance-prompting-guide)
  recommends declaring shot structure and separating shot actions. Its examples
  include both montage and a continuous view. Use the requested format, not every
  effect in the examples. Read via indexed official page; direct fetch failed.
- [Higgsfield: how Cinema Studio was built](https://higgsfield.ai/blog/how-we-built-cinema-studio)
  describes camera/optics choices as model-driven, tuned visual characters,
  explicitly not identical to shooting with real optics. This supports pairing
  named lenses with a visible target instead of treating them as physical proof.
- [Higgsfield reference-video VFX workflow](https://higgsfield.ai/blog/VFX-with-Seedance-4k)
  advocates analyzing source performance/camera/timing, retaining chosen parts,
  and changing the environment/effects. Its exact-reproduction language is a
  requested constraint, not a verified guarantee for our output.
- [ByteDance Seedance 2.0 launch](https://seed.bytedance.com/en/blog/seedance-2-0-official-launch)
  describes multimodal references and extension/editing. It also acknowledges
  detail, multi-subject consistency and complex-edit limitations. Do not equate
  model-family support with a particular Higgsfield CLI mode. Read via indexed
  official text; direct fetch was unavailable on this check.
- [Adobe match-cut guide](https://www.adobe.com/creativecloud/video/post-production/cuts-in-film/match-cut.html)
  distinguishes graphic, action and audio matches. Plan the relation between
  outgoing/incoming shots instead of requesting an unspecified smooth transition.
- [Adobe J/L cuts](https://www.adobe.com/creativecloud/video/discover/j-cut-and-l-cut.html)
  defines audio starting before the new picture or continuing after the old one.
  These are sound-picture offsets, not a visual dissolve.
- [Adobe tracking](https://www.adobe.com/creativecloud/video/discover/tracking-shot.html)
  and [dolly zoom](https://www.adobe.com/creativecloud/video/production/cinematography/camera-shots-and-angles/dolly-zoom-shot.html)
  distinguish following a subject from the specific move/zoom combination that
  changes background perspective while keeping the subject's apparent size.
- [Blender Principled BSDF](https://docs.blender.org/manual/en/dev/render/shader_nodes/shader/principled.html)
  defines roughness, coat, sheen and scattering. Use those material concepts to
  describe distinct surfaces. Inspect the installed Blender before using exact
  node fields; this live manual can describe a newer development version.
- [ARRI Ensō lens manual](https://www.arri.com/resource/blob/389646/5797289cce139989ffd094dcf0c1d545/ens%C5%8D-prime-lenses-user-manual-data.pdf)
  links minimized focus breathing with focus racks that do not noticeably alter
  framing. This is an optics reference, not evidence that a video model honors it.
- [Blender Cryptomatte](https://docs.blender.org/manual/en/4.2/compositing/types/mask/cryptomatte.html)
  requires render data for object/material masks. A generated RGB file does not
  acquire those IDs because its prompt names Cryptomatte.
- [Blender shadow catcher/holdout](https://docs.blender.org/manual/en/2.90/render/cycles/object_settings/object_data.html)
  explains separate shadow reception and alpha holes for compositing. Treat as
  concepts; verify the installed version before implementing properties.

No controlled quality comparison was run in this research. “Professional terms
improve results” is a plausible direction to test, not a measured universal law.

## Installed Higgsfield CLI observation

Read-only checks on 2026-09-30: `higgsfield version`, `model list --video --json`,
`model get seedance_2_0 --json`, `model get seedance_2_5 --json`,
`workflow list --json`, `workflow get cinematic_studio_video_4_0 --json`, and
`generate create --help`. Observed CLI: 1.1.24. No generation or upload was run.

| Entry | Observed schema facts | What remains unknown |
|---|---|---|
| `seedance_2_0` | `mode=std/fast`; resolution includes 480p, 720p, 1080p, 4k; fast disallows 1080p/4k; image/video/audio references; start/end image; `generate_audio` | Duration upper bound not stated in returned integer field; current quote and input-specific restrictions |
| `seedance_2_5` | `mode=t2v/omni_reference/video_edit/video_extension`; extension direction forward/backward; resolution 480p/720p/1080p | Duration ceiling, extension return layout, actual quality and current quote |
| `cinematic_studio_video_4_0` | Separate workflow with camera model/lens/aperture IDs, palette and light fields, plus mode/media fields | ID values must be resolved from actual available presets; field presence alone isn't a valid submission |

Observed 2.0 reference rules: at most 9 image items counting start/end, 3 videos,
3 audios, and 12 total. Observed 2.5: 50 total, 30 image items; text-only mode
rejects references; omni reference mode needs media; video edit needs one video;
extension needs a video and an extension direction. Re-query before execution.

The current `generate create` help says local media paths can auto-upload.
Therefore even a seemingly local create command crosses an upload/billing
boundary. Keep research and drafting read-only; do not use create as a dry run.

`--camerafixed` and `--seed` were not in the inspected Seedance parameter lists.
Do not append historical flags to prompt prose or assume camera/lens UUIDs from
Cinema Studio are accepted by the plain Seedance model. Prompt labels such as
`VFX:` or `LIGHTING:` are prose organization, not demonstrated special syntax.
Reference placeholders must be bound to actual uploaded attachments/recognized
labels by the current integration; `@img1`, `@Image1` and `<<<video_1>>>` are not
interchangeable API fields merely because blogs use them.

## Local decisions (not provider claims)

Keep table registration and exact effects in Blender/post, permit expressive
variation only in named properties, review actual generation, and preserve a
per-job budget. Keep primary sources linked and recheck volatile claims. Do not
select a new paid model, remove a policy restriction, or submit a job merely to
make a prompt example executable.
