"""Generate College Plan's own background music (original, synthesized here, so no licensing issues).
usage: python3 scripts/make_music.py   -> templates/reel/music/<name>.wav (60s each, 44.1kHz stereo)
Tracks: sunny (upbeat pop pluck), breeze (chill lofi), bright (light acoustic-style strum)."""
import numpy as np, pathlib, wave
SR = 44100
OUT = pathlib.Path(__file__).resolve().parent.parent / "templates/reel/music"

def note(n):  # MIDI -> Hz
    return 440.0 * 2 ** ((n - 69) / 12)

def env(length, a=0.005, d=0.3, s=0.0, r=0.05):
    t = np.arange(length) / SR
    e = np.minimum(1, t / a) * (s + (1 - s) * np.exp(-t / d))
    rl = int(r * SR)
    if rl and rl < length:
        e[-rl:] *= np.linspace(1, 0, rl)
    return e

def tone(f, length, harm=(1, .5, .25, .12), detune=0.0):
    t = np.arange(length) / SR
    y = sum(a * np.sin(2 * np.pi * f * (k + 1) * t * (1 + detune)) for k, a in enumerate(harm))
    return y / sum(harm)

def lowpass(x, cut):
    from scipy.signal import lfilter
    a = np.exp(-2 * np.pi * cut / SR)
    return lfilter([1 - a], [1, -a], x)

def add(buf, x, start):
    s = int(start * SR); e = min(len(buf), s + len(x))
    if s < len(buf): buf[s:e] += x[: e - s]

def kick(length=0.35):
    n = int(length * SR); t = np.arange(n) / SR
    f = 120 * np.exp(-t * 18) + 45
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)

def hat(length=0.06, rng=np.random.default_rng(1)):
    n = int(length * SR); x = rng.standard_normal(n)
    x = x - lowpass(x, 6000)  # crude highpass
    return x * np.exp(-np.arange(n) / SR * 60) * 0.5

def snare_soft(length=0.18, rng=np.random.default_rng(2)):
    n = int(length * SR); x = rng.standard_normal(n)
    x = lowpass(x, 5000) - lowpass(x, 900)
    return x * np.exp(-np.arange(n) / SR * 22) * 0.6

def build(name, bpm, prog, pattern, pluck_harm, pad_cut, drums, seconds=60, swing=0.0, root=60):
    beat = 60 / bpm; bar = 4 * beat
    L = int(seconds * SR); mix = np.zeros(L); pad = np.zeros(L); bass = np.zeros(L); dr = np.zeros(L)
    nbars = int(seconds / bar) + 1
    for b in range(nbars):
        chord = prog[b % len(prog)]; t0 = b * bar
        # pad: sustained chord
        for n in chord:
            x = tone(note(root + n), int(bar * SR), harm=(1, .3, .1), detune=0.002) + tone(note(root + n), int(bar * SR), harm=(1, .3, .1), detune=-0.002)
            add(pad, x * env(len(x), a=0.4, d=9, s=0.6, r=0.3) * 0.12, t0)
        # bass: root on beats 1 and 3
        for k in (0, 2):
            x = tone(note(root - 24 + chord[0]), int(beat * 1.8 * SR), harm=(1, .4, .1))
            add(bass, x * env(len(x), a=0.01, d=0.6, s=0.3, r=0.08) * 0.35, t0 + k * beat)
        # pluck arpeggio
        for i, step in enumerate(pattern):
            if step is None: continue
            tt = t0 + i * beat / 2 + (swing * beat / 2 if i % 2 else 0)
            n = chord[step % len(chord)] + 12 * (step // len(chord))
            x = tone(note(root + 12 + n), int(0.6 * SR), harm=pluck_harm)
            add(mix, x * env(len(x), a=0.003, d=0.18, r=0.05) * 0.22, tt)
        # drums
        if drums and b >= 1:
            for k in range(4):
                if k in (0, 2): add(dr, kick() * 0.55, t0 + k * beat)
                if k in (1, 3): add(dr, snare_soft() * 0.35, t0 + k * beat)
            for k in range(8):
                add(dr, hat() * (0.2 if k % 2 else 0.12), t0 + k * beat / 2 + (swing * beat / 2 if k % 2 else 0))
    pad = lowpass(pad, pad_cut)
    y = mix + pad + bass + dr
    # gentle fade in/out, normalize
    fi, fo = int(0.5 * SR), int(2.0 * SR)
    y[:fi] *= np.linspace(0, 1, fi); y[-fo:] *= np.linspace(1, 0, fo)
    y = np.tanh(y / (np.max(np.abs(y)) + 1e-9) * 1.2) * 0.85
    # simple stereo: slightly delayed copy for width
    d = int(0.012 * SR); r = np.concatenate([np.zeros(d), y[:-d]])
    st = np.stack([y * 0.9 + r * 0.1, r * 0.9 + y * 0.1], axis=1)
    OUT.mkdir(parents=True, exist_ok=True)
    with wave.open(str(OUT / f"{name}.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())
    print("wrote", OUT / f"{name}.wav")

if __name__ == "__main__":
    # chords as semitone offsets from root (C): I, V, vi, IV
    I, V, vi, IV = [0, 4, 7], [7, 11, 14], [9, 12, 16], [5, 9, 12]
    build("sunny", 104, [I, V, vi, IV], [0, 1, 2, 3, 2, 1, 0, 2], (1, .6, .3, .15, .08), 1800, True)
    build("breeze", 84, [[2, 5, 9, 12], [7, 11, 14, 17], [0, 4, 7, 11], [9, 12, 16, 19]],  # ii7 V7 Imaj7 vi7, lofi
          [0, None, 2, 1, 3, None, 2, None], (1, .2, .05), 1200, True, swing=0.18, root=57)
    build("bright", 112, [IV, I, V, vi], [0, 2, 1, 2, 0, 2, 1, 3], (1, .7, .45, .3, .2, .1), 2400, True, root=62)
