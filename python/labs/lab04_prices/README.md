# Lab 04: Price parser (feeds the NSE platform)
CSV header: `ticker,date,close,volume` (dates ISO). Implement `parse_prices`, `daily_returns`, `max_drawdown` in `prices.py`.
Design note for your log: why skip bad rows instead of crashing? What would you log or count instead?
