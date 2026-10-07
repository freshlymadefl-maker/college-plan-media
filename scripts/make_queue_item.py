"""Build a newsletter/queue/*.json item for the beehiiv Create Post API.
usage: python3 scripts/make_queue_item.py meta.json body.html
meta.json keys: name (file name, no ext), title, subtitle, subject, preview, segment_id,
scheduled_at (ISO UTC, e.g. 2026-10-12T10:30:00Z), seo_title, seo_description, tags (list)
"""
import json, re, sys, pathlib

meta = json.loads(pathlib.Path(sys.argv[1]).read_text())
html = pathlib.Path(sys.argv[2]).read_text()
html = re.sub(r'\s*data-node-hash="[^"]*"', '', html)

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
    },
    "web_settings": {"display_thumbnail_on_web": False},
    "seo_settings": {
        "default_title": meta.get("seo_title", meta["title"]),
        "default_description": meta.get("seo_description", meta.get("preview", "")),
    },
    "content_tags": meta.get("tags", []),
}
out = pathlib.Path("newsletter/queue") / f"{meta['name']}.json"
out.write_text(json.dumps(body, indent=2))
print("queued", out)
