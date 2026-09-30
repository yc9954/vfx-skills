# Guarded Higgsfield execution

The CLI adapter is based on installed `higgsfield 1.1.24` help, checked 2026-09-30.
It supports scalar prompt/mode/duration/resolution/aspect_ratio/generate_audio parameters and explicit media UUIDs.
Model availability, settings and pricing are live service facts: inspect `higgsfield model get MODEL --json`.
The example is a template, **not a guaranteed accepted model preset**.

1. Reuse an existing film record, approved references and real account session.
2. Copy `examples/generation-request.json` to `.local/requests/shot.json`; replace every placeholder.
   Media must be existing upload/job UUIDs. The adapter intentionally does not upload paths, even for quotes.
   If source verification is needed, add `local_inputs` entries with `path` and `sha256`; paths resolve relative
   to the request file when prepared. Files inside the checkout are stored as workspace-relative paths;
   external inputs remain absolute. Moving external files requires a new request/approval, not silently editing receipts.
   Input-role/identity mapping belongs in the brief and reference packet.
3. Prepare and quote:

   ```sh
   python3 vfx.py job prepare shot-01 .local/requests/shot.json
   python3 vfx.py job quote shot-01
   ```

4. Only after actual user approval for this exact job/account/cap:

   ```sh
   python3 vfx.py job approve shot-01 --cap 100 --source "Exact user message and context authorizing this one job"
   python3 vfx.py job submit shot-01 --execute
   python3 vfx.py job status shot-01
   ```

   The number 100 is an example, not an authorization. Don't copy it as a standing budget.
   `approve` is a bookkeeping action, not an authentication or permission service.

5. Download the actual provider output using a verified service response. Review it and run the existing
   `skills/film-render-delivery/scripts/media_receipt.py` for technical delivery. Consult its `--help` first.
   The adapter does not claim download, render, extension or visual review support it has not implemented.

If submission is uncertain, keep the attempt record, inspect `higgsfield generate list/get` and the service
history, and reconcile manually. Do not erase/rename receipts to unlock another charge. A failed job is not
proof of a refund. Any separately authorized retry needs its own explicit scope and reconciliation.

Existing project-specific `submit_once.py` files remain historical. Do not execute them to resume a new job;
their approvals/model settings may belong to old already-consumed work.
