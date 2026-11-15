import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ DOMATES ----------
d1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ DOMATES</span>
<h1 style="margin-top:50px">Domatesi<br>topraksız<br>yetiştir 🍅</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Seralardaki salkım salkım<br><span class="hl">domatesin sırrı ne?</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <line x1="456" y1="0" x2="456" y2="60" stroke="#B59A6E" stroke-width="4"/>
 <path d="M456 60 C450 120 462 180 456 250" stroke="#3C6E3A" stroke-width="12" fill="none"/>
 <g fill="#5E9B4F"><ellipse cx="400" cy="100" rx="48" ry="18" transform="rotate(-20 400 100)"/><ellipse cx="512" cy="150" rx="48" ry="18" transform="rotate(20 512 150)"/><ellipse cx="398" cy="200" rx="44" ry="16" transform="rotate(-15 398 200)"/></g>
 <g fill="#D9483B"><circle cx="530" cy="215" r="26"/><circle cx="572" cy="240" r="24"/><circle cx="525" cy="262" r="22"/></g>
 <g fill="#3C6E3A"><circle cx="530" cy="190" r="6"/><circle cx="572" cy="217" r="6"/></g>
 <rect x="330" y="250" width="252" height="44" rx="12" fill="#B59A6E"/>
</svg></div>"""

d2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NASIL?</span>
<h2>Seralarda<br>en yaygın yol</h2>
<p>Ticari seralarda domates çoğunlukla <b>cocopeat veya kaya yünü</b> torbalarda, <b>damla sulama</b> ile yetiştirilir.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🧱</div><p style="font-size:30px">Fide <b>küpte</b> çimlenir, sonra torbaya/bloğa oturtulur.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">💧</div><p style="font-size:30px">Besin çözeltisi gün içinde <b>az ve sık</b> verilir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🪣</div><p style="font-size:30px">Evde <b>büyük bir kova</b> (DWC) ya da saksıda damla da olur; domates <span class="hl">büyük kök</span> yapar.</p></div></div>"""

d3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÇEŞİT SEÇİMİ</span>
<h2 style="font-size:60px;margin:22px 0 26px">Sırık mı,<br>bodur mu?</h2>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">📏 Sırık (sınırsız büyüyen)</p><p style="font-size:30px;margin-top:8px">Boyu durmadan uzar, aylarca ürün verir. Seralarda <b>ipe sarılarak</b> yukarı yönlendirilir. Tavanı yüksek yerler için.</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🌿 Bodur (sınırlı büyüyen)</p><p style="font-size:30px;margin-top:8px">Belli boyda durur, ürünü daha kısa sürede verir. <span class="hl">Balkon ve küçük sistemler</span> için daha kolay; çeri çeşitleri de iyi seçenek.</p></div></div>"""

d4 = """<div class="pad" style="padding-top:150px">
<span class="tag">BAKIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Sırık domateste<br>temel işler</h2>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px"><b>Koltuk al:</b> yaprakla gövde arasından çıkan yan sürgünleri küçükken kopar; bitki <b>tek gövde</b> kalsın.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧵</div><p style="font-size:29px"><b>İpe sar:</b> gövdeyi tepeden sarkan ipe düzenli sar, salkımların ağırlığını taşısın.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🍃</div><p style="font-size:29px"><b>Alt yaprakları temizle:</b> olgunlaşan salkımın altındaki yaşlı yapraklar hava akışını keser, hastalığa kapı açar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🐝</div><p style="font-size:29px">Kapalı alanda çiçekleri <span class="hl">hafifçe titret</span>, tozlaşmaya yardım et.</p></div></div>"""

d5 = """<div class="pad" style="padding-top:150px">
<span class="tag">DİKKAT</span>
<h2 style="font-size:60px;margin:22px 0 26px">Meyvede<br>sık görülenler</h2>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">⚫ Dipte kararma</p><p style="font-size:29px;margin-top:8px"><b>Çiçek burnu çürüklüğü.</b> Kalsiyumla ilgilidir ama çoğu zaman sebep çözeltide Ca azlığı değil; <span class="hl">düzensiz sulama</span> ya da çok yüksek EC, Ca'nın meyveye taşınmasını engeller.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">💥 Meyve çatlaması</p><p style="font-size:29px;margin-top:8px">Kuru kalan bitkiye birden bol su verilince meyve hızla şişer ve çatlar. Çözüm: <b>dengeli, düzenli sulama.</b></p></div></div>"""

d6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🧱</div><p style="font-size:33px">Ortam + <b>damla sulama</b> en yaygını.</p></div>
<div class="card"><div class="ic">🌿</div><p style="font-size:33px">Küçük alana <b>bodur/çeri</b> çeşit.</p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px">Koltuk al, <b>ipe sar.</b></p></div>
<div class="card"><div class="ic">💧</div><p style="font-size:33px">Sulama <span class="hl">düzenli</span> olsun.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sen domates denedin mi?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: LED MESAFESİ ----------
l1 = """<div class="pad" style="padding-top:150px">
<span class="tag">LED MESAFESİ</span>
<h1 style="margin-top:50px">Lamba<br>ne kadar<br>yakın? 💡</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Çok yakın da kötü, çok uzak da.<br><span class="hl">Doğru mesafeyi bul.</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <rect x="256" y="10" width="400" height="34" rx="10" fill="#2E3B2A"/>
 <g fill="#F7D98B"><rect x="286" y="44" width="40" height="10" rx="4"/><rect x="366" y="44" width="40" height="10" rx="4"/><rect x="446" y="44" width="40" height="10" rx="4"/><rect x="526" y="44" width="40" height="10" rx="4"/><rect x="606" y="44" width="30" height="10" rx="4"/></g>
 <path d="M266 60 L180 250 L732 250 L646 60 Z" fill="#F7D98B" opacity="0.35"/>
 <line x1="800" y1="44" x2="800" y2="236" stroke="#B59A6E" stroke-width="5"/>
 <path d="M786 60 L800 44 L814 60 M786 220 L800 236 L814 220" stroke="#B59A6E" stroke-width="5" fill="none"/>
 <g fill="#5E9B4F"><ellipse cx="330" cy="240" rx="50" ry="24"/><ellipse cx="456" cy="240" rx="50" ry="24"/><ellipse cx="582" cy="240" rx="50" ry="24"/></g>
 <rect x="180" y="256" width="552" height="34" rx="10" fill="#B59A6E"/>
</svg></div>"""

l2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN ÖNEMLİ?</span>
<h2>Mesafe = ışığın<br>şiddeti</h2>
<p>Lamba uzaklaştıkça ışık daha geniş alana yayılır ve bitkinin yaprağına düşen ışık <b>hızla azalır.</b></p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🔆</div><p style="font-size:30px">Bitkinin ihtiyacı <b>yaprağa ulaşan</b> ışıktır, lambanın watt'ı değil.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">📐</div><p style="font-size:30px">Bu yüzden <span class="hl">tek doğru santim yok:</span> mesafe lambanın gücüne, tipine ve bitkiye göre değişir.</p></div></div>"""

l3 = """<div class="pad" style="padding-top:150px">
<span class="tag">BİTKİ SÖYLER</span>
<h2 style="font-size:60px;margin:22px 0 26px">Belirtileri<br>oku</h2>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🔥 Çok yakın</p><p style="font-size:29px;margin-top:8px">Lambaya en yakın tepe yapraklar <b>ağarır, sararır</b> ya da kenarları kıvrılıp kurur.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🌱 Çok uzak</p><p style="font-size:29px;margin-top:8px">Bitki ışığa doğru <b>uzar, incelir</b>, yapraklar arası açılır, rengi soluklaşır. Fidede hemen görülür.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">✅ Doğru</p><p style="font-size:29px;margin-top:8px"><span class="hl">Kısa boğumlu, tıknaz</span>, canlı yeşil bitki.</p></div></div>"""

l4 = """<div class="pad" style="padding-top:150px">
<span class="tag">NASIL AYARLANIR?</span>
<h2 style="font-size:60px;margin:22px 0 26px">Adım adım</h2>
<div class="card" style="padding:20px 32px"><div class="ic">1️⃣</div><p style="font-size:29px">Lambanın <b>üretici tablosuna</b> bak: farklı yüksekliklerde ne kadar ışık verdiğini (PPFD) gösterir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">2️⃣</div><p style="font-size:29px"><b>Fideyle başla:</b> fide daha az ışık ister; lambayı yükselt ya da kısık (dimmer) aç.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">3️⃣</div><p style="font-size:29px">Bitki büyüdükçe <b>lambayı da yukarı al</b>; tepe ile lamba arası mesafe korunsun.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">4️⃣</div><p style="font-size:29px">Emin olmak için <span class="hl">PAR metre</span> ile ölç; telefon uygulamaları sadece kaba fikir verir.</p></div></div>"""

l5 = """<div class="pad" style="padding-top:150px">
<span class="tag">YAPILAN HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunlara<br>dikkat</h2>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>"Elim yanmıyorsa sorun yok" demek:</b> LED az ısınır, el testi yanıltır. Işık ısı olmadan da yaprağı yakabilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Kenarları unutmak:</b> lambanın altındaki merkez, kenarlardan <span class="hl">daha çok ışık</span> alır. Bitkilerin yerini ara sıra değiştir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Bir kere ayarlayıp bırakmak:</b> bitki her hafta uzar, mesafe kısalır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Az ışığı uzun sürede telafi etmeye çalışmak:</b> her bitkinin ışık süresi sınırı vardır.</p></div></div>"""

l6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">📐</div><p style="font-size:33px">Tek doğru santim <b>yok.</b></p></div>
<div class="card"><div class="ic">📄</div><p style="font-size:33px">Üretici <b>PPFD tablosuna</b> bak.</p></div>
<div class="card"><div class="ic">👀</div><p style="font-size:33px">Ağarma = yakın, <span class="hl">uzama = uzak.</span></p></div>
<div class="card"><div class="ic">⬆️</div><p style="font-size:33px">Bitki büyüdükçe <b>lambayı kaldır.</b></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Senin lamban kaç cm yukarıda?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:92px">Domatesin<br>dibi<br>kararıyorsa<br>sorun sulamada<br>olabilir! 🍅</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45"><b>Çiçek burnu çürüklüğü</b> kalsiyumla ilgilidir; ama çoğu zaman çözeltide kalsiyum vardır. <span class="hl">Düzensiz sulamada</span> meyveye yeterince taşınamaz.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🍅</div><p style="font-size:40px"><b>Domates topraksız nasıl yetişir?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([d1, d2, d3, d4, d5, d6], "gun12/domates")
    render_post([l1, l2, l3, l4, l5, l6], "gun12/led")
    render_story(story, "gun12/hikaye")
