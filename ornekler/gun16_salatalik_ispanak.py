import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TOPRAKSIZ SALATALIK ----------
s1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ SALATALIK</span>
<h1 style="margin-top:50px">Arı yok,<br>salatalık<br>var mı? 🥒</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Seradaki salatalığın<br><span class="hl">az bilinen sırları.</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <rect x="60" y="250" width="792" height="18" rx="8" fill="#B59A6E"/>
 <line x1="456" y1="0" x2="456" y2="250" stroke="#B59A6E" stroke-width="4" stroke-dasharray="10 8"/>
 <path d="M456 250 Q440 180 456 120 Q472 60 456 10" stroke="#3C6E3A" stroke-width="9" fill="none"/>
 <g fill="#5E9B4F"><ellipse cx="400" cy="190" rx="48" ry="26"/><ellipse cx="512" cy="130" rx="48" ry="26"/><ellipse cx="400" cy="70" rx="44" ry="24"/></g>
 <rect x="474" y="170" width="34" height="96" rx="17" fill="#4E8A3E"/>
 <circle cx="491" cy="164" r="12" fill="#F2C94C"/>
 <rect x="360" y="100" width="30" height="80" rx="15" fill="#4E8A3E"/>
 <circle cx="375" cy="95" r="11" fill="#F2C94C"/>
</svg></div>"""

s2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEYİ SEVER?</span>
<h2>Sıcak, ışık<br>ve bol su</h2>
<p>Salatalık hızlı büyüyen, <b>çok su ve besin</b> tüketen bir bitkidir. Soğuğu hiç sevmez.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🌡️</div><p style="font-size:30px"><b>Ilık ortam ister;</b> soğuk gecelerde büyümesi durur.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">💧</div><p style="font-size:30px"><b>Damla sulama + cocopeat</b> ya da kaya yünü en yaygın seçim.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">☀️</div><p style="font-size:30px">Az ışıkta verim düşer; <span class="hl">aydınlık yer</span> şart.</p></div></div>"""

s3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">Tek gövde,<br>ipe sar</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <rect x="80" y="40" width="752" height="14" rx="7" fill="#8C7550"/>
 <line x1="456" y1="54" x2="456" y2="640" stroke="#B59A6E" stroke-width="4" stroke-dasharray="10 8"/>
 <path d="M456 690 Q430 560 456 430 Q482 300 456 170 Q440 100 456 60" stroke="#3C6E3A" stroke-width="12" fill="none"/>
 <path d="M456 60 Q560 70 600 200" stroke="#3C6E3A" stroke-width="9" fill="none"/>
 <path d="M456 60 Q352 70 312 200" stroke="#3C6E3A" stroke-width="9" fill="none"/>
 <g fill="#5E9B4F"><ellipse cx="380" cy="300" rx="58" ry="30"/><ellipse cx="532" cy="240" rx="58" ry="30"/><ellipse cx="380" cy="160" rx="54" ry="28"/></g>
 <rect x="474" y="300" width="30" height="90" rx="15" fill="#4E8A3E"/>
 <rect x="590" y="200" width="26" height="76" rx="13" fill="#4E8A3E"/>
 <rect x="296" y="200" width="26" height="76" rx="13" fill="#4E8A3E"/>
 <rect x="376" y="660" width="160" height="70" rx="12" fill="#E9DCC4" stroke="#B59A6E" stroke-width="6"/>
 <g font-family="Poppins" font-size="28" font-weight="700" fill="#2E3B2A">
  <text x="640" y="110">Tepe telini</text><text x="640" y="145">aşınca uç al,</text><text x="640" y="180" fill="#3C6E3A">2 dal sarksın</text>
  <text x="560" y="420">Meyve gövdede</text>
  <text x="40" y="540">Alt boğumlar</text><text x="40" y="575" fill="#3C6E3A">temiz kalsın</text>
  <text x="560" y="710">Cocopeat torba</text>
 </g>
 <g stroke="#7A6A52" stroke-width="4"><line x1="250" y1="555" x2="440" y2="555"/><line x1="555" y1="410" x2="510" y2="350"/></g>
</svg></div>"""

s4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÇİÇEK VE MEYVE</span>
<h2 style="font-size:60px;margin:22px 0 26px">Arı olmadan<br>meyve</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🌼</div><p style="font-size:29px"><b>Dişi çiçeğin</b> arkasında minik bir salatalık vardır; erkek çiçekte yoktur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🐝</div><p style="font-size:29px">Birçok sera çeşidi <b>partenokarpiktir:</b> tozlaşma olmadan meyve bağlar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📦</div><p style="font-size:29px">Bunu <b>tohum paketinden</b> öğren; serada bu çeşitler tercih edilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🖌️</div><p style="font-size:29px">Partenokarpik değilse tozlaşma gerekir: arı ya da <span class="hl">fırçayla elle.</span></p></div></div>"""

s5 = """<div class="pad" style="padding-top:150px">
<span class="tag">SIK YAPILAN HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Neden<br>olmadı?</h2>
<div class="card" style="padding:20px 32px"><div class="ic">😖</div><p style="font-size:29px"><b>Acı salatalık:</b> genelde <b>stres</b> işaretidir; düzensiz sulama, aşırı sıcak.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">⚪</div><p style="font-size:29px"><b>Yaprakta beyaz pudra:</b> külleme. Havalandır, yaprakları sıkışık bırakma.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🐢</div><p style="font-size:29px"><b>Geç hasat:</b> iri meyve dalda kalırsa bitki yeni meyveyi yavaşlatır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">〰️</div><p style="font-size:29px"><b>Eğri, şekilsiz meyve:</b> çoğu zaman stres ya da <span class="hl">fazla meyve yükü.</span></p></div></div>"""

s6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🌡️</div><p style="font-size:33px"><b>Ilık, aydınlık</b> ve bol su.</p></div>
<div class="card"><div class="ic">🧵</div><p style="font-size:33px">Tek gövde, <b>ipe sar.</b></p></div>
<div class="card"><div class="ic">🐝</div><p style="font-size:33px">Partenokarpik çeşit <b>arı istemez.</b></p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px">Sık ve <span class="hl">genç</span> hasat et.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Salatalık yetiştirdin mi?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: TOPRAKSIZ ISPANAK ----------
i1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ ISPANAK</span>
<h1 style="margin-top:50px">Kışın<br>yıldızı:<br>ıspanak 🍃</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Serin havayı sever,<br><span class="hl">sıcakta tohuma kaçar.</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <rect x="236" y="190" width="440" height="90" rx="16" fill="#5B6B57"/>
 <g fill="#FFF9EE"><circle cx="336" cy="190" r="26"/><circle cx="456" cy="190" r="26"/><circle cx="576" cy="190" r="26"/></g>
 <g fill="#3F7A38"><ellipse cx="306" cy="140" rx="34" ry="52" transform="rotate(-25 306 140)"/><ellipse cx="366" cy="140" rx="34" ry="52" transform="rotate(25 366 140)"/>
 <ellipse cx="426" cy="130" rx="34" ry="56" transform="rotate(-25 426 130)"/><ellipse cx="486" cy="130" rx="34" ry="56" transform="rotate(25 486 130)"/>
 <ellipse cx="546" cy="140" rx="34" ry="52" transform="rotate(-25 546 140)"/><ellipse cx="606" cy="140" rx="34" ry="52" transform="rotate(25 606 140)"/></g>
 <circle cx="780" cy="60" r="44" fill="#CFE3EE"/><text x="780" y="78" font-size="46" text-anchor="middle" font-family="Poppins">❄</text>
</svg></div>"""

i2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NEDEN ŞİMDİ?</span>
<h2>Serin sever</h2>
<p>Ispanak <b>serin mevsim</b> bitkisidir. Sonbahar ve kış, topraksız ıspanak için en rahat dönemdir.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">❄️</div><p style="font-size:30px">Serin havada <b>yaprak</b> yapmaya odaklanır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🔥</div><p style="font-size:30px">Sıcakta tohum <b>zor çimlenir.</b></p></div>
<div class="card" style="padding:22px 32px"><div class="ic">☀️</div><p style="font-size:30px">Uzun gün + sıcak = <span class="hl">tohuma kalkma</span> (sapa kaçma).</p></div></div>"""

i3 = """<div class="pad" style="padding-top:150px">
<span class="tag">HANGİ SİSTEM?</span>
<h2 style="font-size:60px;margin:22px 0 26px">Yapraklılara<br>uyan sistemler</h2>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🫙 Kratky</p><p style="font-size:29px;margin-top:8px">Pompasız, en kolay başlangıç. Balkon ve mutfak için ideal.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🫧 DWC</p><p style="font-size:29px;margin-top:8px">Hava pompasıyla kökler oksijenli suda; <b>hızlı büyüme.</b></p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">〰️ NFT</p><p style="font-size:29px;margin-top:8px">Oluklarda ince çözelti filmi; <span class="hl">çok sayıda bitki</span> için.</p></div></div>"""

i4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ADIM ADIM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Ekimden<br>hasada</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🫘</div><p style="font-size:29px"><b>1.</b> Tohum kabuğu serttir; ekimden önce <b>birkaç saat suda</b> bekletmek çimlenmeye yardım eder.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧊</div><p style="font-size:29px"><b>2.</b> Kaya yünü küpte, <b>serin</b> bir yerde çimlendir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🪴</div><p style="font-size:29px"><b>3.</b> Kök küpten çıkınca küpüyle sisteme aktar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px"><b>4.</b> <b>Dış yapraklardan</b> hasat et; ortadaki büyüme noktasına <span class="hl">dokunma.</span></p></div></div>"""

i5 = """<div class="pad" style="padding-top:150px">
<span class="tag">İPUCU VE HATA</span>
<h2 style="font-size:60px;margin:22px 0 26px">Dikkat<br>et</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🌡️</div><p style="font-size:29px"><b>Ilık çözelti:</b> ıspanak köklerini <b>kök çürümesine</b> açık hale getirir; çözeltiyi serin tut.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌾</div><p style="font-size:29px"><b>Sapa kalktıysa:</b> yapraklar küçülür, tadı acılaşır. Hemen hasat et.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💡</div><p style="font-size:29px"><b>Az ışık:</b> bitki zayıf kalır, yaprakta <b>nitrat birikimi</b> artabilir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🔁</div><p style="font-size:29px"><b>Sürekli hasat için</b> birkaç haftada bir <span class="hl">yeni tohum</span> ek.</p></div></div>"""

i6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">❄️</div><p style="font-size:33px">Ispanak <b>serin mevsim</b> bitkisi.</p></div>
<div class="card"><div class="ic">🫙</div><p style="font-size:33px">Kratky, DWC, NFT <b>uygun.</b></p></div>
<div class="card"><div class="ic">🌡️</div><p style="font-size:33px">Çözeltiyi <b>serin</b> tut.</p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px"><span class="hl">Dış yapraklardan</span> hasat et.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Bu kış ıspanak eker misin?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Bu salatalık<br>arı görmeden<br>meyve verdi!<br>🥒</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Birçok sera salatalığı çeşidi <span class="hl">partenokarpiktir</span>: tozlaşma olmadan meyve bağlar.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🌼</div><p style="font-size:40px"><b>Dişi çiçeği nasıl tanırsın?</b><br><span style="font-size:34px">Bugün 12:30'da anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([s1, s2, s3, s4, s5, s6], "gun16/salatalik")
    render_post([i1, i2, i3, i4, i5, i6], "gun16/ispanak")
    render_story(story, "gun16/hikaye")
