import csv

with open("arabalar_copy.csv","w",newline="") as file:
    basliklar=["Marka","Model","Fiyat"]
    csv_writer=csv.DictWriter(file,basliklar)
    csv_writer.writeheader()
    csv_writer.writerow({
         "Marka": "arabax",
         "Model": "patates",
         "Fiyat": 5000
         })