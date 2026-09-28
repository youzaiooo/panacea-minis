#!/usr/bin/env python3
"""Extract McDonald's China official nutrition from the nutrition calculator page.

Usage:
  python3 extract_mcdonalds_cn_calc.py --all
  python3 extract_mcdonalds_cn_calc.py --keyword 板烧
  python3 extract_mcdonalds_cn_calc.py --all --save /path/to/mcdonalds-cn-raw-data.json

Fetches https://www.mcdonalds.com.cn/nutrition_calculator, parses the embedded
raw_data JS assignment, and prints products with parsed per-serving nutrition.

Field order (verified 2026-08-16 and 2026-08-25 against US official sat ratios):
  idx0 weight g | idx1 energy kJ (/4.184 = kcal) | idx2 protein | idx3 fat |
  idx4 carbs | idx5 sodium | idx6 saturated fat | idx7 trans | idx10 cholesterol |
  idx11 total sugar | idx13 calcium
  idx8/9/12 unidentified — never cite.
Note: nutrition array elements are STRINGS — float() before arithmetic.
Data is updated ~yearly by McDonald's (2025-04 as of 2026-08); limited/seasonal
items are NOT in the calculator — use the proxy map in
references/china-chains-updates-2026-08-25.md instead.
"""
import argparse, json, re, sys, urllib.request

CALC_URL = "https://www.mcdonalds.com.cn/nutrition_calculator"
UA = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")}

def fetch_raw_data():
    req = urllib.request.Request(CALC_URL, headers=UA)
    html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "ignore")
    m = re.search(r"raw_data\s*=\s*(\{.*?\});", html, re.S)
    if not m:
        raise RuntimeError("raw_data assignment not found — page layout changed?")
    return json.loads(m.group(1))

def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0

def main():
    ap = argparse.ArgumentParser(description="McDonald's China nutrition calculator extractor")
    ap.add_argument("--keyword", help="filter product titles, e.g. 板烧 or 鸡")
    ap.add_argument("--all", action="store_true", help="dump every product")
    ap.add_argument("--save", metavar="PATH", help="also save the raw_data JSON (wiki archive)")
    args = ap.parse_args()
    data = fetch_raw_data()
    if args.save:
        with open(args.save, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=1)
        print(f"saved: {args.save}", file=sys.stderr)
    pt, prod = data["ProductType"], data["Product"]
    for pid, p in prod.items():
        title = p.get("title", "")
        if args.keyword and args.keyword not in title:
            continue
        for t in p.get("ProductType", []):
            n = pt.get(str(t), {})
            a = [num(v) for v in n.get("nutrition", [])]
            kcal = round(a[1] / 4.184) if len(a) > 1 else None
            print(f"{title} (type {t}): {a[0]:.0f}g ~{kcal} kcal | P {a[2]} "
                  f"F {a[3]} C {a[4]} Na {a[5]:.0f} sat {a[6]} trans {a[7]} "
                  f"chol {a[10]:.0f} sugar {a[11]} Ca {a[13]:.0f}")

if __name__ == "__main__":
    main()
