# Day 72 — Data Exploration with Pandas: College Major vs Salary

Explored a dataset of starting and mid-career salaries by college major using pandas, practicing DataFrame filtering, sorting, and aggregation.

## What this covers
- Loading a CSV into a DataFrame and inspecting it (`.head()`, `.tail()`, `.shape`, `.columns`)
- Handling missing data with `.isna()` and `.dropna()`
- Finding max values and their index with `.idxmax()`
- Creating a new derived column (`Spread` = 90th percentile − 10th percentile salary) with `.insert()`
- Sorting to find highest earning-potential majors and highest-risk/reward majors with `.sort_values()`
- Grouping and aggregating with `.groupby('Group').mean(numeric_only=True)` — `numeric_only=True` is required here since the DataFrame has a non-numeric `Group`/major-name column, and `.mean()` would otherwise fail trying to average non-numeric data

## Files
- `college_major_salary_exploration.ipynb` — main notebook
- `salaries_by_college_major.csv` — dataset used
