from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FIGURES = DOCS / "assets" / "figures"


def test_all_local_doc_images_exist() -> None:
    missing: list[str] = []
    for page in DOCS.rglob("*.md"):
        content = page.read_text(encoding="utf-8")
        sources = re.findall(r'<img\s+[^>]*src="([^"]+)"', content)
        sources += re.findall(r"!\[[^]]*]\(([^)]+)\)", content)
        for source in sources:
            if source.startswith(("http://", "https://")):
                continue
            target = (page.parent / source).resolve()
            if not target.exists():
                missing.append(f"{page.relative_to(ROOT)} -> {source}")
    assert not missing, "missing documentation images:\n" + "\n".join(missing)


def test_svg_figures_are_accessible_and_reasonably_sized() -> None:
    figures = sorted(FIGURES.glob("*.svg"))
    assert len(figures) == 10
    for figure in figures:
        content = figure.read_text(encoding="utf-8")
        assert "<svg" in content
        assert "<title>" in content
        assert figure.stat().st_size < 500_000


def test_sampling_lab_has_required_controls() -> None:
    page = (DOCS / "labs" / "sampling.md").read_text(encoding="utf-8")
    script = (DOCS / "javascripts" / "sampling-lab.js").read_text(encoding="utf-8")
    assert 'id="sampling-lab"' in page
    assert 'id="signal-frequency"' in page
    assert 'id="sampling-rate"' in page
    assert "aria-live" in page
    assert "addEventListener" in script
