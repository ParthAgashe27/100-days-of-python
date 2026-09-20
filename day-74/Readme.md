# Day 74 — Data Visualization: LEGO Dataset Analysis

Explored Rebrickable's LEGO dataset covering colors, sets, and themes to answer questions about LEGO's history, product growth, and complexity over time.

## What this covers
- Counting unique values with `.nunique()` and `.value_counts()`
- Sorting to find earliest sets and largest sets by part count
- Grouping and counting sets/themes released per year with `.groupby()` and `.agg()`
- Using `pd.Series.nunique` and `pd.Series.mean` inside `.agg()` for custom aggregations
- Slicing time series data to exclude incomplete years
- Dual-axis line charts (`ax.twinx()`) to compare two differently-scaled metrics on one chart
- Scatter plots to visualize trends over time
- Merging DataFrames on a foreign key (`theme_id` → `id`) to join set counts with theme names
- Styled bar charts (figure size, rotated tick labels, axis labels)

## Key findings
- LEGO's first sets were released in 1949
- The LEGO theme with the most individual sets is **Star Wars** (theme_id 158), found by merging set counts against the themes table
- Average parts per set has grown substantially from the 1950s to the 2010s, showing sets have gotten more complex over time

## Files
- `Lego_Analysis_for_Course_(completed).ipynb` — main notebook
- `data/colors.csv`, `data/sets.csv`, `data/themes.csv` — Rebrickable datasets used

## Data source
[Rebrickable](https://rebrickable.com/downloads/)
