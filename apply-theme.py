#!/usr/bin/env python3
"""Reads theme.txt and writes assets/css/theme.css (CSS variables).

Run from the repo root:  python apply-theme.py
Then rebuild the site:   jekyll build   (or jekyll serve)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "theme.txt")
DST = os.path.join(ROOT, "assets", "css", "theme.css")


def main():
    lines = []
    with open(SRC, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if ":" not in line:
                continue
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if not re.fullmatch(r"[a-z0-9-]+", key):
                sys.exit(f"bad key in theme.txt: {key!r}")
            lines.append(f"  --{key}: {value};")
    css = ":root {\n" + "\n".join(lines) + "\n}\n"
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(css)
    print(f"wrote {DST} ({len(lines)} settings)")


if __name__ == "__main__":
    main()
