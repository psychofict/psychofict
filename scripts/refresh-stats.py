#!/usr/bin/env python3
"""Refresh the Claude Code usage block in README.md from local telemetry.

Reads the claude-token-tracker SQLite store (~/.config/claude-token-tracker/history.db)
and rewrites everything between the CLAUDE-STATS markers. The block is REPLACED so the
README always converges to the current data — it is never skipped because a block
already exists.

Run from anywhere: python3 scripts/refresh-stats.py
"""

import datetime as dt
import pathlib
import re
import sqlite3
import sys

DB = pathlib.Path.home() / ".config" / "claude-token-tracker" / "history.db"
README = pathlib.Path(__file__).resolve().parent.parent / "README.md"
START = "<!-- CLAUDE-STATS:START -->"
END = "<!-- CLAUDE-STATS:END -->"


def pretty_model(model_id: str) -> str:
    """claude-opus-4-8 -> 'Opus 4.8'; claude-haiku-4-5-20251001 -> 'Haiku 4.5'."""
    parts = model_id.removeprefix("claude-").split("-")
    parts = [p for p in parts if not (len(p) == 8 and p.isdigit())]  # drop date stamps
    family = parts[0].capitalize()
    version = ".".join(p for p in parts[1:] if p.isdigit())
    return f"{family} {version}".strip()


def main() -> None:
    if not DB.exists():
        sys.exit(f"telemetry DB not found: {DB}")
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    processed, output, sessions, projects, since = con.execute(
        "SELECT SUM(input_tokens + cache_creation_5m + cache_creation_1h"
        "           + cache_read + output_tokens),"
        "       SUM(output_tokens), COUNT(DISTINCT session_id),"
        "       COUNT(DISTINCT project), MIN(timestamp) FROM messages"
    ).fetchone()
    if not processed:
        sys.exit("telemetry DB has no messages")
    (model,) = con.execute(
        "SELECT model FROM messages WHERE model IS NOT NULL"
        " AND model NOT LIKE '%synthetic%'"
        " GROUP BY model ORDER BY SUM(output_tokens) DESC LIMIT 1"
    ).fetchone()
    since_month = dt.datetime.fromisoformat(since).strftime("%b %Y")
    today = dt.date.today().isoformat()

    block = f"""{START}
| Tokens processed | Output generated | Sessions | Projects | Primary model | Since |
|---:|---:|---:|---:|:--|:--|
| **{processed / 1e9:.1f} B** | {output / 1e6:.0f} M | {sessions} | {projects} | {pretty_model(model)} | {since_month} |

<sub>Local Claude Code telemetry via claude-token-tracker (processed = input + cache
writes/reads + output) · snapshot {today} · regenerate with
<code>scripts/refresh-stats.py</code> — never edit these numbers by hand.</sub>
{END}"""

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
    print(
        f"updated: {processed / 1e9:.1f}B processed · {output / 1e6:.0f}M output · "
        f"{sessions} sessions · {projects} projects · {pretty_model(model)} · "
        f"since {since_month}"
    )


if __name__ == "__main__":
    main()
