import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ PAZI ----------
p1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ PAZI</span>
<h1 style="margin-top:50px">Pancarın<br>yaprağı için<br>yetişen<br>kardeşi 🌿</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Bir kez ek,<br><span class="hl">dıştan topla.</span></p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(640 0)">
  <path d="M90 200 C80 140 40 90 20 40" stroke="#B5473A" stroke-width="9" fill="none"/>
  <path d="M90 200 C90 130 90 80 90 20" stroke="#E0A43A" stroke-width="9" fill="none"/>
  <path d="M90 200 C100 140 140 90 165 45" stroke="#C94F7C" stroke-width="9" fill="none"/>
  <g fill="#3F7A3A"><ellipse cx="22" cy="40" rx="30" ry="44" transform="rotate(-30 22 40)"/>
  <ellipse cx="90" cy="25" rx="32" ry="46"/><ellipse cx="165" cy="45" rx="30" ry="44" transform="rotate(30 165 45)"/></g>
  <rect x="25" y="195" width="130" height="32" rx="8" fill="#5B6B57"/>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="80" y="110">Renkli saplar, bol yaprak →</text><text x="80" y="150" fill="#7A6A52" font-size="26">aylarca hasat</text></g>
</svg></div>"""

p2 = """<div class="pad" style="padding-top:150px">
<span class="tag">TANIYALIM</span>
<h2>Pazı ve pancar<br>aynı tür</h2>
<p>Pazı da pancar da <b>Beta vulgaris</b> türündendir. Pancar kökü için, pazı ise <b>yaprağı ve sapı</b> için seçilmiştir.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">❄️</div><p style="font-size:30px"><b>Serin havayı sever;</b> sıcağa ıspanaktan daha dayanıklıdır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌈</div><p style="font-size:30px"><b>Beyaz, sarı, kırmızı</b> saplı çeşitleri vardır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌼</div><p style="font-size:30px"><span class="hl">İki yıllık</span> bitkidir; çiçeğe genelde soğuk bir dönemden sonra kalkar.</p></div></div>"""

p3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Bir "tohum",<br>birkaç fide</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="0" y="0" width="912" height="520" rx="26" fill="#FFF9EE"/>
 <g transform="translate(150 260)">
  <path d="M0 -70 C40 -70 70 -40 70 0 C70 40 40 70 0 70 C-40 70 -70 40 -70 0 C-70 -40 -40 -70 0 -70Z" fill="#B59A6E"/>
  <g fill="#E3D3B8"><circle cx="-25" cy="-20" r="14"/><circle cx="22" cy="-25" r="14"/><circle cx="0" cy="22" r="14"/></g>
  <text x="-120" y="140" font-size="26" fill="#2F5D2D">Tohum kümesi</text>
  <text x="-120" y="172" font-size="22" fill="#7A6A52" font-weight="600">içinde çoğu zaman 2-4 tohum</text>
 </g>
 <path d="M300 260 L380 260 M365 245 L380 260 L365 275" stroke="#3C6E3A" stroke-width="6" fill="none"/>
 <g transform="translate(440 120)">
  <rect x="0" y="200" width="160" height="110" rx="10" fill="#C9A646"/>
  <g stroke="#6FA84B" stroke-width="7" fill="none" stroke-linecap="round"><path d="M45 200 L40 120"/><path d="M80 200 L80 100"/><path d="M115 200 L122 125"/></g>
  <g fill="#6FA84B"><ellipse cx="25" cy="115" rx="22" ry="11"/><ellipse cx="55" cy="112" rx="22" ry="11"/><ellipse cx="65" cy="95" rx="22" ry="11"/><ellipse cx="97" cy="95" rx="22" ry="11"/><ellipse cx="108" cy="120" rx="22" ry="11"/><ellipse cx="138" cy="120" rx="22" ry="11"/></g>
 </g>
 <path d="M630 260 L700 260 M685 245 L700 260 L685 275" stroke="#3C6E3A" stroke-width="6" fill="none"/>
 <g transform="translate(720 120)">
  <rect x="0" y="200" width="160" height="110" rx="10" fill="#C9A646"/>
  <path d="M80 200 L80 90" stroke="#3F7A3A" stroke-width="9" stroke-linecap="round"/>
  <g fill="#3F7A3A"><ellipse cx="48" cy="95" rx="34" ry="16"/><ellipse cx="112" cy="95" rx="34" ry="16"/></g>
  <text x="10" y="350" font-size="24" fill="#2F5D2D">En güçlüsü ✂️</text>
 </g>
 </g>
 <g font-family="Poppins" font-size="28" font-weight="600" fill="#2E3B2A">
 <text x="0" y="590">Pazının "tohumu" aslında <tspan fill="#2F5D2D" font-weight="800">bir tohum kümesidir.</tspan></text>
 <text x="0" y="630">Bir taneden birkaç fide çıkabilir. Fazlasını</text>
 <text x="0" y="670"><tspan fill="#2F5D2D" font-weight="800">makasla dipten kes;</tspan> çekersen kalan</text>
 <text x="0" y="710">fidenin kökleri zarar görür.</text>
 </g>
</svg></div>"""

p4 = """<div class="pad" style="padding-top:150px">
<span class="tag">YETİŞTİRME</span>
<h2 style="font-size:60px;margin:22px 0 26px">Nasıl<br>yetiştirilir?</h2>
<div class="card" style="padding:20px 32px"><div class="ic">💧</div><p style="font-size:29px"><b>Tohumu ekmeden önce</b> birkaç saat suda bekletmek çimlenmeyi hızlandırabilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪣</div><p style="font-size:29px"><b>DWC kova</b> ya da <b>damla + cocopeat:</b> iri, uzun ömürlü bitki için.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌱</div><p style="font-size:29px"><b>NFT veya Kratky:</b> genç (baby) yaprak hasadı için uygun.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px"><b>Dış yaprakları</b> sapın dibinden kes, ortadaki <span class="hl">büyüme noktasına</span> dokunma.</p></div></div>"""

p5 = """<div class="pad" style="padding-top:150px">
<span class="tag">SORUNLAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Yaprakta<br>bunlara dikkat</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🪰</div><p style="font-size:29px"><b>Galeri sineği:</b> larvası yaprağın içini oyar, şeffaf-kahve lekeler bırakır. Lekeli yaprağı kopar, böcek tülü kullan.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔴</div><p style="font-size:29px"><b>Kırmızı kenarlı küçük gri lekeler:</b> mantar hastalığı olabilir; hava akışını artır, yaprakları ıslatma.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🐜</div><p style="font-size:29px"><b>Yaprak biti</b> genç yapraklarda toplanır; yaprak altına bak.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🚫</div><p style="font-size:29px"><b>Hepsini birden kesmek</b> bitkiyi zayıflatır; her seferinde <span class="hl">çoğunu bırak.</span></p></div></div>"""

p6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🌿</div><p style="font-size:33px">Pancarla <b>aynı tür.</b></p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px">Fazla fideyi <b>makasla</b> seyrelt.</p></div>
<div class="card"><div class="ic">🍃</div><p style="font-size:33px"><b>Dıştan içe</b> hasat et.</p></div>
<div class="card"><div class="ic">🪰</div><p style="font-size:33px">Yaprak lekelerini <span class="hl">erken fark et.</span></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Pazıyı nasıl seversin: sarma mı, kavurma mı?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: DEPO (REZERVUAR) SEÇİMİ ----------
d1 = """<div class="pad" style="padding-top:150px">
<span class="tag">DEPO SEÇİMİ</span>
<h1 style="margin-top:50px">Depon<br>küçükse,<br>derdin<br>büyük 🪣</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Besin deposu seçerken<br><span class="hl">nelere bakmalı?</span></p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(620 20)">
  <rect x="0" y="110" width="80" height="90" rx="10" fill="#B59A6E"/>
  <rect x="110" y="20" width="160" height="180" rx="14" fill="#3C6E3A"/>
  <rect x="122" y="60" width="136" height="128" rx="8" fill="#5E9B4F"/>
  <text x="18" y="165" font-family="Poppins" font-size="26" font-weight="800" fill="#FFF9EE">?</text>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="0" y="110">Hacim, renk, malzeme →</text><text x="0" y="150" fill="#7A6A52" font-size="26">hepsi bitkiyi etkiler</text></g>
</svg></div>"""

d2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN ÖNEMLİ?</span>
<h2>Su hacmi<br>= tampon</h2>
<p>Bitkiler her gün sudan <b>su ve besin</b> çeker. Depodaki su azsa bu değişim çok daha hızlı hissedilir.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">📈</div><p style="font-size:30px"><b>EC ve pH</b> küçük depoda daha hızlı kayar.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌡️</div><p style="font-size:30px"><b>Su sıcaklığı</b> az hacimde çabuk ısınır, çabuk soğur.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">💧</div><p style="font-size:30px"><b>Su seviyesi</b> hızla düşer; daha <span class="hl">sık tamamlama</span> gerekir.</p></div></div>"""

d3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Küçük mü,<br>büyük mü?</h2>
<svg width="912" height="780" viewBox="0 0 912 780">
 <g font-family="Poppins" font-weight="700">
 <rect x="0" y="0" width="912" height="610" rx="26" fill="#FFF9EE"/>
 <g transform="translate(70 120)">
  <rect x="40" y="170" width="200" height="200" rx="14" fill="#5B6B57"/>
  <rect x="52" y="250" width="176" height="108" rx="8" fill="#7FB0C9"/>
  <text x="140" y="420" text-anchor="middle" font-size="30" fill="#2F5D2D">Küçük depo</text>
  <text x="140" y="458" text-anchor="middle" font-size="22" fill="#B5473A" font-weight="600">değerler hızlı değişir</text>
  <path d="M140 140 L140 40 M120 60 L140 40 L160 60" stroke="#B5473A" stroke-width="6" fill="none"/>
  <path d="M190 40 L190 140 M170 120 L190 140 L210 120" stroke="#B5473A" stroke-width="6" fill="none"/>
 </g>
 <g transform="translate(470 120)">
  <rect x="0" y="40" width="360" height="330" rx="18" fill="#3C6E3A"/>
  <rect x="14" y="100" width="332" height="256" rx="10" fill="#7FB0C9"/>
  <text x="180" y="420" text-anchor="middle" font-size="30" fill="#2F5D2D">Büyük depo</text>
  <text x="180" y="458" text-anchor="middle" font-size="22" fill="#3C6E3A" font-weight="600">daha dengeli, daha az iş</text>
 </g>
 </g>
 <g font-family="Poppins" font-size="28" font-weight="600" fill="#2E3B2A">
 <text x="0" y="670">Aynı sayıda bitki için <tspan fill="#2F5D2D" font-weight="800">daha büyük depo,</tspan></text>
 <text x="0" y="710">EC, pH ve sıcaklığı daha yavaş değiştirir.</text>
 <text x="0" y="750">Yer ve bütçe elveriyorsa <tspan fill="#2F5D2D" font-weight="800">büyük olanı seç.</tspan></text>
 </g>
</svg></div>"""

d4 = """<div class="pad" style="padding-top:150px">
<span class="tag">SEÇİM LİSTESİ</span>
<h2 style="font-size:60px;margin:22px 0 26px">İyi bir depo<br>nasıl olmalı?</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🌑</div><p style="font-size:29px"><b>Işık geçirmez (opak):</b> ışık alan suda yosun çoğalır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">♻️</div><p style="font-size:29px"><b>Gıdaya uygun plastik:</b> altında genelde <b>2 (HDPE)</b> veya <b>5 (PP)</b> kodu olur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧢</div><p style="font-size:29px"><b>Sıkı kapak:</b> ışığı, tozu ve buharlaşmayı azaltır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🚰</div><p style="font-size:29px"><b>Kolay boşaltma:</b> alt vana ya da pompayla <span class="hl">tam değişim</span> zahmetsiz olur.</p></div></div>"""

d5 = """<div class="pad" style="padding-top:150px">
<span class="tag">SIK HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunları<br>yapma</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🧴</div><p style="font-size:29px"><b>Şeffaf bidon kullanmak:</b> yosun ve kök sorunları başlar; en azından dışını kapla.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🎨</div><p style="font-size:29px"><b>Boya ya da kimyasal kovası:</b> kalıntı suya geçebilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">☀️</div><p style="font-size:29px"><b>Koyu depoyu güneşte bırakmak:</b> çözelti ısınır, oksijen azalır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">⚙️</div><p style="font-size:29px"><b>Pompayı susuz bırakmak:</b> dalgıç pompa kuru çalışınca bozulabilir; <span class="hl">su seviyesini işaretle.</span></p></div></div>"""

d6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🪣</div><p style="font-size:33px"><b>Büyük depo</b> daha dengelidir.</p></div>
<div class="card"><div class="ic">🌑</div><p style="font-size:33px"><b>Opak</b> ve kapaklı olsun.</p></div>
<div class="card"><div class="ic">♻️</div><p style="font-size:33px"><b>Gıdaya uygun</b> plastik seç.</p></div>
<div class="card"><div class="ic">📏</div><p style="font-size:33px">Su seviyesini <span class="hl">işaretle.</span></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sen deponu neyden yaptın?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Pazı ile<br>pancar<br>aynı<br>türdür! 🌿</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">İkisi de <b>Beta vulgaris.</b> Pancar kökü için, pazı <span class="hl">yaprağı için</span> seçilmiş.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🌱</div><p style="font-size:40px"><b>Topraksız nasıl yetişir?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([p1, p2, p3, p4, p5, p6], "gun22/pazi")
    render_post([d1, d2, d3, d4, d5, d6], "gun22/depo")
    render_story(story, "gun22/hikaye")
