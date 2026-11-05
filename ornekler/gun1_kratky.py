import asyncio
from playwright.async_api import async_playwright

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

def page(body, n):
    foot = '<div class="foot"><span>@topraksz_tarmm</span><span>'+('kaydır →' if n<6 else 'kaydet 🔖')+'</span></div>'
    num = f'<div class="num">{n}/6</div>' if n>1 else ''
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{num}{body}{foot}</body></html>"

c1 = """<div class="pad" style="padding-top:150px">
<span class="tag">EVDE TOPRAKSIZ TARIM</span>
<h1 style="margin-top:50px">Pompa yok.<br>Elektrik yok.<br>Sulama yok.</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Sadece bir kavanoz ve<br><span class="hl">KRATKY YÖNTEMİ</span></p>
<svg width="900" height="420" viewBox="0 0 900 420" style="position:absolute;bottom:130px;left:90px">
 <rect x="330" y="150" width="240" height="250" rx="20" fill="#5B4636"/>
 <rect x="350" y="250" width="200" height="130" rx="10" fill="#8CC0B8"/>
 <rect x="315" y="135" width="270" height="30" rx="8" fill="#3C6E3A"/>
 <path d="M450 135 C440 80 380 60 350 40 C410 50 445 80 450 120 C455 80 490 40 560 30 C520 60 460 90 450 135Z" fill="#6FA84B"/>
 <path d="M450 135 C 420 70 360 90 330 70 C 380 110 430 110 450 135Z" fill="#4E8B37"/>
 <g stroke="#F4EBDD" stroke-width="5" fill="none" stroke-linecap="round">
  <path d="M450 165 C440 220 420 260 410 340"/><path d="M450 165 C455 230 470 280 480 350"/><path d="M450 165 C450 240 445 300 450 360"/>
 </g>
</svg></div>"""

c2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDİR?</span>
<h2>Kendi kendine işleyen<br>topraksız sistem</h2>
<p>Hawaii Üniversitesi'nden <b>Bernard Kratky</b>'nin geliştirdiği <b>pasif</b> bir yöntem.</p>
<p style="margin-top:30px">Bitki kapaktaki file saksıda durur, kökleri besin çözeltisine uzanır. Bitki suyu içtikçe seviye düşer, kökler ile su arasında <span class="hl">hava boşluğu</span> oluşur.</p>
<p style="margin-top:30px">Üstteki kökler bu boşluktan <b>oksijen</b>, alttakiler sudan <b>besin</b> alır. Hava pompasına gerek kalmaz.</p></div>"""

c3 = """<div class="pad" style="padding-top:150px">
<span class="tag">NASIL ÇALIŞIR?</span>
<svg width="912" height="900" viewBox="0 0 912 900" style="margin-top:40px">
 <g transform="translate(-130,0)">
 <rect x="230" y="200" width="420" height="600" rx="30" fill="#5B4636"/>
 <rect x="255" y="470" width="370" height="305" rx="16" fill="#8CC0B8"/>
 <rect x="200" y="175" width="480" height="45" rx="10" fill="#3C6E3A"/>
 <rect x="385" y="160" width="110" height="110" rx="10" fill="#C9B48E"/>
 <path d="M440 165 C420 90 350 70 310 40 C380 50 430 90 440 145 C450 90 500 40 580 30 C530 70 460 100 440 165Z" fill="#6FA84B"/>
 <g stroke="#F4EBDD" stroke-width="6" fill="none" stroke-linecap="round">
  <path d="M440 270 C430 350 400 420 390 700"/><path d="M440 270 C450 360 480 440 490 720"/><path d="M440 270 C440 380 440 480 445 740"/>
  <path d="M440 330 C410 360 380 380 350 400"/><path d="M440 330 C470 360 500 380 530 400"/>
 </g>
 <path d="M620 300 L620 440" stroke="#F7D98B" stroke-width="6" marker-end="url(#a)"/>
 </g>
 <defs><marker id="a" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="#F7D98B"/></marker></defs>
 <g font-family="Poppins" font-size="32" font-weight="600" fill="#2E3B2A">
  <line x1="550" y1="198" x2="600" y2="160" stroke="#2E3B2A" stroke-width="3"/><text x="610" y="150">Işık geçirmez</text><text x="610" y="188">kapak</text>
  <line x1="365" y1="240" x2="600" y2="270" stroke="#2E3B2A" stroke-width="3"/><text x="610" y="280">File saksı</text>
  <line x1="400" y1="390" x2="600" y2="390" stroke="#2E3B2A" stroke-width="3"/><text x="610" y="380">Hava boşluğu</text><text x="610" y="418" fill="#3C6E3A">→ oksijen</text>
  <line x1="495" y1="620" x2="600" y2="620" stroke="#2E3B2A" stroke-width="3"/><text x="610" y="610">Besin çözeltisi</text><text x="610" y="648" fill="#3C6E3A">→ beslenme</text>
 </g>
 <text x="0" y="860" font-family="Poppins" font-size="32" font-weight="700" fill="#B5543A">↓ Bitki içtikçe su seviyesi düşer, hava boşluğu büyür.</text>
</svg></div>"""

c4 = """<div class="pad" style="padding-top:150px">
<span class="tag">NELER LAZIM?</span>
<h2 style="font-size:60px;margin:22px 0 26px">5 malzeme yeter</h2>
<div class="card"><div class="ic">🫙</div><p><b>Işık geçirmeyen kap</b><br><span style="font-size:30px">Kavanoz, kova, kutu. Şeffafsa boyayın ya da sarın (yosun olmasın).</span></p></div>
<div class="card"><div class="ic">🧺</div><p><b>File saksı</b><br><span style="font-size:30px">Kapağa açılan deliğe oturur.</span></p></div>
<div class="card"><div class="ic">🪨</div><p><b>Yetiştirme ortamı</b><br><span style="font-size:30px">Perlit, kaya yünü veya cocopeat.</span></p></div>
<div class="card"><div class="ic">🧪</div><p><b>Hidroponik besin</b><br><span style="font-size:30px">Topraksız tarıma özel A+B gübre.</span></p></div>
<div class="card"><div class="ic">📟</div><p><b>pH ölçer</b><br><span style="font-size:30px">Hedef: 5,5 – 6,5</span></p></div></div>"""

c5 = """<div class="pad" style="padding-top:150px">
<span class="tag">ADIM ADIM</span>
<h2 style="font-size:60px">Kurulum 15 dakika</h2>
<div class="card"><div class="ic" style="font-size:46px;font-weight:800;color:#3C6E3A">1</div><p style="font-size:32px">Kabı besin çözeltisiyle doldur, <b>pH'ı 5,5–6,5</b>'e ayarla.</p></div>
<div class="card"><div class="ic" style="font-size:46px;font-weight:800;color:#3C6E3A">2</div><p style="font-size:32px">Fideyi ortamla birlikte <b>file saksıya</b> yerleştir.</p></div>
<div class="card"><div class="ic" style="font-size:46px;font-weight:800;color:#3C6E3A">3</div><p style="font-size:32px">Saksının <b>alt kısmı suya değsin</b>, tamamen batmasın.</p></div>
<div class="card"><div class="ic" style="font-size:46px;font-weight:800;color:#3C6E3A">4</div><p style="font-size:32px">Bekle. Su azaldıkça kökler uzar. <b>Kabı ağzına kadar doldurma</b>, hava boşluğu kalmalı.</p></div>
<div class="card"><div class="ic" style="font-size:46px;font-weight:800;color:#3C6E3A">5</div><p style="font-size:32px">Aydınlık bir yerde tut, <b>4–6 haftada</b> hasat et.</p></div></div>"""

c6 = """<div class="pad" style="padding-top:150px">
<span class="tag">HANGİ BİTKİLER?</span>
<h2>Kısa sürede yetişen<br>yapraklılar ✅</h2>
<p style="font-size:44px;line-height:1.7;font-weight:600">🥬 Marul &nbsp; 🌿 Roka<br>🌱 Fesleğen &nbsp; 🍃 Ispanak<br>🌿 Nane, maydanoz</p>
<div class="card" style="margin-top:44px;background:#F9E3D6;box-shadow:0 4px 0 #E8C2AD"><div class="ic">⚠️</div><p style="font-size:32px">Domates, biber gibi <b>çok su içen büyük bitkiler</b> için uygun değil; çözelti çabuk biter.</p></div>
<p style="margin-top:50px;font-size:40px;font-weight:700;color:#2F5D2D">Bu gönderiyi kaydet, hafta sonu bir kavanozla dene! 🔖</p></div>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':1350})
        for i,c in enumerate([c1,c2,c3,c4,c5,c6],1):
            await pg.set_content(page(c,i)); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'kratky_{i}.png')
        await b.close()
asyncio.run(main())
