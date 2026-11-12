import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: AKUAPONİK (BALIK + BİTKİ) ----------
c1 = """<div class="pad" style="padding-top:150px">
<span class="tag">AKUAPONİK</span>
<h1 style="margin-top:50px">Balık<br>besliyor,<br>bitki büyüyor 🐟</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Aynı suyu paylaşan iki canlı:<br><span class="hl">balık + bitki</span> bir arada.</p>
<svg width="912" height="330" viewBox="0 0 912 330" style="position:absolute;bottom:115px;left:84px">
 <rect x="40" y="150" width="380" height="170" rx="22" fill="#9CC8C9" stroke="#7A6A52" stroke-width="6"/>
 <g transform="translate(160,235)"><ellipse rx="54" ry="26" fill="#E58A3A"/><path d="M50 0 L90 -26 L90 26 Z" fill="#E58A3A"/><circle cx="-30" cy="-6" r="6" fill="#2E3B2A"/></g>
 <g transform="translate(310,270) scale(.7)"><ellipse rx="54" ry="26" fill="#C9962C"/><path d="M50 0 L90 -26 L90 26 Z" fill="#C9962C"/><circle cx="-30" cy="-6" r="6" fill="#2E3B2A"/></g>
 <rect x="510" y="200" width="370" height="70" rx="16" fill="#B59A6E"/>
 <g fill="#5E9B4F">
  <ellipse cx="580" cy="160" rx="34" ry="52"/><ellipse cx="695" cy="150" rx="38" ry="62"/><ellipse cx="810" cy="160" rx="34" ry="52"/>
 </g>
 <g stroke="#3C6E3A" stroke-width="6"><line x1="580" y1="205" x2="580" y2="190"/><line x1="695" y1="205" x2="695" y2="190"/><line x1="810" y1="205" x2="810" y2="190"/></g>
 <path d="M420 190 C470 150 480 150 510 210" stroke="#3C6E3A" stroke-width="8" fill="none" stroke-dasharray="14 10"/>
 <path d="M700 270 C700 320 520 320 425 290" stroke="#3C6E3A" stroke-width="8" fill="none" stroke-dasharray="14 10"/>
 <text x="465" y="130" font-family="Poppins" font-size="44" text-anchor="middle">💧</text>
</svg></div>"""

c2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDİR?</span>
<h2>Balık çiftliği +<br>topraksız tarım</h2>
<p><b>Akuaponik</b>, balık yetiştiriciliği ile topraksız tarımın aynı su döngüsünde birleştiği sistemdir.</p>
<p style="margin-top:30px">Balığın atığı bitkiye <b>besin</b> olur. Bitki de suyu temizleyip balığa <span class="hl">geri gönderir.</span></p>
<p style="margin-top:30px">Sisteme dışarıdan giren ana girdi <b>balık yemidir.</b></p></div>"""

c3 = """<div class="pad" style="padding-top:150px">
<span class="tag">DÖNGÜ</span>
<h2 style="font-size:60px;margin:22px 0 26px">Asıl işçi:<br>bakteriler 🦠</h2>
<div class="card" style="padding:22px 32px"><div class="ic">🐟</div><p style="font-size:30px"><b>Balık</b> solungaç ve dışkıyla suya <b>amonyak</b> bırakır. Amonyak balık için zehirlidir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🦠</div><p style="font-size:30px"><b>Nitrifikasyon bakterileri</b> amonyağı önce <b>nitrite</b>, sonra <b>nitrata</b> çevirir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌱</div><p style="font-size:30px"><b>Bitki</b> nitratı azot kaynağı olarak kökünden alır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🔁</div><p style="font-size:30px"><b>Temizlenen su</b> balık tankına geri döner.</p></div></div>"""

c4 = """<div class="pad" style="padding-top:150px">
<span class="tag">NELER YETİŞİR?</span>
<h2 style="font-size:60px;margin:22px 0 26px">Kim, kiminle?</h2>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🐟 Balıklar</p><p style="font-size:30px;margin-top:8px"><b>Tilapya</b> ve <b>sazan</b> dayanıklıdır, en çok tercih edilenlerdir. Soğuk suyu seven <b>alabalık</b> da kullanılır.</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🥬 Kolay bitkiler</p><p style="font-size:30px;margin-top:8px"><b>Marul, fesleğen, nane, roka:</b> az besin isteyen yeşillikler.</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🍅 Daha zor olanlar</p><p style="font-size:30px;margin-top:8px"><b>Domates, biber:</b> meyve için daha çok besin ister; olgun ve kalabalık bir sistem gerekir.</p></div></div>"""

c5 = """<div class="pad" style="padding-top:150px">
<span class="tag">DİKKAT</span>
<h2 style="font-size:60px;margin:22px 0 26px">Yeni başlayanın<br>hataları</h2>
<div class="card" style="padding:22px 32px"><div class="ic">❌</div><p style="font-size:30px"><b>Balığı ilk gün koymak:</b> bakteri kolonisinin oturması <span class="hl">birkaç hafta</span> sürer.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">❌</div><p style="font-size:30px"><b>Fazla yem atmak:</b> artan yem çürür, amonyak yükselir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">❌</div><p style="font-size:30px"><b>İlaç kullanmak:</b> bitkiye sıkılan pestisit suya karışır, balığa zarar verir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">💡</div><p style="font-size:30px"><b>pH dengesi:</b> balık, bakteri ve bitki için orta yol olan nötre yakın pH hedeflenir.</p></div></div>"""

c6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🐟</div><p style="font-size:33px">Balık atığı = <b>bitki besini.</b></p></div>
<div class="card"><div class="ic">🦠</div><p style="font-size:33px">Amonyağı nitrata <span class="hl">bakteriler</span> çevirir.</p></div>
<div class="card"><div class="ic">🥬</div><p style="font-size:33px">Başlangıç için <b>yeşillikler</b> en kolayı.</p></div>
<div class="card"><div class="ic">⏳</div><p style="font-size:33px">Sabırlı ol: sistem <b>haftalarla</b> olgunlaşır.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Evde balık + marul dener miydin?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: TOPRAKSIZ ÜRÜN HAKKINDA YANLIŞ BİLİNENLER ----------
a1 = """<div class="pad" style="padding-top:150px">
<span class="tag">YANLIŞ BİLİNENLER</span>
<h1 style="margin-top:50px">"Topraksız<br>ürün tatsız<br>ve zararlı"</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Gerçekten öyle mi?<br><span class="hl">4 efsaneyi</span> tek tek ele alalım.</p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:125px;left:84px">
 <circle cx="300" cy="160" r="120" fill="#C9483A"/>
 <path d="M300 45 C280 20 250 20 235 35 M300 45 C320 20 350 20 365 35 M300 45 L300 20" stroke="#3C6E3A" stroke-width="12" fill="none" stroke-linecap="round"/>
 <ellipse cx="255" cy="120" rx="30" ry="18" fill="#E58A7A" opacity=".7"/>
 <circle cx="640" cy="150" r="110" fill="#FFF9EE" stroke="#B59A6E" stroke-width="10"/>
 <text x="640" y="200" font-family="Poppins" font-size="150" font-weight="800" fill="#B5543A" text-anchor="middle">?</text>
</svg></div>"""

a2 = """<div class="pad" style="padding-top:150px">
<span class="tag">EFSANE 1</span>
<h2>"Topraksız =<br>GDO'lu"</h2>
<p style="font-size:44px;font-weight:800;color:#B5543A">❌ Yanlış.</p>
<p style="margin-top:24px">Topraksız tarım bir <b>yetiştirme yöntemidir</b>, tohumun genetiğini değiştirmez.</p>
<p style="margin-top:30px">Toprakta ekilen domates tohumuyla aynı tohum kullanılabilir. Fark sadece köklerin <span class="hl">toprak yerine</span> besin çözeltisi ya da cocopeat, kaya yünü gibi ortamlarda büyümesidir.</p></div>"""

a3 = """<div class="pad" style="padding-top:150px">
<span class="tag">EFSANE 2</span>
<h2>"Kimyasal gübreyle<br>büyüyor, zararlı"</h2>
<p style="font-size:44px;font-weight:800;color:#B5543A">❌ Yanlış.</p>
<p style="margin-top:24px">Bitki, toprakta da besini <b>suda çözünmüş mineral iyonları</b> olarak alır: nitrat, potasyum, kalsiyum…</p>
<p style="margin-top:30px">Topraksız tarımda bu mineraller <span class="hl">doğrudan ve ölçülü</span> verilir. Kök, aynı azotu toprakta da çözeltide de aynı biçimde emer.</p></div>"""

a4 = """<div class="pad" style="padding-top:150px">
<span class="tag">EFSANE 3</span>
<h2>"Domatesi<br>tatsız olur"</h2>
<p style="font-size:44px;font-weight:800;color:#B5543A">❌ Yöntem değil, koşullar.</p>
<p style="margin-top:24px;font-size:34px">Tadı belirleyenler toprak ya da topraksız olmaktan çok şunlardır:</p>
<div class="card" style="margin-top:24px;padding:20px 32px"><div class="ic">🧬</div><p style="font-size:30px"><b>Çeşit:</b> raf ömrü için seçilen çeşitler daha az aromalı olabilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">☀️</div><p style="font-size:30px"><b>Işık:</b> az ışıkta meyvede daha az şeker birikir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">⏰</div><p style="font-size:30px"><b>Hasat:</b> erken toplanan meyve dalında olgunlaşan kadar tatlı olmaz.</p></div></div>"""

a5 = """<div class="pad" style="padding-top:150px">
<span class="tag">EFSANE 4</span>
<h2>"Topraksız ürünün<br>besin değeri düşük"</h2>
<p style="font-size:44px;font-weight:800;color:#B5543A">❌ Kanıt yok.</p>
<p style="margin-top:24px;font-size:34px">Vitamin ve mineral içeriği; <b>çeşit, ışık, besin dengesi ve tazelik</b> gibi etkenlere bağlıdır.</p>
<p style="margin-top:26px;font-size:34px">Karşılaştıran çalışmalarda topraksız ürünler genel olarak topraklı ürünlere <span class="hl">benzer</span> değerler gösterir.</p>
<div class="card" style="margin-top:30px;padding:24px 32px"><div class="ic">💡</div><p style="font-size:30px"><b>Bonus:</b> yakında yetişip taze tüketilen ürün, yolda günler geçirenden avantajlıdır.</p></div></div>"""

a6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🧬</div><p style="font-size:33px">Topraksız ≠ <b>GDO.</b></p></div>
<div class="card"><div class="ic">🧪</div><p style="font-size:33px">Bitki her yerde <b>aynı mineralleri</b> alır.</p></div>
<div class="card"><div class="ic">🍅</div><p style="font-size:33px">Tadı <span class="hl">çeşit, ışık, hasat</span> belirler.</p></div>
<div class="card"><div class="ic">🥗</div><p style="font-size:33px">Besin değeri <b>benzer.</b></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sen hangisini duymuştun?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:96px">Balığın<br>atığı,<br>bitkinin<br>besini! 🐟🌱</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Balık suya <b>amonyak</b> bırakır. Bakteriler onu <span class="hl">nitrata</span> çevirir, bitki de bunu besin olarak kullanır.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🔁</div><p style="font-size:40px"><b>Akuaponik nasıl çalışır?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([c1, c2, c3, c4, c5, c6], "gun9/akuaponik")
    render_post([a1, a2, a3, a4, a5, a6], "gun9/yanlisbilinen")
    render_story(story, "gun9/hikaye")
