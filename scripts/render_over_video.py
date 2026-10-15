"""Native Reel text over a real stock video clip.
usage: python3 scripts/render_over_video.py <cfg name> <clip.mp4> <out.mp4> <secs> [start_sec] [dim 0-1]
The config (templates/reel/native/<cfg>.js) must use bg:'clear'. The clip is center-cropped to 9:16 (1080x1920),
trimmed from start_sec, looped if shorter, darkened by dim (default .25) so white stickers stay readable,
then the transparent text frames are laid on top. Output is silent: run scripts/add_music.py after.
Clips: clips/stock/ (free Mixkit license, see clips/stock/README.md). Never post a clip without our own text on it."""
import sys, os, subprocess, tempfile, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
cfg, clip, out, secs = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4])
start = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0
dim = float(sys.argv[6]) if len(sys.argv) > 6 else 0.25
fps = 30
tmp = tempfile.mkdtemp()
page = ROOT / "templates/reel/native-reel.html"
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto(f"file://{page}?cfg={cfg}"); pg.wait_for_timeout(1500)
    for i in range(int(secs * fps)):
        pg.evaluate(f"setT({i * 1000 / fps})")
        pg.screenshot(path=f"{tmp}/f{i:05d}.png", omit_background=True)
    b.close()
vf = (f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps={fps},"
      f"eq=brightness={-dim * 0.35:.3f}:saturation=1.05,trim=0:{secs},setpts=PTS-STARTPTS[bg];"
      f"[bg][1:v]overlay=0:0:format=auto[v]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-stream_loop", "-1", "-ss", str(start), "-i", clip,
                "-framerate", str(fps), "-i", f"{tmp}/f%05d.png", "-filter_complex", vf, "-map", "[v]",
                "-t", str(secs), "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-movflags", "+faststart", out], check=True)
print("ok", out)
