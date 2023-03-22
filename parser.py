import requests
from bs4 import BeautifulSoup as bs
from math import ceil
from time import sleep


def parse(url: str, items=60):
    data = {
        "NAME": [],
        "BRAND": [],
        "PRICE": [],
        "OLD PRICE": []
    }
    pages = ceil(items / 60)
    p = 1
    r = requests.get(url + f"?page={str(p)}")
    soup = bs(r.text, "html.parser")

    for p in range(1, pages + 1):

        print(f"Сбор данных со станицы {p}")

        brands = soup.find_all('div', {"class": 'x-product-card-description__brand-name'})
        names = soup.find_all('div', {"class": 'x-product-card-description__product-name'})
        prices = soup.find_all('div', {"class": 'x-product-card-description__microdata-wrap'})

        for i in range(0, len(prices), 2):
            if prices[i].find('span', {'class': 'x-product-card-description__price-old'}):
                old_price = prices[i].find('span', {'class': 'x-product-card-description__price-old'}).text + ' ₽'
                price = prices[i].find('span', {'class': 'x-product-card-description__price-new'}).text
                data["OLD PRICE"].append(old_price)
                data["PRICE"].append(price)
            else:
                old_price = None
                data["OLD PRICE"].append(old_price)
                price = prices[i].text.strip()
                data["PRICE"].append(price)

        for item in names:
            data["NAME"].append(item.get_text().strip())

        for item in brands:
            data["BRAND"].append(item.get_text())

        print("OK")
        sleep(1)

        r = requests.get(url + f"?page={str(p)}")
        soup = bs(r.text, "html.parser")

    return data
