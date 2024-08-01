#import packages

import requests, csv
from bs4 import BeautifulSoup

#Target Website

url = "https://www.flipkart.com/search?q=Mobiles"
start_link = "https://www.flip.in/"

#Content Extraction


contents = BeautifulSoup(requests.get(url).text, "html.parser")

classes = contents.find("html").find_all("div")
a = []
for g in classes:
    if g.has_attr("class"):
        a.append(g.get("class"))
m = []
nm =[]
for g in a:
    m.append(contents.find("div",class_=g).find_all("div",class_=g))
for model in m:
    nm = model.find("div",class_="KzDlHZ").text
print(nm)