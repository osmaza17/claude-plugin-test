# claude-plugin-test

A throwaway Claude Code **plugin marketplace** used to test plugin distribution end to end.
It is not meant to be useful: it is meant to fail loudly if any part of the plugin
mechanism is broken.

The repo ships two plugins from one catalogue. Each skill probes a different mechanism, so
a partial failure is still diagnosable.

### `test-lab` (1.4.0)

| Skill | Probes | Passes when |
|---|---|---|
| `plugin-ping` | A bare `SKILL.md` inside a plugin is discovered and loaded | it answers `PONG` with the plugin and marketplace names |
| `plugin-codebook` | A skill can read a file bundled next to it (`references/`) | it returns a code that only exists in `codebook.md` |
| `plugin-script` | A skill can execute a script it ships, and `${CLAUDE_PLUGIN_ROOT}` resolves | the script runs and prints a real plugin root |
| `plugin-version` | An **update** to an already-installed plugin reaches the session | it runs at all, and `plugin.json` reads 1.1.0 or higher |
| `plugin-inventory` | The update synced **every** file, not just the changed ones | the file list it finds matches the one it expects |
| `plugin-selftest` | Nothing new. Runs all of the above and reports one table | every probe it reports was actually run |
| `plugin-changelog` | A brand new bundled file arrives on update | it can read the newest entry of `CHANGELOG.md` |

### `test-lab-2` (1.0.0)

| Skill | Probes | Passes when |
|---|---|---|
| `annex-ping` | A plugin added later shows up in an **already-added** marketplace | it answers `PONG-2` from its own plugin root |
| `annex-codebook` | Two plugins' bundled files do not collide | it returns its own codes, never the sibling's |

`annex-codebook` ships a file at the same relative path as `plugin-codebook`
(`references/codebook.md`) on purpose. If the two ever resolve to the same file, this probe
is the one that notices.

## Testing an update

Installing is one mechanism, updating an installed plugin is another, and a new plugin
appearing in a catalogue you already added is a third. Each release adds markers so a
partial update is visible instead of silent:

- **New skills.** `plugin-selftest` and `plugin-changelog` did not exist in 1.1.0. If they
  trigger, new files arrived.
- **The manifest.** `plugin.json` says `1.2.0`. If it lags while the new skills run, the
  sync was partial.
- **A modified existing file.** `codebook.md` gained `golf` (`GF-7126`). This is the only
  marker that catches a bundled file left stale, and it is why you should always look up
  the newest keyword: an older one passes on a stale file and hides the problem.
- **A brand new bundled file.** `CHANGELOG.md` ships for the first time in 1.2.0, which is
  a different case from modifying a file that already existed.

Keyword per release: `foxtrot` in 1.1.0, `golf` in 1.2.0, `hotel` in 1.3.0, `lima` in
1.4.0.

A release does not need new skills. Neither 1.3.0 nor 1.4.0 ships any: the version bump
alone is the signal a client uses to decide there is something to fetch.

## Install

```
/plugin marketplace add osmaza17/claude-plugin-test
/plugin install test-lab@osmaza-plugin-test-marketplace
/plugin install test-lab-2@osmaza-plugin-test-marketplace
```

Or from the terminal, outside a Claude Code session:

```
claude plugin marketplace add osmaza17/claude-plugin-test
claude plugin install test-lab@osmaza-plugin-test-marketplace
```

Restart the session afterwards, or run `/reload-plugins`. Skills load at startup.

To pull a new release into an existing install:

```
/plugin marketplace update osmaza-plugin-test-marketplace
/plugin update test-lab@osmaza-plugin-test-marketplace
```

Refreshing the marketplace is the step people skip: without it the client still sees the
old catalogue and reports that the plugin is up to date.

## Use

```
plugin selftest                              -> the whole table at once
plugin ping
plugin version                               -> floor 1.1.0, manifest 1.4.0
plugin inventory                             -> 11 files, complete
give me the verification code for lima       -> lima -> LM-4460      (1.4.0 only)
plugin changelog                             -> what each version added
annex ping                                   -> PONG-2, separate root
give me the annex code for juliet            -> juliet -> BC-8809
```

If a codebook skill answers a code that is not in its own `references/codebook.md`, the
probe did **not** pass: the model answered from context instead of reading the bundled
file.

## Uninstall

```
/plugin uninstall test-lab@osmaza-plugin-test-marketplace
/plugin uninstall test-lab-2@osmaza-plugin-test-marketplace
/plugin marketplace remove osmaza-plugin-test-marketplace
```

Removing the marketplace uninstalls both plugins.

## Layout

```
.claude-plugin/marketplace.json        the catalogue, lists both plugins
plugins/test-lab/
  .claude-plugin/plugin.json           the plugin manifest (version lives here)
  skills/plugin-ping/SKILL.md
  skills/plugin-codebook/SKILL.md
  skills/plugin-codebook/references/codebook.md
  skills/plugin-script/SKILL.md
  skills/plugin-script/scripts/probe.py
  skills/plugin-version/SKILL.md
  skills/plugin-inventory/SKILL.md
  skills/plugin-selftest/SKILL.md
  skills/plugin-changelog/SKILL.md
  skills/plugin-changelog/references/CHANGELOG.md
plugins/test-lab-2/
  .claude-plugin/plugin.json           its own version, bumped independently
  skills/annex-ping/SKILL.md
  skills/annex-codebook/SKILL.md
  skills/annex-codebook/references/codebook.md
```

Skills never live inside `.claude-plugin/`; that folder holds manifests only.
