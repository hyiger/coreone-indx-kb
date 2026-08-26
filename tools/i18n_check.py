#!/usr/bin/env python3
"""Detect translations that have fallen behind their English source.

Every translated page records `source_sha`: the SHA-256 of the English page's
body at the moment it was translated. Recomputing that hash is the only
reliable way to catch an English edit that silently orphaned its translation —
nothing in mkdocs notices, and a stale page looks identical to a current one.

  python tools/i18n_check.py                    report, non-zero on drift
  python tools/i18n_check.py --require-complete  also fail on untranslated pages
  python tools/i18n_check.py --mark-stale        write the reader-facing banner
  python tools/i18n_check.py --stamp de          record current hashes (after translating)
"""
import argparse, hashlib, re, sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
SITE = "https://hyiger.github.io/coreone-indx-kb/"
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)

BANNER_ID = "<!-- i18n:stale -->"
BANNER = """{id}
!!! warning "Diese Übersetzung ist nicht auf dem aktuellen Stand"
    Die englische Originalseite wurde geändert, seit diese Übersetzung erstellt
    wurde. Bei Abweichungen ist die [englische Fassung]({url}) maßgeblich.
"""


def split(path):
    t = path.read_text(encoding="utf-8")
    m = FM.match(t)
    return (m.group(1), t[m.end():]) if m else ("", t)


def field(fm, key):
    m = re.search(rf"^{key}:\s*(.*?)\s*$", fm, re.M)
    return m.group(1).strip() if m else None


def strip_banner(body):
    """The banner is ours, not the translator's — never let it affect a hash
    or accumulate on repeated runs."""
    return re.sub(re.escape(BANNER_ID) + r".*?(?=\n#{1,6} |\n\n)", "", body, flags=re.S).lstrip("\n")


def body_hash(body):
    # Normalize line endings and trailing whitespace so a whitespace-only diff
    # does not spuriously invalidate a good translation.
    lines = [l.rstrip() for l in body.replace("\r\n", "\n").strip().split("\n")]
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def url_for(rel):
    p = rel.with_suffix("")
    p = p.parent if p.name == "index" else p
    return SITE + (str(p) + "/" if str(p) != "." else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="de")
    ap.add_argument("--require-complete", action="store_true")
    ap.add_argument("--mark-stale", action="store_true")
    ap.add_argument("--stamp", metavar="LANG")
    a = ap.parse_args()
    lang = a.stamp or a.lang

    sources = sorted(p for p in DOCS.rglob("*.md")
                     if not re.search(r"\.[a-z]{2}\.md$", p.name) and p.name != "_template.md")
    ok, stale, missing, orphan, tier = [], [], [], [], []

    for src in sources:
        rel = src.relative_to(DOCS)
        tr = src.with_suffix(f".{lang}.md")
        _, sbody = split(src)
        want = body_hash(sbody)
        if not tr.exists():
            missing.append(rel)
            continue
        tfm, tbody = split(tr)
        if a.stamp:
            new_fm = re.sub(r"^source_sha:.*$", f"source_sha:   {want}", tfm, flags=re.M) \
                if field(tfm, "source_sha") else tfm + f"\nsource_sha:   {want}"
            tr.write_text(f"---\n{new_fm}\n---\n{strip_banner(tbody)}", encoding="utf-8")
            ok.append(rel)
            continue
        sfm, _ = split(src)
        if field(sfm, "confidence") != field(tfm, "confidence"):
            tier.append((rel, field(sfm, "confidence"), field(tfm, "confidence")))
        (ok if field(tfm, "source_sha") == want else stale).append(rel)

    for tr in sorted(DOCS.rglob(f"*.{lang}.md")):
        if not Path(str(tr).replace(f".{lang}.md", ".md")).exists():
            orphan.append(tr.relative_to(DOCS))

    if a.mark_stale:
        for rel in stale:
            tr = DOCS / str(rel).replace(".md", f".{lang}.md")
            fm, body = split(tr)
            body = strip_banner(body)
            m = re.search(r"^# .*$", body, re.M)
            at = m.end() + 1 if m else 0
            banner = BANNER.format(id=BANNER_ID, url=url_for(rel))
            tr.write_text(f"---\n{fm}\n---\n{body[:at]}\n{banner}{body[at:]}", encoding="utf-8")
        if stale:
            print(f"  banner written to {len(stale)} stale page(s)")

    if a.stamp:
        print(f"  stamped {len(ok)} page(s) with current source hashes")
        return 0

    for label, items in (("STALE", stale), ("UNTRANSLATED", missing), ("ORPHAN", orphan)):
        if items:
            print(f"\n  {label} ({len(items)}):")
            for i in items:
                print(f"    {i}")
    if tier:
        print(f"\n  TIER MISMATCH ({len(tier)}):")
        for rel, e, d in tier:
            print(f"    {rel}: en={e} de={d}")
    print(f"\n  {len(ok)} in sync, {len(stale)} stale, {len(missing)} untranslated, "
          f"{len(orphan)} orphaned, {len(tier)} tier mismatch")

    fail = bool(stale or orphan or tier) or (a.require_complete and bool(missing))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
