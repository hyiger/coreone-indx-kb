# Contributing

This knowledge base exists because the previous community INDX resource went
dark. The goal is durability: plain markdown in git, no hosted service to lapse,
forkable by anyone if this one stalls too.

## Evidence tiers

Every page declares a `confidence` level in its front matter. This is the single
most important convention here, and it is what separates this from a forum
search.

| Level | Means | Requires |
|---|---|---|
| `measured` | Someone ran the test and recorded the result | Hardware, method, date, who |
| `reported` | Multiple independent users report the same thing | At least two linked sources |
| `provisional` | Single report, plausible, unverified | Source link, explicit caveat |

A page may not silently mix levels. If a page carries one `measured` value and
one `provisional` one, mark the provisional claim inline.

**Never publish a number without a tier.** An unsourced calibration value is
worse than no page — someone will act on it.

## What does not go in this repo

- **Verbatim forum posts.** Forum content is copyrighted by its author.
  Extract the finding, write it in your own words, link to the thread.
- **Discord content**, unless the server admins have agreed and participants
  are anonymised. Public forums and private support servers are different.
- **Raw crawl output.** That lives in a separate working repo, gitignored here.
- **Screenshots containing usernames or personal details.**

## Facts versus wording

Facts are not copyrightable. "The 0.6mm INDX profile needs X" is free to state.
The sentence someone wrote saying so is not. Rewrite, then cite.

## Superseded information

Firmware changes; Bondtech ships revisions. When a finding stops being true,
do not delete the page — add a `superseded_by` field to the front matter and a
banner at the top. People arrive from stale search results and need to know.

## Page template

Copy `docs/_template.md`. Fill in every front matter field. `unknown` is an
acceptable value; a missing field is not.

## Review

Calibration values are human-verified. No exceptions, regardless of how the
draft was produced.
