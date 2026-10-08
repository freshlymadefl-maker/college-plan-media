"""Posts every newsletter/queue/*.json to the beehiiv Create Post API (scheduled send).
Each JSON file is the request body (title, body_content, status "confirmed", scheduled_at,
recipients, email_settings, seo_settings, post_template_id, content_tags ...).
Success -> moved to newsletter/sent/ with the API response; failure -> newsletter/failed/ with the error."""
import json, os, pathlib, sys, urllib.request, urllib.error

PUB = "pub_851868ac-cd7b-4156-a1a0-dfac96c6e363"
KEY = os.environ.get("BEEHIIV_API_KEY", "").strip()
if not KEY:
    print("BEEHIIV_API_KEY secret is missing; leaving queue untouched"); sys.exit(0)

root = pathlib.Path("newsletter")
files = sorted(p for p in (root / "queue").glob("*.json"))
if not files:
    print("queue empty"); sys.exit(0)

import re


def image_ok(url):
    """Download the whole image and check it isn't truncated/corrupt (the Oct 8 banner was)."""
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as r:
            data = r.read(); ctype = r.headers.get("Content-Type", "")
    except Exception as e:
        return False, str(e)
    if len(data) < 2000 or not ctype.startswith("image/"):
        return False, f"type {ctype}, {len(data)} bytes"
    if data[:2] == b"\xff\xd8" and not data.rstrip(b"\x00").endswith(b"\xff\xd9"):
        return False, "truncated JPEG"
    if data[:8] == b"\x89PNG\r\n\x1a\n" and b"IEND" not in data[-32:]:
        return False, "truncated PNG"
    return True, ""


def check_images(body):
    html = body.get("body_content", "")
    notes = []
    for m in list(re.finditer(r'<img[^>]+src="([^"]+)"[^>]*>', html)):
        ok, why = image_ok(m.group(1))
        if not ok:
            if "/brand/email/" in m.group(1):
                raise RuntimeError(f"header banner broken: {m.group(1)} ({why})")
            html = html.replace(m.group(0), "")   # drop a broken inline image rather than send it
            notes.append(f"removed broken image {m.group(1)} ({why})")
    body["body_content"] = html
    return notes


bad = 0
for f in files:
    body = json.loads(f.read_text())
    if body.get("_action") == "delete":   # {"_action": "delete", "post_id": "post_..."} archives/unschedules a post
        req = urllib.request.Request(
            f"https://api.beehiiv.com/v2/publications/{PUB}/posts/{body['post_id']}", method="DELETE",
            headers={"Authorization": f"Bearer {KEY}"})
    else:
        try:
            for n in check_images(body):
                print("NOTE", f.name, n)
        except RuntimeError as e:
            bad += 1
            (root / "failed" / f.name).write_text(json.dumps({"request": body, "status": 0, "error": str(e)}, indent=2))
            print("FAILED", f.name, e); f.unlink(); continue
        req = urllib.request.Request(
            f"https://api.beehiiv.com/v2/publications/{PUB}/posts",
            data=json.dumps(body).encode(), method="POST",
            headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            resp = json.loads(r.read() or b"{}")
        out = {"request": body, "response": resp}
        (root / "sent" / f.name).write_text(json.dumps(out, indent=2))
        print("scheduled", f.name, resp.get("data", {}).get("id"), resp.get("data", {}).get("status"))
    except urllib.error.HTTPError as e:
        bad += 1
        err = e.read().decode(errors="replace")
        (root / "failed" / f.name).write_text(json.dumps({"request": body, "status": e.code, "error": err}, indent=2))
        print("FAILED", f.name, e.code, err[:500])
    f.unlink()
sys.exit(1 if bad else 0)
