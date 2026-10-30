"""Refresh the Stars column in README tables and re-sort rows by star count.

Usage: python3 .github/scripts/update_stars.py README.md
Set GITHUB_TOKEN to avoid the unauthenticated API rate limit.
"""

import json
import os
import re
import sys
import urllib.request

ROW = "| **["
REPO = re.compile(r"\(https://github\.com/([\w.-]+/[\w.-]+)\)")


def fetch_stars(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)["stargazers_count"]


def fmt(n):
    if n >= 100_000:
        return f"{round(n / 1000)}k"
    if n >= 1000:
        return f"{n / 1000:.1f}".rstrip("0").rstrip(".") + "k"
    return str(n)


def parse(cell):
    m = re.search(r"([\d.]+)(k?)", cell)
    if not m:
        return -1
    return int(float(m.group(1)) * (1000 if m.group(2) else 1))


def update_row(line):
    head, cell = line.rstrip()[:-1].rstrip().rsplit(" | ", 1)
    m = REPO.search(head)
    if not m:
        return line, parse(cell)
    try:
        stars = fetch_stars(m.group(1))
    except Exception as e:
        print(f"warning: {m.group(1)}: {e}", file=sys.stderr)
        return line, parse(cell)
    return f"{head} | ★ {fmt(stars)} |", stars


def main(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    out, block = [], []
    for line in lines + [""]:
        if line.startswith(ROW):
            block.append(update_row(line))
            continue
        if block:
            out.extend(row for row, _ in sorted(block, key=lambda r: -r[1]))
            block = []
        out.append(line)
    open(path, "w", encoding="utf-8").write("\n".join(out[:-1]))


if __name__ == "__main__":
    main(sys.argv[1])
