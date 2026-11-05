# Günlük içerik görevi – @topraksz_tarmm

Her gün: **2 karusel gönderi + 1 hikâye**, Metricool'da zamanlanır.
- Metricool brand (blogId): **7895249** (topraksz_tarmm), saat dilimi Europe/Istanbul
- Hikâye **10:00**, 1. gönderi **12:30**, 2. gönderi **20:00**

## Adımlar
1. `KONULAR.md`yi oku; daha önce işlenmemiş 2 konu seç (birini "sıradaki fikirler"den).
2. `ornekler/` içindeki kart HTML'lerini örnek al; aynı bej-yeşil tarz, TAMAMEN Türkçe, büyük okunaklı başlık.
   Her gönderi 5-6 kart: kapak (merak uyandıran başlık), açıklama, şema/görsel, liste/adımlar, ipucu/hata, kapanış ("kaydet").
   Bilgiler doğru olmalı; emin olmadığın sayı verme.
3. `sablon/base.py` ile üret: `render_post(cards, "gunN/konu1")`, `render_post(..., "gunN/konu2")`, `render_story(html, "gunN/hikaye")`.
   Hikâye: o günün 1. gönderisinden tek çarpıcı bilgi/soru, 1080x1920.
4. Görsellere bak (birleşik küçük önizleme), taşma/kesilme varsa düzelt.
5. Commit + push (git user: Claude <noreply@anthropic.com>). Görsel URL'si:
   `https://raw.githubusercontent.com/aybarstah/topraksz-tarmm/main/<yol>.jpg` — push sonrası 200 döndüğünü kontrol et.
6. Metricool'da zamanla (autoPublish true, draft false, isAiGenerated false):
   - Hikâye: instagramData.type "STORY", text boş, tek görsel.
   - Gönderiler: type "POST", 5-6 görsel, Türkçe açıklama (soru + "kaydet" çağrısı + 12-15 hashtag).
7. `KONULAR.md`ye tarih + konuları ekle, commit + push.
8. Aybars'a kısa özet gönder (konular, saatler, Metricool linkleri).
