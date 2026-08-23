# Selenium Practice Bot

A small Selenium + Python script built as a substitute for the "Tinder bot" exercise
in Angela Yu's 100 Days of Code (Day 50). Instead of automating a real dating app
(which violates its Terms of Service), this replicates the same core Selenium
concepts on [the-internet.herokuapp.com](https://the-internet.herokuapp.com/), a
site built specifically for Selenium/automation practice.

## What it demonstrates

- **Form login** — locating fields, sending keys, submitting a form
- **Window/tab handling** — opening a new window, switching between window handles
- **Native browser alerts** — handling JS `alert`, `confirm`, and `prompt` dialogs
- **Popup/modal dismissal** — locating and closing an on-page modal
- **Wait-and-retry logic** — handling `NoSuchElementException` while polling for a
  dynamically-loaded element

## Setup

```bash
pip install -r requirements.txt
```

You'll also need Chrome installed and matching ChromeDriver available on PATH
(or managed automatically depending on your Selenium version).

## Run

```bash
python selenium_practice_bot.py
```

The credentials used (`tomsmith` / `SuperSecretPassword!`) are **public test
credentials** provided by the demo site itself — not real or sensitive.

## Notes

- Uses a JS-executed click (`driver.execute_script("arguments[0].click();", el)`)
  instead of Selenium's native `.click()` for the new-window link, since the
  native click wasn't reliably triggering the `target="_blank"` navigation.
- Disables Chrome's built-in password-leak-detection popup via `chrome_options`,
  since it would otherwise intercept clicks meant for the page itself.
