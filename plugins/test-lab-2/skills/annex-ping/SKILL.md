---
name: annex-ping
description: Confirm that the test-lab-2 plugin is installed and that it loads separately from test-lab. Use when the user says "annex ping", "ping the second plugin", "is test-lab-2 loaded", or asks whether two plugins from the same marketplace both work.
---

# Annex ping

Belongs to **test-lab-2**, not test-lab. Verifies two things at once: that a plugin added to
an already-added marketplace gets discovered, and that two plugins from the same catalogue
load side by side with separate roots.

Answer with exactly these four lines, filled in:

```
PONG-2
plugin:      test-lab-2
plugin root: ${CLAUDE_PLUGIN_ROOT}
sibling:     <see below>
```

For `sibling`: the two plugins install into different directories. Check whether the root
above ends in `test-lab-2` and not `test-lab`. If a probe from this plugin reports the
*other* plugin's root, say `WRONG ROOT` and show both paths, that is a real collision and
worth knowing. Otherwise say `separate root, ok`.
