## Türkçe Metin Şifre Çözme Aracı

## Genel Bakış
Bu Python betiği, sayısal anahtarlarla kodlanmış metin dosyalarının şifresini çözmek için basit bir yerine koyma şifrelemesi kullanır. Özellikle Türkçe karakterleri işler ve 1-31 arası sayılar ile Türk alfabesi arasında eşleştirme sağlar.

## Özellikler
- Ç, Ğ, İ, Ö, Ş, Ü dahil olmak üzere Türkçe alfabe desteği
- UTF-8 kodlamalı dosya okuma/yazma işlemleri
- Sayısal anahtardan alfabetik karaktere dönüşüm
- Boşluk ve nokta karakterleri desteği

## Gereksinimler
- Python 3.x
- Uygun okuma/yazma izinlerine sahip metin dosyası
- UTF-8 kodlamalı girdi dosyaları

## Betik Yapısı
```python
key = ["1" ... "31"]              # Sayısal anahtarlar
alfabe = ['A' ... '.']            # Türk alfabesi + özel karakterler
```

## Nasıl Çalışır
1. Betik, sayısal değerler içeren bir girdi dosyasını okur
2. Girdideki her sayı, alfabe dizisindeki bir indekse karşılık gelir
3. Betik aşağıdaki işlemleri gerçekleştirir:
   - Girdi dosyasını UTF-8 kodlaması ile okur
   - Metni nokta karakterlerine göre böler
   - Her sayıyı karşılık gelen harfe dönüştürür
   - Şifresi çözülmüş metni çıktı dosyasına yazar

## Dosya Yolları
- Girdi: `/Users/noor/Desktop/zehrapythonklasor/zehrapython.txt`
- Çıktı: `/Users/noor/Desktop/zehrapythonklasor/sonuc.txt`

## Kullanım
1. Şifrelenmiş metin dosyanızı belirtilen girdi yoluna yerleştirin
2. Betiği çalıştırın:
```bash
python decrypt.py
```
3. Şifresi çözülmüş metin çıktı dosyasına yazılacaktır

## Çıktı Formatı
Betik iki çıktı sağlar:
- Hem şifreli hem de orijinal metni gösteren konsol çıktısı
- Çıktı dosyasına yazılan şifresi çözülmüş metin

## Hata Kontrolü
Lütfen şunlardan emin olun:
- Girdi dosyası mevcut ve okunabilir durumda
- Çıktı dizinine yazma izni mevcut
- Girdi metni beklenen sayı formatında
- Girdideki tüm sayılar geçerli alfabe indekslerine karşılık geliyor

## Güvenlik Değerlendirmeleri
- Bu basit bir yerine koyma şifrelemesidir ve hassas verileri güvence altına almak için kullanılmamalıdır
- Betik güvenilir girdi varsayar ve girdi doğrulaması uygulamaz
- Dosya yolları sabit kodlanmıştır ve üretim kullanımı için değiştirilmelidir

## Sınırlamalar
- Yalnızca UTF-8 kodlamalı dosyaları işler
- Sabit alfabe eşleştirmesi (31 karakter)
- Dosya yolları için komut satırı argümanları yok
- Hatalı girdiler için hata yönetimi yok

## Gelecek İyileştirmeler
- Dosya yolları için komut satırı argümanları ekleme
- Girdi doğrulaması uygulama
- Dosya işlemleri için hata yönetimi ekleme
- Alfabe eşleştirmesini yapılandırılabilir hale getirme
- Farklı karakter kodlamaları için destek ekleme

## Lisans
MIT Lisansı

Telif Hakkı (c) 2023 Zehra Kolsuz

Bu yazılımın ve ilişkili belgelendirme dosyalarının ("Yazılım") bir kopyasını alan herhangi bir kişiye, kullanma, kopyalama, değiştirme, birleştirme, yayınlama, dağıtma, alt lisanslama ve/veya yazılımın kopyalarını satma hakları da dahil olmak üzere ve bununla kısıtlama olmaksızın, yazılımı herhangi bir kısıtlama olmaksızın kullanma izni verilir. Yazılımı alan kişiler, yukarıdaki telif hakkı bildirimi ve bu izin bildirimini yazılımın tüm kopyalarına dahil etmelidir.

YAZILIM "HİÇBİR GARANTİ OLMAKSIZIN" VE SATILABİLİRLİK, BELİRLİ BİR AMACA UYGUNLUK VE İHLAL OLMAMASI DA DAHİL OLMAK ÜZERE AÇIK VEYA ZIMNİ HİÇBİR GARANTİ VERİLMEKSİZİN SUNULMUŞTUR. YAZARLAR VEYA TELİF HAKKI SAHİPLERİ HİÇBİR KOŞULDA YAZILIMIN KULLANIMINDAN KAYNAKLANAN SÖZLEŞME, HAKSIZ FİİL VEYA BAŞKA BİR SEBEPLE OLUŞAN HİÇBİR İDDİA, HASAR VEYA DİĞER YÜKÜMLÜLÜKLERDEN SORUMLU DEĞİLDİR.

## Yazar
Zehra Kolsuz
