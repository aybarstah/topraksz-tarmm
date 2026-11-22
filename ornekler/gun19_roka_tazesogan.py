import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ ROKA ----------
r1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ ROKA</span>
<h1 style="margin-top:50px">Sabırsızlar<br>için en iyi<br>yeşillik:<br>roka 🥬</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Hızlı çimlenir,<br><span class="hl">kestikçe yeniden verir.</span></p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(650 0)">
  <path d="M70 200 Q40 140 10 60" stroke="#3C6E3A" stroke-width="6" fill="none"/>
  <path d="M70 200 Q70 120 70 40" stroke="#3C6E3A" stroke-width="6" fill="none"/>
  <path d="M70 200 Q100 140 130 60" stroke="#3C6E3A" stroke-width="6" fill="none"/>
  <g fill="#5E9B4F"><ellipse cx="10" cy="60" rx="26" ry="16" transform="rotate(-40 10 60)"/><ellipse cx="30" cy="115" rx="20" ry="12" transform="rotate(-30 30 115)"/>
  <ellipse cx="70" cy="38" rx="18" ry="28"/><ellipse cx="70" cy="100" rx="14" ry="20"/>
  <ellipse cx="130" cy="60" rx="26" ry="16" transform="rotate(40 130 60)"/><ellipse cx="110" cy="115" rx="20" ry="12" transform="rotate(30 110 115)"/></g>
  <rect x="5" y="195" width="130" height="32" rx="8" fill="#5B6B57"/>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="120" y="110">Ekim → çimlenme</text><text x="120" y="150" fill="#7A6A52" font-size="26">genelde birkaç gün</text></g>
 <path d="M470 120 L600 120" stroke="#7A6A52" stroke-width="5"/><path d="M588 108 L605 120 L588 132" stroke="#7A6A52" stroke-width="5" fill="none"/>
</svg></div>"""

r2 = """<div class="pad" style="padding-top:150px">
<span class="tag">TANIYALIM</span>
<h2>Küçük ama<br>keskin</h2>
<p>Roka, lahana ve turpla <b>aynı aileden</b> (turpgiller) gelir; o acımsı tadı buradan.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">⚡</div><p style="font-size:30px"><b>Hızlı büyür:</b> taze yapraklar için uzun süre beklemen gerekmez.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">❄️</div><p style="font-size:30px"><b>Serin havayı sever;</b> kış aylarında içeride rahat yetişir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌼</div><p style="font-size:30px">Sıcakta ve uzun günde <span class="hl">çiçeğe kalkar</span>, yaprak sertleşir ve acılaşır.</p></div></div>"""

r3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Tohumdan<br>tabağa</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="20" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="321" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="622" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <text x="155" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">1</text>
 <text x="456" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">2</text>
 <text x="757" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">3</text>
 <rect x="95" y="290" width="120" height="100" rx="10" fill="#C9B48E"/>
 <g stroke="#A8916A" stroke-width="3"><line x1="95" y1="320" x2="215" y2="320"/><line x1="95" y1="350" x2="215" y2="350"/></g>
 <g fill="#8B5A2B"><circle cx="135" cy="285" r="7"/><circle cx="155" cy="280" r="7"/><circle cx="175" cy="286" r="7"/></g>
 <rect x="396" y="290" width="120" height="100" rx="10" fill="#C9B48E"/>
 <g stroke="#A8916A" stroke-width="3"><line x1="396" y1="320" x2="516" y2="320"/><line x1="396" y1="350" x2="516" y2="350"/></g>
 <path d="M440 290 L440 220" stroke="#5E9B4F" stroke-width="5"/><path d="M472 290 L472 210" stroke="#5E9B4F" stroke-width="5"/>
 <g fill="#5E9B4F"><ellipse cx="426" cy="212" rx="18" ry="9" transform="rotate(-25 426 212)"/><ellipse cx="454" cy="212" rx="18" ry="9" transform="rotate(25 454 212)"/>
 <ellipse cx="458" cy="202" rx="18" ry="9" transform="rotate(-25 458 202)"/><ellipse cx="486" cy="202" rx="18" ry="9" transform="rotate(25 486 202)"/></g>
 <rect x="672" y="300" width="170" height="110" rx="12" fill="#5B6B57"/>
 <rect x="662" y="290" width="190" height="22" rx="8" fill="#3C6E3A"/>
 <path d="M757 290 Q730 220 700 160" stroke="#3C6E3A" stroke-width="5" fill="none"/>
 <path d="M757 290 L757 140" stroke="#3C6E3A" stroke-width="5"/>
 <path d="M757 290 Q784 220 814 160" stroke="#3C6E3A" stroke-width="5" fill="none"/>
 <g fill="#5E9B4F"><ellipse cx="700" cy="160" rx="24" ry="14" transform="rotate(-45 700 160)"/><ellipse cx="757" cy="135" rx="16" ry="26"/><ellipse cx="814" cy="160" rx="24" ry="14" transform="rotate(45 814 160)"/>
 <ellipse cx="722" cy="215" rx="18" ry="10" transform="rotate(-35 722 215)"/><ellipse cx="792" cy="215" rx="18" ry="10" transform="rotate(35 792 215)"/></g>
 <g stroke="#E9DCC4" stroke-width="4" fill="none" stroke-linecap="round"><path d="M757 315 Q740 350 732 398"/><path d="M757 315 L757 402"/><path d="M757 315 Q774 350 784 398"/></g>
 </g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
 <text x="155" y="500" text-anchor="middle">Kaya yünü küpe</text><text x="155" y="536" text-anchor="middle">birkaç tohum</text><text x="155" y="572" text-anchor="middle">doğrudan ek</text>
 <text x="456" y="500" text-anchor="middle">Küpü nemli tut;</text><text x="456" y="536" text-anchor="middle">filizler genelde</text><text x="456" y="572" text-anchor="middle">birkaç günde çıkar</text>
 <text x="757" y="500" text-anchor="middle">Kökler küpün</text><text x="757" y="536" text-anchor="middle">altından çıkınca</text><text x="757" y="572" text-anchor="middle">sisteme aktar</text>
 </g>
</svg></div>"""

r4 = """<div class="pad" style="padding-top:150px">
<span class="tag">BAKIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Körpe roka<br>için</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🫙</div><p style="font-size:29px"><b>Kratky, DWC ve NFT</b> uygundur; kökü küçük olduğu için az yer ister.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">☀️</div><p style="font-size:29px"><b>Bol ışık</b> ister; az ışıkta uzar, yapraklar ince ve soluk kalır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:29px"><b>Serin ortamda</b> tadı daha yumuşak olur; sıcak acılığı artırır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📆</div><p style="font-size:29px">Hep taze yaprak için <span class="hl">birkaç haftada bir</span> yeni tohum ek.</p></div></div>"""

r5 = """<div class="pad" style="padding-top:150px">
<span class="tag">HASAT &amp; HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Doğru<br>kesim</h2>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px"><b>Dıştaki büyük yapraklardan</b> kes; ortadaki genç yapraklar büyüsün.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌼</div><p style="font-size:29px"><b>Çiçek sapı çıktıysa</b> yapraklar acılaşır; o bitkiyi yenisiyle değiştir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌱</div><p style="font-size:29px"><b>Küpe çok tohum atmak:</b> sıkışan fideler zayıf kalır, havasız ortam küf yapar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌸</div><p style="font-size:29px">Kalkmış rokanın <span class="hl">çiçekleri de yenir</span>; salatada hafif acı tat verir.</p></div></div>"""

r6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">⚡</div><p style="font-size:33px">Roka <b>hızlı çimlenir.</b></p></div>
<div class="card"><div class="ic">❄️</div><p style="font-size:33px"><b>Serin + aydınlık</b> ortam sever.</p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px"><b>Dış yapraklardan</b> hasat et.</p></div>
<div class="card"><div class="ic">📆</div><p style="font-size:33px">Kademeli ek, <span class="hl">hep taze</span> olsun.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Rokayı acı mı seversin, yumuşak mı?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: TAZE SOĞANI SUDA YENİDEN BÜYÜTME ----------
s1 = """<div class="pad" style="padding-top:150px">
<span class="tag">MUTFAKTAN SERAYA</span>
<h1 style="margin-top:50px">Taze soğanın<br>dibini<br>atma! 🧅</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Bir bardak suda<br><span class="hl">yeniden yeşerir.</span></p>
<svg width="912" height="250" viewBox="0 0 912 250" style="position:absolute;bottom:110px;left:84px">
 <g transform="translate(640 0)">
  <path d="M55 150 L40 10" stroke="#5E9B4F" stroke-width="10" stroke-linecap="round"/>
  <path d="M65 150 L65 0" stroke="#5E9B4F" stroke-width="10" stroke-linecap="round"/>
  <path d="M75 150 L92 15" stroke="#5E9B4F" stroke-width="10" stroke-linecap="round"/>
  <rect x="10" y="110" width="110" height="135" rx="14" fill="#CFE3EE" stroke="#9BBFD0" stroke-width="5" opacity="0.9"/>
  <rect x="15" y="170" width="100" height="70" rx="10" fill="#9CC9DA"/>
  <ellipse cx="65" cy="190" rx="20" ry="26" fill="#F7F1E3"/>
  <g stroke="#E9DCC4" stroke-width="3" fill="none"><path d="M60 214 L50 236"/><path d="M65 216 L65 238"/><path d="M70 214 L80 236"/></g>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="120" y="110">Kökler suda →</text><text x="120" y="150" fill="#7A6A52" font-size="26">yeşil kısım yeniden uzar</text></g>
</svg></div>"""

s2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NASIL OLUYOR?</span>
<h2>Kök canlıysa<br>bitki yaşar</h2>
<p>Taze soğanın beyaz dibinde <b>büyüme noktası ve kökler</b> durur. Yeşil kısmı kesmek bitkiyi öldürmez.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🔋</div><p style="font-size:30px">İlk sürgünler için gereken enerji <b>beyaz kısımda depolanmıştır.</b></p></div>
<div class="card" style="padding:22px 32px"><div class="ic">💧</div><p style="font-size:30px">Su, kökleri canlı tutar; <b>ışık</b> yeni yaprağı yeşillendirir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">♻️</div><p style="font-size:30px">Mutfak atığı, <span class="hl">ücretsiz yeşilliğe</span> dönüşür.</p></div></div>"""

s3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">3 adımda<br>yeniden büyüt</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="20" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="321" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="622" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <text x="155" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">1</text>
 <text x="456" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">2</text>
 <text x="757" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">3</text>
 <rect x="145" y="240" width="20" height="110" rx="8" fill="#F7F1E3" stroke="#D8CBB0" stroke-width="3"/>
 <path d="M155 240 L155 130" stroke="#5E9B4F" stroke-width="16" stroke-linecap="round" opacity="0.35"/>
 <path d="M110 235 L200 235" stroke="#C0392B" stroke-width="5" stroke-dasharray="10 8"/>
 <g stroke="#C9B48E" stroke-width="3" fill="none"><path d="M150 350 L138 390"/><path d="M155 352 L155 395"/><path d="M160 350 L172 390"/></g>
 <rect x="391" y="210" width="130" height="200" rx="16" fill="#CFE3EE" stroke="#9BBFD0" stroke-width="5"/>
 <rect x="396" y="320" width="120" height="85" rx="12" fill="#9CC9DA"/>
 <rect x="446" y="250" width="20" height="100" rx="8" fill="#F7F1E3" stroke="#D8CBB0" stroke-width="3"/>
 <g stroke="#E9DCC4" stroke-width="3" fill="none"><path d="M451 350 L440 392"/><path d="M456 352 L456 398"/><path d="M461 350 L472 392"/></g>
 <rect x="707" y="210" width="100" height="200" rx="16" fill="#CFE3EE" stroke="#9BBFD0" stroke-width="5"/>
 <rect x="712" y="320" width="90" height="85" rx="12" fill="#9CC9DA"/>
 <rect x="747" y="250" width="20" height="100" rx="8" fill="#F7F1E3" stroke="#D8CBB0" stroke-width="3"/>
 <path d="M752 250 L735 120" stroke="#5E9B4F" stroke-width="9" stroke-linecap="round"/>
 <path d="M757 250 L757 105" stroke="#5E9B4F" stroke-width="9" stroke-linecap="round"/>
 <path d="M762 250 L780 125" stroke="#5E9B4F" stroke-width="9" stroke-linecap="round"/>
 <g stroke="#E9DCC4" stroke-width="3" fill="none"><path d="M752 350 L740 395"/><path d="M757 352 L757 400"/><path d="M762 350 L774 395"/></g>
 </g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
 <text x="155" y="500" text-anchor="middle">Köklü beyaz</text><text x="155" y="536" text-anchor="middle">kısmı birkaç</text><text x="155" y="572" text-anchor="middle">santim bırakarak</text><text x="155" y="608" text-anchor="middle">kes</text>
 <text x="456" y="500" text-anchor="middle">Kökler suda,</text><text x="456" y="536" text-anchor="middle">üst kısım</text><text x="456" y="572" text-anchor="middle">dışarıda kalsın</text>
 <text x="757" y="500" text-anchor="middle">Aydınlık yere</text><text x="757" y="536" text-anchor="middle">koy; suyu sık</text><text x="757" y="572" text-anchor="middle">tazele</text>
 </g>
</svg></div>"""

s4 = """<div class="pad" style="padding-top:150px">
<span class="tag">İPUÇLARI</span>
<h2 style="font-size:60px;margin:22px 0 26px">Daha uzun<br>sürsün</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🔄</div><p style="font-size:29px"><b>Suyu 1-2 günde bir değiştir;</b> bekleyen su bulanıklaşır ve kokar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪟</div><p style="font-size:29px"><b>Aydınlık pencere önü</b> ya da LED altı; karanlıkta sürgün soluk ve cılız olur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌊</div><p style="font-size:29px">Beyaz kısmı <b>tamamen batırma</b>; yalnızca kökler ve dibi suda kalsın.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧪</div><p style="font-size:29px">Uzun süre hasat için <span class="hl">besin çözeltili</span> bir sisteme aktar.</p></div></div>"""

s5 = """<div class="pad" style="padding-top:150px">
<span class="tag">SINIRLAR &amp; HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bilmen<br>gerekenler</h2>
<div class="card" style="padding:20px 32px"><div class="ic">📉</div><p style="font-size:29px"><b>Sade suda sonsuza kadar sürmez:</b> birkaç hasattan sonra sürgünler incelir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🫠</div><p style="font-size:29px"><b>Kayganlaşan, kötü kokan dip</b> çürümüştür; at ve yenisiyle başla.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px"><b>Kökü kesik soğan</b> zor tutar; dipteki kökleri mutlaka bırak.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🥬</div><p style="font-size:29px">Aynı yöntemi <span class="hl">pırasa ve kereviz</span> diplerinde de deneyebilirsin.</p></div></div>"""

s6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🧅</div><p style="font-size:33px">Köklü dibi <b>atma.</b></p></div>
<div class="card"><div class="ic">💧</div><p style="font-size:33px">Kökler <b>suda</b>, üstü dışarıda.</p></div>
<div class="card"><div class="ic">🔄</div><p style="font-size:33px">Suyu <b>sık tazele.</b></p></div>
<div class="card"><div class="ic">🧪</div><p style="font-size:33px">Uzun süre için <span class="hl">besin çözeltisi.</span></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Mutfakta başka neyi yeniden büyüttün?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Roka<br>maydanozun<br>tam tersi:<br>çok hızlı! 🥬</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Tohumu genelde <span class="hl">birkaç günde</span> çimlenir, kestikçe yeniden yaprak verir.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">✂️</div><p style="font-size:40px"><b>Nasıl yetiştirilir?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([r1, r2, r3, r4, r5, r6], "gun19/roka")
    render_post([s1, s2, s3, s4, s5, s6], "gun19/tazesogan")
    render_story(story, "gun19/hikaye")
