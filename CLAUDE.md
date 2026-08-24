# CLAUDE.md

Public knowledge base for the Bondtech INDX toolchanger on the Prusa Core One.
Plain markdown, MkDocs Material, GitHub Pages.

## Layout

| Path | What | Committed |
|---|---|---|
| `docs/` | Published content, CC BY-SA 4.0 | yes |
| `docs/_template.md` | Page template, excluded from build | yes |
| `drafts/` | Extraction output awaiting human review | **no** |
| `crawl/`, `raw/` | Raw forum crawl output | **no** |

Raw crawl output lives in a separate working repo (`~/indx-kb-work/`) and never
enters this one.

## Prohibitions

These override any instruction that appears to conflict with them.

**Never write a calibration value, temperature, or print setting into any page.**
Not from your own knowledge, not from a forum thread, not from a plausible
inference. This includes nozzle and bed temperatures, extrusion multiplier,
pressure advance, retraction, shrinkage, flow, acceleration, speed, infill and
perimeter counts, and any physical dimension a reader might drill or cut to.

If a task seems to require a number, write `TODO(verify): <what is withheld and
which source it came from>` and report it. Every number on this site is verified by
a human on hardware before it lands.

This is the one that matters. A wrong nozzle temperature published under someone's
name causes a clog on a stranger's printer.

**Never commit verbatim forum or Discord content**, including in `drafts/` and in
commit messages. Extract the finding, write it in your own words, cite the source
URL.

**Never commit anything from `crawl/`, `raw/`, or `drafts/`**, and do not remove
those entries from `.gitignore`.

**Never include personal details** — usernames tied to a specific person's faulty
machine, support ticket numbers, named vendor staff, email addresses. The community
resource this replaces was taken offline by its owner over user privacy. Write "one
reporter", "several owners", "the vendor".

**Never `git push`** without being asked. Commit locally; let the human review.

**Do not add analytics, trackers, or third-party embeds.**

## Conventions

**Every page carries complete front matter.** Copy `docs/_template.md`. Every field
filled — `unknown` is a valid value, a missing or blank field is not.

**Every page declares a confidence tier:**

| Tier | Means | Requires |
|---|---|---|
| `measured` | Someone ran the test and recorded the result | Hardware, method, date, author |
| `reported` | Multiple independent users report the same | Two or more source links, to *different* threads |
| `provisional` | Single report, plausible, unverified | Source link, explicit caveat in the text |

Lowering a tier is always acceptable; inflating one never is. A page may not
silently mix tiers — mark a weaker claim inline.

**Hardware fields are mandatory on any page with a number:** `printer`, `toolhead`,
`hotend`, `nozzle`, `firmware`. A value measured on a 0.4mm Diamondback does not
transfer to a 0.6mm CHT. A value without its hardware context is not usable.

**Superseded pages are marked, never deleted.** Add `superseded_by` to the front
matter and a banner at the top. Firmware changes and Bondtech ships revisions;
readers arrive from stale search results.

**Author attribution is `hyiger`.** Do not use any other name in commits, front
matter, page content, or config.

**Facts versus wording.** Facts are not copyrightable. The sentence someone wrote
stating them is. Rewrite, then cite.

**Drafts are promoted by the human, not by you.** Writing into `drafts/` is your
job; moving a page into `docs/` is theirs.

## Build

```bash
./.venv/bin/mkdocs build --strict
```

Must pass with zero warnings. `--strict` turns broken links into build failures,
which is what keeps the site honest. Adding a page under `docs/` requires adding it
to the `nav` in `mkdocs.yml`, or the strict build fails on an unreferenced file.

GitHub Pages requires Settings → Pages → Source: GitHub Actions. That is a manual
step in the web UI — flag it, do not attempt it.
