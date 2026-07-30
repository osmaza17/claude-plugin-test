---
name: plugin-ping
description: Confirm that the test-lab plugin is installed and loading. Use when the user says "plugin ping", "ping the plugin", "is the test plugin loaded", "check the plugin works", or asks to verify a Claude Code plugin installation.
---

# Plugin ping

Probe: skill loading. This skill has no bundled files, so it verifies only one thing: that a
`SKILL.md` shipped inside a plugin gets discovered and loaded.

Answer with exactly these four lines, filled in:

```
PONG
plugin:      test-lab
marketplace: osmaza-plugin-test-marketplace
skill file:  <absolute path of this SKILL.md>
```

Get the path from wherever this skill was loaded from. If you cannot determine it, write
`unknown` and say so in one extra line, do not guess a path.

Then stop. No summary, no offer of next steps.
