from bs4 import BeautifulSoup

with open("index.html","r",encoding="utf-8") as file:
    html=file.read()

obj=BeautifulSoup(html,"html.parser")

sonuc=obj.body.div.contents[3]

sonuc=obj.body.div.children
#print(sonuc)

# for x in obj.body.div.children:
#     print(x)

# for x in obj.body.div.descendants:
#     print(x)

sonuc=obj.body.h2.parent
sonuc=obj.body.h2.parent.parent
sonuc=obj.body.ul.next_element.next_element

sonuc=obj.body.div.next_sibling.next_sibling

sonuc=obj.body.div.find_next_sibling("div").find_previous_sibling("div")

print(sonuc)