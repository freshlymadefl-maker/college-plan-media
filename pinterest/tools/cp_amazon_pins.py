"""College Plan branded pins (cheat sheets + college product pins). Copy, replace CHEATS/PRODUCTS with NEW content, run, LOOK at every PNG."""
import base64, os
from playwright.sync_api import sync_playwright
from PIL import Image

W, H = 1000, 1500
import pathlib
R = str(pathlib.Path(__file__).resolve().parents[2]) + "/"
CTA = os.environ.get("CTA", "Shop my picks: tap the link")
OUT = os.environ.get("OUT", R + "pinterest/collegeplan")
os.makedirs(OUT, exist_ok=True)


def uri(p, t="png"):
    return f"data:image/{t};base64," + base64.b64encode(open(p, "rb").read()).decode()


WM = uri(R + "templates/wordmark_navy.png")


def dd(n):
    return "data:image/svg+xml;base64," + base64.b64encode(open(R + "templates/doodles/" + n + ".svg", "rb").read()).decode()


def checklist(items, cols=1):
    return f'<ul class="ck c{cols}">' + "".join(f'<li><span class="bx"></span><span>{i}</span></li>' for i in items) + "</ul>"


def rows(pairs):
    return '<div class="rows">' + "".join(f'<div class="rw"><b>{a}</b><span>{b}</span></div>' for a, b in pairs) + "</div>"


def note(t):
    return f'<div class="note">{t}</div>'


CHEATS = [
    ("cp_amz_hook", "Senior Parent", "Shopping Lists", "6 checklists to save for the year ahead",
     checklist(["SAT + ACT test day bag", "College visit bag", "Senior year study desk", "Dorm room must-haves", "Gifts for college-bound seniors", "Sorority recruitment bag"], 1)),
    ("cp_amz_testday", "SAT + ACT", "Test Day Bag", "Pack it the night before",
     checklist(["Admission ticket (printed if required)", "Photo ID", "Sharpened No. 2 pencils + eraser",
                "Approved calculator + extra batteries", "Charged device (digital SAT)", "Water bottle",
                "Snacks for the break", "Watch with no alarms or internet", "Layers for a cold room"])
     + note("Rules change. Check collegeboard.org or act.org for your test.")),
    ("cp_amz_visit", "College Visit", "Bag Checklist", "What to bring on campus tours",
     checklist(["Comfy walking shoes", "Portable phone charger", "Water bottle", "Small umbrella",
                "Notebook to rate each campus", "Questions for the tour guide", "Snacks for the drive",
                "Sunscreen (it's Florida)"], 1)),
    ("cp_amz_dorm", "Dorm Room", "Must-Haves", "The stuff moms say they forgot",
     checklist(["Twin XL sheets (check your school)", "Mattress topper", "Shower caddy", "Shower shoes",
                "Under-bed storage", "Command hooks", "Clip-on fan", "Laundry hamper", "Desk lamp",
                "First aid kit", "Power strip (check dorm rules)", "Earplugs + sleep mask"], 2)
     + note("Every dorm has its own banned items list. Check housing rules first.")),
    ("cp_amz_desk", "Senior Year", "Study Desk Setup", "Help them get through application season",
     checklist(["Wall calendar for deadlines", "Accordion file for college papers", "Laptop stand",
                "Desk lamp", "Noise-cancelling headphones", "Planner", "Highlighters + sticky notes",
                "Phone stand", "Comfy desk chair cushion"], 1)),
    ("cp_amz_grad", "Gifts for", "College-Bound Seniors", "Useful gifts they'll actually use",
     checklist(["Mini toolkit", "Handheld steamer", "Luggage tags", "Portable charger", "Shower caddy",
                "Laundry bag", "Water bottle", "Dorm cookbook", "Gift card for books"], 1)),
    ("cp_amz_rush", "Sorority Recruitment", "Bag Checklist", "Everything for long days in the heat",
     checklist(["Blister bandages", "Mini fan", "Stain remover pen", "Portable charger", "Fold-up flats",
                "Water bottle", "Mints", "Deodorant", "Hair ties + bobby pins", "Small mirror"], 2)),
]
PRODUCTS = []
BASE = """*{margin:0;padding:0;box-sizing:border-box}
body{width:1000px;height:1500px;overflow:hidden;position:relative;font-family:Inter,sans-serif;color:#2A3D54;
 background:linear-gradient(160deg,#F4F9FE 0%,#EAF3FB 45%,#D4E6F7 100%)}
.top{position:absolute;left:0;right:0;top:64px;text-align:center;padding:0 50px}
.pill{display:inline-block;background:#0B2A4A;color:#fff;font-family:Poppins;font-weight:600;font-size:24px;letter-spacing:.14em;padding:10px 26px;border-radius:999px}
.h{font-family:Poppins;font-weight:700;color:#0B2A4A;line-height:1.02;letter-spacing:-.025em;white-space:nowrap;margin-top:22px}
.ser{font-family:Lora,serif;font-style:italic;font-weight:500;color:#5B8DC9;line-height:1.05;white-space:nowrap}
.sub{font-size:34px;color:#3A4F66;margin-top:14px;font-weight:500}
.card{position:absolute;left:50px;right:50px;background:#fff;border-radius:30px;padding:1.2em 1.4em;box-shadow:0 14px 40px rgba(11,42,74,.10);font-size:34px}
ul.ck{list-style:none;display:grid;row-gap:.5em} ul.c2{grid-template-columns:1fr 1fr;column-gap:1em}
ul.ck li{display:flex;gap:.55em;align-items:flex-start;line-height:1.25}
.bx{flex:none;width:.95em;height:.95em;border:3px solid #0B2A4A;border-radius:6px;margin-top:.12em}
.rows .rw{padding:.45em 0;border-bottom:3px solid #EAF3FB;line-height:1.3}
.rows .rw:last-child{border-bottom:none}
.rows b{display:block;font-family:Poppins;font-weight:700;color:#0B2A4A}
.rows span{color:#3A4F66;font-size:.88em}
.note{margin-top:.6em;font-size:.66em;color:#6A7D92;font-style:italic;text-align:center}
.foot{position:absolute;left:0;right:0;bottom:48px;display:flex;justify-content:center}
.foot img{height:44px}
.dd{position:absolute}
.shot{position:absolute;left:50%;top:0;transform:translateX(-50%) rotate(-1.5deg);border-radius:18px;overflow:hidden;box-shadow:0 26px 60px rgba(11,42,74,.22);background:#fff}
.shot img{display:block;width:100%}
.sticker{position:absolute;right:46px;top:0;background:#fff;border-radius:26px;padding:18px 28px;display:flex;align-items:center;gap:20px;transform:rotate(2.5deg);box-shadow:0 14px 34px rgba(11,42,74,.18)}
.sticker .lab{font-size:24px;font-weight:600;color:#5E7186;line-height:1.2;text-align:left}
.sticker .num{font-family:Poppins;font-weight:700;font-size:60px;color:#0B2A4A;white-space:nowrap}
.cta{background:#B5A21F;color:#fff;font-family:Poppins;font-weight:600;font-size:30px;padding:16px 34px;border-radius:999px}
"""
DECOR = (f'<svg style="position:absolute;left:880px;top:14px" width="84" height="84" viewBox="0 0 150 150"><path d="M20 140 C20 70 70 22 140 18" stroke="#B5A21F" stroke-width="12" fill="none" stroke-linecap="round"/></svg>'
         f'<img class="dd" src="{dd("star-gold")}" style="left:930px;top:92px;width:44px">'
         f'<img class="dd" src="{dd("star-blue")}" style="left:56px;top:60px;width:44px">')
FIT = """<script>(function(){let s=120;const a=document.getElementById('l1'),b=document.getElementById('l2');
function set(v){a.style.fontSize=v+'px';b.style.fontSize=(v*1.12)+'px';}set(s);
while((a.scrollWidth>900||b.scrollWidth>900)&&s>56){s-=2;set(s);}document.body.dataset.size=s;})();</script>"""


def cheat_html(l1, l2, sub, body):
    return f"""<html><head><style>{BASE}</style></head><body>{DECOR}
<div class="top"><div class="pill">SAVE THIS CHECKLIST</div><div class="h" id="l1">{l1}</div><div class="ser" id="l2">{l2}</div><div class="sub" id="sub">{sub}</div></div>
<div class="card" id="card">{body}</div>
<div class="foot" style="flex-direction:column;align-items:center;gap:12px;bottom:28px"><div class="cta">{CTA}</div><div style="font-size:18px;color:#6A7D92">As an Amazon Associate I earn from qualifying purchases.</div><img src="{WM}" style="height:38px"></div>{FIT}
<script>(function(){{const c=document.getElementById('card');const top=document.getElementById('sub').getBoundingClientRect().bottom+34;
const bottom=1500-230;c.style.top=top+'px';let f=40;c.style.fontSize=f+'px';
while(c.getBoundingClientRect().height>bottom-top&&f>18){{f-=1;c.style.fontSize=f+'px';}}
const h=c.getBoundingClientRect().height;c.style.top=(top+Math.max(0,(bottom-top-h)/2))+'px';document.body.dataset.card=f;}})();</script>
</body></html>"""


def product_html(l1, l2, sub, shot, lab, num):
    return f"""<html><head><style>{BASE}</style></head><body>{DECOR}
<div class="top"><div class="pill">EXCEL + GOOGLE SHEETS</div><div class="h" id="l1">{l1}</div><div class="ser" id="l2">{l2}</div><div class="sub" id="sub">{sub}</div></div>
<div class="shot" id="shot"><img src="{uri(shot)}"></div>
<div class="sticker" id="stk"><div class="lab">{lab}</div><div class="num">{num}</div></div>
<div class="foot" style="justify-content:space-between;left:60px;right:60px;align-items:center"><div class="cta">Instant download</div><img src="{WM}"></div>{FIT}
</body></html>"""


LAYOUT = """() => {
  const img=document.querySelector('.shot img'),shot=document.getElementById('shot'),stk=document.getElementById('stk');
  const subB=document.getElementById('sub').getBoundingClientRect().bottom;
  const footT=document.querySelector('.foot').getBoundingClientRect().top;
  const stkH=stk.getBoundingClientRect().height;
  const avail=footT-subB-60-stkH*0.55; const ratio=img.naturalWidth/img.naturalHeight; let w,h;
  if(ratio>1.4){h=Math.min(avail,560);w=h*ratio;shot.style.left='70px';shot.style.transform='rotate(-1.5deg)';shot.style.borderRadius='18px 0 0 18px';}
  else{w=Math.min(900,avail*ratio);h=w/ratio;}
  img.style.width=w+'px'; const top=subB+34+Math.max(0,(avail-h)/2); shot.style.top=top+'px';
  stk.style.top=(top+h-stkH*0.45)+'px'; }"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": W, "height": H})
    for name, l1, l2, sub, body in CHEATS:
        pg.set_content(cheat_html(l1, l2, sub, body)); pg.wait_for_timeout(300)
        print(name, pg.evaluate("() => document.body.dataset.size + '/' + document.body.dataset.card"))
        pg.screenshot(path=f"/tmp/{name}.png")
        Image.open(f"/tmp/{name}.png").convert("RGB").save(f"{OUT}/{name}.jpg", quality=92)
    for name, l1, l2, sub, shot, lab, num in PRODUCTS:
        pg.set_content(product_html(l1, l2, sub, shot, lab, num))
        pg.wait_for_function("() => document.querySelector('.shot img').complete && document.querySelector('.shot img').naturalWidth > 0")
        pg.evaluate(LAYOUT); pg.wait_for_timeout(200)
        print(name, pg.evaluate("() => document.body.dataset.size"))
        pg.screenshot(path=f"/tmp/{name}.png")
        Image.open(f"/tmp/{name}.png").convert("RGB").save(f"{OUT}/{name}.jpg", quality=92)
    b.close()
