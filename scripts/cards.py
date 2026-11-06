#!/usr/bin/env python3
"""Draw the profile's SVG cards (light and dark) into assets/.

The cards follow IBM's Carbon system: flat square tiles, IBM Plex Sans, one blue accent.
IBM Plex Sans (SIL Open Font License, scripts/fonts/OFL.txt) is embedded in each SVG,
because an SVG shown as an image cannot load a web font.

  python3 scripts/cards.py          # redraws the "at a glance" card
  python3 scripts/refresh-stats.py  # redraws the Claude Code card (imports this module)

The README shows each card at 640px through <picture>, with a dark source for GitHub's dark
theme. GitHub wraps README images in links, so only the theme switch works; a source keyed
on screen width would be ignored. The type is sized to stay legible when a phone shrinks a
card to about 360px.
"""

import base64
import pathlib
from html import escape

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONTS = pathlib.Path(__file__).resolve().parent / "fonts"

# Carbon White and Gray 100 themes.
THEMES = {
    "light": dict(tile="#f4f4f4", ink="#161616", muted="#525252", subtle="#6f6f6f",
                  rule="#e0e0e0", accent="#0f62fe"),
    "dark": dict(tile="#161616", ink="#f4f4f4", muted="#c6c6c6", subtle="#a8a8a8",
                 rule="#393939", accent="#78a9ff"),
}
CLAUDE = "#d97757"
FAMILY = "'Plex', 'IBM Plex Sans', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"


def _font_css() -> str:
    faces = []
    for weight, name in ((300, "Light"), (400, "Regular"), (600, "SemiBold")):
        data = base64.b64encode((FONTS / f"IBMPlexSans-{name}.woff2").read_bytes()).decode()
        faces.append(
            f"@font-face{{font-family:'Plex';font-weight:{weight};"
            f"src:url(data:font/woff2;base64,{data}) format('woff2');}}"
        )
    return "".join(faces)


def _svg(width: int, height: int, theme: str, title: str, body: str) -> str:
    t = THEMES[theme]
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">'
        f"<title>{escape(title)}</title>"
        f"<style>{_font_css()}text{{font-family:{FAMILY};}}"
        f".num{{font-weight:300;fill:{t['accent']};}}"
        f".val{{font-weight:400;fill:{t['ink']};}}"
        f".lbl{{font-weight:400;fill:{t['muted']};}}"
        f".eye{{font-weight:600;fill:{t['subtle']};letter-spacing:1.4px;}}"
        f"</style>"
        f'<rect width="{width}" height="{height}" fill="{t["tile"]}"/>'
        f"{body}</svg>"
    )


def _text(x, y, cls, size, s, anchor="start") -> str:
    return (f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" '
            f'text-anchor="{anchor}">{escape(s)}</text>')


def _cells(items, x0, y0, cell_w, cell_h, cols, theme, num_size, lbl_size, cls="num"):
    """A grid of figure-over-label cells split by hairlines; items are (figure, [label lines])."""
    t = THEMES[theme]
    out = []
    for i, (fig, label) in enumerate(items):
        col, row = i % cols, i // cols
        x, y = x0 + col * cell_w, y0 + row * cell_h
        if col:
            out.append(f'<rect x="{x}" y="{y + 16}" width="1" height="{cell_h - 32}" fill="{t["rule"]}"/>')
        if row:
            out.append(f'<rect x="{x + 16}" y="{y}" width="{cell_w - 32}" height="1" fill="{t["rule"]}"/>')
        out.append(_text(x + 20, y + 20 + num_size, cls, num_size, fig))
        for j, line in enumerate(label):
            out.append(_text(x + 20, y + 26 + num_size + (j + 1) * (lbl_size + 4), "lbl", lbl_size, line))
    return "".join(out)


def write(name: str, svgs: dict) -> None:
    ASSETS.mkdir(exist_ok=True)
    for variant, svg in svgs.items():
        (ASSETS / f"{name}-{variant}.svg").write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------- at a glance

GLANCE = [  # the same four figures as the portfolio's stat bar
    ("4", ["first-author", "papers"]),
    ("2", ["peer-reviewed", "papers"]),
    ("1", ["Korean patent", "filed"]),
    ("2019", ["shipping", "since"]),
]
GLANCE_TITLE = ("At a glance: 4 first-author papers, 2 of them peer-reviewed, "
                "1 Korean patent application filed, shipping software since 2019")


def glance_cards() -> dict:
    return {theme: _svg(640, 156, theme, GLANCE_TITLE,
                        _cells(GLANCE, 0, 0, 160, 156, 4, theme, 52, 18))
            for theme in THEMES}


# ---------------------------------------------------------------- Claude Code usage

def usage_cards(processed: str, stats: list, since: str, snapshot: str) -> dict:
    """processed: e.g. "325.6B"; stats: four (value, label) pairs; since/snapshot: "May 2026"."""
    title = (f"Claude Code usage from local telemetry, {since} to {snapshot}: {processed} tokens "
             "processed, " + ", ".join(f"{label} {value}" for value, label in stats))
    svgs = {}
    for theme in THEMES:
        t = THEMES[theme]
        body = (f'<rect x="24" y="27" width="10" height="10" fill="{CLAUDE}"/>'
                + _text(44, 37, "eye", 13, "CLAUDE CODE")
                + _text(616, 37, "eye", 13, f"{since.upper()} – {snapshot.upper()}", "end")
                + _text(21, 120, "num", 76, processed)
                + _text(24, 150, "lbl", 18, "tokens processed")
                + f'<rect x="24" y="174" width="592" height="1" fill="{t["rule"]}"/>'
                + _cells([(v, [label]) for v, label in stats], 0, 176, 160, 100, 4, theme, 26, 16, "val"))
        svgs[theme] = _svg(640, 276, theme, title, body)
    return svgs


if __name__ == "__main__":
    write("glance", glance_cards())
    print("drew assets/glance-*.svg")
