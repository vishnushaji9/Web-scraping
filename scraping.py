from bs4 import BeautifulSoup
import requests


response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, 'lxml')

details =  soup.find_all('article', class_ = 'product_pod')

for books in details:
    title =  books.h3.a['title'].replace(' ', '')
    price = books.find('p',class_ = 'price_color').text
    stock =  books.find('p',class_ = 'instock availability').text
    print(f"{title} : {price} : {stock}")