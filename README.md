# claude-plugin-test

A throwaway Claude Code **plugin marketplace** used to test plugin distribution end to end.
It is not meant to be useful: it is meant to fail loudly if any part of the plugin
mechanism is broken.

The repo ships one plugin, `test-lab`, with three probe skills. Each probe checks a
different mechanism, so a partial failure is still diagnosable.

| Skill | Probes | Passes when |
|---|---|---|
| `plugin-ping` | A bare `SKILL.md` inside a plugin is discovered and loaded | it answers `PONG` with the plugin and marketplace names |
| `plugin-codebook` | A skill can read a file bundled next to it (`references/`) | it returns a code that only exists in `codebook.md` |
| `plugin-script` | A skill can execute a script it ships, and `${CLAUDE_PLUGIN_ROOT}` resolves | the script runs and prints a real plugin root |

## Install

```
/plugin marketplace add osmaza17/claude-plugin-test
/plugin install test-lab@osmaza-plugin-test-marketplace
```

Or from the terminal, outside a Claude Code session:

```
claude plugin marketplace add osmaza17/claude-plugin-test
claude plugin install test-lab@osmaza-plugin-test-marketplace
```

Restart the session afterwards. Skills load at startup.

## Use

```
plugin ping
give me the verification code for bravo      -> bravo -> ZM-1180
run the plugin script probe
```

If `plugin-codebook` answers a code that is not in `references/codebook.md`, the probe did
**not** pass: the model answered from context instead of reading the bundled file.

## Uninstall

```
/plugin uninstall test-lab@osmaza-plugin-test-marketplace
/plugin marketplace remove osmaza-plugin-test-marketplace
```

## Layout

```
.claude-plugin/marketplace.json        the catalogue
plugins/test-lab/
  .claude-plugin/plugin.json           the plugin manifest (version lives here)
  skills/plugin-ping/SKILL.md
  skills/plugin-codebook/SKILL.md
  skills/plugin-codebook/references/codebook.md
  skills/plugin-script/SKILL.md
  skills/plugin-script/scripts/probe.py
```

Skills never live inside `.claude-plugin/`; that folder holds manifests only.
