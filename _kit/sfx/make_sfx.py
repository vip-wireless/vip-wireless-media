"""Synthesize VIP Wireless Halloween sound effects (no samples, no licensing issues).

  python3 _kit/sfx/make_sfx.py          # writes _kit/sfx/*.wav (44.1 kHz mono)

Effects: drone (eerie bed), wind, flicker (light/electrical buzz + clicks), whoosh (ghost fly-by),
crack (glass/screen break), thunder, heartbeat, creak (door/floor), phone_buzz (vibration),
sting (scare hit), ding (notification / reveal).
"""
import numpy as np, wave, os
SR = 44100
OUT = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(7)

def t(sec): return np.arange(int(SR * sec)) / SR
def noise(sec): return rng.standard_normal(int(SR * sec))
def lp(x, a):  # one-pole low-pass, a in (0,1): smaller = darker
    y = np.empty_like(x); acc = 0.0; arr = np.ndim(a) > 0
    for i, v in enumerate(x): acc += (a[i] if arr else a) * (v - acc); y[i] = acc
    return y
def hp(x, a): return x - lp(x, a)
def env(n, att, rel):
    e = np.ones(n); a = int(att * SR); r = int(rel * SR)
    if a: e[:a] = np.linspace(0, 1, a)
    if r: e[-r:] *= np.linspace(1, 0, r)
    return e
def norm(x, peak=.9): return x / (np.max(np.abs(x)) + 1e-9) * peak
def save(name, x):
    x = np.clip(norm(x), -1, 1)
    with wave.open(os.path.join(OUT, name + ".wav"), "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())

def drone(sec=14):
    tt = t(sec); x = 0
    for f, d in [(55, .3), (55.7, .3), (82.4, .2), (110.9, .12), (164.8, .06)]:
        x = x + d * np.sin(2 * np.pi * f * tt + 2 * np.sin(2 * np.pi * .13 * tt))
    x += .15 * lp(noise(sec), .01) * (1 + .5 * np.sin(2 * np.pi * .2 * tt))
    return x * env(len(tt), 1.5, 1.5)

def wind(sec=6):
    tt = t(sec); n = noise(sec)
    gust = .5 + .5 * np.sin(2 * np.pi * .35 * tt) * np.sin(2 * np.pi * .11 * tt + 1)
    return lp(n, .02 + .04 * gust) * (0.3 + gust) * env(len(tt), .8, 1.2)

def flicker(sec=1.4):
    tt = t(sec); buzz = np.sign(np.sin(2 * np.pi * 120 * tt)) * .3 + np.sin(2 * np.pi * 60 * tt) * .3
    gate = np.zeros_like(tt); pos = 0
    while pos < len(tt):  # random on/off stutters
        on = int(rng.uniform(.02, .12) * SR); off = int(rng.uniform(.02, .15) * SR)
        gate[pos:pos + on] = 1; pos += on + off
    x = lp(buzz, .3) * gate
    clicks = np.zeros_like(tt); edges = np.where(np.diff(gate) != 0)[0]
    for e in edges: clicks[e:e + 200] += hp(noise(200 / SR), .5) * np.linspace(1, 0, 200)
    return x + clicks * .8

def whoosh(sec=1.3):
    tt = t(sec); n = noise(sec); y = np.empty_like(n); acc = 0.0
    a = .02 + .35 * np.sin(np.pi * tt / sec) ** 2  # filter sweeps open then closed
    for i, v in enumerate(n): acc += a[i] * (v - acc); y[i] = acc
    ghost = .25 * np.sin(2 * np.pi * (420 - 180 * tt / sec) * tt) * np.sin(np.pi * tt / sec) ** 3
    return (y + ghost) * np.sin(np.pi * tt / sec) ** 2

def crack(sec=1.2):
    tt = t(sec); x = np.zeros_like(tt)
    for k in range(9):  # cluster of sharp snaps
        s = int((k * .025 + rng.uniform(0, .03)) * SR); L = int(.06 * SR)
        x[s:s + L] += hp(noise(L / SR), .6) * np.exp(-np.linspace(0, 9, L)) * rng.uniform(.5, 1)
    tinkle = 0
    for f in rng.uniform(2500, 7000, 12):
        st = rng.uniform(.05, .4); seg = (tt > st) * np.exp(-(tt - st).clip(0) * 14)
        tinkle = tinkle + .12 * np.sin(2 * np.pi * f * tt) * seg
    thump = .7 * np.sin(2 * np.pi * 70 * tt) * np.exp(-tt * 18)
    return x + tinkle + thump

def thunder(sec=4):
    tt = t(sec); x = lp(noise(sec), .008) * np.exp(-tt * .9)
    x[: int(.08 * SR)] += hp(noise(.08), .3) * .6
    return x * (1 + .6 * np.sin(2 * np.pi * 3 * tt) * np.exp(-tt))

def heartbeat(sec=2.4, bpm=70):
    tt = t(sec); x = np.zeros_like(tt); per = 60 / bpm
    for b in np.arange(0, sec, per):
        for off, amp in [(0, 1), (.18, .7)]:
            s = b + off; seg = (tt >= s) * np.exp(-(tt - s).clip(0) * 25)
            x += amp * np.sin(2 * np.pi * 50 * (tt - s)) * seg
    return x

def creak(sec=1.6):
    tt = t(sec); f = 180 + 120 * np.sin(2 * np.pi * .6 * tt) + 40 * rng.standard_normal(len(tt)).cumsum() / 3000
    ph = 2 * np.cumsum(np.pi * f / SR); x = np.sign(np.sin(ph)) * (np.sin(2 * np.pi * 23 * tt) > 0)
    return lp(x, .2) * env(len(tt), .1, .3)

def phone_buzz(sec=1.2):
    tt = t(sec); x = np.sin(2 * np.pi * 150 * tt) * (np.sin(2 * np.pi * 2.5 * tt) > 0)
    return lp(x + .3 * np.sign(np.sin(2 * np.pi * 150 * tt)), .2)

def sting(sec=2.0):
    tt = t(sec); x = 0
    for f in [233, 247, 311, 466, 494]:
        x = x + np.sin(2 * np.pi * f * tt + .3 * np.sin(2 * np.pi * 6 * tt))
    return (x / 5 + .4 * lp(noise(sec), .05)) * np.exp(-tt * 1.6) * env(len(tt), .005, .2)

def ding(sec=1.2):
    tt = t(sec); return (np.sin(2 * np.pi * 1318 * tt) + .5 * np.sin(2 * np.pi * 1976 * tt)) * np.exp(-tt * 5)

if __name__ == "__main__":
    for fn in [drone, wind, flicker, whoosh, crack, thunder, heartbeat, creak, phone_buzz, sting, ding]:
        save(fn.__name__, fn()); print("wrote", fn.__name__ + ".wav")
