"""Build social/feed.json from Metricool Instagram post rows.
usage: python3 scripts/update_social_feed.py rows.json
rows.json = the "rows" array from Metricool getAnalyticsDataByMetrics with metrics
            ["IGPO02","IGPO03","IGPO05","IGPO06","IGPO07"] (date, caption, image url, post url, type).
Writes fetch/social.txt for images not yet saved (the Fetch images action downloads them to social/img/),
and social/feed.json (newest first, max 8). The website widget tools/social-feed.js reads feed.json."""
import json, sys, pathlib, re, datetime
rows = json.load(open(sys.argv[1]))
if isinstance(rows, dict): rows = rows.get("rows", [])
root = pathlib.Path(__file__).resolve().parent.parent
posts, fetch = [], []
for r in rows:
    date, caption, img, url, typ = (r + [None] * 5)[:5]
    if not url or not img: continue
    code = re.search(r"/(?:p|reel)/([^/]+)/", url)
    code = code.group(1) if code else re.sub(r"\W", "", url)[-12:]
    dest = f"social/img/{code}.jpg"
    if not (root / dest).exists(): fetch.append(f"{dest} {img}")
    first = (caption or "").strip().split("\n")[0][:140]
    d = datetime.datetime.strptime(str(date)[:8], "%Y%m%d").strftime("%b %-d")
    posts.append({"url": url, "img": dest, "date": str(date), "label": d, "caption": first, "type": typ or ""})
posts.sort(key=lambda p: p["date"], reverse=True)
feed = {"updated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "instagram": "https://www.instagram.com/college.plan/",
        "facebook": "https://www.facebook.com/1362425533621807", "posts": posts[:8]}
(root / "social").mkdir(exist_ok=True)
(root / "social/feed.json").write_text(json.dumps(feed, indent=1))
if fetch:
    (root / "fetch").mkdir(exist_ok=True)
    (root / "fetch/social.txt").write_text("\n".join(fetch) + "\n")
print(len(posts[:8]), "posts;", len(fetch), "images to fetch")
