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

`foxtrot` was added in 1.1.0. It is the update marker: if a lookup for `foxtrot` comes back
"not in the table", this file is the stale 1.0.0 copy, even if the new skills loaded fine.

