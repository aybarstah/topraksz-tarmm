import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: HASAT ZAMANI ----------
h1 = """<div class="pad" style="padding-top:150px">
<span class="tag">HASAT ZAMANI</span>
<h1 style="margin-top:50px">Ne zaman<br>koparmalı?<br>✂️</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Erken de olmaz, geç de.<br><span class="hl">Hasadın püf noktaları.</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <path d="M120 270 Q456 300 792 270 L760 180 L152 180 Z" fill="#B59A6E"/>
 <path d="M152 180 L760 180" stroke="#8C7550" stroke-width="6"/>
 <g fill="#5E9B4F"><ellipse cx="250" cy="150" rx="70" ry="36"/><ellipse cx="300" cy="125" rx="55" ry="30" fill="#7DB56A"/></g>
 <g fill="#D9483B"><circle cx="440" cy="150" r="34"/><circle cx="500" cy="160" r="30"/></g>
 <g fill="#3C6E3A"><circle cx="440" cy="118" r="7"/><circle cx="500" cy="132" r="7"/></g>
 <path d="M600 165 C590 120 640 110 660 130 C680 110 720 125 705 165 Z" fill="#D9483B"/>
 <path d="M640 120 L655 100 L670 120" stroke="#3C6E3A" stroke-width="8" fill="none"/>
</svg></div>"""

h2 = """<div class="pad" style="padding-top:150px">
<span class="tag">GENEL KURAL</span>
<h2>Sabah serinliği<br>en iyi saat</h2>
<p>Sabah erken saatlerde bitkinin dokuları <b>suyla dolu ve diridir;</b> hasat edilen ürün daha geç solar.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🌅</div><p style="font-size:30px">Öğle sıcağında koparılan yeşillik <b>çabuk pörsür.</b></p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🔪</div><p style="font-size:30px">Temiz ve keskin <b>makas/bıçak</b> kullan; yolmak bitkiyi yaralar.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">❄️</div><p style="font-size:30px">Yeşillikleri hasattan sonra <span class="hl">hemen serinlet.</span></p></div></div>"""

h3 = """<div class="pad" style="padding-top:150px">
<span class="tag">YEŞİLLİKLER</span>
<h2 style="font-size:60px;margin:22px 0 26px">Marul ve<br>fesleğen</h2>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🥬 Yaprak marul</p><p style="font-size:30px;margin-top:8px">Tek seferde sökmek zorunda değilsin: <b>dıştaki olgun yaprakları</b> kopar, ortadaki büyüme noktasını bırak. Bitki yeni yaprak vermeye devam eder.</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🌿 Fesleğen</p><p style="font-size:30px;margin-top:8px">Uçtan, bir yaprak çiftinin hemen üstünden kes. <span class="hl">Çiçeklenmeden önce</span> topla; çiçek açınca yapraklar sertleşir, tadı değişir.</p></div></div>"""

h4 = """<div class="pad" style="padding-top:150px">
<span class="tag">MEYVELER</span>
<h2 style="font-size:60px;margin:22px 0 26px">Dalda mı,<br>sonra mı?</h2>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🍅 Domates</p><p style="font-size:29px;margin-top:8px">Koparıldıktan sonra da <b>olgunlaşmaya devam eder.</b> Renk dönmeye başlayınca toplayıp oda sıcaklığında kızartabilirsin.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🍓 Çilek</p><p style="font-size:29px;margin-top:8px">Kopardıktan sonra <span class="hl">olgunlaşmaz.</span> Tamamen kızarınca, sapı ve yeşil çanağıyla birlikte topla.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🫑 Biber</p><p style="font-size:29px;margin-top:8px">Yeşilken de yenir. Kırmızı/sarı rengi istiyorsan dalda bekle; meyveyi <b>makasla</b> kes.</p></div></div>"""

h5 = """<div class="pad" style="padding-top:150px">
<span class="tag">YAPILAN HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunlara<br>dikkat</h2>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Geç kalmak:</b> marul fazla bekleyince <b>tohuma kalkar</b> (uzar), yaprakları acılaşır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Olgun meyveyi dalda unutmak:</b> bitkinin yeni meyve bağlamasını yavaşlatır, düzenli topla.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Domatesi buzdolabına koymak:</b> soğuk, <span class="hl">aromasını azaltır.</span> Oda sıcaklığında sakla.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Bitkiyi bir seferde tıraşlamak:</b> fesleğende yaprakların en fazla üçte birini al.</p></div></div>"""

h6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🌅</div><p style="font-size:33px">Hasadı <b>sabah serinliğinde</b> yap.</p></div>
<div class="card"><div class="ic">🥬</div><p style="font-size:33px">Marulda <b>dış yapraklardan</b> başla.</p></div>
<div class="card"><div class="ic">🍓</div><p style="font-size:33px">Çilek dalda <span class="hl">tam kızarsın.</span></p></div>
<div class="card"><div class="ic">🍅</div><p style="font-size:33px">Domates <b>buzdolabına değil.</b></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Bu hafta ne hasat ettin?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: SİSTEM TEMİZLİĞİ ----------
t1 = """<div class="pad" style="padding-top:150px">
<span class="tag">SİSTEM TEMİZLİĞİ</span>
<h1 style="margin-top:50px">Sezon<br>bitti,<br>şimdi ne? 🧽</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Yeni ekimden önce<br><span class="hl">sistemi sıfırla.</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <rect x="236" y="90" width="440" height="190" rx="22" fill="#FFF9EE" stroke="#B59A6E" stroke-width="8"/>
 <rect x="244" y="170" width="424" height="102" rx="16" fill="#9CC9D9" opacity="0.7"/>
 <g fill="#FFFFFF" stroke="#9CC9D9" stroke-width="4"><circle cx="330" cy="60" r="26"/><circle cx="390" cy="34" r="18"/><circle cx="560" cy="50" r="30"/><circle cx="620" cy="22" r="16"/></g>
 <rect x="700" y="150" width="120" height="70" rx="14" fill="#F7D98B" transform="rotate(-12 760 185)"/>
</svg></div>"""

t2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN?</span>
<h2>Görünmeyen<br>kalıntılar</h2>
<p>Bir sezon boyunca depoda, boruda ve ortamda <b>kök artıkları, yosun, biyofilm (sümüksü tabaka) ve tuz birikintisi</b> oluşur.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🦠</div><p style="font-size:30px">Kök çürüklüğü gibi hastalıkların etkenleri bu kalıntılarda <b>yeni sezona taşınabilir.</b></p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🚿</div><p style="font-size:30px">Birikinti <span class="hl">damlatıcı ve boruları tıkar</span>, pompayı zorlar.</p></div></div>"""

t3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ADIM ADIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Temizlik<br>sırası</h2>
<div class="card" style="padding:20px 32px"><div class="ic">1️⃣</div><p style="font-size:29px"><b>Boşalt:</b> bitkileri, kökleri ve eski çözeltiyi tamamen çıkar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">2️⃣</div><p style="font-size:29px"><b>Fırçala:</b> depo, kanal ve kapakları su ve bulaşık deterjanıyla ovarak <b>görünür kiri</b> sök.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">3️⃣</div><p style="font-size:29px"><b>Dezenfekte et:</b> etiketine uygun seyreltilmiş <b>çamaşır suyu</b> ya da <b>hidrojen peroksit</b> kullan.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">4️⃣</div><p style="font-size:29px"><b>Durula ve kurut:</b> <span class="hl">koku kalmayana kadar</span> bol suyla durula.</p></div></div>"""

t4 = """<div class="pad" style="padding-top:150px">
<span class="tag">PARÇA PARÇA</span>
<h2 style="font-size:60px;margin:22px 0 26px">Unutulan<br>yerler</h2>
<div class="card" style="padding:20px 32px"><div class="ic">⚙️</div><p style="font-size:29px"><b>Pompa:</b> girişindeki süngeri/filtreyi söküp yıka, pervaneye takılan kökleri temizle.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💨</div><p style="font-size:29px"><b>Hava taşı:</b> zamanla tıkanır, kabarcık azalır. Temizle ya da <b>yenisiyle değiştir.</b></p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🚰</div><p style="font-size:29px"><b>Hortum ve damlatıcılar:</b> içinden temizlik çözeltisi geçirip durula, tıkalı olanı değiştir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🟤</div><p style="font-size:29px"><b>Hidroton:</b> kökleri ayıkla, yıka, dezenfekte et; <span class="hl">tekrar kullanılabilir.</span></p></div></div>"""

t5 = """<div class="pad" style="padding-top:150px">
<span class="tag">GÜVENLİK</span>
<h2 style="font-size:60px;margin:22px 0 26px">Asla<br>karıştırma! ⚠️</h2>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">☠️ Çamaşır suyu + sirke/asit</p><p style="font-size:29px;margin-top:8px">Çamaşır suyu; sirke, kireç sökücü ya da pH düşürücü asitle karışınca <span class="hl">zehirli klor gazı</span> çıkarır. Ayrı ayrı kullan, arada bol suyla durula.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🧤 Korun</p><p style="font-size:29px;margin-top:8px"><b>Eldiven ve gözlük</b> tak, havalandırılan bir yerde çalış.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🌱 Bitki varken yapma</p><p style="font-size:29px;margin-top:8px">Bu güçlü temizlik <b>boş sistem</b> içindir.</p></div></div>"""

t6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🪣</div><p style="font-size:33px">Boşalt, <b>fırçala</b>, dezenfekte et.</p></div>
<div class="card"><div class="ic">💧</div><p style="font-size:33px"><b>Bol suyla</b> durula, kurut.</p></div>
<div class="card"><div class="ic">⚙️</div><p style="font-size:33px">Pompa filtresi ve <b>hava taşı</b> da.</p></div>
<div class="card"><div class="ic">⚠️</div><p style="font-size:33px">Çamaşır suyu + asit <span class="hl">asla!</span></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sen sistemini ne sıklıkla temizliyorsun?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:92px">Çilek<br>dalından<br>koptuktan<br>sonra<br>olgunlaşmaz! 🍓</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Domates koparıldıktan sonra da kızarmaya devam eder; çilek ise <span class="hl">dalda tam kızarınca</span> toplanmalı.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">✂️</div><p style="font-size:40px"><b>Hasat ne zaman yapılır?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([h1, h2, h3, h4, h5, h6], "gun13/hasat")
    render_post([t1, t2, t3, t4, t5, t6], "gun13/temizlik")
    render_story(story, "gun13/hikaye")
