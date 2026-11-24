import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ KARALAHANA ----------
k1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ KARALAHANA</span>
<h1 style="margin-top:50px">Bir kez ek,<br>aylarca<br>yaprak<br>topla! 🥬</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Sırrı <span class="hl">alttan yukarı</span><br>hasatta.</p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(640 0)">
  <path d="M90 205 L90 60" stroke="#3C6E3A" stroke-width="8"/>
  <g fill="#3F7A3A"><ellipse cx="90" cy="40" rx="34" ry="40"/>
  <ellipse cx="45" cy="95" rx="48" ry="24" transform="rotate(-25 45 95)"/><ellipse cx="135" cy="95" rx="48" ry="24" transform="rotate(25 135 95)"/>
  <ellipse cx="38" cy="150" rx="52" ry="24" transform="rotate(-15 38 150)" fill="#5E9B4F"/><ellipse cx="142" cy="150" rx="52" ry="24" transform="rotate(15 142 150)" fill="#5E9B4F"/></g>
  <rect x="25" y="195" width="130" height="32" rx="8" fill="#5B6B57"/>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="80" y="110">Alt yaprakları kes →</text><text x="80" y="150" fill="#7A6A52" font-size="26">tepe büyümeye devam eder</text></g>
</svg></div>"""

k2 = """<div class="pad" style="padding-top:150px">
<span class="tag">TANIYALIM</span>
<h2>Baş bağlamayan<br>lahana</h2>
<p>Karalahana, lahanayla <b>aynı türdendir</b> ama baş bağlamaz; yaprakları tek bir gövde üzerinde dizilir.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">❄️</div><p style="font-size:30px"><b>Serine dayanıklıdır;</b> soğukta yapraklar daha tatlı olabilir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🔥</div><p style="font-size:30px"><b>Sıcakta yapraklar</b> sertleşir ve acılaşabilir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌼</div><p style="font-size:30px"><span class="hl">İki yıllık</span> bitkidir; çiçeğe genelde ikinci yılında kalkar.</p></div></div>"""

k3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Nereden<br>keselim?</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="0" y="0" width="912" height="560" rx="26" fill="#FFF9EE"/>
 <g transform="translate(-100 0)">
 <path d="M300 520 L300 120" stroke="#3C6E3A" stroke-width="12"/>
 <ellipse cx="300" cy="95" rx="50" ry="60" fill="#3F7A3A"/>
 <g fill="#4F8A45"><ellipse cx="225" cy="200" rx="80" ry="30" transform="rotate(-25 225 200)"/><ellipse cx="375" cy="200" rx="80" ry="30" transform="rotate(25 375 200)"/></g>
 <g fill="#5E9B4F"><ellipse cx="215" cy="300" rx="90" ry="32" transform="rotate(-15 215 300)"/><ellipse cx="385" cy="300" rx="90" ry="32" transform="rotate(15 385 300)"/></g>
 <g fill="#8DB86F"><ellipse cx="205" cy="405" rx="95" ry="32" transform="rotate(-8 205 405)"/><ellipse cx="395" cy="405" rx="95" ry="32" transform="rotate(8 395 405)"/></g>
 <rect x="230" y="505" width="140" height="40" rx="10" fill="#5B6B57"/>
 </g>
 <path d="M410 95 L470 95" stroke="#3C6E3A" stroke-width="5"/>
 <text x="485" y="88" font-size="30" fill="#2F5D2D">Tepe: dokunma</text>
 <text x="485" y="122" font-size="22" fill="#7A6A52" font-weight="600">yeni yapraklar buradan çıkar</text>
 <path d="M420 405 L470 405" stroke="#C9A646" stroke-width="5"/>
 <text x="485" y="398" font-size="30" fill="#2F5D2D">Alt yapraklar: kes ✂️</text>
 <text x="485" y="432" font-size="22" fill="#7A6A52" font-weight="600">sapın dibinden, gövdeye yakın</text>
 </g>
 <g font-family="Poppins" font-size="28" font-weight="600" fill="#2E3B2A">
 <text x="0" y="620">Her hasatta <tspan fill="#2F5D2D" font-weight="800">en alttaki olgun yaprakları</tspan></text>
 <text x="0" y="660">al, tepede birkaç yaprak bırak. Bitki</text>
 <text x="0" y="700">boyuna uzar ve <tspan fill="#2F5D2D" font-weight="800">yaprak vermeye devam eder.</tspan></text>
 </g>
</svg></div>"""

k4 = """<div class="pad" style="padding-top:150px">
<span class="tag">YETİŞTİRME</span>
<h2 style="font-size:60px;margin:22px 0 26px">Hangi<br>sistem?</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🪣</div><p style="font-size:29px"><b>DWC kova</b> ya da <b>damla + cocopeat</b>: büyük, uzun ömürlü bitki için.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌱</div><p style="font-size:29px"><b>NFT veya Kratky:</b> genç yaprak (baby) hasadı için uygun.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">☀️</div><p style="font-size:29px"><b>Bol ışık</b> ister; az ışıkta gövde uzar, yapraklar incelir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📏</div><p style="font-size:29px">Bitki uzayıp ağırlaşır; gerekirse gövdeye <span class="hl">destek</span> ver.</p></div></div>"""

k5 = """<div class="pad" style="padding-top:150px">
<span class="tag">ZARARLILAR &amp; HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Yaprakları<br>kontrol et</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🐛</div><p style="font-size:29px"><b>Lahana kelebeği tırtılı:</b> yaprak altındaki yumurtaları erken topla, böcek tülü kullan.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🐜</div><p style="font-size:29px"><b>Yaprak biti</b> kıvrımlara saklanır; yaprak altına da bak.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🚫</div><p style="font-size:29px"><b>Tepeyi kesmek:</b> büyüme noktası gider, yeni yaprak gelmez.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🍂</div><p style="font-size:29px">Sararan en alt yaprakları <span class="hl">temizle</span>; hastalık ve zararlı barınağı olur.</p></div></div>"""

k6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">❄️</div><p style="font-size:33px"><b>Serin</b> ve aydınlık sever.</p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px"><b>Alttan yukarı</b> hasat et.</p></div>
<div class="card"><div class="ic">🚫</div><p style="font-size:33px">Tepeye <b>dokunma.</b></p></div>
<div class="card"><div class="ic">🐛</div><p style="font-size:33px">Yaprak altını <span class="hl">sık kontrol et.</span></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Karalahanayı nasıl yersin: sarma mı, çorba mı?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: ELEKTRİK KESİLİNCE ----------
e1 = """<div class="pad" style="padding-top:150px">
<span class="tag">ACİL DURUM</span>
<h1 style="margin-top:50px">Elektrik<br>kesildi,<br>bitkiler<br>ne olacak? ⚡</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Sistemine göre<br><span class="hl">ne kadar risktesin?</span></p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(680 10)">
  <path d="M90 0 L30 120 L80 120 L50 220 L150 80 L95 80 L130 0 Z" fill="#F7D98B" stroke="#C9A646" stroke-width="6"/>
  <line x1="0" y1="210" x2="200" y2="10" stroke="#B5473A" stroke-width="12" stroke-linecap="round"/>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="0" y="110">Pompa durur →</text><text x="0" y="150" fill="#7A6A52" font-size="26">su ve oksijen kesilir</text></g>
</svg></div>"""

e2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN ÖNEMLİ?</span>
<h2>Her sistem<br>aynı değil</h2>
<p>Çoğu topraksız sistem <b>pompa ile çalışır.</b> Elektrik gidince ya su akışı ya da hava kesilir.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">💧</div><p style="font-size:30px"><b>Su akışı kesilirse</b> kökler kurumaya başlar.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🫧</div><p style="font-size:30px"><b>Hava kesilirse</b> sudaki oksijen azalır, kök boğulur.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌡️</div><p style="font-size:30px"><b>Sıcak havada</b> iki risk de <span class="hl">çok daha hızlı</span> büyür.</p></div></div>"""

e3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Hangisi<br>daha riskli?</h2>
<div class="card" style="padding:22px 32px;border-left:14px solid #B5473A"><div class="ic">🔴</div><p style="font-size:30px"><b>NFT &amp; aeroponik:</b> kökler ince su filminde ya da havada; <b>en hızlı</b> etkilenenler.</p></div>
<div class="card" style="padding:22px 32px;border-left:14px solid #E0A43A"><div class="ic">🟠</div><p style="font-size:30px"><b>DWC:</b> kök suda kalır ama hava taşı durur; oksijen giderek azalır.</p></div>
<div class="card" style="padding:22px 32px;border-left:14px solid #E0A43A"><div class="ic">🟠</div><p style="font-size:30px"><b>Damla + ortam:</b> cocopeat, kaya yünü nemi bir süre tutar; tampon görevi görür.</p></div>
<div class="card" style="padding:22px 32px;border-left:14px solid #3C6E3A"><div class="ic">🟢</div><p style="font-size:30px"><b>Kratky &amp; fitil:</b> pompasız çalışır; elektrik kesintisinden <span class="hl">etkilenmez.</span></p></div></div>"""

e4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖNLEM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Önceden<br>hazırlan</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🔋</div><p style="font-size:29px"><b>Pilli / şarjlı hava pompası</b> DWC için ucuz bir yedektir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔌</div><p style="font-size:29px"><b>Kesintisiz güç kaynağı (UPS)</b> küçük pompaları bir süre çalıştırabilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📱</div><p style="font-size:29px"><b>Akıllı priz ya da alarm,</b> evde yokken elektriğin gittiğini haber verir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪣</div><p style="font-size:29px">NFT'de bitkileri hızla taşımak için <span class="hl">yedek bir kap</span> hazır tut.</p></div></div>"""

e5 = """<div class="pad" style="padding-top:150px">
<span class="tag">ELEKTRİK GELİNCE</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunları<br>kontrol et</h2>
<div class="card" style="padding:20px 32px"><div class="ic">⏲️</div><p style="font-size:29px"><b>Mekanik zamanlayıcı</b> kesinti süresi kadar geri kalır; saati yeniden ayarla.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💦</div><p style="font-size:29px"><b>Pompa gerçekten çalışıyor mu?</b> Oluklara ve damlatıcılara su geldiğini gör.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🥀</div><p style="font-size:29px"><b>Pörsüyen bitki</b> su gelince çoğu zaman toparlanır; kökü kahverengileşen bitkiyi izle.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔁</div><p style="font-size:29px">Pompa suyu geri çektiyse <span class="hl">çek valf</span> taktığından emin ol.</p></div></div>"""

e6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🔴</div><p style="font-size:33px"><b>NFT</b> en hassas sistemdir.</p></div>
<div class="card"><div class="ic">🔋</div><p style="font-size:33px">DWC'ye <b>pilli pompa</b> ayır.</p></div>
<div class="card"><div class="ic">⏲️</div><p style="font-size:33px">Sonra <b>zamanlayıcıyı</b> ayarla.</p></div>
<div class="card"><div class="ic">🟢</div><p style="font-size:33px">Kratky <span class="hl">elektriksiz</span> güvendedir.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Senin sistemin kesintide ne yaşadı?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Karalahana<br>tepesinden<br>değil,<br>altından<br>hasat edilir! 🥬</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Alttaki yaprakları kes, <span class="hl">tepeye dokunma</span>; bitki uzar ve yaprak vermeye devam eder.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🌱</div><p style="font-size:40px"><b>Topraksız nasıl yetişir?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([k1, k2, k3, k4, k5, k6], "gun21/karalahana")
    render_post([e1, e2, e3, e4, e5, e6], "gun21/elektrik")
    render_story(story, "gun21/hikaye")
