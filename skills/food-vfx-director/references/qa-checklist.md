# Food-VFX candidate QA

Review the actual candidate and identify its file/job/version. A prompt, still,
submission receipt or previous report is not candidate evidence.

## Inspection passes

1. Watch at normal speed for material identity, appetite/readability and distracting artifacts.
2. Inspect consecutive frames around onset, first impact, maximum disturbance,
   shutoff and settling. Use slow playback without treating it as the audience view.
3. Compare scale and fixed anchors against the approved reference/guide.
4. Inspect a representative highlight/occlusion frame for material response.
5. If hidden or resolution-limited, mark the claim unverified; do not infer physics.

## Gates

### Source-sink causality

- [ ] Material begins at the actual source after the named trigger.
- [ ] Stream/vapor/particles do not emerge through walls or empty space.
- [ ] The receiver is positioned under or downstream of the exit.
- [ ] Impact response begins at contact, not before or elsewhere.
- [ ] Flow stops for a visible reason; final material and residue stay in plausible sinks.

### Motion and rheology read

- [ ] The requested material class is distinguishable from its nearest failure class.
- [ ] Stream coherence, narrowing, sheet/ribbon behavior and breakup agree with that class.
- [ ] Splash, ripple, wake, bubbles or steam match the event energy and scene scale.
- [ ] Motion has onset, response, decay and settle; no unrelated loop or frozen mid-flow.

### Particulate scale and continuity

- [ ] Grain/ingredient size is checked against named anchors at delivery resolution.
- [ ] Count, species, size and location do not drift or mutate between frames.
- [ ] Ingredients move with their carrier/food and obey containment/occlusion.
- [ ] Fine texture is not “fixed” by enlarging grains until they change the dish.

### Surface response

- [ ] Opacity/transmission, highlight width and scattering support the material identity.
- [ ] At delivery framing, food is distinguishable from its vessel: a filled dish
  must not read as empty merely because albedo, scattering and fine relief merge.
  Check a quiet/end frame as well as the active pour. A close diagnostic cannot
  substitute for this master-view check.
- [ ] Wetness follows contact history and is localized to touched surfaces.
- [ ] Contact shadows/occlusion ground food and vessels without black halos.
- [ ] No wax, plastic, chrome, chalk or glow unless intentionally specified.

### Projection and handoff survival when applicable

- [ ] Plate/vessel anchors, character scale and crop remain fixed.
- [ ] No camera drift, reframing, zoom, focus breathing or unrequested cut.
- [ ] Blender-established openings, grips, collision/support and end states survive.

## Verdict

Use `verified for stated scope`, `failed`, or `unverified` for each gate group.
Source-sink failure, wrong material class, gross scale/species drift or broken fixed
geometry blocks food-VFX approval. A minor highlight issue may remain a bounded
presentation defect. Pass the scoped results to the overall animation review; do
not relabel a technically playable file as an approved scene.
