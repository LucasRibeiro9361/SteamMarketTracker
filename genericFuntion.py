from bs4 import BeautifulSoup
import requests

def exchange( itemValue ):
    itemValue = itemValue[1:-4]
    itemValue = float(itemValue)
    url = "https://www.dolarhoje.net.br"
    link = requests.get(url)
    mainpage = BeautifulSoup(link.text, features="html.parser")
    item = mainpage.find("input", {"id": "moeda"})
    dolarToday = item["value"]
    dolarToday = dolarToday.replace(",", ".")
    dolarToday = float(dolarToday)
    dolarToday = "%.2f" % dolarToday
    dolarToday = float(dolarToday)
    itemValue = itemValue * dolarToday
    itemValue = "%.2f" % itemValue
    itemValue = float(itemValue)

    return itemValue

def queryItem( itemName ):
    itemName = itemName.replace(' ', '+')
    print(itemName)
    url = f'https://steamcommunity.com/market/search?q={itemName}'
    link = requests.get(url)
    mainpage = BeautifulSoup(link.text, features="html.parser")
    container = mainpage.find("div", {"id": "searchResultsRows"})
    itemContainer = container.find("a", {"class": "market_listing_row_link"})
    normal_price = exchange( itemContainer.find("span", attrs={'data-price': True}).text )
    sale_price = exchange(itemContainer.find("span", {"class": "sale_price"}).text)
    itemPair = (normal_price, sale_price)
    return itemPair

def priceDifference(pricePaid,priceNow):
    resultPercentage = (priceNow * 100) / pricePaid
    resultNumber = priceNow - pricePaid
    pricePair = (resultPercentage, resultNumber)
    print(pricePair)
    return pricePair
