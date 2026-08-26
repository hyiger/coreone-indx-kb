#!/usr/bin/env python3
"""Compare each translation against its English source, structurally.

i18n_check.py answers "has the English changed since this was translated".
This answers a different question: "is the translation faithful in the ways
that matter here". It compares the things a translator must NOT alter —
code, URLs, front-matter values, withheld-number markers — and the numbers
themselves, because the sharpest risk in this knowledge base is a
translation quietly resolving a value the English deliberately withheld.

  python tools/i18n_verify.py [--lang de]
"""
import argparse, re, sys
from pathlib import Path
from collections import Counter

DOCS = Path(__file__).resolve().parent.parent / "docs"
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FENCE = re.compile(r"```.*?```", re.S)
INLINE = re.compile(r"`[^`\n]*`")
LINK = re.compile(r"\]\(([^)\s]+)\)")
URL = re.compile(r"https?://[^\s)\]]+")
TODO = re.compile(r"TODO\(verify\)")
ADMON = re.compile(r"^!!!\s+(\w+)", re.M)
NUM = re.compile(r"\d+(?:[.,]\d+)*")
# Language-neutral: only the title is expected to differ.
TRANSLATABLE_KEYS = {"title"}


def split(p):
    t = p.read_text(encoding="utf-8")
    m = FM.match(t)
    return (m.group(1), t[m.end():]) if m else ("", t)


def fm_map(fm):
    out, key = {}, None
    for line in fm.split("\n"):
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            key = m.group(1); out[key] = m.group(2).strip()
        elif line.strip().startswith("-") and key:
            out.setdefault(key + "[]", []).append(line.strip())
    return out


def numbers(body):
    """Numbers outside code, URLs and the front matter. German may reformat a
    date's punctuation, so compare digit-runs rather than literal tokens."""
    b = FENCE.sub(" ", body); b = INLINE.sub(" ", b); b = URL.sub(" ", b)
    return Counter(n.replace(",", ".") for n in NUM.findall(b))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--lang", default="de")
    lang = ap.parse_args().lang
    problems = 0; checked = 0

    for src in sorted(p for p in DOCS.rglob("*.md")
                      if not re.search(r"\.[a-z]{2}\.md$", p.name) and p.name != "_template.md"):
        tr = src.with_suffix(f".{lang}.md")
        if not tr.exists():
            continue
        checked += 1
        rel = src.relative_to(DOCS)
        issues = []
        sfm, sb = split(src); tfm, tb = split(tr)

        if FENCE.findall(sb) != FENCE.findall(tb):
            issues.append(f"code fences differ ({len(FENCE.findall(sb))} en / {len(FENCE.findall(tb))} de)")
        if Counter(INLINE.findall(sb)) != Counter(INLINE.findall(tb)):
            d = Counter(INLINE.findall(sb)) - Counter(INLINE.findall(tb))
            a = Counter(INLINE.findall(tb)) - Counter(INLINE.findall(sb))
            issues.append(f"inline code differs: missing {list(d)[:4]} added {list(a)[:4]}")
        if Counter(LINK.findall(sb)) != Counter(LINK.findall(tb)):
            issues.append(f"link targets differ: {list((Counter(LINK.findall(sb)) - Counter(LINK.findall(tb))))[:4]}")
        if len(TODO.findall(sb)) != len(TODO.findall(tb)):
            issues.append(f"TODO(verify) count {len(TODO.findall(sb))} en vs {len(TODO.findall(tb))} de")
        if ADMON.findall(sb) != ADMON.findall(tb):
            issues.append(f"admonition types differ: {ADMON.findall(sb)} vs {ADMON.findall(tb)}")

        sm, tm = fm_map(sfm), fm_map(tfm)
        for k, v in sm.items():
            if k.rstrip("[]") in TRANSLATABLE_KEYS:
                continue
            if k not in tm:
                issues.append(f"front matter missing key: {k}")
            elif tm[k] != v:
                issues.append(f"front matter {k}: en={v!r} de={tm[k]!r}")

        sn, tn = numbers(sb), numbers(tb)
        if sn != tn:
            extra = tn - sn; gone = sn - tn
            if extra:
                issues.append(f"NUMBERS ADDED in translation: {dict(extra)}")
            if gone:
                issues.append(f"numbers dropped: {dict(gone)}")

        if issues:
            problems += 1
            print(f"\n  {rel}")
            for i in issues:
                print(f"     - {i}")

    print(f"\n  {checked} pair(s) checked, {problems} with structural differences")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
