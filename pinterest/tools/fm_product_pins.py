"""FreshlyMadeFL product pins (1000x1500). Usage: python3 pinterest/tools/fm_product_pins.py [pins.json]
Every sticker number must be a real value visible in the screenshot. Edit/replace PINS or pass a JSON file."""
import base64, os, sys, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pinterest/tools"))
from themes import THEMES
from playwright.sync_api import sync_playwright
from PIL import Image

W, H = 1000, 1500
OUT = os.environ.get("OUT", str(ROOT / "pinterest/freshlymadefl"))
os.makedirs(OUT, exist_ok=True)

# name, theme, line1, line2, sub, screenshot, sticker label, sticker number
PINS = [
    ("fsa_1", "blush", "FSA Spend-Down", "Tracker", "Use your FSA money before it expires",
     str(ROOT / "pinterest/assets/win") + "/fsa_02_dashboard.png", "Spend per week<br>to use it all", "$58.92"),
    ("fsa_2", "blush", "Don't Lose Your", "FSA Money", "A weekly plan to use it all on time",
     str(ROOT / "pinterest/assets/win") + "/fsa_03_weekly_pace.png", "Weeks left<br>in the plan", "12"),
    ("sinking_1", "sage", "Sinking Funds", "Planner", "Know what to save from every paycheck",
     str(ROOT / "pinterest/assets/win") + "/psp_02_dashboard.png", "Set aside from<br>next paycheck", "$398.57"),
    ("sinking_2", "sage", "How Much to Save", "Each Paycheck", "Every goal gets its own amount",
     str(ROOT / "pinterest/assets/win") + "/psp_03_savings_goals.png", "Christmas fund<br>per paycheck", "$41.67"),
    ("cake_1", "peach", "Cake Pricing", "Calculator", "Stop guessing what to charge",
     str(ROOT / "pinterest/assets/win") + "/bake_02_price_it.png", "Suggested price<br>8-inch cake", "$109.00"),
    ("cake_2", "peach", "Are You", "Undercharging?", "See your real hourly pay on every cake",
     str(ROOT / "pinterest/assets/win") + "/bake_03_undercharging.png", "Real pay on a<br>$55 cake", "$11.52/hr"),
    ("order_1", "lavender", "Order Tracker", "Spreadsheet", "Never miss a due date again",
     str(ROOT / "pinterest/assets/win") + "/ord_02_dashboard.png", "Sales<br>this month", "$392.00"),
    ("order_2", "lavender", "Organize Every", "Customer Order", "Totals, balances and alerts done for you",
     str(ROOT / "pinterest/assets/win") + "/ord_03_orders.png", "Room for", "1,000 orders"),
    ("pl_1", "sky", "Profit & Loss", "Spreadsheet", "See what your business really earns",
     str(ROOT / "pinterest/assets/win") + "/pl_02_dashboard.png", "Net profit<br>this year", "$1,834.96"),
    ("pl_2", "sky", "P&L Statement", "Made Easy", "Full year, quarter or month in one click",
     str(ROOT / "pinterest/assets/win") + "/pl_03_statement.png", "Profit<br>margin", "51%"),
    ("candle_1", "honey", "Candle Pricing", "Calculator", "Retail and wholesale prices in seconds",
     str(ROOT / "pinterest/assets/win") + "/candle_02_price_it.png", "Suggested price<br>8 oz candle", "$17.00"),
    ("candle_2", "honey", "Losing Money on", "Wholesale?", "Find the retail price that keeps you profitable",
     str(ROOT / "pinterest/assets/win") + "/candle_03_wholesale.png", "Loss per candle<br>at 50% wholesale", "-$3.37"),
]

if len(sys.argv) > 1:  # optional: pins from a JSON list of [name, theme, line1, line2, sub, screenshot path (repo-relative), sticker label, sticker number]
    PINS = [tuple(p[:5]) + (str(ROOT / p[5]),) + tuple(p[6:]) for p in json.load(open(sys.argv[1]))]

STAR = ('<svg style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px" viewBox="0 0 100 100">'
        '<path d="M50 0 C55 38 62 45 100 50 C62 55 55 62 50 100 C45 62 38 55 0 50 C38 45 45 38 50 0Z" fill="{c}"/></svg>')


def data_uri(path):
    ext = "png" if path.endswith(".png") else "jpeg"
    return f"data:image/{ext};base64," + base64.b64encode(open(path, "rb").read()).decode()


def shot_crop(path):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    c = im.crop((int(w * 0.02), int(h * 0.11), int(w * 0.98), int(h * 0.93)))
    tmp = f"/tmp/crop3_{os.path.basename(os.path.dirname(os.path.dirname(path)))}_{os.path.basename(path)}"
    c.save(tmp, quality=92)
    return tmp


def html(t, l1, l2, sub, shot, lab, num):
    return f"""<html><head><style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:{W}px;height:{H}px;overflow:hidden;background:{t['bg']};font-family:Inter,sans-serif;position:relative}}
.blob{{position:absolute;border-radius:50%;background:rgba(255,255,255,.45)}}
.top{{position:absolute;left:0;right:0;top:64px;text-align:center;padding:0 50px}}
.pill{{display:inline-block;background:{t['pill']};color:{t['ink']};font-weight:800;font-size:30px;letter-spacing:2px;padding:12px 32px;border-radius:50px}}
.h{{font-family:Poppins,sans-serif;font-weight:800;line-height:1.0;letter-spacing:-3px;white-space:nowrap}}
.l1{{color:{t['ink']};margin-top:30px}}
.l2{{color:{t['pop']}}}
.sub{{color:{t['ink']};font-size:42px;font-weight:600;line-height:1.25;margin-top:22px}}
.shot{{position:absolute;left:50%;top:0;transform:translateX(-50%) rotate(-1.5deg);border-radius:18px;overflow:hidden;
 box-shadow:0 26px 60px rgba(40,25,30,.25)}}
.shot img{{display:block;width:100%}}
.sticker{{position:absolute;right:46px;top:0;background:#fff;border:5px solid {t['ink']};border-radius:30px;
 padding:20px 30px;display:flex;align-items:center;gap:22px;transform:rotate(3deg);box-shadow:0 16px 36px rgba(40,25,30,.2)}}
.sticker .lab{{font-size:26px;font-weight:700;color:#444;line-height:1.2;text-align:left}}
.sticker .num{{font-family:Poppins;font-weight:800;font-size:64px;color:{t['ink']};letter-spacing:-2px;white-space:nowrap}}
.foot{{position:absolute;left:60px;right:60px;bottom:56px;display:flex;align-items:center;justify-content:space-between}}
.cta{{background:{t['ink']};color:#fff;font-weight:800;font-size:32px;padding:20px 40px;border-radius:60px}}
.shop{{color:{t['ink']};font-size:26px;font-weight:800;letter-spacing:3px}}
</style></head><body>
<div class="blob" style="width:560px;height:560px;left:-230px;top:-240px"></div>
<div class="blob" style="width:520px;height:520px;right:-230px;bottom:-200px"></div>
{STAR.format(x=58, y=58, s=56, c=t['pop'])}{STAR.format(x=890, y=96, s=40, c='#fff')}
{STAR.format(x=70, y=1290, s=34, c='#fff')}
<div class="top">
 <div class="pill">EXCEL + GOOGLE SHEETS</div>
 <div class="h l1" id="l1">{l1}</div>
 <div class="h l2" id="l2">{l2}</div>
 <div class="sub" id="sub">{sub}</div>
</div>
<div class="shot" id="shot"><img src="{shot}"></div>
<div class="sticker" id="stk"><div class="lab">{lab}</div><div class="num">{num}</div></div>
<div class="foot"><div class="cta">Instant download on Etsy</div><div class="shop">FRESHLYMADEFL</div></div>
<script>(function(){{
let s = 140; const a = document.getElementById('l1'), b = document.getElementById('l2');
function set(v){{a.style.fontSize=v+'px'; b.style.fontSize=v+'px';}}
set(s);
while ((a.scrollWidth > 900 || b.scrollWidth > 900) && s > 60) {{ s -= 2; set(s); }}
document.body.dataset.size = s;
}})();</script>
</body></html>"""


with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    for name, theme, l1, l2, sub, shot, lab, num in PINS:
        pg.set_content(html(THEMES[theme], l1, l2, sub, data_uri(shot), lab, num))
        pg.wait_for_function("() => document.querySelector('.shot img').complete && document.querySelector('.shot img').naturalWidth > 0")
        pg.evaluate("""() => {
          const img = document.querySelector('.shot img'), shot = document.getElementById('shot'), stk = document.getElementById('stk');
          const subB = document.getElementById('sub').getBoundingClientRect().bottom;
          const footT = document.querySelector('.foot').getBoundingClientRect().top;
          const stkH = stk.getBoundingClientRect().height;
          const avail = footT - subB - 60 - stkH * 0.55;
          const ratio = img.naturalWidth / img.naturalHeight;
          let w, h;
          if (ratio > 1.4) {
            h = Math.min(avail, 560); w = h * ratio;
            shot.style.left = '70px'; shot.style.transform = 'rotate(-1.5deg)';
            shot.style.borderRadius = '18px 0 0 18px';
          } else {
            w = Math.min(900, avail * ratio); h = w / ratio;
          }
          img.style.width = w + 'px';
          const top = subB + 34 + Math.max(0, (avail - h) / 2);
          shot.style.top = top + 'px';
          stk.style.top = (top + h - stkH * 0.45) + 'px';
        }""")
        pg.wait_for_timeout(150)
        info = pg.evaluate("""() => {const s=document.getElementById('stk').getBoundingClientRect();
            const f=document.querySelector('.foot').getBoundingClientRect();
            return {size: document.body.dataset.size, shotW: Math.round(document.querySelector('.shot img').getBoundingClientRect().width),
                    stickerBottom: Math.round(s.bottom), footTop: Math.round(f.top), stickerLeft: Math.round(s.left)}}""")
        png = f"/tmp/v3_{name}.png"
        pg.screenshot(path=png)
        Image.open(png).convert("RGB").save(f"{OUT}/pin_{name}.jpg", quality=92)
        print(name, info)
    br.close()
