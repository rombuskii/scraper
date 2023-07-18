from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.parse

products=[] #List to store name of the product
prices=[] #List prices 

#Takes input
inp = input("Search: ")
res = urllib.parse.quote(inp)
url = f"https://www.newegg.com/p/pl?d={res}"

#Gets search result
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")
#Gets details
for div in doc.find_all('div', class_='item-container'):
    info = div.find("div", class_="item-info")
    action = div.find("div", class_="item-action")
    try:
        name = info.find("a", class_='item-title').text
        temp = action.find("li", class_="price-current")
        price = temp.find("strong").text
        price = int(price.replace(',', ''))
        products.append(name)
        prices.append(price)
    except:
        continue

df = pd.DataFrame({"name": products, "price": prices})
avg = df['price'].mean()
df = df[(df.price < avg + (0.2 * avg)) & (df.price > avg - (0.2 * avg))]
df.to_csv('products.csv', index=False, encoding='utf-8')
#print(avg)
print("Done")