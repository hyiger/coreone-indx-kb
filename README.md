# Core One INDX Knowledge Base

Community reference for the Bondtech INDX toolchanger on the Prusa Core One.

Plain markdown in git, built with MkDocs Material, published to GitHub Pages. There
is no database and no hosted service to lapse — if this copy stalls, anyone can fork
it and carry on. That is the point: this exists because the previous community INDX
resource went offline.

**Live site: <https://hyiger.github.io/coreone-indx-kb/>**

## Who it's for

Someone whose INDX is misbehaving right now, and who needs to tell their fault apart
from the three others that look like it. Pages lead with the mechanism, not the fix,
because several INDX faults present almost identically and have unrelated causes.

## Evidence tiers

Every page declares a `confidence` level in its front matter. This is the convention
that separates the site from a forum search.

| Tier | Means | Requires |
|---|---|---|
| `measured` | Someone ran the test and recorded the result | Hardware, method, date, author |
| `reported` | Multiple independent users report the same | Two or more source links |
| `provisional` | Single report, plausible, unverified | Source link and an explicit caveat |

**Every calibration value on this site is verified by a human on hardware before it
is published.** Where a page shows a `TODO(verify)` marker in place of a number, that
number is deliberately withheld until someone has checked it. A wrong nozzle
temperature published under someone's name causes a clog on a stranger's printer.

Pages also state the hardware they apply to — printer, toolhead, hotend, nozzle,
firmware — because a value measured on one nozzle does not transfer to another.

## Running it locally

```bash
python3 -m venv .venv
```

```bash
./.venv/bin/pip install -r requirements.txt
```

```bash
./.venv/bin/mkdocs serve
```

Then open the address it prints. To reproduce what CI does:

```bash
./.venv/bin/mkdocs build --strict
```

`--strict` turns broken links into build failures. It is not optional here — it is
what keeps the site honest as pages get superseded and moved.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md), which points at the published guide in
[`docs/contributing.md`](docs/contributing.md).

The most valuable contribution is one that moves a page from `provisional` to
`measured` by running the test and documenting the hardware it ran on.

Corrections to a page that has gone stale are the second most valuable. Superseded
pages are marked with `superseded_by` and kept, never deleted — people arrive from
stale search results and need to know they have.

## Licenses

Two licenses, because code and prose have different reuse needs and contributors need
to know which applies to what.

| What | License | File |
|---|---|---|
| Build config, workflows, scripts | MIT | [LICENSE](LICENSE) |
| Everything under `docs/` | CC BY-SA 4.0 | [LICENSE-CONTENT](LICENSE-CONTENT) |

Cited forum threads and other external sources remain the copyright of their
authors and are not covered by either license. Findings here are rewritten and
sourced, never reproduced verbatim.

## Repository layout

```
docs/          published content (CC BY-SA 4.0)
  _template.md page template, excluded from the build
drafts/        extraction output awaiting human review — gitignored
mkdocs.yml     site config and navigation
.github/       Pages deploy workflow
```

`drafts/`, `crawl/` and `raw/` are gitignored. Raw forum crawl output lives in a
separate working repository and never enters this one.
