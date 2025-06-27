import csv
with open ("example.csv") as file :
 csv_reader =csv.DictReader(file)
 #print(list(csv_reader))
 for x in csv_reader:
  print(x["Name"])