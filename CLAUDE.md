# CLAUDE.md

Internal guide for future Claude instances working on this repo.

## What this is

A Claude Code plugin marketplace whose only purpose is testing the plugin system. No
production use. If a change makes the probes *nicer* but less able to detect a broken
mechanism, it is a bad change.

There is a sibling repo, `osmaza17/claude-demo-plugin` (marketplace
`osmaza-demo-marketplace`, plugin `demo-toolkit`), from an earlier test. Both can be
installed at once: marketplace names, plugin names and skill names are all distinct, and
they must stay that way. Skill names are global once loaded, a collision silently shadows
one of them.

## Stack

Plain files. JSON manifests, Markdown skills, one Python 3 script (stdlib only). No build,
no dependencies, no package manager.

## Structure

```
.claude-plugin/marketplace.json    catalogue: marketplace name, owner, plugin list
plugins/test-lab/
  .claude-plugin/plugin.json       plugin manifest, this is where `version` lives
  skills/<name>/SKILL.md           one folder per skill
  skills/<name>/references/        files the skill reads at answer time
  skills/<name>/scripts/           scripts the skill executes
```

Hard rule from the docs: skills go in `plugins/<plugin>/skills/<name>/SKILL.md`, never
inside `.claude-plugin/`.

## Commands

```
claude plugin validate .                                  validate manifests
python plugins/test-lab/skills/plugin-script/scripts/probe.py --selftest
claude plugin marketplace add osmaza17/claude-plugin-test
claude plugin install test-lab@osmaza-plugin-test-marketplace
claude plugin marketplace update osmaza-plugin-test-marketplace
```

## Releasing a change

`version` is the propagation signal. A change with no version bump does not reach anyone
who already installed the plugin. So: bump `version` in **both** `plugin.json` and the
matching entry in `marketplace.json`, they must agree or `claude plugin tag` complains.

## Conventions

- Skill `name` in the frontmatter matches its folder name.
- `description` carries the trigger phrases, that is what routing matches on. Write the
  phrases a user would actually say.
- Every probe skill states explicitly what "passed" means and forbids guessing. A probe
  that lets the model improvise an answer reports success on a broken mechanism, which is
  worse than no probe.
- Repo docs are in English, matching the sibling repo, even though the owner works in
  Spanish.
