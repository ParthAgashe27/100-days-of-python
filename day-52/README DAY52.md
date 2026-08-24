# Day 52 — Automated Checkout Bot (Selenium)

Part of Angela Yu's 100 Days of Python Bootcamp. The original brief for this day
was to build an Instagram follow/unfollow bot, but that violates Instagram's
Terms of Service — so this project reimplements the same Selenium skills
(finding elements, filling forms, clicking through multi-step flows) against
[saucedemo.com](https://www.saucedemo.com/), a site built specifically for
practicing browser automation.

## What it does

`InventoryBot` drives a full shopping flow on saucedemo.com:

1. Logs in with the standard test account
2. Randomly selects a product sort filter (e.g. "Price (low to high)")
3. Adds a set number of items to the cart
4. Fills out the checkout form and completes the order
5. Generates the order PDF and prints the confirmation message

## Setup

```bash
pip install -r requirements.txt
```

You'll also need Chrome installed and matching `chromedriver` available on
your PATH (or managed automatically, depending on your Selenium version).

## Usage

```bash
python inventory_bot.py
```

The browser window stays open after the script finishes (`detach=True`) so
you can inspect the result. Call `bot.close()` at the end of the script if
you'd rather it quit automatically.

## Notes / limitations

- Waits are handled with `WebDriverWait` on the key transitions, but not
  every single element lookup — reasonably safe for a stable test site like
  saucedemo, less safe if pointed at a real, slower-loading site.
- Error handling around the PDF/confirmation step will print a message and
  continue rather than crash, but earlier steps (login, checkout form) will
  still raise if the page structure changes.
- No headless mode configured — runs with a visible browser window by
  default.

## Why not the original Instagram bot?

Automating follow/unfollow actions on Instagram violates their [Terms of
Service](https://help.instagram.com/581066165581870) and can get an account
flagged or banned. This version keeps the same learning objectives
(Selenium navigation, forms, dynamic dropdowns, exception handling) without
touching a real platform's TOS.
