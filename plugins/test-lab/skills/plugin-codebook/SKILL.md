---
name: plugin-codebook
description: Look up a verification code from the test-lab codebook. Use when the user asks for a "verification code", a "codebook" lookup, "code for <word>", or wants to check that a plugin skill can read its own bundled reference files.
---

# Plugin codebook

Probe: bundled reference files. Verifies that a skill can read a file bundled next to it,
which is the mechanism every real skill uses for references, templates and checklists.

1. Read `references/codebook.md`, which sits next to this `SKILL.md`. Do not answer from
   memory: the whole point of the probe is that the file gets read at answer time.
2. Find the row whose keyword matches what the user asked for, case-insensitive.
3. Answer with one line: `<keyword> -> <code>`.
4. If the keyword is not in the table, say so and list the keywords that are. Never invent
   a code, a fabricated code makes the probe pass while the mechanism is broken.

If the file cannot be read at all, say that plainly. That is a failed probe, not a reason
to improvise an answer.
