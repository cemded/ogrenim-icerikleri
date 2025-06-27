import json
with open("1 produst.json") as file:
    data=json.load(file)
products=data["products"]
print(data)
print(type(data))
print(products[0]["title"])

# import json

# json_str = '{"isim": "cem", "yas": 25}'
# data = json.loads(json_str)

# print(data["isim"])  # cem
