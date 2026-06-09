import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://quotes.toscrape.com")
if response.status_code != 200:
    print(f"Failed: {response.status_code}")
else:
    quote_soup = BeautifulSoup(response.text, "html.parser")

    quotes = quote_soup.find_all("div",class_="quote")

    quote_data = []

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        quote_data.append({
        "quote":text,
        "author":author
        })

    print (f"Scraped {len(quote_data)} quotes.")

    df = pd.DataFrame(quote_data)
    print(df.head())