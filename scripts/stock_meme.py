"""Meme-style vertical video from a real stock clip (the 'relatable mom' format that gets reach).
Layout (1080x1920): white background, big caption on top, the clip in the middle, a punchline sticker that
pops in, an end card with ONE ask, small brand tag. Music is added after with scripts/add_music.py.

usage: python3 scripts/stock_meme.py config.json
config: {"clip": "clips/stock/<file>.mp4", "start": 0, "dur": 8,
         "top": "caption", "punch": "punchline", "punch_t": 3.2,
         "end": "end card text", "end_t": 5.8,
         "brand": "collegeplan" | "freshlymadefl", "out": "path/out-silent.mp4",
         optional "crop_x": pixels to shift the square crop right (+) or left (-) to keep the face in frame}
Stock clips live in clips/stock/ (Mixkit Stock Video Free License: commercial + social media use, no credit
needed; never post a clip on its own, always with our captions). Keep text out of the top 250px and bottom 300px.
"""
import json, os, subprocess, sys, tempfile, pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
BRANDS = {"collegeplan": {"ink": "#0B2A4A", "pill": "#FFE27A", "end_bg": "#0B2A4A", "end_fg": "#FFFFFF",
                          "logo": ROOT / "templates/wordmark_navy.png"},
          "freshlymadefl": {"ink": "#5B1E3C", "pill": "#FFE27A", "end_bg": "#E8457F", "end_fg": "#FFFFFF",
                            "logo": None, "tag": "FRESHLYMADEFL"}}


def wrap(draw, text, font, maxw):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split():
            t = (cur + " " + w).strip()
            if draw.textlength(t, font=font) <= maxw:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def text_block(text, size, fg, maxw, bg=None, pad=26, radius=26):
    font = ImageFont.truetype(FONT, size)
    d = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    lines = wrap(d, text, font, maxw - 2 * pad)
    lh = int(size * 1.22)
    tw = max(int(d.textlength(l, font=font)) for l in lines)
    im = Image.new("RGBA", (tw + 2 * pad, lh * len(lines) + 2 * pad), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    if bg:
        dr.rounded_rectangle((0, 0, im.width - 1, im.height - 1), radius=radius, fill=bg)
    for i, l in enumerate(lines):
        x = (im.width - dr.textlength(l, font=font)) / 2
        dr.text((x, pad + i * lh - int(size * 0.08)), l, font=font, fill=fg)
    return im


def main(cfg):
    b = BRANDS[cfg.get("brand", "collegeplan")]
    tmp = tempfile.mkdtemp()
    # caption layer (always on)
    cap = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    top = text_block(cfg["top"], cfg.get("top_size", 66), "#111111", 980)
    vy = cfg.get("video_y", 0)
    cap_y = 270
    cap.alpha_composite(top, ((W - top.width) // 2, cap_y))
    # brand tag right under the caption, then a square crop of the clip below it
    if b.get("logo"):
        lg = Image.open(b["logo"]).convert("RGBA")
        lg = lg.resize((200, int(200 * lg.height / lg.width)))
        cap.alpha_composite(lg, ((W - lg.width) // 2, cap_y + top.height + 6))
        tag_h = lg.height + 6
    else:
        tg = text_block(b["tag"], 24, b["ink"], 600, pad=4)
        cap.alpha_composite(tg, ((W - tg.width) // 2, cap_y + top.height + 6))
        tag_h = tg.height + 6
    video_y = vy or (cap_y + top.height + tag_h + 24)
    vh = W  # square
    cap.save(f"{tmp}/cap.png")
    punch = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if cfg.get("punch"):
        p = text_block(cfg["punch"], cfg.get("punch_size", 54), b["ink"], 940, bg=b["pill"])
        punch.alpha_composite(p, ((W - p.width) // 2, min(H - 330 - p.height, video_y + vh - p.height - 60)))
    punch.save(f"{tmp}/punch.png")
    end = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    e = text_block(cfg["end"], cfg.get("end_size", 52), b["end_fg"], 940, bg=b["end_bg"])
    end.alpha_composite(e, ((W - e.width) // 2, min(H - 330 - e.height, video_y + vh - e.height - 60)))
    end.save(f"{tmp}/end.png")
    dur = cfg.get("dur", 8)
    pt, et = cfg.get("punch_t", 3), cfg.get("end_t", dur - 2.2)
    clip = str(ROOT / cfg["clip"])
    fc = (f"color=white:s={W}x{H}:d={dur}[bg];"
          f"[0:v]trim=start={cfg.get('start', 0)}:duration={dur},setpts=PTS-STARTPTS,scale=-2:{vh},crop={W}:{vh}:(iw-{W})/2+{cfg.get('crop_x', 0)}:0[v];"
          f"[bg][v]overlay=0:{video_y}[a];[a][1:v]overlay=0:0[b];"
          f"[b][2:v]overlay=0:0:enable='between(t,{pt},{et})'[c];[c][3:v]overlay=0:0:enable='gte(t,{et})',format=yuv420p[out]")
    out = str(ROOT / cfg["out"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-stream_loop", "-1", "-i", clip,
                    "-loop", "1", "-i", f"{tmp}/cap.png", "-loop", "1", "-i", f"{tmp}/punch.png",
                    "-loop", "1", "-i", f"{tmp}/end.png", "-filter_complex", fc, "-map", "[out]",
                    "-t", str(dur), "-r", "30", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-an", out],
                   check=True)
    print("ok", out)


if __name__ == "__main__":
    main(json.load(open(sys.argv[1])))
