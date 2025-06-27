from bs4 import BeautifulSoup

with open("index.html","r",encoding="utf-8") as file:
    html=file.read()

obj=BeautifulSoup(html,"html.parser")

sonuc=obj.div
sonuc=obj.find("div")
sonuc=obj.find_all("div")
sonuc=len(obj.find_all("div"))
sonuc=obj.find_all("div")[1]
sonuc=obj.find_all("div")[1].h2
sonuc=obj.find_all("div")[1].ul
sonuc=obj.find_all("div")[1].ul.find_all("li")[0]

sonuc=obj.find_all("div")

# for div in obj.find_all("div"):
#     print(div.text)

# for div in obj.find_all("div"):
#     print(div.h2)
#print(sonuc)

# for a in obj.find_all("a"):
#     print(a)

for div in obj.find_all("div"):
     if div.h2.a != None:
      print(div.h2.a.string.strip())
     else:
        print(div.h2.string.strip())

for div in obj.find_all("div"):
   print(div.h2.text)