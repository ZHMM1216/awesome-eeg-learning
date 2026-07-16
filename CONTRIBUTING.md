# Contributing

欢迎提交新的论文、数据集、代码链接或教程修正。

新增论文必须：

1. 提供 DOI，并通过 `eeg-catalog --online`；
2. 保留英文原题，不复制摘要；
3. 给出简短中文导读；
4. 明确代码属于作者官方、作者相关、社区复现或未发现；
5. 不提交受限临床数据、患者信息或未经许可的论文 PDF。

提交前运行：

```bash
pytest
ruff check .
mkdocs build --strict
```

