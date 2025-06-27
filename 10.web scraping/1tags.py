from bs4 import BeautifulSoup

with open("index.html","r",encoding="utf-8") as file:
    html=file.read()
obj =BeautifulSoup(html,"html.parser")

sonuc=obj
sonuc=type(obj)
sonuc=type(html)

sonuc=obj.prettify()

#sonuc=obj.title
#sonuc=type(obj.title)

#sonuc=obj.title.string
sonuc=obj.body
sonuc=obj.body.h1
#sonuc=obj.h1.string
# sonuc=obj.div
# sonuc=obj.ul
# sonuc=obj.h2
print(sonuc)