# Zillow-Clone Scraper + Google Forms Autofill

A capstone project combining BeautifulSoup web scraping with Selenium form
automation. Scrapes rental listings from App Brewery's Zillow-Clone practice
site, then automatically fills out and submits a Google Form once per listing,
producing a spreadsheet of all the data.

## What it does

1. Scrapes all listings from https://appbrewery.github.io/Zillow-Clone/ using
   BeautifulSoup + requests — pulling each listing's link, price, and address
2. Cleans the scraped data (strips `+`/`/mo` from prices, removes pipes and
   extra whitespace from addresses)
3. Uses Selenium to open a Google Form and submit one response per listing,
   looping through all scraped data
4. Responses collect into a linked Google Sheet, giving a full spreadsheet of
   rental listings

## What it demonstrates

- BeautifulSoup: `find_all`, filtering by `data-test` attributes, extracting
  text and `href` attributes, and cleaning/normalizing scraped strings
- Selenium: locating form inputs positionally (`find_elements` + indexing)
  when a page's underlying `entry.XXXXX` field IDs aren't easily exposed
- Looping a full scrape-and-submit pipeline across many records, reloading
  the form fresh for each submission

## Setup

```bash
pip install -r requirements.txt
```

You'll need your own Google Form with 3 short-answer questions (address,
price per month, link) — replace `FORM_URL` in the script with your own
form's URL.

## Run

```bash
python main.py
```
