"""tts/<name>.txt (first line may be 'voice: en-US-AvaNeural') -> tts/out/<name>.mp3 + <name>.words.json
(word timings in ms, for word-by-word captions). Runs in the TTS GitHub Action (edge-tts needs internet)."""
import asyncio, json, pathlib, sys
import edge_tts

async def one(txt: pathlib.Path):
    lines = txt.read_text().strip().splitlines()
    voice, rate = "en-US-AvaNeural", "+4%"
    while lines and ":" in lines[0] and lines[0].split(":")[0].strip() in ("voice", "rate"):
        k, v = lines.pop(0).split(":", 1)
        if k.strip() == "voice": voice = v.strip()
        else: rate = v.strip()
    text = " ".join(l.strip() for l in lines if l.strip())
    out = pathlib.Path("tts/out"); out.mkdir(parents=True, exist_ok=True)
    try:
        com = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
    except TypeError:
        com = edge_tts.Communicate(text, voice, rate=rate)
    words, audio = [], bytearray()
    async for ch in com.stream():
        if ch["type"] == "audio":
            audio += ch["data"]
        elif ch["type"] == "WordBoundary":
            words.append({"t": ch["offset"] / 10000, "d": ch["duration"] / 10000, "w": ch["text"]})
    (out / f"{txt.stem}.mp3").write_bytes(bytes(audio))
    (out / f"{txt.stem}.words.json").write_text(json.dumps({"voice": voice, "text": text, "words": words}, indent=1))
    print(txt.stem, voice, len(words), "words")

async def main():
    for t in sorted(pathlib.Path("tts").glob("*.txt")):
        await one(t)
        t.unlink()

asyncio.run(main())
