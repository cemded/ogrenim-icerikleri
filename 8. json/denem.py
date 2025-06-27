import json
with open("4 kisi.json", "r", encoding="utf-8") as dosya:
    yeni_kisi = json.load(dosya)
#kisi=yeni_kisi["kisi"] 
print(yeni_kisi[0]["sehir"])