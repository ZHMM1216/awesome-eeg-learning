"""List curated datasets and show their access instructions."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def load_datasets() -> list[dict]:
    with (ROOT / "catalog" / "datasets.yml").open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset", nargs="?", help="dataset id; omit to list all datasets")
    args = parser.parse_args()
    datasets = load_datasets()
    if not args.dataset:
        for dataset in datasets:
            print(f"{dataset['id']:<20} {dataset['name']}")
        return
    for dataset in datasets:
        if dataset["id"] == args.dataset:
            print(dataset["name"])
            print(f"Official URL: {dataset['official_url']}")
            print(f"Access: {dataset['access']}")
            print(f"License: {dataset['license']}")
            print(dataset.get("instructions_zh", "请遵循官方页面的数据访问说明。"))
            return
    raise SystemExit(f"Unknown dataset: {args.dataset}")


if __name__ == "__main__":
    main()

