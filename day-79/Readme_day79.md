# Day 79 — Nobel Prize Analysis

Exploratory analysis of every Nobel Prize awarded since 1901, using `pandas`, `plotly`, `matplotlib` and `seaborn` to look at gender gaps, repeat winners, country/organization dominance, and laureate age trends.

## What this notebook covers

**Data cleaning**
- Checked for duplicate rows and NaN values (`.duplicated()`, `.isna().sum()`)
- Investigated *why* NaNs exist: birth-date/city/country/sex are missing for laureates that are organizations (e.g. UN, Red Cross), not individuals; organization fields are missing when the laureate is an individual with no institutional affiliation
- Converted `birth_date` to `datetime`
- Parsed `prize_share` (e.g. `"1/3"`) into a numeric `share_pct` column

**Gender & repeat winners**
- Donut chart of male vs. female laureates
- First 3 women to win a Nobel Prize
- Identified repeat winners using both `.duplicated(subset=...)` and an alternate `.groupby().filter()` approach

**Prizes by category**
- Count and bar chart of prizes per category
- First Economics prize awarded
- Male/female split by category (grouped bar chart)

**Trends over time**
- Prizes awarded per year with a 5-year rolling average (scatter + line)
- Average prize share per year — are prizes being split among more people over time? (dual-axis chart, including an inverted-axis variant)

**Geography**
- Top 20 countries by number of prizes (horizontal bar chart)
- Choropleth map of prizes by country (ISO codes)
- Category breakdown within each top country (merged DataFrame + stacked horizontal bar)
- Cumulative prizes per country over time (line chart) — when did the US overtake other countries?
- Top 20 research organizations and organization cities
- Top 20 laureate birth cities
- Sunburst chart combining organization country → city → name

**Laureate age**
- Calculated `winning_age` from birth year and award year
- Oldest and youngest winners (`nlargest`/`nsmallest`)
- Descriptive stats and histogram of age distribution
- Age vs. year regression (lowess) — are laureates getting older over time?
- Age by category (box plots, both seaborn and plotly)
- Age-vs-year trend split by category (`sns.lmplot` with `row=` and `hue=`)

## Key techniques used
- `groupby().agg()` with custom aggregation functions
- `pd.merge()` to combine per-category and per-country totals
- Nested `groupby().cumsum()` for cumulative time series per group
- Plotly: pie/donut, bar (vertical/horizontal/grouped/stacked), choropleth, sunburst, line
- Seaborn: histplot, regplot (lowess), boxplot, lmplot (faceted regression)

## Requirements
```
pandas
numpy
plotly
seaborn
matplotlib
```

## Data
`nobel_prize_data.csv` — place in the same directory as the notebook.
