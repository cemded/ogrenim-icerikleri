import requests
import json
response=requests.get("https://jsonplaceholder.typicode.com/posts")

sonuc=response
sonuc=type(response)
sonuc=response.status_code
sonuc=response.headers #headers içi bilgileri verir
sonuc=response.headers["Date"] #spesifik bir bilgi almak için
sonuc=response.url
sonuc=response.encoding
sonuc=response.text
Posts=json.loads(response.text)
sonuc=Posts[0]["title"]
#print(sonuc)
for x in Posts:
    if x["userId"]==1:
        print(x["title"])