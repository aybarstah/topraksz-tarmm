"""Reels üretici: zamana bağlı HTML sahnesini kare kare çekip MP4 yapar.
Kullanım:
from sablon.reel import render_reel
render_reel(html, "gun9/akuaponik_reel", sure=18, fps=30)
html içinde global bir `render(t)` JS fonksiyonu olmalı (t saniye). Görünüm 1080x1920.
"""
import asyncio, os, subprocess, shutil, tempfile
from playwright.async_api import async_playwright

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;font-family:'Poppins',sans-serif;background:#F4EBDD;color:#2E3B2A;position:relative;overflow:hidden}
.hook{position:absolute;top:210px;left:70px;right:70px;text-align:center;font-weight:800;font-size:92px;line-height:1.08;color:#2F5D2D}
.hook u{text-decoration:none;display:block;width:560px;height:14px;background:#F2C94C;border-radius:8px;margin:26px auto 0}
.cap{position:absolute;left:70px;right:70px;bottom:330px;text-align:center;font-size:56px;font-weight:700;line-height:1.3;color:#2E3B2A}
.cap .hl{background:#F7D98B;padding:0 12px;border-radius:10px}
.brand{position:absolute;bottom:170px;left:0;right:0;text-align:center;font-size:32px;font-weight:700;color:#7A6A52}
.scene{position:absolute;inset:0}
"""

def page(body, js):
    return f"<html><head><meta charset='utf-8'><style>{BASE_CSS}</style></head><body>{body}<div class='brand'>@topraksz_tarmm</div><script>{js}</script></body></html>"

async def _frames(html, sure, fps, tmp):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':1920})
        await pg.set_content(html); await pg.wait_for_timeout(400)
        n = int(sure*fps)
        for i in range(n):
            await pg.evaluate(f"render({i/fps})")
            await pg.screenshot(path=f"{tmp}/f{i:05d}.png")
        await b.close()

def render_reel(html, out, sure=18, fps=30):
    tmp = tempfile.mkdtemp()
    try:
        asyncio.run(_frames(html, sure, fps, tmp))
        os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
        subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-i",f"{tmp}/f%05d.png",
            "-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest",
            "-c:v","libx264","-pix_fmt","yuv420p","-profile:v","high","-crf","20","-preset","medium",
            "-c:a","aac","-b:a","128k","-movflags","+faststart", out+".mp4"], check=True)
        # kapak görseli: ilk sahnenin oturmuş hali
        subprocess.run(["ffmpeg","-y","-loglevel","error","-ss","2.5","-i",out+".mp4","-frames:v","1","-q:v","3",out+"_kapak.jpg"], check=True)
    finally:
        shutil.rmtree(tmp)
