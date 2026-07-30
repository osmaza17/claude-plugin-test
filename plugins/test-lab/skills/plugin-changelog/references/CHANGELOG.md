# test-lab changelog

Newest first.

## 1.4.0

No new skills, same as 1.3.0. A second consecutive version bump, to check that the update
path keeps working once it has worked once. Codebook gained `lima` (`LM-4460`) as the 1.4.0
stale-file marker, and a note that the sibling plugin's keywords must NOT resolve here.


## 1.3.0

No new skills. A version bump on purpose, to test whether Cowork offers an update button or
syncs on its own once the Claude GitHub App has access to the repository. Codebook gained
`hotel` (`HT-9948`) as the 1.3.0 stale-file marker.


## 1.2.0

Added `plugin-selftest` (runs all probes, one pass/fail table) and `plugin-changelog` (this
file's reader). Codebook gained the keyword `golf` (`GF-7126`) as the 1.2.0 stale-file
marker. A sibling plugin, `test-lab-2`, was added to the same marketplace in this release,
to test whether a new plugin shows up in a catalogue that was already added.

## 1.1.0

Added `plugin-version` and `plugin-inventory`, the two probes for update propagation.
Codebook gained `foxtrot` (`HL-2287`) as the 1.1.0 stale-file marker.

## 1.0.0

First release. `plugin-ping` (skill loading), `plugin-codebook` (bundled reference files),
`plugin-script` (bundled scripts and `${CLAUDE_PLUGIN_ROOT}`).
