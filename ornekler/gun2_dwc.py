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
<span class="tag">TOPRAKSIZ SİSTEMLER</span>
<h1 style="margin-top:50px">Kökler<br>suda yaşar,<br>bitki uçar.</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Hızlı büyümenin sırrı:<br><span class="hl">DWC – DERİN SU KÜLTÜRÜ</span></p>
<svg width="900" height="420" viewBox="0 0 900 420" style="position:absolute;bottom:130px;left:90px">
 <rect x="180" y="150" width="540" height="250" rx="20" fill="#5B4636"/>
 <rect x="200" y="175" width="500" height="205" rx="10" fill="#8CC0B8"/>
 <rect x="165" y="135" width="570" height="30" rx="8" fill="#3C6E3A"/>
 <g fill="#6FA84B"><path d="M300 135 C290 80 240 60 215 45 C270 55 295 85 300 120 C305 85 335 50 390 40 C355 65 310 95 300 135Z"/>
 <path d="M600 135 C590 80 540 60 515 45 C570 55 595 85 600 120 C605 85 635 50 690 40 C655 65 610 95 600 135Z"/></g>
 <g stroke="#F4EBDD" stroke-width="5" fill="none" stroke-linecap="round">
  <path d="M300 165 C290 230 280 290 270 360"/><path d="M300 165 C305 240 320 300 330 365"/><path d="M600 165 C590 230 580 290 570 360"/><path d="M600 165 C605 240 620 300 630 365"/>
 </g>
 <g fill="#FFFFFF" opacity=".85"><circle cx="450" cy="350" r="9"/><circle cx="440" cy="310" r="7"/><circle cx="458" cy="270" r="8"/><circle cx="446" cy="230" r="6"/><circle cx="455" cy="200" r="5"/></g>
 <rect x="438" y="360" width="24" height="16" rx="4" fill="#C9B48E"/>
</svg></div>"""

c2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDİR?</span>
<h2>Köklerin sürekli<br>besin çözeltisinde<br>durduğu sistem</h2>
<p>DWC'de (Deep Water Culture) bitkiler kapağa yerleştirilir, kökleri <b>tamamen</b> besin çözeltisine daldırılır.</p>
<p style="margin-top:30px">Kökler suda boğulmasın diye bir <b>hava pompası</b> ve <b>hava taşı</b> suya sürekli kabarcık verir, <span class="hl">çözünmüş oksijen</span> sağlar.</p>
<p style="margin-top:30px">Kratky'den farkı bu: Oksijen hava boşluğundan değil, <b>pompadan</b> gelir.</p></div>"""

c3 = """<div class="pad" style="padding-top:150px">
<span class="tag">NASIL ÇALIŞIR?</span>
<svg width="912" height="900" viewBox="0 0 912 900" style="margin-top:40px">
 <g transform="translate(-130,0)">
 <rect x="230" y="200" width="420" height="600" rx="30" fill="#5B4636"/>
 <rect x="255" y="250" width="370" height="525" rx="16" fill="#8CC0B8"/>
 <rect x="200" y="175" width="480" height="45" rx="10" fill="#3C6E3A"/>
 <rect x="385" y="160" width="110" height="110" rx="10" fill="#C9B48E"/>
 <path d="M440 165 C420 90 350 70 310 40 C380 50 430 90 440 145 C450 90 500 40 580 30 C530 70 460 100 440 165Z" fill="#6FA84B"/>
 <g stroke="#F4EBDD" stroke-width="6" fill="none" stroke-linecap="round">
  <path d="M440 270 C430 350 400 420 390 650"/><path d="M440 270 C450 360 480 440 490 660"/><path d="M440 270 C440 380 440 480 445 690"/>
 </g>
 <rect x="530" y="740" width="70" height="26" rx="6" fill="#C9B48E"/>
 <path d="M565 740 C565 600 680 560 690 300 L690 120" stroke="#2E3B2A" stroke-width="6" fill="none"/>
 <rect x="660" y="60" width="90" height="60" rx="10" fill="#B5543A"/>
 <g fill="#FFFFFF" opacity=".9"><circle cx="560" cy="700" r="10"/><circle cx="575" cy="650" r="8"/><circle cx="555" cy="600" r="9"/><circle cx="570" cy="540" r="7"/><circle cx="558" cy="480" r="8"/><circle cx="572" cy="420" r="6"/><circle cx="560" cy="360" r="7"/></g>
 </g>
 <g font-family="Poppins" font-size="32" font-weight="600" fill="#2E3B2A">
  <line x1="630" y1="90" x2="660" y2="90" stroke="#2E3B2A" stroke-width="3"/><text x="670" y="80">Hava pompası</text><text x="670" y="116" fill="#3C6E3A">(prize takılı)</text>
  <line x1="365" y1="240" x2="660" y2="250" stroke="#2E3B2A" stroke-width="3"/><text x="670" y="260">File saksı</text>
  <line x1="450" y1="480" x2="660" y2="460" stroke="#2E3B2A" stroke-width="3"/><text x="670" y="450">Kabarcıklar</text><text x="670" y="488" fill="#3C6E3A">→ oksijen</text>
  <line x1="470" y1="753" x2="660" y2="700" stroke="#2E3B2A" stroke-width="3"/><text x="670" y="700">Hava taşı</text>
 </g>
 <text x="0" y="860" font-family="Poppins" font-size="32" font-weight="700" fill="#B5543A">Kökler suyun içinde ama oksijenden mahrum değil!</text>
</svg></div>"""

c4 = """<div class="pad" style="padding-top:150px">
<span class="tag">NELER LAZIM?</span>
<h2 style="font-size:60px;margin:22px 0 26px">5 temel malzeme</h2>
<div class="card"><div class="ic">🪣</div><p><b>Işık geçirmeyen kova/kutu</b><br><span style="font-size:30px">15–20 litre, kapaklı. Işık yosun demek.</span></p></div>
<div class="card"><div class="ic">💨</div><p><b>Hava pompası + hortum</b><br><span style="font-size:30px">Akvaryum pompası yeterli.</span></p></div>
<div class="card"><div class="ic">🫧</div><p><b>Hava taşı</b><br><span style="font-size:30px">Kabarcıkları dağıtır, dibe konur.</span></p></div>
<div class="card"><div class="ic">🧺</div><p><b>File saksı + ortam</b><br><span style="font-size:30px">Perlit, kaya yünü veya hidroton.</span></p></div>
<div class="card"><div class="ic">🧪</div><p><b>Hidroponik besin + pH/EC ölçer</b><br><span style="font-size:30px">pH 5,5–6,5 hedefi.</span></p></div></div>"""

c5 = """<div class="pad" style="padding-top:150px">
<span class="tag">KRATKY Mİ, DWC Mİ?</span>
<h2 style="font-size:60px">Hangisi sana uygun?</h2>
<div style="display:flex;gap:24px">
 <div class="card" style="flex:1;display:block;padding:36px"><p style="font-size:40px;font-weight:800;color:#2F5D2D">Kratky</p>
 <p style="font-size:30px;margin-top:18px;line-height:1.8">✅ Elektrik yok<br>✅ Çok ucuz<br>✅ Bakım yok<br>⚠️ Yavaş büyüme<br>⚠️ Küçük bitkiler</p></div>
 <div class="card" style="flex:1;display:block;padding:36px;background:#E6F0DE;box-shadow:0 4px 0 #C6D9B6"><p style="font-size:40px;font-weight:800;color:#2F5D2D">DWC</p>
 <p style="font-size:30px;margin-top:18px;line-height:1.8">✅ Hızlı büyüme<br>✅ Büyük bitkiler<br>✅ Daha çok verim<br>⚠️ Elektrik ister<br>⚠️ Pompa durursa risk</p></div>
</div>
<p style="margin-top:40px;font-size:34px">🔰 Yeni başlıyorsan <b>Kratky</b> ile dene, el alışınca <b>DWC</b>'ye geç.</p></div>"""

c6 = """<div class="pad" style="padding-top:150px">
<span class="tag">DİKKAT!</span>
<h2>DWC'de en sık<br>yapılan 4 hata</h2>
<div class="card"><div class="ic">🔌</div><p style="font-size:32px"><b>Pompayı kapatmak.</b> Birkaç saat oksijensiz kalan kökler çürümeye başlar.</p></div>
<div class="card"><div class="ic">🌡️</div><p style="font-size:32px"><b>Suyun ısınması.</b> 18–22 °C ideal; sıcak su daha az oksijen tutar.</p></div>
<div class="card"><div class="ic">☀️</div><p style="font-size:32px"><b>Şeffaf kap.</b> Işık alan suda yosun ürer.</p></div>
<div class="card"><div class="ic">🔁</div><p style="font-size:32px"><b>Çözeltiyi hiç değiştirmemek.</b> 1–2 haftada bir tazele.</p></div></div>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':1350})
        for i,c in enumerate([c1,c2,c3,c4,c5,c6],1):
            await pg.set_content(page(c,i)); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'dwc_{i}.png')
        await b.close()
asyncio.run(main())
