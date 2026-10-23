# Web scraping experiments

- `cse-exploration.ipynb`: early requests/BeautifulSoup exploration with saved output removed.
- `legacy_cse.py`: historical Selenium script for stock-market pages. A personal absolute driver path was replaced with `chromedriver.exe`.

The scraper uses old Selenium APIs and fixed page selectors. It is archived for learning, has not been run or modernized, and is not expected to work unchanged with current Selenium or website layouts. It writes `stock update.csv` in its working folder. No driver binary or collected data is included. Check the site's terms and access requirements before any automated collection.

Dependencies referenced by these experiments: selenium, requests, beautifulsoup4. No known-working versions are claimed.
