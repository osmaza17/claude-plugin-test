# LOG

Newest entry first.

## 30 07 2026 — test-lab 1.2.0 and a second plugin, test-lab-2 1.0.0

Two things at once, because they answer two different questions. `test-lab` goes to 1.2.0
with `plugin-selftest` and `plugin-changelog`, so the update button has something to
offer an install already sitting at 1.1.0. And a second plugin, `test-lab-2`, joins the
same catalogue, to see whether a plugin added *after* a marketplace was added shows up at
all.

Context: 1.1.0 was installed in Cowork and its update button was greyed out, correctly, it
was already the newest version. This release is what makes that button live.

Decisions:

- `annex-codebook` ships its file at the same relative path as `plugin-codebook`
  (`references/codebook.md`) on purpose, with codes from a disjoint prefix set. Two plugins
  sharing a filename is exactly the case where a collision would be silent, so the probe
  is built to make it loud.
- Dropped the "Probe N of M" numbering from every skill. It was already wrong (`4 of 5`
  next to `3 of 3`) and every release would break it again. Each skill now names the
  mechanism it probes instead of its position.
- `plugin-version` now states a **floor**, not an exact version. It said "shipped in 1.1.0"
  and demanded a match, which would have reported a false partial sync the moment the
  plugin reached 1.2.0 without that file changing. A floor needs no maintenance.
- `plugin-selftest` is told to use the newest codebook keyword, `golf`. An older keyword
  passes on a stale file, so a selftest that used `alpha` would report green on exactly the
  failure it exists to catch.
- Bumped only `test-lab`. `test-lab-2` starts at 1.0.0 and its version moves independently,
  which is the point of two plugins in one catalogue.

Pending:

- Whether Cowork lists a plugin added to an already-added marketplace without re-adding the
  marketplace. That is the open question this release exists to answer.
- The expected-file list in `plugin-inventory` still needs a manual edit per release. It is
  now wrong-by-default rather than silently stale, since the count is stated, but it is
  still the first thing to break if someone adds a skill and forgets.


## 30 07 2026 — v1.1.0, two probes for update propagation

Added `plugin-version` and `plugin-inventory`, bumped to 1.1.0 in both manifests. Purpose:
1.0.0 only proved that a *first install* works. Updating an already-installed plugin is a
separate mechanism and was untested, which matters most in Cowork, where the session is
remote and the install is not the one on this machine.

Decisions:

- Three markers instead of one, because the ways an update half-lands are different and a
  single marker hides the others: new files arriving (`plugin-version` and
  `plugin-inventory` exist at all), the manifest advancing (`plugin.json` says 1.1.0), and
  an *existing* bundled file being replaced rather than left stale (`foxtrot` added to
  `codebook.md`). Only the third one catches a stale cached file.
- `plugin-version` hardcodes "shipped in 1.1.0" in its own text on purpose. `SKILL.md` and
  `plugin.json` come from the same commit, so if they disagree the sync is partial. Costs
  one line per release.
- `plugin-inventory` lists the expected files explicitly. Counting is what turns a partial
  sync from invisible into obvious.

Pending:

- Update path verified in local Claude Code only, still not in Cowork.
- The expected-file list in `plugin-inventory` is maintained by hand. If it ever drifts
  from what the plugin ships, the probe cries wolf. Fine at five skills, revisit if the
  plugin grows.


## 30 07 2026 — repo created, v1.0.0

Created the marketplace and the `test-lab` plugin with three probe skills.

Decisions:

- One probe per mechanism instead of three arbitrary toy skills. The earlier test repo
  (`claude-demo-plugin`) proved "a plugin installs"; it could not tell you *which* part
  broke. Here `plugin-ping` covers skill loading, `plugin-codebook` covers bundled
  reference files, `plugin-script` covers bundled script execution plus
  `${CLAUDE_PLUGIN_ROOT}`.
- `codebook.md` holds unguessable codes on purpose. If the answer contains a code that is
  not in the file, the file was not read, and the probe correctly reports a failure.
- The probe script ships a `--selftest` flag so the script can be cleared of blame before
  blaming the plugin plumbing.
- Names kept distinct from `claude-demo-plugin` at every level (marketplace, plugin,
  skills) so both can be installed simultaneously without shadowing.

Pending:

- Not yet checked in a Cowork cloud session, only in local Claude Code.
- No slash commands, hooks or agents in the plugin. Those are separate plugin mechanisms
  and are still untested; add a probe each if they ever matter.
