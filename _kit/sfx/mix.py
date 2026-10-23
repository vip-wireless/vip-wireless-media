"""Mix timed sound effects into a rendered (silent) post video.

  python3 _kit/sfx/mix.py in.mp4 out.mp4 drone@0:0.35 flicker@0.6 whoosh@1.4 crack@2.2:1.0 ...

Each cue is name@seconds[:volume]; name is a wav in _kit/sfx (run make_sfx.py first).
Sync cues to the on-screen events (flicker with light flicker, crack when the screen breaks, etc.).
"""
import os, subprocess, sys
SFX = os.path.dirname(os.path.abspath(__file__))
src, out, cues = sys.argv[1], sys.argv[2], sys.argv[3:]
args = ["ffmpeg", "-y", "-loglevel", "error", "-i", src]; parts = []
for k, c in enumerate(cues):
    name, rest = c.split("@"); at, vol = (rest.split(":") + ["0.8"])[:2]
    args += ["-i", os.path.join(SFX, name + ".wav")]
    ms = int(float(at) * 1000)
    parts.append(f"[{k+1}:a]adelay={ms}|{ms},volume={vol}[a{k}]")
mix = "".join(f"[a{k}]" for k in range(len(cues)))
fc = ";".join(parts) + f";{mix}amix=inputs={len(cues)}:normalize=0,alimiter=limit=0.95[aout]"
args += ["-filter_complex", fc, "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac",
         "-b:a", "192k", "-shortest", out]
subprocess.run(args, check=True); print("mixed", out)
