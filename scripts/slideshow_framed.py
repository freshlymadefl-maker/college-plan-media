"""Carousel -> music slideshow Reel with a FRESH LOOK (Nov 9 owner direction: don't make every slideshow look the same).
usage: python3 scripts/slideshow_framed.py <style> out.mp4 secs_per_slide slide1.png slide2.png ...
style: scrap = kraft-paper background, slides as taped, slightly tilted photos (alternating tilt)
       block = bold color-block background (navy top / orange middle / gold bottom), slide as a flat card with a hard shadow
First slide is fully visible on frame 0. Music via scripts/add_music.py (Instagram library track goes on with audioConfiguration)."""
import sys, subprocess, tempfile, pathlib, random
from PIL import Image, ImageDraw, ImageFilter
style, out, per, slides = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4:]
W, H = 1080, 1920
tmp = pathlib.Path(tempfile.mkdtemp()); clips = []
random.seed(7)

def background():
    if style == 'block':
        bg = Image.new('RGB', (W, H), '#F05A28'); d = ImageDraw.Draw(bg)
        d.rectangle([0, 0, W, 420], fill='#0B2A4A'); d.rectangle([0, H - 380, W, H], fill='#F1E27A')
        return bg
    bg = Image.new('RGB', (W, H), '#C9A77C'); px = bg.load()
    for _ in range(60000):
        x, y = random.randrange(W), random.randrange(H); r, g, b = px[x, y]; k = random.randint(-14, 14)
        px[x, y] = (max(0, min(255, r + k)), max(0, min(255, g + k)), max(0, min(255, b + k)))
    return bg.filter(ImageFilter.GaussianBlur(0.6))

BG = background()
for i, s in enumerate(slides):
    sl = Image.open(s).convert('RGB'); sw = 900; sl = sl.resize((sw, int(sl.height * sw / sl.width)))
    fr = BG.copy()
    if style == 'block':
        sh = Image.new('RGB', sl.size, '#0B2A4A'); x, y = (W - sw) // 2, (H - sl.height) // 2 - 30
        fr.paste(sh, (x + 22, y + 22)); fr.paste(sl, (x, y))
    else:
        pad = 26; card = Image.new('RGB', (sl.width + 2 * pad, sl.height + 2 * pad + 40), '#FFFEF8'); card.paste(sl, (pad, pad))
        ang = 2.2 if i % 2 == 0 else -2.0
        card = card.convert('RGBA').rotate(ang, expand=True, resample=Image.BICUBIC)
        shadow = Image.new('RGBA', card.size, (0, 0, 0, 0)); shadow.paste((0, 0, 0, 90), mask=card.split()[3])
        shadow = shadow.filter(ImageFilter.GaussianBlur(14))
        x, y = (W - card.width) // 2, (H - card.height) // 2 - 30
        fr.paste(shadow, (x + 10, y + 16), shadow); fr.paste(card, (x, y), card)
        tape = Image.new('RGBA', (230, 64), (241, 226, 122, 190))
        for tx, ta in ((x + 70, 14), (x + card.width - 300, -10)):
            t = tape.rotate(ta, expand=True); fr.paste(t, (tx, y - 28), t)
    f = tmp / f'f{i}.png'; fr.save(f)
    c = tmp / f'c{i}.mp4'; n = int(per * 30)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-t', str(per), '-i', str(f), '-vf',
                    f"zoompan=z='1+0.0005*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps=30,format=yuv420p",
                    '-t', str(per), '-r', '30', '-c:v', 'libx264', '-crf', '20', str(c)], check=True); clips.append(c)
lst = tmp / 'l.txt'; lst.write_text(''.join(f"file '{c}'\n" for c in clips))
silent = tmp / 's.mp4'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', str(silent)], check=True)
subprocess.run(['python3', str(pathlib.Path(__file__).resolve().parent / 'add_music.py'), str(silent), out], check=True)
print('ok', out)
