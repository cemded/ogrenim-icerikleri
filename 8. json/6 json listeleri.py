import json
kisi_ekle={
    "isim": "beyza",
    "yas": 27,
    "sehir": "istanbul",
    "hobiler": [
        "müzik",
        "yüzme",
        "kodlama"
    ]
}
with open ("4 kisi.json") as file:
    kisiler=json.load(file)
kisiler.append(kisi_ekle)
kisiler.remove(kisiler[0])
with open("4 kisi.json", "w", encoding="utf-8") as dosya:
    json.dump(kisiler, dosya, ensure_ascii=False, indent=4)