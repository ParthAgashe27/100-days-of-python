# Day 78 — Seaborn & Linear Regression: Do Bigger Budgets Mean Bigger Box Office?

Using movie budget and revenue data scraped from [the-numbers.com](https://www.the-numbers.com/movie/budgets), this notebook investigates whether higher production budgets lead to higher worldwide gross, using `pandas`, `seaborn`, and `scikit-learn`.

## What this notebook covers

**Data cleaning**
- Stripped `$` and `,` from the budget/gross columns and converted them to numeric
- Converted `Release_Date` to datetime
- Checked for NaNs and duplicate rows

**Investigating problem rows**
- Films with $0 domestic and/or $0 worldwide gross (sorted by budget to spot the biggest "zero" films)
- Filtering with both boolean masks (`.loc`) and `.query()` (including `@variable` syntax)
- Removed films released after the data scrape date (1 May 2018), since they hadn't had time to earn revenue
- Percentage of films where budget exceeded worldwide gross (money-losing films)

**Visualization with Seaborn**
- Scatter and bubble charts (budget vs. gross; release date vs. budget, with size/hue for gross)
- Styling with `sns.axes_style()`, axis limits, figure size and DPI
- Regression plots (`sns.regplot`) with custom scatter/line styling

**Feature engineering**
- Converted release years to decades using `year // 10 * 10`
- Split the data into `old_films` (up to the 1960s) and `new_films` (1970s onward)

**Linear regression with scikit-learn**
- Fit `REVENUE = θ₀ + θ₁ × BUDGET` separately for old and new films
- Compared intercept, slope and R² to see how much variance the budget explains in each era
- Used the fitted model to estimate worldwide revenue for a $350M film

## Key takeaways
- Zero-revenue rows and unreleased films distort any analysis, so they need investigating before modelling
- A regression line can look reasonable on a chart while R² shows how weak the relationship really is
- Splitting by era changes the story: the budget-revenue relationship differs a lot between old and new films

## Requirements
```
pandas
matplotlib
seaborn
scikit-learn
```

## Data
`cost_revenue_dirty.csv` — place in the same directory as the notebook.
