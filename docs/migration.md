# Folder and path migration

## Physical layout

The working folder is now named `VFX Skills`. The original Kimodo directory was moved intact into
`.local/legacy/` instead of merging 44 GB of media, models and experiments into the source repository.
An old-name compatibility link points at that legacy directory so open processes, embedded Blender paths,
virtual environments and historical evidence can still resolve their original paths.

**New work uses the real new repository, not the old-name link.** The installed 11 skills link to `skills/`
in this repository. New Python entry points derive paths from their own location or `VFX_SKILLS_ROOT`.
Installation and CI are tested with spaces in checkout paths and from another working directory.

## What may be rewritten

Active legacy Python source path literals and shell entry-point paths can be migrated with a backup and
syntax checks. Historical JSON receipts, approval hashes, logs, Notion exports, generated files, binaries,
FBX/Blender embedded paths and nested Git histories are not bulk-edited. Old evidence remains old evidence.
The local migration receipt identifies changed files and old/new hashes, and is not committed.

`tools/migrate_legacy_paths.py` is an explicit local maintenance command. It does not walk model caches,
third-party dependencies or archived skill copies. Dry run first; `--apply` makes backed-up source edits.
This makes local legacy scripts point at the actual new data location; it does **not** make every old
experiment portable to a different computer. The reusable new layer is the portable part.

## Cleanup and restoration

Only specifically verified regenerable caches/intermediate sequences are candidates for cleanup.
Original video/model/scene/motion files, weights, credentials and previous working versions are retained.
Recoverable cleanup moves selected targets to a dedicated macOS Trash directory and records their exact
original paths in a local receipt. Moving to Trash does not free disk space until the user empties it.
There is no broad recursive deletion command or automatic Trash emptying.

Skill installation backs up the previous directories under `.local/skill-backups/<timestamp>/` before linking.
To restore, use its receipt, remove only a verified matching symlink, and move that exact backup back;
never overwrite an unrelated newly edited skill.

## New clone

Clone the private source repo, use Python 3.10+, run `doctor`, then install the registered skills.
Provide your own authorized media/tool installations and current logins. `.local` and old-name links are
machine-local migration conveniences, not part of the Git clone. An app task opened in the legacy location
does not automatically change its working folder: open the new `VFX Skills` directory for future tasks.
