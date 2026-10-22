# Evaluating summaries and sentiment/risk flags

1. Collect 100 real items across tickers and event types. Hand-label: sentiment (neg/neutral/pos), risk flags (none/governance/political/regulatory/liquidity), and write a reference one-sentence summary.
2. Split: 50 dev / 50 test. Fix the test set before tuning prompts.
3. Metrics: per-class precision/recall for flags; sentiment accuracy and macro-F1; summary faithfulness (0/1: any claim not in the source = fail).
4. Baselines: keyword rules; a simple lexicon. Your LLM pipeline must beat the baseline on the test set to ship.
5. Log: prompt version, model, date, metrics. Show failures in your weekly review.
