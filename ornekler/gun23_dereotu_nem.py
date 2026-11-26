import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ DEREOTU ----------
d1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ DEREOTU</span>
<h1 style="margin-top:50px">Dereotu<br>neden hemen<br>boy atıp<br>bitiyor? 🌿</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Doğru çeşit, doğru ekim,<br><span class="hl">sık hasat.</span></p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(650 0)">
  <path d="M70 200 L70 20" stroke="#3C6E3A" stroke-width="5"/>
  <g stroke="#5E9B4F" stroke-width="3" fill="none" stroke-linecap="round">
   <path d="M70 150 Q40 130 15 135"/><path d="M50 140 L40 120"/><path d="M35 137 L25 118"/>
   <path d="M70 150 Q100 130 125 135"/><path d="M90 140 L100 120"/><path d="M105 137 L115 118"/>
   <path d="M70 100 Q45 80 22 82"/><path d="M52 90 L44 70"/><path d="M38 85 L30 66"/>
   <path d="M70 100 Q95 80 118 82"/><path d="M88 90 L96 70"/><path d="M102 85 L110 66"/>
  </g>
  <g stroke="#C9A646" stroke-width="3"><path d="M70 22 L35 0"/><path d="M70 22 L55 -5"/><path d="M70 22 L85 -5"/><path d="M70 22 L105 0"/></g>
  <g fill="#E0B83A"><circle cx="35" cy="0" r="7"/><circle cx="55" cy="-5" r="7"/><circle cx="85" cy="-5" r="7"/><circle cx="105" cy="0" r="7"/></g>
  <rect x="5" y="195" width="130" height="32" rx="8" fill="#5B6B57"/>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="120" y="110">Sıcak + uzun gün →</text><text x="120" y="150" fill="#7A6A52" font-size="26">sarı şemsiye çiçek, az yaprak</text></g>
 <path d="M470 120 L600 120" stroke="#7A6A52" stroke-width="5"/><path d="M588 108 L605 120 L588 132" stroke="#7A6A52" stroke-width="5" fill="none"/>
</svg></div>"""

d2 = """<div class="pad" style="padding-top:150px">
<span class="tag">TANIYALIM</span>
<h2>İnce yapraklı<br>tek yıllık</h2>
<p>Dereotu, maydanoz ve kişnişle <b>aynı aileden</b> (maydanozgiller) gelir. Yaprağı da tohumu da mutfakta kullanılır.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">📅</div><p style="font-size:30px"><b>Tek yıllıktır;</b> bir sezonda büyür, çiçek açar, tohum bağlar.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🥕</div><p style="font-size:30px"><b>Kazık kökü</b> vardır; sonradan yer değiştirmekten hoşlanmaz.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">☀️</div><p style="font-size:30px"><b>Bol ışık</b> ister; ama sıcak ve uzun günde <span class="hl">çiçeğe kalkar.</span></p></div></div>"""

d3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Yerinde ek,<br>yerinde büyüt</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="20" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="321" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="622" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <text x="155" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">1</text>
 <text x="456" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">2</text>
 <text x="757" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">3</text>
 <!-- 1: küp + tohum -->
 <rect x="85" y="260" width="140" height="130" rx="12" fill="#C9B48E"/>
 <g stroke="#A8916A" stroke-width="3"><line x1="85" y1="300" x2="225" y2="300"/><line x1="85" y1="340" x2="225" y2="340"/></g>
 <g fill="#7A5A32"><ellipse cx="135" cy="252" rx="10" ry="6"/><ellipse cx="160" cy="248" rx="10" ry="6"/><ellipse cx="182" cy="254" rx="10" ry="6"/></g>
 <!-- 2: fide + kazık kök -->
 <rect x="386" y="260" width="140" height="130" rx="12" fill="#C9B48E"/>
 <g stroke="#A8916A" stroke-width="3"><line x1="386" y1="300" x2="526" y2="300"/><line x1="386" y1="340" x2="526" y2="340"/></g>
 <path d="M456 260 L456 170" stroke="#5E9B4F" stroke-width="5"/>
 <g stroke="#5E9B4F" stroke-width="3" fill="none"><path d="M456 200 Q430 185 415 190"/><path d="M456 200 Q482 185 497 190"/><path d="M456 175 Q440 160 428 162"/><path d="M456 175 Q472 160 484 162"/></g>
 <path d="M456 390 L456 425" stroke="#E8DCC4" stroke-width="7" stroke-linecap="round"/>
 <!-- 3: sistemde -->
 <rect x="672" y="320" width="170" height="90" rx="10" fill="#5B6B57"/>
 <rect x="684" y="350" width="146" height="50" rx="6" fill="#7FB0C9"/>
 <rect x="727" y="290" width="60" height="50" rx="6" fill="#C9B48E"/>
 <path d="M757 290 L757 150" stroke="#3C6E3A" stroke-width="6"/>
 <g stroke="#5E9B4F" stroke-width="3" fill="none"><path d="M757 250 Q720 230 700 236"/><path d="M757 250 Q794 230 814 236"/><path d="M757 205 Q725 185 708 188"/><path d="M757 205 Q789 185 806 188"/><path d="M757 165 Q735 150 722 152"/><path d="M757 165 Q779 150 792 152"/></g>
 <g stroke="#E8DCC4" stroke-width="4"><path d="M745 340 L740 395"/><path d="M757 340 L757 398"/><path d="M769 340 L774 395"/></g>
 </g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
 <text x="155" y="500" text-anchor="middle">Küpe 2-3 tohum</text><text x="155" y="536" text-anchor="middle">at, üstünü çok</text><text x="155" y="572" text-anchor="middle">kalın örtme</text>
 <text x="456" y="500" text-anchor="middle">Kazık kök aşağı</text><text x="456" y="536" text-anchor="middle">iner; fideyi</text><text x="456" y="572" text-anchor="middle">küpünden sökme</text>
 <text x="757" y="500" text-anchor="middle">Küpüyle birlikte</text><text x="757" y="536" text-anchor="middle">son yerine</text><text x="757" y="572" text-anchor="middle">bir kez koy</text>
 </g>
 <g font-family="Poppins" font-size="28" font-weight="600" fill="#2E3B2A">
 <text x="20" y="660">Çimlenme <tspan fill="#2F5D2D" font-weight="800">çoğu zaman 1-3 hafta</tspan> sürer;</text>
 <text x="20" y="700">küpü bu sürede nemli tut, sabırlı ol.</text>
 </g>
</svg></div>"""

d4 = """<div class="pad" style="padding-top:150px">
<span class="tag">BAKIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Yaprakta<br>tutmak için</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🏷️</div><p style="font-size:29px"><b>Bodur çeşit seç:</b> 'Fernleaf' gibi kısa boylu, geç çiçeklenen çeşitler iç mekâna daha uygundur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🫙</div><p style="font-size:29px"><b>Kratky, DWC, NFT</b> ya da <b>damla + cocopeat</b> ile yetişir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:29px"><b>Ilıman, serince ortam</b> yaprak dönemini uzatır; sıcak, çiçeğe kalkmayı hızlandırır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪵</div><p style="font-size:29px"><b>Uzun çeşitler</b> devrilebilir; <span class="hl">çubuk ya da ip</span> ile destekle.</p></div></div>"""

d5 = """<div class="pad" style="padding-top:150px">
<span class="tag">HASAT &amp; SORUNLAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Sık kes,<br>az kes</h2>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px"><b>Dış yaprakları</b> gövdeye yakın kes; bir seferde bitkinin <b>üçte birinden</b> fazlasını alma.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌼</div><p style="font-size:29px"><b>Çiçek sapı çıktıysa</b> yaprak üretimi azalır; yaprak istiyorsan sapı erken kopar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🐛</div><p style="font-size:29px"><b>Yaprak biti</b> ve <b>kırlangıçkuyruk kelebeği tırtılı</b> dereotunu sever; yaprak altına bak.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📆</div><p style="font-size:29px">Kesintisiz yaprak için <span class="hl">birkaç haftada bir</span> yeni tohum ek.</p></div></div>"""

d6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🧱</div><p style="font-size:33px">Küpe <b>doğrudan</b> ek, fideyi taşıma.</p></div>
<div class="card"><div class="ic">🏷️</div><p style="font-size:33px"><b>Bodur, geç çiçeklenen</b> çeşit seç.</p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px"><b>Dıştan</b> ve azar azar hasat et.</p></div>
<div class="card"><div class="ic">📆</div><p style="font-size:33px"><span class="hl">Kademeli</span> ekim yap.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Dereotunu en çok nereye koyarsın: börek mi, cacık mı?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: HAVA NEMİ ----------
n1 = """<div class="pad" style="padding-top:150px">
<span class="tag">HAVA NEMİ</span>
<h1 style="margin-top:50px">Bitkinin<br>gizli ayarı:<br>havadaki<br>nem 💧</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Fazlası da azı da<br><span class="hl">sorun çıkarır.</span></p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:115px;left:84px">
 <g transform="translate(640 10)">
  <rect x="0" y="20" width="230" height="180" rx="22" fill="#3C6E3A"/>
  <rect x="18" y="38" width="194" height="110" rx="12" fill="#FFF9EE"/>
  <text x="115" y="112" text-anchor="middle" font-family="Poppins" font-size="56" font-weight="800" fill="#2F5D2D">%?</text>
  <text x="115" y="182" text-anchor="middle" font-family="Poppins" font-size="22" font-weight="700" fill="#F4EBDD">NEM ÖLÇER</text>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="0" y="110">Ölçmeden bilinmez →</text><text x="0" y="150" fill="#7A6A52" font-size="26">gözle değil, sayıyla bak</text></g>
</svg></div>"""

n2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN ÖNEMLİ?</span>
<h2>Yaprak<br>su buharlaştırır</h2>
<p>Bitki yapraklarındaki gözeneklerden su buharı verir; buna <b>terleme</b> denir. Bu çekiş, kökten <b>su ve kalsiyumu</b> yukarı taşır.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🏜️</div><p style="font-size:30px"><b>Hava kuruysa</b> terleme hızlanır, bitki çabuk su kaybeder.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌫️</div><p style="font-size:30px"><b>Hava çok nemliyse</b> terleme yavaşlar, taşınma azalır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌡️</div><p style="font-size:30px"><b>Bağıl nem</b> sıcaklığa bağlıdır: hava soğuyunca <span class="hl">nem yükselir.</span></p></div></div>"""

n3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Çok kuru,<br>çok nemli</h2>
<svg width="912" height="780" viewBox="0 0 912 780">
 <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#E0A43A"/><stop offset="0.5" stop-color="#6FA84B"/><stop offset="1" stop-color="#5A8FB0"/></linearGradient></defs>
 <g font-family="Poppins" font-weight="700">
 <rect x="0" y="0" width="912" height="620" rx="26" fill="#FFF9EE"/>
 <rect x="40" y="50" width="832" height="44" rx="22" fill="url(#g)"/>
 <text x="40" y="140" font-size="28" fill="#B5473A">KURU</text>
 <text x="456" y="140" font-size="28" fill="#3C6E3A" text-anchor="middle">DENGELİ</text>
 <text x="872" y="140" font-size="28" fill="#3A6E8F" text-anchor="end">ÇOK NEMLİ</text>
 <path d="M456 98 L456 120" stroke="#3C6E3A" stroke-width="5"/>
 </g>
 <g font-family="Poppins" font-size="26" font-weight="600" fill="#2E3B2A">
  <rect x="30" y="180" width="410" height="410" rx="20" fill="#FBEBD0"/>
  <text x="55" y="230" font-weight="800" fill="#B5473A" font-size="28">Kuru havada</text>
  <text x="55" y="285">• Bitki çabuk pörsür</text>
  <text x="55" y="335">• Yaprak kenarları</text>
  <text x="80" y="370">kuruyabilir</text>
  <text x="55" y="420">• Kırmızı örümcek</text>
  <text x="80" y="455">kuru, sıcak havayı sever</text>
  <text x="55" y="505">• Su ve besin</text>
  <text x="80" y="540">tüketimi artar</text>
  <rect x="472" y="180" width="410" height="410" rx="20" fill="#DCEAF1"/>
  <text x="497" y="230" font-weight="800" fill="#3A6E8F" font-size="28">Nemli havada</text>
  <text x="497" y="285">• Kurşuni küf ve</text>
  <text x="522" y="320">mantarlar çoğalır</text>
  <text x="497" y="370">• Marulda uç yanığı</text>
  <text x="522" y="405">riski artar</text>
  <text x="497" y="455">• Gece yoğuşan su</text>
  <text x="522" y="490">yaprakta damlar</text>
  <text x="497" y="540">• Yosun ve koku</text>
 </g>
 <g font-family="Poppins" font-size="28" font-weight="600" fill="#2E3B2A">
 <text x="0" y="690">Amaç uç değerlerden kaçmak: <tspan fill="#2F5D2D" font-weight="800">orta nem</tspan></text>
 <text x="0" y="730">ve <tspan fill="#2F5D2D" font-weight="800">hareketli hava</tspan> çoğu bitkiye iyi gelir.</text>
 </g>
</svg></div>"""

n4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖLÇ &amp; AYARLA</span>
<h2 style="font-size:60px;margin:22px 0 26px">Nemi nasıl<br>dengelersin?</h2>
<div class="card" style="padding:20px 32px"><div class="ic">📟</div><p style="font-size:29px"><b>Nem ölçer (higrometre)</b> kullan; bitki hizasına koy, gece ve gündüz değerlerine bak.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌀</div><p style="font-size:29px"><b>Fan</b> ile hafif hava akışı sağla; yaprak çevresindeki nemli hava dağılır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪟</div><p style="font-size:29px"><b>Nem yüksekse</b> havalandır; seraya soğuk gece öncesi kısa havalandırma yoğuşmayı azaltır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💨</div><p style="font-size:29px"><b>Nem düşükse</b> nemlendirici kullan; ısıtıcıların <span class="hl">havayı kuruttuğunu</span> unutma.</p></div></div>"""

n5 = """<div class="pad" style="padding-top:150px">
<span class="tag">SIK HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunları<br>yapma</h2>
<div class="card" style="padding:20px 32px"><div class="ic">⛺</div><p style="font-size:29px"><b>Kapalı yetiştirme çadırında fan kullanmamak:</b> nem birikir, mantar başlar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🕛</div><p style="font-size:29px"><b>Sadece öğlen ölçmek:</b> nem çoğu zaman gece, hava soğuyunca yükselir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💦</div><p style="font-size:29px"><b>Yaprağa su püskürtüp nemi çözdüğünü sanmak:</b> etkisi kısa sürer, ıslak yaprak mantara davetiyedir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪣</div><p style="font-size:29px"><b>Depoyu açık bırakmak:</b> buharlaşan su, kapalı alanda <span class="hl">nemi artırır.</span></p></div></div>"""

n6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">💧</div><p style="font-size:33px">Nem, <b>terlemeyi</b> ve su taşınmasını etkiler.</p></div>
<div class="card"><div class="ic">📟</div><p style="font-size:33px"><b>Ölçmeden</b> tahmin etme.</p></div>
<div class="card"><div class="ic">🌀</div><p style="font-size:33px"><b>Hava akışı</b> mantarı azaltır.</p></div>
<div class="card"><div class="ic">🌙</div><p style="font-size:33px"><span class="hl">Gece nemine</span> dikkat et.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Senin yetiştirme alanında nem kaç?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Dereotu<br>fide<br>taşımayı<br>sevmez! 🌿</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Aşağı inen bir <b>kazık kökü</b> var. Bu yüzden <span class="hl">yerinde ekmek</span> en iyisi.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🌱</div><p style="font-size:40px"><b>Topraksız nasıl yetişir?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([d1, d2, d3, d4, d5, d6], "gun23/dereotu")
    render_post([n1, n2, n3, n4, n5, n6], "gun23/nem")
    render_story(story, "gun23/hikaye")
