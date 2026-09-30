# Working rules

- This is the canonical **VFX Skills** source workspace. Read README and route only the current stage.
- Never hardcode a user's home path. Resolve from `__file__`, explicit configuration, or tool discovery.
  The repository name contains a space: subprocesses must use argument arrays; quote shell paths.
- `.local/legacy` contains private historical projects, not publishable source. Inspect narrowly when needed.
  Preserve original assets, receipts, hash evidence, credentials, and nested repositories.
- Existing `film_state.json` is the project record. Don't fork a second state framework or rewrite old evidence.
- Paid submission requires real current user authorization for this exact scope and account.
  `job approve` only records that authority; a local JSON record cannot create it.
  Never call paid tools merely to test code. Unit tests mock the provider.
- `doctor`, route selection and status checks do not authorize uploads, new jobs or retries.
  Unknown submission: inspect service history, never blindly retry or erase the attempt ledger.
- Request-bound one-attempt receipts are safety guards, not a security boundary against the local file owner.
- The user-selected backend and full deliverable take precedence over skill examples.
  Don't replace a requested finished Higgsfield video with endless Blender/plugin tests.
- For skill edits read skill-creator and the target SKILL.md fully, follow required references,
  and run metadata/link validation plus bounded forward tests.
- Before commit: run tests, skill validation, and `tools/check_publish.py` after staging.
  Stage explicit source directories; never force-add `.local`, raw media or secrets.
- Report what was actually verified. GPU discovery, job success and physical/acting quality are separate facts.
