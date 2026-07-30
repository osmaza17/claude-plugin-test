# LOG

Newest entry first.

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
