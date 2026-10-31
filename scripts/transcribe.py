import glob, os, traceback
try:
    from faster_whisper import WhisperModel
    m = WhisperModel("base.en", device="cpu", compute_type="int8")
    for f in glob.glob("transcribe/*.wav"):
        out = f[:-4] + ".txt"
        segs, _ = m.transcribe(f, vad_filter=False)
        with open(out, "w") as o:
            for s in segs: o.write(f"[{s.start:5.1f}-{s.end:5.1f}] {s.text.strip()}\n")
        os.remove(f)
except Exception:
    open("transcribe/error.log", "w").write(traceback.format_exc())
