import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: DAMLA SULAMA ----------
d1 = """<div class="pad" style="padding-top:150px">
<span class="tag">DAMLA SULAMA</span>
<h1 style="margin-top:50px">Damla damla<br>besleme 💧</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Topraksız tarımda<br><span class="hl">damla sulama nasıl kurulur?</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <rect x="20" y="40" width="860" height="22" rx="11" fill="#3C6E3A"/>
 <g stroke="#2E3B2A" stroke-width="5" fill="none">
  <path d="M170 62 C170 100 200 110 200 140"/><path d="M450 62 C450 100 480 110 480 140"/><path d="M730 62 C730 100 760 110 760 140"/>
 </g>
 <g fill="#5BA3C9"><path d="M200 150 C190 168 192 180 200 180 C208 180 210 168 200 150 Z"/><path d="M480 150 C470 168 472 180 480 180 C488 180 490 168 480 150 Z"/><path d="M760 150 C750 168 752 180 760 180 C768 180 770 168 760 150 Z"/></g>
 <g fill="#B59A6E"><rect x="110" y="190" width="180" height="90" rx="14"/><rect x="390" y="190" width="180" height="90" rx="14"/><rect x="670" y="190" width="180" height="90" rx="14"/></g>
 <g fill="#5E9B4F"><ellipse cx="170" cy="180" rx="40" ry="22"/><ellipse cx="450" cy="180" rx="40" ry="22"/><ellipse cx="730" cy="180" rx="40" ry="22"/></g>
</svg></div>"""

d2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDİR?</span>
<h2>Her bitkiye<br>kendi damlatıcısı</h2>
<p>Besin çözeltisi pompayla borulara basılır, <b>damlatıcılar</b> aracılığıyla her bitkinin dibine azar azar verilir.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🪴</div><p style="font-size:30px"><b>Cocopeat, kaya yünü, perlit</b> gibi ortamlarla kullanılır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🍅</div><p style="font-size:30px">Domates, biber, salatalık, çilek seralarında <span class="hl">en yaygın</span> yöntemdir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">⏱️</div><p style="font-size:30px">Pompa bir <b>zamanlayıcı</b> ile kısa süreli ve sık çalışır.</p></div></div>"""

d3 = """<div class="pad" style="padding-top:150px">
<span class="tag">SİSTEM ŞEMASI</span>
<h2 style="font-size:60px;margin:22px 0 26px">Parçalar<br>neler?</h2>
<div class="card" style="padding:18px 32px"><div class="ic">🛢️</div><p style="font-size:29px"><b>Depo:</b> ışık geçirmeyen, kapaklı (yosunu önler).</p></div>
<div class="card" style="padding:18px 32px"><div class="ic">⚙️</div><p style="font-size:29px"><b>Pompa + zamanlayıcı:</b> sulama sayısını ve süresini belirler.</p></div>
<div class="card" style="padding:18px 32px"><div class="ic">🧽</div><p style="font-size:29px"><b>Filtre:</b> damlatıcıları tıkanmaktan korur.</p></div>
<div class="card" style="padding:18px 32px"><div class="ic">〰️</div><p style="font-size:29px"><b>Ana boru + ince hortum + damla kazığı:</b> çözeltiyi köke taşır.</p></div>
<div class="card" style="padding:18px 32px"><div class="ic">💧</div><p style="font-size:29px"><b>Basınç ayarlı damlatıcı:</b> hattın başı ve sonu <span class="hl">eşit su</span> alır.</p></div></div>"""

d4 = """<div class="pad" style="padding-top:150px">
<span class="tag">AÇIK MI, KAPALI MI?</span>
<h2 style="font-size:60px;margin:22px 0 26px">Fazla su<br>nereye gider?</h2>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🚰 Açık sistem</p><p style="font-size:30px;margin-top:8px">Ortamdan süzülen fazla çözelti (drenaj) <b>geri kullanılmaz.</b> Kurulumu basit, ama su ve gübre kaybı olur.</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">♻️ Kapalı sistem</p><p style="font-size:30px;margin-top:8px">Drenaj toplanır, <b>süzülüp depoya geri döner.</b> Tasarruflu, ama EC ve pH'ı daha sık takip etmek gerekir.</p></div></div>"""

d5 = """<div class="pad" style="padding-top:150px">
<span class="tag">PÜF NOKTALARI</span>
<h2 style="font-size:60px;margin:22px 0 26px">Drenaj<br>senin göstergen</h2>
<div class="card" style="padding:20px 32px"><div class="ic">💦</div><p style="font-size:29px">Verilen suyun bir kısmı <b>dışarı süzülmeli.</b> Ortamlı sistemlerde genelde <span class="hl">%20–30 drenaj</span> hedeflenir; birikmiş tuzu yıkar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📏</div><p style="font-size:29px">Drenajın <b>EC'si</b> verilenden çok yüksekse ortamda tuz birikiyor demektir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔁</div><p style="font-size:29px"><b>Az ve sık</b> sula: güneşli günlerde sayı artar, bulutlu günlerde azalır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px">Damlatıcıları düzenli <b>kontrol et</b>; tek bir tıkalı uç o bitkiyi susuz bırakır.</p></div></div>"""

d6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">💧</div><p style="font-size:33px">Her bitkiye <b>kendi damlatıcısı.</b></p></div>
<div class="card"><div class="ic">🧽</div><p style="font-size:33px">Filtre kullan, <b>tıkanmayı önle.</b></p></div>
<div class="card"><div class="ic">💦</div><p style="font-size:33px">Biraz drenaj <span class="hl">hata değil</span>, gerekli.</p></div>
<div class="card"><div class="ic">📏</div><p style="font-size:33px">Drenajın <b>EC'sini ölç.</b></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sen hangi sistemi kullanıyorsun?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: KIŞIN TOPRAKSIZ TARIM ----------
k1 = """<div class="pad" style="padding-top:150px">
<span class="tag">KIŞ GELDİ</span>
<h1 style="margin-top:50px">Kışın<br>topraksız<br>tarım ❄️</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Soğuk ve kısa günlerde<br><span class="hl">hasadı sürdürmenin yolları</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <path d="M200 280 L200 140 L456 30 L712 140 L712 280 Z" fill="#FFF9EE" stroke="#B59A6E" stroke-width="8"/>
 <line x1="456" y1="30" x2="456" y2="280" stroke="#E3D3B8" stroke-width="6"/>
 <g fill="#5E9B4F"><ellipse cx="290" cy="255" rx="45" ry="25"/><ellipse cx="400" cy="255" rx="45" ry="25"/><ellipse cx="512" cy="255" rx="45" ry="25"/><ellipse cx="622" cy="255" rx="45" ry="25"/></g>
 <g fill="#FFFFFF" stroke="#9BB7C9" stroke-width="3"><circle cx="90" cy="60" r="12"/><circle cx="140" cy="150" r="9"/><circle cx="60" cy="220" r="11"/><circle cx="800" cy="70" r="12"/><circle cx="860" cy="170" r="9"/><circle cx="780" cy="230" r="11"/></g>
</svg></div>"""

k2 = """<div class="pad" style="padding-top:150px">
<span class="tag">SORUN</span>
<h2>Kış neden<br>zor geçer?</h2>
<div class="card" style="padding:22px 32px"><div class="ic">🌥️</div><p style="font-size:30px"><b>Gün kısa, ışık az:</b> bitki daha az fotosentez yapar, yavaş büyür.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🥶</div><p style="font-size:30px"><b>Çözelti soğur:</b> soğuk suda kökler besini ve suyu daha yavaş alır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">💧</div><p style="font-size:30px"><b>Yoğuşma ve nem:</b> soğuk yüzeyde biriken damlalar <span class="hl">küf hastalıklarına</span> zemin hazırlar.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🔥</div><p style="font-size:30px"><b>Isıtma maliyeti:</b> sıcak seven bitkilerde gider artar.</p></div></div>"""

k3 = """<div class="pad" style="padding-top:150px">
<span class="tag">BİTKİ SEÇİMİ</span>
<h2 style="font-size:60px;margin:22px 0 26px">Kışın ne<br>yetiştirilir?</h2>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">✅ Serin sevenler</p><p style="font-size:30px;margin-top:8px"><b>Marul, ıspanak, roka, tere, maydanoz.</b> Düşük sıcaklıkta da büyür, ısıtma ihtiyacı azdır.</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">⚠️ Sıcak sevenler</p><p style="font-size:30px;margin-top:8px"><b>Domates, biber, salatalık, fesleğen.</b> Hem ısı hem bol ışık ister; kışın <span class="hl">ek ısıtma ve aydınlatma</span> olmadan zorlanır.</p></div></div>"""

k4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÇÖZÜMLER</span>
<h2 style="font-size:60px;margin:22px 0 26px">Isıyı ve ışığı<br>koru</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:29px"><b>Çözeltiyi ısıt:</b> depoya termostatlı akvaryum ısıtıcısı. Genelde <span class="hl">18–22 °C</span> civarı önerilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💡</div><p style="font-size:29px"><b>Ek LED aydınlatma:</b> kısa günü uzatır, büyümeyi hızlandırır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🫧</div><p style="font-size:29px"><b>Yalıtım:</b> çift kat örtü ya da balonlu naylon ısı kaybını azaltır (ışığı biraz keser).</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧊</div><p style="font-size:29px"><b>Depoyu yerden kaldır:</b> soğuk zemine değmesin.</p></div></div>"""

k5 = """<div class="pad" style="padding-top:150px">
<span class="tag">DİKKAT</span>
<h2 style="font-size:60px;margin:22px 0 26px">Kış hataları</h2>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Hiç havalandırmamak:</b> nem birikir, küf artar. Günün ılık saatinde <b>kısa süre</b> havalandır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Hava hareketini kesmek:</b> küçük bir fan nemli havayı dağıtır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Yazdaki gibi sulamak:</b> bitki kışın daha az su kullanır; ortamlı sistemlerde sulamayı <span class="hl">ihtiyaca göre azalt.</span></p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Bitkiyi soğuk cama dayamak:</b> yapraklar üşür ve zarar görür.</p></div></div>"""

k6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🥬</div><p style="font-size:33px">Kışa <b>serin seven</b> yeşillik seç.</p></div>
<div class="card"><div class="ic">🌡️</div><p style="font-size:33px">Çözeltiyi <span class="hl">ılık</span> tut.</p></div>
<div class="card"><div class="ic">💡</div><p style="font-size:33px">Kısa günü <b>LED'le</b> destekle.</p></div>
<div class="card"><div class="ic">🌬️</div><p style="font-size:33px">Kısa havalandır, <b>nemi at.</b></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Kışın sistemin çalışıyor mu?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:92px">Saksının<br>altından su<br>akması<br>hata değil! 💧</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Ortamlı topraksız sistemlerde verilen suyun bir kısmının <span class="hl">süzülüp akması</span> istenir. Bu <b>drenaj</b>, ortamda biriken tuzu yıkar.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">💧</div><p style="font-size:40px"><b>Damla sulama nasıl kurulur?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([d1, d2, d3, d4, d5, d6], "gun11/damla")
    render_post([k1, k2, k3, k4, k5, k6], "gun11/kis")
    render_story(story, "gun11/hikaye")
