# usage: python3 render-reel.py reel.html out.mp4 [seconds=13] [fps=30] [music=auto|sunny|breeze|bright|none]
# Non-voiceover Reels get one of our own music tracks baked in (scripts/add_music.py) so TikTok + Facebook copies aren't silent.
# On Instagram, attach a library track via audioConfiguration with videoVolume 0 (see CONTENT-PLAN.md "Music").
import sys, os, subprocess, tempfile
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]
secs = float(sys.argv[3]) if len(sys.argv) > 3 else 13; fps = int(sys.argv[4]) if len(sys.argv) > 4 else 30
tmp = tempfile.mkdtemp()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://' + os.path.abspath(src)); pg.wait_for_timeout(1000)
    pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
    for i in range(int(secs*fps)):
        pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={i*1000/fps}); window.setT && window.setT({i*1000/fps})")
        pg.screenshot(path=f'{tmp}/f{i:04d}.png')
    b.close()
# silent AAC track so Instagram treats it as a normal video
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',f'{tmp}/f%04d.png','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-c:a','aac','-movflags','+faststart',out], check=True)
music = sys.argv[5] if len(sys.argv) > 5 else 'auto'
if music != 'none':
    here = os.path.dirname(os.path.abspath(__file__)); tmpout = out + '.music.mp4'
    cmd = ['python3', os.path.join(here, '..', '..', 'scripts', 'add_music.py'), out, tmpout] + ([] if music == 'auto' else [music])
    subprocess.run(cmd, check=True); os.replace(tmpout, out)
print('ok', out)
