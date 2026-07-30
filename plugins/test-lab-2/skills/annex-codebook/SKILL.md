---
name: annex-codebook
description: Look up a verification code from the test-lab-2 annex codebook. Use when the user asks for an "annex code", a code from the "second codebook", or wants to check that two plugins' bundled files do not collide.
---

# Annex codebook

Belongs to **test-lab-2**. Deliberately near-identical to `plugin-codebook` in the sibling
plugin: same shape, same filename (`references/codebook.md`), different codes. That is the
point. If the two plugins' bundled files collide, this skill answers with test-lab's codes
instead of its own, and the collision becomes visible.

1. Read `references/codebook.md`, the one next to *this* `SKILL.md`. Do not answer from
   memory or from the other plugin's table.
2. Answer with one line: `<keyword> -> <code>`.
3. If the keyword is not in this table, say so and list the keywords that are.

The codes here all start with a letter pair the sibling never uses. If you ever return
`QX-`, `ZM-`, `KD-`, `RT-`, `VN-`, `HL-` or `GF-` from this skill, you read the wrong file:
say so instead of answering.
