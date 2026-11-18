import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sablon.base import render_post, render_story

# ---------- GÖNDERİ 1: TÜRKİYE'DE TOPRAKSIZ TARIM / SERA TEŞVİKLERİ ----------
t1 = """<div class="pad" style="padding-top:150px">
<span class="tag">DEVLET DESTEĞİ</span>
<h1 style="margin-top:50px">Sera<br>kuracaklara<br>hibe var mı?</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">Türkiye'deki ana program,<br><span class="hl">şartlarıyla birlikte.</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <rect x="60" y="250" width="792" height="18" rx="8" fill="#B59A6E"/>
 <path d="M150 250 L150 140 Q300 40 450 140 L450 250 Z" fill="#FFF9EE" stroke="#3C6E3A" stroke-width="8"/>
 <path d="M450 250 L450 140 Q600 40 750 140 L750 250 Z" fill="#FFF9EE" stroke="#3C6E3A" stroke-width="8"/>
 <g stroke="#3C6E3A" stroke-width="5"><line x1="300" y1="72" x2="300" y2="250"/><line x1="600" y1="72" x2="600" y2="250"/></g>
 <g fill="#5E9B4F"><ellipse cx="225" cy="225" rx="40" ry="22"/><ellipse cx="375" cy="225" rx="40" ry="22"/><ellipse cx="525" cy="225" rx="40" ry="22"/><ellipse cx="675" cy="225" rx="40" ry="22"/></g>
 <circle cx="820" cy="60" r="48" fill="#F7D98B"/><text x="820" y="78" font-size="50" font-weight="800" text-anchor="middle" fill="#7A6A52" font-family="Poppins">%</text>
</svg></div>"""

t2 = """<div class="pad" style="padding-top:150px">
<span class="tag">ANA PROGRAM</span>
<h2 style="font-size:60px">Kırsal Kalkınma<br>Yatırım Programı</h2>
<p style="font-size:33px">Tarım ve Orman Bakanlığı'nın hibe programı. <b>Kapalı ortamda bitkisel üretim</b> yatırımları (modern sera dahil) destek konuları arasında.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">💰</div><p style="font-size:30px">2026 çağrısında hibe: proje tutarının <span class="hl">%50–70'i</span> (KDV dahil).</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🤖</div><p style="font-size:30px"><b>Otomasyon, sensör, akıllı tarım</b> uygulamaları da kapsamda.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🏡</div><p style="font-size:30px">Yatırım <b>kırsal alanda</b> olmalı.</p></div></div>"""

t3 = """<div class="pad" style="padding-top:150px">
<span class="tag">2026 ŞARTLARI</span>
<h2 style="font-size:60px;margin:22px 0 26px">Kimler<br>başvurabilir?</h2>
<div class="card" style="padding:20px 32px"><div class="ic">👤</div><p style="font-size:29px"><b>Gerçek kişiler</b> ve şirketler, tarımsal örgütler.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">👩‍🌾</div><p style="font-size:29px"><b>Genç, kadın girişimci</b> ve aile işletmelerine bütçeden pay ayrılıyor.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📄</div><p style="font-size:29px">Kiralık arazi olur; kira <b>en az 7 yıl</b> sürmeli.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🚫</div><p style="font-size:29px">Vadesi geçmiş <b>vergi/SGK borcu</b> engel. Kişi başı <span class="hl">tek proje.</span></p></div></div>"""

t4 = """<div class="pad" style="padding-top:150px">
<span class="tag">TAKVİM</span>
<h2 style="font-size:60px;margin:22px 0 26px">2026 başvurusu<br>kapandı</h2>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">📅 2026 dönemi</p><p style="font-size:29px;margin-top:8px">Başvurular <b>Nisan–Temmuz 2026</b> arasında alındı, sonuçlar Eylül'de açıklandı.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">📢 Yeni dönem</p><p style="font-size:29px;margin-top:8px">Her çağrı <b>tebliğle</b> duyurulur; oranlar ve şartlar değişebilir.</p></div>
<div class="card" style="display:block;padding:24px 34px"><p style="font-size:33px;font-weight:800;color:#2F5D2D">🔎 Nereden takip?</p><p style="font-size:29px;margin-top:8px"><b>tarimorman.gov.tr</b> ve <span class="hl">il/ilçe tarım müdürlüğü.</span></p></div></div>"""

t5 = """<div class="pad" style="padding-top:150px">
<span class="tag">BİLMEN GEREKENLER</span>
<h2 style="font-size:60px;margin:22px 0 26px">Sürpriz<br>yaşama</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🧾</div><p style="font-size:29px"><b>Hibe, gerçekleşen harcamaya göre</b> belirlenir; bütçeni buna göre planla.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📏</div><p style="font-size:29px">2026'da <b>100 bin TL altı</b> projeler kabul edilmedi; balkon kurulumu kapsam dışı.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">⚖️</div><p style="font-size:29px">Aynı proje için <b>başka bir kamu desteği</b> alınamaz.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💧</div><p style="font-size:29px">Damla sulama gibi <span class="hl">tasarruflu sulama</span> için ayrı hibe programı var.</p></div></div>"""

t6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🏛️</div><p style="font-size:33px"><b>Kırsal Kalkınma</b> hibesi seraları kapsıyor.</p></div>
<div class="card"><div class="ic">💰</div><p style="font-size:33px">2026'da oran <b>%50–70</b> idi.</p></div>
<div class="card"><div class="ic">📅</div><p style="font-size:33px">2026 başvurusu <b>kapandı.</b></p></div>
<div class="card"><div class="ic">📢</div><p style="font-size:33px">Yeni çağrıyı <span class="hl">şimdiden</span> takip et.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Sera kurmayı düşünüyor musun?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- GÖNDERİ 2: FİTİL (WICK) SİSTEMİ ----------
f1 = """<div class="pad" style="padding-top:150px">
<span class="tag">FİTİL SİSTEMİ</span>
<h1 style="margin-top:50px">Bitkiyi<br>bir ip<br>sulasın 🧵</h1>
<p style="font-size:44px;margin-top:40px;font-weight:600">En basit topraksız sistem:<br><span class="hl">pompa yok, hareket yok.</span></p>
<svg width="912" height="300" viewBox="0 0 912 300" style="position:absolute;bottom:115px;left:84px">
 <rect x="296" y="170" width="320" height="120" rx="14" fill="#5B6B57"/>
 <rect x="306" y="200" width="300" height="80" rx="10" fill="#8FC1D9"/>
 <path d="M326 70 L586 70 L566 170 L346 170 Z" fill="#FFF9EE" stroke="#B59A6E" stroke-width="6"/>
 <path d="M456 150 Q440 200 470 260" stroke="#E8A43A" stroke-width="10" fill="none" stroke-linecap="round"/>
 <path d="M456 70 L456 20" stroke="#3C6E3A" stroke-width="9"/>
 <g fill="#5E9B4F"><ellipse cx="420" cy="26" rx="40" ry="20"/><ellipse cx="492" cy="20" rx="40" ry="20"/></g>
</svg></div>"""

f2 = """<div class="pad" style="padding-top:150px">
<span class="tag">NASIL ÇALIŞIR?</span>
<h2>Kılcal<br>hareket</h2>
<p>Fitil, alttaki haznedeki <b>besin çözeltisini</b> kılcal hareketle yukarıdaki ortama taşır. Tıpkı gaz lambasının fitili gibi.</p>
<div class="card" style="margin-top:30px;padding:22px 32px"><div class="ic">🔌</div><p style="font-size:30px"><b>Pasif sistem:</b> pompa, elektrik, zamanlayıcı yok.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">🌱</div><p style="font-size:30px">Kökler suya değil, <b>nemli ortama</b> uzanır.</p></div>
<div class="card" style="padding:22px 32px"><div class="ic">⚖️</div><p style="font-size:30px">Ortam kurudukça fitil <span class="hl">yeniden çeker.</span></p></div></div>"""

f3 = """<div class="pad" style="padding-top:150px">
<span class="tag">ŞEMA</span>
<h2 style="font-size:60px;margin:22px 0 20px">İki kap,<br>bir fitil</h2>
<svg width="912" height="760" viewBox="0 0 912 760">
 <rect x="226" y="420" width="460" height="300" rx="24" fill="#5B6B57"/>
 <rect x="244" y="500" width="424" height="200" rx="16" fill="#8FC1D9"/>
 <path d="M256 170 L656 170 L626 420 L286 420 Z" fill="#E9DCC4" stroke="#B59A6E" stroke-width="8"/>
 <g fill="#FFF9EE"><circle cx="330" cy="240" r="9"/><circle cx="400" cy="300" r="9"/><circle cx="520" cy="250" r="9"/><circle cx="580" cy="320" r="9"/><circle cx="460" cy="370" r="9"/><circle cx="360" cy="380" r="9"/></g>
 <path d="M420 260 Q400 400 430 470 Q450 560 410 670" stroke="#E8A43A" stroke-width="14" fill="none" stroke-linecap="round"/>
 <path d="M500 260 Q520 400 490 470 Q470 560 510 670" stroke="#E8A43A" stroke-width="14" fill="none" stroke-linecap="round"/>
 <path d="M456 170 L456 70" stroke="#3C6E3A" stroke-width="12"/>
 <g fill="#5E9B4F"><ellipse cx="400" cy="80" rx="62" ry="28"/><ellipse cx="512" cy="70" rx="62" ry="28"/><ellipse cx="456" cy="40" rx="30" ry="40"/></g>
 <g font-family="Poppins" font-size="30" font-weight="700" fill="#2E3B2A">
  <text x="680" y="250">Ortam</text><text x="680" y="285" font-size="24" font-weight="600" fill="#7A6A52">perlit/cocopeat</text>
  <text x="40" y="470">Fitil</text>
  <text x="700" y="600">Hazne</text><text x="700" y="635" font-size="24" font-weight="600" fill="#7A6A52">çözelti</text>
 </g>
 <g stroke="#7A6A52" stroke-width="4"><line x1="110" y1="460" x2="400" y2="460"/><line x1="676" y1="260" x2="600" y2="260"/><line x1="696" y1="590" x2="640" y2="590"/></g>
</svg></div>"""

f4 = """<div class="pad" style="padding-top:150px">
<span class="tag">KURULUM</span>
<h2 style="font-size:60px;margin:22px 0 26px">Doğru<br>malzeme</h2>
<div class="card" style="padding:20px 32px"><div class="ic">🧵</div><p style="font-size:29px"><b>Fitil:</b> emici ve çürümeyen; akrilik ip ya da keçe şerit. Pamuk iyi emer ama <b>zamanla çürüyebilir.</b></p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🟤</div><p style="font-size:29px"><b>Ortam:</b> perlit, vermikülit, cocopeat suyu iyi taşır. <b>Hidroton</b> fitille iyi çalışmaz.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📏</div><p style="font-size:29px"><b>Mesafe:</b> ortam ile çözelti arası kısa olsun; fitil yolu uzadıkça su azalır.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">📦</div><p style="font-size:29px"><b>Hazne:</b> <span class="hl">ışık geçirmez</span> olsun, yoksa yosun büyür.</p></div></div>"""

f5 = """<div class="pad" style="padding-top:150px">
<span class="tag">İPUCU VE HATA</span>
<h2 style="font-size:60px;margin:22px 0 26px">Neye<br>uygun?</h2>
<div class="card" style="padding:20px 32px"><div class="ic">✅</div><p style="font-size:29px"><b>Küçük bitkiler:</b> fesleğen, nane, maydanoz, marul gibi az su isteyenler.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">❌</div><p style="font-size:29px"><b>Büyük meyveli bitkiler:</b> domates, biber gibi çok su içenlere fitil <b>yetişmez.</b></p></div>
<div class="card" style="padding:20px 32px"><div class="ic">🧂</div><p style="font-size:29px"><b>Tuz birikimi:</b> ortamı arada <b>sade suyla</b> yıka, beyaz kabuğu önle.</p></div>
<div class="card" style="padding:20px 32px"><div class="ic">💦</div><p style="font-size:29px"><b>Hazneyi kurutma:</b> fitil kuruyunca zor ıslanır; <span class="hl">seviyeyi</span> takip et.</p></div></div>"""

f6 = """<div class="pad" style="padding-top:150px">
<span class="tag">ÖZET</span>
<h2>Kısacası…</h2>
<div class="card"><div class="ic">🧵</div><p style="font-size:33px">Fitil suyu <b>kılcal hareketle</b> taşır.</p></div>
<div class="card"><div class="ic">🟤</div><p style="font-size:33px">Ortam: <b>perlit, cocopeat.</b></p></div>
<div class="card"><div class="ic">🌿</div><p style="font-size:33px">Küçük yeşillikler için <b>ideal.</b></p></div>
<div class="card"><div class="ic">🧂</div><p style="font-size:33px">Arada <span class="hl">sade suyla</span> yıka.</p></div>
<p style="margin-top:40px;font-size:38px;font-weight:700;color:#2F5D2D">Fitil sistemini denedin mi?<br>Yorumlara yaz, bu kartı kaydet 🔖</p></div>"""

# ---------- HİKÂYE ----------
story = """<div class="pad">
<span class="tag">BİLİYOR MUYDUN?</span>
<h1 style="margin-top:60px;font-size:88px">Sera<br>yatırımına<br>devlet hibesi<br>var! 🏛️</h1>
<p style="font-size:44px;margin-top:60px;line-height:1.45">Kırsal Kalkınma programının 2026 çağrısında hibe oranı proje tutarının <span class="hl">%50–70'i</span> oldu.</p>
<div class="card" style="margin-top:70px;padding:40px 44px"><div class="ic">📋</div><p style="font-size:40px"><b>Kimler başvurabilir?</b><br><span style="font-size:34px">Bugün 12:30'da şartlarıyla anlatıyoruz.</span></p></div>
</div>"""

if __name__ == "__main__":
    render_post([t1, t2, t3, t4, t5, t6], "gun15/tesvik")
    render_post([f1, f2, f3, f4, f5, f6], "gun15/fitil")
    render_story(story, "gun15/hikaye")
