import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ PAK CHOI ----------
p1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ PAK CHOI</span>
<h1 style="margin-top:50px">Baş bağlamayan<br>lahana:<br>pak choi 🥬</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Çıtır sap, yumuşak yaprak,<br><span class="hl">serin havada hızlı büyüme.</span></p>
<svg width="912" height="260" viewBox="0 0 912 260" style="position:absolute;bottom:105px;left:84px">
 <g transform="translate(640 0)">
  <rect x="20" y="200" width="220" height="50" rx="12" fill="#5B6B57"/>
  <path d="M130 200 C118 160 96 120 70 70" stroke="#F1F3E6" stroke-width="18" fill="none" stroke-linecap="round"/>
  <path d="M130 200 C142 160 164 120 190 70" stroke="#F1F3E6" stroke-width="18" fill="none" stroke-linecap="round"/>
  <path d="M130 200 C130 150 130 100 130 50" stroke="#F1F3E6" stroke-width="18" fill="none" stroke-linecap="round"/>
  <ellipse cx="62" cy="58" rx="44" ry="56" fill="#4F8E3E" transform="rotate(-25 62 58)"/>
  <ellipse cx="198" cy="58" rx="44" ry="56" fill="#4F8E3E" transform="rotate(25 198 58)"/>
  <ellipse cx="130" cy="40" rx="42" ry="56" fill="#6FA84B"/>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="0" y="130">Kratky, DWC ya da NFT →</text><text x="0" y="170" fill="#7A6A52" font-size="26">yapraklı sistemlere çok uygun</text></g>
</svg></div>"""

p2 = """<div class="pad" style="padding-top:150px">
<span class="tag">TANIYALIM</span>
<h2>Şalgamla<br>aynı tür!</h2>
<p>Pak choi (bok choy) <b><i>Brassica rapa</i></b> türüdür: <b>şalgam</b> ve baş bağlayan Çin lahanası ile aynı tür, turpgiller ailesinden.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🥬</div><p style="font-size:30px"><b>Baş bağlamaz;</b> kalın saplar tabanda bir rozet oluşturur.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">⚡</div><p style="font-size:30px"><b>Tohumu çabuk çimlenir;</b> çoğu zaman birkaç gün yeter.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">❄️</div><p style="font-size:30px"><b>Serin sever;</b> sıcakta ve uzun günde <span class="hl">çiçeğe kalkar.</span></p></div></div>"""

p3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Küpten hasada,<br>3 adımda</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <g font-family="Poppins" font-weight="700">
 <rect x="20" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="321" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <rect x="622" y="20" width="270" height="420" rx="26" fill="#FFF9EE"/>
 <text x="155" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">1</text>
 <text x="456" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">2</text>
 <text x="757" y="80" font-size="40" text-anchor="middle" fill="#3C6E3A">3</text>
 <!-- 1 küp + tohum -->
 <rect x="100" y="250" width="110" height="100" rx="10" fill="#C9B48E"/>
 <g stroke="#A8916A" stroke-width="3"><line x1="100" y1="285" x2="210" y2="285"/><line x1="100" y1="318" x2="210" y2="318"/></g>
 <path d="M155 250 L155 205" stroke="#3C6E3A" stroke-width="5"/>
 <ellipse cx="138" cy="208" rx="18" ry="9" fill="#6FA84B"/><ellipse cx="172" cy="208" rx="18" ry="9" fill="#6FA84B"/>
 <!-- 2 file saksı sistemde -->
 <rect x="351" y="290" width="210" height="110" rx="10" fill="#5B6B57"/>
 <rect x="363" y="320" width="186" height="70" rx="6" fill="#7FB0C9"/>
 <path d="M421 260 L491 260 L483 340 L429 340 Z" fill="#3F4B3C"/>
 <path d="M456 262 C450 230 438 205 420 185" stroke="#F1F3E6" stroke-width="9" fill="none" stroke-linecap="round"/>
 <path d="M456 262 C462 230 474 205 492 185" stroke="#F1F3E6" stroke-width="9" fill="none" stroke-linecap="round"/>
 <ellipse cx="414" cy="176" rx="22" ry="30" fill="#4F8E3E" transform="rotate(-25 414 176)"/>
 <ellipse cx="498" cy="176" rx="22" ry="30" fill="#4F8E3E" transform="rotate(25 498 176)"/>
 <g stroke="#E8DCC4" stroke-width="4"><path d="M445 340 L440 385"/><path d="M456 340 L456 390"/><path d="M467 340 L472 385"/></g>
 <!-- 3 hasat: makas -->
 <path d="M757 330 C745 280 725 240 700 200" stroke="#F1F3E6" stroke-width="14" fill="none" stroke-linecap="round"/>
 <path d="M757 330 C769 280 789 240 814 200" stroke="#F1F3E6" stroke-width="14" fill="none" stroke-linecap="round"/>
 <path d="M757 330 C757 270 757 220 757 175" stroke="#F1F3E6" stroke-width="14" fill="none" stroke-linecap="round"/>
 <ellipse cx="694" cy="186" rx="32" ry="44" fill="#4F8E3E" transform="rotate(-25 694 186)"/>
 <ellipse cx="820" cy="186" rx="32" ry="44" fill="#4F8E3E" transform="rotate(25 820 186)"/>
 <ellipse cx="757" cy="160" rx="30" ry="44" fill="#6FA84B"/>
 <path d="M690 345 L830 345" stroke="#2F5D2D" stroke-width="4" stroke-dasharray="10 7"/>
 <text x="840" y="395" font-size="44" text-anchor="middle">✂️</text>
 </g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
 <text x="155" y="500" text-anchor="middle">Kaya yünü küpe</text><text x="155" y="536" text-anchor="middle">1-2 tohum ek,</text><text x="155" y="572" text-anchor="middle">nemli tut</text>
 <text x="456" y="500" text-anchor="middle">Kök küpten çıkınca</text><text x="456" y="536" text-anchor="middle">file saksıyla</text><text x="456" y="572" text-anchor="middle">sisteme aktar</text>
 <text x="757" y="500" text-anchor="middle">Dış yapraklarını al</text><text x="757" y="536" text-anchor="middle">ya da bütün bitkiyi</text><text x="757" y="572" text-anchor="middle">tabandan kes</text>
 </g>
 <g font-family="Poppins" font-size="28" font-weight="600" fill="#2E3B2A">
 <text x="20" y="660">Mini (baby) pak choi için <tspan fill="#2F5D2D" font-weight="800">genç hasat</tspan> et:</text>
 <text x="20" y="700">sap daha körpe, tadı daha yumuşak olur.</text>
 </g>
</svg></div>"""

p4 = """<div class="pad" style="padding-top:150px">
<span class="tag">BAKIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Sağlıklı<br>pak choi için</h2>
<div class="card" style="padding:20px 32px"><div class="ic">☀️</div><p style="font-size:29px"><b>Bol ışık ver;</b> ışık az olursa saplar uzar, bitki gevşek ve soluk kalır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:29px"><b>Serin ortam</b> tercih et; sıcakta yapraklar sertleşir, bitki çiçeğe kalkar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💨</div><p style="font-size:29px"><b>Hava akışını sağla;</b> marul gibi pak choi de <span class="hl">uç yanığına</span> (kalsiyum) yatkındır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📏</div><p style="font-size:29px"><b>Aralık bırak;</b> rozet yana açılır, sık dikimde yapraklar havasız kalır.</p></div></div>"""

p5 = """<div class="pad" style="padding-top:150px">
<span class="tag">SORUNLAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunlara<br>dikkat</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🌼</div><p style="font-size:29px"><b>Ortada çiçek sapı yükseliyorsa</b> bitki çiçeğe kalkıyordur; hemen hasat et.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🐛</div><p style="font-size:29px"><b>Lahana kelebeği tırtılı:</b> yaprak altında yumurtaya bak; serada <b>böcek tülü</b> kullan.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🐜</div><p style="font-size:29px"><b>Yaprak biti</b> genç yapraklarda ve sap diplerinde toplanır; erken fark et.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🕳️</div><p style="font-size:29px"><b>Yaprakta minik delikler</b> pire böceği belirtisi olabilir; <span class="hl">tül yine işe yarar.</span></p></div></div>"""

p6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">❄️</div><p style="font-size:33px"><b>Serin</b> ve <b>aydınlık</b> ortam.</p></div>
<div class="card"><div class="ic">🫙</div><p style="font-size:33px"><b>Kratky, DWC, NFT</b> uygundur.</p></div>
<div class="card"><div class="ic">💨</div><p style="font-size:33px"><b>Hava akışı</b> uç yanığını azaltır.</p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px">Çiçeğe kalkmadan <span class="hl">hasat et.</span></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Pak choi'yi hiç denedin mi: sote mi, çorbada mı?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: ÜRETİM DEFTERİ ----------
d1 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÜRETİM DEFTERİ</span>
<h1 style="margin-top:50px">Sorunu<br>tahmin etme,<br>kaydını tut 📓</h1>
<p style="font-size:42px;margin-top:40px;font-weight:600">Birkaç satırlık not,<br><span class="hl">nedeni bulmanı kolaylaştırır.</span></p>
<svg width="912" height="240" viewBox="0 0 912 240" style="position:absolute;bottom:110px;left:84px">
 <g transform="translate(620 0)">
  <rect x="20" y="10" width="240" height="220" rx="14" fill="#FFF9EE" stroke="#C9B48E" stroke-width="4"/>
  <rect x="20" y="10" width="34" height="220" rx="10" fill="#3C6E3A"/>
  <g stroke="#C9B48E" stroke-width="3"><line x1="74" y1="60" x2="236" y2="60"/><line x1="74" y1="100" x2="236" y2="100"/><line x1="74" y1="140" x2="236" y2="140"/><line x1="74" y1="180" x2="236" y2="180"/></g>
  <g font-family="Poppins" font-size="22" font-weight="700" fill="#2F5D2D"><text x="78" y="52">EC 1,4</text><text x="78" y="92">pH 6,0</text><text x="78" y="132">19 °C</text><text x="78" y="172">+2 L su</text></g>
 </g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2F5D2D"><text x="0" y="110">Her ölçüm bir ipucu →</text><text x="0" y="150" fill="#7A6A52" font-size="26">defter ya da telefonda tablo</text></g>
</svg></div>"""

d2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN?</span>
<h2>Hafıza yanıltır,<br>kayıt yanıltmaz</h2>
<p>Topraksız sistemde sorunlar çoğu zaman <b>günler içinde yavaşça</b> gelişir. Yaprak sararınca geriye bakacak kaydın olursa nedeni daha kolay bulursun.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">📈</div><p style="font-size:30px"><b>Eğilimi görürsün:</b> tek ölçüm değil, günden güne değişim.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🔁</div><p style="font-size:30px"><b>İşe yarayanı tekrarlarsın:</b> başarılı ekimin tarifi elinde olur.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🙋</div><p style="font-size:30px"><b>Yardım isterken</b> <span class="hl">gerçek veriyle</span> sorarsın.</p></div></div>"""

d3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Bir sayfada<br>neler olsun?</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <rect x="20" y="10" width="872" height="560" rx="26" fill="#FFF9EE"/>
 <rect x="20" y="10" width="872" height="80" rx="26" fill="#3C6E3A"/>
 <rect x="20" y="60" width="872" height="30" fill="#3C6E3A"/>
 <g font-family="Poppins" font-size="28" font-weight="700" fill="#F4EBDD">
  <text x="50" y="62">Tarih</text><text x="200" y="62">EC</text><text x="310" y="62">pH</text><text x="420" y="62">Su °C</text><text x="560" y="62">Eklenen</text><text x="720" y="62">Not</text>
 </g>
 <g stroke="#E3D3B8" stroke-width="3"><line x1="40" y1="180" x2="872" y2="180"/><line x1="40" y1="270" x2="872" y2="270"/><line x1="40" y1="360" x2="872" y2="360"/><line x1="40" y1="450" x2="872" y2="450"/></g>
 <g font-family="Poppins" font-size="27" font-weight="600" fill="#2E3B2A">
  <text x="50" y="145">1. gün</text><text x="200" y="145">1,2</text><text x="310" y="145">5,9</text><text x="420" y="145">19</text><text x="560" y="145">çözelti</text><text x="720" y="145">aktarma</text>
  <text x="50" y="235">3. gün</text><text x="200" y="235">1,3</text><text x="310" y="235">6,1</text><text x="420" y="235">20</text><text x="560" y="235">1 L su</text><text x="720" y="235">büyüme</text>
  <text x="50" y="325">5. gün</text><text x="200" y="325" fill="#B5683E" font-weight="800">1,5</text><text x="310" y="325">6,2</text><text x="420" y="325">21</text><text x="560" y="325">2 L su</text><text x="720" y="325">sıcak gün</text>
  <text x="50" y="415">7. gün</text><text x="200" y="415">1,3</text><text x="310" y="415">6,0</text><text x="420" y="415">19</text><text x="560" y="415">sade su</text><text x="720" y="415">kök beyaz</text>
  <text x="50" y="505" fill="#7A6A52">…</text>
 </g>
 <g font-family="Poppins" font-size="26" font-weight="600" fill="#7A6A52"><text x="456" y="545" text-anchor="middle">(örnek tablo; değerler bitkiye ve sisteme göre değişir)</text></g>
 <g font-family="Poppins" font-size="28" font-weight="600" fill="#2E3B2A">
  <text x="20" y="650">Ayrıca yaz: <tspan fill="#2F5D2D" font-weight="800">ekim/aktarma tarihi, çeşit,</tspan></text>
  <text x="20" y="690">ışık süresi, tam değişim günü, hasat.</text>
 </g>
</svg></div>"""

d4 = """<div class="pad" style="padding-top:150px">
<span class="tag">İPUÇLARI</span>
<h2 style="font-size:60px;margin:22px 0 26px">Kaydın işe<br>yaraması için</h2>
<div class="card" style="padding:20px 32px"><div class="ic">⏰</div><p style="font-size:29px"><b>Her gün aynı saatte ölç;</b> su sıcaklığı ve pH gün içinde değişebilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📷</div><p style="font-size:29px"><b>Aynı açıdan fotoğraf çek;</b> yaprak rengi ve büyüme farkı yan yana belli olur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">1️⃣</div><p style="font-size:29px"><b>Tek seferde tek şeyi değiştir;</b> yoksa hangisinin <span class="hl">etki ettiğini bilemezsin.</span></p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧪</div><p style="font-size:29px"><b>Ölçerin kalibrasyon tarihini</b> de not et; kayan ölçer kaydı yanıltır.</p></div></div>"""

d5 = """<div class="pad" style="padding-top:150px">
<span class="tag">KAYDI OKUMAK</span>
<h2 style="font-size:60px;margin:22px 0 26px">Rakamlar<br>ne anlatıyor?</h2>
<div class="card" style="padding:20px 32px"><div class="ic">⬆️</div><p style="font-size:29px"><b>EC yükseliyorsa</b> bitki besinden çok su alıyordur; genelde <b>sade su</b> ile tamamlanır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">⬇️</div><p style="font-size:29px"><b>EC düşüyorsa</b> bitki besini hızlı alıyordur; <b>hafif çözelti</b> ile tamamlanır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💧</div><p style="font-size:29px"><b>Su tüketimi birden arttıysa</b> sıcaklığa, kuru havaya ya da büyüyen bitkiye bak.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔍</div><p style="font-size:29px"><b>Sorun çıkınca</b> son günlerin satırlarına bak: <span class="hl">ne değişmiş?</span></p></div></div>"""

d6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">📓</div><p style="font-size:33px"><b>EC, pH, su sıcaklığı</b> ve ekleneni yaz.</p></div>
<div class="card"><div class="ic">⏰</div><p style="font-size:33px"><b>Aynı saatte</b> ölç, aynı açıdan çek.</p></div>
<div class="card"><div class="ic">1️⃣</div><p style="font-size:33px"><b>Tek seferde</b> tek değişiklik.</p></div>
<div class="card"><div class="ic">📈</div><p style="font-size:33px">Tek ölçüme değil, <span class="hl">eğilime</span> bak.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sen kayıt tutuyor musun: defter mi, telefon mu?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Pak choi,<br>lahanadan çok<br>şalgama<br>yakındır! 🥬</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Pak choi ile şalgam <b>aynı türdür</b> (<i>Brassica rapa</i>). Baş lahana ise <span class="hl">başka bir tür.</span></p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🌱</div><p style="font-size:40px"><b>Topraksız pak choi nasıl yetişir?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([p1, p2, p3, p4, p5, p6], "gun25/pakchoi")
    render_post([d1, d2, d3, d4, d5, d6], "gun25/defter")
    render_story(story, "gun25/hikaye")
