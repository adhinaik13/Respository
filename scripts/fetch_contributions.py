#!/usr/bin/env python3
"""Fetch the public contribution calendar without a token."""
from __future__ import annotations
import json
from collections import Counter
from datetime import date, datetime
from pathlib import Path
import re
import requests
from bs4 import BeautifulSoup

USERNAME = "vankudothuadhinaik"
URL = f"https://github.com/users/{USERNAME}/contributions"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "contributions.json"

def main() -> None:
    response = requests.get(URL, timeout=30, headers={"User-Agent": "profile-art-generator/1.0"})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    days = []
    for cell in soup.select("td.ContributionCalendar-day"):
        day = cell.get("data-date")
        if not day:
            continue
        level = cell.get("data-level", "0")
        match = re.search(r"\d+", str(level))
        days.append({"date": day, "level": int(match.group()) if match else 0,
                     "count": int(cell.get("data-count", "0") or 0)})
    if not days:
        raise RuntimeError("GitHub returned no contribution day cells; refusing to overwrite valid data.")
    days.sort(key=lambda item: item["date"])
    active = [item for item in days if item["count"] > 0]
    best = max(days, key=lambda item: item["count"])
    streak = longest = current = 0
    previous = None
    for item in days:
        current_date = date.fromisoformat(item["date"])
        if item["count"] > 0:
            current = current + 1 if previous and (current_date - previous).days == 1 else 1
            longest = max(longest, current)
        else:
            current = 0
        previous = current_date
    # Count backwards from today (or yesterday if today's cell is not yet updated).
    day_map = {date.fromisoformat(item["date"]): item["count"] for item in days}
    cursor = date.today()
    if day_map.get(cursor, 0) == 0 and day_map.get(cursor.fromordinal(cursor.toordinal() - 1), 0) > 0:
        cursor = cursor.fromordinal(cursor.toordinal() - 1)
    current_streak = 0
    while day_map.get(cursor, 0) > 0:
        current_streak += 1
        cursor = cursor.fromordinal(cursor.toordinal() - 1)
    totals = Counter()
    for item in days:
        totals[item["date"][:7]] += item["count"]
    payload = {"username": USERNAME, "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
               "days": days, "total": sum(item["count"] for item in days),
               "current_streak": current_streak, "longest_streak": longest,
               "best_day": best["date"], "best_day_count": best["count"],
               "monthly_totals": dict(sorted(totals.items()))}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(days)} contribution days ({payload['total']} contributions) to {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
