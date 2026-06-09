Quotes Collection Pipeline
An end-to-end data pipeline that scrapes quotes from the web, stores them in a database, analyzes them, and produces a visualization. Built as the capstone project for IS 303.
What it does
The program scrapes the first three pages of quotes.toscrape.com, stores each quote-tag pair in a SQLite database, queries it back with Pandas, and charts the most common tags. It demonstrates a complete workflow: web data acquisition, database storage with an ORM, data analysis, and visualization.
Tech stack

Python 3
requests — fetching web pages
BeautifulSoup — parsing HTML
Peewee — ORM for SQLite storage
Pandas — querying and aggregating the data
matplotlib — charting

How to run
Install the dependencies:
bashpip install requests beautifulsoup4 peewee pandas matplotlib
Run the pipeline:
bashpython quote_scraper.py
The program will scrape the site (with a one-second delay between pages), populate quotes.db, print a summary to the console, and save the chart.
Pipeline structure
The code is organized into five functions plus a main() that orchestrates them:
FunctionPurposefetch_page()Sends the request, checks the status code, returns parsed HTMLscrape_quotes()Loops over the pages and extracts text, author, and tagsstore_quotes()Saves each quote-tag pair to the database, skipping duplicatesanalyze()Loads the data into a DataFrame and runs a groupby aggregationvisualize()Builds and saves the bar chart
Output
Running the program produces:

quotes.db — SQLite database (82 quote-tag rows, 29 unique quotes, 20 unique authors)
quotes_per_tag.png — bar chart of the ten most common tags
Console output — total records, unique counts, and quotes-per-tag

The most common tags were life, love, and inspirational.
Files

quote_scraper.py — the pipeline
quotes.db — the database
quotes_per_tag.png — the chart
analysis.md — full write-up of the dataset, findings, ethics, and limitations

Notes on ethics
quotes.toscrape.com is designed for scraping practice, requires no login, and contains no personal data. The scraper includes rate limiting (time.sleep(1)) to avoid overloading the server.
