"""FreshlyMadeFL free cheat-sheet pins (1000x1500). Copy, replace GUIDES with NEW topics (never re-render an old one), run, LOOK at every PNG."""
import os, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pinterest/tools"))
from themes import THEMES
from playwright.sync_api import sync_playwright
from PIL import Image

W, H = 1000, 1500
OUT = os.environ.get("OUT", str(ROOT / "pinterest/freshlymadefl"))
os.makedirs(OUT, exist_ok=True)


def checklist(items, cols=2):
    lis = "".join(f'<li><span class="box"></span><span>{i}</span></li>' for i in items)
    return f'<ul class="check c{cols}">{lis}</ul>'


def sections(secs):
    out = ""
    for title, items in secs:
        out += f'<div class="sec">{title}</div>' + checklist(items, 2)
    return out


def steps(items):
    lis = "".join(f'<li><span class="num">{n}</span><span>{t}</span></li>' for n, t in enumerate(items, 1))
    return f'<ol class="steps">{lis}</ol>'


def table(rows, head=None):
    h = f'<tr><th>{head[0]}</th><th>{head[1]}</th></tr>' if head else ""
    r = "".join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in rows)
    return f'<table class="tbl">{h}{r}</table>'


def formula(lines, result):
    out = ""
    for i, (op, a, b) in enumerate(lines):
        out += f'<div class="fl"><span class="op">{op}</span><span class="fa">{a}</span><span class="fb">{b}</span></div>'
    out += f'<div class="fres"><span class="fa">{result[0]}</span><span class="fb">{result[1]}</span></div>'
    return out


def example(title, rows):
    r = "".join(f'<div class="exr"><span>{a}</span><b>{b}</b></div>' for a, b in rows)
    return f'<div class="ex"><div class="ext">{title}</div>{r}</div>'


def note(t):
    return f'<div class="note">{t}</div>'


GUIDES = [
    ("g01_fsa_items", "blush", "FSA Eligible", "Items Checklist", "Commonly covered things to buy before your deadline",
     sections([
         ("Medicine cabinet", ["Pain relievers", "Allergy medicine", "Cold &amp; flu medicine", "Antacids",
                               "Thermometer", "First aid kit", "Bandages", "Heating pad"]),
         ("Personal care", ["Sunscreen, SPF 15+", "Period products", "Acne treatment", "Contact lens solution",
                            "Reading glasses", "Blood pressure cuff"]),
         ("Appointments", ["Copays &amp; deductibles", "Dental cleanings", "Eye exams",
                           "Glasses &amp; contacts", "Prescriptions", "Physical therapy"]),
     ]) + note("Rules vary by plan. Check with yours before you buy.")),

    ("g02_fsa_yearend", "blush", "FSA Year-End", "Checklist", "Use your money before it's gone",
     steps(["Find your plan's deadline (it's not always Dec 31)",
            "Ask if your plan has a grace period or carryover",
            "Look up your current balance",
            "Book eye, dental and doctor visits now",
            "Restock eligible medicine cabinet items",
            "Order new glasses or contacts",
            "Submit claims for anything you paid out of pocket",
            "Save every receipt"])),

    ("g03_sinking_ideas", "sage", "Sinking Fund", "Ideas", "20 expenses that sneak up every year",
     checklist(["Christmas &amp; holidays", "Birthdays", "Car repairs", "Car registration", "Car insurance",
                "Vacation", "Back to school", "Pet care &amp; vet", "Medical bills", "Home repairs",
                "Yearly subscriptions", "Clothing", "Gifts", "Weddings &amp; showers", "Kids' activities",
                "Hair &amp; beauty", "New phone", "Furniture", "Taxes", "Emergency fund"], 2)),

    ("g04_sinking_formula", "sage", "How Much to Save", "Per Paycheck", "One simple formula for every savings goal",
     formula([("", "Goal amount", "$600"), ("÷", "Paychecks left", "26")], ("Save per paycheck", "$23.08"))
     + example("Example: Christmas fund", [("Goal", "$600"), ("Paid every 2 weeks for a year", "26 paychecks"),
                                           ("$600 ÷ 26", "$23.08 per paycheck")])),

    ("g05_paychecks", "sage", "Paychecks", "Per Year", "Know your number before you budget",
     table([("Weekly", "52"), ("Every 2 weeks", "26*"), ("Twice a month", "24"), ("Monthly", "12")],
           ("If you're paid…", "Paychecks a year"))
     + example("Bonus for every-2-weeks pay", [("Most months", "2 paychecks"), ("2 months a year", "3 paychecks")])
     + note("*Some years have 27. Check your pay calendar.")),

    ("g06_baking_conv", "peach", "Baking", "Conversions", "Screenshot this for your next bake",
     '<div class="two">' + table([("3 tsp", "1 tbsp"), ("4 tbsp", "¼ cup"), ("5 tbsp + 1 tsp", "⅓ cup"), ("8 tbsp", "½ cup"),
            ("16 tbsp", "1 cup")]) + table([("1 cup", "8 fl oz"), ("2 cups", "1 pint"), ("4 cups", "1 quart"),
            ("4 quarts", "1 gallon"), ("1 lb", "16 oz")]) + '</div>'
     + example("Butter", [("1 stick", "½ cup · 8 tbsp · 4 oz · 113 g"), ("4 sticks", "1 lb · 2 cups")])),

    ("g07_cake_price", "peach", "How to Price", "Your Bakes", "The formula home bakers forget",
     formula([("", "Ingredients", ""), ("+", "Packaging", "boxes, boards, liners"),
              ("+", "Your time", "hours × your hourly pay"), ("+", "Overhead", "power, equipment, fees")],
             ("Your price", ""))
     + '<div class="sec">Often forgotten</div>'
     + checklist(["Cake boards", "Boxes", "Piping bags", "Sprinkles", "Cleanup time", "Delivery gas",
                  "Card fees", "Test bakes"], 2)),

    ("g08_candle_costs", "honey", "Candle Costs", "Checklist", "Count every one of these in your price",
     checklist(["Wax", "Fragrance oil", "Wick", "Wick sticker", "Jar or tin", "Lid", "Dye", "Front label",
                "Warning label", "Gift box or bag", "Shipping box", "Box filler", "Test batches", "Your time",
                "Market fees", "Selling fees"], 2)),

    ("g09_candle_wholesale", "honey", "Retail vs.", "Wholesale", "Check this before a shop places an order",
     steps(["Add up your cost per candle: supplies, time and overhead",
            "Set your retail price",
            "Wholesale is usually half of retail",
            "Wholesale minus cost has to be more than $0"])
     + example("Example: 8 oz candle", [("Cost per candle", "$7.00"), ("Retail price", "$17.00"),
                                        ("Wholesale (half)", "$8.50"), ("Profit per wholesale candle", "$1.50")])),

    ("g10_order_questions", "lavender", "Custom Order", "Questions", "Ask these before you say yes",
     checklist(["Name and best way to reach them", "What they want and how many", "Sizes and colors",
                "Exact wording (check spelling!)", "Due date and time", "Pickup, delivery or shipping",
                "Allergies or things to avoid", "Price and deposit amount", "When the balance is due",
                "Photos of styles they like"], 1)),

    ("g11_expense_categories", "sky", "Business Expense", "Categories", "Sort every receipt into one of these",
     checklist(["Materials &amp; supplies", "Packaging", "Shipping &amp; postage", "Selling fees",
                "Payment processing fees", "Advertising", "Software &amp; apps", "Equipment &amp; tools",
                "Booth &amp; market fees", "Classes &amp; education", "Office supplies", "Phone &amp; internet"], 1)
     + note("Ask a tax pro what you can deduct.")),

    ("g12_profit", "sky", "Sales vs.", "Profit", "What your business really keeps",
     formula([("", "Sales", "$1,000"), ("−", "Cost of goods", "$250")], ("Gross profit", "$750"))
     + formula([("", "Gross profit", "$750"), ("−", "Expenses", "$150")], ("Net profit", "$600"))
     + formula([("", "Net profit", "$600"), ("÷", "Sales", "$1,000")], ("Profit margin", "60%"))),
]

STAR = ('<svg style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px" viewBox="0 0 100 100">'
        '<path d="M50 0 C55 38 62 45 100 50 C62 55 55 62 50 100 C45 62 38 55 0 50 C38 45 45 38 50 0Z" fill="{c}"/></svg>')


def page(t, l1, l2, sub, body):
    return f"""<html><head><style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:{W}px;height:{H}px;overflow:hidden;background:{t['bg']};font-family:Inter,sans-serif;position:relative;color:{t['text']}}}
.blob{{position:absolute;border-radius:50%;background:rgba(255,255,255,.45)}}
.top{{position:absolute;left:0;right:0;top:56px;text-align:center;padding:0 50px}}
.pill{{display:inline-block;background:{t['pill']};color:{t['ink']};font-weight:800;font-size:26px;letter-spacing:3px;padding:10px 28px;border-radius:50px}}
.h{{font-family:Poppins,sans-serif;font-weight:800;line-height:1.0;letter-spacing:-3px;white-space:nowrap}}
.l1{{color:{t['ink']};margin-top:22px}} .l2{{color:{t['pop']}}}
.sub{{color:{t['ink']};font-size:34px;font-weight:600;margin-top:16px}}
.card{{position:absolute;left:50px;right:50px;background:#fff;border:4px solid {t['ink']};border-radius:34px;
 padding:1.3em 1.5em;box-shadow:0 18px 44px rgba(40,25,30,.14);font-size:34px}}
.sec{{font-family:Poppins;font-weight:800;color:{t['pop']};font-size:.8em;letter-spacing:2px;text-transform:uppercase;margin:.7em 0 .35em}}
.sec:first-child{{margin-top:0}}
ul.check{{list-style:none;display:grid;column-gap:1em;row-gap:.45em}}
ul.c2{{grid-template-columns:1fr 1fr}} ul.c1{{grid-template-columns:1fr}}
ul.check li{{display:flex;align-items:center;gap:.5em;font-weight:500;line-height:1.2}}
.box{{flex:none;width:1em;height:1em;border:3px solid {t['ink']};border-radius:50%}}
ol.steps{{list-style:none;display:grid;row-gap:.55em}}
ol.steps li{{display:flex;align-items:center;gap:.6em;font-weight:500;line-height:1.25}}
.num{{flex:none;width:1.6em;height:1.6em;border-radius:50%;background:{t['ink']};color:#fff;font-family:Poppins;font-weight:800;
 display:flex;align-items:center;justify-content:center;font-size:.85em}}
table.tbl{{width:100%;border-collapse:collapse;font-size:1.05em}}
.tbl th{{background:{t['ink']};color:#fff;font-weight:700;padding:.45em .7em;text-align:left;font-size:.8em}}
.tbl th:first-child{{border-radius:14px 0 0 14px}} .tbl th:last-child{{border-radius:0 14px 14px 0;text-align:right}}
.tbl td{{padding:.38em .7em;border-bottom:3px solid {t['line']};font-weight:600}}
.tbl td:last-child{{text-align:right;color:{t['ink']};font-weight:800;font-family:Poppins}}
.fl,.fres{{display:flex;align-items:baseline;gap:.5em;padding:.32em 0;border-bottom:3px solid {t['line']}}}
.op{{width:1em;font-family:Poppins;font-weight:800;color:{t['pop']};font-size:1.2em}}
.fl .fa{{font-weight:700;color:{t['ink']}}} .fl .fb{{margin-left:auto;font-weight:600;color:#666;font-size:.85em}}
.fres{{background:{t['ink']};color:#fff;border-radius:18px;padding:.45em .7em;margin:.45em 0 .8em;border:none}}
.fres .fa{{font-weight:800}} .fres .fb{{margin-left:auto;font-family:Poppins;font-weight:800;color:{t['pill']};font-size:1.15em}}
.ex{{background:{t['tint']};border-radius:22px;padding:.7em .9em;margin-top:.6em}}
.ext{{font-family:Poppins;font-weight:800;color:{t['pop']};font-size:.75em;letter-spacing:2px;text-transform:uppercase;margin-bottom:.3em}}
.exr{{display:flex;justify-content:space-between;gap:1em;padding:.18em 0;font-weight:500}} .exr b{{color:{t['ink']};text-align:right}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:.8em}} .two table.tbl{{font-size:.85em}} .two td{{white-space:nowrap}}
.note{{margin-top:.8em;font-size:.68em;color:#666;font-style:italic;text-align:center}}
.foot{{position:absolute;left:0;right:0;bottom:46px;text-align:center;color:{t['ink']};font-size:24px;font-weight:800;letter-spacing:4px}}
</style></head><body>
<div class="blob" style="width:560px;height:560px;left:-240px;top:-250px"></div>
<div class="blob" style="width:520px;height:520px;right:-240px;bottom:-220px"></div>
{STAR.format(x=56, y=54, s=54, c=t['pop'])}{STAR.format(x=892, y=88, s=40, c=t['pill'])}
{STAR.format(x=900, y=1380, s=30, c='#fff')}{STAR.format(x=60, y=1390, s=26, c='#fff')}
<div class="top"><div class="pill">SAVE THIS CHEAT SHEET</div>
<div class="h l1" id="l1">{l1}</div><div class="h l2" id="l2">{l2}</div><div class="sub" id="sub">{sub}</div></div>
<div class="card" id="card">{body}</div>
<div class="foot">FRESHLYMADEFL</div>
<script>(function(){{
let s=130;const a=document.getElementById('l1'),b=document.getElementById('l2');
function set(v){{a.style.fontSize=v+'px';b.style.fontSize=v+'px';}} set(s);
while((a.scrollWidth>900||b.scrollWidth>900)&&s>60){{s-=2;set(s);}}
const card=document.getElementById('card');
const top=document.getElementById('sub').getBoundingClientRect().bottom+34;
const bottom={H}-110; card.style.top=top+'px';
let f=40; card.style.fontSize=f+'px';
while(card.getBoundingClientRect().height>bottom-top && f>18){{f-=1;card.style.fontSize=f+'px';}}
const h=card.getBoundingClientRect().height; card.style.top=(top+Math.max(0,(bottom-top-h)/2))+'px';
document.body.dataset.info=s+'/'+f;
}})();</script></body></html>"""


with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(viewport={"width": W, "height": H})
    for name, theme, l1, l2, sub, body in GUIDES:
        pg.set_content(page(THEMES[theme], l1, l2, sub, body))
        pg.wait_for_timeout(200)
        info = pg.evaluate("() => document.body.dataset.info")
        png = f"/tmp/{name}.png"
        pg.screenshot(path=png)
        Image.open(png).convert("RGB").save(f"{OUT}/{name}.jpg", quality=92)
        print(name, "headline/card font", info)
    br.close()
