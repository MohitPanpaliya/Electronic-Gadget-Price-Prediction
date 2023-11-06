import pandas as pd
import requests
from bs4 import BeautifulSoup


Product_name = []
Price = []
Specifications = []
Product_link=[]


for i in range(1,245):
              
              url ="https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

              r = requests.get(url)

              soup = BeautifulSoup(r.text,"lxml")

              data = soup.find_all("div",class_="_2kHMtA")

              for items in data:
                    link = items.find("a", href=True)["href"]
                    Product_link.append("https://www.flipkart.com"+link)



for p_url in Product_link:
            r = requests.get(p_url)
            soup = BeautifulSoup(r.text,"lxml")
            # box = soup.find_all("div",class_="_1YokD2 _3Mn1Gg col-8-12")
            name = soup.find("span",class_="B_NuCI")
            price = soup.find("div",class_="_30jeq3 _16Jk6d")
            specs =soup.find("div",class_="_1UhVsV")
            try:
                  Product_name.append(name.text)
            except AttributeError:
                  Product_name.append("")
            try:
                  Price.append(price.text)
            except AttributeError:
                  Price.append("")
            try:
                  Specifications.append(specs.text)
            except AttributeError:
                  Specifications.append("")

df = pd.DataFrame({"Product Name":Product_name,"Price":Price,"Specifications":Specifications})
df.to_csv("C:/Users/MI/Desktop/Dsci/New_Scraping.csv")