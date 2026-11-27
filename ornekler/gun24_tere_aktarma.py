import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ TERE ----------
t1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ TERE</span>
<h1 style="margin-top:50px">Toprak yok,<br>bekleme yok:<br>en hızlı<br>yeşillik 🌱</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Tere birkaç günde çimlenir,<br><span class="hl">kısa sürede sofrada.</span></p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(560 30)">
  <rect x="0" y="140" width="330" height="50" rx="12" fill="#5B6B57"/>
  <rect x="14" y="128" width="302" height="22" rx="6" fill="#E8DCC4"/>
  <g stroke="#5E9B4F" stroke-width="4" stroke-linecap="round">
   <path d="M40 128 L40 60"/><path d="M80 128 L82 50"/><path d="M120 128 L118 58"/><path d="M160 128 L162 45"/><path d="M200 128 L198 55"/><path d="M240 128 L242 48"/><path d="M280 128 L278 60"/>
  </g>
  <g fill="#6FA84B">
   <ellipse cx="32" cy="58" rx="12" ry="7"/><ellipse cx="48" cy="58" rx="12" ry="7"/>
   <ellipse cx="74" cy="48" rx="12" ry="7"/><ellipse cx="90" cy="48" rx="12" ry="7"/>
   <ellipse cx="110" cy="56" rx="12" ry="7"/><ellipse cx="126" cy="56" rx="12" ry="7"/>
   <ellipse cx="154" cy="43" rx="12" ry="7"/><ellipse cx="170" cy="43" rx="12" ry="7"/>
   <ellipse cx="190" cy="53" rx="12" ry="7"/><ellipse cx="206" cy="53" rx="12" ry="7"/>
   <ellipse cx="234" cy="46" rx="12" ry="7"/><ellipse cx="250" cy="46" rx="12" ry="7"/>
   <ellipse cx="270" cy="58" rx="12" ry="7"/><ellipse cx="286" cy="58" rx="12" ry="7"/>
  </g>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="0" y="110">Tepside, ıslak keçede →</text><text x="0" y="150" fill="#7A6A52" font-size="26">pompa, toprak, gübre şart değil</text></g>
</svg></div>"""

t2 = """<div class="pad" style="padding-top:150px">
<span class="tag">TANIYALIM</span>
<h2>Küçük ama<br>keskin lezzet</h2>
<p>Tere (<i>Lepidium sativum</i>), roka ve lahana ile <b>aynı aileden</b> (turpgiller) gelir. Tadı acımsı, <b>hardalı andıran</b> bir keskinliktedir.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">⚡</div><p style="font-size:30px"><b>Çok hızlı çimlenir;</b> çoğu zaman 1-3 gün yeter.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🫧</div><p style="font-size:30px">Tohumu ıslanınca <b>jöle gibi bir tabaka</b> ile kaplanır ve yüzeye yapışır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">❄️</div><p style="font-size:30px"><b>Serin sever;</b> sıcakta çabuk <span class="hl">çiçeğe kalkar.</span></p></div></div>"""

t3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Tepside tere,<br>3 adımda</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="20" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="321" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="622" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <text x="155" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">1</text>
 <text x="456" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">2</text>
 <text x="757" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">3</text>
 <!-- 1 tepsi + ıslak keçe + tohum -->
 <rect x="50" y="330" width="210" height="50" rx="10" fill="#5B6B57"/>
 <rect x="62" y="318" width="186" height="20" rx="5" fill="#9FC3D4"/>
 <g fill="#7A5A32"><circle cx="85" cy="314" r="5"/><circle cx="110" cy="312" r="5"/><circle cx="135" cy="315" r="5"/><circle cx="160" cy="312" r="5"/><circle cx="185" cy="314" r="5"/><circle cx="210" cy="312" r="5"/><circle cx="232" cy="315" r="5"/></g>
 <!-- 2 karanlık / kapak + filiz -->
 <rect x="351" y="330" width="210" height="50" rx="10" fill="#5B6B57"/>
 <rect x="363" y="318" width="186" height="20" rx="5" fill="#9FC3D4"/>
 <g stroke="#E8DCC4" stroke-width="4" stroke-linecap="round"><path d="M390 318 Q392 295 400 290"/><path d="M430 318 Q432 292 440 288"/><path d="M470 318 Q472 295 480 290"/><path d="M510 318 Q512 292 520 288"/></g>
 <path d="M345 270 L567 270" stroke="#7A6A52" stroke-width="8" stroke-linecap="round" stroke-dasharray="2 14"/>
 <!-- 3 ışık + yeşil -->
 <rect x="652" y="330" width="210" height="50" rx="10" fill="#5B6B57"/>
 <rect x="664" y="318" width="186" height="20" rx="5" fill="#9FC3D4"/>
 <g stroke="#5E9B4F" stroke-width="4"><path d="M690 318 L690 240"/><path d="M730 318 L730 230"/><path d="M770 318 L770 236"/><path d="M810 318 L810 228"/></g>
 <g fill="#6FA84B"><ellipse cx="682" cy="238" rx="11" ry="6"/><ellipse cx="698" cy="238" rx="11" ry="6"/><ellipse cx="722" cy="228" rx="11" ry="6"/><ellipse cx="738" cy="228" rx="11" ry="6"/><ellipse cx="762" cy="234" rx="11" ry="6"/><ellipse cx="778" cy="234" rx="11" ry="6"/><ellipse cx="802" cy="226" rx="11" ry="6"/><ellipse cx="818" cy="226" rx="11" ry="6"/></g>
 <circle cx="757" cy="140" r="28" fill="#F7D98B"/>
 <g stroke="#E0B83A" stroke-width="5" stroke-linecap="round"><path d="M757 95 L757 82"/><path d="M712 140 L699 140"/><path d="M802 140 L815 140"/><path d="M725 108 L716 99"/><path d="M789 108 L798 99"/></g>
 </g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
 <text x="155" y="500" text-anchor="middle">Islak keçe ya da</text><text x="155" y="536" text-anchor="middle">pamuğa tohumu</text><text x="155" y="572" text-anchor="middle">tek kat serp</text>
 <text x="456" y="500" text-anchor="middle">Üstünü örtme;</text><text x="456" y="536" text-anchor="middle">yüzeyi kurutmadan</text><text x="456" y="572" text-anchor="middle">nemli tut</text>
 <text x="757" y="500" text-anchor="middle">Filizler çıkınca</text><text x="757" y="536" text-anchor="middle">aydınlık yere</text><text x="757" y="572" text-anchor="middle">ya da LED altına al</text>
 </g>
 <g font-family="Poppins" font-size="28" font-weight="600" fill="#2E3B2A">
 <text x="20" y="660">Tohumu suda bekletme: <tspan fill="#2F5D2D" font-weight="800">jöle tabakası</tspan> topaklanır.</text>
 <text x="20" y="700">Islak yüzeye serpmek yeterli.</text>
 </g>
</svg></div>"""

t4 = """<div class="pad" style="padding-top:150px">
<span class="tag">BAKIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Sağlıklı<br>tere için</h2>
<div class="card" style="padding:20px 32px"><div class="ic">💧</div><p style="font-size:29px"><b>Tepsiyi alttan sula</b> ya da hafif püskürt; tohumlar ve kökler kurumasın.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">☀️</div><p style="font-size:29px"><b>Işık az olursa</b> filizler uzar, incelir ve soluk kalır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🫙</div><p style="font-size:29px"><b>Daha iri yaprak</b> istersen kaya yünü küpte Kratky ya da NFT'de de yetişir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:29px"><b>Serin ortam</b> tadı ve yaprağı korur; sıcakta <span class="hl">çabuk çiçeğe kalkar.</span></p></div></div>"""

t5 = """<div class="pad" style="padding-top:150px">
<span class="tag">HASAT &amp; HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Kes,<br>yeniden ek</h2>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px"><b>Makasla tabana yakın kes;</b> filiz olarak çoğu zaman 1-2 haftada hazırdır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔁</div><p style="font-size:29px"><b>Kesilen filiz genelde yeniden büyümez;</b> kesintisiz tere için her hafta yeni tepsi ek.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🍄</div><p style="font-size:29px"><b>Çok sık ekim + durgun hava</b> küfe yol açar; tohumu üst üste yığma.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💦</div><p style="font-size:29px"><b>Tepsiyi su içinde bırakma:</b> nemli tut ama <span class="hl">göllendirme.</span></p></div></div>"""

t6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🫧</div><p style="font-size:33px">Tohumu <b>ıslak yüzeye</b> serp, bekletme.</p></div>
<div class="card"><div class="ic">💧</div><p style="font-size:33px"><b>Nemli tut,</b> kurumasın.</p></div>
<div class="card"><div class="ic">☀️</div><p style="font-size:33px">Filizlenince <b>bol ışık</b> ver.</p></div>
<div class="card"><div class="ic">🔁</div><p style="font-size:33px"><span class="hl">Her hafta</span> yeni tepsi ek.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Tereyi en çok nerede seversin: salatada mı, sandviçte mi?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: FİDEYİ SİSTEME AKTARMA ----------
a1 = """<div class="pad" style="padding-top:150px">
<span class="tag">FİDE AKTARMA</span>
<h1 style="margin-top:50px">Fideyi<br>sisteme ne<br>zaman ve<br>nasıl koymalı?</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Erken de geç de<br><span class="hl">fideyi zorlar.</span></p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(660 0)">
  <rect x="40" y="90" width="120" height="100" rx="10" fill="#C9B48E"/>
  <g stroke="#A8916A" stroke-width="3"><line x1="40" y1="125" x2="160" y2="125"/><line x1="40" y1="158" x2="160" y2="158"/></g>
  <path d="M100 90 L100 30" stroke="#3C6E3A" stroke-width="6"/>
  <ellipse cx="78" cy="38" rx="24" ry="12" fill="#6FA84B"/><ellipse cx="122" cy="38" rx="24" ry="12" fill="#6FA84B"/>
  <g stroke="#E8DCC4" stroke-width="5" stroke-linecap="round"><path d="M75 190 L70 225"/><path d="M100 190 L100 228"/><path d="M125 190 L130 225"/></g>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="0" y="110">Kökler küpten çıkınca →</text><text x="0" y="150" fill="#7A6A52" font-size="26">aktarma zamanı gelmiştir</text></g>
</svg></div>"""

a2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NE ZAMAN?</span>
<h2>Fide hazır mı,<br>nasıl anlarsın?</h2>
<p>Fideyi çimlendirdiğin küpten asıl sisteme taşımanın en iyi zamanı, fidenin <b>kendini taşıyabildiği</b> andır.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🌿</div><p style="font-size:30px"><b>Çenek yapraklardan sonra</b> 2-4 gerçek yaprak çıkmış olsun.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🧱</div><p style="font-size:30px"><b>Beyaz kökler</b> küpün altından ya da yanından görünsün.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">⏳</div><p style="font-size:30px"><b>Çok bekleme:</b> kökler birbirine dolanır, <span class="hl">ayırırken kopar.</span></p></div></div>"""

a3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Küpüyle birlikte<br>yerleştir</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="20" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="321" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="622" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <text x="155" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">1</text>
 <text x="456" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">2</text>
 <text x="757" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">3</text>
 <!-- 1 küp + kökler -->
 <rect x="100" y="230" width="110" height="100" rx="10" fill="#C9B48E"/>
 <g stroke="#A8916A" stroke-width="3"><line x1="100" y1="265" x2="210" y2="265"/><line x1="100" y1="298" x2="210" y2="298"/></g>
 <path d="M155 230 L155 160" stroke="#3C6E3A" stroke-width="5"/>
 <ellipse cx="135" cy="168" rx="22" ry="10" fill="#6FA84B"/><ellipse cx="175" cy="168" rx="22" ry="10" fill="#6FA84B"/>
 <g stroke="#E8DCC4" stroke-width="5" stroke-linecap="round"><path d="M130 330 L125 380"/><path d="M155 330 L155 390"/><path d="M180 330 L186 380"/></g>
 <!-- 2 file saksı + hidroton -->
 <path d="M386 220 L526 220 L506 380 L406 380 Z" fill="#5B6B57"/>
 <g stroke="#7E8F79" stroke-width="3"><line x1="392" y1="260" x2="520" y2="260"/><line x1="397" y1="300" x2="515" y2="300"/><line x1="402" y1="340" x2="510" y2="340"/><line x1="430" y1="220" x2="440" y2="380"/><line x1="482" y1="220" x2="472" y2="380"/></g>
 <rect x="416" y="250" width="80" height="72" rx="8" fill="#C9B48E"/>
 <g fill="#B5683E"><circle cx="402" cy="238" r="12"/><circle cx="426" cy="236" r="12"/><circle cx="486" cy="236" r="12"/><circle cx="510" cy="238" r="12"/><circle cx="408" cy="262" r="11"/><circle cx="504" cy="262" r="11"/></g>
 <path d="M456 250 L456 170" stroke="#3C6E3A" stroke-width="5"/>
 <ellipse cx="436" cy="178" rx="22" ry="10" fill="#6FA84B"/><ellipse cx="476" cy="178" rx="22" ry="10" fill="#6FA84B"/>
 <!-- 3 sistemde su seviyesi -->
 <rect x="660" y="260" width="194" height="140" rx="10" fill="#5B6B57"/>
 <rect x="672" y="300" width="170" height="90" rx="6" fill="#7FB0C9"/>
 <path d="M717 230 L797 230 L787 320 L727 320 Z" fill="#3F4B3C"/>
 <rect x="730" y="252" width="54" height="50" rx="6" fill="#C9B48E"/>
 <path d="M757 252 L757 160" stroke="#3C6E3A" stroke-width="5"/>
 <ellipse cx="737" cy="168" rx="22" ry="10" fill="#6FA84B"/><ellipse cx="777" cy="168" rx="22" ry="10" fill="#6FA84B"/>
 <g stroke="#E8DCC4" stroke-width="4"><path d="M745 320 L740 370"/><path d="M757 320 L757 378"/><path d="M769 320 L774 370"/></g>
 <path d="M650 300 L866 300" stroke="#2F5D2D" stroke-width="3" stroke-dasharray="8 6"/>
 </g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
 <text x="155" y="500" text-anchor="middle">Küpü sökme,</text><text x="155" y="536" text-anchor="middle">köke dokunmadan</text><text x="155" y="572" text-anchor="middle">bütün olarak al</text>
 <text x="456" y="500" text-anchor="middle">File saksıya koy,</text><text x="456" y="536" text-anchor="middle">çevresini</text><text x="456" y="572" text-anchor="middle">hidrotonla sabitle</text>
 <text x="757" y="500" text-anchor="middle">Başta su, saksı</text><text x="757" y="536" text-anchor="middle">tabanına değsin;</text><text x="757" y="572" text-anchor="middle">kök uzayınca indir</text>
 </g>
 <g font-family="Poppins" font-size="28" font-weight="600" fill="#2E3B2A">
 <text x="20" y="660">Kökler henüz kısa: <tspan fill="#2F5D2D" font-weight="800">suya ulaşamazsa</tspan> fide kurur.</text>
 <text x="20" y="700">DWC'de hava taşı ilk günden çalışsın.</text>
 </g>
</svg></div>"""

a4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ADIM ADIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Aktarma şokunu<br>azalt</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🧤</div><p style="font-size:29px"><b>Temiz elle ve hızlı çalış;</b> açıkta kalan kökler çabuk kurur ve hasar görür.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧪</div><p style="font-size:29px"><b>İlk günlerde çözeltiyi hafif tut;</b> genç kökler yüksek EC'ye hassastır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💡</div><p style="font-size:29px"><b>Işığa alıştır:</b> fidelikten güçlü LED'e ya da güneşe geçişi kademeli yap.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🥕</div><p style="font-size:29px"><b>Kazık köklüler</b> (kişniş, dereotu) taşınmayı sevmez; <span class="hl">tek seferde</span> yerine koy.</p></div></div>"""

a5 = """<div class="pad" style="padding-top:150px">
<span class="tag">SIK HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunları<br>yapma</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🐣</div><p style="font-size:29px"><b>Kökü çıkmamış fideyi aktarmak:</b> suya ulaşamaz, küp kurur, fide pörsür.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪢</div><p style="font-size:29px"><b>Kökleri küpten çekip ayıklamak:</b> ince kök tüyleri kopar, büyüme durur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌊</div><p style="font-size:29px"><b>Küpü ve gövdeyi suya gömmek:</b> gövde dibi havasız kalır, çürüme riski artar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">😟</div><p style="font-size:29px"><b>Birkaç günlük hafif pörsümeye panik:</b> çoğu zaman <span class="hl">fide toparlanır.</span></p></div></div>"""

a6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🧱</div><p style="font-size:33px"><b>Kök küpten çıkınca</b> aktar.</p></div>
<div class="card"><div class="ic">🤲</div><p style="font-size:33px"><b>Küpüyle birlikte,</b> köke dokunmadan.</p></div>
<div class="card"><div class="ic">💧</div><p style="font-size:33px">Başta suyu <b>saksı tabanına</b> değdir.</p></div>
<div class="card"><div class="ic">🧪</div><p style="font-size:33px"><span class="hl">Hafif çözelti,</span> kademeli ışık.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sen fideyi kaç yapraklıyken aktarıyorsun?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Tere tohumu<br>ıslanınca<br>jöleye<br>bürünür! 🫧</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Bu kaygan tabaka tohumu <b>ıslak yüzeye yapıştırır.</b> Yani suda bekletmene <span class="hl">gerek yok.</span></p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🌱</div><p style="font-size:40px"><b>Topraksız tere nasıl yetişir?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([t1, t2, t3, t4, t5, t6], "gun24/tere")
    render_post([a1, a2, a3, a4, a5, a6], "gun24/aktarma")
    render_story(story, "gun24/hikaye")
