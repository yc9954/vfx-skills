# Architecture

## One route, one stage, one project record

```text
current user request + existing film_state.json
                    ↓
         backend / stage / required specialists
                    ↓
 reference → performance + physical contracts → implementation
                    ↓                         Blender | Higgsfield | hybrid
           actual candidate → visual/physical QA → technical delivery
```

`config/workflow.json` is the machine-readable routing catalog. `catalog.py` validates skill metadata
and local Markdown links. The CLI returns a route; it does not secretly start an agent or render.
The 12 skills remain the knowledge layer, not 12 compulsory pipeline stages.
Image-first Higgsfield work can select `image`, `prompt` and `generate` directly.
`previs` remains an explicit optional route; selecting generation does not imply Blender work.
The current tabletop compositing order is one-plate scene → per-plate background removal and
matte-boundary review → four-seat foreground placement → selected-background composite.
Repeated sources reuse a validated cutout; distinct source videos are removed independently.
User-supplied backgrounds are composited locally. Generative background editing is an explicitly
chosen option rather than a compulsory final stage. See the
[production loop](../skills/miniature-film-director/references/collaborative-production-loop.md).
`tools/ci.template.yml` is an inactive CI template. It is not an installed workflow: the publishing account's
current OAuth grant lacks the workflow permission. Local tests are the verified baseline.

`runtime.py` owns repository discovery, hashes and atomic JSON writes. `jobs.py` handles the small
Higgsfield CLI subset actually used by this workflow. `cli.py` exposes the actions without shell interpolation.
An existing `film_state.json` links to `.local/runs/<id>`; the latter stores only request/quote/attempt evidence.
No new production database or duplicate budget history is introduced.

## Cost boundary

Prepare is offline. Quote reads the current schema/cost with already-uploaded UUIDs. Approval records a real
user decision and the current account identity hash. Submit rechecks the request, local input hashes, quote,
account and available balance, then claims an exclusive effective-provider-request hash marker **before** the paid call.
Timeout, malformed output or ambiguous result leaves the attempt claimed. Status never creates or retries.
Two run names with the same provider arguments cannot bypass the guard by changing local bookkeeping.
Workspace-local input paths are stored relative to the checkout, so moving an intact workspace preserves
request hashes. External files remain explicitly absolute and must remain accessible.

This is not provider-side idempotency or a distributed lock. Another machine, a modified request, or manual
deletion can bypass it. Existing approvals elsewhere must be reconciled by the agent; the adapter is not a
global account budget manager. Approved cap and fresh quote are not a guarantee against provider billing bugs.
`actual_charged` stays unknown until a billing record verifies it.

## Reuse and performance

- Reuse unchanged references, actors, scene contracts and checks by version/hash.
- Don't regenerate motion for a codec fix, rebuild geometry for a prompt tweak, or re-download weights.
- Load the current stage plus needed acting/biomechanics/food references, not every research file.
- Keep generated media and caches off Git; clean only after identifying a usable successor and active consumers.
- New source code is relocatable. Legacy experiments are preserved separately and migrated only as documented.

## Quality boundary

File decoding, dimensions and duration establish technical validity only. Contact, face/gaze, foot planting,
silhouette, timing, framing and projection readability need actual candidate review. The shared skills record
pass/fail/unverified scope, not an unsupported universal "physics perfect" flag.
