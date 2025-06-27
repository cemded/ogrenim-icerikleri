urun=[{"title":"samsung 23","price":7000},
      {"title":"samsung 24","price":8000},
      {"title":"samsung 25","price":9000}]
enucuz=min(urun,key=lambda x:x["price"])
sonuc=f"{enucuz["title"]},{enucuz["price"]}"
print(sonuc)