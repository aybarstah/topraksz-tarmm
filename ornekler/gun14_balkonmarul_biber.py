import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: BALKONDA TOPRAKSIZ MARUL MALİYETİ ----------
m1 = """<div class="pad" style="padding-top:150px">
<span class="tag">BALKONDA MARUL</span>
<h1 style="margin-top:50px">Kaça<br>mal olur?<br>🥬</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Fiyat değişir, kalemler değişmez.<br><span class="hl">Kendi hesabını yap.</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <rect x="60" y="240" width="792" height="20" rx="8" fill="#B59A6E"/>
 <g stroke="#8C7550" stroke-width="8"><line x1="100" y1="240" x2="100" y2="140"/><line x1="812" y1="240" x2="812" y2="140"/><line x1="90" y1="140" x2="822" y2="140"/></g>
 <rect x="250" y="150" width="412" height="88" rx="16" fill="#FFF9EE" stroke="#B59A6E" stroke-width="6"/>
 <g fill="#5E9B4F"><ellipse cx="330" cy="130" rx="60" ry="34"/><ellipse cx="456" cy="125" rx="62" ry="36"/><ellipse cx="582" cy="130" rx="60" ry="34"/></g>
 <g fill="#7DB56A"><ellipse cx="330" cy="112" rx="36" ry="22"/><ellipse cx="456" cy="106" rx="38" ry="24"/><ellipse cx="582" cy="112" rx="36" ry="22"/></g>
 <circle cx="760" cy="60" r="44" fill="#F7D98B"/><text x="760" y="76" font-size="46" font-weight="800" text-anchor="middle" fill="#7A6A52" font-family="Poppins">₺</text>
</svg></div>"""

m2 = """<div class="pad" style="padding-top:150px">
<span class="tag">EN UCUZ YOL</span>
<h2>Kratky ile<br>başla</h2>
<p>Balkon için en düşük maliyetli kurulum: <b>kapaklı, ışık geçirmeyen bir kap + besin çözeltisi.</b></p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🔌</div><p style="font-size:30px"><b>Pompa ve elektrik gerekmez;</b> fatura kalemi sıfır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">♻️</div><p style="font-size:30px">Kap olarak temiz, <b>koyu renkli</b> bir saklama kutusu iş görür.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌞</div><p style="font-size:30px">Güneş ışığı balkonda <span class="hl">bedava</span>; ek lamba şart değil.</p></div></div>"""

m3 = """<div class="pad" style="padding-top:150px">
<span class="tag">BİR KERE ALINIR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Kurulum<br>kalemleri</h2>
<div class="card" style="padding:20px 32px"><div class="ic">📦</div><p style="font-size:29px"><b>Kap:</b> ışık geçirmeyen, kapaklı kutu (yosunu önler).</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🕳️</div><p style="font-size:29px"><b>File saksı:</b> kapağa açılan deliklere oturur.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🟤</div><p style="font-size:29px"><b>Ortam:</b> kaya yünü küp veya hidroton; hidroton <b>tekrar kullanılır.</b></p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📟</div><p style="font-size:29px"><b>EC ve pH ölçer:</b> genelde <span class="hl">en büyük kalem</span>, ama yıllarca kullanılır.</p></div></div>"""

m4 = """<div class="pad" style="padding-top:150px">
<span class="tag">HER SEZON</span>
<h2 style="font-size:60px;margin:22px 0 26px">Sürekli<br>giderler</h2>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🌱 Tohum</p><p style="font-size:29px;margin-top:8px">Bir paket <b>birçok ekime</b> yeter; marul başına maliyeti çok düşüktür.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🧪 Besin (A+B gübre)</p><p style="font-size:29px;margin-top:8px">Konsantre satılır, suyla seyreltilir. Küçük bir şişe <b>bir balkonu uzun süre</b> besler.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">💧 Su</p><p style="font-size:29px;margin-top:8px">Kapalı kapta buharlaşma azdır; <span class="hl">tüketim düşüktür.</span></p></div></div>"""

m5 = """<div class="pad" style="padding-top:150px">
<span class="tag">PARAYI YAKAN HATALAR</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunlara<br>dikkat</h2>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Şeffaf kap:</b> ışık alan çözeltide yosun büyür, çözelti erken çöpe gider.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Hazır set alıp sonra öğrenmek:</b> önce tek kutuyla dene, sonra büyüt.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Göz kararı gübre:</b> fazlası hem para israfı hem <b>kök yakar.</b> Etikete uy.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Tek seferde sökmek:</b> <span class="hl">dış yaprakları</span> kopar, aynı bitkiden tekrar hasat al.</p></div></div>"""

m6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">📦</div><p style="font-size:33px"><b>Koyu kap</b> + file saksı + ortam.</p></div>
<div class="card"><div class="ic">📟</div><p style="font-size:33px">EC/pH ölçer: <b>bir kere</b> alınır.</p></div>
<div class="card"><div class="ic">🔌</div><p style="font-size:33px">Kratky'de <span class="hl">elektrik yok.</span></p></div>
<div class="card"><div class="ic">🧮</div><p style="font-size:33px">Fiyatları yaz, <b>kendin topla.</b></p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sen balkonunda ne yetiştirmek istersin?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: TOPRAKSIZ BİBER ----------
b1 = """<div class="pad" style="padding-top:150px">
<span class="tag">TOPRAKSIZ BİBER</span>
<h1 style="margin-top:50px">Biber<br>neden çiçek<br>döküyor? 🫑</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Sıcak seven bitkinin<br><span class="hl">püf noktaları.</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <path d="M456 290 L456 60" stroke="#3C6E3A" stroke-width="12"/>
 <path d="M456 150 Q360 120 300 70" stroke="#3C6E3A" stroke-width="9" fill="none"/>
 <path d="M456 120 Q560 90 620 40" stroke="#3C6E3A" stroke-width="9" fill="none"/>
 <g fill="#5E9B4F"><ellipse cx="290" cy="60" rx="50" ry="24"/><ellipse cx="630" cy="32" rx="50" ry="24"/><ellipse cx="456" cy="50" rx="30" ry="46"/></g>
 <path d="M300 90 C270 150 290 230 330 240 C370 230 380 150 350 92 Z" fill="#D9483B"/>
 <path d="M600 70 C570 130 585 200 620 210 C655 200 668 130 640 72 Z" fill="#E8A43A"/>
 <g fill="#FFFFFF"><circle cx="520" cy="190" r="16"/><circle cx="400" cy="210" r="14"/></g>
 <rect x="356" y="270" width="200" height="24" rx="10" fill="#B59A6E"/>
</svg></div>"""

b2 = """<div class="pad" style="padding-top:150px">
<span class="tag">TEMEL BİLGİ</span>
<h2>Sıcağı ve<br>ışığı sever</h2>
<p>Biber, domates gibi <b>ılık ve aydınlık</b> ortam isteyen bir yaz sebzesidir; marul gibi serin seven yeşilliklerden farklıdır.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🌡️</div><p style="font-size:30px">Soğuk gecelerde <b>büyüme yavaşlar</b>, meyve tutumu zayıflar.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">💡</div><p style="font-size:30px">Az ışıkta bitki uzar, <b>az çiçek</b> verir.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌼</div><p style="font-size:30px">Çiçekleri <span class="hl">kendi kendini tozlar;</span> hafif sallamak yardımcı olur.</p></div></div>"""

b3 = """<div class="pad" style="padding-top:150px">
<span class="tag">KURULUM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Hangi<br>sistem?</h2>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">💧 Damla + cocopeat / kaya yünü</p><p style="font-size:29px;margin-top:8px">Büyük biber çeşitleri için en yaygın yöntem. Kök hacmi geniş, <b>bitki sağlam durur.</b></p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🫧 DWC (derin su kültürü)</p><p style="font-size:29px;margin-top:8px">Evde küçük ve acı biber çeşitleri için uygundur; çözeltinin <b>havalandırılması</b> şart.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🪢 Destek</p><p style="font-size:29px;margin-top:8px">Meyve yüklü dallar kırılabilir; <span class="hl">çubuk veya iple</span> destekle.</p></div></div>"""

b4 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÇİÇEK DÖKÜMÜ</span>
<h2 style="font-size:60px;margin:22px 0 26px">En sık<br>sebepler</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🔥</div><p style="font-size:29px"><b>Aşırı sıcak veya soğuk:</b> uç sıcaklıklarda çiçekler tozlaşmadan dökülür.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🌥️</div><p style="font-size:29px"><b>Yetersiz ışık:</b> bitki tüm çiçekleri besleyemez, bir kısmını bırakır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💦</div><p style="font-size:29px"><b>Düzensiz sulama:</b> ortamın bir kuruyup bir ıslanması bitkiyi strese sokar.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🍂</div><p style="font-size:29px"><b>Aşırı meyve yükü:</b> bitki <span class="hl">taşıyabileceğinden fazlasını</span> kendisi döker.</p></div></div>"""

b5 = """<div class="pad" style="padding-top:150px">
<span class="tag">İPUCU VE HATA</span>
<h2 style="font-size:60px;margin:22px 0 26px">Bunları<br>bil</h2>
<div class="card" style="padding:20px 32px"><div class="ic">✂️</div><p style="font-size:29px"><b>İlk çiçek:</b> genç bitkide ilk çiçeği koparmak, enerjiyi <b>gövde ve köke</b> yönlendirir.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">⚫</div><p style="font-size:29px"><b>Dipte kararma:</b> çiçek burnu çürüklüğü biberde de görülür; sulamayı <span class="hl">düzenli</span> tut.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🟢</div><p style="font-size:29px"><b>Renk:</b> kırmızı ve sarı biberler genelde önce yeşildir; dalda beklerse renk döner.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Yolarak koparmak:</b> dal kırılır; meyveyi <b>makasla</b> kes.</p></div></div>"""

b6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🌡️</div><p style="font-size:33px">Biber <b>ılık ve aydınlık</b> ister.</p></div>
<div class="card"><div class="ic">💧</div><p style="font-size:33px">Sulamada <b>düzen</b> esastır.</p></div>
<div class="card"><div class="ic">🪢</div><p style="font-size:33px">Dalları <b>destekle.</b></p></div>
<div class="card"><div class="ic">✂️</div><p style="font-size:33px">Meyveyi <span class="hl">makasla</span> kes.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Senin biberin hiç çiçek döktü mü?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:92px">Balkonda<br>marul için<br>pompa da<br>elektrik de<br>şart değil! 🥬</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Kratky yönteminde bitki, kapaklı bir kaptaki <span class="hl">besin çözeltisinden</span> kendi suyunu çeker.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">🧮</div><p style="font-size:40px"><b>Peki kaça mal olur?</b><br><span style="font-size:34px">Bugün 12:30'da kalem kalem anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([m1, m2, m3, m4, m5, m6], "gun14/balkonmarul")
    render_post([b1, b2, b3, b4, b5, b6], "gun14/biber")
    render_story(story, "gun14/hikaye")
