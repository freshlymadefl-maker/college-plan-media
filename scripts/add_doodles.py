"""Add a few College Plan doodles to an already-rendered post PNG, only in empty areas.
usage: python3 scripts/add_doodles.py in.png out.png [count=3] [seed]
Finds the calmest spots (low detail, away from text) near the edges and drops 2-4 doodles there.
Always LOOK at the result: if a doodle touches text or a face, rerun with another seed or a lower count.
New posts should place doodles in the HTML instead (see templates/doodles/README.md)."""
import sys, random, pathlib
import numpy as np
from PIL import Image, ImageFilter
root = pathlib.Path(__file__).resolve().parent.parent
src, out = sys.argv[1], sys.argv[2]
count = int(sys.argv[3]) if len(sys.argv) > 3 else 3
rng = random.Random(int(sys.argv[4]) if len(sys.argv) > 4 else hash(pathlib.Path(out).name) % 10000)
im = Image.open(src).convert("RGBA"); W, H = im.size
arr = np.asarray(im.convert("RGB"), dtype=float)
g = np.asarray(im.convert("L").filter(ImageFilter.FIND_EDGES), dtype=float)
cell = 150; pad = 30; cand = []
for y in range(30, H - cell - 30, 25):
    for x in range(30, W - cell - 30, 25):
        edge = min(x, W - x - cell, y, H - y - cell)
        if edge > 280: continue  # keep to an edge band
        y0, y1, x0, x1 = max(0, y - pad), min(H, y + cell + pad), max(0, x - pad), min(W, x + cell + pad)
        patch = arr[y0:y1, x0:x1]
        # must be plain background: same color as the nearest image edge at this height/width, and flat
        ref = arr[min(H - 1, y + cell // 2), 6] if x < W / 2 else arr[min(H - 1, y + cell // 2), W - 7]
        dist = np.abs(patch - ref).max(axis=2)
        if (dist > 14).mean() > 0.01: continue
        busy = g[y0:y1, x0:x1].mean()
        cand.append((busy + edge * 0.01, x, y))
cand.sort()
shapes = ["star", "burst", "heart", "plus", "squiggle", "dots"]
colors = ["gold", "orange", "coral", "mist", "blue"]
placed = []
for busy, x, y in cand:
    if len(placed) >= count or busy > 9: break
    if any(abs(x - px) < 260 and abs(y - py) < 260 for px, py in placed): continue
    placed.append((x, y))
for i, (x, y) in enumerate(placed):
    shape = shapes[(i + rng.randint(0, 5)) % len(shapes)]
    if shape == "squiggle": shape = "star"
    d = Image.open(root / f"templates/doodles/png/{shape}-{rng.choice(colors)}.png").convert("RGBA"); d = d.crop(d.getbbox())
    size = rng.randint(80, 120) if shape != "dots" else 70
    d.thumbnail((size, size)); d = d.rotate(rng.randint(-18, 18), expand=True, resample=Image.BICUBIC)
    im.alpha_composite(d, (x + (cell - d.width) // 2, y + (cell - d.height) // 2))
im.convert("RGB").save(out); print("ok", out, len(placed), "doodles")
