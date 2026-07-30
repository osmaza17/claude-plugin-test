---
name: plugin-inventory
description: List every skill and bundled file the test-lab plugin actually shipped to this machine, to check an update synced completely. Use when the user says "plugin inventory", "list the plugin skills", "what did the plugin install", "check the plugin files synced", or asks which skills a plugin brought.
---

# Plugin inventory

Probe: sync completeness. Verifies that an update synced *every* file, not just the ones
that happened to change. A partial sync looks identical to a working one until you count.

1. List the contents of `${CLAUDE_PLUGIN_ROOT}` recursively. Ignore `.in_use`, it is
   runtime bookkeeping, not plugin content.
2. Report the skill folder names found under `skills/`, and the bundled non-`SKILL.md`
   files.
3. Compare against what 1.2.0 ships, 11 files:

```
.claude-plugin/plugin.json
skills/plugin-ping/SKILL.md
skills/plugin-codebook/SKILL.md
skills/plugin-codebook/references/codebook.md
skills/plugin-script/SKILL.md
skills/plugin-script/scripts/probe.py
skills/plugin-version/SKILL.md
skills/plugin-inventory/SKILL.md
skills/plugin-selftest/SKILL.md
skills/plugin-changelog/SKILL.md
skills/plugin-changelog/references/CHANGELOG.md
```

If the manifest reports a version below 1.2.0, compare against that version's list in
`plugin-changelog` instead of calling the missing files a failure.

Answer with the count found, then either `complete` or the list of missing files. Anything
present that is not on the list above is also worth naming: leftovers from an older version
mean the cache was added to rather than replaced.
