import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: FESLEĞEN BUDAMA ----------
c1 = """<div class="pad" style="padding-top:150px">
<span class="tag">FESLEĞEN BUDAMA</span>
<h1 style="margin-top:50px">Kestikçe<br>gürleşen<br>bitki 🌿</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Fesleğenini doğru yerden kes,<br><span class="hl">bir dal yerine iki dal</span> çıksın.</p>
<svg width="912" height="360" viewBox="0 0 912 360" style="position:absolute;bottom:115px;left:84px">
 <rect x="330" y="270" width="250" height="90" rx="18" fill="#B59A6E"/>
 <path d="M455 280 L455 120" stroke="#3C6E3A" stroke-width="12" fill="none"/>
 <path d="M455 130 C420 90 400 50 390 20" stroke="#3C6E3A" stroke-width="10" fill="none"/>
 <path d="M455 130 C490 90 510 50 520 20" stroke="#3C6E3A" stroke-width="10" fill="none"/>
 <g fill="#5E9B4F">
  <ellipse cx="400" cy="230" rx="55" ry="26" transform="rotate(-20 400 230)"/>
  <ellipse cx="510" cy="230" rx="55" ry="26" transform="rotate(20 510 230)"/>
  <ellipse cx="405" cy="170" rx="48" ry="23" transform="rotate(-25 405 170)"/>
  <ellipse cx="505" cy="170" rx="48" ry="23" transform="rotate(25 505 170)"/>
  <ellipse cx="350" cy="60" rx="42" ry="20" transform="rotate(-30 350 60)"/>
  <ellipse cx="420" cy="40" rx="36" ry="18" transform="rotate(20 420 40)"/>
  <ellipse cx="490" cy="40" rx="36" ry="18" transform="rotate(-20 490 40)"/>
  <ellipse cx="560" cy="60" rx="42" ry="20" transform="rotate(30 560 60)"/>
 </g>
 <g transform="translate(660,110) rotate(-30)">
  <circle cx="0" cy="0" r="26" fill="none" stroke="#7A6A52" stroke-width="9"/>
  <circle cx="0" cy="70" r="26" fill="none" stroke="#7A6A52" stroke-width="9"/>
  <path d="M20 14 L120 60 M20 56 L120 10" stroke="#7A6A52" stroke-width="10" stroke-linecap="round"/>
 </g>
</svg></div>"""

c2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN BUDAMALI?</span>
<h2>Tepe büyüdükçe<br>yanlar bekler</h2>
<p>Fesleğenin <b>tepe sürgünü</b> büyürken, alttaki yan tomurcuklar uykuda kalır. Bitki tek gövdeyle boylanır.</p>
<p style="margin-top:30px">Tepeyi kestiğinde o boğumdaki iki yan tomurcuk uyanır ve <span class="hl">iki yeni dal</span> verir.</p>
<p style="margin-top:30px">Fesleğen <b>tek yıllıktır</b>: çiçeğe kalkınca enerjisini tohuma verir, yeni yaprak üretimi yavaşlar.</p></div>"""

c3 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEREDEN KESİLİR?</span>
<h2 style="font-size:60px;margin:22px 0 10px">Yaprak çiftinin<br>hemen üstünden</h2>
<svg width="912" height="700" viewBox="0 0 912 700">
 <path d="M300 690 L300 120" stroke="#3C6E3A" stroke-width="14"/>
 <g fill="#5E9B4F">
  <ellipse cx="225" cy="590" rx="70" ry="30" transform="rotate(-15 225 590)"/>
  <ellipse cx="375" cy="590" rx="70" ry="30" transform="rotate(15 375 590)"/>
  <ellipse cx="230" cy="420" rx="64" ry="28" transform="rotate(-15 230 420)"/>
  <ellipse cx="370" cy="420" rx="64" ry="28" transform="rotate(15 370 420)"/>
  <ellipse cx="240" cy="160" rx="54" ry="24" transform="rotate(-20 240 160)"/>
  <ellipse cx="360" cy="160" rx="54" ry="24" transform="rotate(20 360 160)"/>
 </g>
 <g fill="#9CCB7E"><circle cx="286" cy="392" r="12"/><circle cx="314" cy="392" r="12"/></g>
 <line x1="170" y1="360" x2="430" y2="360" stroke="#B5543A" stroke-width="7" stroke-dasharray="18 12"/>
 <text x="440" y="370" font-family="Poppins" font-size="34" font-weight="800" fill="#B5543A">✂️ buradan kes</text>
 <path d="M318 392 L520 470" stroke="#7A6A52" stroke-width="4"/>
 <text x="530" y="470" font-family="Poppins" font-size="30" font-weight="700" fill="#2E3B2A">yan tomurcuklar</text>
 <text x="530" y="508" font-family="Poppins" font-size="28" fill="#7A6A52">→ 2 yeni dal olur</text>
 <text x="440" y="600" font-family="Poppins" font-size="30" font-weight="700" fill="#3C6E3A">en az 2 yaprak</text>
 <text x="440" y="638" font-family="Poppins" font-size="30" font-weight="700" fill="#3C6E3A">çifti bırak</text>
</svg></div>"""

c4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ADIM ADIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Böyle buda</h2>
<div class="card" style="padding:22px 32px"><div class="ic">1️⃣</div><p style="font-size:30px"><b>Başla:</b> bitkide 3–4 yaprak çifti olunca ilk tepe kesimini yap.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">2️⃣</div><p style="font-size:30px"><b>Kes:</b> temiz makasla, bir yaprak çiftinin hemen üstünden.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">3️⃣</div><p style="font-size:30px"><b>Tekrarla:</b> yeni dallar da 2–3 yaprak çifti yapınca aynı işlem.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">4️⃣</div><p style="font-size:30px"><b>Çiçeği kopar:</b> tepede tomurcuk görür görmez sıkıştırıp al.</p></div></div>"""

c5 = """<div class="pad" style="padding-top:150px">
<span class="tag">SIK YAPILAN HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunları yapma</h2>
<div class="card" style="padding:22px 32px"><div class="ic">❌</div><p style="font-size:30px"><b>Alttan yaprak toplamak:</b> bitki boylanır, altı çıplak kalır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">❌</div><p style="font-size:30px"><b>Çıplak saptan kesmek:</b> yaprak olmayan yerden yeni dal çıkmaz.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">❌</div><p style="font-size:30px"><b>Bir kerede çok kesmek:</b> bitkinin <span class="hl">üçte birinden</span> fazlasını alma.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">💡</div><p style="font-size:30px"><b>Bonus:</b> kestiğin dalı suya koy; birkaç haftada kök salar, yeni bitki olur.</p></div></div>"""

c6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px">Yaprak çiftinin <b>hemen üstünden</b> kes.</p></div>
<div class="card"><div class="ic">🌿</div><p style="font-size:33px">Her kesim = <span class="hl">iki yeni dal.</span></p></div>
<div class="card"><div class="ic">🌸</div><p style="font-size:33px">Çiçek tomurcuğunu <b>erken kopar.</b></p></div>
<div class="card"><div class="ic">⚖️</div><p style="font-size:33px">Tek seferde en fazla <b>üçte bir.</b></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Senin fesleğenin çalı mı, sırık mı?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: FOTOPERİYOT ----------
a1 = """<div class="pad" style="padding-top:150px">
<span class="tag">FOTOPERİYOT</span>
<h1 style="margin-top:50px">Işık günde<br>kaç saat<br>yanmalı?</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Bitkin saati sayar.<br>Asıl önemli olan <span class="hl">karanlık.</span></p>
<svg width="912" height="320" viewBox="0 0 912 320" style="position:absolute;bottom:125px;left:84px">
 <circle cx="456" cy="160" r="150" fill="#FFF9EE" stroke="#E3D3B8" stroke-width="8"/>
 <path d="M456 160 L456 10 A150 150 0 1 1 326 235 Z" fill="#F7D98B"/>
 <path d="M456 160 L326 235 A150 150 0 0 1 456 10 Z" fill="#2E3B2A"/>
 <circle cx="456" cy="160" r="14" fill="#B5543A"/>
 <path d="M456 160 L456 60" stroke="#B5543A" stroke-width="10" stroke-linecap="round"/>
 <path d="M456 160 L530 200" stroke="#B5543A" stroke-width="10" stroke-linecap="round"/>
 <text x="190" y="120" font-family="Poppins" font-size="80" text-anchor="middle">🌙</text>
 <text x="730" y="120" font-family="Poppins" font-size="80" text-anchor="middle">☀️</text>
</svg></div>"""

a2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDİR?</span>
<h2>Gündüz + gece<br>= fotoperiyot</h2>
<p><b>Fotoperiyot</b>, bitkinin 24 saat içinde aldığı ışık ve karanlık süresidir.</p>
<p style="margin-top:30px">Bitkiler yapraklarındaki ışık algılayıcılarla günün uzunluğunu "ölçer". Asıl hesaba kattıkları şey <span class="hl">kesintisiz gece</span> süresidir.</p>
<p style="margin-top:30px">Bu süre, bazı bitkilerde <b>ne zaman çiçek açacağına</b> karar verir.</p></div>"""

a3 = """<div class="pad" style="padding-top:150px">
<span class="tag">3 GRUP</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bitkin hangi takımda?</h2>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">☀️ Uzun gün bitkileri</p><p style="font-size:30px;margin-top:8px">Günler uzayınca çiçeğe kalkar. <b>Marul, ıspanak.</b> Uzun ışıkta "tohuma kaçabilir".</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">🌙 Kısa gün bitkileri</p><p style="font-size:30px;margin-top:8px">Geceler uzayınca çiçek açar. <b>Krizantem, Atatürk çiçeği,</b> klasik (bir kez ürün veren) çilek.</p></div>
<div class="card" style="display:block;padding:26px 34px"><p style="font-size:34px;font-weight:800;color:#2F5D2D">⚖️ Gün nötr bitkiler</p><p style="font-size:30px;margin-top:8px">Gün uzunluğuna pek bakmaz. <b>Domates, biber,</b> gün nötr çilek çeşitleri.</p></div></div>"""

a4 = """<div class="pad" style="padding-top:150px">
<span class="tag">PRATİKTE</span>
<h2 style="font-size:60px;margin:22px 0 26px">Kapalı ortamda<br>ışık süresi</h2>
<div class="card" style="padding:24px 32px"><div class="ic">🥬</div><p style="font-size:30px"><b>Yeşillik ve otlar:</b> günde 14–16 saat yaygın bir başlangıçtır.</p></div>
<div class="card" style="padding:24px 32px"><div class="ic">⏲️</div><p style="font-size:30px"><b>Zamanlayıcı kullan:</b> her gün aynı saatte aç, aynı saatte kapat.</p></div>
<div class="card" style="padding:24px 32px"><div class="ic">🚫</div><p style="font-size:30px"><b>24 saat açık bırakma:</b> domates gibi bitkilerde sürekli ışık yaprak sararmasına yol açabilir.</p></div>
<div class="card" style="padding:24px 32px"><div class="ic">🌙</div><p style="font-size:30px"><b>Karanlık gerçek olsun:</b> gece ışık sızmasın.</p></div></div>"""

a5 = """<div class="pad" style="padding-top:150px">
<span class="tag">YANLIŞ BİLİNEN</span>
<h2 style="font-size:60px;margin:22px 0 26px">"Daha çok saat =<br>daha çok ürün" mü?</h2>
<p style="font-size:34px">Hayır. Bitki için önemli olan günlük <b>toplam ışık miktarıdır</b>: ışığın <span class="hl">gücü × süresi.</span></p>
<p style="font-size:34px;margin-top:26px">Zayıf bir lambayı daha uzun yakmak, güçlü ışığın yerini tam tutmaz; sadece elektrik faturası artar.</p>
<div class="card" style="margin-top:30px;padding:26px 32px"><div class="ic">💡</div><p style="font-size:30px"><b>Kısa gün bitkisinde dikkat:</b> gece birkaç dakika lamba yakmak bile çiçeklenmeyi geciktirebilir.</p></div></div>"""

a6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🕒</div><p style="font-size:33px">Fotoperiyot = günlük <b>ışık + karanlık</b> düzeni.</p></div>
<div class="card"><div class="ic">🌙</div><p style="font-size:33px">Bitki asıl <span class="hl">gece süresini</span> ölçer.</p></div>
<div class="card"><div class="ic">🥬</div><p style="font-size:33px">Marul uzun ışıkta <b>tohuma kaçabilir.</b></p></div>
<div class="card"><div class="ic">⏲️</div><p style="font-size:33px">Zamanlayıcı kur, <b>24 saat yakma.</b></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Senin lamban kaç saat yanıyor?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:100px">Fesleğeni<br>tepeden<br>kesersen,<br>2 dal çıkar! 🌿</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Kestiğin yerin altındaki yaprak çiftinde uyuyan <b>iki yan tomurcuk</b> <span class="hl">uyanır.</span></p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">✂️</div><p style="font-size:40px"><b>Tam olarak nereden kesmeli?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([c1, c2, c3, c4, c5, c6], "gun8/feslegen")
    render_post([a1, a2, a3, a4, a5, a6], "gun8/fotoperiyot")
    render_story(story, "gun8/hikaye")
