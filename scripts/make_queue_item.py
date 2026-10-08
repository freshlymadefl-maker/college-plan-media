"""Build a newsletter/queue/*.json item for the beehiiv Create Post API.
usage: python3 scripts/make_queue_item.py meta.json body.html
meta.json keys: name (file name, no ext), title, subtitle, subject, preview, segment_id,
scheduled_at (ISO UTC, e.g. 2026-10-12T10:30:00Z), seo_title, seo_description, tags (list), slug (optional)

The API stores body_content as one raw-HTML block, so beehiiv's editor theme does NOT style it.
This script converts our editor-style draft HTML (figure data-src banner, node-section boxes,
node-referralProgram) into email-safe HTML with inline styles in the College Plan look.
"""
import json, re, sys, pathlib

NAVY, INK, GOLD, MUTED = "#0B2A4A", "#2A3D54", "#B5A21F", "#5E7186"
FONT = "Inter, Helvetica, Arial, sans-serif"
HFONT = "Poppins, Helvetica, Arial, sans-serif"


def to_email_html(html: str) -> str:
    html = re.sub(r'\s*data-node-hash="[^"]*"', '', html)
    html = html.replace("{{first_name|there}}", "there")  # merge-tag fallbacks aren't parsed in raw HTML
    # banner image
    html = re.sub(r'<figure[^>]*data-src="([^"]+)"[^>]*?(?:data-alt="([^"]*)")?[^>]*>.*?</figure>',
                  lambda m: f'<img src="{m.group(1)}" alt="{m.group(2) or "College Plan"}" width="590" '
                            f'style="display:block;width:100%;max-width:590px;height:auto;border:0;border-radius:10px;margin:0 0 18px">',
                  html, flags=re.S)
    # section boxes
    html = re.sub(r'<div[^>]*class="node-section"[^>]*data-background-color="([^"]+)"[^>]*>|<div[^>]*data-background-color="([^"]+)"[^>]*class="node-section"[^>]*>',
                  lambda m: f'<div style="background:{m.group(1) or m.group(2)};border-radius:10px;padding:14px 20px;margin:18px 0">',
                  html)
    # referral block: merge tags don't work inside the API's raw-HTML block, so the personal share link
    # lives in the publication email footer instead ({{rp_refer_url}}). Drop the editor-only node here.
    html = re.sub(r'<div[^>]*class="node-referralProgram"[^>]*>\s*</div>', '', html)
    html = html.replace("Share your link below.", "Your personal share link is at the bottom of this email.")
    # one referral mention only: it lives in the email footer, so drop any P.S./divider in the body
    html = re.sub(r'<hr[^>]*>\s*<p[^>]*>\s*<strong>P\.S\.</strong>.*?</p>', '', html, flags=re.S)
    # typography
    html = re.sub(r'<h2>', f'<h2 style="font-family:{HFONT};color:{NAVY};font-size:21px;line-height:1.3;margin:26px 0 6px">', html)
    html = re.sub(r'<h3>', f'<h3 style="font-family:{HFONT};color:{NAVY};font-size:17px;line-height:1.3;margin:4px 0 6px">', html)
    html = re.sub(r'<p>', f'<p style="font-family:{FONT};color:{INK};font-size:16px;line-height:1.55;margin:10px 0">', html)
    html = re.sub(r'<ul>', f'<ul style="font-family:{FONT};color:{INK};font-size:16px;line-height:1.5;margin:8px 0;padding-left:22px">', html)
    html = re.sub(r'<li>\s*<p[^>]*>(.*?)</p>\s*</li>', r'<li style="margin:6px 0">\1</li>', html, flags=re.S)
    html = re.sub(r'<a (?![^>]*style=)', f'<a style="color:{NAVY};font-weight:600;text-decoration:underline;text-decoration-color:{GOLD}" ', html)
    html = re.sub(r'<hr>', f'<hr style="border:0;border-top:2px solid {GOLD};width:30%;margin:26px 0 10px">', html)
    return f'<div style="font-family:{FONT};color:{INK};max-width:590px;margin:0 auto">{html}</div>'


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:80]


if __name__ == "__main__":
    meta = json.loads(pathlib.Path(sys.argv[1]).read_text())
    html = to_email_html(pathlib.Path(sys.argv[2]).read_text())
    body = {
        "title": meta["title"],
        "subtitle": meta.get("subtitle", ""),
        "body_content": html,
        "status": "confirmed",
        "scheduled_at": meta["scheduled_at"],
        "post_template_id": "post_template_92da00b7-d6e0-447a-aded-93f586f22255",
        "recipients": {
            "web": {"tier_ids": ["free"]},
            "email": {"include_segment_ids": [meta["segment_id"]]},
        },
        "email_settings": {
            "email_subject_line": meta["subject"],
            "email_preview_text": meta["preview"],
            "display_title_in_email": False,
            "display_subtitle_in_email": False,
            "display_byline_in_email": False,
        },
        "web_settings": {"display_thumbnail_on_web": False, "slug": meta.get("slug") or slugify(meta["title"])},
        "seo_settings": {
            "default_title": meta.get("seo_title", meta["title"]),
            "default_description": meta.get("seo_description", meta.get("preview", "")),
        },
        "content_tags": meta.get("tags", []),
    }
    out = pathlib.Path("newsletter/queue") / f"{meta['name']}.json"
    out.write_text(json.dumps(body, indent=2))
    print("queued", out)
