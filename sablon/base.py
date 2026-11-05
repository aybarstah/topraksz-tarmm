"""Topraksız tarım kart şablonu. Kullanım:
from sablon.base import render_post, render_story
render_post([html1,...,html6], "gun3/ortam", )   -> gun3/ortam_1.jpg ... _6.jpg (1080x1350)
render_story(html, "gun3/hikaye")                 -> gun3/hikaye.jpg (1080x1920)
Kart HTML örnekleri için ornekler/ klasörüne bak (c1..c6). Sınıflar: .pad .tag h1 h2 p .card .ic .hl
"""
import asyncio, os
from playwright.async_api import async_playwright
from PIL import Image

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;font-family:'Poppins',sans-serif;background:#F4EBDD;color:#2E3B2A;position:relative;overflow:hidden}
.pad{padding:90px 84px}
.tag{display:inline-block;background:#3C6E3A;color:#F4EBDD;font-weight:600;font-size:28px;padding:10px 26px;border-radius:40px;letter-spacing:1px}
h1{font-size:96px;line-height:1.02;font-weight:800;color:#2F5D2D}
h2{font-size:68px;line-height:1.1;font-weight:800;color:#2F5D2D;margin:28px 0 36px}
p{font-size:36px;line-height:1.5}
.foot{position:absolute;bottom:56px;left:84px;right:84px;display:flex;justify-content:space-between;font-size:26px;color:#7A6A52;font-weight:600}
.num{position:absolute;top:70px;right:84px;font-size:28px;font-weight:700;color:#B59A6E}
.card{background:#FFF9EE;border-radius:28px;padding:26px 36px;margin-bottom:18px;box-shadow:0 4px 0 #E3D3B8;display:flex;gap:26px;align-items:center}
.ic{font-size:54px;width:70px;text-align:center}
.card b{color:#2F5D2D}
.hl{background:#F7D98B;padding:0 10px;border-radius:8px}
"""


STORY_EXTRA = "body{width:1080px;height:1920px} .pad{padding:220px 84px}"

def _page(body, n, total, story=False):
    if story:
        foot = '<div class="foot" style="bottom:200px"><span>@topraksz_tarmm</span><span>gönderiye bak 👆</span></div>'
        return f"<html><head><meta charset='utf-8'><style>{CSS}{STORY_EXTRA}</style></head><body>{body}{foot}</body></html>"
    foot = '<div class="foot"><span>@topraksz_tarmm</span><span>'+('kaydır →' if n<total else 'kaydet 🔖')+'</span></div>'
    num = f'<div class="num">{n}/{total}</div>' if n>1 else ''
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{num}{body}{foot}</body></html>"

async def _shot(items, h):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':h})
        for html, out in items:
            os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
            await pg.set_content(html); await pg.wait_for_timeout(300)
            await pg.screenshot(path=out+'.png')
            Image.open(out+'.png').convert('RGB').save(out+'.jpg', quality=85); os.remove(out+'.png')
        await b.close()

def render_post(cards, prefix):
    t=len(cards); asyncio.run(_shot([(_page(c,i,t), f"{prefix}_{i}") for i,c in enumerate(cards,1)], 1350))

def render_story(html, out):
    asyncio.run(_shot([(_page(html,1,1,True), out)], 1920))
