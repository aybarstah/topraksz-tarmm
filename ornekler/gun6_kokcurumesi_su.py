import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: KÖK ÇÜRÜMESİ (PYTHIUM) ----------
c1 = """<div class="pad" style="padding-top:150px">
<span class="tag">KÖK SAĞLIĞI</span>
<h1 style="margin-top:50px">Kökler neden<br>kahverengi<br>oluyor?</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Suda yayılan sessiz düşman:<br><span class="hl">PYTHIUM</span></p>
<svg width="912" height="380" viewBox="0 0 912 380" style="position:absolute;bottom:115px;left:84px">
 <rect x="60" y="60" width="360" height="310" rx="26" fill="#5B4636"/>
 <rect x="492" y="60" width="360" height="310" rx="26" fill="#5B4636"/>
 <g stroke-width="9" fill="none" stroke-linecap="round">
  <g stroke="#FFFFFF"><path d="M240 75 C235 150 250 240 235 355"/><path d="M225 90 C180 150 175 250 140 335"/><path d="M255 90 C300 150 310 250 345 335"/><path d="M235 120 C210 190 200 270 185 355"/><path d="M245 120 C275 190 285 270 295 355"/></g>
  <g stroke="#B08A60"><path d="M672 75 C667 140 682 200 664 280"/><path d="M657 90 C617 140 607 195 582 245"/><path d="M687 90 C727 140 737 195 762 245"/><path d="M667 120 C647 165 642 215 632 285"/></g>
 </g>
 <g font-family="Poppins" font-size="34" font-weight="700" text-anchor="middle">
  <text x="240" y="40" fill="#3C6E3A">sağlıklı ✅</text><text x="672" y="40" fill="#B5543A">hasta ⚠️</text>
 </g>
</svg></div>"""

c2 = """<div class="pad" style="padding-top:150px">
<span class="tag">PYTHIUM NEDİR?</span>
<h2>Mantar gibi görünür,<br>ama gerçek mantar değil</h2>
<p>Pythium, <b>oomiset</b> denen mantar benzeri bir organizmadır. Köklere saldırır ve kök çürümesine yol açar.</p>
<p style="margin-top:30px">Yüzebilen sporları (<span class="hl">zoospor</span>) çözeltide taşınır. Yani suyun olduğu yerde yol bulur.</p>
<p style="margin-top:30px">En sinsi yanı: enfeksiyon <b>belirti vermeden</b> başlayabilir, yapraklar uzun süre yeşil kalabilir.</p></div>"""

c3 = """<div class="pad" style="padding-top:150px">
<span class="tag">KARŞILAŞTIR</span>
<h2 style="font-size:60px;margin:22px 0 30px">Köküne bak, farkı gör</h2>
<div style="display:flex;gap:22px">
 <div class="card" style="flex:1;display:block;padding:44px 30px">
  <div style="font-size:64px;text-align:center">🌱</div>
  <p style="font-weight:800;text-align:center;color:#3C6E3A;margin-bottom:18px">Sağlıklı</p>
  <p style="font-size:34px;margin-bottom:16px">Beyaz ya da krem</p>
  <p style="font-size:34px;margin-bottom:16px">Sıkı, dolgun</p>
  <p style="font-size:34px;margin-bottom:16px">Bol ince yan kök</p>
  <p style="font-size:34px">Bitki canlı ve gergin</p>
 </div>
 <div class="card" style="flex:1;display:block;padding:44px 30px">
  <div style="font-size:64px;text-align:center">🥀</div>
  <p style="font-weight:800;text-align:center;color:#B5543A;margin-bottom:18px">Pythium şüphesi</p>
  <p style="font-size:34px;margin-bottom:16px">Kahverengi, sarımsı</p>
  <p style="font-size:34px;margin-bottom:16px">Yumuşak, kaygan</p>
  <p style="font-size:34px;margin-bottom:16px">Kısa, küt kökler</p>
  <p style="font-size:34px">Solgunluk, gerileme</p>
 </div>
</div>
<p style="font-size:29px;margin-top:22px;color:#7A6A52">Kesin tanı için laboratuvar gerekir; besin eksikliği ve oksijensizlik de kökü bozabilir.</p></div>"""

c4 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN YAYILIR?</span>
<h2 style="font-size:60px;margin:22px 0 26px">5 davetiye</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:30px"><b>Sıcak çözelti.</b> Kök bölgesi ısındıkça hastalık genelde ağırlaşır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🫧</div><p style="font-size:30px"><b>Düşük oksijen.</b> Havasız kalan kök zayıflar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌿</div><p style="font-size:30px"><b>Hasta fide.</b> Belirtisiz fide, salgını başlatabilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">♻️</div><p style="font-size:30px"><b>Kullanılmış küp/alet.</b> Dayanıklı sporlar sistemde kalabilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪰</div><p style="font-size:30px"><b>Sinekler ve toz.</b> Mantar sinekleri spor taşıyabilir.</p></div></div>"""

c5 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖNLEM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Tedavi değil,<br>önlem kazandırır</h2>
<div class="card" style="padding:20px 32px"><div class="ic">❄️</div><p style="font-size:30px"><b>Çözeltiyi serin tut.</b> Depoyu güneşten koru.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💨</div><p style="font-size:30px"><b>Kökü havalandır.</b> Hava taşı ve iyi akış şart.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧼</div><p style="font-size:30px"><b>Sezon arası temizlik.</b> Bitki yokken dezenfekte et, bol durula.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🚫</div><p style="font-size:30px"><b>Eski küpü tekrar kullanma.</b> Temiz fideyle başla.</p></div>
<p style="font-size:33px;margin-top:22px;font-weight:600">Unutma: salgın başladıktan sonra durdurmak <span class="hl">çok zordur.</span></p></div>"""

c6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">👀</div><p style="font-size:33px">Yaprağa değil, <b>köke de bak.</b></p></div>
<div class="card"><div class="ic">🌊</div><p style="font-size:33px">Pythium <b>suyla</b> yayılır, sistem boyunca dolaşır.</p></div>
<div class="card"><div class="ic">❄️</div><p style="font-size:33px"><span class="hl">Serin + oksijenli çözelti</span> en iyi kalkan.</p></div>
<div class="card"><div class="ic">🌱</div><p style="font-size:33px">Hastalığı sisteme <b>sokmamak</b> en kolay yol.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Köklerin bugün ne renk?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: SU KALİTESİ VE TDS ----------
a1 = """<div class="pad" style="padding-top:150px">
<span class="tag">SU KALİTESİ</span>
<h1 style="margin-top:50px">TDS cihazın<br>sana yalan<br>söylüyor mu?</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Suyun iyi mi, <span class="hl">tek sayıdan</span><br>anlaşılmaz.</p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:130px;left:84px">
 <rect x="140" y="30" width="170" height="250" rx="26" fill="#2E3B2A"/>
 <rect x="162" y="56" width="126" height="84" rx="10" fill="#8CC0B8"/>
 <text x="225" y="112" font-family="Poppins" font-size="40" font-weight="800" fill="#2E3B2A" text-anchor="middle">???</text>
 <rect x="208" y="280" width="34" height="20" fill="#B59A6E"/>
 <path d="M520 40 L500 280 L760 280 L740 40 Z" fill="#FFF9EE" stroke="#E3D3B8" stroke-width="6"/>
 <path d="M512 130 L503 272 L757 272 L748 130 Z" fill="#8CC0B8"/>
 <text x="630" y="210" font-family="Poppins" font-size="27" font-weight="700" fill="#2E3B2A" text-anchor="middle">içinde ne var?</text>
</svg></div>"""

a2 = """<div class="pad" style="padding-top:150px">
<span class="tag">CİHAZ NE ÖLÇER?</span>
<h2>TDS metre aslında<br>TDS ölçmez</h2>
<p>Cihaz, suyun <b>elektrik iletkenliğini (EC)</b> ölçer ve bunu bir <b>katsayıyla</b> ppm'e çevirir.</p>
<div style="display:flex;gap:22px;margin:30px 0">
 <div class="card" style="flex:1;display:block;text-align:center;padding:30px 12px"><p style="font-size:30px">0,5 ölçekli cihaz</p><p style="font-size:60px;font-weight:800;color:#2F5D2D">500 ppm</p></div>
 <div class="card" style="flex:1;display:block;text-align:center;padding:30px 12px"><p style="font-size:30px">0,7 ölçekli cihaz</p><p style="font-size:60px;font-weight:800;color:#2F5D2D">700 ppm</p></div>
</div>
<p>İkisi de <span class="hl">aynı su:</span> EC 1,0 mS/cm. O yüzden reçetelerde <b>EC</b> ile konuşmak daha güvenlidir.</p></div>"""

a3 = """<div class="pad" style="padding-top:150px">
<span class="tag">KÖR NOKTA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Aynı EC,<br>bambaşka su</h2>
<svg width="912" height="510" viewBox="0 0 912 510">
 <g>
  <path d="M60 40 L95 360 L335 360 L370 40 Z" fill="#FFF9EE" stroke="#E3D3B8" stroke-width="6"/>
  <path d="M76 120 L100 352 L330 352 L354 120 Z" fill="#8CC0B8"/>
  <g font-family="Poppins" font-size="36" font-weight="800" fill="#2F5D2D" text-anchor="middle"><text x="165" y="200">Ca</text><text x="270" y="230">Mg</text><text x="175" y="300">Ca</text><text x="265" y="310">Mg</text></g>
 </g>
 <g>
  <path d="M540 40 L575 360 L815 360 L850 40 Z" fill="#FFF9EE" stroke="#E3D3B8" stroke-width="6"/>
  <path d="M556 120 L580 352 L810 352 L834 120 Z" fill="#8CC0B8"/>
  <g font-family="Poppins" font-size="36" font-weight="800" fill="#B5543A" text-anchor="middle"><text x="645" y="200">Na</text><text x="750" y="230">Cl</text><text x="655" y="300">Na</text><text x="745" y="310">Cl</text></g>
 </g>
 <g font-family="Poppins" font-size="33" font-weight="700" text-anchor="middle">
  <text x="215" y="415" fill="#3C6E3A">işe yarayan iyonlar</text><text x="695" y="415" fill="#B5543A">devridaimde birikir</text>
  <text x="456" y="480" fill="#2E3B2A">EC metrede ikisi de aynı görünebilir</text>
 </g>
</svg>
<p style="font-size:32px">EC, <b>faydalı–zararlı</b> ayrımı yapmaz; yalnızca toplam iyonu gösterir.</p></div>"""

a4 = """<div class="pad" style="padding-top:150px">
<span class="tag">SUYUNA BAK</span>
<h2 style="font-size:60px;margin:22px 0 22px">Kaynak suda<br>rehber değerler</h2>
<div class="card" style="padding:30px 32px"><div class="ic">⚡</div><p style="font-size:33px"><b>EC:</b> 0,2–0,8 mS/cm, ideali 1'in altında</p></div>
<div class="card" style="padding:30px 32px"><div class="ic">🪨</div><p style="font-size:33px"><b>Alkalinite:</b> 40–160 ppm CaCO₃</p></div>
<div class="card" style="padding:30px 32px"><div class="ic">🧂</div><p style="font-size:33px"><b>Sodyum:</b> 50 ppm altı</p></div>
<div class="card" style="padding:30px 32px"><div class="ic">🌿</div><p style="font-size:33px"><b>Bor:</b> 0,5 ppm altı</p></div>
<p style="font-size:29px;margin-top:22px;color:#7A6A52">Kaynak: Missouri Üniversitesi Yayım Rehberi G6984. Değerler ürün ve sisteme göre değişebilir; kapalı sistemlerde tuzlar birikir.</p></div>"""

a5 = """<div class="pad" style="padding-top:150px">
<span class="tag">İPUCU</span>
<h2 style="font-size:60px;margin:22px 0 26px">pH metre her şeyi<br>göstermez</h2>
<div class="card"><div class="ic">📈</div><p style="font-size:31px"><b>Alkalinite yüksekse</b> pH'ı düşürmek için daha çok asit gerekir.</p></div>
<div class="card"><div class="ic">🎢</div><p style="font-size:31px"><b>Alkalinite çok düşükse</b> pH sürekli oynar.</p></div>
<div class="card"><div class="ic">🔬</div><p style="font-size:31px"><b>Başlamadan su analizi yaptır:</b> pH, EC, alkalinite ve elementler.</p></div>
<div class="card"><div class="ic">🌧️</div><p style="font-size:31px"><b>Yağmur suyu</b> çoğu zaman çok iyidir; tuzlu suda ters ozmoz gerekir.</p></div></div>"""

a6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">📟</div><p style="font-size:33px">TDS metre <b>EC'den hesaplar</b>, ölçek önemlidir.</p></div>
<div class="card"><div class="ic">🧂</div><p style="font-size:33px">Aynı EC, <span class="hl">farklı içerik</span> olabilir.</p></div>
<div class="card"><div class="ic">🪨</div><p style="font-size:33px">pH kadar <b>alkalinite</b> de önemli.</p></div>
<div class="card"><div class="ic">🔬</div><p style="font-size:33px">Bir kez <b>laboratuvar analizi</b>, çok sorunu önler.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sen hangi suyu kullanıyorsun?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:100px">Yapraklar<br>yemyeşil ama<br>kök çürüyor<br>olabilir! 😱</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Pythium köke sessizce girer. Bitki uzun süre <b>sağlıklı görünebilir</b>, sonra <span class="hl">hızla solabilir.</span></p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🥀</div><p style="font-size:40px"><b>Kök çürümesi nasıl önlenir?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([c1, c2, c3, c4, c5, c6], "gun6/kokcurumesi")
    render_post([a1, a2, a3, a4, a5, a6], "gun6/sukalitesi")
    render_story(story, "gun6/hikaye")
