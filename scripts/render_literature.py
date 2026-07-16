"""Render human-readable paper tables from the verified YAML catalog."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog" / "papers.yml"
README_PATH = ROOT / "README.md"
LITERATURE_PATH = ROOT / "docs" / "literature.md"

START_MARKER = "<!-- LITERATURE-LIST:START -->"
END_MARKER = "<!-- LITERATURE-LIST:END -->"

TOPICS = (
    (
        "foundation",
        "基础、工具与科研规范",
        "从 EEG 历史、功率谱和数据标准，走到 MNE、EEGLAB 与可复现流程。",
    ),
    ("p300", "Oddball / P300", "学习刺激锁定 ERP、稀有目标效应与 P300-BCI。"),
    ("ssvep", "SSVEP", "学习频率标记、枕区响应、谐波与 CCA。"),
    (
        "motor-imagery",
        "运动想象",
        "学习 Mu/Beta ERD/ERS、CSP 与跨会话、跨受试者评估。",
    ),
    ("ern", "错误相关负波 ERN", "学习反应锁定 ERP 与错误监测。"),
    ("n170", "人脸 N170", "学习视觉 ERP、枕颞分布与条件比较。"),
    ("stroke", "卒中", "连接运动想象解码、患者差异与康复结局。"),
    ("epilepsy", "癫痫", "区分发作检测、预测、分类与临床诊断。"),
    ("sleep", "睡眠分期", "学习 30 秒 Epoch、五分类、序列模型和外部验证。"),
    ("anesthesia", "麻醉", "学习原始波形、频谱图、爆发抑制与药物特异性。"),
)

TOPIC_LABELS = {
    "foundation": "基础",
    "tooling": "工具",
    "p300": "P300",
    "ssvep": "SSVEP",
    "motor-imagery": "运动想象",
    "ern": "ERN",
    "n170": "N170",
    "stroke": "卒中",
    "epilepsy": "癫痫",
    "sleep": "睡眠",
    "anesthesia": "麻醉",
}

CODE_LABELS = {
    "official": "作者代码",
    "author_related": "相关实现",
    "community": "社区复现",
    "none_found": "未发现",
}


def load_papers() -> list[dict]:
    return yaml.safe_load(CATALOG_PATH.read_text(encoding="utf-8"))


def clean(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def code_cell(paper: dict) -> str:
    relation = paper["code_relation"]
    label = CODE_LABELS[relation]
    url = paper.get("code_url")
    return f"[{label}]({url})" if url else label


def paper_cell(paper: dict) -> str:
    title = clean(paper["title"])
    summary = clean(paper["summary_zh"])
    return f"[{title}]({paper['paper_url']})<br>{summary}"


def topic_cell(paper: dict) -> str:
    labels = [TOPIC_LABELS[t] for t in paper["topics"] if t in TOPIC_LABELS]
    return " / ".join(dict.fromkeys(labels))


def rows_as_table(papers: list[dict], include_topic: bool) -> list[str]:
    if include_topic:
        rows = [
            "| Year | Direction | Venue | Paper Title and Interpretation | DOI | Code |",
            "|---:|---|---|---|---|---|",
        ]
    else:
        rows = [
            "| Year | Venue | Paper Title and Interpretation | DOI | Code |",
            "|---:|---|---|---|---|",
        ]

    for paper in papers:
        common = [
            str(paper["year"]),
            clean(paper["venue"]),
            paper_cell(paper),
            f"[{paper['doi']}](https://doi.org/{paper['doi']})",
            code_cell(paper),
        ]
        if include_topic:
            common.insert(1, topic_cell(paper))
        rows.append("| " + " | ".join(common) + " |")
    return rows


def render_readme_block(papers: list[dict]) -> str:
    recent = sorted(
        (paper for paper in papers if paper["recent"]),
        key=lambda paper: (paper["year"], paper["title"]),
        reverse=True,
    )
    classics = sorted(
        (paper for paper in papers if paper["classic"]),
        key=lambda paper: (paper["year"], paper["title"]),
        reverse=True,
    )

    lines = [
        START_MARKER,
        "## 论文列表",
        "",
        (
            f"当前收录 **{len(papers)} 篇**经过 DOI 核验的论文。"
            "首页提供类似 Awesome List 的快速浏览；"
            "[专题文献库](docs/literature.md)按范式和临床方向展开。"
        ),
        "",
        "### 近五年",
        "",
        "本项目当前把 2022–2026 定义为近五年，并优先收录开放数据、评估规范和可复现方法。",
        "",
    ]
    for year in sorted({paper["year"] for paper in recent}, reverse=True):
        year_papers = [paper for paper in recent if paper["year"] == year]
        lines.extend([f"#### {year}", "", *rows_as_table(year_papers, True), ""])

    lines.extend(
        [
            "### 经典与奠基论文",
            "",
            "经典论文用于建立概念和方法坐标，不按引用量自动排序。",
            "",
            *rows_as_table(classics, True),
            "",
            END_MARKER,
        ]
    )
    return "\n".join(lines)


def render_literature(papers: list[dict]) -> str:
    lines = [
        "# EEG 精选论文库",
        "",
        (
            f"这里从 `catalog/papers.yml` 自动生成 **{len(papers)} 篇**论文的可浏览列表。"
            "每条记录都包含真实 DOI、中文导读和代码关系；不要直接手改本页表格。"
        ),
        "",
        "## 如何阅读这份列表",
        "",
        "- **作者代码**：论文作者或项目官方公开的实现。",
        "- **相关实现**：作者相关生态或标准工具中的数据接入，不等同于论文原始训练代码。",
        "- **社区复现**：第三方复现，需要独立检查与原文的一致性。",
        "- **未发现**：核验时未找到可信公开代码，不代表代码永远不存在。",
        "- 2022–2026 是本项目当前的“近五年”；更早论文按经典或重要工具工作收录。",
        "",
    ]

    for topic, title, description in TOPICS:
        selected = sorted(
            (paper for paper in papers if topic in paper["topics"]),
            key=lambda paper: (paper["year"], paper["title"]),
            reverse=True,
        )
        lines.extend([f"## {title}", "", description, ""])
        for year in sorted({paper["year"] for paper in selected}, reverse=True):
            year_papers = [paper for paper in selected if paper["year"] == year]
            lines.extend([f"### {year}", "", *rows_as_table(year_papers, False), ""])

    lines.extend(
        [
            "## 维护与复核",
            "",
            "```bash",
            "eeg-catalog --online",
            "python scripts/render_literature.py --check",
            "```",
            "",
            (
                "第一条命令通过 Crossref/DataCite 重查 DOI、标题和年份；"
                "第二条命令确认 README 与本页没有偏离机器目录。"
            ),
            "",
        ]
    )
    return "\n".join(lines)


def replace_readme_block(readme: str, block: str) -> str:
    if START_MARKER not in readme or END_MARKER not in readme:
        raise RuntimeError("README is missing literature list markers")
    before, remainder = readme.split(START_MARKER, maxsplit=1)
    _, after = remainder.split(END_MARKER, maxsplit=1)
    return before.rstrip() + "\n\n" + block + "\n\n" + after.lstrip()


def write_or_check(path: Path, content: str, check: bool) -> bool:
    expected = content.rstrip() + "\n"
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if current == expected:
        return True
    if check:
        print(f"out of date: {path.relative_to(ROOT)}")
        return False
    path.write_text(expected, encoding="utf-8")
    print(f"rendered: {path.relative_to(ROOT)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    papers = load_papers()
    readme = README_PATH.read_text(encoding="utf-8")
    readme_output = replace_readme_block(readme, render_readme_block(papers))
    results = [
        write_or_check(README_PATH, readme_output, args.check),
        write_or_check(LITERATURE_PATH, render_literature(papers), args.check),
    ]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
