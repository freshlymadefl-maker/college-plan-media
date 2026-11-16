import base64
from playwright.sync_api import sync_playwright
wm="data:image/png;base64,"+base64.b64encode(open('templates/wordmark_navy.png','rb').read()).decode()
items=["Wearable blanket hoodie","White noise machine","Reading pillow with arms","Lap desk for bed homework","Bedside caddy"]
li="".join(f'<li><span class="bx">✓</span>{i}</li>' for i in items)
snow="".join(f'<div style="position:absolute;left:{(i*233)%1080}px;top:{(i*397)%1920}px;width:{4+(i*37)%9}px;height:{4+(i*37)%9}px;border-radius:50%;background:#fff;opacity:.5"></div>' for i in range(50))
html=f"""<html><body style="margin:0;width:1080px;height:1920px;overflow:hidden;position:relative;font-family:Inter;background:radial-gradient(circle at 50% 30%,#2F6FA8,#0B2A4A)">{snow}
<div style="position:absolute;top:250px;left:0;right:0;text-align:center"><div style="display:inline-block;background:#9B1C1C;color:#fff;font-family:Poppins;font-weight:600;font-size:34px;letter-spacing:.12em;padding:14px 34px;border-radius:999px">🎁 GIFTS FOR COLLEGE KIDS</div>
<div style="font-family:Poppins;font-weight:700;color:#fff;font-size:100px;line-height:1.05;margin-top:40px">The cozy<br>dorm list</div>
<div style="font-family:Lora;font-style:italic;color:#E9C46A;font-size:64px;margin-top:16px">they'll use it every day</div></div>
<div style="position:absolute;top:820px;left:90px;right:90px;background:#FFFDF6;border-radius:34px;padding:56px 60px;box-shadow:0 20px 50px rgba(0,0,0,.35)">
<ul style="list-style:none;padding:0;margin:0;font-size:46px;color:#14382A;line-height:1.25">{li.replace('<li>','<li style="display:flex;gap:26px;align-items:flex-start;margin:16px 0">').replace('class="bx"','style="flex:none;width:58px;height:58px;border:5px solid #1E6B47;border-radius:12px;color:#9B1C1C;font-weight:800;font-size:46px;line-height:48px;text-align:center"')}</ul>
<div style="margin-top:30px;text-align:center"><img src="{wm}" style="height:46px"></div></div>
<div style="position:absolute;top:1530px;left:0;right:0;text-align:center"><div style="display:inline-block;background:#E9C46A;color:#0C3626;font-family:Poppins;font-weight:700;font-size:62px;padding:22px 54px;border-radius:999px">Gift lists: link in bio</div>
<div style="color:rgba(255,255,255,.8);font-size:28px;margin-top:40px">As an Amazon Associate I earn from qualifying purchases. #ad</div></div></body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1920});pg.set_content(html);pg.wait_for_timeout(400)
    pg.screenshot(path='instagram/2026-11-16-story-gift-lists/story.png');b.close()
