# EEG 精选论文库

这里从 `catalog/papers.yml` 自动生成 **29 篇**论文的可浏览列表。每条记录都包含真实 DOI、中文导读和代码关系；不要直接手改本页表格。

## 如何阅读这份列表

- **作者代码**：论文作者或项目官方公开的实现。
- **相关实现**：作者相关生态或标准工具中的数据接入，不等同于论文原始训练代码。
- **社区复现**：第三方复现，需要独立检查与原文的一致性。
- **未发现**：核验时未找到可信公开代码，不代表代码永远不存在。
- 2022–2026 是本项目当前的“近五年”；更早论文按经典或重要工具工作收录。

## 基础、工具与科研规范

从 EEG 历史、功率谱和数据标准，走到 MNE、EEGLAB 与可复现流程。

### 2023

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2023 | Scientific Data | [DISCOVER-EEG: an open, fully automated EEG pipeline for biomarker discovery in clinical neuroscience](https://doi.org/10.1038/s41597-023-02525-0)<br>面向临床神经科学生物标志物发现的自动化静息态 EEG 流程，适合参考质控和批处理设计。 | [10.1038/s41597-023-02525-0](https://doi.org/10.1038/s41597-023-02525-0) | 未发现 |

### 2019

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2019 | Scientific Data | [EEG-BIDS, an extension to the brain imaging data structure for electroencephalography](https://doi.org/10.1038/s41597-019-0104-8)<br>EEG-BIDS 标准论文，规定可共享、可机器读取的 EEG 数据与事件元数据结构。 | [10.1038/s41597-019-0104-8](https://doi.org/10.1038/s41597-019-0104-8) | [相关实现](https://github.com/mne-tools/mne-bids) |

### 2013

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2013 | Frontiers in Neuroscience | [MEG and EEG data analysis with MNE-Python](https://doi.org/10.3389/fnins.2013.00267)<br>本项目所采用的 Python EEG/MEG 分析主工具，覆盖读取、预处理、可视化、统计和解码。 | [10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267) | [作者代码](https://github.com/mne-tools/mne-python) |

### 2004

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2004 | Journal of Neuroscience Methods | [EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis](https://doi.org/10.1016/j.jneumeth.2003.10.009)<br>EEGLAB 工具箱论文，推动了单试次 EEG、ICA 和可复现分析流程的普及。 | [10.1016/j.jneumeth.2003.10.009](https://doi.org/10.1016/j.jneumeth.2003.10.009) | [作者代码](https://github.com/sccn/eeglab) |

### 1967

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1967 | IEEE Transactions on Audio and Electroacoustics | [The use of fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms](https://doi.org/10.1109/TAU.1967.1161901)<br>Welch 功率谱估计的经典论文，是 EEG 频带功率和功率谱密度分析的基础。 | [10.1109/TAU.1967.1161901](https://doi.org/10.1109/TAU.1967.1161901) | 未发现 |

### 1929

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1929 | Archiv für Psychiatrie und Nervenkrankheiten | [Über das Elektrenkephalogramm des Menschen](https://doi.org/10.1007/BF01797193)<br>人体脑电研究的奠基性工作。适合了解 EEG 的历史起点，而不是直接作为现代分析规范使用。 | [10.1007/BF01797193](https://doi.org/10.1007/BF01797193) | 未发现 |

## Oddball / P300

学习刺激锁定 ERP、稀有目标效应与 P300-BCI。

### 2018

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2018 | Journal of Neural Engineering | [EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces](https://doi.org/10.1088/1741-2552/aace8c)<br>紧凑型 EEG 深度网络，常作为跨范式基线；首学时仍应先掌握经典线性方法和正确划分。 | [10.1088/1741-2552/aace8c](https://doi.org/10.1088/1741-2552/aace8c) | [作者代码](https://github.com/vlawhern/arl-eegmodels) |

### 1988

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1988 | Electroencephalography and Clinical Neurophysiology | [Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials](https://doi.org/10.1016/0013-4694(88)90149-6)<br>P300 拼写器的代表性论文，展示 Oddball ERP 如何转化为脑机接口控制信号。 | [10.1016/0013-4694(88)90149-6](https://doi.org/10.1016/0013-4694(88)90149-6) | 未发现 |

## SSVEP

学习频率标记、枕区响应、谐波与 CCA。

### 2018

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2018 | Journal of Neural Engineering | [EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces](https://doi.org/10.1088/1741-2552/aace8c)<br>紧凑型 EEG 深度网络，常作为跨范式基线；首学时仍应先掌握经典线性方法和正确划分。 | [10.1088/1741-2552/aace8c](https://doi.org/10.1088/1741-2552/aace8c) | [作者代码](https://github.com/vlawhern/arl-eegmodels) |

### 1966

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1966 | Electroencephalography and Clinical Neurophysiology | [Some characteristics of average steady-state and transient responses evoked by modulated light](https://doi.org/10.1016/0013-4694(66)90088-5)<br>早期系统描述稳态视觉诱发响应的经典研究，为频率标记和 SSVEP-BCI 奠定基础。 | [10.1016/0013-4694(66)90088-5](https://doi.org/10.1016/0013-4694(66)90088-5) | 未发现 |

## 运动想象

学习 Mu/Beta ERD/ERS、CSP 与跨会话、跨受试者评估。

### 2026

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2026 | Scientific Data | [An Upper-Limb Motor Imagery EEG Dataset of Chronic Stroke Patients](https://doi.org/10.1038/s41597-026-07742-x)<br>慢性卒中患者多会话上肢运动想象数据，包含临床量表，可用于纵向和恢复程度相关研究。 | [10.1038/s41597-026-07742-x](https://doi.org/10.1038/s41597-026-07742-x) | 未发现 |

### 2025

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2025 | Frontiers in Neuroscience | [UET175: EEG dataset of motor imagery tasks in Vietnamese stroke patients](https://doi.org/10.3389/fnins.2025.1580931)<br>越南卒中患者四肢运动想象数据，适合研究低成本设备、跨患者和跨设备泛化。 | [10.3389/fnins.2025.1580931](https://doi.org/10.3389/fnins.2025.1580931) | [作者代码](https://github.com/nmk-k66-uet/UET175) |

### 2024

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2024 | Scientific Data | [An EEG motor imagery dataset for brain computer interface in acute stroke patients](https://doi.org/10.1038/s41597-023-02787-8)<br>50 名急性卒中患者的左右手握持运动想象数据，含原始/预处理数据、提示和患者特征。 | [10.1038/s41597-023-02787-8](https://doi.org/10.1038/s41597-023-02787-8) | [相关实现](https://moabb.neurotechx.com/docs/generated/moabb.datasets.Liu2024.html) |

### 2018

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2018 | Journal of Neural Engineering | [EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces](https://doi.org/10.1088/1741-2552/aace8c)<br>紧凑型 EEG 深度网络，常作为跨范式基线；首学时仍应先掌握经典线性方法和正确划分。 | [10.1088/1741-2552/aace8c](https://doi.org/10.1088/1741-2552/aace8c) | [作者代码](https://github.com/vlawhern/arl-eegmodels) |
| 2018 | Annals of Clinical and Translational Neurology | [Brain-computer interfaces for post-stroke motor rehabilitation: a meta-analysis](https://doi.org/10.1002/acn3.544)<br>汇总 BCI 辅助卒中运动康复的临床证据，帮助区分解码性能与康复结局。 | [10.1002/acn3.544](https://doi.org/10.1002/acn3.544) | 未发现 |

### 2001

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2001 | Proceedings of the IEEE | [Motor imagery and direct brain-computer communication](https://doi.org/10.1109/5.939829)<br>运动想象 BCI 的经典综述，重点理解感觉运动节律、ERD/ERS 与训练反馈。 | [10.1109/5.939829](https://doi.org/10.1109/5.939829) | 未发现 |

## 错误相关负波 ERN

学习反应锁定 ERP 与错误监测。

### 1993

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1993 | Psychological Science | [A Neural System for Error Detection and Compensation](https://doi.org/10.1111/j.1467-9280.1993.tb00586.x)<br>错误相关负波 ERN 的奠基研究，适合学习反应锁定 ERP 和认知控制实验设计。 | [10.1111/j.1467-9280.1993.tb00586.x](https://doi.org/10.1111/j.1467-9280.1993.tb00586.x) | 未发现 |

## 人脸 N170

学习视觉 ERP、枕颞分布与条件比较。

### 1996

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1996 | Journal of Cognitive Neuroscience | [Electrophysiological Studies of Face Perception in Humans](https://doi.org/10.1162/jocn.1996.8.6.551)<br>人脸加工 N170 成分的经典工作，连接视觉范式、刺激控制、ERP 与头皮分布。 | [10.1162/jocn.1996.8.6.551](https://doi.org/10.1162/jocn.1996.8.6.551) | 未发现 |

## 卒中

连接运动想象解码、患者差异与康复结局。

### 2026

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2026 | Scientific Data | [An Upper-Limb Motor Imagery EEG Dataset of Chronic Stroke Patients](https://doi.org/10.1038/s41597-026-07742-x)<br>慢性卒中患者多会话上肢运动想象数据，包含临床量表，可用于纵向和恢复程度相关研究。 | [10.1038/s41597-026-07742-x](https://doi.org/10.1038/s41597-026-07742-x) | 未发现 |

### 2025

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2025 | Frontiers in Neuroscience | [UET175: EEG dataset of motor imagery tasks in Vietnamese stroke patients](https://doi.org/10.3389/fnins.2025.1580931)<br>越南卒中患者四肢运动想象数据，适合研究低成本设备、跨患者和跨设备泛化。 | [10.3389/fnins.2025.1580931](https://doi.org/10.3389/fnins.2025.1580931) | [作者代码](https://github.com/nmk-k66-uet/UET175) |

### 2024

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2024 | Scientific Data | [An EEG motor imagery dataset for brain computer interface in acute stroke patients](https://doi.org/10.1038/s41597-023-02787-8)<br>50 名急性卒中患者的左右手握持运动想象数据，含原始/预处理数据、提示和患者特征。 | [10.1038/s41597-023-02787-8](https://doi.org/10.1038/s41597-023-02787-8) | [相关实现](https://moabb.neurotechx.com/docs/generated/moabb.datasets.Liu2024.html) |

### 2018

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2018 | Annals of Clinical and Translational Neurology | [Brain-computer interfaces for post-stroke motor rehabilitation: a meta-analysis](https://doi.org/10.1002/acn3.544)<br>汇总 BCI 辅助卒中运动康复的临床证据，帮助区分解码性能与康复结局。 | [10.1002/acn3.544](https://doi.org/10.1002/acn3.544) | 未发现 |

## 癫痫

区分发作检测、预测、分类与临床诊断。

### 2024

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2024 | Epilepsia | [SzCORE: Seizure Community Open-Source Research Evaluation framework for the validation of electroencephalography-based automated seizure detection algorithms](https://doi.org/10.1111/epi.18113)<br>统一癫痫发作检测的数据、划分、文件和临床相关指标，首版评估实现以此为规范。 | [10.1111/epi.18113](https://doi.org/10.1111/epi.18113) | [作者代码](https://github.com/esl-epfl/sz-validation-framework) |

### 2018

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2018 | Frontiers in Neuroinformatics | [The Temple University Hospital Seizure Detection Corpus](https://doi.org/10.3389/fninf.2018.00083)<br>介绍大型临床癫痫发作语料 TUSZ，突出真实临床连续 EEG 与小型片段数据集的差异。 | [10.3389/fninf.2018.00083](https://doi.org/10.3389/fninf.2018.00083) | 未发现 |

### 2001

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2001 | Physical Review E | [Indications of nonlinear deterministic and finite-dimensional structures in time series of brain electrical activity: Dependence on recording region and brain state](https://doi.org/10.1103/PhysRevE.64.061907)<br>Bonn 癫痫 EEG 数据相关经典工作；同时提醒初学者不要把短片段分类等同于临床连续发作检测。 | [10.1103/PhysRevE.64.061907](https://doi.org/10.1103/PhysRevE.64.061907) | 未发现 |

## 睡眠分期

学习 30 秒 Epoch、五分类、序列模型和外部验证。

### 2025

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2025 | npj Digital Medicine | [SLEEPYLAND: trust begins with fair evaluation of automatic sleep staging models](https://doi.org/10.1038/s41746-025-02237-2)<br>强调自动睡眠分期的公平、多中心和外部分布评估，提醒避免只报告单一数据集高分。 | [10.1038/s41746-025-02237-2](https://doi.org/10.1038/s41746-025-02237-2) | 未发现 |

### 2022

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2022 | IEEE Transactions on Biomedical Engineering | [SleepTransformer: Automatic Sleep Staging With Interpretability and Uncertainty Quantification](https://doi.org/10.1109/TBME.2022.3147187)<br>将序列到序列 Transformer、注意力可解释性和不确定性估计用于自动睡眠分期。 | [10.1109/TBME.2022.3147187](https://doi.org/10.1109/TBME.2022.3147187) | [作者代码](https://github.com/pquochuy/SleepTransformer) |

### 2021

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2021 | npj Digital Medicine | [U-Sleep: resilient high-frequency sleep staging](https://doi.org/10.1038/s41746-021-00440-5)<br>大规模多中心训练的睡眠分期系统，强调跨数据集、跨导联和跨人群的泛化能力。 | [10.1038/s41746-021-00440-5](https://doi.org/10.1038/s41746-021-00440-5) | [作者代码](https://github.com/perslev/U-Time) |
| 2021 | eLife | [An open-source, high-performance tool for automated sleep staging](https://doi.org/10.7554/eLife.70092)<br>易用的开源自动睡眠分期工具，适合用于教学比较，但输出不替代专业睡眠技师评分。 | [10.7554/eLife.70092](https://doi.org/10.7554/eLife.70092) | [作者代码](https://github.com/raphaelvallat/yasa) |

### 2017

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2017 | IEEE Transactions on Neural Systems and Rehabilitation Engineering | [DeepSleepNet: A Model for Automatic Sleep Stage Scoring Based on Raw Single-Channel EEG](https://doi.org/10.1109/TNSRE.2017.2721116)<br>自动睡眠分期的代表性深度学习方法，组合多尺度 CNN 与双向循环网络。 | [10.1109/TNSRE.2017.2721116](https://doi.org/10.1109/TNSRE.2017.2721116) | [作者代码](https://github.com/akaraspt/deepsleepnet) |

### 2010

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2010 | New England Journal of Medicine | [General Anesthesia, Sleep, and Coma](https://doi.org/10.1056/NEJMra0808281)<br>从神经回路和脑状态角度比较麻醉、睡眠与昏迷，是理解麻醉 EEG 的重要概念入口。 | [10.1056/NEJMra0808281](https://doi.org/10.1056/NEJMra0808281) | 未发现 |

## 麻醉

学习原始波形、频谱图、爆发抑制与药物特异性。

### 2022

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2022 | Scientific Data | [VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients](https://doi.org/10.1038/s41597-022-01411-5)<br>大规模术中多参数数据库，包含部分 BIS 原始 EEG、BIS、SQI、SEF 和抑制率轨道。 | [10.1038/s41597-022-01411-5](https://doi.org/10.1038/s41597-022-01411-5) | [作者代码](https://github.com/vitaldb/examples) |
| 2022 | Anesthesia & Analgesia | [Open Reimplementation of the BIS Algorithms for Depth of Anesthesia](https://doi.org/10.1213/ANE.0000000000006119)<br>对 BIS 算法进行透明重实现，适合讨论专有处理指数的可解释性、局限与可复现性。 | [10.1213/ANE.0000000000006119](https://doi.org/10.1213/ANE.0000000000006119) | 未发现 |

### 2015

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2015 | Anesthesiology | [Clinical Electroencephalography for Anesthesiologists](https://doi.org/10.1097/ALN.0000000000000841)<br>面向麻醉专业人员的临床 EEG 教程，强调原始波形与谱图，而非只依赖单一指数。 | [10.1097/ALN.0000000000000841](https://doi.org/10.1097/ALN.0000000000000841) | 未发现 |

### 2013

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2013 | Proceedings of the National Academy of Sciences | [Electroencephalogram signatures of loss and recovery of consciousness from propofol](https://doi.org/10.1073/pnas.1221180110)<br>描述丙泊酚诱导意识消失和恢复时的典型 EEG 频谱与相干变化。 | [10.1073/pnas.1221180110](https://doi.org/10.1073/pnas.1221180110) | 未发现 |

### 2010

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2010 | New England Journal of Medicine | [General Anesthesia, Sleep, and Coma](https://doi.org/10.1056/NEJMra0808281)<br>从神经回路和脑状态角度比较麻醉、睡眠与昏迷，是理解麻醉 EEG 的重要概念入口。 | [10.1056/NEJMra0808281](https://doi.org/10.1056/NEJMra0808281) | 未发现 |

## 维护与复核

```bash
eeg-catalog --online
python scripts/render_literature.py --check
```

第一条命令通过 Crossref/DataCite 重查 DOI、标题和年份；第二条命令确认 README 与本页没有偏离机器目录。
