#!/usr/bin/env python3
"""USDA FoodData Central lookup for Panacea meal records.

Usage:
    python3 usda_fdc_lookup.py search --query "french bread" [--pagesize 6]
    python3 usda_fdc_lookup.py detail --fdcid 172675

Prints per-100g key nutrients (energy, protein, carbs, total fat,
saturated fat, fiber, sodium). Saves raw JSON responses to the health
Wiki under raw/sources/usda/ (WIKI_PATH env var, default /var/minis/memory/panacea-wiki).
"""
import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request

API = "https://api.nal.usda.gov/fdc/v1"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}
WIKI = os.environ.get("WIKI_PATH", os.path.expanduser("/var/minis/memory/panacea-wiki"))

NUTRIENTS = {
    1008: "Energy kcal",
    1003: "Protein g",
    1005: "Carbs g",
    1004: "Total fat g",
    1258: "Sat fat g",
    1079: "Fiber g",
    1093: "Sodium mg",
}


def fetch(url, retries=3):
    """Fetch JSON with retry/backoff; USDA API intermittently fails with
    SSL connect errors (curl exit 35) on the first attempt."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            if attempt == retries - 1:
                sys.exit(f"USDA API error after {retries} attempts: {e}")
            time.sleep(2 * (attempt + 1))


def save(data, name):
    out = os.path.join(WIKI, "raw", "sources", "usda", name)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        json.dump(data, f, indent=2)
    print(f"saved: {out}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("--query", required=True)
    s.add_argument("--pagesize", type=int, default=6)
    d = sub.add_parser("detail")
    d.add_argument("--fdcid", required=True)
    a = ap.parse_args()

    if a.cmd == "search":
        q = urllib.parse.quote(a.query)
        url = f"{API}/foods/search?query={q}&dataType=SR%20Legacy&pageSize={a.pagesize}&api_key=DEMO_KEY"
        data = fetch(url)
        safe = a.query.replace(" ", "-").replace("/", "_")
        save(data, f"usda-search-{safe}.json")
        for f in data.get("foods", []):
            print(f["fdcId"], "|", f["description"])
    else:
        url = f"{API}/food/{a.fdcid}?api_key=DEMO_KEY"
        data = fetch(url)
        save(data, f"usda-fdc-{a.fdcid}-detail.json")
        print("description:", data["description"])
        for n in data["foodNutrients"]:
            nid = n["nutrient"]["id"]
            if nid in NUTRIENTS:
                print(f"{NUTRIENTS[nid]} = {n.get('amount')} {n['nutrient'].get('unitName', '')}")


if __name__ == "__main__":
    main()
