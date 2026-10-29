#!/usr/bin/env python3
"""Generate a self-contained animated neofetch-style profile card."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "info-card.svg"
ROWS = [
    ("ROLE", "Aspiring Software Engineer"),
    ("FOCUS", "Backend · Systems · Developer Tools"),
    ("LANG", "C++ · Python · SQL · TypeScript"),
    ("BUILD", "Reliable services & measurable systems"),
    ("PROJECTS", "Matching Engine · RepoPilot · FluxQueue"),
    ("PRINCIPLE", "Evidence over guesses"),
]
def main() -> None:
    row_svg = []
    for i, (key, value) in enumerate(ROWS):
        y = 105 + i * 43
        row_svg.append(f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{0.35+i*0.16:.2f}s" dur=".45s" fill="freeze"/><animateTransform attributeName="transform" type="translate" from="0 7" to="0 0" begin="{0.35+i*0.16:.2f}s" dur=".45s" fill="freeze"/><text x="28" y="{y}" fill="#7ee787" font-family="ui-monospace,monospace" font-size="13">{key}</text><text x="132" y="{y}" fill="#e6edf3" font-family="ui-monospace,monospace" font-size="13">{value.replace('&','&amp;').replace('<','&lt;')}</text></g>')
    OUT.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="390" viewBox="0 0 640 390" role="img" aria-labelledby="title desc">
<title id="title">Adhi's neofetch-style developer profile</title><desc id="desc">Terminal information card describing engineering focus, tools, projects, and principles.</desc>
<rect width="640" height="390" rx="14" fill="#0d1117" stroke="#30363d"/><path d="M1 42H639" stroke="#30363d"/>
<circle cx="22" cy="21" r="5" fill="#ff7b72"/><circle cx="40" cy="21" r="5" fill="#d29922"/><circle cx="58" cy="21" r="5" fill="#3fb950"/>
<text x="82" y="26" fill="#8b949e" font-family="ui-monospace,monospace" font-size="12">adhi@github — neofetch</text>
<text x="28" y="72" fill="#e6edf3" font-family="ui-monospace,monospace" font-size="19" font-weight="700">ADHI NAIK</text>
<text x="28" y="88" fill="#8b949e" font-family="ui-monospace,monospace" font-size="11">──────────────────────────────────────────────</text>
{''.join(row_svg)}
<text x="28" y="365" fill="#8b949e" font-family="ui-monospace,monospace" font-size="11">BUILD · TEST · OBSERVE · IMPROVE</text>
</svg>\n''', encoding="utf-8")
    print(f"Rendered {OUT.relative_to(ROOT)}")
if __name__ == "__main__":
    main()
