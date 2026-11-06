#!/usr/bin/env python3
"""Refresh the Claude Code usage card in README.md from local telemetry.

Reads the claude-token-tracker SQLite store (~/.config/claude-token-tracker/history.db),
redraws assets/claude-usage-*.svg (scripts/cards.py) and rewrites everything between the
CLAUDE-STATS markers. The block is REPLACED so the README always converges to the
current data — it is never skipped because a block already exists.

Run from anywhere: python3 scripts/refresh-stats.py
"""

import datetime as dt
import pathlib
import re
import sqlite3
import sys
from html import escape, unescape

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cards  # noqa: E402

DB = pathlib.Path.home() / ".config" / "claude-token-tracker" / "history.db"
README = pathlib.Path(__file__).resolve().parent.parent / "README.md"
RAW = "https://raw.githubusercontent.com/psychofict/psychofict/main/assets"
START = "<!-- CLAUDE-STATS:START -->"
END = "<!-- CLAUDE-STATS:END -->"
# The claude-mem plugin's background sessions summarise other sessions; they are not
# coding sessions, and counting them inflated Sessions by about half (Nov 2026).
EXCLUDED = "project != 'observer-sessions'"


def pretty_model(model_id: str) -> str:
    """claude-opus-4-8 -> 'Opus 4.8'; claude-haiku-4-5-20251001 -> 'Haiku 4.5'."""
    parts = model_id.removeprefix("claude-").split("-")
    parts = [p for p in parts if not (len(p) == 8 and p.isdigit())]  # drop date stamps
    family = parts[0].capitalize()
    version = ".".join(p for p in parts[1:] if p.isdigit())
    return f"{family} {version}".strip()


def tokens(n: float) -> str:
    """325_563_790_314 -> '325.6B'; 47_000_000 -> '47M'."""
    return f"{n / 1e9:.1f}B" if n >= 1e9 else f"{n / 1e6:.0f}M"


def picture(name: str, version: str, alt: str) -> str:
    """The <picture> block for a card drawn by scripts/cards.py."""
    src = lambda variant: f"{RAW}/{name}-{variant}.svg?v={version}"  # noqa: E731
    return f"""<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{src('dark')}" />
    <img width="640" src="{src('light')}" alt="{escape(alt)}" />
  </picture>
</p>"""


def main() -> None:
    if not DB.exists():
        sys.exit(f"telemetry DB not found: {DB}")
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    processed, output, sessions, days, since = con.execute(
        "SELECT SUM(input_tokens + cache_creation_5m + cache_creation_1h"
        "           + cache_read + output_tokens),"
        "       SUM(output_tokens), COUNT(DISTINCT session_id),"
        "       COUNT(DISTINCT substr(timestamp, 1, 10)), MIN(timestamp) FROM messages"
        f" WHERE {EXCLUDED}"
    ).fetchone()
    if not processed:
        sys.exit("telemetry DB has no messages")
    (model,) = con.execute(
        "SELECT model FROM messages WHERE model IS NOT NULL"
        f" AND model NOT LIKE '%synthetic%' AND {EXCLUDED}"
        " GROUP BY model ORDER BY SUM(output_tokens) DESC LIMIT 1"
    ).fetchone()

    today = dt.date.today()
    snap = today.strftime("%b %Y")
    since_txt = dt.datetime.fromisoformat(since).strftime("%b %Y")
    stats = [
        (tokens(output), "output tokens"),
        (f"{sessions:,}", "sessions"),
        # Active days, not "projects": every worktree and scratch folder counts as a project.
        (f"{days:,}", "active days"),
        (pretty_model(model), "primary model"),
    ]
    svgs = cards.usage_cards(tokens(processed), stats, since_txt, snap)
    cards.write("claude-usage", svgs)
    alt = unescape(re.search(r"<title>(.*?)</title>", svgs["light"]).group(1))

    block = f"{START}\n{picture('claude-usage', today.strftime('%Y%m%d'), alt)}\n{END}"
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit("CLAUDE-STATS markers not found in README.md")
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        lambda _: block,
        text,
        count=1,
        flags=re.S,
    )
    README.write_text(new, encoding="utf-8")
    print(f"updated: {tokens(processed)} processed · "
          + " · ".join(f"{v} {label}" for v, label in stats) + f" ({since_txt} to {snap})")


if __name__ == "__main__":
    main()
