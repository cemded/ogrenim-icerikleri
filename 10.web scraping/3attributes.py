from bs4 import BeautifulSoup

with open("index.html","r",encoding="utf-8") as file:
    html=file.read()

obj=BeautifulSoup(html,"html.parser")

sonuc=obj.find_all("div")

# sonuc=obj.find_all(id="item1")
# print(sonuc)

# for div in obj.find_all(id="item1"):
#     print(div.text)


sonuc=obj.find_all(class_="item")
sonuc=obj.find_all(class_="item")[1]

sonuc=obj.select("#header")  # #işareti id anlamına geliyor
sonuc=obj.select("#item1")
sonuc=obj.select(".item")  # . işareti class anlamına geliyor

sonuc=obj.select_one(".item") #bulduğu ilk kayıt


sonuc=obj.div.attrs["id"]

sonuc=obj.ul.get_text()
sonuc=obj.div.get_text()
#print(sonuc)

for a in obj.find_all("a"):
    #print(a.get("href"))
    print(a["href"])
