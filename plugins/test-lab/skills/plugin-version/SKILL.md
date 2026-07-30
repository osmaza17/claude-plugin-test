---
name: plugin-version
description: Report which version of the test-lab plugin is actually loaded, to check that a plugin update propagated. Use when the user says "plugin version", "which version of the plugin", "did the plugin update", "check the plugin updated", or asks whether a plugin upgrade reached this session.
---

# Plugin version

Probe 4 of 5. Added in **1.1.0**. Verifies that an update to an installed plugin reaches
the session, which is a different mechanism from a first install.

Two independent signals, report both:

1. **This skill exists at all.** It did not ship in 1.0.0. If it is running, the new
   version arrived.
2. **The manifest agrees.** Read `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json` and
   report its `version`. Read it, do not recall it from context.

Answer in three lines:

```
skill shipped in: 1.1.0
manifest version: <version from plugin.json>
verdict:          <see below>
```

Verdict rules:

- Both say 1.1.0 or higher and match → `ok, update propagated`.
- Manifest says 1.0.0 while this skill is running → `partial sync, new files arrived but the
  manifest is stale`. Say it plainly, this is the interesting failure.
- Manifest unreadable or `${CLAUDE_PLUGIN_ROOT}` unset → `cannot verify`, and say which one
  failed. Never fill the gap with a guess: an invented version makes a broken update look
  clean.
