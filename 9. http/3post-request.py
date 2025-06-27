import requests

response=requests.post("https://jsonplaceholder.typicode.com/posts",data={
    "userId": 1,
    "title": "yeni başlık",
    "body": "yeni body başlık açıklama"
})
sonuc=response
sonuc=response.text
sonuc=response.json()
sonuc=response.headers
print(sonuc)