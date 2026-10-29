#!/usr/bin/env python3
"""Validate the SVG assets wired into the GitHub profile README."""
from __future__ import annotations
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

class ImageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sources: list[str] = []
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "img":
            attrs_map = dict(attrs)
            src = attrs_map.get("src")
            if src:
                self.sources.append(src)

def main() -> None:
    parser = ImageParser()
    parser.feed(README.read_text(encoding="utf-8"))
    checked = 0
    for src in parser.sources:
        if src.startswith("./"):
            relative = src[2:].split("?", 1)[0]
            path = ROOT / relative
            if not path.is_file():
                raise SystemExit(f"README image is missing: {src}")
            if "?" not in src or "v=" not in src:
                raise SystemExit(f"README local image needs cache-busting version: {src}")
            if path.suffix.lower() == ".svg":
                root = ET.parse(path).getroot()
                if not root.tag.endswith("svg"):
                    raise SystemExit(f"Not an SVG root element: {path}")
                for element in root.iter():
                    if element.tag.endswith("script"):
                        raise SystemExit(f"JavaScript is not allowed in GitHub README SVGs: {path}")
                    for key, value in element.attrib.items():
                        if key.endswith("href") and value and not value.startswith("#") and not value.startswith("data:"):
                            raise SystemExit(f"External resource reference is not self-contained: {path}: {value}")
            checked += 1
    for required in ("hero.svg", "about-life.svg", "stack.svg", "id-dashboard.svg", "connect.svg", "contrib-heatmap.svg"):
        path = ROOT / required
        if not path.is_file():
            raise SystemExit(f"Required profile SVG missing: {required}")
        ET.parse(path)
    print(f"Validated {checked} local README images and all required profile SVGs.")
if __name__ == "__main__":
    main()
