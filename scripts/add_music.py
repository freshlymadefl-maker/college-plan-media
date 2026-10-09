"""Put one of College Plan's own music tracks under a Reel/TikTok video that has NO voiceover.
usage: python3 scripts/add_music.py in.mp4 out.mp4 [sunny|breeze|bright]
Tracks live in templates/reel/music/ (made by scripts/make_music.py; original, no licensing).
If no track is named, one is picked from the file name so tracks rotate.
Never use this on voiceover videos."""
import sys, subprocess, pathlib, zlib
root = pathlib.Path(__file__).resolve().parent.parent
tracks = sorted(p.stem for p in (root / "templates/reel/music").glob("*.m4a"))
src, out = sys.argv[1], sys.argv[2]
name = sys.argv[3] if len(sys.argv) > 3 else tracks[zlib.crc32(pathlib.Path(out).stem.encode()) % len(tracks)]
music = root / "templates/reel/music" / f"{name}.m4a"
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src]).decode().strip())
fade = max(0.5, min(1.5, dur / 8))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-i", str(music), "-map", "0:v", "-map", "1:a",
                "-af", f"afade=t=in:d=0.3,afade=t=out:st={dur - fade:.2f}:d={fade:.2f},volume=0.8",
                "-t", f"{dur:.2f}", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out], check=True)
print("ok", out, "music:", name)
