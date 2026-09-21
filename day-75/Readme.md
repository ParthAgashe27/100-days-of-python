# Day 75 — Google Trends & Data Visualization: Search Trends vs Real-World Data

Explored whether Google search volume correlates with real-world signals — Tesla stock price, Bitcoin price, and the U.S. unemployment rate — using pandas and matplotlib.

## What this covers
- Exploring multiple DataFrames: shape, `.describe()`, min/max via f-strings
- Detecting and removing missing values with `.isna()` and `.dropna()`
- Converting string dates to `datetime` objects with `pd.to_datetime()` across multiple DataFrames
- Resampling daily data to monthly with `.resample('M', on='DATE').last()`
- Dual-axis line charts (`ax1.twinx()`) to compare two differently-scaled metrics (e.g. stock price vs. search volume) on one chart
- Chart styling: custom colors (hex + named), figure size, DPI, rotated tick labels, axis limits
- Date-aware tick formatting with `mdates.YearLocator()` / `MonthLocator()` / `DateFormatter()`
- Smoothing noisy series with a rolling average (`.rolling(window=3).mean()`) to reveal trend vs. noise
- Comparing pre-2020 vs. including-2020 data to see the effect of COVID-era unemployment spikes on the correlation

## Key takeaways
- Tesla search volume and stock price show visible correlation, especially around major news events
- Bitcoin search volume tends to spike alongside (and sometimes slightly lag) price surges
- "Unemployment Benefits" search volume tracks the actual U/E rate closely — and the 2020 data shows an extreme, unprecedented spike that dwarfs the historical pattern

## Files
- `Google_Trends_and_Data_Visualisation_(complete).ipynb` — main notebook
- `TESLA Search Trend vs Price.csv`
- `Bitcoin Search Trend.csv`
- `Daily Bitcoin Price.csv`
- `UE Benefits Search vs UE Rate 2004-19.csv`
- `UE Benefits Search vs UE Rate 2004-20.csv`

## Data sources
- [FRED — Unemployment Rate](https://fred.stlouisfed.org/series/UNRATE/)
- [Google Trends](https://trends.google.com/)
