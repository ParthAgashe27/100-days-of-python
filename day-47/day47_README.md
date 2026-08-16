# Day 47 - Amazon Price Tracker

Scrapes a product's price off a static practice page, compares it to a target price, and emails an alert if it's below target.

## Notes
- Credentials (email + app password) moved to `.env`, not committed.
- Ran into a UnicodeEncodeError sending the email - the product title had a non-ASCII character, fixed by encoding the message as UTF-8 before sending.
- Skipped the live Amazon site (Step 4) - the assignment itself warns Amazon usually responds with a Captcha instead of real data, not worth the time for a practice project.
