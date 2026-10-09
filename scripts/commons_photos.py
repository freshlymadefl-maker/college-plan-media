"""Find freely licensed photos on Wikimedia Commons and save them with credits.
Runs in the "Find photos" GitHub Action (the Claude sandbox can't reach Commons directly).
Request file: photoreq/<anything>.txt, one request per line:
    <slug> | <search terms> [| <max images, default 6>]
e.g.  uf-stadium | Ben Hill Griffin Stadium | 6
Output: photos/commons/<slug>/<n>.jpg (1600px wide), credits.json (title, artist, license, source page),
        and contact.jpg (numbered thumbnails so Claude can pick the best ones by looking).
Only licenses that allow commercial reuse with credit: CC0, Public domain, CC BY, CC BY-SA. No NC/ND, no fair use."""
import json, pathlib, re, sys, time, urllib.parse, urllib.request
from io import BytesIO
from PIL import Image, ImageDraw

UA = "CollegePlanPhotoBot/1.0 (https://collegeplan.beehiiv.com; freshlymadefl@gmail.com)"
API = "https://commons.wikimedia.org/w/api.php"
OK = re.compile(r"^(cc0|public domain|pd|cc by(-sa)? ?\d(\.\d)?)", re.I)
BAD = re.compile(r"(nc|nd|fair use|non-free)", re.I)
root = pathlib.Path(__file__).resolve().parent.parent

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def strip(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html or "")).strip()

def search(q, limit):
    params = {"action": "query", "format": "json", "generator": "search", "gsrsearch": f"{q} filetype:bitmap",
              "gsrnamespace": "6", "gsrlimit": str(max(limit * 4, 20)), "prop": "imageinfo",
              "iiprop": "url|size|extmetadata|mime", "iiurlwidth": "1600"}
    data = json.loads(get(API + "?" + urllib.parse.urlencode(params)))
    pages = sorted(data.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 999))
    out = []
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]; md = ii.get("extmetadata", {})
        lic = strip(md.get("LicenseShortName", {}).get("value", ""))
        if not OK.match(lic) or BAD.search(lic): continue
        if ii.get("mime") not in ("image/jpeg", "image/png"): continue
        if ii.get("width", 0) < 1200 or ii.get("height", 0) < 800: continue
        out.append({"title": p["title"], "thumb": ii.get("thumburl") or ii["url"], "page": ii.get("descriptionurl"),
                    "artist": strip(md.get("Artist", {}).get("value", "")) or "Unknown",
                    "license": lic, "width": ii["width"], "height": ii["height"]})
        if len(out) >= limit: break
    return out

def contact(folder, n):
    ims = [Image.open(folder / f"{i}.jpg").convert("RGB") for i in range(1, n + 1)]
    W, H = 400, 300; cols = 3; rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * W, rows * H), "white"); d = ImageDraw.Draw(sheet)
    for k, im in enumerate(ims):
        im.thumbnail((W - 10, H - 10)); x, y = (k % cols) * W + 5, (k // cols) * H + 5
        sheet.paste(im, (x, y)); d.rectangle([x, y, x + 46, y + 40], fill="black"); d.text((x + 14, y + 10), str(k + 1), fill="white")
    sheet.save(folder / "contact.jpg", quality=85)

for req in sorted((root / "photoreq").glob("*.txt")):
    for line in req.read_text().splitlines():
        if not line.strip() or line.startswith("#"): continue
        parts = [x.strip() for x in line.split("|")]
        slug, q = parts[0], parts[1]; limit = int(parts[2]) if len(parts) > 2 and parts[2] else 6
        folder = root / "photos/commons" / slug; folder.mkdir(parents=True, exist_ok=True)
        try:
            found = search(q, limit)
        except Exception as e:
            print("search failed", slug, e); continue
        credits = []
        for i, f in enumerate(found, 1):
            try:
                im = Image.open(BytesIO(get(f["thumb"]))).convert("RGB")
                im.save(folder / f"{i}.jpg", quality=90); credits.append({"file": f"{i}.jpg", **f})
                time.sleep(0.5)
            except Exception as e:
                print("download failed", f["title"], e)
        # renumber if any failed
        for k, c in enumerate(credits, 1):
            if c["file"] != f"{k}.jpg":
                (folder / c["file"]).rename(folder / f"{k}.jpg"); c["file"] = f"{k}.jpg"
        (folder / "credits.json").write_text(json.dumps({"query": q, "photos": credits}, indent=1))
        if credits: contact(folder, len(credits))
        print(slug, len(credits), "photos")
    req.unlink()
