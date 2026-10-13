"""Render a VIP Wireless post from an HTML file.

Usage:
  python3 _kit/render.py image  path/to/post.html  out.png        # 1080x1350 still
  python3 _kit/render.py video  path/to/video.html out.mp4 [secs]  # 1080x1920, 30fps

Video pages animate with CSS; every animation is paused and stepped frame by
frame, so the output is smooth and deterministic. Needs playwright + ffmpeg.
"""
import os, subprocess, sys, tempfile
from playwright.sync_api import sync_playwright


def render_image(html, out):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        pg.goto("file://" + os.path.abspath(html))
        pg.wait_for_timeout(700)
        pg.screenshot(path=out)
        b.close()


def render_video(html, out, secs=12.4, fps=30):
    tmp = tempfile.mkdtemp()
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto("file://" + os.path.abspath(html))
        pg.wait_for_timeout(800)
        pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        for i in range(int(fps * secs)):
            pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={i*1000/fps})")
            pg.screenshot(path=f"{tmp}/f{i:04d}.jpg", type="jpeg", quality=90)
        b.close()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps),
                    "-i", f"{tmp}/f%04d.jpg", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-crf", "20", "-movflags", "+faststart", out], check=True)


if __name__ == "__main__":
    kind, html, out = sys.argv[1:4]
    if kind == "image":
        render_image(html, out)
    else:
        render_video(html, out, float(sys.argv[4]) if len(sys.argv) > 4 else 12.4)
    print("rendered", out)
