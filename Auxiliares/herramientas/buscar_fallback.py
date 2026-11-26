#!/usr/bin/env python3
"""Buscador de respaldo con ddgs (Yahoo/Mojeek/Startpage/Brave) para cuando DDG bloquea."""
import argparse, json, random, sys, time
from ddgs import DDGS


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--pages", type=int, default=12)
    ap.add_argument("--backend", default="yahoo")
    ap.add_argument("--out", required=True)
    ap.add_argument("--delay", type=float, default=3.0)
    ap.add_argument("--page-size", type=int, default=10)
    a = ap.parse_args()
    rows = []
    for page in range(1, a.pages + 1):
        try:
            with DDGS(timeout=30) as d:
                raw = d.text(a.query, region="wt-wt", max_results=a.page_size, page=page, backend=a.backend)
        except Exception as e:
            print(f"P{page:02d} ERROR {e}", file=sys.stderr, flush=True)
            break
        items = [
            {
                "page": page,
                "position": i,
                "title": x.get("title", ""),
                "url": x.get("href", "") or x.get("url", ""),
                "snippet": x.get("body", "") or x.get("snippet", ""),
            }
            for i, x in enumerate(raw, 1)
        ]
        rows.extend(items)
        print(f"P{page:02d} {len(items)} resultados (total {len(rows)})", flush=True)
        if not items:
            break
        time.sleep(a.delay + random.random())
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    print(f"Guardados {len(rows)} en {a.out}")


if __name__ == "__main__":
    main()
