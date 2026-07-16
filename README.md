# Awesome EEG Learning

> 从经典 EEG 范式到卒中、癫痫、睡眠分期与麻醉的中文入门项目。

[![CI](https://github.com/YOUR_GITHUB_USERNAME/awesome-eeg-learning/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_GITHUB_USERNAME/awesome-eeg-learning/actions/workflows/ci.yml)
[![Pages](https://github.com/YOUR_GITHUB_USERNAME/awesome-eeg-learning/actions/workflows/pages.yml/badge.svg)](https://github.com/YOUR_GITHUB_USERNAME/awesome-eeg-learning/actions/workflows/pages.yml)
[![DOI verified](https://img.shields.io/badge/DOI-Crossref%20%2B%20DataCite-2ea44f)](catalog/papers.yml)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)

这个仓库把三件经常分散的事放在一起：

1. 一条面向初学者的 EEG 学习路线；
2. 可复现的经典范式和临床数据实验；
3. 带真实 DOI、数据集与作者代码状态的精选文献目录。

## 从哪里开始

| 阶段 | 内容 | 动手目标 |
|---|---|---|
| 1 | 信号、电极、参考、滤波、伪迹 | 读入 EDF/BIDS，画原始波形和 PSD |
| 2 | Epoch、ERP、时频 | 复现睁闭眼 Alpha 与 Oddball/P300 |
| 3 | 经典 BCI | SSVEP、运动想象、CSP/CCA/xDAWN |
| 4 | 临床 EEG | 卒中、癫痫、睡眠分期、麻醉谱图 |
| 5 | 科研规范 | 受试者级划分、无泄漏评估、可复现报告 |

完整学习页面见部署后的文档站，或直接阅读 [`docs/index.md`](docs/index.md)。

发布自己的 GitHub Pages 站点请见 [`DEPLOY.md`](DEPLOY.md)。

## 安装

推荐 Python 3.10–3.12。Python 3.13 下部分神经科学依赖可能尚未提供完整支持。

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[bci,clinical,notebooks,docs,dev]"
```

验证文献目录：

```bash
eeg-catalog
eeg-catalog --online
```

查看数据访问要求：

```bash
eeg-data
eeg-data chbmit
```

启动本地文档：

```bash
mkdocs serve
```

## 真实数据案例

- 睁闭眼 Alpha、运动想象：[PhysioNet EEGMMIDB](https://physionet.org/content/eegmmidb/1.0.0/)
- Oddball/P300：[OpenNeuro ds003061](https://openneuro.org/datasets/ds003061/versions/1.1.1)
- SSVEP：MNE 自带 BIDS 示例数据
- 卒中运动想象：MOABB `Liu2024`
- 癫痫发作：[CHB-MIT](https://physionet.org/content/chbmit/1.0.0/) 与进阶 TUSZ
- 睡眠分期：[Sleep-EDF Expanded](https://physionet.org/content/sleep-edfx/1.0.0/)
- 麻醉：[PhysioNet GABA anesthesia](https://physionet.org/content/eeg-gaba-anesthesia/1.0.0/) 与 VitalDB

仓库不提交或重新分发临床原始数据。下载前请阅读每个数据集的数据卡和许可。

## 文献质量规则

- 每条论文必须有可解析 DOI；标题、年份和作者通过 Crossref/DataCite 核对。
- 2022–2026 标记为本项目“近五年”；经典论文单独标记，不用引用量自动替代学术判断。
- 代码明确区分作者官方、作者相关、社区复现和未发现代码。
- 只写中文导读，不复制论文摘要；链接优先指向 DOI、期刊、作者仓库和官方数据页。

## 医疗声明

本项目仅用于教育与科研方法学习。代码、模型和示例结果未经医疗器械验证，不能用于诊断、治疗、监护、麻醉给药或其他临床决策。

## 许可

代码采用 [MIT License](LICENSE)。原创文档建议引用并保留出处；外部论文、代码和数据遵循各自许可。
