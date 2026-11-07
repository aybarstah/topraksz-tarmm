import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOHUMDAN FİDEYE (KÜPTE ÇİMLENDİRME) ----------
c1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOHUMDAN FİDEYE</span>
<h1 style="margin-top:50px">Toprak yok,<br>tohum nerede<br>çimlenir?</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Küçük bir küpte<br><span class="hl">6 ADIMDA FİDE</span></p>
<svg width="912" height="400" viewBox="0 0 912 400" style="position:absolute;bottom:130px;left:84px">
 <g>
  <rect x="60" y="230" width="170" height="150" rx="16" fill="#C9B48E"/>
  <g fill="#8A6A45"><rect x="78" y="255" width="134" height="12" rx="6"/><rect x="78" y="285" width="134" height="12" rx="6"/><rect x="78" y="315" width="134" height="12" rx="6"/><rect x="78" y="345" width="134" height="12" rx="6"/></g>
  <ellipse cx="145" cy="228" rx="16" ry="10" fill="#7A5236"/>
 </g>
 <g>
  <rect x="370" y="230" width="170" height="150" rx="16" fill="#C9B48E"/>
  <g fill="#8A6A45"><rect x="388" y="255" width="134" height="12" rx="6"/><rect x="388" y="285" width="134" height="12" rx="6"/><rect x="388" y="315" width="134" height="12" rx="6"/><rect x="388" y="345" width="134" height="12" rx="6"/></g>
  <path d="M455 230 C455 200 455 185 455 170" stroke="#6FA84B" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="M455 175 C435 150 410 150 395 160 C410 175 435 180 455 175Z" fill="#6FA84B"/>
  <path d="M455 175 C475 150 500 150 515 160 C500 175 475 180 455 175Z" fill="#6FA84B"/>
 </g>
 <g>
  <rect x="680" y="230" width="170" height="150" rx="16" fill="#C9B48E"/>
  <g fill="#8A6A45"><rect x="698" y="255" width="134" height="12" rx="6"/><rect x="698" y="285" width="134" height="12" rx="6"/><rect x="698" y="315" width="134" height="12" rx="6"/><rect x="698" y="345" width="134" height="12" rx="6"/></g>
  <path d="M765 230 L765 120" stroke="#6FA84B" stroke-width="8" stroke-linecap="round"/>
  <path d="M765 160 C730 120 690 125 670 140 C695 165 735 170 765 160Z" fill="#6FA84B"/>
  <path d="M765 140 C800 95 845 100 865 115 C840 145 795 150 765 140Z" fill="#5C9440"/>
  <path d="M765 120 C750 80 760 50 775 35 C790 60 785 95 765 120Z" fill="#6FA84B"/>
  <g stroke="#F4EBDD" stroke-width="5" stroke-linecap="round"><path d="M740 380 L735 395"/><path d="M765 380 L765 398"/><path d="M790 380 L796 395"/></g>
 </g>
 <g stroke="#B59A6E" stroke-width="6" fill="none" stroke-linecap="round"><path d="M260 300 L330 300 M315 285 L330 300 L315 315"/><path d="M570 300 L640 300 M625 285 L640 300 L625 315"/></g>
 <g font-family="Poppins" font-size="26" font-weight="700" fill="#2E3B2A" text-anchor="middle">
  <text x="145" y="200">tohum</text><text x="455" y="135">çimlenme</text>
 </g>
</svg></div>"""

c2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN KÜP?</span>
<h2>Fideler toprakta<br>değil, küpte doğar</h2>
<p>Topraksız tarımda tohumlar genelde <b>kaya yünü küpü</b> ya da <b>hidroponik fide süngeri</b> içinde çimlendirilir.</p>
<p style="margin-top:30px">Küp, tohumu <span class="hl">nemli</span> tutar ama arada <span class="hl">hava</span> da bırakır. Fide büyüyünce küpüyle birlikte sisteme taşınır.</p>
<p style="margin-top:30px">Böylece kökler <b>hiç sökülmez</b>, fide aktarma stresini çok daha az yaşar.</p></div>"""

c3 = """<div class="pad" style="padding-top:150px">
<span class="tag">NASIL ÇALIŞIR?</span>
<h2 style="font-size:60px;margin:22px 0 10px">Küpün içinde neler olur?</h2>
<svg width="912" height="820" viewBox="0 0 912 820">
 <rect x="60" y="520" width="520" height="80" rx="14" fill="#5B4636"/>
 <rect x="76" y="535" width="488" height="50" rx="8" fill="#8CC0B8"/>
 <rect x="170" y="250" width="300" height="280" rx="22" fill="#C9B48E"/>
 <g fill="#8A6A45"><rect x="195" y="285" width="250" height="14" rx="7"/><rect x="195" y="325" width="250" height="14" rx="7"/><rect x="195" y="365" width="250" height="14" rx="7"/><rect x="195" y="405" width="250" height="14" rx="7"/><rect x="195" y="445" width="250" height="14" rx="7"/><rect x="195" y="485" width="250" height="14" rx="7"/></g>
 <path d="M320 250 L320 110" stroke="#6FA84B" stroke-width="10" stroke-linecap="round"/>
 <path d="M320 140 C280 90 230 95 205 115 C235 145 285 150 320 140Z" fill="#6FA84B"/>
 <path d="M320 140 C360 90 410 95 435 115 C405 145 355 150 320 140Z" fill="#6FA84B"/>
 <g stroke="#F4EBDD" stroke-width="6" fill="none" stroke-linecap="round">
  <path d="M320 250 C315 330 330 410 318 520"/><path d="M300 300 C270 360 270 440 250 520"/><path d="M340 300 C370 370 380 450 400 520"/>
 </g>
 <rect x="30" y="20" width="270" height="70" rx="14" fill="#F7D98B"/>
 <text x="165" y="66" font-family="Poppins" font-size="32" text-anchor="middle">💡 ışık</text>
 <path d="M165 90 L240 110" stroke="#B59A6E" stroke-width="4" stroke-dasharray="8 6"/>
 <g font-family="Poppins" font-size="30" font-weight="600" fill="#2E3B2A">
  <line x1="440" y1="125" x2="560" y2="125" stroke="#2E3B2A" stroke-width="3"/><text x="570" y="120">İlk yapraklar</text><text x="570" y="155" fill="#3C6E3A">(çenek yaprakları)</text>
  <line x1="470" y1="330" x2="560" y2="330" stroke="#2E3B2A" stroke-width="3"/><text x="570" y="325">Lifler arası</text><text x="570" y="360" fill="#3C6E3A">nem + hava</text>
  <line x1="400" y1="520" x2="560" y2="480" stroke="#2E3B2A" stroke-width="3"/><text x="570" y="475">Kök alttan çıkınca</text><text x="570" y="510" fill="#3C6E3A">aktarma zamanı</text>
  <text x="320" y="650" text-anchor="middle">Su / hafif çözelti</text>
 </g>
</svg></div>"""

c4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ADIM ADIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">6 adımda fide</h2>
<div class="card" style="padding:20px 32px"><div class="ic">💧</div><p style="font-size:30px"><b>1. Küpü ıslat.</b> pH'ı ayarlı suda beklet, fazlasını ezmeden süzdür.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌰</div><p style="font-size:30px"><b>2. Tohumu ek.</b> Her deliğe 1-2 tohum; küçük tohumu derine itme.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🫙</div><p style="font-size:30px"><b>3. Üstünü ört.</b> Şeffaf kapak nemi korur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">☀️</div><p style="font-size:30px"><b>4. Filiz görünce kapağı aç</b> ve hemen ışık ver.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧪</div><p style="font-size:30px"><b>5. İlk gerçek yapraklarda</b> hafif besin çözeltisine geç.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪴</div><p style="font-size:30px"><b>6. Kök alttan çıkınca</b> küpüyle birlikte sisteme aktar.</p></div></div>"""

c5 = """<div class="pad" style="padding-top:150px">
<span class="tag">DİKKAT!</span>
<h2>Çimlendirmede<br>4 sık hata</h2>
<div class="card"><div class="ic">🌊</div><p style="font-size:31px"><b>Küpü su içinde boğmak.</b> Tohum havasız kalır, fide çürüyebilir.</p></div>
<div class="card"><div class="ic">🦒</div><p style="font-size:31px"><b>Filize geç ışık vermek.</b> Fide ışık arar, ince ve uzun boy atar.</p></div>
<div class="card"><div class="ic">🏜️</div><p style="font-size:31px"><b>Küpü kurutmak.</b> Çimlenen tohum bir kez kurursa genelde geri dönmez.</p></div>
<div class="card"><div class="ic">🧽</div><p style="font-size:31px"><b>Bulaşık süngeri kullanmak.</b> Bazıları antibakteriyel katkı içerir; fide için üretileni seç.</p></div></div>"""

c6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🧱</div><p style="font-size:33px">Tohum <b>küpte</b> çimlenir, küpüyle sisteme geçer.</p></div>
<div class="card"><div class="ic">⚖️</div><p style="font-size:33px">Küp <span class="hl">nemli ama sırılsıklam değil</span> olmalı.</p></div>
<div class="card"><div class="ic">☀️</div><p style="font-size:33px">Filiz çıkınca <b>kapak kalkar, ışık gelir.</b></p></div>
<div class="card"><div class="ic">🌱</div><p style="font-size:33px">Kök alttan görününce <b>aktarma</b> zamanı.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">İlk tohumunu ne zaman ekiyorsun?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: DEPODA YOSUN (ALG) ----------
a1 = """<div class="pad" style="padding-top:150px">
<span class="tag">SORUN ÇÖZÜCÜ</span>
<h1 style="margin-top:50px">Depon<br>yeşillendi mi?</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Besin çözeltisinin gizli<br>ortağı: <span class="hl">YOSUN (ALG)</span></p>
<svg width="912" height="420" viewBox="0 0 912 420" style="position:absolute;bottom:120px;left:84px">
 <rect x="80" y="60" width="330" height="340" rx="26" fill="#FFF9EE" stroke="#E3D3B8" stroke-width="5"/>
 <rect x="96" y="130" width="298" height="254" rx="16" fill="#8CC0B8"/>
 <rect x="96" y="250" width="298" height="134" rx="16" fill="#6FA84B" opacity=".75"/>
 <g fill="#3C6E3A" opacity=".8"><circle cx="140" cy="200" r="14"/><circle cx="200" cy="170" r="9"/><circle cx="320" cy="210" r="16"/><circle cx="260" cy="230" r="10"/><circle cx="360" cy="160" r="8"/></g>
 <text x="245" y="40" font-family="Poppins" font-size="30" font-weight="700" fill="#B5543A" text-anchor="middle">şeffaf depo 😬</text>
 <rect x="500" y="60" width="330" height="340" rx="26" fill="#2E3B2A"/>
 <rect x="516" y="130" width="298" height="254" rx="16" fill="#3F4F3A"/>
 <g fill="#8CC0B8" opacity=".35"><rect x="530" y="150" width="270" height="10" rx="5"/></g>
 <text x="665" y="40" font-family="Poppins" font-size="30" font-weight="700" fill="#3C6E3A" text-anchor="middle">ışık geçirmez ✅</text>
 <path d="M665 250 C640 230 640 200 665 185 C690 200 690 230 665 250Z" fill="#6FA84B"/>
</svg></div>"""

a2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN OLUŞUR?</span>
<h2>3 şey bir araya<br>gelince yosun başlar</h2>
<div style="display:flex;gap:22px;margin:10px 0 34px">
 <div class="card" style="flex:1;display:block;text-align:center;padding:30px 10px"><div style="font-size:70px">☀️</div><p style="font-weight:700">Işık</p></div>
 <div class="card" style="flex:1;display:block;text-align:center;padding:30px 10px"><div style="font-size:70px">💧</div><p style="font-weight:700">Su</p></div>
 <div class="card" style="flex:1;display:block;text-align:center;padding:30px 10px"><div style="font-size:70px">🧪</div><p style="font-weight:700">Besin</p></div>
</div>
<p>Besin çözeltisi yosun için de <b>hazır bir sofradır</b>. Su ve besini çıkaramazsın.</p>
<p style="margin-top:26px">Elinde tek bir koz var: <span class="hl">ışığı kesmek.</span></p></div>"""

a3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ZARARI NE?</span>
<h2 style="font-size:60px">Sadece görüntü<br>sorunu değil</h2>
<div class="card"><div class="ic">🍽️</div><p style="font-size:31px"><b>Besine ortak olur.</b> Bitkiye ayırdığın besini o da tüketir.</p></div>
<div class="card"><div class="ic">🫧</div><p style="font-size:31px"><b>Oksijeni azaltır.</b> Geceleri solunum yapar, ölen yosun çürürken de oksijen harcar.</p></div>
<div class="card"><div class="ic">📈</div><p style="font-size:31px"><b>pH'ı oynatır.</b> Gündüz fotosentezle CO₂ çekip pH'ı yükseltebilir.</p></div>
<div class="card"><div class="ic">🔧</div><p style="font-size:31px"><b>Pompayı ve hortumu tıkar,</b> köklerde çürümeye zemin hazırlar.</p></div></div>"""

a4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖNLEM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Işığı 5 yerden kes</h2>
<div class="card"><div class="ic">🪣</div><p style="font-size:31px"><b>Depo:</b> koyu, ışık geçirmeyen kap seç. Beyaz ve ince plastik de ışık geçirebilir.</p></div>
<div class="card"><div class="ic">🕳️</div><p style="font-size:31px"><b>Boş delikler:</b> kapağı ya da bantla kapat.</p></div>
<div class="card"><div class="ic">🌀</div><p style="font-size:31px"><b>Şeffaf hortumlar:</b> koyu bantla sar ya da opak hortum kullan.</p></div>
<div class="card"><div class="ic">🧱</div><p style="font-size:31px"><b>Küp üstleri:</b> ışık alan nemli yüzey yeşerir; örtü kullan.</p></div>
<div class="card"><div class="ic">🔦</div><p style="font-size:31px"><b>Test:</b> depoya içeriden fener tut; dışarıdan ışık görünüyorsa kaplaman gerekir.</p></div></div>"""

a5 = """<div class="pad" style="padding-top:150px">
<span class="tag">TEMİZLİK</span>
<h2>Yosun çoktan<br>geldiyse ne yapmalı?</h2>
<div class="card"><div class="ic">1️⃣</div><p style="font-size:32px"><b>Kaynağı bul:</b> ışık nereden sızıyor? Önce onu kapat.</p></div>
<div class="card"><div class="ic">2️⃣</div><p style="font-size:32px"><b>Çözeltiyi yenile,</b> depo duvarındaki yeşil tabakayı sil.</p></div>
<div class="card"><div class="ic">3️⃣</div><p style="font-size:32px"><b>Hasat sonrası, bitki yokken</b> sistemi fırçala, dezenfekte et.</p></div>
<div class="card"><div class="ic">4️⃣</div><p style="font-size:32px"><b>Bol suyla durula.</b> Dezenfektan kalıntısı köklere zarar verir.</p></div></div>"""

a6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">☀️</div><p style="font-size:33px">Yosun için <b>ışık + su + besin</b> yeter.</p></div>
<div class="card"><div class="ic">🌑</div><p style="font-size:33px">Kontrol edebildiğin tek şey: <span class="hl">ışık.</span></p></div>
<div class="card"><div class="ic">🪣</div><p style="font-size:33px">Depo, delik, hortum ve küpü <b>karanlıkta tut.</b></p></div>
<div class="card"><div class="ic">🧽</div><p style="font-size:33px">Temizliği <b>bitki yokken</b> yap, iyice durula.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Senin deponda hiç yosun oldu mu?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:100px">Bazı tohumlar<br>çimlenmek için<br>ışık ister! ☀️</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Marul gibi bazı küçük tohumlar <b>ışıkla</b> daha iyi çimlenir. Onları derine gömersen <span class="hl">uyanamayabilirler.</span></p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🌱</div><p style="font-size:40px"><b>Tohumdan fide nasıl yapılır?</b><br><span style="font-size:34px">Bugün 12:30'da 6 adımda anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([c1, c2, c3, c4, c5, c6], "gun4/cimlendirme")
    render_post([a1, a2, a3, a4, a5, a6], "gun4/yosun")
    render_story(story, "gun4/hikaye")
