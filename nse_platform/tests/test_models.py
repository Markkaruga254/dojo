from nse_insights.models import NewsItem, canonical_url, dedupe_news, tag_tickers


def test_canonical_url_strips_tracking_and_fragment():
    assert canonical_url("https://Example.com/a/?utm_source=x&id=1#frag") == "https://example.com/a?id=1"
    assert canonical_url("https://example.com/") == "https://example.com/"


def test_dedupe_keeps_first_by_canonical_url():
    items = [
        NewsItem("https://example.com/a?utm_campaign=z", "A", "s1"),
        NewsItem("https://EXAMPLE.com/a/", "A again", "s2"),
        NewsItem("https://example.com/b", "B", "s1"),
    ]
    out = dedupe_news(items)
    assert [i.title for i in out] == ["A", "B"]


UNIVERSE = {"SCOM": ["Safaricom"], "KCB": ["KCB Group", "KCB"], "EQTY": ["Equity Group"]}


def test_tag_tickers_word_boundaries_and_case():
    assert tag_tickers("Safaricom and KCB Group report results", UNIVERSE) == ["KCB", "SCOM"]
    assert tag_tickers("equity group rallies", UNIVERSE) == ["EQTY"]
    assert tag_tickers("Nothing relevant here", UNIVERSE) == []
    assert tag_tickers("KCBX is not KCB", {"KCB": ["KCB"]}) == ["KCB"]
    assert tag_tickers("KCBX only", {"KCB": ["KCB"]}) == []
