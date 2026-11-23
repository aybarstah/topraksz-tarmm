import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ KİŞNİŞ ----------
k1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ KİŞNİŞ</span>
<h1 style="margin-top:50px">Kişniş<br>neden hep<br>çiçeğe<br>kaçıyor? 🌿</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Sırrı <span class="hl">serinlikte</span><br>ve doğru ekimde.</p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(650 0)">
  <path d="M70 200 Q45 140 20 70" stroke="#3C6E3A" stroke-width="5" fill="none"/>
  <path d="M70 200 L70 40" stroke="#3C6E3A" stroke-width="5"/>
  <path d="M70 200 Q95 140 120 70" stroke="#3C6E3A" stroke-width="5" fill="none"/>
  <g fill="#5E9B4F"><circle cx="20" cy="66" r="20"/><circle cx="6" cy="84" r="13"/><circle cx="34" cy="88" r="13"/>
  <circle cx="70" cy="36" r="22"/><circle cx="54" cy="56" r="13"/><circle cx="86" cy="56" r="13"/>
  <circle cx="120" cy="66" r="20"/><circle cx="106" cy="88" r="13"/><circle cx="134" cy="84" r="13"/></g>
  <rect x="5" y="195" width="130" height="32" rx="8" fill="#5B6B57"/>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="120" y="110">Sıcak + uzun gün →</text><text x="120" y="150" fill="#7A6A52" font-size="26">çiçek sapı, az yaprak</text></g>
 <path d="M470 120 L600 120" stroke="#7A6A52" stroke-width="5"/><path d="M588 108 L605 120 L588 132" stroke="#7A6A52" stroke-width="5" fill="none"/>
</svg></div>"""

k2 = """<div class="pad" style="padding-top:150px">
<span class="tag">TANIYALIM</span>
<h2>Maydanozun<br>akrabası</h2>
<p>Kişniş, maydanoz ve dereotuyla <b>aynı aileden</b> gelir. Hem yaprağı hem tohumu mutfakta kullanılır.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">❄️</div><p style="font-size:30px"><b>Serin mevsim bitkisidir;</b> sıcakta yaprak yerine çiçeğe yönelir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🥕</div><p style="font-size:30px"><b>Kazık kökü</b> vardır; sonradan yer değiştirmekten pek hoşlanmaz.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🧼</div><p style="font-size:30px">Bazı insanlara <span class="hl">sabun gibi</span> gelir; bunun kısmen genetik olduğu düşünülüyor.</p></div></div>"""

k3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Bir “tohum”,<br>iki bitki</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="20" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="321" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="622" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <text x="155" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">1</text>
 <text x="456" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">2</text>
 <text x="757" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">3</text>
 <circle cx="155" cy="250" r="70" fill="#C9A46A" stroke="#A8844E" stroke-width="5"/>
 <g stroke="#A8844E" stroke-width="3" fill="none"><path d="M110 200 Q155 250 110 300"/><path d="M200 200 Q155 250 200 300"/><path d="M155 180 L155 320"/></g>
 <path d="M386 250 A60 60 0 0 1 446 190 L446 310 A60 60 0 0 1 386 250 Z" fill="#C9A46A" stroke="#A8844E" stroke-width="5"/>
 <path d="M526 250 A60 60 0 0 0 466 190 L466 310 A60 60 0 0 0 526 250 Z" fill="#C9A46A" stroke="#A8844E" stroke-width="5"/>
 <rect x="672" y="300" width="170" height="110" rx="12" fill="#C9B48E"/>
 <g stroke="#A8916A" stroke-width="3"><line x1="672" y1="335" x2="842" y2="335"/><line x1="672" y1="370" x2="842" y2="370"/></g>
 <path d="M725 300 L725 210" stroke="#5E9B4F" stroke-width="5"/><path d="M790 300 L790 200" stroke="#5E9B4F" stroke-width="5"/>
 <g fill="#5E9B4F"><ellipse cx="711" cy="205" rx="20" ry="9" transform="rotate(-25 711 205)"/><ellipse cx="739" cy="205" rx="20" ry="9" transform="rotate(25 739 205)"/>
 <ellipse cx="776" cy="195" rx="20" ry="9" transform="rotate(-25 776 195)"/><ellipse cx="804" cy="195" rx="20" ry="9" transform="rotate(25 804 195)"/></g>
 </g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
 <text x="155" y="500" text-anchor="middle">Yuvarlak “tohum”</text><text x="155" y="536" text-anchor="middle">aslında içinde</text><text x="155" y="572" text-anchor="middle">2 tohum taşır</text>
 <text x="456" y="500" text-anchor="middle">Ekmeden önce</text><text x="456" y="536" text-anchor="middle">hafifçe bastırıp</text><text x="456" y="572" text-anchor="middle">ikiye ayır</text>
 <text x="757" y="500" text-anchor="middle">Kaya yünü küpe</text><text x="757" y="536" text-anchor="middle">doğrudan ek;</text><text x="757" y="572" text-anchor="middle">fideyi taşıma</text>
 </g>
</svg></div>"""

k4 = """<div class="pad" style="padding-top:150px">
<span class="tag">BAKIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Yaprakta<br>tutmak için</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🫙</div><p style="font-size:29px"><b>Kratky, DWC ve NFT</b> uygundur; küpü en baştan son yerine koy.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:29px"><b>Serin ortam</b> ister; sıcak, çiçeğe kalkmayı hızlandırır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">☀️</div><p style="font-size:29px"><b>Aydınlık yer</b> ama çok uzun ışık süresinden kaçın; uzun gün de kalkmayı tetikler.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🏷️</div><p style="font-size:29px">Tohum alırken <span class="hl">geç tohuma kalkan</span> çeşitleri seç.</p></div></div>"""

k5 = """<div class="pad" style="padding-top:150px">
<span class="tag">HASAT &amp; HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Sık sık<br>kes</h2>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px"><b>Dıştaki sapları dibe yakın</b> kes; ortadaki genç sürgünler büyüsün.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪶</div><p style="font-size:29px"><b>Yapraklar incecik, tüy gibi</b> olmaya başladıysa çiçeğe kalkıyordur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">⏳</div><p style="font-size:29px"><b>Sabırsızlık:</b> çimlenme rokadan yavaştır, çoğu zaman 1-2 hafta sürer.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📆</div><p style="font-size:29px">Kesintisiz yaprak için <span class="hl">birkaç haftada bir</span> yeni tohum ek.</p></div></div>"""

k6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🌰</div><p style="font-size:33px">Tohumu <b>ikiye ayırıp</b> ek.</p></div>
<div class="card"><div class="ic">🚫</div><p style="font-size:33px">Fideyi <b>taşıma</b>, yerinde ek.</p></div>
<div class="card"><div class="ic">❄️</div><p style="font-size:33px"><b>Serin</b> tut, sık hasat et.</p></div>
<div class="card"><div class="ic">📆</div><p style="font-size:33px">Kademeli ek, <span class="hl">hep taze</span> olsun.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Kişniş sana taze mi gelir, sabun mu?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: HAVA POMPASI VE HAVA TAŞI ----------
h1 = """<div class="pad" style="padding-top:150px">
<span class="tag">EKİPMAN</span>
<h1 style="margin-top:50px">Kökler<br>de nefes<br>alır! 🫧</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Hava pompası ve<br><span class="hl">hava taşı rehberi</span></p>
<svg width="912" height="250" viewBox="0 0 912 250" style="position:absolute;bottom:110px;left:84px">
 <g transform="translate(600 0)">
  <rect x="0" y="80" width="300" height="165" rx="16" fill="#CFE3EE" stroke="#9BBFD0" stroke-width="5"/>
  <rect x="6" y="110" width="288" height="130" rx="12" fill="#9CC9DA"/>
  <rect x="110" y="215" width="80" height="20" rx="10" fill="#7A6A52"/>
  <g fill="#FFFFFF" opacity="0.85"><circle cx="130" cy="195" r="7"/><circle cx="150" cy="180" r="9"/><circle cx="170" cy="196" r="6"/>
  <circle cx="140" cy="155" r="8"/><circle cx="162" cy="140" r="7"/><circle cx="148" cy="120" r="6"/></g>
  <path d="M150 215 L150 40 L-40 40" stroke="#5B6B57" stroke-width="6" fill="none"/>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="0" y="60">Pompa → hortum → taş</text><text x="0" y="100" fill="#7A6A52" font-size="26">kabarcık suyu karıştırır</text></g>
</svg></div>"""

h2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN GEREKLİ?</span>
<h2>Durgun su,<br>havasız kök</h2>
<p>Kökler de <b>oksijen kullanır.</b> Kökü sürekli suda duran sistemlerde (DWC gibi) oksijen zamanla azalır.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🫧</div><p style="font-size:30px"><b>Kabarcıklar suyu karıştırır;</b> yüzeydeki hareket havayla oksijen alışverişini artırır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌡️</div><p style="font-size:30px"><b>Ilık su daha az oksijen tutar;</b> yazın havalandırma daha da önemlidir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🦠</div><p style="font-size:30px">Havasız kalan kök zayıflar ve <span class="hl">kök çürümesine</span> açık hale gelir.</p></div></div>"""

h3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Doğru<br>bağlantı</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="0" y="0" width="912" height="560" rx="26" fill="#FFF9EE"/>
 <rect x="40" y="60" width="200" height="120" rx="20" fill="#5B6B57"/>
 <circle cx="95" cy="120" r="22" fill="#7E8E79"/><rect x="140" y="105" width="70" height="30" rx="8" fill="#7E8E79"/>
 <text x="140" y="220" font-size="28" text-anchor="middle" fill="#2F5D2D">Pompa</text>
 <text x="140" y="254" font-size="22" text-anchor="middle" fill="#7A6A52" font-weight="600">su seviyesinin üstünde</text>
 <path d="M240 120 L440 120" stroke="#9BBFD0" stroke-width="10" stroke-linecap="round"/>
 <path d="M440 120 L560 120 L560 470" stroke="#9BBFD0" stroke-width="10" fill="none" stroke-linecap="round"/>
 <rect x="410" y="95" width="70" height="50" rx="10" fill="#F7D98B" stroke="#C9A646" stroke-width="4"/>
 <path d="M430 108 L460 120 L430 132 Z" fill="#7A6A52"/>
 <text x="445" y="200" font-size="28" text-anchor="middle" fill="#2F5D2D">Çek valf</text>
 <text x="445" y="234" font-size="22" text-anchor="middle" fill="#7A6A52" font-weight="600">suyun geri kaçmasını önler</text>
 <rect x="440" y="300" width="420" height="230" rx="16" fill="#CFE3EE" stroke="#9BBFD0" stroke-width="5"/>
 <rect x="446" y="330" width="408" height="194" rx="12" fill="#9CC9DA"/>
 <rect x="520" y="470" width="80" height="26" rx="12" fill="#7A6A52"/>
 <g fill="#FFFFFF" opacity="0.9"><circle cx="545" cy="450" r="8"/><circle cx="570" cy="430" r="10"/><circle cx="590" cy="452" r="7"/>
 <circle cx="555" cy="395" r="9"/><circle cx="582" cy="375" r="8"/><circle cx="565" cy="350" r="7"/></g>
 <text x="720" y="420" font-size="28" text-anchor="middle" fill="#2F5D2D">Hava taşı</text>
 <text x="720" y="454" font-size="22" text-anchor="middle" fill="#2E3B2A" font-weight="600">depo dibinde</text>
 </g>
 <g font-family="Poppins" font-size="28" font-weight="600" fill="#2E3B2A">
 <text x="0" y="620">Pompa elektrik kesilince suyu geri</text>
 <text x="0" y="660">çekebilir: <tspan fill="#2F5D2D" font-weight="800">çek valf tak</tspan> ya da pompayı</text>
 <text x="0" y="700">su seviyesinden <tspan fill="#2F5D2D" font-weight="800">yukarıya</tspan> koy.</text>
 </g>
</svg></div>"""

h4 = """<div class="pad" style="padding-top:150px">
<span class="tag">KURULUM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Doğru<br>yerleştir</h2>
<div class="card" style="padding:20px 32px"><div class="ic">⏱️</div><p style="font-size:29px"><b>DWC'de pompa genelde 7/24 çalışır;</b> zamanlayıcıya bağlama.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔀</div><p style="font-size:29px"><b>Birden çok taş</b> için çoklu vana kullan; pompanın gücü hepsine yetmeli.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">〰️</div><p style="font-size:29px"><b>Hortum bükülmesin, ezilmesin;</b> kıvrılan hortum havayı keser.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔇</div><p style="font-size:29px">Titreşim sesini azaltmak için pompayı <span class="hl">yumuşak bir altlığa</span> koy.</p></div></div>"""

h5 = """<div class="pad" style="padding-top:150px">
<span class="tag">BAKIM &amp; HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Kabarcık<br>azaldıysa</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🪨</div><p style="font-size:29px"><b>Taş tıkanmış olabilir:</b> tuz ve biyofilm gözenekleri kapatır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧽</div><p style="font-size:29px"><b>Temizle ya da yenile;</b> hava taşı ucuz bir sarf malzemesidir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">👂</div><p style="font-size:29px"><b>Pompa sesini dinle:</b> ses değiştiyse zarı yıpranmış olabilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🫙</div><p style="font-size:29px">Kratky'de pompa yok; orada kökler <span class="hl">üstteki hava boşluğundan</span> nefes alır.</p></div></div>"""

h6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🫧</div><p style="font-size:33px">Durgun suya <b>hava ver.</b></p></div>
<div class="card"><div class="ic">⬆️</div><p style="font-size:33px">Pompa <b>yukarıda</b> ya da çek valfli.</p></div>
<div class="card"><div class="ic">〰️</div><p style="font-size:33px">Hortumu <b>bükme.</b></p></div>
<div class="card"><div class="ic">🪨</div><p style="font-size:33px">Taşı <span class="hl">temiz tut.</span></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sisteminde hava pompası var mı?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Bir kişniş<br>“tohumu”<br>aslında<br>iki tohum! 🌿</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Yuvarlak kabuğun içinde <span class="hl">iki tohum</span> saklıdır. Ekmeden önce hafifçe ikiye ayırabilirsin.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🌱</div><p style="font-size:40px"><b>Topraksız nasıl yetişir?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([k1, k2, k3, k4, k5, k6], "gun20/kisnis")
    render_post([h1, h2, h3, h4, h5, h6], "gun20/havapompasi")
    render_story(story, "gun20/hikaye")
