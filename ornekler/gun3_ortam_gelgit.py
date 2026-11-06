import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: YETİŞTİRME ORTAMLARI ----------
o1 = """<div class="pad" style="padding-top:150px">
<span class="tag">YETİŞTİRME ORTAMLARI</span>
<h1 style="margin-top:50px">Toprak yoksa<br>kök neye<br>tutunur?</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Topraksız tarımın<br><span class="hl">4 GİZLİ KAHRAMANI</span></p>
<svg width="912" height="400" viewBox="0 0 912 400" style="position:absolute;bottom:130px;left:84px">
 <g>
  <rect x="10" y="150" width="190" height="230" rx="22" fill="#C9B48E"/>
  <g fill="#8A6A45"><rect x="30" y="175" width="150" height="14" rx="7"/><rect x="30" y="205" width="150" height="14" rx="7"/><rect x="30" y="235" width="150" height="14" rx="7"/><rect x="30" y="265" width="150" height="14" rx="7"/><rect x="30" y="295" width="150" height="14" rx="7"/><rect x="30" y="325" width="150" height="14" rx="7"/></g>
 </g>
 <g>
  <rect x="240" y="150" width="190" height="230" rx="22" fill="#7A5236"/>
  <g fill="#5B3B26"><circle cx="280" cy="190" r="10"/><circle cx="330" cy="230" r="12"/><circle cx="390" cy="200" r="9"/><circle cx="300" cy="300" r="11"/><circle cx="370" cy="290" r="13"/><circle cx="270" cy="345" r="9"/><circle cx="400" cy="350" r="10"/></g>
 </g>
 <g>
  <rect x="470" y="150" width="190" height="230" rx="22" fill="#FFF9EE" stroke="#E3D3B8" stroke-width="4"/>
  <g fill="#E8E1D4"><circle cx="510" cy="190" r="16"/><circle cx="560" cy="215" r="13"/><circle cx="620" cy="190" r="15"/><circle cx="525" cy="270" r="14"/><circle cx="600" cy="260" r="17"/><circle cx="560" cy="320" r="15"/><circle cx="625" cy="340" r="12"/><circle cx="505" cy="345" r="12"/></g>
 </g>
 <g>
  <rect x="700" y="150" width="190" height="230" rx="22" fill="#B5543A"/>
  <g fill="#D27A5A"><circle cx="745" cy="200" r="26"/><circle cx="815" cy="195" r="24"/><circle cx="855" cy="260" r="20"/><circle cx="760" cy="275" r="25"/><circle cx="820" cy="330" r="24"/><circle cx="745" cy="345" r="18"/></g>
 </g>
 <path d="M455 140 C445 80 395 55 360 40 C415 48 448 80 455 120 C462 80 500 45 555 35 C515 60 465 95 455 140Z" fill="#6FA84B"/>
 <g font-family="Poppins" font-size="26" font-weight="700" fill="#2E3B2A" text-anchor="middle">
  <text x="105" y="140">kaya yünü</text><text x="335" y="140">cocopeat</text><text x="565" y="140">perlit</text><text x="795" y="140">hidroton</text>
 </g>
</svg></div>"""

o2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDİR?</span>
<h2>Besin vermez,<br>kökü taşır</h2>
<p>Topraksız tarımda bitkinin besini <b>çözeltiden</b> gelir. Yetiştirme ortamı ise köke <b>tutunacak yer</b> sağlar.</p>
<p style="margin-top:30px">İyi bir ortam aynı anda iki iş yapar: <span class="hl">suyu tutar</span> ama arada köklerin nefes alacağı <span class="hl">hava boşluğu</span> da bırakır.</p>
<p style="margin-top:30px">Hangi ortamı seçeceğin; kullandığın <b>sisteme</b> ve <b>bitkiye</b> göre değişir.</p></div>"""

o3 = """<div class="pad" style="padding-top:150px">
<span class="tag">TANIŞALIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">4 ortam, 4 karakter</h2>
<div class="card"><div class="ic">🧱</div><p><b>Kaya yünü</b><br><span style="font-size:29px">Bazalt kayası eritilip lif yapılır. Suyu ve havayı dengeli tutar.</span></p></div>
<div class="card"><div class="ic">🥥</div><p><b>Cocopeat (hindistan cevizi lifi)</b><br><span style="font-size:29px">Kabuk liflerinden. Çok su tutar, doğada çözünür.</span></p></div>
<div class="card"><div class="ic">⚪</div><p><b>Perlit</b><br><span style="font-size:29px">Isıtılıp patlatılan volkanik cam. Hafif, havalandırır.</span></p></div>
<div class="card"><div class="ic">🟤</div><p><b>Hidroton (kil topu)</b><br><span style="font-size:29px">Fırınlanmış kil. Yıkanıp tekrar tekrar kullanılır.</span></p></div></div>"""

o4 = """<div class="pad" style="padding-top:150px">
<span class="tag">KARŞILAŞTIRMA</span>
<h2 style="font-size:60px">Su mu, hava mı?</h2>
<div class="card" style="display:block;padding:34px 40px">
 <div style="display:flex;font-size:28px;font-weight:700;color:#7A6A52;margin-bottom:14px"><span style="flex:1.3">Ortam</span><span style="flex:1">Su tutma</span><span style="flex:1">Havalanma</span></div>
 <div style="display:flex;font-size:32px;line-height:2.1"><b style="flex:1.3">Kaya yünü</b><span style="flex:1">💧💧💧</span><span style="flex:1">🌬️🌬️</span></div>
 <div style="display:flex;font-size:32px;line-height:2.1"><b style="flex:1.3">Cocopeat</b><span style="flex:1">💧💧💧</span><span style="flex:1">🌬️🌬️</span></div>
 <div style="display:flex;font-size:32px;line-height:2.1"><b style="flex:1.3">Perlit</b><span style="flex:1">💧</span><span style="flex:1">🌬️🌬️🌬️</span></div>
 <div style="display:flex;font-size:32px;line-height:2.1"><b style="flex:1.3">Hidroton</b><span style="flex:1">💧</span><span style="flex:1">🌬️🌬️🌬️</span></div>
</div>
<p style="margin-top:34px;font-size:33px">🌱 <b>Çimlendirme:</b> kaya yünü küpü<br>🪣 <b>Kratky / DWC:</b> file saksıda hidroton<br>🪴 <b>Saksı + damla:</b> cocopeat + perlit karışımı</p></div>"""

o5 = """<div class="pad" style="padding-top:150px">
<span class="tag">DİKKAT!</span>
<h2>Ortam seçerken<br>4 sık hata</h2>
<div class="card"><div class="ic">🧪</div><p style="font-size:31px"><b>Kaya yününü direkt kullanmak.</b> pH'ı yüksek olabilir; önce pH'ı ayarlı suda bekletip ıslat.</p></div>
<div class="card"><div class="ic">🧂</div><p style="font-size:31px"><b>Yıkanmamış cocopeat.</b> Tuz içerebilir; "yıkanmış / tamponlanmış" yazanı seç.</p></div>
<div class="card"><div class="ic">🚿</div><p style="font-size:31px"><b>Hidrotonu yıkamamak.</b> Tozu suyu bulandırır, pompayı tıkayabilir.</p></div>
<div class="card"><div class="ic">😷</div><p style="font-size:31px"><b>Kuru perliti savurmak.</b> Tozunu soluma; nemlendirerek kullan.</p></div></div>"""

o6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🌱</div><p style="font-size:33px">Ortam <b>besin değil</b>, köke yuva ve denge sağlar.</p></div>
<div class="card"><div class="ic">⚖️</div><p style="font-size:33px">Amaç: <span class="hl">nem + hava</span> dengesini kurmak.</p></div>
<div class="card"><div class="ic">🔁</div><p style="font-size:33px">Su tutan ortamı <b>perlit</b> ile hafifletebilirsin.</p></div>
<div class="card"><div class="ic">♻️</div><p style="font-size:33px">Uzun vadede tekrar kullanmak istersen: <b>hidroton</b>.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Hangi ortamı kullanıyorsun?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: GEL-GİT (EBB & FLOW) ----------
g1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ SİSTEMLER</span>
<h1 style="margin-top:50px">Bitkini<br>gelgitle<br>sula.</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Dolar, boşalır, kök nefes alır:<br><span class="hl">GEL-GİT (EBB &amp; FLOW)</span></p>
<svg width="912" height="400" viewBox="0 0 912 400" style="position:absolute;bottom:130px;left:84px">
 <rect x="120" y="120" width="680" height="70" rx="14" fill="#3C6E3A"/>
 <rect x="140" y="140" width="640" height="40" rx="8" fill="#8CC0B8"/>
 <g fill="#C9B48E"><rect x="200" y="95" width="90" height="85" rx="10"/><rect x="415" y="95" width="90" height="85" rx="10"/><rect x="630" y="95" width="90" height="85" rx="10"/></g>
 <g fill="#6FA84B">
  <path d="M245 95 C235 50 195 35 170 25 C215 30 240 55 245 80 C250 55 275 28 320 20 C290 40 255 65 245 95Z"/>
  <path d="M460 95 C450 50 410 35 385 25 C430 30 455 55 460 80 C465 55 490 28 535 20 C505 40 470 65 460 95Z"/>
  <path d="M675 95 C665 50 625 35 600 25 C645 30 670 55 675 80 C680 55 705 28 750 20 C720 40 685 65 675 95Z"/>
 </g>
 <rect x="220" y="250" width="480" height="130" rx="18" fill="#5B4636"/>
 <rect x="240" y="275" width="440" height="85" rx="10" fill="#8CC0B8"/>
 <path d="M330 190 L330 300" stroke="#2E3B2A" stroke-width="8"/>
 <path d="M590 190 L590 300" stroke="#2E3B2A" stroke-width="8"/>
 <path d="M300 230 L330 205 L360 230" stroke="#3C6E3A" stroke-width="7" fill="none" stroke-linecap="round"/>
 <path d="M560 210 L590 235 L620 210" stroke="#B5543A" stroke-width="7" fill="none" stroke-linecap="round"/>
</svg></div>"""

g2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDİR?</span>
<h2>Tepsi dolar,<br>sonra geri boşalır</h2>
<p>Gel-git sisteminde bitkiler bir <b>tepsiye</b> dizilir. Altta besin çözeltisi dolu bir <b>depo</b> bulunur.</p>
<p style="margin-top:30px">Zamanlayıcı pompayı çalıştırır, tepsi dolar ve kökleri ıslatır. Pompa durunca su <span class="hl">yine depoya</span> akar.</p>
<p style="margin-top:30px">Su çekilirken ortamdaki boşluklara <b>taze hava</b> dolar. Kökler hem beslenir hem nefes alır.</p></div>"""

g3 = """<div class="pad" style="padding-top:150px">
<span class="tag">NASIL ÇALIŞIR?</span>
<svg width="912" height="900" viewBox="0 0 1010 997" style="margin-top:40px">
 <rect x="20" y="230" width="620" height="90" rx="16" fill="#3C6E3A"/>
 <rect x="40" y="250" width="580" height="55" rx="10" fill="#8CC0B8"/>
 <g fill="#C9B48E"><rect x="80" y="190" width="110" height="110" rx="12"/><rect x="275" y="190" width="110" height="110" rx="12"/><rect x="470" y="190" width="110" height="110" rx="12"/></g>
 <g fill="#6FA84B">
  <path d="M135 190 C125 130 80 110 50 95 C105 100 130 130 135 165 C140 130 170 95 225 85 C190 110 145 140 135 190Z"/>
  <path d="M330 190 C320 130 275 110 245 95 C300 100 325 130 330 165 C335 130 365 95 420 85 C385 110 340 140 330 190Z"/>
  <path d="M525 190 C515 130 470 110 440 95 C495 100 520 130 525 165 C530 130 560 95 615 85 C580 110 535 140 525 190Z"/>
 </g>
 <rect x="90" y="520" width="480" height="260" rx="24" fill="#5B4636"/>
 <rect x="112" y="560" width="436" height="200" rx="14" fill="#8CC0B8"/>
 <rect x="150" y="690" width="80" height="60" rx="10" fill="#B5543A"/>
 <path d="M190 690 L190 320" stroke="#2E3B2A" stroke-width="10"/>
 <path d="M160 420 L190 390 L220 420" stroke="#F4EBDD" stroke-width="6" fill="none" stroke-linecap="round"/>
 <path d="M470 270 L470 600" stroke="#2E3B2A" stroke-width="10"/>
 <path d="M440 470 L470 500 L500 470" stroke="#F4EBDD" stroke-width="6" fill="none" stroke-linecap="round"/>
 <rect x="456" y="245" width="28" height="30" rx="4" fill="#2E3B2A"/>
 <rect x="640" y="640" width="90" height="70" rx="12" fill="#C9B48E"/>
 <text x="685" y="688" font-family="Poppins" font-size="34" text-anchor="middle">⏱️</text>
 <path d="M640 675 L230 715" stroke="#7A6A52" stroke-width="4" stroke-dasharray="10 8"/>
 <g font-family="Poppins" font-size="30" font-weight="600" fill="#2E3B2A">
  <text x="660" y="265">Tepsi</text><text x="660" y="300" fill="#3C6E3A">(bitkiler burada)</text>
  <line x1="484" y1="250" x2="650" y2="160" stroke="#2E3B2A" stroke-width="3"/><text x="660" y="150">Taşma borusu</text><text x="660" y="185" fill="#3C6E3A">(seviyeyi sınırlar)</text>
  <line x1="500" y1="480" x2="650" y2="450" stroke="#2E3B2A" stroke-width="3"/><text x="660" y="450">Dönüş hattı</text>
  <line x1="230" y1="400" x2="300" y2="400" stroke="#2E3B2A" stroke-width="3"/><text x="310" y="410">Dolum</text>
  <text x="660" y="750">Zamanlayıcı</text>
  <line x1="150" y1="740" x2="60" y2="840" stroke="#2E3B2A" stroke-width="3"/><text x="60" y="875">Dalgıç pompa (depoda)</text>
 </g>
</svg></div>"""

g4 = """<div class="pad" style="padding-top:150px">
<span class="tag">NELER LAZIM?</span>
<h2 style="font-size:60px;margin:22px 0 26px">5 temel parça</h2>
<div class="card"><div class="ic">🟩</div><p><b>Sulama tepsisi</b><br><span style="font-size:30px">Bitkiler file saksılarla içine dizilir.</span></p></div>
<div class="card"><div class="ic">🪣</div><p><b>Işık geçirmeyen depo</b><br><span style="font-size:30px">Tepsiyi dolduracak sudan daha fazlasını almalı.</span></p></div>
<div class="card"><div class="ic">⚙️</div><p><b>Dalgıç pompa</b><br><span style="font-size:30px">Depodaki çözeltiyi tepsiye basar.</span></p></div>
<div class="card"><div class="ic">⏱️</div><p><b>Zamanlayıcı (timer priz)</b><br><span style="font-size:30px">Pompanın ne zaman çalışacağını belirler.</span></p></div>
<div class="card"><div class="ic">🔧</div><p><b>Taşma + dönüş bağlantısı</b><br><span style="font-size:30px">Su seviyesini sınırlar, fazlayı depoya döndürür.</span></p></div></div>"""

g5 = """<div class="pad" style="padding-top:150px">
<span class="tag">ARTI / EKSİ</span>
<h2 style="font-size:60px">Sana uygun mu?</h2>
<div style="display:flex;gap:24px">
 <div class="card" style="flex:1;display:block;padding:36px;background:#E6F0DE;box-shadow:0 4px 0 #C6D9B6"><p style="font-size:40px;font-weight:800;color:#2F5D2D">Artıları</p>
 <p style="font-size:30px;margin-top:18px;line-height:1.8">✅ Köke bol hava<br>✅ Farklı bitki ve<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;saksı bir arada<br>✅ Kolay büyütülür<br>✅ Su geri döner</p></div>
 <div class="card" style="flex:1;display:block;padding:36px"><p style="font-size:40px;font-weight:800;color:#2F5D2D">Eksileri</p>
 <p style="font-size:30px;margin-top:18px;line-height:1.8">⚠️ Elektrik ister<br>⚠️ Pompa ya da<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timer bozulursa<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;kök kurur<br>⚠️ Sızıntı riski</p></div>
</div>
<p style="margin-top:40px;font-size:34px">💡 Sulama sıklığını <b>ortam</b> belirler: su tutan ortam daha seyrek, hidroton daha sık sulama ister.</p></div>"""

g6 = """<div class="pad" style="padding-top:150px">
<span class="tag">DİKKAT!</span>
<h2>Gel-gitte en sık<br>yapılan 4 hata</h2>
<div class="card"><div class="ic">🌊</div><p style="font-size:32px"><b>Taşma borusu koymamak.</b> Pompa fazla basarsa tepsi taşar.</p></div>
<div class="card"><div class="ic">🪣</div><p style="font-size:32px"><b>Küçük depo.</b> Tepsi dolarken depo boşalır, pompa kuru çalışır.</p></div>
<div class="card"><div class="ic">⏰</div><p style="font-size:32px"><b>Zamanlayıcıyı kontrol etmemek.</b> Tek aksama, köklerin kurumasına yeter.</p></div>
<div class="card"><div class="ic">💦</div><p style="font-size:32px"><b>Çok sık sulamak.</b> Ortam hiç kurumazsa kök havasız kalır.</p></div>
<p style="margin-top:26px;font-size:36px;font-weight:700;color:#2F5D2D">Kaydet, kurulumda lazım olacak 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:104px">Kaya yünü<br>gerçekten<br>bir kayadan<br>yapılıyor! 🪨</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Volkanik <b>bazalt</b> kayası çok yüksek sıcaklıkta eritilir, sonra <span class="hl">ince lifler</span> halinde eğrilir.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🤔</div><p style="font-size:40px"><b>Sen hangi ortamı kullanıyorsun?</b><br><span style="font-size:34px">Bugün 12:30'da 4 ortamı karşılaştırıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([o1, o2, o3, o4, o5, o6], "gun3/ortam")
    render_post([g1, g2, g3, g4, g5, g6], "gun3/gelgit")
    render_story(story, "gun3/hikaye")
