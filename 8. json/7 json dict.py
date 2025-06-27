data={
    "1":{
        "title":"patates1",
        "price":10
    },
     "2":{
        "title":"patates2",
        "price":20
    }
}

import json

with open("7kisi.json","r",encoding="utf-8") as file:
    kisi=json.load(file)


kisi.update(
    {"1":
     {
        "title":"patates1",
        "price":10
    }

})

#kisi.pop("1")
with open("7kisi.json","w",encoding="utf-8") as file:
    json.dump(kisi,file,ensure_ascii=False,indent=4)
print(kisi["1"])