import json

veri = {"isim": "Cem", "yas": 25}

# JSON string'e çeviriyoruz (serileştirme)
json_string = json.dumps(veri)

print(json_string)  # Çıktı: {"isim": "Cem", "yas": 25}
print(veri["isim"])
print(type(json_string))


# import json

# # Python objesi
# kisi = {"isim": "Cem", "yas": 25}

# # Serileştirme (JSON'a dönüştür)
# json_veri = json.dumps(kisi)

# # Deserileştirme (JSON'dan geri dön)
# geri_donus = json.loads(json_veri)

# print(geri_donus["isim"])  # Çıktı: Cem
