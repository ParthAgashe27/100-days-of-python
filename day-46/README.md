# Day 46 - Spotify Time Machine

## What works
Step 1 done - scrapes Billboard Hot 100 for a given date. Billboard's live site is now paywalled for historical charts, so this uses a Wayback Machine snapshot instead.

## What doesn't
Steps 2-4 (Spotify auth + playlist creation) are blocked. As of Feb/March 2026, Spotify requires the app owner to have Premium just to use the Web API in dev mode. Don't have Premium, so couldn't complete this part.

Source: https://developer.spotify.com/documentation/web-api/references/changes/february-2026

Looked into JioSaavn's unofficial API as an alternative but skipped it - it's no-auth, so it wouldn't actually teach the OAuth flow this project is built around.
