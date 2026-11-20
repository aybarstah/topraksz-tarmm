import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ NANE ----------
n1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ NANE</span>
<h1 style="margin-top:50px">Bir dal<br>naneden<br>bütün bir<br>saksı 🌿</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Tohum şart değil,<br><span class="hl">bir bardak su yeter.</span></p>
<svg width="912" height="260" viewBox="0 0 912 260" style="position:absolute;bottom:115px;left:84px">
 <rect x="560" y="70" width="150" height="180" rx="18" fill="#CFE3EE" opacity=".8" stroke="#9BBFD0" stroke-width="5"/>
 <rect x="566" y="120" width="138" height="124" rx="14" fill="#9CC9DA"/>
 <path d="M635 240 L635 20" stroke="#3C6E3A" stroke-width="8"/>
 <g fill="#5E9B4F"><ellipse cx="600" cy="40" rx="36" ry="20" transform="rotate(-20 600 40)"/><ellipse cx="670" cy="40" rx="36" ry="20" transform="rotate(20 670 40)"/>
 <ellipse cx="605" cy="85" rx="32" ry="18" transform="rotate(-20 605 85)"/><ellipse cx="665" cy="85" rx="32" ry="18" transform="rotate(20 665 85)"/></g>
 <g stroke="#FFF9EE" stroke-width="4" fill="none" stroke-linecap="round"><path d="M635 200 Q615 215 605 235"/><path d="M635 200 Q655 215 668 236"/><path d="M635 175 Q612 185 598 195"/><path d="M635 175 Q660 185 674 196"/></g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="200" y="130">Çelik → kök</text><text x="200" y="170" fill="#7A6A52" font-size="26">genelde 1-2 haftada</text></g>
 <path d="M440 140 L540 140" stroke="#7A6A52" stroke-width="5"/><path d="M528 128 L545 140 L528 152" stroke="#7A6A52" stroke-width="5" fill="none"/>
</svg></div>"""

n2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN NANE?</span>
<h2>Zor beğenmez,<br>hızlı büyür</h2>
<p>Nane, topraksız sisteme en kolay uyum sağlayan aromatik bitkilerdendir.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">💧</div><p style="font-size:30px"><b>Nemli kökü sever;</b> suda yaşamaya yatkındır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">⛅</div><p style="font-size:30px"><b>Yarı gölgeye dayanır</b>, ama aydınlıkta daha gür ve aromalı olur.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">✂️</div><p style="font-size:30px">Kestikçe <span class="hl">yeniden sürer;</span> aylarca hasat.</p></div></div>"""

n3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Çelikle<br>çoğaltma</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="20" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="321" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="622" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <text x="155" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">1</text>
 <text x="456" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">2</text>
 <text x="757" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">3</text>
 <path d="M155 400 L155 130" stroke="#3C6E3A" stroke-width="8"/>
 <g fill="#5E9B4F"><ellipse cx="120" cy="150" rx="34" ry="18" transform="rotate(-20 120 150)"/><ellipse cx="190" cy="150" rx="34" ry="18" transform="rotate(20 190 150)"/></g>
 <g fill="#C9B48E"><circle cx="155" cy="250" r="9"/><circle cx="155" cy="320" r="9"/></g>
 <path d="M110 395 L200 395" stroke="#7A6A52" stroke-width="5"/>
 <rect x="391" y="190" width="130" height="220" rx="16" fill="#CFE3EE" stroke="#9BBFD0" stroke-width="5"/>
 <rect x="396" y="250" width="120" height="155" rx="12" fill="#9CC9DA"/>
 <path d="M456 380 L456 120" stroke="#3C6E3A" stroke-width="8"/>
 <g fill="#5E9B4F"><ellipse cx="421" cy="140" rx="34" ry="18" transform="rotate(-20 421 140)"/><ellipse cx="491" cy="140" rx="34" ry="18" transform="rotate(20 491 140)"/></g>
 <g stroke="#FFF9EE" stroke-width="4" fill="none" stroke-linecap="round"><path d="M456 340 Q436 352 426 372"/><path d="M456 340 Q476 352 486 372"/><path d="M456 300 Q434 310 422 322"/><path d="M456 300 Q478 310 490 322"/></g>
 <rect x="672" y="300" width="170" height="110" rx="12" fill="#5B6B57"/>
 <rect x="662" y="290" width="190" height="22" rx="8" fill="#3C6E3A"/>
 <path d="M757 290 L757 130" stroke="#3C6E3A" stroke-width="8"/>
 <g fill="#5E9B4F"><ellipse cx="722" cy="150" rx="34" ry="18" transform="rotate(-20 722 150)"/><ellipse cx="792" cy="150" rx="34" ry="18" transform="rotate(20 792 150)"/><ellipse cx="725" cy="215" rx="34" ry="18" transform="rotate(-20 725 215)"/><ellipse cx="789" cy="215" rx="34" ry="18" transform="rotate(20 789 215)"/></g>
 <g stroke="#E9DCC4" stroke-width="4" fill="none" stroke-linecap="round"><path d="M757 315 Q737 350 727 395"/><path d="M757 315 Q777 350 790 395"/><path d="M757 315 L757 400"/></g>
 </g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
 <text x="155" y="500" text-anchor="middle">Sağlıklı dalı</text><text x="155" y="536" text-anchor="middle">boğum altından</text><text x="155" y="572" text-anchor="middle">kes, alt yaprakları</text><text x="155" y="608" text-anchor="middle">temizle</text>
 <text x="456" y="500" text-anchor="middle">Boğumlar suda</text><text x="456" y="536" text-anchor="middle">kalsın, yapraklar</text><text x="456" y="572" text-anchor="middle">dışarıda; suyu</text><text x="456" y="608" text-anchor="middle">sık tazele</text>
 <text x="757" y="500" text-anchor="middle">Kökler birkaç</text><text x="757" y="536" text-anchor="middle">santim olunca</text><text x="757" y="572" text-anchor="middle">sisteme aktar</text>
 </g>
</svg></div>"""

n4 = """<div class="pad" style="padding-top:150px">
<span class="tag">BAKIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Gür nane<br>için</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🫙</div><p style="font-size:29px"><b>Kratky ve DWC</b> evde en kolay seçimler; küçük bir kap bile yeter.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px">Dalı <b>bir yaprak çiftinin üstünden</b> kes; oradan yeni sürgünler çıkar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌸</div><p style="font-size:29px"><b>Çiçek tomurcuğunu</b> erken kopar; bitki yaprak yapmaya devam eder.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔄</div><p style="font-size:29px">Hiçbir zaman <span class="hl">bitkinin tamamını</span> birden kesme.</p></div></div>"""

n5 = """<div class="pad" style="padding-top:150px">
<span class="tag">SIK YAPILAN HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Dikkat<br>et</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🕸️</div><p style="font-size:29px"><b>Kökler istilacıdır:</b> NFT oluğunu ve pompa girişini tıkayabilir. Naneyi <b>ayrı kapta</b> yetiştir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌱</div><p style="font-size:29px"><b>Tohumdan ekmek:</b> nane kolay melezlenir; tohumdan çıkan bitki aynı kokuyu vermeyebilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🟠</div><p style="font-size:29px"><b>Yaprak altında turuncu kabarcık:</b> pas hastalığı. Hasta dalları at.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:29px"><b>Ilık, durgun su:</b> kökler kahverengi ve kaygan olursa <span class="hl">kök çürümesi.</span></p></div></div>"""

n6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🥛</div><p style="font-size:33px">Bir dal <b>suda köklenir.</b></p></div>
<div class="card"><div class="ic">🫙</div><p style="font-size:33px">Kratky / DWC, <b>ayrı kap.</b></p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px">Yaprak çiftinin <b>üstünden</b> kes.</p></div>
<div class="card"><div class="ic">🌸</div><p style="font-size:33px">Çiçeği <span class="hl">erken</span> kopar.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Mutfağında nane var mı?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: MARULDA UÇ YANIĞI ----------
u1 = """<div class="pad" style="padding-top:150px">
<span class="tag">MARULDA UÇ YANIĞI</span>
<h1 style="margin-top:50px">Çözeltide<br>kalsiyum var,<br>yaprak yine<br>yanıyor 🥬</h1>
<p style="font-size:42px;margin-top:36px;font-weight:600">Sorun gübrede değil,<br><span class="hl">taşınmada olabilir.</span></p>
<svg width="912" height="230" viewBox="0 0 912 230" style="position:absolute;bottom:110px;left:84px">
 <g transform="translate(640 120)">
 <ellipse cx="-70" cy="30" rx="80" ry="55" fill="#6FA84B" transform="rotate(-25 -70 30)"/>
 <ellipse cx="70" cy="30" rx="80" ry="55" fill="#6FA84B" transform="rotate(25 70 30)"/>
 <ellipse cx="0" cy="0" rx="60" ry="80" fill="#9CCB6B"/>
 <path d="M-55 -30 Q0 -105 55 -30" stroke="#8B5A2B" stroke-width="12" fill="none" stroke-linecap="round"/>
 </g>
 <g font-family="Poppins" font-size="28" font-weight="700" fill="#7A6A52"><text x="160" y="60">Genç iç yaprak</text><text x="160" y="96" fill="#8B5A2B">kenarı kahverengi</text></g>
 <path d="M440 75 L570 75" stroke="#7A6A52" stroke-width="5"/>
</svg></div>"""

u2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDİR?</span>
<h2>Uç yanığı<br>(tipburn)</h2>
<p>Marulun <b>ortadaki genç yapraklarının</b> kenarlarının kahverengileşip kurumasıdır.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🦴</div><p style="font-size:30px">Sebebi, büyüyen dokuda <b>yerel kalsiyum eksikliği.</b></p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🚚</div><p style="font-size:30px">Kalsiyum bitkide <b>suyla taşınır</b> ve yaşlı yapraktan gence geçemez.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🥬</div><p style="font-size:30px">Bu yüzden çözeltide yeterli olsa bile <span class="hl">iç yapraklar</span> aç kalabilir.</p></div></div>"""

u3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Kalsiyum<br>nereye gider?</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <rect x="80" y="560" width="752" height="170" rx="20" fill="#9CC9DA"/>
 <rect x="80" y="540" width="752" height="30" rx="8" fill="#5B6B57"/>
 <g stroke="#FFF9EE" stroke-width="5" fill="none" stroke-linecap="round"><path d="M456 570 Q430 620 410 700"/><path d="M456 570 Q480 630 500 700"/><path d="M456 570 L456 710"/></g>
 <ellipse cx="300" cy="420" rx="170" ry="80" fill="#6FA84B" transform="rotate(-20 300 420)"/>
 <ellipse cx="612" cy="420" rx="170" ry="80" fill="#6FA84B" transform="rotate(20 612 420)"/>
 <ellipse cx="456" cy="300" rx="80" ry="140" fill="#9CCB6B"/>
 <path d="M386 220 Q456 130 526 220" stroke="#8B5A2B" stroke-width="14" fill="none" stroke-linecap="round"/>
 <g stroke="#2F5D2D" stroke-width="7" fill="none"><path d="M456 540 L456 470"/><path d="M456 500 Q380 470 240 410"/><path d="M456 500 Q532 470 672 410"/></g>
 <g fill="#2F5D2D"><path d="M226 398 L250 396 L240 420Z"/><path d="M686 398 L662 396 L672 420Z"/></g>
 <g font-family="Poppins" font-size="28" font-weight="700" fill="#2E3B2A">
  <text x="20" y="300">Dış yaprak</text><text x="20" y="335">çok terler →</text><text x="20" y="370" fill="#3C6E3A">bol kalsiyum</text>
  <text x="660" y="230">İç yaprak</text><text x="660" y="265">az terler →</text><text x="660" y="300" fill="#8B5A2B">az kalsiyum</text>
  <text x="120" y="660" fill="#2E3B2A">Ca²⁺ çözeltide</text>
 </g>
 <g stroke="#7A6A52" stroke-width="4"><line x1="650" y1="250" x2="530" y2="215"/></g>
 <text x="456" y="90" font-family="Poppins" font-size="30" font-weight="700" fill="#7A6A52" text-anchor="middle">Su (ve kalsiyum) en çok terleyen yaprağa akar</text>
</svg></div>"""

u4 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDENLERİ</span>
<h2 style="font-size:60px;margin:22px 0 26px">Riski ne<br>artırır?</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🌫️</div><p style="font-size:29px"><b>Yüksek nem ve durgun hava:</b> yaprak terleyemez, su akışı yavaşlar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🚀</div><p style="font-size:29px"><b>Çok hızlı büyüme:</b> güçlü ışık ve sıcakta yeni doku kalsiyumdan hızlı oluşur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧂</div><p style="font-size:29px"><b>Yüksek EC:</b> köklerin su alımı zorlaşır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📏</div><p style="font-size:29px"><b>Hasadı geciktirmek:</b> baş iri ve sıkı oldukça <span class="hl">risk artar.</span></p></div></div>"""

u5 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÇÖZÜM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Nasıl<br>önlenir?</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🌀</div><p style="font-size:29px"><b>Hava hareketi:</b> küçük bir fanla bitkilerin üstünde hafif hava akışı sağla.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💨</div><p style="font-size:29px"><b>Nemi dengele:</b> özellikle gece havalandır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">⚖️</div><p style="font-size:29px"><b>EC'yi gereksiz yükseltme;</b> "fazla gübre daha iyi" değildir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Ekstra kalsiyum</b> genelde çözmez; sorun eksiklik değil, <span class="hl">taşınma.</span></p></div></div>"""

u6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🥬</div><p style="font-size:33px">Uç yanığı = <b>iç yaprakta Ca eksiği.</b></p></div>
<div class="card"><div class="ic">🚚</div><p style="font-size:33px">Sorun çoğu zaman <b>taşınma.</b></p></div>
<div class="card"><div class="ic">🌀</div><p style="font-size:33px">Hava akışı + <b>dengeli nem.</b></p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px">Hasadı <span class="hl">geciktirme.</span></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Marulunda bu izi gördün mü?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Naneyi<br>tohumdan<br>ekmene gerek<br>yok! 🌿</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Sağlıklı bir nane dalı <span class="hl">bir bardak suda</span> kök salar.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">✂️</div><p style="font-size:40px"><b>Nereden kesmeli?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([n1, n2, n3, n4, n5, n6], "gun17/nane")
    render_post([u1, u2, u3, u4, u5, u6], "gun17/ucyanigi")
    render_story(story, "gun17/hikaye")
