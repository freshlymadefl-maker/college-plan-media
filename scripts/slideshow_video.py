"""Turn carousel slides (1080x1350 PNGs) into a 1080x1920 TikTok/Reel slideshow video with music.
TikTok photo posts got 0 views in Metricool (Oct 13 check) while videos got 13-46, so TikTok gets videos.
usage: python3 scripts/slideshow_video.py out.mp4 secs_per_slide slide1.png slide2.png ...
Each slide sits on a blurred, darkened copy of itself with a slow zoom; first slide is fully visible on frame 0."""
import sys, subprocess, tempfile, os, pathlib
out, per, slides = sys.argv[1], float(sys.argv[2]), sys.argv[3:]
tmp = tempfile.mkdtemp(); clips = []
for i, s in enumerate(slides):
    c = f"{tmp}/c{i}.mp4"; n = int(per * 30)
    vf = (f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:2,eq=brightness=-0.12[bg];"
          f"[0:v]scale=1080:-1,zoompan=z='1+0.0006*on':d={n}:s=1080x1350:fps=30[fg];"
          f"[bg][fg]overlay=0:(H-h)/2-40,format=yuv420p")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", str(per), "-i", s, "-filter_complex", vf,
                    "-t", str(per), "-r", "30", "-c:v", "libx264", "-crf", "20", c], check=True); clips.append(c)
lst = f"{tmp}/l.txt"; open(lst, "w").write("".join(f"file '{c}'\n" for c in clips))
silent = f"{tmp}/s.mp4"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", silent], check=True)
root = pathlib.Path(__file__).resolve().parent
subprocess.run(["python3", str(root / "add_music.py"), silent, out], check=True)
