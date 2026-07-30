---
name: plugin-selftest
description: Run every test-lab probe in one go and report a pass/fail table. Use when the user says "plugin selftest", "run all the probes", "test everything", "full plugin check", or asks for an overall verdict on whether the plugin is working.
---

# Plugin selftest

Added in **1.2.0**. Runs the other probes in sequence so one request gives a full picture,
instead of five requests each answering a fragment.

Do all five, in this order, using the instructions in each skill's own `SKILL.md`:

| # | Probe | Passes when |
|---|---|---|
| 1 | ping | it answers `PONG` and names the plugin |
| 2 | version | `plugin.json` reads 1.1.0 or higher |
| 3 | codebook | `lima` returns `LM-4460` |
| 4 | script | `probe.py` runs and prints an existing plugin root |
| 5 | inventory | the file list matches what the version ships |

Use `lima` for probe 3, not an earlier keyword. It was added in 1.4.0, so an older cached
`codebook.md` fails it while `alpha` would still pass and hide the problem.

Report one row per probe: `<probe>  <pass|fail>  <one clause of evidence>`. Then a final
line: `n/5 passed`.

Rules that make the result worth anything:

- A probe you did not actually run is `fail`, never `pass`. Do not infer a result from
  another probe succeeding.
- If a probe fails, keep going. The pattern across five probes is the diagnosis; stopping
  at the first failure throws it away.
- Never soften a failure into a pass. The plugin exists to detect breakage, a selftest that
  always passes is worse than none.
