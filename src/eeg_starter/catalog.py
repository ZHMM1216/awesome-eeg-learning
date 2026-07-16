"""Validate the curated paper and dataset catalogs."""

from __future__ import annotations

import argparse
from difflib import SequenceMatcher
import re
import sys
from pathlib import Path
from typing import Any

import requests
import yaml

ROOT = Path(__file__).resolve().parents[2]
CATALOG_DIR = ROOT / "catalog"
DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)
CODE_RELATIONS = {"official", "author_related", "community_reproduction", "none_found"}
TOPICS = {
    "foundation",
    "tooling",
    "p300",
    "ssvep",
    "motor-imagery",
    "ern",
    "n170",
    "stroke",
    "epilepsy",
    "sleep",
    "anesthesia",
}


def load_yaml(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        payload = yaml.safe_load(handle)
    if not isinstance(payload, list):
        raise ValueError(f"{path} must contain a YAML list")
    return payload


def validate_papers(papers: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_dois: set[str] = set()
    required = {"id", "title", "authors", "year", "venue", "doi", "topics", "summary_zh"}
    for index, paper in enumerate(papers, start=1):
        label = paper.get("id", f"row-{index}")
        missing = required - paper.keys()
        if missing:
            errors.append(f"{label}: missing fields {sorted(missing)}")
        paper_id = str(paper.get("id", ""))
        if paper_id in seen_ids:
            errors.append(f"{label}: duplicate id")
        seen_ids.add(paper_id)
        doi = str(paper.get("doi", "")).strip().lower()
        if not DOI_PATTERN.match(doi):
            errors.append(f"{label}: invalid DOI syntax {doi!r}")
        if doi in seen_dois:
            errors.append(f"{label}: duplicate DOI {doi}")
        seen_dois.add(doi)
        relation = paper.get("code_relation", "none_found")
        if relation not in CODE_RELATIONS:
            errors.append(f"{label}: invalid code_relation {relation!r}")
        if relation != "none_found" and not paper.get("code_url"):
            errors.append(f"{label}: code_url required for {relation}")
        unknown_topics = set(paper.get("topics", [])) - TOPICS
        if unknown_topics:
            errors.append(f"{label}: unknown topics {sorted(unknown_topics)}")
        recent = paper.get("recent", False)
        year = paper.get("year")
        if recent and (not isinstance(year, int) or not 2022 <= year <= 2026):
            errors.append(f"{label}: recent papers must be published in 2022-2026")
    return errors


def validate_datasets(datasets: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    required = {"id", "name", "topics", "official_url", "access", "license", "formats"}
    for index, dataset in enumerate(datasets, start=1):
        label = dataset.get("id", f"row-{index}")
        missing = required - dataset.keys()
        if missing:
            errors.append(f"{label}: missing fields {sorted(missing)}")
        if label in seen:
            errors.append(f"{label}: duplicate id")
        seen.add(label)
        unknown_topics = set(dataset.get("topics", [])) - TOPICS
        if unknown_topics:
            errors.append(f"{label}: unknown topics {sorted(unknown_topics)}")
    return errors


def check_doi_online(paper: dict[str, Any], timeout: float = 15.0) -> str | None:
    doi = paper["doi"]
    response = requests.get(
        f"https://api.crossref.org/works/{requests.utils.quote(doi, safe='')}",
        headers={"User-Agent": "awesome-eeg-learning/0.1 (mailto:maintainer@example.com)"},
        timeout=timeout,
    )
    source = "crossref"
    if response.status_code == 404:
        # DataCite indexes datasets and some non-Crossref records.
        response = requests.get(f"https://api.datacite.org/dois/{doi}", timeout=timeout)
        source = "datacite"
    if not response.ok:
        return f"{paper['id']}: DOI lookup returned HTTP {response.status_code}"
    payload = response.json()
    if source == "crossref":
        metadata = payload["message"]
        remote_title = metadata.get("title", [""])[0]
        date_parts = metadata.get("published", {}).get("date-parts", [[None]])
        remote_year = date_parts[0][0]
    else:
        metadata = payload["data"]["attributes"]
        titles = metadata.get("titles", [])
        remote_title = titles[0].get("title", "") if titles else ""
        remote_year = int(str(metadata.get("publicationYear", "0"))[:4] or 0)

    def normalize(value: str) -> str:
        return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()

    similarity = SequenceMatcher(None, normalize(paper["title"]), normalize(remote_title)).ratio()
    if similarity < 0.72:
        return f"{paper['id']}: DOI title mismatch ({remote_title!r})"
    if remote_year and abs(int(paper["year"]) - int(remote_year)) > 1:
        return f"{paper['id']}: DOI year mismatch ({paper['year']} vs {remote_year})"
    return None


def run_validation(online: bool = False) -> list[str]:
    papers = load_yaml(CATALOG_DIR / "papers.yml")
    datasets = load_yaml(CATALOG_DIR / "datasets.yml")
    errors = validate_papers(papers) + validate_datasets(datasets)
    if online:
        for paper in papers:
            try:
                error = check_doi_online(paper)
            except requests.RequestException as exc:
                error = f"{paper['id']}: DOI lookup failed: {exc}"
            if error:
                errors.append(error)
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", action="store_true", help="also resolve every DOI online")
    args = parser.parse_args()
    errors = run_validation(online=args.online)
    if errors:
        print("Catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)
    print("Catalog validation passed.")


if __name__ == "__main__":
    main()
