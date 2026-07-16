# Awesome EEG Learning

> 从经典 EEG 范式到卒中、癫痫、睡眠分期与麻醉的中文入门项目。

[![CI](https://github.com/ZHMM1216/awesome-eeg-learning/actions/workflows/ci.yml/badge.svg)](https://github.com/ZHMM1216/awesome-eeg-learning/actions/workflows/ci.yml)
[![Pages](https://github.com/ZHMM1216/awesome-eeg-learning/actions/workflows/pages.yml/badge.svg)](https://github.com/ZHMM1216/awesome-eeg-learning/actions/workflows/pages.yml)
[![DOI verified](https://img.shields.io/badge/DOI-Crossref%20%2B%20DataCite-2ea44f)](catalog/papers.yml)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)

这个仓库把三件经常分散的事放在一起：

1. 一条面向初学者的 EEG 学习路线；
2. 可复现的经典范式和临床数据实验；
3. 带真实 DOI、数据集与作者代码状态的精选文献目录。

## 学习地图

| 专题 | 你要识别的 EEG 特征 | 入门方法 | 学习页 |
|---|---|---|---|
| 睁眼/闭眼 Alpha | 枕区 8–13 Hz 功率变化 | Welch PSD、相对功率 | [Alpha](docs/paradigms/alpha.md) |
| Oddball / P300 | 目标刺激后约 300 ms 正波 | ERP、xDAWN + LDA | [P300](docs/paradigms/p300.md) |
| SSVEP | 刺激频率及谐波响应 | PSD、CCA | [SSVEP](docs/paradigms/ssvep.md) |
| 运动想象 | 感觉运动区 Mu/Beta ERD/ERS | 时频、CSP + LDA | [运动想象](docs/paradigms/motor-imagery.md) |
| ERN / N170 | 错误监测与人脸加工 ERP | 反应/刺激锁定平均 | [ERN 与 N170](docs/paradigms/ern-n170.md) |
| 卒中 | 患侧差异、运动网络重组 | 患者内与跨患者评估 | [卒中](docs/stroke.md) |
| 癫痫 | 发作事件、异常波形 | 事件检测、误报/小时 | [癫痫](docs/epilepsy.md) |
| 睡眠分期 | 慢波、纺锤、K 复合波、REM | 30 秒 Epoch、Macro-F1 | [睡眠](docs/sleep.md) |
| 麻醉 | 药物特异频谱与爆发抑制 | 频谱图、SEF、抑制率 | [麻醉](docs/anesthesia.md) |

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

<!-- LITERATURE-LIST:START -->
## 论文列表

当前收录 **29 篇**经过 DOI 核验的论文。首页提供类似 Awesome List 的快速浏览；[专题文献库](docs/literature.md)按范式和临床方向展开。

### 近五年

本项目当前把 2022–2026 定义为近五年，并优先收录开放数据、评估规范和可复现方法。

#### 2026

| Year | Direction | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|---|
| 2026 | 卒中 / 运动想象 | Scientific Data | [An Upper-Limb Motor Imagery EEG Dataset of Chronic Stroke Patients](https://doi.org/10.1038/s41597-026-07742-x)<br>慢性卒中患者多会话上肢运动想象数据，包含临床量表，可用于纵向和恢复程度相关研究。 | [10.1038/s41597-026-07742-x](https://doi.org/10.1038/s41597-026-07742-x) | 未发现 |

#### 2025

| Year | Direction | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|---|
| 2025 | 卒中 / 运动想象 | Frontiers in Neuroscience | [UET175: EEG dataset of motor imagery tasks in Vietnamese stroke patients](https://doi.org/10.3389/fnins.2025.1580931)<br>越南卒中患者四肢运动想象数据，适合研究低成本设备、跨患者和跨设备泛化。 | [10.3389/fnins.2025.1580931](https://doi.org/10.3389/fnins.2025.1580931) | [作者代码](https://github.com/nmk-k66-uet/UET175) |
| 2025 | 睡眠 | npj Digital Medicine | [SLEEPYLAND: trust begins with fair evaluation of automatic sleep staging models](https://doi.org/10.1038/s41746-025-02237-2)<br>强调自动睡眠分期的公平、多中心和外部分布评估，提醒避免只报告单一数据集高分。 | [10.1038/s41746-025-02237-2](https://doi.org/10.1038/s41746-025-02237-2) | 未发现 |

#### 2024

| Year | Direction | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|---|
| 2024 | 癫痫 | Epilepsia | [SzCORE: Seizure Community Open-Source Research Evaluation framework for the validation of electroencephalography-based automated seizure detection algorithms](https://doi.org/10.1111/epi.18113)<br>统一癫痫发作检测的数据、划分、文件和临床相关指标，首版评估实现以此为规范。 | [10.1111/epi.18113](https://doi.org/10.1111/epi.18113) | [作者代码](https://github.com/esl-epfl/sz-validation-framework) |
| 2024 | 卒中 / 运动想象 | Scientific Data | [An EEG motor imagery dataset for brain computer interface in acute stroke patients](https://doi.org/10.1038/s41597-023-02787-8)<br>50 名急性卒中患者的左右手握持运动想象数据，含原始/预处理数据、提示和患者特征。 | [10.1038/s41597-023-02787-8](https://doi.org/10.1038/s41597-023-02787-8) | [相关实现](https://moabb.neurotechx.com/docs/generated/moabb.datasets.Liu2024.html) |

#### 2023

| Year | Direction | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|---|
| 2023 | 工具 / 基础 | Scientific Data | [DISCOVER-EEG: an open, fully automated EEG pipeline for biomarker discovery in clinical neuroscience](https://doi.org/10.1038/s41597-023-02525-0)<br>面向临床神经科学生物标志物发现的自动化静息态 EEG 流程，适合参考质控和批处理设计。 | [10.1038/s41597-023-02525-0](https://doi.org/10.1038/s41597-023-02525-0) | 未发现 |

#### 2022

| Year | Direction | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|---|
| 2022 | 麻醉 | Scientific Data | [VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients](https://doi.org/10.1038/s41597-022-01411-5)<br>大规模术中多参数数据库，包含部分 BIS 原始 EEG、BIS、SQI、SEF 和抑制率轨道。 | [10.1038/s41597-022-01411-5](https://doi.org/10.1038/s41597-022-01411-5) | [作者代码](https://github.com/vitaldb/examples) |
| 2022 | 睡眠 | IEEE Transactions on Biomedical Engineering | [SleepTransformer: Automatic Sleep Staging With Interpretability and Uncertainty Quantification](https://doi.org/10.1109/TBME.2022.3147187)<br>将序列到序列 Transformer、注意力可解释性和不确定性估计用于自动睡眠分期。 | [10.1109/TBME.2022.3147187](https://doi.org/10.1109/TBME.2022.3147187) | [作者代码](https://github.com/pquochuy/SleepTransformer) |
| 2022 | 麻醉 | Anesthesia & Analgesia | [Open Reimplementation of the BIS Algorithms for Depth of Anesthesia](https://doi.org/10.1213/ANE.0000000000006119)<br>对 BIS 算法进行透明重实现，适合讨论专有处理指数的可解释性、局限与可复现性。 | [10.1213/ANE.0000000000006119](https://doi.org/10.1213/ANE.0000000000006119) | 未发现 |

### 经典与奠基论文

经典论文用于建立概念和方法坐标，不按引用量自动排序。

| Year | Direction | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|---|
| 2021 | 睡眠 | npj Digital Medicine | [U-Sleep: resilient high-frequency sleep staging](https://doi.org/10.1038/s41746-021-00440-5)<br>大规模多中心训练的睡眠分期系统，强调跨数据集、跨导联和跨人群的泛化能力。 | [10.1038/s41746-021-00440-5](https://doi.org/10.1038/s41746-021-00440-5) | [作者代码](https://github.com/perslev/U-Time) |
| 2019 | 基础 / 工具 | Scientific Data | [EEG-BIDS, an extension to the brain imaging data structure for electroencephalography](https://doi.org/10.1038/s41597-019-0104-8)<br>EEG-BIDS 标准论文，规定可共享、可机器读取的 EEG 数据与事件元数据结构。 | [10.1038/s41597-019-0104-8](https://doi.org/10.1038/s41597-019-0104-8) | [相关实现](https://github.com/mne-tools/mne-bids) |
| 2018 | 癫痫 | Frontiers in Neuroinformatics | [The Temple University Hospital Seizure Detection Corpus](https://doi.org/10.3389/fninf.2018.00083)<br>介绍大型临床癫痫发作语料 TUSZ，突出真实临床连续 EEG 与小型片段数据集的差异。 | [10.3389/fninf.2018.00083](https://doi.org/10.3389/fninf.2018.00083) | 未发现 |
| 2018 | 工具 / 运动想象 / P300 / SSVEP | Journal of Neural Engineering | [EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces](https://doi.org/10.1088/1741-2552/aace8c)<br>紧凑型 EEG 深度网络，常作为跨范式基线；首学时仍应先掌握经典线性方法和正确划分。 | [10.1088/1741-2552/aace8c](https://doi.org/10.1088/1741-2552/aace8c) | [作者代码](https://github.com/vlawhern/arl-eegmodels) |
| 2018 | 卒中 / 运动想象 | Annals of Clinical and Translational Neurology | [Brain-computer interfaces for post-stroke motor rehabilitation: a meta-analysis](https://doi.org/10.1002/acn3.544)<br>汇总 BCI 辅助卒中运动康复的临床证据，帮助区分解码性能与康复结局。 | [10.1002/acn3.544](https://doi.org/10.1002/acn3.544) | 未发现 |
| 2017 | 睡眠 | IEEE Transactions on Neural Systems and Rehabilitation Engineering | [DeepSleepNet: A Model for Automatic Sleep Stage Scoring Based on Raw Single-Channel EEG](https://doi.org/10.1109/TNSRE.2017.2721116)<br>自动睡眠分期的代表性深度学习方法，组合多尺度 CNN 与双向循环网络。 | [10.1109/TNSRE.2017.2721116](https://doi.org/10.1109/TNSRE.2017.2721116) | [作者代码](https://github.com/akaraspt/deepsleepnet) |
| 2015 | 麻醉 | Anesthesiology | [Clinical Electroencephalography for Anesthesiologists](https://doi.org/10.1097/ALN.0000000000000841)<br>面向麻醉专业人员的临床 EEG 教程，强调原始波形与谱图，而非只依赖单一指数。 | [10.1097/ALN.0000000000000841](https://doi.org/10.1097/ALN.0000000000000841) | 未发现 |
| 2013 | 基础 / 工具 | Frontiers in Neuroscience | [MEG and EEG data analysis with MNE-Python](https://doi.org/10.3389/fnins.2013.00267)<br>本项目所采用的 Python EEG/MEG 分析主工具，覆盖读取、预处理、可视化、统计和解码。 | [10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267) | [作者代码](https://github.com/mne-tools/mne-python) |
| 2013 | 麻醉 | Proceedings of the National Academy of Sciences | [Electroencephalogram signatures of loss and recovery of consciousness from propofol](https://doi.org/10.1073/pnas.1221180110)<br>描述丙泊酚诱导意识消失和恢复时的典型 EEG 频谱与相干变化。 | [10.1073/pnas.1221180110](https://doi.org/10.1073/pnas.1221180110) | 未发现 |
| 2010 | 麻醉 / 睡眠 | New England Journal of Medicine | [General Anesthesia, Sleep, and Coma](https://doi.org/10.1056/NEJMra0808281)<br>从神经回路和脑状态角度比较麻醉、睡眠与昏迷，是理解麻醉 EEG 的重要概念入口。 | [10.1056/NEJMra0808281](https://doi.org/10.1056/NEJMra0808281) | 未发现 |
| 2004 | 基础 / 工具 | Journal of Neuroscience Methods | [EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis](https://doi.org/10.1016/j.jneumeth.2003.10.009)<br>EEGLAB 工具箱论文，推动了单试次 EEG、ICA 和可复现分析流程的普及。 | [10.1016/j.jneumeth.2003.10.009](https://doi.org/10.1016/j.jneumeth.2003.10.009) | [作者代码](https://github.com/sccn/eeglab) |
| 2001 | 运动想象 | Proceedings of the IEEE | [Motor imagery and direct brain-computer communication](https://doi.org/10.1109/5.939829)<br>运动想象 BCI 的经典综述，重点理解感觉运动节律、ERD/ERS 与训练反馈。 | [10.1109/5.939829](https://doi.org/10.1109/5.939829) | 未发现 |
| 2001 | 癫痫 | Physical Review E | [Indications of nonlinear deterministic and finite-dimensional structures in time series of brain electrical activity: Dependence on recording region and brain state](https://doi.org/10.1103/PhysRevE.64.061907)<br>Bonn 癫痫 EEG 数据相关经典工作；同时提醒初学者不要把短片段分类等同于临床连续发作检测。 | [10.1103/PhysRevE.64.061907](https://doi.org/10.1103/PhysRevE.64.061907) | 未发现 |
| 1996 | N170 | Journal of Cognitive Neuroscience | [Electrophysiological Studies of Face Perception in Humans](https://doi.org/10.1162/jocn.1996.8.6.551)<br>人脸加工 N170 成分的经典工作，连接视觉范式、刺激控制、ERP 与头皮分布。 | [10.1162/jocn.1996.8.6.551](https://doi.org/10.1162/jocn.1996.8.6.551) | 未发现 |
| 1993 | ERN | Psychological Science | [A Neural System for Error Detection and Compensation](https://doi.org/10.1111/j.1467-9280.1993.tb00586.x)<br>错误相关负波 ERN 的奠基研究，适合学习反应锁定 ERP 和认知控制实验设计。 | [10.1111/j.1467-9280.1993.tb00586.x](https://doi.org/10.1111/j.1467-9280.1993.tb00586.x) | 未发现 |
| 1988 | P300 | Electroencephalography and Clinical Neurophysiology | [Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials](https://doi.org/10.1016/0013-4694(88)90149-6)<br>P300 拼写器的代表性论文，展示 Oddball ERP 如何转化为脑机接口控制信号。 | [10.1016/0013-4694(88)90149-6](https://doi.org/10.1016/0013-4694(88)90149-6) | 未发现 |
| 1967 | 基础 | IEEE Transactions on Audio and Electroacoustics | [The use of fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms](https://doi.org/10.1109/TAU.1967.1161901)<br>Welch 功率谱估计的经典论文，是 EEG 频带功率和功率谱密度分析的基础。 | [10.1109/TAU.1967.1161901](https://doi.org/10.1109/TAU.1967.1161901) | 未发现 |
| 1966 | SSVEP | Electroencephalography and Clinical Neurophysiology | [Some characteristics of average steady-state and transient responses evoked by modulated light](https://doi.org/10.1016/0013-4694(66)90088-5)<br>早期系统描述稳态视觉诱发响应的经典研究，为频率标记和 SSVEP-BCI 奠定基础。 | [10.1016/0013-4694(66)90088-5](https://doi.org/10.1016/0013-4694(66)90088-5) | 未发现 |
| 1929 | 基础 | Archiv für Psychiatrie und Nervenkrankheiten | [Über das Elektrenkephalogramm des Menschen](https://doi.org/10.1007/BF01797193)<br>人体脑电研究的奠基性工作。适合了解 EEG 的历史起点，而不是直接作为现代分析规范使用。 | [10.1007/BF01797193](https://doi.org/10.1007/BF01797193) | 未发现 |

<!-- LITERATURE-LIST:END -->

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
