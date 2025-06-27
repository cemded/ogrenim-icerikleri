import csv

with open("example.csv") as file:
    csv_reader = csv.reader(file)
    print(csv_reader)
    #liste=list(csv_reader)
    #print(liste[1])
    #next(csv_reader)
    for x in csv_reader:
        print(x[1])
    #     if x[3] == "True":
 