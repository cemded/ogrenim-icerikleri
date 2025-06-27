from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from csv import writer
import time

# ✅ requests yerine selenium başlıyor
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=options)

url = "https://www.btkakademi.gov.tr/portal/catalog?categoryId=353"
driver.get(url)
time.sleep(20)  # Sayfanın yüklenmesini bekle

html = BeautifulSoup(driver.page_source, "html.parser")

kurslar = html.find_all("div", class_="ant-ribbon-wrapper css-tpassh")

# for kurs in kurslar:
#     print(kurs.text.strip())
with open ("kurslar.csv","w",encoding="utf-8") as file :
    csv_writer=writer(file)
    csv_writer.writerow(["link","image","title","seviye","like","ogrenci"])
    for kurs in kurslar:
        anchor = kurs.find("a")
        link = "https://www.btkakademi.gov.tr" + anchor.get("href")
        title=kurs.text.strip()
        seviye=anchor.find(class_="txt-secondary font-medium").string
        image= anchor.img.get("src")
          # ✅ Beğeni sayısı
        like_tag = kurs.select_one("span.absolute.top-\\[20px\\].left-\\[43px\\].font-medium.text-sm")
        like = like_tag.get_text(strip=True) if like_tag else ""

        # ✅ Öğrenci sayısı
        ogrenci_tag = kurs.select_one("span.mr-2.font-medium.text-sm.order-0.mx-1")
        ogrenci = ogrenci_tag.get_text(strip=True) if ogrenci_tag else ""
        csv_writer.writerow([link,image,title,seviye,like,ogrenci])