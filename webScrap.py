import requests
from bs4 import BeautifulSoup
import csv

search = input("Enter the product:")
search = search.replace(" ", "+")
url = f"https://www.amazon.in/s?k={search}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.5"
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
product = soup.find_all("div", {"data-component-type": "s-search-result"})

with open("amazon.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Current Price", "Original Price", "Rating"])

    for item in product:
        if item.h2:
            name = item.h2.text.strip()
            link_tag = item.h2.a
            link = "https://www.amazon.in" + link_tag["href"] if link_tag else "No link"
            price_tag = item.find("span", class_="a-offscreen")
            price = price_tag.text.strip() if price_tag else "Price not listed"
            old_price_tag = item.find("span", class_="a-text-price")
            old_price_span = old_price_tag.find("span", class_="a-offscreen") if old_price_tag else None
            old_price = old_price_span.text.strip() if old_price_span else "No original price"
            rating_tag = item.find("span", class_="a-icon-alt")
            rating = rating_tag.text.strip() if rating_tag else "No rating"

            print("\n")
            print("Product:", name)
            print("Current Price:", price)
            print("Old Price:", old_price)
            print("Rating:", rating)

            writer.writerow([name, price, old_price, rating])

