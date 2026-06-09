"""
IS 303 - A07
Jeremy Eldredge

Inputs:
- quotes.toscrape.com (3 pages of quotes) (https://quotes.toscrape.com)

Processes:
- scrape quote data
- store in SQLite via Peewee
- query and analyze with Pandas
- create chart of quotes per tag

Outputs:
- printed analysis
- quotes.db
- quotes_per_tag.png
"""

import requests, time
from bs4 import BeautifulSoup
import pandas as pd
from peewee import SqliteDatabase, Model, CharField, FloatField, IntegerField, BooleanField
import matplotlib.pyplot as plt


# ------ Database Setup ------
db = SqliteDatabase("quotes.db")

class Quote(Model):
    text = CharField()
    author = CharField()
    tag = CharField()
    class Meta:
        database = db

    def __str__(self):
        return f"{self.text}, {self.author}"


# ------ Scraping Functions ------

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    else:
        print(f"Failed to fetch {url}: status {response.status_code}")
        return None

def scrape_quotes(num_pages=3):
    """Scrape quote data from multiple pages."""
    results = []
    for page in range(1, num_pages + 1):
        soup = fetch_page(f"https://quotes.toscrape.com/page/{page}/")
        if soup is None:
            break
        for quote in soup.find_all("div", class_="quote"):
            text = quote.find(class_="text").get_text(strip=True)
            author = quote.find(class_="author").get_text(strip=True)
            tags = [t.get_text(strip=True) for t in quote.find_all("a", class_="tag")]
            for tag in tags:
                results.append({"text": text, "author": author, "tag": tag})
        time.sleep(1)
    return results 

# ------ Storage Function ------

def store_quotes(quote_list):
    """Store quotes in database, skip duplicates."""
    for q in quote_list:
        exists = Quote.select().where(
            (Quote.text == q["text"]) & (Quote.tag == q["tag"])
        ).exists()
        if not exists:
            Quote.create(**q)

# ------ Analysis Functions ------

def analyze():
    """Query DB, build DataFrame, run groupby, print results."""
    df = pd.DataFrame(list(Quote.select().dicts()))

    print(f"Total rows (quote-tag pairs): {len(df)}")
    print(f"Unique quotes: {df['text'].nunique()}")
    print(f"Unique authors: {df['author'].nunique()}\n")

    print("Quotes per tag:")
    print(df.groupby("tag")["text"].count().sort_values(ascending=False))
    return df

def visualize(df):
    """Create and save a chart of quotes per tag."""
    tag_counts = df.groupby("tag")["text"].count().sort_values(ascending=False).head(10)
    plt.bar(tag_counts.index, tag_counts.values)
    plt.title("Quotes per Tag (Top 10)")
    plt.xlabel("Tag")
    plt.ylabel("Number of Quotes")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("quotes_per_tag.png")
    print("\nSaved chart to quotes_per_tag.png")

# ------ Main Pipeline ------

def main():
    db.connect()
    db.create_tables([Quote])
    quotes = scrape_quotes()
    store_quotes(quotes)
    df = analyze()
    visualize(df)
    db.close()

main()