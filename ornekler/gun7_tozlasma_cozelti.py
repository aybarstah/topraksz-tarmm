import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: SERADA TOZLAŞMA (DOMATES / ÇİLEK) ----------
c1 = """<div class="pad" style="padding-top:150px">
<span class="tag">SERADA TOZLAŞMA</span>
<h1 style="margin-top:50px">Çiçek var,<br>meyve yok.<br>Neden?</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Domates ve çilekte gizli kahraman:<br><span class="hl">titreşim ve arılar</span></p>
<svg width="912" height="360" viewBox="0 0 912 360" style="position:absolute;bottom:115px;left:84px">
 <path d="M300 20 C300 120 320 220 300 340" stroke="#3C6E3A" stroke-width="12" fill="none"/>
 <g transform="translate(300,150)">
  <g fill="#F2C94C">
   <ellipse cx="0" cy="-70" rx="26" ry="60"/><ellipse cx="0" cy="-70" rx="26" ry="60" transform="rotate(72)"/>
   <ellipse cx="0" cy="-70" rx="26" ry="60" transform="rotate(144)"/><ellipse cx="0" cy="-70" rx="26" ry="60" transform="rotate(216)"/>
   <ellipse cx="0" cy="-70" rx="26" ry="60" transform="rotate(288)"/>
  </g>
  <circle r="34" fill="#C9962C"/>
 </g>
 <g transform="translate(610,130)">
  <ellipse cx="0" cy="0" rx="90" ry="62" fill="#2E3B2A"/>
  <rect x="-40" y="-60" width="34" height="122" fill="#F2C94C"/>
  <rect x="26" y="-60" width="30" height="122" fill="#F2C94C"/>
  <ellipse cx="-20" cy="-80" rx="60" ry="32" fill="#FFFFFF" opacity=".85"/>
  <ellipse cx="40" cy="-76" rx="52" ry="28" fill="#FFFFFF" opacity=".85"/>
  <circle cx="-92" cy="-6" r="30" fill="#2E3B2A"/>
 </g>
 <g stroke="#B59A6E" stroke-width="6" fill="none" stroke-linecap="round">
  <path d="M760 70 q20 20 0 40 q-20 20 0 40"/><path d="M800 50 q24 28 0 56 q-24 28 0 56"/>
 </g>
 <text x="610" y="270" font-family="Poppins" font-size="32" font-weight="700" fill="#3C6E3A" text-anchor="middle">bzzz… 🐝</text>
</svg></div>"""

c2 = """<div class="pad" style="padding-top:150px">
<span class="tag">DOMATESİN SIRRI</span>
<h2>Polen var,<br>ama dökülmüyor</h2>
<p>Domates çiçeği <b>kendine tozlaşır</b>: erkek ve dişi organ aynı çiçektedir.</p>
<p style="margin-top:30px">Ama polen, kapalı bir başçık içinde durur. Dışarı çıkması için çiçeğin <span class="hl">titremesi</span> gerekir.</p>
<p style="margin-top:30px">Açık arazide bunu <b>rüzgâr ve böcekler</b> yapar. Serada hava durgundur; yardım etmezsen meyve tutumu zayıflar.</p></div>"""

c3 = """<div class="pad" style="padding-top:150px">
<span class="tag">KİM YAPAR?</span>
<h2 style="font-size:60px;margin:22px 0 30px">Bombus arısı<br>çiçeği "vızıldatır"</h2>
<div style="display:flex;gap:22px">
 <div class="card" style="flex:1;display:block;padding:40px 30px">
  <div style="font-size:64px;text-align:center">🐝</div>
  <p style="font-weight:800;text-align:center;color:#3C6E3A;margin-bottom:18px">Bombus arısı</p>
  <p style="font-size:32px;margin-bottom:16px">Çiçeğe tutunup kaslarıyla titreşim yapar</p>
  <p style="font-size:32px">Polen bulut gibi dökülür</p>
 </div>
 <div class="card" style="flex:1;display:block;padding:40px 30px">
  <div style="font-size:64px;text-align:center">🍯</div>
  <p style="font-weight:800;text-align:center;color:#B5543A;margin-bottom:18px">Bal arısı</p>
  <p style="font-size:32px;margin-bottom:16px">Bu titreşimi yapamaz</p>
  <p style="font-size:32px">Domates çiçeğini pek tercih etmez</p>
 </div>
</div>
<p style="font-size:30px;margin-top:24px;color:#7A6A52">Bu yüzden domates seralarında ticari <b>bombus kovanları</b> kullanılır. Ziyaret edilen çiçekte kahverengi küçük ısırık izleri görülür.</p></div>"""

c4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÇİLEK</span>
<h2 style="font-size:60px;margin:22px 0 26px">Şekilsiz çilek =<br>eksik tozlaşma</h2>
<p style="font-size:34px">Çileğin üstündeki küçük "tohumlar" aslında <b>meyvecikler</b>dir (aken).</p>
<p style="font-size:34px;margin-top:24px">Döllenen her aken, çevresindeki etli dokunun büyümesini sağlar.</p>
<svg width="912" height="330" viewBox="0 0 912 330" style="margin-top:20px">
 <path d="M150 40 C40 40 40 170 110 240 C150 290 190 310 220 310 C250 310 290 290 330 240 C400 170 400 40 290 40 Z" fill="#D9534F"/>
 <path d="M640 40 C560 40 545 150 590 230 C620 280 650 300 680 300 C720 300 760 220 770 150 C780 80 740 40 700 60 Z" fill="#D9534F"/>
 <g fill="#F7D98B">
  <ellipse cx="150" cy="100" rx="8" ry="12"/><ellipse cx="220" cy="90" rx="8" ry="12"/><ellipse cx="290" cy="100" rx="8" ry="12"/>
  <ellipse cx="120" cy="170" rx="8" ry="12"/><ellipse cx="190" cy="160" rx="8" ry="12"/><ellipse cx="255" cy="160" rx="8" ry="12"/><ellipse cx="320" cy="170" rx="8" ry="12"/>
  <ellipse cx="170" cy="230" rx="8" ry="12"/><ellipse cx="240" cy="230" rx="8" ry="12"/>
  <ellipse cx="700" cy="110" rx="8" ry="12"/><ellipse cx="740" cy="150" rx="8" ry="12"/><ellipse cx="720" cy="210" rx="8" ry="12"/>
 </g>
 <g fill="#B59A6E"><ellipse cx="600" cy="120" rx="6" ry="9"/><ellipse cx="620" cy="190" rx="6" ry="9"/><ellipse cx="650" cy="250" rx="6" ry="9"/></g>
 <g font-family="Poppins" font-size="31" font-weight="700" text-anchor="middle">
  <text x="220" y="20" fill="#3C6E3A">iyi tozlaşmış ✅</text><text x="670" y="20" fill="#B5543A">yarım tozlaşmış ⚠️</text>
 </g>
</svg></div>"""

c5 = """<div class="pad" style="padding-top:150px">
<span class="tag">EVDE / KÜÇÜK SERADA</span>
<h2 style="font-size:60px;margin:22px 0 26px">Arın yoksa<br>sen yardım et</h2>
<div class="card" style="padding:22px 32px"><div class="ic">🍅</div><p style="font-size:30px"><b>Domates:</b> açık çiçek salkımını sapından hafifçe titret ya da tıklat.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🪥</div><p style="font-size:30px"><b>Pratik hile:</b> çalışan elektrikli diş fırçasının sapını salkıma değdir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🖌️</div><p style="font-size:30px"><b>Çilek:</b> yumuşak fırçayla çiçeğin ortasını her yönden nazikçe sür.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">💨</div><p style="font-size:30px"><b>Fan:</b> hafif hava akışı da çiçekleri sallayarak yardım eder.</p></div>
<p style="font-size:30px;margin-top:20px;color:#7A6A52">Birkaç günde bir, polenin kuru olduğu gün ortasında tekrarla.</p></div>"""

c6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🍅</div><p style="font-size:33px">Domates polenini <b>titreşimle</b> bırakır.</p></div>
<div class="card"><div class="ic">🐝</div><p style="font-size:33px">Serada bu işin ustası <span class="hl">bombus arısı.</span></p></div>
<div class="card"><div class="ic">🍓</div><p style="font-size:33px">Şekilsiz çilek, çoğu zaman <b>eksik tozlaşma</b> işaretidir.</p></div>
<div class="card"><div class="ic">🤲</div><p style="font-size:33px">Arı yoksa <b>titreşim, fırça ve hafif hava</b> akışı.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Senin domatesin meyve tutuyor mu?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: ÇÖZELTİYİ NE SIKLIKLA DEĞİŞTİRMELİ? ----------
a1 = """<div class="pad" style="padding-top:150px">
<span class="tag">BESİN ÇÖZELTİSİ</span>
<h1 style="margin-top:50px">Depoyu en son<br>ne zaman<br>boşalttın?</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">EC doğru görünse bile<br>çözelti <span class="hl">yorulur.</span></p>
<svg width="912" height="320" viewBox="0 0 912 320" style="position:absolute;bottom:125px;left:84px">
 <rect x="120" y="60" width="440" height="240" rx="26" fill="#FFF9EE" stroke="#E3D3B8" stroke-width="8"/>
 <rect x="134" y="130" width="412" height="158" rx="16" fill="#8CC0B8"/>
 <g fill="#FFFFFF" opacity=".7"><circle cx="220" cy="200" r="10"/><circle cx="300" cy="240" r="7"/><circle cx="420" cy="190" r="9"/><circle cx="480" cy="250" r="6"/></g>
 <rect x="630" y="70" width="200" height="210" rx="22" fill="#FFF9EE" stroke="#E3D3B8" stroke-width="6"/>
 <rect x="630" y="70" width="200" height="60" rx="22" fill="#B5543A"/><rect x="630" y="104" width="200" height="26" fill="#B5543A"/>
 <rect x="672" y="50" width="14" height="40" rx="7" fill="#7A6A52"/><rect x="774" y="50" width="14" height="40" rx="7" fill="#7A6A52"/>
 <text x="730" y="240" font-family="Poppins" font-size="100" font-weight="800" fill="#2F5D2D" text-anchor="middle">?</text>
</svg></div>"""

a2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN DEĞİŞİR?</span>
<h2>Bitki her şeyi<br>eşit yemez</h2>
<p>Bitki bazı elementleri <b>hızlı</b>, bazılarını <b>yavaş</b> alır. Kullanmadıklarını depoda bırakır.</p>
<p style="margin-top:30px">Su da azalır. Her ekleme yaptığında musluk suyundaki <span class="hl">sodyum ve klorür</span> gibi iyonlar biraz daha birikir.</p>
<p style="margin-top:30px">Sonuç: EC metre "tamam" der, ama içerideki <b>oranlar bozulmuştur.</b></p></div>"""

a3 = """<div class="pad" style="padding-top:150px">
<span class="tag">EC'Yİ OKU</span>
<h2 style="font-size:60px;margin:22px 0 26px">Su eklerken<br>EC sana ipucu verir</h2>
<div class="card" style="padding:34px 34px"><div class="ic">📈</div><p style="font-size:32px"><b>EC yükseliyorsa:</b> bitki sudan çok su alıyor. Sade su ile tamamla.</p></div>
<div class="card" style="padding:34px 34px"><div class="ic">📉</div><p style="font-size:32px"><b>EC düşüyorsa:</b> bitki besini hızlı tüketiyor. Hedef EC'deki çözelti ile tamamla.</p></div>
<div class="card" style="padding:34px 34px"><div class="ic">⚖️</div><p style="font-size:32px"><b>Hep ölçerek ekle:</b> önce su seviyesini tamamla, sonra EC ve pH'a bak.</p></div></div>"""

a4 = """<div class="pad" style="padding-top:150px">
<span class="tag">NE ZAMAN?</span>
<h2 style="font-size:60px;margin:22px 0 26px">Yaygın kural:<br>1–3 haftada bir</h2>
<p style="font-size:34px;margin-bottom:26px">Küçük hobi sistemlerinde çözelti genelde <b>1–3 haftada bir</b> tamamen yenilenir. Erken değiştirmen gereken işaretler:</p>
<div class="card" style="padding:20px 32px"><div class="ic">🔁</div><p style="font-size:30px">Eklediğin su, toplamda <b>depo hacmine</b> ulaştı</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🎢</div><p style="font-size:30px">pH ve EC <b>tutmuyor</b>, sürekli oynuyor</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">👃</div><p style="font-size:30px">Kötü koku, bulanıklık ya da <b>kaygan kök</b></p></div></div>"""

a5 = """<div class="pad" style="padding-top:150px">
<span class="tag">İPUCU</span>
<h2 style="font-size:60px;margin:22px 0 26px">Değişimi kolaylaştır</h2>
<div class="card"><div class="ic">🪣</div><p style="font-size:31px"><b>Küçük depo hızlı bozulur.</b> Büyük depo daha dengeli kalır.</p></div>
<div class="card"><div class="ic">📒</div><p style="font-size:31px"><b>Defter tut:</b> tarih, eklenen su, EC ve pH. Düzen kendini gösterir.</p></div>
<div class="card"><div class="ic">🧽</div><p style="font-size:31px"><b>Boşaltınca depoyu sil,</b> dibe çöken tortuyu temizle.</p></div>
<div class="card"><div class="ic">🌳</div><p style="font-size:31px"><b>Eski çözeltiyi dökme:</b> seyreltip bahçe bitkilerinde kullan.</p></div></div>"""

a6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">⚖️</div><p style="font-size:33px">Doğru EC, <b>doğru oran</b> demek değil.</p></div>
<div class="card"><div class="ic">📈</div><p style="font-size:33px">EC'nin yönü, nasıl tamamlayacağını söyler.</p></div>
<div class="card"><div class="ic">🗓️</div><p style="font-size:33px">Hobi sistemde <span class="hl">1–3 haftada bir</span> tam değişim.</p></div>
<div class="card"><div class="ic">📒</div><p style="font-size:33px">Ölç, yaz, sonra karar ver.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sen çözeltini kaç günde değiştiriyorsun?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:100px">Domates<br>çiçeği,<br>sallanmadan<br>polen vermez! 🍅</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Polen kapalı başçıkta durur. Bombus arısı çiçeği <b>titreştirerek</b> poleni <span class="hl">döker.</span></p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🐝</div><p style="font-size:40px"><b>Serada arı yoksa ne yapmalı?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([c1, c2, c3, c4, c5, c6], "gun7/tozlasma")
    render_post([a1, a2, a3, a4, a5, a6], "gun7/cozelti")
    render_story(story, "gun7/hikaye")
