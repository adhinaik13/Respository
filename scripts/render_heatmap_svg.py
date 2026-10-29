#!/usr/bin/env python3
"""Render the public contribution data as a self-contained animated SVG."""
from __future__ import annotations
import json
from datetime import date
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "contributions.json"
OUT = ROOT / "contrib-heatmap.svg"
COLORS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

def esc(value: object) -> str:
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    days = payload["days"][-371:]
    if not days:
        raise RuntimeError("No contribution days available.")
    dates = [date.fromisoformat(day["date"]) for day in days]
    first = dates[0]
    # Align the first cell to Sunday; columns are calendar weeks.
    offset = (first.weekday() + 1) % 7
    total_cols = max(1, (len(days) + offset + 6) // 7)
    cell, gap, left, top = 11, 4, 28, 42
    width, height = left + total_cols * (cell + gap) + 12, 154
    rects = []
    for i, item in enumerate(days):
        col, row = (i + offset) // 7, (i + offset) % 7
        level = max(0, min(4, int(item.get("level", 0))))
        delay = col * 0.012 + row * 0.035
        title = f"{item['date']}: {item.get('count', 0)} contributions"
        rects.append(f'<g><title>{esc(title)}</title><rect x="{left+col*(cell+gap)}" y="{top+row*(cell+gap)}" width="{cell}" height="{cell}" rx="2" fill="{COLORS[level]}" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{delay:.3f}s" dur="0.32s" fill="freeze"/></rect></g>')
    total = int(payload.get("total", sum(x.get("count", 0) for x in days)))
    streak = int(payload.get("current_streak", 0))
    longest = int(payload.get("longest_streak", 0))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">GitHub contribution heatmap for {esc(payload.get("username", "vankudothuadhinaik"))}</title><desc id="desc">Animated contribution calendar with {total} contributions in the displayed year.</desc>
<rect width="100%" height="100%" rx="12" fill="#0d1117" stroke="#30363d"/>
<text x="22" y="25" fill="#e6edf3" font-family="ui-monospace, SFMono-Regular, Consolas, monospace" font-size="13" font-weight="600">adhi@github ~ $ ./contributions.sh</text>
{''.join(rects)}
<text x="24" y="{height-22}" fill="#8b949e" font-family="ui-monospace, monospace" font-size="10">{total:,} contributions · current streak {streak} days · longest streak {longest} days</text>
<text x="{width-125}" y="{height-22}" fill="#8b949e" font-family="ui-monospace, monospace" font-size="10">Less</text>
{''.join(f'<rect x="{width-93+i*14}" y="{height-31}" width="10" height="10" rx="2" fill="{c}"/>' for i,c in enumerate(COLORS))}
<text x="{width-20}" y="{height-22}" text-anchor="end" fill="#8b949e" font-family="ui-monospace, monospace" font-size="10">More</text>
</svg>'''
    OUT.write_text(svg + "\n", encoding="utf-8")
    print(f"Rendered {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
