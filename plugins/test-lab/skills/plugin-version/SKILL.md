---
name: plugin-version
description: Report which version of the test-lab plugin is actually loaded, to check that a plugin update propagated. Use when the user says "plugin version", "which version of the plugin", "did the plugin update", "check the plugin updated", or asks whether a plugin upgrade reached this session.
---

# Plugin version

Probe: update propagation. Verifies that an update to an already-installed plugin reaches
the session, which is a different mechanism from a first install.

Two independent signals, report both:

1. **This skill exists at all.** It first shipped in 1.1.0, so if it is running, the
   installed version is at least 1.1.0.
2. **The manifest agrees.** Read `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json` and
   report its `version`. Read it, do not recall it from context.

Answer in three lines:

```
floor (this skill): 1.1.0
manifest version:   <version from plugin.json>
verdict:            <see below>
```

Verdict rules, comparing the manifest against the 1.1.0 floor:

- Manifest is 1.1.0 or higher → `ok, update propagated`. Higher is normal and expected:
  this skill does not change every release, so it states a floor, not the current version.
- Manifest is below 1.1.0 while this skill is running → `partial sync, new files arrived
  but the manifest is stale`. Say it plainly, this is the interesting failure.
- Manifest unreadable or `${CLAUDE_PLUGIN_ROOT}` unset → `cannot verify`, and say which one
  failed. Never fill the gap with a guess: an invented version makes a broken update look
  clean.
