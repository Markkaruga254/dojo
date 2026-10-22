from pathlib import Path

from scripts.check_markdown_links import check_links


def test_detects_missing_relative_target(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("[missing](docs/not-here.md)\n", encoding="utf-8")
    errors = check_links(tmp_path)
    assert len(errors) == 1
    assert "missing target" in errors[0]


def test_accepts_existing_relative_target_and_heading(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "guide.md").write_text("# Getting Started\n\nBody.\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("[guide](docs/guide.md#getting-started)\n", encoding="utf-8")
    assert check_links(tmp_path) == []


def test_detects_missing_heading_anchor(tmp_path: Path) -> None:
    (tmp_path / "guide.md").write_text("# Valid Heading\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("[bad](guide.md#not-a-heading)\n", encoding="utf-8")
    errors = check_links(tmp_path)
    assert len(errors) == 1
    assert "missing anchor" in errors[0]


def test_ignores_external_links_and_empty_fragment(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("[external](https://example.com/docs) [top](#)\n", encoding="utf-8")
    assert check_links(tmp_path) == []
