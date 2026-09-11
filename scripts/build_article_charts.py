#!/usr/bin/env python3
"""Render the article's two most visual tables as charts.

Hashnode strips inline CSS, so a published table cannot carry the emphasis the
artifact gives it. A chart carries more than colour would and survives any
renderer. Figures are drawn in the article's own palette so the published piece
and the artifact stay recognisably the same work.

Usage:  build_article_charts.py <output-dir>
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

from findings.command_fail_rates import rates as command_fail_rates

PAPER = "#f5f6f8"
INK = "#131820"
MUTED = "#5c6672"
RULE = "#dde1e7"
ACCENT = "#b26a00"
WARN = "#a33a2a"
OK = "#2f6f5e"

SANS = next(
    (
        name
        for name in ("DejaVu Sans", "Liberation Sans", "Arial")
        if any(f.name == name for f in font_manager.fontManager.ttflist)
    ),
    "sans-serif",
)

# clustered-services: every task installs software, so the polling loop has
# plenty of chances to fire. Ordered as the article orders it, fastest first.
CLUSTERED = [
    ("CentOS Stream 10", 4.8, 0.9),
    ("RHEL 10.0", 4.8, 0.7),
    ("RHEL 9.8", 5.5, 0.5),
    ("AlmaLinux 9", 6.4, 1.1),
    ("Alpine", 9.9, 2.7),
    ("RHEL 7.9", 12.0, 2.5),
    ("Ubuntu 24.04", 17.2, 7.0),
    ("Ubuntu 16.04", 21.4, 8.6),
]


def style(ax) -> None:
    ax.set_facecolor(PAPER)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(RULE)
    ax.tick_params(colors=MUTED, labelsize=9, length=0)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontname(SANS)


def chart_sleep(destination: Path) -> None:
    names = [row[0] for row in CLUSTERED][::-1]
    total = [row[1] for row in CLUSTERED][::-1]
    sleep = [row[2] for row in CLUSTERED][::-1]
    working = [t - s for t, s in zip(total, sleep)]

    fig, ax = plt.subplots(figsize=(9, 4.6), dpi=170)
    fig.patch.set_facecolor(PAPER)
    ax.barh(names, working, color=ACCENT, height=0.62, label="Working")
    ax.barh(names, sleep, left=working, color=WARN, height=0.62, label="Asleep")

    for index, (t, s) in enumerate(zip(total, sleep)):
        ax.text(t + 0.35, index, f"{t:.1f} min", va="center", ha="left",
                color=INK, fontsize=9, fontname=SANS, fontweight="bold")
        if s >= 2.0:
            ax.text(working[index] + s / 2, index, f"{s:.1f}", va="center",
                    ha="center", color="white", fontsize=8.5, fontname=SANS)

    style(ax)
    ax.set_xlim(0, max(total) * 1.16)
    ax.set_xlabel("Median run time, minutes", color=MUTED, fontsize=9, fontname=SANS)
    ax.set_title("Time spent working versus time spent asleep, clustered-services",
                 color=INK, fontsize=11.5, fontname=SANS, fontweight="bold",
                 loc="left", pad=14)
    legend = ax.legend(frameon=False, loc="upper right", fontsize=9)
    for text in legend.get_texts():
        text.set_color(MUTED)
        text.set_fontname(SANS)
    fig.tight_layout()
    fig.savefig(destination, facecolor=PAPER)
    plt.close(fig)


def chart_components(destination: Path) -> None:
    linux_rates, network_rates = command_fail_rates()
    linux = [(label, rate) for label, _, _, _, rate in linux_rates]
    network = [(label, rate) for label, _, _, _, rate in network_rates]
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(11, 4.1),
        dpi=170,
        sharey=True,
        gridspec_kw={"width_ratios": [1.25, 1]},
    )
    fig.patch.set_facecolor(PAPER)

    groups = [
        (axes[0], "Linux releases", linux),
        (axes[1], "Network operating systems", network),
    ]
    maximum = max([row[1] for row in linux] + [row[1] for row in network])

    for ax, subtitle, values in groups:
        names = [row[0] for row in values]
        rates = [row[1] for row in values]
        colors = [WARN if rate >= 10 else OK if rate < 5 else ACCENT for rate in rates]
        bars = ax.bar(names, rates, color=colors, width=0.58)
        for bar, rate in zip(bars, rates):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                rate + 0.28,
                f"{rate:.1f}%",
                ha="center",
                color=INK,
                fontsize=9.5,
                fontname=SANS,
                fontweight="bold",
            )
        style(ax)
        ax.set_ylim(0, maximum * 1.25)
        ax.set_yticks([])
        ax.set_ylabel("")
        ax.set_title(
            subtitle,
            color=MUTED,
            fontsize=10,
            fontname=SANS,
            fontweight="bold",
            loc="left",
            pad=10,
        )

    fig.suptitle(
        "Command fail rate by operating-system component",
        color=INK,
        fontsize=12,
        fontname=SANS,
        fontweight="bold",
        x=0.055,
        ha="left",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    fig.savefig(destination, facecolor=PAPER)
    plt.close(fig)


def main() -> int:
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "docs/images")
    out.mkdir(parents=True, exist_ok=True)
    chart_sleep(out / "clustered-sleep.png")
    chart_components(out / "fail-rate-by-component.png")
    for name in ("clustered-sleep.png", "fail-rate-by-component.png"):
        size = (out / name).stat().st_size / 1024
        print(f"  {name:28} {size:6.0f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
