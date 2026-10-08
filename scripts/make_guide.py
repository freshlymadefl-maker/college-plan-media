"""Build a newsletter/queue item that publishes a WEB-ONLY guide article (no email) on collegeplan.beehiiv.com.
usage: python3 scripts/make_guide.py guides/<slug>.meta.json guides/<slug>.html
meta: name, title, subtitle, slug, seo_title (<60), seo_description (<155), tags, faq (optional list of {question, answer})
Email targeting is set to the paid tier, which has no subscribers (the API requires an email audience),
so nobody is emailed. If a paid tier is ever added, revisit this.
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from make_queue_item import to_email_html, NAVY, HFONT

meta = json.loads(pathlib.Path(sys.argv[1]).read_text())
html = to_email_html(pathlib.Path(sys.argv[2]).read_text())
cta = (f'<div style="background:{NAVY};border-radius:12px;padding:22px 24px;margin:28px 0;text-align:center">'
       f'<p style="font-family:{HFONT};color:#ffffff;font-size:20px;font-weight:700;margin:0 0 6px">Get Florida college deadlines for your student\'s grade</p>'
       f'<p style="color:#C9DAEC;font-size:15px;margin:0 0 14px">Free weekly email + the Bright Futures Cheat Sheet.</p>'
       f'<a href="https://collegeplan.beehiiv.com" style="display:inline-block;background:#B5A21F;color:#ffffff;font-family:{HFONT};font-weight:600;'
       f'text-decoration:none;padding:12px 22px;border-radius:8px">Sign up free</a></div>')
html = html.replace("<!--CTA-->", cta) if "<!--CTA-->" in html else html + cta
body = {
    "title": meta["title"], "subtitle": meta.get("subtitle", ""), "body_content": html, "status": "confirmed",
    "recipients": {"web": {"tier_ids": ["free"]}, "email": {"tier_ids": ["premium"]}},
    "web_settings": {"slug": meta["slug"], "display_thumbnail_on_web": False},
    "seo_settings": {"default_title": meta["seo_title"], "default_description": meta["seo_description"]},
    "content_tags": meta.get("tags", []) + ["Guides"],
}
out = pathlib.Path("newsletter/queue") / f"guide-{meta['name']}.json"
out.write_text(json.dumps(body, indent=2)); print("queued", out)
