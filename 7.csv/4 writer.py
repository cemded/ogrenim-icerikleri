import csv
data=[["Marka","Model","Fiyat"],["Toyota","Corolla",10000],["Mazda","Cx-5",20000]]

with open("arabalar.csv","w",newline="") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)
with open("arabalar.csv","a",newline="") as file: # "a" ekleme yapar
    csv_writer=csv.writer(file)
    csv_writer.writerow(["Opel","Astra",15000])

# import csv
# import os

# filename = "arabalar.csv"
# data = [["Marka", "Model"], ["Toyota", "Corolla"], ["Mazda", "Cx-5"]]

# Eğer dosya yoksa oluştur ve başlıkları + veriyi yaz
# if not os.path.exists(filename):
#     with open(filename, "w", newline="") as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerows(data)
#     print("Dosya oluşturuldu.")
# else:
#     print("Dosya zaten var, sadece ekleme yapılacak.")

# # Dosyaya yeni satır ekle
# with open(filename, "a", newline="") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Opel", "Astra"])
#     print("Yeni satır eklendi.")
with open("arabalar.csv","r+",newline="") as file:
    csv_reader=csv.reader(file)
    csv_writer=csv.writer(file)
    next(csv_reader)
    urunler=[[x[0],x[1],float(x[2])*1.3] for x in csv_reader]
    file.seek(0)

    csv_writer.writerow(["Marka","Model","Fiyat"])
    csv_writer.writerows(urunler)