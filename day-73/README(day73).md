# Day 73 — Data Visualization: Programming Language Trends (Stack Overflow Data)

Analyzed Stack Overflow question tags over time to see how programming language popularity has changed, using data cleaning, reshaping, and time series visualization.

## What this covers
- Reading a CSV with custom column names (`names=`, `header=0`)
- Exploring shape, counts, and grouped sums (`.groupby('TAG').sum()`, `.count()`)
- Converting string dates to proper `datetime` objects with `pd.to_datetime()`
- Reshaping data from long to wide format with `.pivot()` (rows = dates, columns = languages, values = post counts)
- Handling missing values with `.fillna(0)` — some languages (e.g. Go, Swift) have fewer months of data since they didn't exist/weren't tagged for the dataset's full date range, which is why raw `.count()` differs per language
- Plotting single and multiple time series with Matplotlib, including labeled axes, legends, and custom figure sizing
- Smoothing noisy time series data using a rolling mean (`.rolling(window=6).mean()`) to reveal underlying trends

## Files
- `programming_languages_trends.ipynb` — main notebook
- `QueryResults.csv` — Stack Overflow tag/post-count dataset used

## Data source
Stack Overflow post tags queried via StackExchange Data Explorer (query included in notebook markdown).
