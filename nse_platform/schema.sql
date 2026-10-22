-- Postgres schema (v1)
CREATE TABLE companies (
  ticker      TEXT PRIMARY KEY,
  name        TEXT NOT NULL,
  sector      TEXT,
  aliases     TEXT[] NOT NULL DEFAULT '{}'
);

CREATE TABLE prices (
  ticker      TEXT NOT NULL REFERENCES companies(ticker),
  day         DATE NOT NULL,
  open        NUMERIC(14,4),
  high        NUMERIC(14,4),
  low         NUMERIC(14,4),
  close       NUMERIC(14,4) NOT NULL CHECK (close > 0),
  volume      BIGINT,
  source      TEXT NOT NULL,
  fetched_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (ticker, day)
);

CREATE TABLE news_items (
  id            BIGSERIAL PRIMARY KEY,
  canonical_url TEXT NOT NULL UNIQUE,
  title         TEXT NOT NULL,
  source        TEXT NOT NULL,
  published_at  TIMESTAMPTZ,
  fetched_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  body_excerpt  TEXT,
  content_hash  TEXT NOT NULL
);

CREATE TABLE news_tickers (
  news_id  BIGINT NOT NULL REFERENCES news_items(id) ON DELETE CASCADE,
  ticker   TEXT   NOT NULL REFERENCES companies(ticker),
  PRIMARY KEY (news_id, ticker)
);

CREATE TABLE summaries (
  news_id        BIGINT NOT NULL REFERENCES news_items(id) ON DELETE CASCADE,
  model          TEXT NOT NULL,
  prompt_version TEXT NOT NULL,
  input_hash     TEXT NOT NULL,
  text           TEXT NOT NULL,
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (news_id, model, prompt_version, input_hash)
);

CREATE TABLE risk_flags (
  news_id     BIGINT NOT NULL REFERENCES news_items(id) ON DELETE CASCADE,
  ticker      TEXT NOT NULL REFERENCES companies(ticker),
  flag        TEXT NOT NULL CHECK (flag IN ('governance','political','regulatory','liquidity','other')),
  confidence  REAL CHECK (confidence BETWEEN 0 AND 1),
  PRIMARY KEY (news_id, ticker, flag)
);

CREATE INDEX idx_news_published ON news_items (published_at DESC);
CREATE INDEX idx_prices_day ON prices (day DESC);
