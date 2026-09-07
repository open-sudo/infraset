#!/usr/bin/env python3
"""Convert the published findings artifact into Markdown.

The article is authored as a self-contained HTML page so it can be read as an
artifact. Publishing platforms want Markdown, so this walks that page and emits
an equivalent document: evidence blocks become tables or fenced code, risk boxes
become blockquotes, caveats become italic notes.

Usage:  article_to_markdown.py <article.html> <output.md> [image-url]
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path


def text_of(fragment: str) -> str:
    """Flatten inline markup, keeping links, code spans and emphasis."""
    out = fragment
    out = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', r"[\2](\1)", out, flags=re.S)
    out = re.sub(r"<code>(.*?)</code>", r"`\1`", out, flags=re.S)
    out = re.sub(r"<(em|i)>(.*?)</\1>", r"*\2*", out, flags=re.S)
    out = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", out, flags=re.S)
    out = re.sub(r"<br\s*/?>", "\n", out)
    out = re.sub(r"<[^>]+>", "", out)
    out = html.unescape(out)
    return re.sub(r"[ \t]+", " ", out).strip()


def convert_table(block: str) -> str:
    """Render a table, carrying the page's good/bad emphasis into the text.

    Markdown has no styling, and Hashnode strips inline CSS, so the colour the
    artifact applies through classes is re-expressed with a marker and bold.
    """
    rows = [
        re.findall(r"<t[hd]([^>]*)>(.*?)</t[hd]>", row, re.S)
        for row in re.findall(r"<tr>(.*?)</tr>", block, re.S)
    ]
    if not rows:
        return ""

    # A marker only earns its place where a column mixes good and bad. Flagging
    # every row of an all-failure table adds noise and no information.
    width = max(len(row) for row in rows)
    mixed = []
    for column in range(width):
        classes = {
            "bad" if "bad" in attrs else "good" if "good" in attrs else ""
            for row in rows
            for attrs, _ in [row[column]]
            if column < len(row)
        }
        mixed.append({"good", "bad"} <= classes)

    lines = []
    for index, row in enumerate(rows):
        cells = []
        for column, (attrs, inner) in enumerate(row):
            value = text_of(inner)
            if value and mixed[column]:
                if "bad" in attrs:
                    value = f"🔴 **{value}**"
                elif "good" in attrs:
                    value = f"🟢 {value}"
            elif value and "bad" in attrs:
                value = f"**{value}**"
            cells.append(value)
        lines.append("| " + " | ".join(cells) + " |")
        if index == 0:
            lines.append(
                "|" + "|".join("---:" if "num" in a else "---" for a, _ in row) + "|"
            )
    return "\n".join(lines)


def convert_evidence(block: str) -> str:
    label = re.search(r'<p class="ev-label">(.*?)</p>', block, re.S)
    parts = []
    if label:
        parts.append(f"**{text_of(label.group(1))}**")
    if "<table>" in block:
        parts.append(convert_table(block))
    pre = re.search(r"<pre>(.*?)</pre>", block, re.S)
    if pre:
        body = re.sub(r"<[^>]+>", "", pre.group(1))
        parts.append("```\n" + html.unescape(body).strip() + "\n```")
    return "\n\n".join(parts)


def convert_risk(block: str) -> str:
    label = re.search(r'<p class="risk-label">(.*?)</p>', block, re.S)
    paragraphs = re.findall(r"<p(?! class=\"risk-label\")[^>]*>(.*?)</p>", block, re.S)
    lines = []
    if label:
        lines.append(f"> **{text_of(label.group(1))}**")
        lines.append(">")
    for index, paragraph in enumerate(paragraphs):
        if index:
            lines.append(">")
        lines.append("> " + text_of(paragraph).replace("\n", "\n> "))
    return "\n".join(lines)


def convert(source: Path, image_url: str) -> str:
    raw = source.read_text()
    body = raw[raw.index("<p class=\"eyebrow\">") :]
    body = body[: body.index("<footer>")]

    out: list[str] = []
    position = 0
    pattern = re.compile(
        r'<h1>(?P<h1>.*?)</h1>'
        r'|<p class="standfirst">(?P<stand>.*?)</p>'
        r'|<h2 class="section">(?P<section>.*?)</h2>'
        r'|<div class="fnum">(?P<fnum>[^<]*)</div>'
        r'|<h3[^>]*>(?P<h3>.*?)</h3>'
        r'|<div class="ev">(?P<ev>.*?)</div>\s*</div>'
        r'|<div class="risk">(?P<risk>.*?)</div>'
        r'|<figure class="lab">(?P<fig>.*?)</figure>'
        r'|<div class="close">\s*<h2>(?P<close>.*?)</h2>'
        r'|<p class="caveat">(?P<caveat>.*?)</p>'
        r'|<dt>(?P<dt>.*?)</dt>\s*<dd>(?P<dd>.*?)</dd>'
        r'|<p(?P<attrs>[^>]*)>(?P<p>.*?)</p>',
        re.S,
    )
    pending_number = ""
    scale: list[str] = []

    for match in pattern.finditer(body):
        if match.start() < position:
            continue
        position = match.end()
        group = match.groupdict()

        if group["h1"]:
            out.append(f"# {text_of(group['h1'])}")
        elif group["stand"]:
            out.append(text_of(group["stand"]))
        elif group["dt"] is not None:
            scale.append(f"**{text_of(group['dt'])}** {text_of(group['dd'])}")
        elif group["section"]:
            if scale:
                out.append(" · ".join(scale))
                scale = []
            out.append(f"## {text_of(group['section'])}")
        elif group["fnum"] is not None:
            pending_number = text_of(group["fnum"])
        elif group["h3"]:
            heading = text_of(group["h3"])
            prefix = f"{pending_number}. " if pending_number.isdigit() else ""
            out.append(f"### {prefix}{heading}")
            pending_number = ""
        elif group["ev"]:
            out.append(convert_evidence(match.group(0)))
        elif group["risk"]:
            out.append(convert_risk(match.group(0)))
        elif group["fig"]:
            caption = re.search(r"<figcaption>(.*?)</figcaption>", group["fig"], re.S)
            alt = re.search(r'alt="([^"]*)"', group["fig"])
            out.append(f"![{alt.group(1) if alt else 'The lab'}]({image_url})")
            if caption:
                out.append(f"*{text_of(caption.group(1))}*")
        elif group["close"]:
            out.append(f"## {text_of(group['close'])}")
        elif group["caveat"]:
            out.append(f"*{text_of(group['caveat'])}*")
        elif group["p"] is not None:
            if "eyebrow" in (group["attrs"] or ""):
                continue
            rendered = text_of(group["p"])
            if rendered:
                out.append(rendered)

    return "\n\n".join(out) + "\n"


def main() -> int:
    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    image_url = sys.argv[3] if len(sys.argv) > 3 else "images/lab.jpg"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(convert(source, image_url))
    words = len(destination.read_text().split())
    print(f"wrote {destination} ({words} words)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
