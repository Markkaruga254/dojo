# Lab 04: Price parser and basic analytics

## Goal

Parse a small CSV price feed into validated records, then calculate daily returns and maximum drawdown. This lab feeds the NSE platform, but its sample data is educational and is not investment advice.

## Build

CSV header: `ticker,date,close,volume`; dates use ISO format `YYYY-MM-DD`.

Implement `parse_prices`, `daily_returns`, and `max_drawdown` in `prices.py`.

- Parse valid rows into `Bar` objects and skip rows with missing or non-numeric close/volume, invalid dates, or a close less than or equal to zero.
- Sort parsed records by ticker, then date.
- Calculate each ticker's close-to-close return as `current_close / previous_close - 1`; the first observation per ticker has no return.
- Calculate maximum drawdown as a positive fraction from a prior running peak to a later trough. Return `0.0` for empty or non-declining input.

## Verify

From this directory:

```bash
python -m pytest -q
```

The supplied tests cover bad rows, sorting, per-ticker returns, and drawdown. Add at least one edge-case test, such as a header-only CSV, duplicate ticker/date rows, zero volume, or a recovery after a drawdown. Make an explicit choice about duplicate dates and document it; the current function contract does not yet specify deduplication.

## Explain and record

- Why silently skipping invalid rows can hide data-quality problems, and what you would count or log in a production ingestion pipeline.
- Why returns must be calculated separately per ticker and in chronological order.
- Why maximum drawdown is measured against a running peak, not just the first close.
- The test command, result, added test, and any assumptions you made.

## Data and safety

Use only data you are permitted to use. Preserve source and date metadata for real datasets, validate units and adjustment conventions before analysis, and do not present this simple calculation as a trading signal or investment recommendation.
