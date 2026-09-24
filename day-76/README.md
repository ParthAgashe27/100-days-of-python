# Google Play Store App Analytics

Exploratory data analysis of ~10,000 Android apps scraped from the Google Play Store, using `pandas` for cleaning/aggregation and `plotly.express` for interactive visualizations.

**Dataset:** [Google Play Store Apps (Kaggle, Lavanya Gupta, 2018)](https://www.kaggle.com/lava18/google-play-store-apps)

## What this notebook does

**Data Cleaning**
- Drops unused `Last_Updated` and `Android_Ver` columns
- Removes rows with NaN ratings
- Finds and removes duplicate app entries (deduping on `App`, `Type`, `Price` — plain `.duplicated()` isn't enough since the same app can appear with different types/prices)
- Converts `Installs` from string (`"10,000+"` style with commas) to numeric
- Converts `Price` from string (`"$4.99"`) to numeric, then filters out junk entries priced above $250

**Analysis**
- Highest-rated apps, largest apps by size, most-reviewed apps
- Content rating distribution (pie/donut charts)
- Install counts by category (bar charts, log scale)
- Category concentration: number of apps vs. total installs (scatter plot) — shows which categories are saturated vs. under-served
- Genre analysis: splits the semicolon-separated `Genres` column (apps can belong to multiple genres) using `.str.split(';').stack()` to get accurate per-genre counts
- Free vs. paid app counts by category (grouped bar chart)
- Revenue estimate (`Installs × Price` as a ballpark) — highest-grossing paid apps, revenue by category
- Paid app pricing strategy by category (box plots)

## Key techniques used
- `groupby().agg()` for category-level aggregation
- `pd.merge()` to combine app-count and install-count DataFrames
- String cleaning + `pd.to_numeric()` for messy currency/count columns
- `.str.split(expand=True).stack()` for exploding a nested/multi-value column
- Plotly Express: pie, bar (vertical/horizontal/grouped), scatter, box plots, log-scale axes

## Requirements
```
pandas
plotly
```

## Usage
Place `apps.csv` in the same directory and run the notebook top to bottom.
