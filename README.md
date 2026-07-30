# claude-plugin-test

A throwaway Claude Code **plugin marketplace** used to test plugin distribution end to end.
It is not meant to be useful: it is meant to fail loudly if any part of the plugin
mechanism is broken.

The repo ships one plugin, `test-lab`, with five probe skills. Each probe checks a
different mechanism, so a partial failure is still diagnosable.

| Skill | Probes | Passes when |
|---|---|---|
| `plugin-ping` | A bare `SKILL.md` inside a plugin is discovered and loaded | it answers `PONG` with the plugin and marketplace names |
| `plugin-codebook` | A skill can read a file bundled next to it (`references/`) | it returns a code that only exists in `codebook.md` |
| `plugin-script` | A skill can execute a script it ships, and `${CLAUDE_PLUGIN_ROOT}` resolves | the script runs and prints a real plugin root |
| `plugin-version` | An **update** to an already-installed plugin reaches the session | it runs at all, and `plugin.json` reports the same version |
| `plugin-inventory` | The update synced **every** file, not just the changed ones | the file list it finds matches the one it expects |

## Testing an update

Installing is one mechanism, updating an installed plugin is another. The 1.1.0 release
exists to test the second one. Three independent markers, so a partial update is visible
instead of silent:

- `plugin-version` and `plugin-inventory` did not exist in 1.0.0. If they trigger, new
  files arrived.
- `plugin.json` says `1.1.0`. If it still says `1.0.0` while the new skills run, the sync
  was partial.
- `codebook.md` gained the keyword `foxtrot` (`HL-2287`). If a lookup for `foxtrot` fails,
  an existing bundled file was left stale, which is the failure the two new skills alone
  cannot see.

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

To pull a new release into an existing install:

```
/plugin marketplace update osmaza-plugin-test-marketplace
/plugin update test-lab@osmaza-plugin-test-marketplace
```

Refreshing the marketplace is the step people skip: without it the client still sees the
old catalogue and reports that the plugin is up to date.

## Use

```
plugin ping
give me the verification code for bravo      -> bravo -> ZM-1180
run the plugin script probe
plugin version                               -> 1.1.0, twice
plugin inventory                             -> 8 files, complete
give me the verification code for foxtrot    -> foxtrot -> HL-2287   (1.1.0 only)
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
  skills/plugin-version/SKILL.md
  skills/plugin-inventory/SKILL.md
```

Skills never live inside `.claude-plugin/`; that folder holds manifests only.
