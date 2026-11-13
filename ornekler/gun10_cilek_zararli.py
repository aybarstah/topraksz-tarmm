import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ ÇİLEK ----------
c1 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÇİLEK</span>
<h1 style="margin-top:50px">Topraksız<br>çilek<br>yetiştirmek 🍓</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Tarlada değil, askıda:<br><span class="hl">bilmen gereken püf noktaları</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <line x1="120" y1="0" x2="120" y2="60" stroke="#7A6A52" stroke-width="6"/>
 <line x1="790" y1="0" x2="790" y2="60" stroke="#7A6A52" stroke-width="6"/>
 <rect x="60" y="60" width="790" height="60" rx="14" fill="#B59A6E"/>
 <g fill="#5E9B4F">
  <ellipse cx="200" cy="40" rx="50" ry="30"/><ellipse cx="455" cy="40" rx="50" ry="30"/><ellipse cx="710" cy="40" rx="50" ry="30"/>
 </g>
 <g stroke="#3C6E3A" stroke-width="5" fill="none">
  <path d="M200 120 C200 160 230 170 240 200"/><path d="M455 120 C455 170 420 180 410 215"/><path d="M710 120 C710 160 740 170 750 195"/>
 </g>
 <g fill="#C9483A">
  <path d="M215 200 C215 190 265 190 265 200 C265 245 245 270 240 270 C235 270 215 245 215 200 Z"/>
  <path d="M385 215 C385 205 435 205 435 215 C435 260 415 285 410 285 C405 285 385 260 385 215 Z"/>
  <path d="M725 195 C725 185 775 185 775 195 C775 240 755 265 750 265 C745 265 725 240 725 195 Z"/>
 </g>
 <g fill="#F7D98B"><circle cx="232" cy="215" r="3"/><circle cx="248" cy="228" r="3"/><circle cx="236" cy="242" r="3"/><circle cx="402" cy="230" r="3"/><circle cx="418" cy="245" r="3"/><circle cx="405" cy="258" r="3"/><circle cx="742" cy="210" r="3"/><circle cx="758" cy="224" r="3"/><circle cx="746" cy="238" r="3"/></g>
</svg></div>"""

c2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN TOPRAKSIZ?</span>
<h2>Meyve topraktan<br>uzakta kalır</h2>
<p>Çilek, topraksız sistemlerde en çok yetiştirilen meyvelerden biridir. Bitki yukarıda olunca meyve <b>sarkar, toprağa değmez.</b></p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">✨</div><p style="font-size:30px">Daha <b>temiz meyve</b>, eğilmeden <b>rahat hasat.</b></p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🛡️</div><p style="font-size:30px">Toprak kaynaklı hastalık ve zararlı riski <b>azalır.</b></p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🤓</div><p style="font-size:30px"><b>Biliyor muydun?</b> Çileğin üstündeki noktalar tohum değil; her biri <span class="hl">ayrı bir meyvedir.</span></p></div></div>"""

c3 = """<div class="pad" style="padding-top:150px">
<span class="tag">SİSTEMLER</span>
<h2 style="font-size:60px;margin:22px 0 26px">Çilek nerede<br>yetişir?</h2>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🪴 Askılı oluk / torba</p><p style="font-size:30px;margin-top:8px"><b>Cocopeat</b> dolu oluk veya torba + <b>damla sulama.</b> Ticari seralarda çok yaygındır.</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🌊 NFT kanalı</p><p style="font-size:30px;margin-top:8px">Kökler kanalda akan ince besin çözeltisi filminden beslenir.</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🗼 Dikey kule</p><p style="font-size:30px;margin-top:8px">Balkon ve küçük alanlar için: <span class="hl">az yerde çok bitki.</span></p></div></div>"""

c4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÇEŞİT SEÇİMİ</span>
<h2 style="font-size:60px;margin:22px 0 26px">Her çilek<br>aynı değil</h2>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🍂 Kısa gün çeşitleri</p><p style="font-size:30px;margin-top:8px">Kısalan günlerde çiçek tomurcuğu oluşturur. Genelde yılda <b>bir ana hasat</b> verir.</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🔁 Gün nötr çeşitler</p><p style="font-size:30px;margin-top:8px">Gün uzunluğuna bakmaz; sıcaklık uygunsa <b>sürekli çiçek</b> açar. Sera ve kapalı alan için <span class="hl">en uygunu.</span></p></div>
<div class="card" style="padding:22px 32px"><div class="ic">💡</div><p style="font-size:30px">Fide alırken etikette çeşidin <b>tipini</b> mutlaka sor.</p></div></div>"""

c5 = """<div class="pad" style="padding-top:150px">
<span class="tag">DİKKAT</span>
<h2 style="font-size:60px;margin:22px 0 26px">En sık yapılan<br>hatalar</h2>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Tacı gömmek:</b> yaprakların çıktığı kök boğazı ortamın <span class="hl">üstünde</span> kalmalı, gömülürse çürür.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Stolonları bırakmak:</b> uzayan sürgünler enerjiyi yavru bitkiye harcar. Meyve için kopar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Havasız ve nemli ortam:</b> meyvede <b>kurşuni küf</b> (Botrytis) çürümesi yapar. Havalandır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💡</div><p style="font-size:29px"><b>Arı yoksa</b> çiçekleri yumuşak fırçayla tozla, yoksa meyve şekilsiz olur.</p></div></div>"""

c6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🍓</div><p style="font-size:33px">Meyve sarkar, <b>temiz kalır.</b></p></div>
<div class="card"><div class="ic">🔁</div><p style="font-size:33px">Sera için <span class="hl">gün nötr</span> çeşit seç.</p></div>
<div class="card"><div class="ic">👑</div><p style="font-size:33px">Tacı <b>gömme</b>, stolonu <b>kopar.</b></p></div>
<div class="card"><div class="ic">🌬️</div><p style="font-size:33px">Havalandır, küfü <b>önle.</b></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Balkonda çilek dener miydin?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: TOPRAKSIZ TARIMDA ZARARLILAR ----------
a1 = """<div class="pad" style="padding-top:150px">
<span class="tag">ZARARLILAR</span>
<h1 style="margin-top:50px">Toprak yok,<br>böcek de<br>yok mu? 🐛</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Maalesef var.<br><span class="hl">5 yaygın zararlı</span> ve çözümleri.</p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <path d="M80 260 C200 60 480 40 560 160 C480 280 220 300 80 260 Z" fill="#5E9B4F"/>
 <path d="M80 260 C250 200 400 180 560 160" stroke="#3C6E3A" stroke-width="6" fill="none"/>
 <g fill="#FFF9EE" stroke="#B59A6E" stroke-width="3"><circle cx="260" cy="180" r="9"/><circle cx="300" cy="200" r="9"/><circle cx="340" cy="165" r="9"/><circle cx="390" cy="190" r="9"/></g>
 <rect x="660" y="40" width="190" height="240" rx="14" fill="#F2C94C" stroke="#C9962C" stroke-width="6"/>
 <line x1="755" y1="10" x2="755" y2="40" stroke="#7A6A52" stroke-width="6"/>
 <g fill="#2E3B2A"><circle cx="710" cy="100" r="6"/><circle cx="790" cy="130" r="6"/><circle cx="730" cy="190" r="6"/><circle cx="810" cy="220" r="6"/><circle cx="760" cy="160" r="6"/></g>
</svg></div>"""

a2 = """<div class="pad" style="padding-top:150px">
<span class="tag">GERÇEK</span>
<h2>Topraksız ≠<br>zararlısız</h2>
<p>Toprak olmayınca <b>toprak kaynaklı</b> bazı zararlı ve hastalıklar azalır.</p>
<p style="margin-top:30px">Ama yaprakta beslenen böcekler için toprak gerekmez. Seraya şuradan girerler:</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🚪</div><p style="font-size:30px">Açık kapı, <b>havalandırma</b> boşlukları</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌱</div><p style="font-size:30px">Dışarıdan alınan <b>yeni fide</b> ve bitkiler</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">👕</div><p style="font-size:30px"><b>Kıyafet</b>, alet ve ekipmanlar</p></div></div>"""

a3 = """<div class="pad" style="padding-top:150px">
<span class="tag">TANI</span>
<h2 style="font-size:60px;margin:22px 0 22px">Kimi nasıl<br>tanırsın?</h2>
<div class="card" style="padding:16px 30px;margin-bottom:14px"><div class="ic">🟢</div><p style="font-size:27px"><b>Yaprak biti:</b> filiz uçlarında koloni, yaprakta yapışkan tabaka.</p></div>
<div class="card" style="padding:16px 30px;margin-bottom:14px"><div class="ic">🤍</div><p style="font-size:27px"><b>Beyaz sinek:</b> yaprağa dokununca havalanan minik beyaz sinekler.</p></div>
<div class="card" style="padding:16px 30px;margin-bottom:14px"><div class="ic">🕸️</div><p style="font-size:27px"><b>Kırmızı örümcek:</b> yaprakta sarı noktacıklar, ince ağ. <span class="hl">Sıcak ve kuru</span> havayı sever.</p></div>
<div class="card" style="padding:16px 30px;margin-bottom:14px"><div class="ic">🩶</div><p style="font-size:27px"><b>Thrips:</b> yaprakta gümüşi lekeler ve çizgiler.</p></div>
<div class="card" style="padding:16px 30px;margin-bottom:14px"><div class="ic">🦟</div><p style="font-size:27px"><b>Mantar sineği:</b> ortam üstünde minik siyah sinekler; larvası <b>sürekli ıslak</b> ortamda köke zarar verir.</p></div></div>"""

a4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖNLEM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Girmeden<br>durdur</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🟨</div><p style="font-size:29px"><b>Sarı yapışkan tuzak:</b> beyaz sinek, kanatlı yaprak biti ve mantar sineğini yakalar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🟦</div><p style="font-size:29px"><b>Mavi yapışkan tuzak:</b> özellikle <b>thrips</b> için.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🥅</div><p style="font-size:29px"><b>Böcek tülü:</b> havalandırma ve pencerelere ince gözlü file.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔍</div><p style="font-size:29px"><b>Yeni bitkiyi ayrı tut</b>, yaprak altlarını <span class="hl">düzenli</span> kontrol et.</p></div></div>"""

a5 = """<div class="pad" style="padding-top:150px">
<span class="tag">BİYOLOJİK MÜCADELE</span>
<h2 style="font-size:60px;margin:22px 0 26px">Böceğe karşı<br>böcek 🐞</h2>
<div class="card" style="padding:18px 32px"><div class="ic">🐞</div><p style="font-size:29px"><b>Uğur böceği</b> → yaprak biti</p></div>
<div class="card" style="padding:18px 32px"><div class="ic">🕷️</div><p style="font-size:29px"><b>Avcı akar</b> (Phytoseiulus) → kırmızı örümcek</p></div>
<div class="card" style="padding:18px 32px"><div class="ic">🐝</div><p style="font-size:29px"><b>Parazitoit arı</b> (Encarsia) → beyaz sinek</p></div>
<div class="card" style="padding:18px 32px"><div class="ic">🪲</div><p style="font-size:29px"><b>Avcı böcek</b> (Orius) → thrips</p></div>
<div class="card" style="margin-top:26px;padding:22px 32px;background:#F7E3C4"><div class="ic">⚠️</div><p style="font-size:28px">İlaç kullanırsan <b>faydalı böcekler de ölür.</b> Ürüne ruhsatlı ilaç seç, etiketteki <span class="hl">hasat bekleme süresine</span> uy.</p></div></div>"""

a6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🐛</div><p style="font-size:33px">Topraksız sistemde de <b>zararlı olur.</b></p></div>
<div class="card"><div class="ic">🔍</div><p style="font-size:33px">Erken fark et: <b>yaprak altına bak.</b></p></div>
<div class="card"><div class="ic">🟨</div><p style="font-size:33px">Tuzak ve tülle <span class="hl">girişi engelle.</span></p></div>
<div class="card"><div class="ic">🐞</div><p style="font-size:33px">Önce <b>faydalı böcekleri</b> düşün.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Seninkinde en çok hangisi var?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:92px">Çileğin<br>üstündeki<br>noktalar<br>tohum değil! 🍓</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Her biri <b>aken</b> denen <span class="hl">ayrı bir meyvedir</span> ve içinde tek bir tohum taşır. Yediğimiz kırmızı kısım ise büyüyüp etlenen <b>çiçek tablasıdır.</b></p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🍓</div><p style="font-size:40px"><b>Topraksız çilek nasıl yetişir?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([c1, c2, c3, c4, c5, c6], "gun10/cilek")
    render_post([a1, a2, a3, a4, a5, a6], "gun10/zararli")
    render_story(story, "gun10/hikaye")
