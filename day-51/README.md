# Sauce Demo Checkout Bot

A Selenium + Python script that automates a full shopping flow on
[saucedemo.com](https://www.saucedemo.com/), a demo e-commerce site built for
test-automation practice.

This was built as a substitute for Angela Yu's 100 Days of Code Day 51 project
("Internet Speed Twitter Complainer"), which automates logging into and posting
from a real X/Twitter account. That approach runs into two problems: it violates
X's Terms of Service around automated accounts, and in practice X's own bot-detection
("Confirm your account" identity checks) blocks the login flow outright, even when
attempted manually. Sauce Demo covers the same Selenium concepts with no such
restrictions.

## What it does

1. Logs in with test credentials
2. Randomly picks one of the 4 product sort filters (Name A-Z/Z-A, Price low-high/high-low)
3. Adds the first 3 products (in whatever order the chosen filter produces) to the cart
4. Proceeds to checkout and fills in shipping info (prompted from the user)
5. Completes the order and downloads the order PDF
6. Prints the final confirmation message to verify success

## What it demonstrates

- Form login
- Working with a native `<select>` dropdown via Selenium's `Select` class
- Random decision-making combined with browser automation
- Locating and looping over multiple elements (`find_elements`) instead of a single one
- Avoiding `StaleElementReferenceException` by reading element data *before*
  triggering an action that changes the DOM
- Multi-step form flows (checkout -> info -> confirmation)

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python sauce_demo_checkout_bot.py
```

You'll be prompted for a first name, last name, and zip code during checkout —
these are just used to fill Sauce Demo's checkout form, no real data required.
