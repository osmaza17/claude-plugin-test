---
name: plugin-script
description: Run the test-lab bundled probe script to check that a plugin can execute code it ships. Use when the user says "run the plugin script", "plugin script probe", "test CLAUDE_PLUGIN_ROOT", or asks to verify that a plugin's bundled scripts execute.
---

# Plugin script

Probe: bundled scripts. Verifies that a plugin can execute a script it ships, and that
`${CLAUDE_PLUGIN_ROOT}` resolves to the installed plugin directory.

Run:

```
python "${CLAUDE_PLUGIN_ROOT}/skills/plugin-script/scripts/probe.py" <text the user gave, or nothing>
```

On Windows use `python`; if that fails, retry once with `py -3`. If `${CLAUDE_PLUGIN_ROOT}`
is empty, the probe has already failed: say so and run the script by its absolute path
instead, so the two failures stay distinguishable.

Show the script's output verbatim, then one line saying whether the probe passed. Passed
means: the script ran, and the plugin root it printed is a real directory.

To check the script itself rather than the plumbing, run it with `--selftest`.
