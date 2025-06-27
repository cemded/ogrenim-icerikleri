class product:
    def __init__(self,id,title,price):
        self.id=id
        self.title=title
        self.price=price
#serialize
# p1=product(1,"lexa",1000)
# p2=product(2,"ace",2000)
# p3=product(3,"alice",3000)

# #products=[p1.__dict__,p2.__dict__,p3.__dict__] #liste halinde yazmak için

# products= {
#     p1.id:p1.__dict__,
#     p2.id:p2.__dict__,
#     p3.id:p3.__dict__} #dict şeklinde yazmak için
# import json

# with open("9product.json","w",encoding="utf-8") as file:
#     json.dump(products,file,ensure_ascii=False,indent=4)


#deserialize

import json

with open("9product.json","r",encoding="utf-8") as file:
    data=json.load(file)
print(data)
print(type(data))
products=[]
for key,value in data.items():
    products.append(product(key,value["title"],value["price"]))
print(type(products))
for x in products:
    print(x.title)
    print(x.id)
    print(x.price)
