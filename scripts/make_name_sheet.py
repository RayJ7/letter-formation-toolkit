#!/usr/bin/env python3
"""Make a printable name-tracing sheet as SVG. No dependencies, no account.

Usage:
    python make_name_sheet.py Emma > emma.svg
    python make_name_sheet.py "Mary-Jane" --rows 3 --size kindergarten > mary.svg
"""
import argparse

SIZES = {"preschool": 15.0, "kindergarten": 12.0, "grade1": 9.5}   # capital ink height, mm
PITCH = {"preschool": 26.0, "kindergarten": 22.0, "grade1": 18.0}  # row pitch, mm
MM = 3.7795275591  # px per mm at 96 dpi (CSS)


def sheet(name, size="kindergarten", rows=3, paper="letter", style="dotted"):
    cap = SIZES[size] * MM
    pitch = PITCH[size] * MM
    page_w, page_h = (8.5 * 96, 11 * 96) if paper == "letter" else (8.27 * 96, 11.69 * 96)
    margin = 0.6 * 96
    top = margin + 40

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{page_w:.0f}" height="{page_h:.0f}" viewBox="0 0 {page_w:.0f} {page_h:.0f}">',
             f'<rect width="100%" height="100%" fill="#fff"/>']
    y = top + pitch
    for i in range(rows + 1):
        base_y = y + i * pitch
        parts.append(f'<line x1="{margin:.1f}" y1="{base_y - cap:.1f}" x2="{page_w - margin:.1f}" y2="{base_y - cap:.1f}" stroke="#c9d3e6" stroke-width="1"/>')
        parts.append(f'<line x1="{margin:.1f}" y1="{base_y - cap / 2:.1f}" x2="{page_w - margin:.1f}" y2="{base_y - cap / 2:.1f}" stroke="#c9d3e6" stroke-width="1" stroke-dasharray="4 4"/>')
        parts.append(f'<line x1="{margin:.1f}" y1="{base_y:.1f}" x2="{page_w - margin:.1f}" y2="{base_y:.1f}" stroke="#8d9bb5" stroke-width="1.2"/>')

    # 前 rows 行是描红，最后一行留空
    for i in range(rows):
        base_y = y + i * pitch
        fill = "#e9edf7" if style == "solid" else "none"
        stroke = "none" if style == "solid" else "#9aa8c4"
        dash = '' if style == "solid" else ' stroke-dasharray="2 2"'
        parts.append(
            f'<text x="{margin + 8:.1f}" y="{base_y:.1f}" font-family="Andika, Arial, sans-serif" '
            f'font-size="{cap * 1.35:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="0.8"{dash}>{name}</text>')
    parts.append('</svg>')
    return "\n".join(parts)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("name")
    ap.add_argument("--rows", type=int, default=3, choices=range(1, 6))
    ap.add_argument("--size", default="kindergarten", choices=list(SIZES))
    ap.add_argument("--paper", default="letter", choices=["letter", "a4"])
    ap.add_argument("--style", default="dotted", choices=["dotted", "solid"])
    a = ap.parse_args()
    print(sheet(a.name, a.size, a.rows, a.paper, a.style))
