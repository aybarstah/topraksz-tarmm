import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ MAYDANOZ ----------
m1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ MAYDANOZ</span>
<h1 style="margin-top:50px">Maydanoz<br>tohumu neden<br>bu kadar<br>sabır ister? 🌿</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Bekleme süresini<br><span class="hl">kısaltmanın yolu var.</span></p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(660 0)">
  <path d="M60 220 L60 70" stroke="#3C6E3A" stroke-width="7"/>
  <path d="M60 140 Q20 110 0 70" stroke="#3C6E3A" stroke-width="6" fill="none"/>
  <path d="M60 140 Q100 110 125 70" stroke="#3C6E3A" stroke-width="6" fill="none"/>
  <g fill="#5E9B4F"><circle cx="60" cy="55" r="30"/><circle cx="35" cy="40" r="20"/><circle cx="85" cy="40" r="20"/>
  <circle cx="0" cy="58" r="26"/><circle cx="-18" cy="42" r="16"/><circle cx="125" cy="58" r="26"/><circle cx="143" cy="42" r="16"/></g>
  <rect x="0" y="200" width="125" height="30" rx="8" fill="#5B6B57"/>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="120" y="110">Ekim → çimlenme</text><text x="120" y="150" fill="#7A6A52" font-size="26">çoğu zaman 2-4 hafta</text></g>
 <path d="M470 120 L600 120" stroke="#7A6A52" stroke-width="5"/><path d="M588 108 L605 120 L588 132" stroke="#7A6A52" stroke-width="5" fill="none"/>
</svg></div>"""

m2 = """<div class="pad" style="padding-top:150px">
<span class="tag">TANIYALIM</span>
<h2>Yavaş başlar,<br>uzun verir</h2>
<p>Maydanoz geç çimlenir ama bir kez tutunduğunda <b>aylarca</b> hasat verir.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🌱</div><p style="font-size:30px">Tohum kabuğunda <b>çimlenmeyi geciktiren maddeler</b> vardır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌿</div><p style="font-size:30px"><b>Düz yapraklı</b> ve <b>kıvırcık</b> çeşitleri var; ikisi de topraksızda olur.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">📅</div><p style="font-size:30px"><b>İki yıllık</b> bitkidir: ikinci yıl <span class="hl">çiçeğe kalkar</span>, yaprak tadı acılaşır.</p></div></div>"""

m3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Tohumdan<br>sisteme</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="20" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="321" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="622" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <text x="155" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">1</text>
 <text x="456" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">2</text>
 <text x="757" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">3</text>
 <rect x="80" y="230" width="150" height="160" rx="16" fill="#CFE3EE" stroke="#9BBFD0" stroke-width="5"/>
 <rect x="85" y="270" width="140" height="115" rx="12" fill="#9CC9DA"/>
 <g fill="#B59A6E"><ellipse cx="120" cy="330" rx="10" ry="6"/><ellipse cx="150" cy="350" rx="10" ry="6"/><ellipse cx="180" cy="320" rx="10" ry="6"/><ellipse cx="140" cy="300" rx="10" ry="6"/><ellipse cx="190" cy="360" rx="10" ry="6"/></g>
 <rect x="396" y="290" width="120" height="100" rx="10" fill="#C9B48E"/>
 <g stroke="#A8916A" stroke-width="3"><line x1="396" y1="320" x2="516" y2="320"/><line x1="396" y1="350" x2="516" y2="350"/></g>
 <path d="M456 290 L456 210" stroke="#5E9B4F" stroke-width="6"/>
 <g fill="#5E9B4F"><ellipse cx="436" cy="200" rx="22" ry="10" transform="rotate(-25 436 200)"/><ellipse cx="476" cy="200" rx="22" ry="10" transform="rotate(25 476 200)"/></g>
 <rect x="672" y="300" width="170" height="110" rx="12" fill="#5B6B57"/>
 <rect x="662" y="290" width="190" height="22" rx="8" fill="#3C6E3A"/>
 <path d="M757 290 L757 170" stroke="#3C6E3A" stroke-width="7"/>
 <path d="M757 240 Q720 210 705 175" stroke="#3C6E3A" stroke-width="5" fill="none"/>
 <path d="M757 240 Q794 210 809 175" stroke="#3C6E3A" stroke-width="5" fill="none"/>
 <g fill="#5E9B4F"><circle cx="757" cy="155" r="24"/><circle cx="705" cy="165" r="20"/><circle cx="809" cy="165" r="20"/></g>
 <g stroke="#E9DCC4" stroke-width="4" fill="none" stroke-linecap="round"><path d="M757 315 Q740 350 732 398"/><path d="M757 315 L757 402"/><path d="M757 315 Q774 350 784 398"/></g>
 </g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
 <text x="155" y="500" text-anchor="middle">Tohumu bir gece</text><text x="155" y="536" text-anchor="middle">ılık suda beklet,</text><text x="155" y="572" text-anchor="middle">suyu dök</text>
 <text x="456" y="500" text-anchor="middle">Kaya yünü küpe</text><text x="456" y="536" text-anchor="middle">birkaç tohum ek,</text><text x="456" y="572" text-anchor="middle">küpü hep nemli tut</text>
 <text x="757" y="500" text-anchor="middle">Kökler küpün</text><text x="757" y="536" text-anchor="middle">altından çıkınca</text><text x="757" y="572" text-anchor="middle">sisteme aktar</text>
 </g>
</svg></div>"""

m4 = """<div class="pad" style="padding-top:150px">
<span class="tag">BAKIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Gür maydanoz<br>için</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🫙</div><p style="font-size:29px"><b>Kratky, DWC ve NFT</b> uygundur; evde küçük bir kap bile yeter.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">⛅</div><p style="font-size:29px"><b>Yarı gölgeye dayanır</b>, ama bol ışıkta daha gür ve koyu yeşil olur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:29px"><b>Serin-ılık ortamı</b> sever; aşırı sıcak onu yorar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">✌️</div><p style="font-size:29px">Küpte çok fide çıktıysa <span class="hl">en güçlü 2-3 tanesini</span> bırak.</p></div></div>"""

m5 = """<div class="pad" style="padding-top:150px">
<span class="tag">HASAT &amp; HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Doğru<br>kesim</h2>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px"><b>Dıştaki saplardan</b>, dibe yakın kes. Ortadaki genç filiz büyümeye devam etsin.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🚫</div><p style="font-size:29px"><b>Tepeden kırpma:</b> fesleğen gibi dallanmaz; ortayı kesersen bitki zayıflar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔄</div><p style="font-size:29px"><b>Bir seferde çok kesme:</b> yaprakların çoğunu bitkide bırak.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">⏳</div><p style="font-size:29px"><b>Erken pes etme:</b> ilk haftalarda bir şey görünmemesi <span class="hl">normal.</span></p></div></div>"""

m6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">💧</div><p style="font-size:33px">Tohumu ekmeden <b>suda beklet.</b></p></div>
<div class="card"><div class="ic">⏳</div><p style="font-size:33px">Çimlenme <b>yavaş</b>, sabırlı ol.</p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px"><b>Dış saplardan</b> hasat et.</p></div>
<div class="card"><div class="ic">🌱</div><p style="font-size:33px">Ortadaki filize <span class="hl">dokunma.</span></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Maydanozun kaç günde çimlendi?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: EC/pH ÖLÇER KALİBRASYONU ----------
k1 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖLÇER KALİBRASYONU</span>
<h1 style="margin-top:50px">Ölçerin<br>yanlış<br>söylüyorsa? 📟</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Bütün ayarların<br><span class="hl">o sayıya bağlı.</span></p>
<svg width="912" height="250" viewBox="0 0 912 250" style="position:absolute;bottom:110px;left:84px">
 <g transform="translate(640 10)">
  <rect x="0" y="0" width="110" height="230" rx="22" fill="#2E3B2A"/>
  <rect x="15" y="25" width="80" height="50" rx="8" fill="#CFE3EE"/>
  <text x="55" y="62" font-family="Poppins" font-size="28" font-weight="800" fill="#2E3B2A" text-anchor="middle">?.?</text>
  <circle cx="35" cy="110" r="12" fill="#B59A6E"/><circle cx="75" cy="110" r="12" fill="#B59A6E"/>
  <rect x="35" y="150" width="40" height="80" rx="6" fill="#5B6B57"/>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="120" y="110">Yanlış ölçüm →</text><text x="120" y="150" fill="#7A6A52" font-size="26">yanlış gübre, yanlış pH</text></g>
</svg></div>"""

k2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN?</span>
<h2>Ölçerler<br>zamanla şaşar</h2>
<p>EC ve pH ölçerler kullanıldıkça <b>kayar</b>; bunu ekrana bakarak anlayamazsın.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🧪</div><p style="font-size:30px">pH probunun ucundaki <b>cam hazne</b> zamanla yaşlanır, tepkisi yavaşlar.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🧂</div><p style="font-size:30px">Uçta biriken <b>tuz ve kir</b> ölçümü bozar.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">📏</div><p style="font-size:30px"><b>Kalibrasyon</b>, ölçeri bilinen değerli bir sıvıyla <span class="hl">yeniden ayarlamaktır.</span></p></div></div>"""

k3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">pH ölçer<br>2 noktada ayarlanır</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="20" y="20" width="270" height="440" rx="26" fill="#FFF9EE"/>
 <rect x="321" y="20" width="270" height="440" rx="26" fill="#FFF9EE"/>
 <rect x="622" y="20" width="270" height="440" rx="26" fill="#FFF9EE"/>
 <text x="155" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">1</text>
 <text x="456" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">2</text>
 <text x="757" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">3</text>
 <rect x="85" y="250" width="140" height="170" rx="14" fill="#CFE3EE" stroke="#9BBFD0" stroke-width="5"/>
 <rect x="90" y="300" width="130" height="115" rx="10" fill="#E9F3F7"/>
 <rect x="135" y="120" width="40" height="230" rx="10" fill="#2E3B2A"/>
 <text x="155" y="390" font-size="26" text-anchor="middle" fill="#7A6A52">saf su</text>
 <rect x="386" y="250" width="140" height="170" rx="14" fill="#CFE3EE" stroke="#9BBFD0" stroke-width="5"/>
 <rect x="391" y="300" width="130" height="115" rx="10" fill="#9CCB6B"/>
 <rect x="436" y="120" width="40" height="230" rx="10" fill="#2E3B2A"/>
 <text x="456" y="390" font-size="34" text-anchor="middle" fill="#2F5D2D">pH 7</text>
 <rect x="687" y="250" width="140" height="170" rx="14" fill="#CFE3EE" stroke="#9BBFD0" stroke-width="5"/>
 <rect x="692" y="300" width="130" height="115" rx="10" fill="#F2B880"/>
 <rect x="737" y="120" width="40" height="230" rx="10" fill="#2E3B2A"/>
 <text x="757" y="390" font-size="34" text-anchor="middle" fill="#8B5A2B">pH 4</text>
 </g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
 <text x="155" y="530" text-anchor="middle">Probu saf suyla</text><text x="155" y="566" text-anchor="middle">durula</text>
 <text x="456" y="530" text-anchor="middle">Önce pH 7</text><text x="456" y="566" text-anchor="middle">tamponunda</text><text x="456" y="602" text-anchor="middle">ayarla</text>
 <text x="757" y="530" text-anchor="middle">Durula, sonra</text><text x="757" y="566" text-anchor="middle">pH 4 tamponunda</text><text x="757" y="602" text-anchor="middle">ayarla</text>
 </g>
 <text x="456" y="700" font-family="Poppins" font-size="27" font-weight="700" fill="#7A6A52" text-anchor="middle">Sıra ve tuşlar modele göre değişir; kılavuza bak.</text>
</svg></div>"""

k4 = """<div class="pad" style="padding-top:150px">
<span class="tag">EC ÖLÇER</span>
<h2 style="font-size:60px;margin:22px 0 26px">EC için<br>tek sıvı yeter</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🧴</div><p style="font-size:29px">Değeri <b>şişede yazan</b> bir EC kalibrasyon sıvısı kullan.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🎯</div><p style="font-size:29px">Sıvının değeri, <b>senin çalıştığın EC aralığına</b> yakın olsun.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:29px">EC <b>sıcaklıkla değişir</b>; ölçerinde sıcaklık dengeleme (ATC) olsun.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧽</div><p style="font-size:29px">Elektrotları <span class="hl">temiz tut</span>; tuz kabuğu ölçümü düşürür.</p></div></div>"""

k5 = """<div class="pad" style="padding-top:150px">
<span class="tag">SIK YAPILAN HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunları<br>yapma</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🚱</div><p style="font-size:29px"><b>pH probunu saf suda saklamak:</b> probu bozar. Saklama sıvısında (KCl) tut.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🏜️</div><p style="font-size:29px"><b>Probu kuru bırakmak:</b> kapağını hep sıvılı kapat.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">↩️</div><p style="font-size:29px"><b>Kullanılmış tamponu şişeye geri dökmek:</b> sıvıyı kirletir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📅</div><p style="font-size:29px"><b>Hiç kalibre etmemek:</b> düzenli ve şüphelendiğinde <span class="hl">mutlaka</span> ayarla.</p></div></div>"""

k6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">📟</div><p style="font-size:33px">Ölçer <b>zamanla şaşar.</b></p></div>
<div class="card"><div class="ic">🧪</div><p style="font-size:33px">pH: <b>7 ve 4</b> tamponuyla ayarla.</p></div>
<div class="card"><div class="ic">🧴</div><p style="font-size:33px">EC: <b>kalibrasyon sıvısı</b> ile.</p></div>
<div class="card"><div class="ic">🚱</div><p style="font-size:33px">pH probu <span class="hl">saf suda</span> saklanmaz.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Ölçerini en son ne zaman ayarladın?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Maydanoz<br>tohumu<br>haftalarca<br>çimlenmeyebilir! 🌿</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Çoğu zaman <span class="hl">2-4 hafta</span> sürer. Tohum kabuğu çimlenmeyi geciktirir.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">💧</div><p style="font-size:40px"><b>Nasıl hızlandırılır?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([m1, m2, m3, m4, m5, m6], "gun18/maydanoz")
    render_post([k1, k2, k3, k4, k5, k6], "gun18/kalibrasyon")
    render_story(story, "gun18/hikaye")
