"""Render the Cozy Little Finds campy-Christmas slides to PNG (1080x1350).
usage: python3 cozy-little-finds/templates/render.py [outdir]  -> cover.png list.png joke.png sheet.png"""
import sys, pathlib
from playwright.sync_api import sync_playwright
here = pathlib.Path(__file__).resolve().parent
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else here.parent / "2026-11-campy-xmas")
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
    for s in ["cover", "list", "joke", "sheet"]:
        pg.goto(f"file://{here}/campy-xmas.html?s={s}"); pg.wait_for_timeout(800)
        pg.screenshot(path=str(out / f"{s}.png")); print(out / f"{s}.png")
    b.close()
