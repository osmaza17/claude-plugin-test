# LOG

Newest entry first.

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
