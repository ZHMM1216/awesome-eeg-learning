from eeg_starter.catalog import load_yaml, run_validation, validate_papers
from eeg_starter.catalog import CATALOG_DIR


def test_catalog_is_valid():
    assert run_validation(online=False) == []


def test_duplicate_doi_is_rejected():
    papers = load_yaml(CATALOG_DIR / "papers.yml")
    duplicate = dict(papers[0])
    duplicate["id"] = "duplicate-example"
    errors = validate_papers([*papers, duplicate])
    assert any("duplicate DOI" in error for error in errors)

