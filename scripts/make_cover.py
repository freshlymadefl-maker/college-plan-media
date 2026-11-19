#!/usr/bin/env python3
"""Make a Reel/TikTok cover image (1080x1920 JPG) that reads well in the
Instagram grid, the Reels tab and the TikTok profile.

Why: our Reels build up on screen (empty checklist -> filled, kinetic words),
so frame 0 looks almost blank, and the hook sits near the top where the grid's
center crop cuts it off. The cover puts the hook BIG in the middle safe zone
(inside every crop) over a blurred frame from the video, with the fully built
frame shown below it as a tilted card.

Usage:
  python3 scripts/make_cover.py <video.mp4> <out.jpg> --t 6.5 --hook "Hook line" [--kicker "9th & 10th grade parents"]
  python3 scripts/make_cover.py <video.mp4> <out.jpg> --t 0 --frame   # use the frame as-is (title-card slideshows)

--t = seconds into the video for the background frame: pick the moment where the
most content is on screen (fully built list/tier/checklist), before the end card.
Always LOOK at the result (Read) and at a 3:4 center crop before using it.
Then pass it to Metricool as info.videoThumbnailUrl (raw.githubusercontent URL
pinned to the commit sha).
"""
import argparse, html, os, subprocess, sys, tempfile, base64

ap = argparse.ArgumentParser()
ap.add_argument('video'); ap.add_argument('out')
ap.add_argument('--t', type=float, default=0.0)
ap.add_argument('--hook', default='')
ap.add_argument('--kicker', default='')
ap.add_argument('--frame', action='store_true', help='use the video frame as the cover, no overlay')
a = ap.parse_args()

tmp = tempfile.mkdtemp()
fr = os.path.join(tmp, 'f.png')
subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', str(a.t), '-i', a.video,
                '-frames:v', '1', '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920', fr], check=True)
if a.frame:
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', fr, '-q:v', '2', a.out], check=True)
    print(a.out); sys.exit()
if not a.hook:
    sys.exit('--hook is required unless --frame')

here = os.path.dirname(os.path.abspath(__file__))
burst = os.path.join(here, '..', 'templates', 'doodles', 'burst-gold.svg')
b64 = base64.b64encode(open(fr, 'rb').read()).decode()
burst_tag = f'<img class="burst" src="file://{os.path.abspath(burst)}">' if os.path.exists(burst) else ''
kick = f'<div class="kick">{html.escape(a.kicker)}</div>' if a.kicker else ''
n = len(a.hook)
size = 84 if n <= 40 else 74 if n <= 60 else 64 if n <= 85 else 56
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;800&display=block" rel="stylesheet">
<style>
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden}}
.bg{{position:absolute;inset:-60px;background:url(data:image/png;base64,{b64}) center/cover;filter:blur(26px) brightness(.62) saturate(1.25)}}
.shot{{width:430px;height:764px;border:12px solid #fff;border-radius:28px;background:url(data:image/png;base64,{b64}) center/cover;box-shadow:0 26px 60px rgba(0,0,0,.45);transform:rotate(-3deg);margin-top:46px;flex:none}}
.wrap{{position:absolute;left:70px;right:70px;top:290px;bottom:290px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}}
.kick{{font-family:Poppins;font-weight:800;font-size:36px;background:#F1E27A;color:#0B2A4A;padding:10px 28px;border-radius:999px;margin-bottom:28px}}
.hook{{font-family:Poppins;font-weight:800;font-size:{size}px;line-height:1.32;margin:0}}
.hook span{{background:#fff;color:#0B2A4A;padding:4px 28px;border-radius:22px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.burst{{position:absolute;width:130px;right:120px;bottom:330px}}
</style></head><body><div class="bg"></div>{burst_tag}
<div class="wrap">{kick}<p class="hook"><span>{html.escape(a.hook)}</span></p><div class="shot"></div></div></body></html>"""
hp = os.path.join(tmp, 'c.html'); open(hp, 'w').write(page)
png = os.path.join(tmp, 'c.png')
try:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto('file://' + hp); pg.wait_for_timeout(1200)
        pg.screenshot(path=png); b.close()
except ImportError:  # no Python Playwright: use the Node one
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
          "const p=await b.newPage({viewport:{width:1080,height:1920}});"
          f"await p.goto('file://{hp}');await p.waitForTimeout(1200);"
          f"await p.screenshot({{path:'{png}'}});await b.close();}})();")
    subprocess.run(['node', '-e', js], check=True)
subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', png, '-q:v', '2', a.out], check=True)
print(a.out)
