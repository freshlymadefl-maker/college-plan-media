"""Posts every newsletter/queue/*.json to the beehiiv Create Post API (scheduled send).
Each JSON file is the request body (title, body_content, status "confirmed", scheduled_at,
recipients, email_settings, seo_settings, post_template_id, content_tags ...).
Success -> moved to newsletter/sent/ with the API response; failure -> newsletter/failed/ with the error."""
import json, os, pathlib, sys, urllib.request, urllib.error

PUB = "pub_851868ac-cd7b-4156-a1a0-dfac96c6e363"
KEY = os.environ.get("BEEHIIV_API_KEY", "").strip()
if not KEY:
    print("BEEHIIV_API_KEY secret is missing"); sys.exit(1)

root = pathlib.Path("newsletter")
files = sorted(p for p in (root / "queue").glob("*.json"))
if not files:
    print("queue empty"); sys.exit(0)

bad = 0
for f in files:
    body = json.loads(f.read_text())
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
