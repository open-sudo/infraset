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


PALETTE = {
    "head_bg": "#b26a00",
    "head_fg": "#ffffff",
    "rule": "#dde1e7",
    "stripe": "#fafbfc",
    "ink": "#131820",
    "good": "#2f6f5e",
    "warn": "#a33a2a",
    "mid": "#b26a00",
}


def inline_html(fragment: str) -> str:
    """Flatten a fragment for use inside an HTML table cell.

    Markdown is not processed inside a raw HTML block, so links and code spans
    have to stay as HTML here rather than becoming [text](url) and backticks.
    """
    out = re.sub(r"<br\s*/?>", " ", fragment)
    out = re.sub(r"<(?!/?(?:a|code|em|strong|b|i)\b)[^>]+>", "", out)
    return re.sub(r"\s+", " ", out).strip()


def convert_table(block: str) -> str:
    """Render a table as styled HTML in the article's palette.

    Inline style attributes survive the publishing platform's sanitiser, so the
    colour the artifact carries through CSS classes can be carried through here
    too. Markdown tables would drop both the colour and the alignment.
    """
    rows = [
        re.findall(r"<t[hd]([^>]*)>(.*?)</t[hd]>", row, re.S)
        for row in re.findall(r"<tr>(.*?)</tr>", block, re.S)
    ]
    if not rows:
        return ""

    table_style = (
        "border-collapse:collapse;width:100%;"
        f"font-size:0.95em;border:1px solid {PALETTE['rule']}"
    )
    out = [f'<table style="{table_style}">']

    for index, row in enumerate(rows):
        if index == 0:
            out.append("<thead><tr>")
            for attrs, inner in row:
                align = "right" if "num" in attrs else "left"
                out.append(
                    f'<th style="background:{PALETTE["head_bg"]};'
                    f'color:{PALETTE["head_fg"]};text-align:{align};'
                    f'padding:9px 12px;font-weight:600">{inline_html(inner)}</th>'
                )
            out.append("</tr></thead><tbody>")
            continue

        stripe = f"background:{PALETTE['stripe']};" if index % 2 == 0 else ""
        out.append(f'<tr style="{stripe}">')
        for attrs, inner in row:
            align = "right" if "num" in attrs else "left"
            if "bad" in attrs:
                emphasis = f"color:{PALETTE['warn']};font-weight:700;"
            elif "good" in attrs:
                emphasis = f"color:{PALETTE['good']};font-weight:600;"
            else:
                emphasis = f"color:{PALETTE['ink']};"
            out.append(
                f'<td style="{emphasis}text-align:{align};padding:8px 12px;'
                f'border-top:1px solid {PALETTE["rule"]}">{inline_html(inner)}</td>'
            )
        out.append("</tr>")

    out.append("</tbody></table>")
    return "".join(out)


def convert_table_markdown(block: str) -> str:
    """Plain Markdown fallback, kept for renderers that strip HTML."""
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
            if value and mixed[column] and index > 0:
                if "bad" in attrs:
                    value = f"🔴 **{value}**"
                elif "good" in attrs:
                    value = f"🟢 {value}"
                else:
                    value = f"🟠 {value}"
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
        body = html.unescape(re.sub(r"<[^>]+>", "", pre.group(1))).strip()
        readout = as_readout(body)
        parts.append(readout if readout else "```\n" + body + "\n```")
    return "\n\n".join(parts)


def as_readout(body: str) -> str:
    """Render a label/value readout as a table rather than a code block.

    These panels are aligned statistics, not code. Left as fenced blocks they
    pick up the host's syntax-highlighting theme, which is wrong for figures.
    Anything that is genuinely a command stays fenced.
    """
    rows = []
    for line in body.splitlines():
        if not line.strip():
            continue
        match = re.match(r"^(\S.*?)\s{2,}(\S.*)$", line)
        if not match:
            return ""
        rows.append((match.group(1).strip(), re.sub(r"\s{2,}", " ", match.group(2)).strip()))
    if len(rows) < 2:
        return ""
    lines = ["| | |", "|---|---:|"]
    lines += [f"| {label} | {value} |" for label, value in rows]
    return "\n".join(lines)


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


def balanced_div(text: str, start: int) -> int:
    """Index just past the <div> opening at `start`, matching nesting properly.

    An evidence block may or may not nest a scroll wrapper, so a pattern that
    counts closing tags gets one of the two shapes wrong and silently swallows
    whatever follows.
    """
    depth = 0
    for match in re.finditer(r"<div\b[^>]*>|</div>", text[start:]):
        depth += 1 if match.group(0) != "</div>" else -1
        if depth == 0:
            return start + match.end()
    return len(text)


def extract_blocks(body: str) -> tuple[str, dict[str, str]]:
    """Replace evidence and risk blocks with placeholders, converted in place."""
    blocks: dict[str, str] = {}
    out = []
    cursor = 0
    for match in re.finditer(r'<div class="(ev|risk)">', body):
        if match.start() < cursor:
            continue
        end = balanced_div(body, match.start())
        raw = body[match.start():end]
        token = f"\x00block{len(blocks)}\x00"
        blocks[token] = (
            convert_evidence(raw) if match.group(1) == "ev" else convert_risk(raw)
        )
        out.append(body[cursor:match.start()])
        out.append(f"<p>{token}</p>")
        cursor = end
    out.append(body[cursor:])
    return "".join(out), blocks


def convert(source: Path, image_url: str) -> str:
    raw = source.read_text()
    body = raw[raw.index("<p class=\"eyebrow\">") :]
    body = body[: body.index("<footer>")]
    body, blocks = extract_blocks(body)

    out: list[str] = []
    position = 0
    pattern = re.compile(
        r'<h1>(?P<h1>.*?)</h1>'
        r'|<p class="standfirst">(?P<stand>.*?)</p>'
        r'|<h2 class="section">(?P<section>.*?)</h2>'
        r'|<div class="fnum">(?P<fnum>[^<]*)</div>'
        r'|<h3[^>]*>(?P<h3>.*?)</h3>'
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

    text = "\n\n".join(out) + "\n"
    for token, rendered in blocks.items():
        text = text.replace(token, rendered)
    return text


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
