# Evaluate the saved result, including the missing surfaces

Use when a saved-scene audit or grouping/contact claim conflicts with visible faults.
Keep this evidence separate from normal-speed performance and material review.

## Freeze the object under test

Record the saved scene hash, external dependency identities, evaluated frame/time,
software version, unit conversion, relevant modifiers and constraint states. Reopen
the scene without the builder's in-memory caches. The producer's target points are
not an independent measurement of the rendered surface.

Use an unchanged snapshot for a long audit. If the scene or cache changes during
measurement, keep the earlier evidence tied to its original input; mark a mixed run
invalid rather than stamping its report with the latest scene hash afterward.

## Name the geometry and meaning of each number

| Claim | Required distinction |
|---|---|
| No penetration | Evaluated surfaces, containment and crossing; a wrist/ankle or bounding-box gap is a different observation |
| Depth | Signed depth requires a justified inside/outside definition; nearest-triangle normal distance on an open garment is not general solid penetration depth |
| Grounded foot | Actual deformed sole versus intended support, including toe/heel; zero ankle drift may coexist with a floating shoe |
| Safe path | Approach, held interval, release and recovery, with subframes/swept checks where motion can cross between samples |
| Held/grouped prop | Actual transform dependency and support transfer; same collection, matching curves or coincident markers do not establish ownership |
| Entire film | Explicit tested intervals/pairs and exclusions; a critical-frame subset cannot establish all-frame or continuous safety |

Separate intersection counts, positive gaps and estimated depth. Record failures
even when another metric improves. Avoid global `collision_free: true` summaries
whose scope exceeds the tested geometry or time range.

## Challenge masks and approximations

- Show which vertices/triangles were included and excluded. A hand exclusion must
  not silently remove its cuff, forearm or the vessel rim. Inspect mask boundaries.
- Use all relevant shoe skin weights, including leg/toe contributions; convert
  rig-local thresholds to scene units explicitly. Check both heel and toe support
  on steps and curved dishes instead of substituting one horizontal plane.
- Use broad-phase bounds to find candidates, then test the relevant surfaces.
  A decimated mesh needs an approximation/error statement; a missed narrow handle
  or closed hole cannot become proof of safety. Preserve a known crossing control.
- Cache by geometry/deformation/frame identity, not object name alone. Inspect a
  changed pose and a known collision to expose stale BVHs or omitted modifiers.

## Test actual attachment

On a disposable copy of the saved scene, perturb the real owner control by a small
known transform. Check the prop root, handle/blade, carried food and secondary hand
in world space. Confirm the relation survives reopening and grip switching, then
restore the copy. This tests a bounded dependency claim; it does not prove pressure,
finger closure, load response or the whole path. Inspect those separately.

## Bound the conclusion

Report `candidate | pair/surface | interval | sample count/spacing | unit/tolerance |
method | exclusions | observation | verdict`. Sparse or partial audits remain
partial, even with zero hits. If a corrective modifier reduces one gap while
increasing cloth crossings or evaluation cost, reject that correction for the
affected requirements and compare with the last valid candidate.
