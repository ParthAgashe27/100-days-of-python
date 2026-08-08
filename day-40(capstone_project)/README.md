# Flight Club — Day 39 & 40 (100 Days of Code)

A flight deal tracker that checks live prices against a Google Sheet of destinations, and emails subscribed customers when a cheaper fare is found.

## What it does

- **DataManager** — reads/writes destination + lowest-price data to a Google Sheet via the Sheety API.
- **UserManager** — reads customer sign-ups (name, email) from a second Sheety-backed sheet, fed by a Google Form.
- **FlightSearch** — queries FlightAPI.io for round-trip prices across a list of destination cities.
- **flight_data** — parses the cheapest quote from the API response and extracts flight details (IATA codes, dates) from the response.
- **NotificationManager** — sends a single combined email to every subscribed customer, listing every destination that dropped below its recorded lowest price.

## Design choices worth noting

- **Amadeus → FlightAPI.io**: Amadeus Self-Service API access was shut down (July 2026, now enterprise-only), so flight search was rebuilt on FlightAPI.io instead. Kiwi Tequila was considered and ruled out (50k MAU minimum requirement).
- **One email, not one per destination**: instead of firing off a separate email per city with a price drop, all deals from a single run are collected into one list and sent as a single combined email per customer. Cleaner for the recipient, and avoids reconnecting to the SMTP server per city.
- **Hardcoded IATA codes**: the 5 test cities (Paris/CDG, Frankfurt/FRA, Tokyo/HND, Melbourne/MEL, Delhi/DEL) use hardcoded IATA codes rather than a city-search API, to keep the free-tier API usage minimal.

## Known limitation — Multi-city search

FlightAPI.io's Multi Trip API (`/multitrip`) is implemented in `flight_search.py` (`search_multi_city_flights`) but is **commented out** and untested against live data. The endpoint consistently returns `401 Unauthorized` despite valid credentials and unused request credits — confirmed via testing that the identical API key succeeds on the round-trip endpoint but fails on multi-trip. Third-party research confirms multi-city search is gated to paid FlightAPI.io plans, separate from the free-tier request-credit allowance shown on the dashboard.

The method's request-building logic (dynamic `arp`/`date` param construction for 3–5 leg trips) is complete and should work once run against a paid-tier key — it just hasn't been verified live.

## Free tier limits

FlightAPI's free tier gives 30 request credits. A full 5-city run burns through these fast (~2 credits per round-trip call), so I had to switch between a couple of free accounts while testing. Not a real solution long-term, just what got the project working without paying.

## Setup

Requires a `.env` or config with:
- Sheety endpoints (prices sheet + users sheet)
- FlightAPI.io API key
- Gmail address + app password (for SMTP)

## Tech

Python, `requests`, `smtplib`, Sheety (Google Sheets as a REST API), Google Forms.
