-----

# Character Encryption with Python (Python ile Karakter Şifreleme)

-----

## Overview (Genel Bakış)

This Python script implements a simple **substitution cipher** for decrypting text files encoded with numerical keys. It's specifically designed to handle **Turkish characters** and maps numbers (1-31) to the Turkish alphabet.

## Features (Özellikler)

  * **Turkish Alphabet Support (Türk Alfabesi Desteği):** Includes special Turkish characters (Ç, Ğ, İ, Ö, Ş, Ü).
  * **UTF-8 Encoding (UTF-8 Kodlama):** Handles file read/write operations with UTF-8 encoding.
  * **Numeric to Alphabetic Conversion (Sayısal-Alfabetik Dönüşüm):** Transforms numerical keys into corresponding alphabetic characters.
  * **Whitespace & Punctuation Support (Boşluk ve Noktalama Desteği):** Decrypts spaces and periods effectively.

-----

## Requirements (Gereksinimler)

  * **Python 3.x**
  * A text file with appropriate read/write permissions.
  * Input files must be UTF-8 encoded.

-----

## Script Structure (Betik Yapısı)

The core logic revolves around two main lists:

```python
key = ["1" ... "31"]                 # Numerical keys (Sayısal anahtarlar)
alfabe = ['A' ... '.']               # Turkish alphabet + special characters (Türk alfabesi + özel karakterler)
```

-----

## How It Works (Nasıl Çalışır)

1.  The script reads an input file containing numerical values. (Betik, sayısal değerler içeren bir girdi dosyasını okur.)
2.  Each number in the input corresponds to an index within the predefined alphabet array. (Girdideki her sayı, önceden tanımlanmış alfabe dizisindeki bir indekse karşılık gelir.)
3.  The script performs the following operations: (Betik aşağıdaki işlemleri gerçekleştirir:)
      * Reads the input file with UTF-8 encoding. (Girdi dosyasını UTF-8 kodlaması ile okur.)
      * Splits the text based on period characters. (Metni nokta karakterlerine göre böler.)
      * Converts each number to its corresponding letter. (Her sayıyı karşılık gelen harfe dönüştürür.)
      * Writes the decrypted text to an output file. (Şifresi çözülmüş metni çıktı dosyasına yazar.)

-----

## File Paths (Dosya Yolları)

  * **Input (Girdi):** `/Users/Desktop/zehrapythonklasor/zehrapython.txt`
  * **Output (Çıktı):** `/Users/Desktop/zehrapythonklasor/sonuc.txt`

-----

## Usage (Kullanım)

1.  Place your encrypted text file at the specified input path. (Şifrelenmiş metin dosyanızı belirtilen girdi yoluna yerleştirin.)
2.  Run the script: (Betiği çalıştırın:)
    ```bash
    python decrypt.py
    ```
3.  The decrypted text will be written to the output file. (Şifresi çözülmüş metin çıktı dosyasına yazılacaktır.)

-----

## Output Format (Çıktı Formatı)

The script provides two forms of output: (Betik iki çıktı sağlar:)

  * **Console Output (Konsol Çıktısı):** Displays both the encrypted and original text. (Hem şifreli hem de orijinal metni gösteren konsol çıktısı.)
  * **File Output (Dosya Çıktısı):** The decrypted text is written to the specified output file. (Şifresi çözülmüş metin çıktı dosyasına yazılır.)

-----

## Error Handling Considerations (Hata Yönetimi Hususları)

Please ensure the following for smooth operation: (Sorunsuz çalışma için lütfen şunlardan emin olun:)

  * The input file exists and is readable. (Girdi dosyası mevcut ve okunabilir durumda.)
  * Write permissions are available for the output directory. (Çıktı dizinine yazma izni mevcut.)
  * The input text adheres to the expected numerical format. (Girdi metni beklenen sayı formatında.)
  * All numbers in the input correspond to valid alphabet indices. (Girdideki tüm sayılar geçerli alfabe indekslerine karşılık geliyor.)

-----

## Security Considerations (Güvenlik Hususları)

  * This is a **simple substitution cipher** and should **not** be used for securing sensitive data. (Bu basit bir yerine koyma şifrelemesidir ve hassas verileri güvence altına almak için kullanılmamalıdır.)
  * The script assumes trusted input and does not implement input validation. (Betik güvenilir girdi varsayar ve girdi doğrulaması uygulamaz.)
  * File paths are hardcoded and should be modified for production use. (Dosya yolları sabit kodlanmıştır ve üretim kullanımı için değiştirilmelidir.)

-----

## Limitations (Sınırlamalar)

  * Processes only UTF-8 encoded files. (Yalnızca UTF-8 kodlamalı dosyaları işler.)
  * Fixed alphabet mapping (31 characters). (Sabit alfabe eşleştirmesi (31 karakter).)
  * No command-line arguments for file paths. (Dosya yolları için komut satırı argümanları yok.)
  * Lacks robust error management for malformed inputs. (Hatalı girdiler için sağlam hata yönetimi yok.)

-----

## Future Enhancements (Gelecek İyileştirmeler)

  * Add **command-line arguments** for file paths. (Dosya yolları için komut satırı argümanları ekleme.)
  * Implement **input validation**. (Girdi doğrulaması uygulama.)
  * Incorporate **error handling** for file operations. (Dosya işlemleri için hata yönetimi ekleme.)
  * Make alphabet mapping **configurable**. (Alfabe eşleştirmesini yapılandırılabilir hale getirme.)
  * Add support for **different character encodings**. (Farklı karakter kodlamaları için destek ekleme.)

-----

## Author (Yazar)

Zehra Kolsuz
