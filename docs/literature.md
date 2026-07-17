# EEG 精选论文库

这里从 `catalog/papers.yml` 自动生成 **57 篇**论文的可浏览列表。每条记录都包含真实 DOI、中文导读和代码关系；不要直接手改本页表格。

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
| 2023 | Scientific Data | [DISCOVER-EEG: an open, fully automated EEG pipeline for biomarker discovery in clinical neuroscience](https://doi.org/10.1038/s41597-023-02525-0)<br>面向临床神经科学生物标志物发现的自动化静息态 EEG 流程，适合参考质控和批处理设计。 | [10.1038/s41597-023-02525-0](https://doi.org/10.1038/s41597-023-02525-0) | [作者代码](https://github.com/crisglav/discover-eeg) |

### 2019

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2019 | Scientific Data | [EEG-BIDS, an extension to the brain imaging data structure for electroencephalography](https://doi.org/10.1038/s41597-019-0104-8)<br>EEG-BIDS 标准论文，规定可共享、可机器读取的 EEG 数据与事件元数据结构。 | [10.1038/s41597-019-0104-8](https://doi.org/10.1038/s41597-019-0104-8) | [相关实现](https://github.com/mne-tools/mne-bids) |

### 2013

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2013 | Frontiers in Neuroscience | [MEG and EEG data analysis with MNE-Python](https://doi.org/10.3389/fnins.2013.00267)<br>本项目所采用的 Python EEG/MEG 分析主工具，覆盖读取、预处理、可视化、统计和解码。 | [10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267) | [作者代码](https://github.com/mne-tools/mne-python) |

### 2012

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2012 | IEEE Transactions on Biomedical Engineering | [Multiclass Brain-Computer Interface Classification by Riemannian Geometry](https://doi.org/10.1109/TBME.2011.2172210)<br>协方差矩阵与黎曼几何 BCI 分类的代表性工作，是 CSP+LDA 之外的重要透明基线。 | [10.1109/TBME.2011.2172210](https://doi.org/10.1109/TBME.2011.2172210) | [相关实现](https://github.com/pyRiemann/pyRiemann) |

### 2004

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2004 | Journal of Neuroscience Methods | [EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis](https://doi.org/10.1016/j.jneumeth.2003.10.009)<br>EEGLAB 工具箱论文，推动了单试次 EEG、ICA 和可复现分析流程的普及。 | [10.1016/j.jneumeth.2003.10.009](https://doi.org/10.1016/j.jneumeth.2003.10.009) | [作者代码](https://github.com/sccn/eeglab) |

### 2000

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2000 | Psychophysiology | [Removing electroencephalographic artifacts by blind source separation](https://doi.org/10.1111/1469-8986.3720163)<br>ICA 去除眼动、肌电等混合伪迹的经典工作；实际使用必须记录成分判定和删除依据，并比较清理前后信号。 | [10.1111/1469-8986.3720163](https://doi.org/10.1111/1469-8986.3720163) | 未发现 |

### 1999

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1999 | Brain Research Reviews | [EEG alpha and theta oscillations reflect cognitive and memory performance: a review and analysis](https://doi.org/10.1016/S0165-0173(98)00056-3)<br>Alpha/Theta 与认知和记忆关系的经典综述，是理解个体 Alpha 峰及任务相关节律变化的概念入口。 | [10.1016/S0165-0173(98)00056-3](https://doi.org/10.1016/S0165-0173(98)00056-3) | 未发现 |

### 1967

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1967 | IEEE Transactions on Audio and Electroacoustics | [The use of fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms](https://doi.org/10.1109/TAU.1967.1161901)<br>Welch 功率谱估计的经典论文，是 EEG 频带功率和功率谱密度分析的基础。 | [10.1109/TAU.1967.1161901](https://doi.org/10.1109/TAU.1967.1161901) | 未发现 |

### 1929

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1929 | Archiv für Psychiatrie und Nervenkrankheiten | [Über das Elektrenkephalogramm des Menschen](https://doi.org/10.1007/BF01797193)<br>人体脑电研究的奠基性工作。适合了解 EEG 的历史起点，而不是直接作为现代分析规范使用。 | [10.1007/BF01797193](https://doi.org/10.1007/BF01797193) | 未发现 |

## 预处理与质量控制

从坏导、参考和滤波走到伪迹标记、ICA 与可审计质控。

### 2022

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2022 | Developmental Cognitive Neuroscience | [The HAPPE plus Event-Related (HAPPE+ER) software: A standardized preprocessing pipeline for event-related potential analyses](https://doi.org/10.1016/j.dcn.2022.101140)<br>面向 ERP 的标准化预处理流程，尤其适合高伪迹人群；使用时仍要按自身范式审查默认参数。 | [10.1016/j.dcn.2022.101140](https://doi.org/10.1016/j.dcn.2022.101140) | [作者代码](https://github.com/PINE-Lab/HAPPE) |

### 2019

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2019 | NeuroImage | [ICLabel: An automated electroencephalographic independent component classifier, dataset, and website](https://doi.org/10.1016/j.neuroimage.2019.05.026)<br>自动标注 ICA 成分为脑、眼、肌肉等类别；概率输出用于辅助审核，不能代替对拓扑、频谱和时程的检查。 | [10.1016/j.neuroimage.2019.05.026](https://doi.org/10.1016/j.neuroimage.2019.05.026) | [作者代码](https://github.com/sccn/ICLabel) |

### 2017

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2017 | NeuroImage | [Autoreject: Automated artifact rejection for MEG and EEG data](https://doi.org/10.1016/j.neuroimage.2017.06.030)<br>通过交叉验证学习通道级峰峰值阈值并修复或拒绝 Epoch，适合作为人工阈值之外的可复现方案。 | [10.1016/j.neuroimage.2017.06.030](https://doi.org/10.1016/j.neuroimage.2017.06.030) | [作者代码](https://github.com/autoreject/autoreject) |

### 2015

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2015 | Frontiers in Neuroinformatics | [PREP pipeline: standardized preprocessing for large-scale EEG analysis](https://doi.org/10.3389/fninf.2015.00016)<br>提出稳健参考、工频处理和坏导识别的标准化流程，适合学习“自动化仍需质控报告”的原则。 | [10.3389/fninf.2015.00016](https://doi.org/10.3389/fninf.2015.00016) | [作者代码](https://github.com/VisLab/EEG-Clean-Tools) |

### 2000

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2000 | Psychophysiology | [Removing electroencephalographic artifacts by blind source separation](https://doi.org/10.1111/1469-8986.3720163)<br>ICA 去除眼动、肌电等混合伪迹的经典工作；实际使用必须记录成分判定和删除依据，并比较清理前后信号。 | [10.1111/1469-8986.3720163](https://doi.org/10.1111/1469-8986.3720163) | 未发现 |

## ERP 与时频分析

理解事件锁定平均、基线、诱发/非相位锁定活动与多重比较。

### 2022

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2022 | Developmental Cognitive Neuroscience | [The HAPPE plus Event-Related (HAPPE+ER) software: A standardized preprocessing pipeline for event-related potential analyses](https://doi.org/10.1016/j.dcn.2022.101140)<br>面向 ERP 的标准化预处理流程，尤其适合高伪迹人群；使用时仍要按自身范式审查默认参数。 | [10.1016/j.dcn.2022.101140](https://doi.org/10.1016/j.dcn.2022.101140) | [作者代码](https://github.com/PINE-Lab/HAPPE) |

### 2017

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2017 | NeuroImage | [Autoreject: Automated artifact rejection for MEG and EEG data](https://doi.org/10.1016/j.neuroimage.2017.06.030)<br>通过交叉验证学习通道级峰峰值阈值并修复或拒绝 Epoch，适合作为人工阈值之外的可复现方案。 | [10.1016/j.neuroimage.2017.06.030](https://doi.org/10.1016/j.neuroimage.2017.06.030) | [作者代码](https://github.com/autoreject/autoreject) |

### 2007

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2007 | Clinical Neurophysiology | [The mismatch negativity (MMN) in basic research of central auditory processing: A review](https://doi.org/10.1016/j.clinph.2007.04.026)<br>系统梳理 MMN 的产生、范式变量和解释边界，适合在动手做听觉 Oddball 前建立分析框架。 | [10.1016/j.clinph.2007.04.026](https://doi.org/10.1016/j.clinph.2007.04.026) | 未发现 |

### 1978

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1978 | Acta Psychologica | [Early selective-attention effect on evoked potential reinterpreted](https://doi.org/10.1016/0001-6918(78)90006-9)<br>MMN 概念的早期奠基工作。入门时重点理解标准刺激、偏差刺激与差异波，而不是把一个负峰直接当作诊断指标。 | [10.1016/0001-6918(78)90006-9](https://doi.org/10.1016/0001-6918(78)90006-9) | 未发现 |

## 连接性、源定位与静息态

学习频谱参数化、功能连接、微状态和体积传导边界。

### 2018

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2018 | NeuroImage | [EEG microstates as a tool for studying the temporal dynamics of whole-brain neuronal networks: A review](https://doi.org/10.1016/j.neuroimage.2017.11.062)<br>EEG 微状态的经典综述，帮助理解毫秒尺度头皮拓扑序列及聚类、回配和重测信度问题。 | [10.1016/j.neuroimage.2017.11.062](https://doi.org/10.1016/j.neuroimage.2017.11.062) | 未发现 |

### 2011

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2011 | Computational Intelligence and Neuroscience | [FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data](https://doi.org/10.1155/2011/156869)<br>FieldTrip 工具箱论文，覆盖时频、源分析和连接性；适合与 MNE、EEGLAB 的教程交叉学习。 | [10.1155/2011/156869](https://doi.org/10.1155/2011/156869) | [作者代码](https://github.com/fieldtrip/fieldtrip) |
| 2011 | Computational Intelligence and Neuroscience | [Brainstorm: A User-Friendly Application for MEG/EEG Analysis](https://doi.org/10.1155/2011/879716)<br>以图形界面组织 MEG/EEG 预处理、源定位和组分析，适合初学者理解完整分析树和可追溯处理历史。 | [10.1155/2011/879716](https://doi.org/10.1155/2011/879716) | [作者代码](https://github.com/brainstorm-tools/brainstorm3) |

## 机器学习与基础模型

从透明线性基线走向深度网络、自监督预训练和外部验证。

### 2025

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2025 | Scientific Data | [A multi-day and high-quality EEG dataset for motor imagery brain-computer interface](https://doi.org/10.1038/s41597-025-04826-y)<br>多日、经过系统质控的运动想象数据，适合研究会话漂移、校准需求和跨天泛化，而不是随机混合所有试次。 | [10.1038/s41597-025-04826-y](https://doi.org/10.1038/s41597-025-04826-y) | [作者代码](https://doi.org/10.25452/figshare.plus.22671172) |

### 2024

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2024 | Advances in Neural Information Processing Systems | [EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals](https://doi.org/10.52202/079017-1239)<br>大规模 EEG 预训练 Transformer 的近年代表工作；复现时必须记录预训练语料重叠、通道映射和测试集隔离。 | [10.52202/079017-1239](https://doi.org/10.52202/079017-1239) | [作者代码](https://github.com/BINE022/EEGPT) |

### 2023

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2023 | NeuroImage | [Deep learning-based EEG analysis to classify normal, mild cognitive impairment, and dementia: Algorithms and dataset](https://doi.org/10.1016/j.neuroimage.2023.120054)<br>提出 CAUEEG 临床数据和端到端分类模型；入门复现应先检查年龄、诊断流程、划分单位与外部泛化。 | [10.1016/j.neuroimage.2023.120054](https://doi.org/10.1016/j.neuroimage.2023.120054) | [作者代码](https://github.com/ipis-mjkim/caueeg-ceednet) |
| 2023 | Scientific Data | [A large EEG database with users' profile information for motor imagery brain-computer interface research](https://doi.org/10.1038/s41597-023-02445-z)<br>87 名用户、超过 20,800 个试次并含用户画像，适合跨受试者算法和 BCI 个体差异研究。 | [10.1038/s41597-023-02445-z](https://doi.org/10.1038/s41597-023-02445-z) | 未发现 |

### 2022

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2022 | Scientific Data | [The two decades brainclinics research archive for insights in neurophysiology (TDBRAIN) database](https://doi.org/10.1038/s41597-022-01409-z)<br>1274 名参与者的临床生命周期 EEG 数据库，含睁闭眼、任务、人口学和临床信息，访问需注册并接受数据使用协议。 | [10.1038/s41597-022-01409-z](https://doi.org/10.1038/s41597-022-01409-z) | [作者代码](https://www.synapse.org/TDBRAIN) |

### 2021

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2021 | Frontiers in Neuroscience | [The NMT Scalp EEG Dataset: An Open-Source Annotated Dataset of Healthy and Pathological EEG Recordings for Predictive Modeling](https://doi.org/10.3389/fnins.2021.755817)<br>大型临床常规头皮 EEG 数据说明，适合研究正常/异常筛查，同时必须防止记录来源和患者身份泄漏。 | [10.3389/fnins.2021.755817](https://doi.org/10.3389/fnins.2021.755817) | 未发现 |
| 2021 | Frontiers in Human Neuroscience | [BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data](https://doi.org/10.3389/fnhum.2021.653659)<br>EEG 自监督预训练的早期代表工作，适合学习预训练数据、通道映射、下游微调和跨数据集迁移。 | [10.3389/fnhum.2021.653659](https://doi.org/10.3389/fnhum.2021.653659) | [作者代码](https://github.com/SPOClab-ca/BENDR) |

### 2017

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2017 | Human Brain Mapping | [Deep learning with convolutional neural networks for EEG decoding and visualization](https://doi.org/10.1002/hbm.23730)<br>EEG 深度解码与可视化的代表性工作；复现时应与 CSP、黎曼几何等基线使用同一受试者级划分比较。 | [10.1002/hbm.23730](https://doi.org/10.1002/hbm.23730) | [作者代码](https://github.com/braindecode/braindecode) |

## 静息态 EEG

学习睁闭眼、个体 Alpha 峰、周期/非周期成分与重测信度。

### 2024

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2024 | Scientific Data | [Resting-state EEG data before and after cognitive activity across the adult lifespan and a 5-year follow-up](https://doi.org/10.1038/s41597-024-03797-w)<br>608 名成人、其中 208 名约五年随访的 64 导静息态 BIDS 数据，适合学习年龄、疲劳和纵向变化。 | [10.1038/s41597-024-03797-w](https://doi.org/10.1038/s41597-024-03797-w) | 未发现 |

### 2023

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2023 | Data | [A Dataset of Scalp EEG Recordings of Alzheimer's Disease, Frontotemporal Dementia and Healthy Subjects from Routine EEG](https://doi.org/10.3390/data8060095)<br>88 名受试者的睁眼/闭眼静息态临床 EEG 数据说明，可在 OpenNeuro ds004504 获取；规模适合教学而不适合宣称临床诊断性能。 | [10.3390/data8060095](https://doi.org/10.3390/data8060095) | 未发现 |

### 2022

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2022 | Scientific Data | [The two decades brainclinics research archive for insights in neurophysiology (TDBRAIN) database](https://doi.org/10.1038/s41597-022-01409-z)<br>1274 名参与者的临床生命周期 EEG 数据库，含睁闭眼、任务、人口学和临床信息，访问需注册并接受数据使用协议。 | [10.1038/s41597-022-01409-z](https://doi.org/10.1038/s41597-022-01409-z) | [作者代码](https://www.synapse.org/TDBRAIN) |
| 2022 | Neurorehabilitation and Neural Repair | [The Prognostic Utility of Electroencephalography in Stroke Recovery: A Systematic Review and Meta-Analysis](https://doi.org/10.1177/15459683221078294)<br>汇总 EEG 与卒中恢复结局的关联证据；重点区分相关性、增量预后价值与真正可用于临床决策的外部验证。 | [10.1177/15459683221078294](https://doi.org/10.1177/15459683221078294) | 未发现 |

### 2020

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2020 | Nature Neuroscience | [Parameterizing neural power spectra into periodic and aperiodic components](https://doi.org/10.1038/s41593-020-00744-x)<br>将功率谱拆为周期峰和非周期背景，避免把 1/f 斜率变化误解为固定频带振荡变化。 | [10.1038/s41593-020-00744-x](https://doi.org/10.1038/s41593-020-00744-x) | [作者代码](https://github.com/fooof-tools/fooof) |

### 2018

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2018 | NeuroImage | [EEG microstates as a tool for studying the temporal dynamics of whole-brain neuronal networks: A review](https://doi.org/10.1016/j.neuroimage.2017.11.062)<br>EEG 微状态的经典综述，帮助理解毫秒尺度头皮拓扑序列及聚类、回配和重测信度问题。 | [10.1016/j.neuroimage.2017.11.062](https://doi.org/10.1016/j.neuroimage.2017.11.062) | 未发现 |

### 2004

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2004 | Clinical Neurophysiology | [EEG dynamics in patients with Alzheimer's disease](https://doi.org/10.1016/j.clinph.2004.01.001)<br>阿尔茨海默病 EEG 动力学经典综述，概括频谱减慢、复杂度和同步变化，同时提醒这些群体差异并不等于个体确诊。 | [10.1016/j.clinph.2004.01.001](https://doi.org/10.1016/j.clinph.2004.01.001) | 未发现 |

### 1999

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1999 | Brain Research Reviews | [EEG alpha and theta oscillations reflect cognitive and memory performance: a review and analysis](https://doi.org/10.1016/S0165-0173(98)00056-3)<br>Alpha/Theta 与认知和记忆关系的经典综述，是理解个体 Alpha 峰及任务相关节律变化的概念入口。 | [10.1016/S0165-0173(98)00056-3](https://doi.org/10.1016/S0165-0173(98)00056-3) | 未发现 |

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
| 2025 | Scientific Data | [A multi-day and high-quality EEG dataset for motor imagery brain-computer interface](https://doi.org/10.1038/s41597-025-04826-y)<br>多日、经过系统质控的运动想象数据，适合研究会话漂移、校准需求和跨天泛化，而不是随机混合所有试次。 | [10.1038/s41597-025-04826-y](https://doi.org/10.1038/s41597-025-04826-y) | [作者代码](https://doi.org/10.25452/figshare.plus.22671172) |

### 2024

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2024 | Scientific Data | [An EEG motor imagery dataset for brain computer interface in acute stroke patients](https://doi.org/10.1038/s41597-023-02787-8)<br>50 名急性卒中患者的左右手握持运动想象数据，含原始/预处理数据、提示和患者特征。 | [10.1038/s41597-023-02787-8](https://doi.org/10.1038/s41597-023-02787-8) | [相关实现](https://moabb.neurotechx.com/docs/generated/moabb.datasets.Liu2024.html) |

### 2023

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2023 | Scientific Data | [A large EEG database with users' profile information for motor imagery brain-computer interface research](https://doi.org/10.1038/s41597-023-02445-z)<br>87 名用户、超过 20,800 个试次并含用户画像，适合跨受试者算法和 BCI 个体差异研究。 | [10.1038/s41597-023-02445-z](https://doi.org/10.1038/s41597-023-02445-z) | 未发现 |

### 2018

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2018 | Journal of Neural Engineering | [EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces](https://doi.org/10.1088/1741-2552/aace8c)<br>紧凑型 EEG 深度网络，常作为跨范式基线；首学时仍应先掌握经典线性方法和正确划分。 | [10.1088/1741-2552/aace8c](https://doi.org/10.1088/1741-2552/aace8c) | [作者代码](https://github.com/vlawhern/arl-eegmodels) |
| 2018 | Annals of Clinical and Translational Neurology | [Brain-computer interfaces for post-stroke motor rehabilitation: a meta-analysis](https://doi.org/10.1002/acn3.544)<br>汇总 BCI 辅助卒中运动康复的临床证据，帮助区分解码性能与康复结局。 | [10.1002/acn3.544](https://doi.org/10.1002/acn3.544) | 未发现 |

### 2017

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2017 | Human Brain Mapping | [Deep learning with convolutional neural networks for EEG decoding and visualization](https://doi.org/10.1002/hbm.23730)<br>EEG 深度解码与可视化的代表性工作；复现时应与 CSP、黎曼几何等基线使用同一受试者级划分比较。 | [10.1002/hbm.23730](https://doi.org/10.1002/hbm.23730) | [作者代码](https://github.com/braindecode/braindecode) |

### 2012

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2012 | IEEE Transactions on Biomedical Engineering | [Multiclass Brain-Computer Interface Classification by Riemannian Geometry](https://doi.org/10.1109/TBME.2011.2172210)<br>协方差矩阵与黎曼几何 BCI 分类的代表性工作，是 CSP+LDA 之外的重要透明基线。 | [10.1109/TBME.2011.2172210](https://doi.org/10.1109/TBME.2011.2172210) | [相关实现](https://github.com/pyRiemann/pyRiemann) |

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

## MMN 与听觉 Oddball

学习被动听觉变化检测、差异波和前注意加工。

### 2007

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2007 | Clinical Neurophysiology | [The mismatch negativity (MMN) in basic research of central auditory processing: A review](https://doi.org/10.1016/j.clinph.2007.04.026)<br>系统梳理 MMN 的产生、范式变量和解释边界，适合在动手做听觉 Oddball 前建立分析框架。 | [10.1016/j.clinph.2007.04.026](https://doi.org/10.1016/j.clinph.2007.04.026) | 未发现 |

### 1978

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1978 | Acta Psychologica | [Early selective-attention effect on evoked potential reinterpreted](https://doi.org/10.1016/0001-6918(78)90006-9)<br>MMN 概念的早期奠基工作。入门时重点理解标准刺激、偏差刺激与差异波，而不是把一个负峰直接当作诊断指标。 | [10.1016/0001-6918(78)90006-9](https://doi.org/10.1016/0001-6918(78)90006-9) | 未发现 |

## 听觉稳态反应 ASSR

学习周期刺激、频率跟随、相位一致性和谐波。

### 1981

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 1981 | Proceedings of the National Academy of Sciences | [A 40-Hz auditory potential recorded from the human scalp](https://doi.org/10.1073/pnas.78.4.2643)<br>40 Hz 听觉稳态反应的经典论文，帮助理解周期刺激、频率跟随和相位一致性。 | [10.1073/pnas.78.4.2643](https://doi.org/10.1073/pnas.78.4.2643) | 未发现 |

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

### 2022

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2022 | Neurorehabilitation and Neural Repair | [The Prognostic Utility of Electroencephalography in Stroke Recovery: A Systematic Review and Meta-Analysis](https://doi.org/10.1177/15459683221078294)<br>汇总 EEG 与卒中恢复结局的关联证据；重点区分相关性、增量预后价值与真正可用于临床决策的外部验证。 | [10.1177/15459683221078294](https://doi.org/10.1177/15459683221078294) | 未发现 |

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

### 2021

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2021 | Frontiers in Neuroscience | [The NMT Scalp EEG Dataset: An Open-Source Annotated Dataset of Healthy and Pathological EEG Recordings for Predictive Modeling](https://doi.org/10.3389/fnins.2021.755817)<br>大型临床常规头皮 EEG 数据说明，适合研究正常/异常筛查，同时必须防止记录来源和患者身份泄漏。 | [10.3389/fnins.2021.755817](https://doi.org/10.3389/fnins.2021.755817) | 未发现 |
| 2021 | Journal of Clinical Neurophysiology | [American Clinical Neurophysiology Society's Standardized Critical Care EEG Terminology: 2021 Version](https://doi.org/10.1097/WNP.0000000000000806)<br>重症连续 EEG 的标准术语，定义背景、周期/节律放电、爆发抑制与发作等报告语言，但不把术语自动等同于病因或治疗决策。 | [10.1097/WNP.0000000000000806](https://doi.org/10.1097/WNP.0000000000000806) | 未发现 |

### 2019

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2019 | Scientific Data | [A dataset of neonatal EEG recordings with seizure annotations](https://doi.org/10.1038/sdata.2019.39)<br>79 名足月新生儿、多专家独立发作标注的数据说明，适合学习标签不确定性和观察者一致性。 | [10.1038/sdata.2019.39](https://doi.org/10.1038/sdata.2019.39) | [作者代码](https://github.com/ktapani/Neonatal_Seizure_Detection) |

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

## 重症监护 EEG

学习连续 EEG 术语、时间轴、周期/节律模式和临床语境。

### 2021

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2021 | Frontiers in Neuroscience | [The NMT Scalp EEG Dataset: An Open-Source Annotated Dataset of Healthy and Pathological EEG Recordings for Predictive Modeling](https://doi.org/10.3389/fnins.2021.755817)<br>大型临床常规头皮 EEG 数据说明，适合研究正常/异常筛查，同时必须防止记录来源和患者身份泄漏。 | [10.3389/fnins.2021.755817](https://doi.org/10.3389/fnins.2021.755817) | 未发现 |
| 2021 | Journal of Clinical Neurophysiology | [American Clinical Neurophysiology Society's Standardized Critical Care EEG Terminology: 2021 Version](https://doi.org/10.1097/WNP.0000000000000806)<br>重症连续 EEG 的标准术语，定义背景、周期/节律放电、爆发抑制与发作等报告语言，但不把术语自动等同于病因或治疗决策。 | [10.1097/WNP.0000000000000806](https://doi.org/10.1097/WNP.0000000000000806) | 未发现 |

### 2019

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2019 | Scientific Data | [A dataset of neonatal EEG recordings with seizure annotations](https://doi.org/10.1038/sdata.2019.39)<br>79 名足月新生儿、多专家独立发作标注的数据说明，适合学习标签不确定性和观察者一致性。 | [10.1038/sdata.2019.39](https://doi.org/10.1038/sdata.2019.39) | [作者代码](https://github.com/ktapani/Neonatal_Seizure_Detection) |

## 新生儿 EEG

学习年龄相关背景、发作标注一致性和 NICU 连续监测。

### 2019

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2019 | Scientific Data | [A dataset of neonatal EEG recordings with seizure annotations](https://doi.org/10.1038/sdata.2019.39)<br>79 名足月新生儿、多专家独立发作标注的数据说明，适合学习标签不确定性和观察者一致性。 | [10.1038/sdata.2019.39](https://doi.org/10.1038/sdata.2019.39) | [作者代码](https://github.com/ktapani/Neonatal_Seizure_Detection) |

## 神经退行性疾病

学习静息态减慢、混杂控制、筛查与诊断边界。

### 2024

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2024 | Scientific Data | [Resting-state EEG data before and after cognitive activity across the adult lifespan and a 5-year follow-up](https://doi.org/10.1038/s41597-024-03797-w)<br>608 名成人、其中 208 名约五年随访的 64 导静息态 BIDS 数据，适合学习年龄、疲劳和纵向变化。 | [10.1038/s41597-024-03797-w](https://doi.org/10.1038/s41597-024-03797-w) | 未发现 |

### 2023

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2023 | NeuroImage | [Deep learning-based EEG analysis to classify normal, mild cognitive impairment, and dementia: Algorithms and dataset](https://doi.org/10.1016/j.neuroimage.2023.120054)<br>提出 CAUEEG 临床数据和端到端分类模型；入门复现应先检查年龄、诊断流程、划分单位与外部泛化。 | [10.1016/j.neuroimage.2023.120054](https://doi.org/10.1016/j.neuroimage.2023.120054) | [作者代码](https://github.com/ipis-mjkim/caueeg-ceednet) |
| 2023 | Data | [A Dataset of Scalp EEG Recordings of Alzheimer's Disease, Frontotemporal Dementia and Healthy Subjects from Routine EEG](https://doi.org/10.3390/data8060095)<br>88 名受试者的睁眼/闭眼静息态临床 EEG 数据说明，可在 OpenNeuro ds004504 获取；规模适合教学而不适合宣称临床诊断性能。 | [10.3390/data8060095](https://doi.org/10.3390/data8060095) | 未发现 |

### 2022

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2022 | Scientific Data | [The two decades brainclinics research archive for insights in neurophysiology (TDBRAIN) database](https://doi.org/10.1038/s41597-022-01409-z)<br>1274 名参与者的临床生命周期 EEG 数据库，含睁闭眼、任务、人口学和临床信息，访问需注册并接受数据使用协议。 | [10.1038/s41597-022-01409-z](https://doi.org/10.1038/s41597-022-01409-z) | [作者代码](https://www.synapse.org/TDBRAIN) |

### 2004

| Year | Venue | Paper Title and Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2004 | Clinical Neurophysiology | [EEG dynamics in patients with Alzheimer's disease](https://doi.org/10.1016/j.clinph.2004.01.001)<br>阿尔茨海默病 EEG 动力学经典综述，概括频谱减慢、复杂度和同步变化，同时提醒这些群体差异并不等于个体确诊。 | [10.1016/j.clinph.2004.01.001](https://doi.org/10.1016/j.clinph.2004.01.001) | 未发现 |

## 维护与复核

```bash
eeg-catalog --online
python scripts/render_literature.py --check
```

第一条命令通过 Crossref/DataCite 重查 DOI、标题和年份；第二条命令确认 README 与本页没有偏离机器目录。
