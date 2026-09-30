# Sources and evidence boundary · checked 2026-09-30

This is a dated source map, not a promise that a provider or local application
exposes every documented feature. Recheck the actual selected tool before execution.

## Official provider guidance

- [Higgsfield camera-control guide](https://higgsfield.ai/blog/ai-video-camera-control)
  separates text direction from explicit camera/lens/settings and recommends naming
  start/end framing, path and speed. Use this to reduce ambiguity, not to claim
  deterministic generation.
- [Higgsfield Academy camera examples](https://higgsfield.ai/academy) define a
  static shot with no drift, shake, breathing, reframing or end-frame change. This
  supports the projection-master lock vocabulary; actual outputs still need review.
- [BytePlus Seedance 2.0 tutorial](https://docs.byteplus.com/en/docs/ModelArk/seedance-2-0)
  documents typed image/video/audio references and distinct first/last-frame roles.
- [BytePlus Seedance 2.0 prompt guide](https://docs.byteplus.com/en/docs/modelark/seedance-2-0-prompt-guide)
  documents numbered asset references and recommends explicit reference subjects,
  actions and ordered edits. Attachment syntax remains integration-specific.
- [BytePlus video-generation tutorial](https://docs.byteplus.com/en/docs/modelark/video-generation-tutorial)
  recommends concise subject/motion, background/motion and camera/motion direction.
  Version limits and parameters are volatile; do not hard-code them here.

## Official CG references

- [Blender Principled BSDF](https://docs.blender.org/manual/en/dev/render/shader_nodes/shader/principled.html)
  distinguishes roughness, specular, transmission and subsurface/volume response;
  the manual specifically cites milk as a subsurface-scattering use case.
- [Blender liquid viscosity](https://docs.blender.org/manual/en/3.6/physics/fluid/type/domain/liquid/viscosity.html)
  confirms viscosity is a solver property. Verify the installed Blender version
  before copying UI values or property names.
- [Blender secondary liquid particles](https://docs.blender.org/manual/en/latest/physics/fluid/type/domain/liquid/particles.html)
  distinguishes airborne spray, surface foam and submerged bubbles; do not collapse
  them into one generic particle effect.
- [Blender liquid effectors](https://docs.blender.org/manual/en/latest/physics/fluid/type/effector.html)
  documents collision/guiding and substeps for moving effectors. A generative prompt
  does not create this solver evidence.

No controlled provider A/B test was run while creating this skill. The prompt rules
encode observable production hypotheses and known project failures; candidate QA,
not terminology, determines whether they worked.
