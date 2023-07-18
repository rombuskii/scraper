#New Egg Pricing Software
from bs4 import BeautifulSoup
import requests
import pandas as pd

def getItems(item):
    products=[] #List to store name of the product
    prices=[] #List prices 
    parsed = item.split()
    parsed = "+".join(parsed)
    url = f"https://www.newegg.com/p/pl?d={parsed}"
    
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

        df = pd.DataFrame({"Name": products, "Price": prices})
        avg = df['Price'].mean().__round__(2)
        entry = ['Average', avg]
        df.loc[len(df)] = entry
        df = df[(df.Price < avg + (0.2 * avg)) & (df.Price > avg - (0.2 * avg))]
        df.to_csv('products.csv', index=False, encoding='utf-8')

