import json

# 1. Python'da bir dict (sözlük) oluşturalım
kisi = {
    "isim": "Cem",
    "yas": 25,
    "sehir": "Ankara",
    "hobiler": ["müzik", "yüzme", "kodlama"]
}

kisiler=[kisi]

# 2. Serileştirip dosyaya yaz (kisi.json adında)
with open("4 kisi.json", "w", encoding="utf-8") as dosya:
    json.dump(kisiler, dosya, ensure_ascii=False, indent=4)

# print("✅ JSON dosyaya yazıldı.")

# 3. Dosyadan geri okuyup deserileştirelim
with open("4 kisi.json", "r", encoding="utf-8") as dosya:
    yeni_kisi = json.load(dosya)
# yeni_kisi["yas"]=30
# anlık güncelleme resette kaybolur
# with open("4 kisi.json", "w", encoding="utf-8") as dosya:
#     json.dump(yeni_kisi, dosya, ensure_ascii=False, indent=4)

print("✅ JSON dosyaya yazıldı.")
# 4. Şimdi geri okuduğumuz veriyi kullanalım
print("🔁 JSON dosyadan okundu:")
print("İsim:", yeni_kisi[0]["isim"])
print("Şehir:", yeni_kisi[0]["sehir"])
print("Hobiler:", ", ".join(yeni_kisi[0]["hobiler"]))
