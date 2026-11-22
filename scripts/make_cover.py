#!/usr/bin/env python3
"""Make a Reel/TikTok cover image (1080x1920 JPG) that reads well in the
Instagram grid, the Reels tab and the TikTok profile.

Owner, Nov 22 2026: "I don't like that all our cover images are looking the same."
So covers now ROTATE between several looks. `--style auto` (the default) picks the
look used least recently (log: covers/style-log.json), never the same look twice
in a row. Every look keeps the hook BIG inside the grid's center 3:4 crop
(y 240-1680), so nothing important gets cut off.

Looks:
  card      blurred frame + white sticker hook + tilted phone card (the original)
  bigtype   no video frame: one flat brand color, oversized hook, doodles
  split     flat color top half with the hook, the video frame filling the bottom half
  sticky    the real frame (dimmed) with the hook handwritten on a taped sticky note
  scrapbook cream paper, the frame as a taped polaroid, handwritten hook
  photo     the frame full-bleed, dark fade at the bottom, big white hook
            (best for stock-clip / face Reels)

Mark ONE accent word with asterisks to set it in Lora italic gold: "Senior parent *math*".

Usage:
  python3 scripts/make_cover.py <video.mp4> <out.jpg> --t 6.5 --hook "Hook line" [--kicker "9th grade parents"] [--style auto|card|bigtype|split|sticky|scrapbook|photo]
  python3 scripts/make_cover.py <video.mp4> <out.jpg> --t 0 --frame   # use the frame as-is (title-card slideshows)

--t = seconds into the video for the frame: pick the moment where the most content
is on screen (fully built list/tier/checklist), before the end card. For `photo`,
pick a moment where the person/photo is visible.
Always LOOK at the result (Read) and at a 3:4 center crop before using it.
Then pass it to Metricool as info.videoThumbnailUrl (raw.githubusercontent URL
pinned to the commit sha).
"""
import argparse, base64, html, json, os, re, subprocess, sys, tempfile

STYLES = ['bigtype', 'split', 'sticky', 'scrapbook', 'photo', 'card']
NAVY, BLUE, GOLD, YELLOW, CORAL, CREAM, SKY = '#0B2A4A', '#5B8DC9', '#B5A21F', '#F1E27A', '#F05A28', '#FFF8EC', '#DCE9F7'

ap = argparse.ArgumentParser()
ap.add_argument('video'); ap.add_argument('out')
ap.add_argument('--t', type=float, default=0.0)
ap.add_argument('--hook', default='')
ap.add_argument('--kicker', default='')
ap.add_argument('--style', default='auto', choices=['auto'] + STYLES)
ap.add_argument('--color', type=int, default=None, help='color variant 0-3 (default: rotates per look)')
ap.add_argument('--no-log', action='store_true', help="don't record this cover in covers/style-log.json")
ap.add_argument('--frame', action='store_true', help='use the video frame as the cover, no overlay')
a = ap.parse_args()

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..'))
tmp = tempfile.mkdtemp()
fr = os.path.join(tmp, 'f.png')
subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', str(a.t), '-i', a.video,
                '-frames:v', '1', '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920', fr], check=True)
if a.frame:
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', fr, '-q:v', '2', a.out], check=True)
    print(a.out); sys.exit()
if not a.hook:
    sys.exit('--hook is required unless --frame')

# ---- pick the look -------------------------------------------------------
log_path = os.path.join(root, 'covers', 'style-log.json')
try:
    log = json.load(open(log_path))
except Exception:
    log = []
name = os.path.splitext(os.path.basename(a.out))[0]
style = a.style
if style == 'auto':
    recent = [e['style'] for e in log if e.get('name') != name]
    def last_used(s):
        idx = [i for i, x in enumerate(recent) if x == s]
        return idx[-1] if idx else -1
    style = min(STYLES, key=lambda s: (last_used(s), STYLES.index(s)))
# color variant: rotates each time a look is reused (or --color N)
seed = a.color if a.color is not None else sum(1 for e in log if e.get('style') == style and e.get('name') != name)

def pick(options):
    return options[seed % len(options)]

# ---- shared bits ---------------------------------------------------------
b64 = base64.b64encode(open(fr, 'rb').read()).decode()
IMG = f'url(data:image/png;base64,{b64})'
dd = lambda n: 'file://' + os.path.join(root, 'templates', 'doodles', n + '.svg')
caveat = 'file://' + os.path.join(root, 'templates', 'fonts', 'caveat-700.woff2')

def hook_html(accent_color):
    """escape the hook, turning *word* into the Lora italic accent."""
    out, parts = '', re.split(r'(\*[^*]+\*)', a.hook)
    for p in parts:
        if p.startswith('*') and p.endswith('*') and len(p) > 2:
            out += f'<em style="color:{accent_color}">{html.escape(p[1:-1])}</em>'
        else:
            out += html.escape(p)
    return out

n = len(a.hook.replace('*', ''))
def fit(sizes):  # sizes for <=25, <=40, <=60, <=85, longer
    for lim, s in zip((25, 40, 60, 85), sizes):
        if n <= lim:
            return s
    return sizes[-1]

def doodle(nm, left=None, top=None, right=None, bottom=None, w=110, rot=0):
    pos = ';'.join(f'{k}:{v}px' for k, v in (('left', left), ('top', top), ('right', right), ('bottom', bottom)) if v is not None)
    return f'<img class="dd" src="{dd(nm)}" style="{pos};width:{w}px;transform:rotate({rot}deg)">'

kick = html.escape(a.kicker)
base_css = f"""
@font-face{{font-family:Caveat;src:url({caveat}) format('woff2');font-weight:700}}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;font-family:Poppins}}
.dd{{position:absolute;z-index:5}}
em{{font-family:Lora;font-style:italic;font-weight:600}}
.wm{{position:absolute;bottom:300px;left:0;right:0;text-align:center;font-family:Poppins;font-weight:700;font-size:34px;letter-spacing:-.5px}}
.wm i{{font-family:Lora;font-weight:500}}
"""
wm = lambda c: f'<div class="wm" style="color:{c}"><i>college</i>plan</div>'

# ---- looks -----------------------------------------------------------------
if style == 'card':
    size = 84 if n <= 40 else 74 if n <= 60 else 64 if n <= 85 else 56
    k = f'<div class="kick">{kick}</div>' if kick else ''
    css = f"""
.bg{{position:absolute;inset:-60px;background:{IMG} center/cover;filter:blur(26px) brightness(.62) saturate(1.25)}}
.shot{{width:430px;height:764px;border:12px solid #fff;border-radius:28px;background:{IMG} center/cover;box-shadow:0 26px 60px rgba(0,0,0,.45);transform:rotate(-3deg);margin-top:46px;flex:none}}
.wrap{{position:absolute;left:70px;right:70px;top:290px;bottom:290px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}}
.kick{{font-weight:800;font-size:36px;background:{YELLOW};color:{NAVY};padding:10px 28px;border-radius:999px;margin-bottom:28px}}
.hook{{font-weight:800;font-size:{size}px;line-height:1.32;margin:0}}
.hook span{{background:#fff;color:{NAVY};padding:4px 28px;border-radius:22px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
"""
    body = f'<div class="bg"></div>{doodle("burst-gold", right=120, bottom=330, w=130)}<div class="wrap">{k}<p class="hook"><span>{hook_html(CORAL)}</span></p><div class="shot"></div></div>'

elif style == 'bigtype':
    bg, fg, acc, kbg, kfg, dds = pick([
        (NAVY, '#FFFFFF', YELLOW, YELLOW, NAVY, ('star-gold', 'squiggle-blue', 'burst-orange')),
        (YELLOW, NAVY, CORAL, NAVY, '#FFFFFF', ('star-navy', 'squiggle-coral', 'burst-navy')),
        (CORAL, '#FFFFFF', YELLOW, '#FFFFFF', CORAL, ('star-gold', 'squiggle-navy', 'burst-gold')),
        (SKY, NAVY, BLUE, NAVY, '#FFFFFF', ('star-orange', 'squiggle-navy', 'burst-gold')),
    ])
    size = fit([150, 128, 108, 92, 80])
    k = f'<div class="kick">{kick}</div>' if kick else ''
    css = f"""
body{{background:{bg}}}
.wrap{{position:absolute;left:96px;right:96px;top:330px;bottom:400px;display:flex;flex-direction:column;justify-content:center}}
.kick{{align-self:flex-start;font-weight:800;font-size:38px;background:{kbg};color:{kfg};padding:10px 30px;border-radius:999px;margin-bottom:40px}}
.hook{{font-weight:800;font-size:{size}px;line-height:1.04;letter-spacing:-2px;color:{fg};margin:0}}
.hook em{{letter-spacing:0}}
"""
    body = (f'{doodle(dds[0], right=110, top=300, w=120, rot=12)}{doodle(dds[1], left=96, bottom=420, w=230)}'
            f'{doodle(dds[2], right=120, bottom=400, w=150, rot=-8)}<div class="wrap">{k}<p class="hook">{hook_html(acc)}</p></div>{wm(fg)}')

elif style == 'split':
    bg, fg, acc, edge = pick([(NAVY, '#FFFFFF', YELLOW, YELLOW), (YELLOW, NAVY, CORAL, NAVY),
                              (CORAL, '#FFFFFF', YELLOW, NAVY), (BLUE, '#FFFFFF', YELLOW, YELLOW)])
    size = fit([118, 100, 86, 74, 64])
    k = f'<div class="kick">{kick}</div>' if kick else ''
    css = f"""
.top{{position:absolute;left:0;right:0;top:0;height:1010px;background:{bg}}}
.bot{{position:absolute;left:0;right:0;top:1010px;bottom:0;background:{IMG} center 42%/1260px auto no-repeat;background-color:#eee}}
.edge{{position:absolute;left:0;right:0;top:996px;height:28px;background:{edge};z-index:3}}
.wrap{{position:absolute;left:84px;right:84px;top:300px;height:670px;display:flex;flex-direction:column;justify-content:flex-end}}
.kick{{align-self:flex-start;font-weight:800;font-size:36px;color:{acc};margin-bottom:22px;letter-spacing:1px;text-transform:uppercase}}
.hook{{font-weight:800;font-size:{size}px;line-height:1.08;letter-spacing:-1.5px;color:{fg};margin:0}}
"""
    body = (f'<div class="top"></div><div class="bot"></div><div class="edge"></div>'
            f'{doodle("star-gold" if bg != YELLOW else "star-navy", right=90, top=330, w=110, rot=10)}'
            f'<div class="wrap">{k}<p class="hook">{hook_html(acc)}</p></div>')

elif style == 'sticky':
    note, rot = pick([(YELLOW, -3), ('#FFD4C2', 2.5), ('#CFE6FF', -2), ('#D9F2D0', 3)])
    size = fit([170, 150, 128, 108, 92])
    k = f'<div class="kick">{kick}</div>' if kick else ''
    css = f"""
.bg{{position:absolute;inset:-40px;background:{IMG} center/cover;filter:blur(7px) brightness(.45) saturate(1.1)}}
.note{{position:absolute;left:110px;right:110px;top:430px;min-height:900px;background:{note};transform:rotate({rot}deg);
  box-shadow:0 30px 60px rgba(0,0,0,.45);padding:100px 64px 80px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:center}}
.tape{{position:absolute;top:-34px;left:50%;width:260px;height:70px;margin-left:-130px;background:rgba(255,255,255,.6);transform:rotate(-4deg)}}
.kick{{font-family:Poppins;font-weight:800;font-size:34px;color:{NAVY};opacity:.75;margin-bottom:18px}}
.hook{{font-family:Caveat;font-weight:700;font-size:{size}px;line-height:1.02;color:{NAVY};margin:0}}
.hook em{{font-family:Caveat;font-style:normal;color:{CORAL};text-decoration:underline;text-decoration-thickness:6px;text-underline-offset:10px}}
"""
    body = (f'<div class="bg"></div><div class="note"><div class="tape"></div>{k}<p class="hook">{hook_html(CORAL)}</p></div>'
            f'{doodle("burst-gold", right=60, top=1330, w=150, rot=8)}')

elif style == 'scrapbook':
    size = fit([140, 124, 108, 94, 82])
    k = f'<div class="kick">{kick}</div>' if kick else ''
    css = f"""
body{{background:{CREAM} radial-gradient(rgba(11,42,74,.08) 2px,transparent 2px) 0 0/34px 34px}}
.wrap{{position:absolute;left:80px;right:80px;top:290px;text-align:left}}
.kick{{display:inline-block;font-weight:800;font-size:32px;background:{NAVY};color:#fff;padding:8px 24px;transform:rotate(-2deg);margin-bottom:16px}}
.hook{{font-family:Caveat;font-weight:700;font-size:{size}px;line-height:1;color:{NAVY};margin:0}}
.hook em{{font-family:Caveat;font-style:normal;background:linear-gradient(transparent 55%,{YELLOW} 55%)}}
.pol{{position:absolute;left:300px;top:960px;width:520px;height:700px;background:#fff;padding:26px 26px 90px;box-sizing:border-box;
  transform:rotate(4deg);box-shadow:0 22px 50px rgba(0,0,0,.22)}}
.pol div{{width:100%;height:100%;background:{IMG} center 40%/cover}}
.tape{{position:absolute;width:200px;height:60px;background:rgba(241,226,122,.85);z-index:4}}
"""
    body = (f'<div class="wrap">{k}<p class="hook">{hook_html(CORAL)}</p></div>'
            f'<div class="pol"><div></div></div><div class="tape" style="left:280px;top:950px;transform:rotate(-30deg)"></div>'
            f'<div class="tape" style="left:720px;top:980px;transform:rotate(35deg)"></div>'
            f'{doodle("heart-coral", left=110, top=1300, w=110, rot=-12)}{doodle("squiggle-blue", left=90, top=1480, w=170)}'
            f'{doodle("star-gold", right=70, top=1560, w=100, rot=15)}')

elif style == 'photo':
    size = fit([128, 108, 92, 80, 70])
    k = f'<div class="kick">{kick}</div>' if kick else ''
    css = f"""
.bg{{position:absolute;inset:-40px;background:{IMG} center/cover;filter:blur(9px) brightness(.85)}}
.fade{{position:absolute;inset:0;background:linear-gradient(rgba(11,42,74,0) 25%,rgba(11,42,74,.78) 52%,rgba(11,42,74,.95) 100%)}}
.wrap{{position:absolute;left:80px;right:80px;top:300px;bottom:330px;display:flex;flex-direction:column;justify-content:flex-end}}
.kick{{align-self:flex-start;font-weight:800;font-size:34px;background:{YELLOW};color:{NAVY};padding:8px 26px;border-radius:10px;margin-bottom:26px}}
.hook{{font-weight:800;font-size:{size}px;line-height:1.06;letter-spacing:-1.5px;color:#fff;margin:0;text-shadow:0 4px 30px rgba(0,0,0,.35)}}
"""
    body = f'<div class="bg"></div><div class="fade"></div><div class="wrap">{k}<p class="hook">{hook_html(YELLOW)}</p></div>'

page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Lora:ital,wght@1,500;1,600&display=block" rel="stylesheet">
<style>{base_css}{css}</style></head><body>{body}</body></html>"""
hp = os.path.join(tmp, 'c.html'); open(hp, 'w').write(page)
png = os.path.join(tmp, 'c.png')
try:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto('file://' + hp); pg.wait_for_timeout(1500)
        pg.screenshot(path=png); b.close()
except ImportError:  # no Python Playwright: use the Node one
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
          "const p=await b.newPage({viewport:{width:1080,height:1920}});"
          f"await p.goto('file://{hp}');await p.waitForTimeout(1500);"
          f"await p.screenshot({{path:'{png}'}});await b.close();}})();")
    subprocess.run(['node', '-e', js], check=True)
subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', png, '-q:v', '2', a.out], check=True)

if not a.no_log:
    log = [e for e in log if e.get('name') != name] + [{'name': name, 'style': style}]
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    json.dump(log, open(log_path, 'w'), indent=1)
print(a.out, style)
