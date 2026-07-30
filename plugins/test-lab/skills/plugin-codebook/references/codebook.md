# Codebook

Arbitrary lookup table. Its only job is to hold values that cannot be guessed, so an
answer containing the right code proves this file was actually read.

| Keyword | Code |
|---|---|
| alpha | QX-7734 |
| bravo | ZM-1180 |
| charlie | KD-9052 |
| delta | RT-4419 |
| echo | VN-6603 |
| foxtrot | HL-2287 |
| golf | GF-7126 |
| hotel | HT-9948 |

Each release adds one keyword, and it is the stale-file marker for that release: `foxtrot`
in 1.1.0, `golf` in 1.2.0, `hotel` in 1.3.0. If a lookup for the newest keyword comes back "not in the
table", this file is a stale copy from an earlier version, even if the new skills loaded
fine. Always test with the newest keyword; an old one passes on a stale file and hides it.

