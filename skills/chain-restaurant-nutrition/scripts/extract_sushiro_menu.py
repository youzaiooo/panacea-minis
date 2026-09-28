#!/usr/bin/env python3
"""Extract item->kcal pairs from a cached Sushiro Japan store-menu page.

Usage:
    python3 extract_sushiro_menu.py <path-to-cached-markdown>

The official page (https://www.akindo-sushiro.co.jp/menu/menu_detail/?s_id=<id>)
lists each item as: image, name, price (NNN円(税込)), kcal — name and kcal on
separate lines. web_extract caches sometimes embed literal backslash-n sequences
in addition to real newlines; both are normalized before matching.

If the price pattern differs (other chains / menu periods), tweak PRICE_RE and
ITEM_RE to match the page structure.
"""
import re
import sys

ITEM_RE = re.compile(
    r'!\[([^\]]*)\]\([^)]*\)\n\n'   # image markdown
    r'([^\n]+)\n\n'                  # item name
    r'(\d+円\(税込\))\n\n'           # price line
    r'(\d+kcal)'                     # calories
)


def load(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def main(path):
    text = load(path)
    # Normalize web_extract's escaped-newline artifacts to real newlines.
    text = text.replace('\\\n', '\n').replace('\\n', '\n')
    items = ITEM_RE.findall(text)
    seen = set()
    out = []
    for _alt, name, _price, kcal in items:
        if (name, kcal) in seen:
            continue
        seen.add((name, kcal))
        out.append((name, kcal))
    if not out:
        print('No item/kcal pairs matched — check the price regex against the cached page.',
              file=sys.stderr)
        sys.exit(1)
    for name, kcal in out:
        print(f'{name}\t{kcal}')
    print(f'--- {len(out)} unique items', file=sys.stderr)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1])
