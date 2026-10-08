# faster renderer for long JS-driven Reels: jpeg frames, setT only. usage: render-fast.py page.html out.mp4 secs fps [audio.mp3]
import sys, os, subprocess, tempfile
from playwright.sync_api import sync_playwright
src, out, secs, fps = sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4]); audio = sys.argv[5] if len(sys.argv) > 5 else None
tmp = tempfile.mkdtemp()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://' + os.path.abspath(src)); pg.wait_for_timeout(1500)
    for i in range(int(secs*fps)):
        pg.evaluate(f"setT({i*1000/fps})")
        pg.screenshot(path=f'{tmp}/f{i:05d}.jpg', type='jpeg', quality=90)
    b.close()
a = ['-i', audio] if audio else ['-f','lavfi','-i','anullsrc=r=44100:cl=stereo']
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',f'{tmp}/f%05d.jpg',*a,'-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-c:a','aac','-b:a','160k','-af','apad','-shortest','-movflags','+faststart',out], check=True)
print('ok', out)
