---
name: plugin-changelog
description: Report what each version of the test-lab plugin added, read from its bundled changelog. Use when the user says "plugin changelog", "what changed in the plugin", "what did this version add", or asks which release introduced a skill.
---

# Plugin changelog

Added in **1.2.0**. Doubles as a probe: this skill *and* its bundled changelog are both new
in 1.2.0, so a session that can read the 1.2.0 entry has received a brand new bundled file,
not just a modified one.

1. Read `references/CHANGELOG.md`, next to this `SKILL.md`. Read it, do not summarise from
   memory.
2. Answer what the user asked: the whole history, one version, or which release introduced
   a given skill.
3. If the file has no 1.2.0 entry but this skill is running, say so. That means the
   `SKILL.md` synced and its bundled file did not, which is a partial sync.

Keep it short: the version, and what it added. No commentary.
