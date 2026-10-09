"""Build + render a School Showdown carousel from a JSON config.
usage: python3 scripts/build_showdown.py showdowns/<name>.json
Writes templates/weeks/showdown-<name>.html and instagram/<folder>/sd1..sd6.png (1080x1350).
Config keys: folder, pill, question, a{name,short,place,color,cover,photo,big,bigsmall,bullets[],source,vote},
b{...same}, second{photo,pill,title,lead}, vote_note, credits (list of strings), not_affiliated (e.g. "UF or FSU").
Photo paths are relative to the repo root (photos/commons/<slug>/<n>.jpg). Styles: templates/showdown-style.css.html."""
import json, sys, os, html, pathlib, re
from playwright.sync_api import sync_playwright
root = pathlib.Path(__file__).resolve().parent.parent
cfg = json.load(open(sys.argv[1])); name = pathlib.Path(sys.argv[1]).stem
css = (root / "templates/showdown-style.css.html").read_text()
e = html.escape
def img(p): return f"../../{p}"
def school(id_, s):
    lis = "".join(f"<li>{e(x)}</li>" for x in s["bullets"])
    return f'''<div class="s" id="{id_}"><div class="bg" style="--img:url({img(s['photo'])})"></div><div class="shade"></div>
<div class="in"><span class="pill" style="background:{s['color']}">{e(s['name'])}</span><h2>{e(s['short'])}</h2><p class="lead">{e(s['place'])}</p></div>
<div class="stat"><div class="big">{e(s['big'])}<small>{e(s['bigsmall'])}</small></div><ul>{lis}</ul></div>
<div class="foot" style="bottom:50px"><span style="font-size:21px;color:#C9D6E4">Source: {e(s['source'])}</span><span class="swipe">→</span></div></div>'''
a, b, sec = cfg["a"], cfg["b"], cfg["second"]
body = f'''
<div class="s" id="sd1"><div class="split"><div style="--img:url({img(a['cover'])})"></div><div style="--img:url({img(b['cover'])})"></div></div><div class="shade"></div>
<div class="cover-top"><span class="pill">{e(cfg.get('pill','Florida school showdown'))}</span><h1>{e(cfg['question'])}</h1></div><div class="vs">VS</div>
<div class="labels"><div>{e(a['label'])}<small>{e(a['sub'])}</small></div><div>{e(b['label'])}<small>{e(b['sub'])}</small></div></div>
<div class="foot"><img src="../wordmark_white.png"><span class="swipe">Vote at the end →</span></div></div>
<div class="s" id="sd2"><div class="bg" style="--img:url({img(sec['photo'])})"></div><div class="shade"></div>
<div class="in"><span class="pill">{e(sec['pill'])}</span><h2>{e(sec['title'])}</h2><p class="lead">{e(sec['lead'])}</p></div>
<div class="foot"><img src="../wordmark_white.png"><span class="swipe">Swipe →</span></div></div>
{school('sd3', a)}
{school('sd4', b)}
<div class="s solid" id="sd5"><div class="vote"><span class="pill">Your vote</span><h2>{e(cfg['vote_q'])}</h2>
<div class="choices"><div>{e(a['vote'])}<small>comment it 👇</small></div><div>{e(b['vote'])}<small>comment it 👇</small></div></div>
<p>{e(cfg['vote_note'])}</p></div><div class="foot"><img src="../wordmark_white.png"><span class="swipe">→</span></div></div>
<div class="s solid" id="sd6"><div class="vote"><span class="pill">Next showdown?</span><h2>Save this + follow for more Florida matchups</h2>
<p>Deadlines, Bright Futures and campus life for Florida families. Free newsletter, link in bio.</p></div>
<div class="credits">Photos via Wikimedia Commons, text added: {e('; '.join(cfg['credits']))}. College Plan is not affiliated with {e(cfg['not_affiliated'])}.</div>
<div class="foot"><img src="../wordmark_white.png"><span style="font-family:'Poppins';font-weight:600;font-size:26px">@college.plan</span></div></div>'''
def dd(n, pos, w, rot): return f'<img class="dd" src="../doodles/{n}.svg" style="{pos};width:{w}px;transform:rotate({rot}deg)">'
DOODLES = cfg.get("doodles", {
 "sd1": [dd("star-orange","left:50px;top:420px",92,-14), dd("burst-gold","right:50px;top:430px",96,10), dd("dots-coral","left:470px;top:860px",60,0)],
 "sd2": [dd("plus-coral","right:70px;top:66px",64,8)],
 "sd3": [dd("star-gold","right:70px;top:58px",76,12)],
 "sd4": [dd("heart-coral","right:70px;top:58px",76,-10)],
 "sd5": [dd("star-gold","left:70px;top:70px",110,-12), dd("burst-mist","right:60px;top:90px",130,0), dd("heart-orange","left:120px;bottom:190px",120,-8), dd("plus-coral","right:150px;bottom:230px",70,14), dd("squiggle-gold","left:400px;bottom:250px",220,0)],
 "sd6": [dd("star-navy","left:80px;top:80px",0,0).replace('width:0px','display:none'), dd("star-orange","right:80px;top:70px",100,15), dd("heart-gold","left:90px;top:640px",120,-10), dd("burst-gold","right:110px;top:640px",120,0), dd("dots-coral","left:480px;top:690px",60,0)],
})
for sid, items in DOODLES.items():
    body = re.sub(rf'(<div class="s[^"]*" id="{sid}">)', lambda m: m.group(1) + "".join(items), body, count=1)
css = css.replace("</style>", ".dd{position:absolute;pointer-events:none;z-index:5}</style>")
out_html = root / "templates/weeks" / f"showdown-{name}.html"; out_html.parent.mkdir(parents=True, exist_ok=True)
out_html.write_text(f'<!doctype html><html><head><meta charset="utf-8">{css}</head><body>{body}</body></html>')
out = root / "instagram" / cfg["folder"]; out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file://' + str(out_html)); pg.wait_for_timeout(1200)
    for i in range(1, 7):
        pg.evaluate(f"document.querySelectorAll('body > div').forEach(d=>d.style.display = d.id=='sd{i}'?'block':'none')")
        pg.wait_for_timeout(700); pg.locator(f'#sd{i}').screenshot(path=str(out / f'sd{i}.png'))
    br.close()
from PIL import Image
ims = [Image.open(out / f"sd{i}.png") for i in range(1, 7)]; W, H = 540, 675
sheet = Image.new('RGB', (W * 3, H * 2), 'white')
for k, im in enumerate(ims): sheet.paste(im.resize((W, H)), ((k % 3) * W, (k // 3) * H))
sheet.save(out / "preview.jpg", quality=88); print("ok", out)
