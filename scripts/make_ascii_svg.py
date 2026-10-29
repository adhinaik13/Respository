#!/usr/bin/env python3
"""Generate an animated monochrome ASCII-style SVG.

For a personalized photographic portrait, install Pillow and pass a local image
as the first argument. Without one, a clean terminal monogram is generated.
"""
from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "avi-ascii.svg"
RAMP = " .`:-=+*cs#%@"

def main() -> None:
    rows: list[str] = []
    if len(sys.argv) > 1:
        try:
            from PIL import Image
            image = Image.open(sys.argv[1]).convert("L")
            image.thumbnail((72, 38))
            for y in range(image.height):
                line = "".join(RAMP[min(len(RAMP)-1, int(px) * (len(RAMP)-1) // 256)] for px in [image.getpixel((x,y)) for x in range(image.width)])
                rows.append(line.rstrip())
        except ImportError as exc:
            raise SystemExit("Install Pillow to convert a photo: python -m pip install pillow") from exc
    if not rows:
        rows = [
            "              .-=================-.",
            "           .-'   .:::::::::::.   '-.",
            "         .'     :::::::::::::::     '.",
            "        /       :::  ADHI  :::        \\",
            "       |        :::  NAIK  :::         |",
            "       |        :::::::::::::          |",
            "       |          .-------.             |",
            "       |         /  _____  \\            |",
            "       |        |  /     \\  |           |",
            "       |        | |  o o  | |           |",
            "       |        | |   ^   | |           |",
            "       |        | |  '-'  | |           |",
            "       |         \\  '---'  /            |",
            "        \\         '-------'            /",
            "         '.                           .'",
            "           '-._____________________.-'",
        ]
    width = max(map(len, rows))
    row_markup = []
    for index, line in enumerate(rows):
        y = 26 + index * 13
        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        row_markup.append(f'<g opacity="0"><text x="8" y="{y}" fill="#c9d1d9" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10" xml:space="preserve">{safe}</text><animate attributeName="opacity" from="0" to="1" begin="{index*0.11:.2f}s" dur=".15s" fill="freeze"/></g>')
    w = max(300, min(560, width * 6 + 20))
    h = len(rows) * 13 + 42
    OUT.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">Animated ASCII portrait of Adhi Naik</title><desc id="desc">A monochrome terminal portrait that reveals line by line.</desc>
<rect width="100%" height="100%" rx="12" fill="#0d1117" stroke="#30363d"/><text x="10" y="16" fill="#7ee787" font-family="ui-monospace,monospace" font-size="10">adhi@github ~ $ whoami</text>
{''.join(row_markup)}
</svg>\n''', encoding="utf-8")
    print(f"Rendered {OUT.relative_to(ROOT)}")
if __name__ == "__main__":
    main()
