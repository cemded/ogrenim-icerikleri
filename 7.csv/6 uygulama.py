import csv

with open("onlinefoods.csv") as file:
    csv_reader=csv.reader(file)
    liste=list(csv_reader)
    print(len(liste)-1)

with open("onlinefoods.csv") as file:
    csv_reader=csv.DictReader(file)
    count=len([x for x in csv_reader if x["Occupation"]=="Student"])
    print(count)

with open("onlinefoods.csv") as file:
    csv_reader=csv.DictReader(file)
    count=[x for x in csv_reader if int(x["Age"])>=20 and int(x["Age"])<=30]
    for i in count:
        print(i["latitude"],i["longitude"])
    print(len(count))

    # count=sum(1 for x in csv_reader if int(x["Age"])>=20 and int(x["Age"])<=30)
    # print(count) sadece sayı için iyi az hafıza harcar