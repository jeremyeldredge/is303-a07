1. Dataset Description
I scraped the first three pages of quotes.toscrape.com, a site built specifically for scraping practice. The data is stored in a SQLite database (quotes.db) with one table, Quote, holding three columns: text (the quote), author, and tag. Because each quote can carry several tags, I store one row per quote-tag pair. This produced 82 rows representing 29 unique quotes from 20 unique authors.

2. Pipeline Description
The pipeline runs as five functions orchestrated by main(). fetch_page() sends a requests.get(), checks for a 200 status code before parsing, and returns a BeautifulSoup object. scrape_quotes() loops over the three pages, extracts the text, author, and tags from each quote div, and calls time.sleep(1) between requests. store_quotes() writes each pair to the database using Peewee, first checking .exists() on the (text, tag) combination so re-running the program never duplicates data. analyze() loads the table into a Pandas DataFrame, prints summary counts, and runs a groupby("tag") aggregation. visualize() charts the ten most common tags as a bar graph and saves it with savefig().

3. Findings
The most common tags were life (7), love (6), and inspirational (5), followed by humor (4) and friends (3). The tag distribution is heavily concentrated: a few broad themes dominate while most tags appear only once. I also found that the 82 rows collapse to just 29 unique quotes, which shows how aggressively quotes are multi-tagged on this site.

4. Ethical Considerations
quotes.toscrape.com is explicitly designed for scraping and its robots.txt does not disallow these pages. It requires no login and contains no personal data — the authors are publicly attributed figures, not private individuals. I included time.sleep(1) between requests to avoid hammering the server.

5. Limitations
Three pages is a small sample, so the rankings may not generalize. Because I store one row per tag, any quote with no tags would be dropped entirely, which likely explains why I have 29 unique quotes rather than 30. With more time I would scrape every page, add author-level analysis, and explore tag co-occurrence.