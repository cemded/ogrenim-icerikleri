data={
    "kullanici":{
    "cem dede":
    {
    "ad":"cem",
    "soyad":"dede"
    }
    },
    "products":{
    "1":{
        "title":"patates1",
        "price":10
    },
     "2":{
        "title":"patates2",
        "price":20
    }
}
}
import json



with open("7kisi.json","r",encoding="utf-8") as file:
    data=json.load(file)


# data.update(
#     {"1":
#      {
#         "title":"patates1",
#         "price":10
#     }

# })

#data.pop("1")
print(data["kullanici"]["cem dede"])
print(data["products"]["2"]["title"])

data["kullanici"].update({"beyza benzer":
                          {
                              "ad":"beyza",
                              "soyad":"benzer"
                          }})
with open("7kisi.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=4)