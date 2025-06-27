import re

text="cem dede beyza fıstık"
pattern="cem"

match= re.search(pattern,text) #obje
match= re.findall(pattern,text) #liste
sonuc= match
print(sonuc)