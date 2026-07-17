# 从脑电波形到可复现研究

Awesome EEG Learning 是一套中文优先、科研规范优先的 EEG 入门项目。你会先用经典范式建立“任务—信号—分析”的直觉，再进入卒中、癫痫、睡眠分期和麻醉等临床方向。

[开始学习](getting-started.md){ .md-button .md-button--primary }
[浏览全部论文](literature.md){ .md-button }
[打开 GitHub](https://github.com/ZHMM1216/awesome-eeg-learning){ .md-button }

## 先用图建立直觉

如果你是第一次接触 EEG，不要从模型公式开始。先完成三件事：

1. 浏览[EEG 可视化图谱](visual-atlas.md)，学会读电极、伪迹、PSD、ERP、时频图、模型阶梯和临床时间线。
2. 打开[采样与混叠实验室](labs/sampling.md)，拖动参数理解 Nyquist 条件。
3. 遇到陌生词时查[初学者术语表](glossary.md)，再回到具体范式。

![常用 EEG 10–20 电极示意图](assets/figures/electrode-map.svg)

*图解：先把范式与通道位置联系起来，再理解为什么不能从头皮电位直接跳到脑源结论。*

!!! warning "仅限教学科研"
    本项目不是医疗器械，不能用于诊断、治疗、麻醉给药或患者监护。临床 EEG 必须由具备资质的专业人员结合完整临床信息解释。

## 项目学习地图

| 层级 | 专题 | 核心现象 | 推荐基线 | 学习成果 |
|---|---|---|---|---|
| 信号基础 | [睁闭眼 Alpha](paradigms/alpha.md) | 闭眼时枕区 Alpha 增强 | Welch PSD | 完成第一张可解释 EEG 图 |
| 静息态 | [静息态 EEG](paradigms/resting-state.md) | 峰、1/f、连接与微状态 | 谱参数化 | 区分特征与生物标志物 |
| 事件相关 | [Oddball / P300](paradigms/p300.md) | 稀有目标诱发正向 ERP | xDAWN + LDA | 掌握事件、Epoch 与 ERP |
| 听觉范式 | [MMN / ASSR](paradigms/mmn-assr.md) | 变化检测与频率跟随 | 差异 ERP / 频谱 | 区分瞬态与稳态响应 |
| 频率标记 | [SSVEP](paradigms/ssvep.md) | 枕区跟随刺激频率 | CCA | 理解频谱与谐波 |
| 节律解码 | [运动想象](paradigms/motor-imagery.md) | Mu/Beta ERD/ERS | CSP + LDA | 完成受试者级 BCI 评估 |
| 认知 ERP | [ERN / N170](paradigms/ern-n170.md) | 错误与人脸加工成分 | 条件平均 | 理解刺激锁定与反应锁定 |
| 临床研究 | [卒中](stroke.md) | 运动网络改变 | 患者内/跨患者模型 | 区分解码性能与康复疗效 |
| 临床监测 | [癫痫](epilepsy.md) | 发作事件与异常波形 | 特征模型 + 事件后处理 | 正确报告误报/小时和延迟 |
| 生理状态 | [睡眠分期](sleep.md) | 睡眠结构与阶段转换 | 频谱特征 + RF | 完成整夜受试者级五分类 |
| 意识状态 | [麻醉](anesthesia.md) | 药物特异频谱与爆发抑制 | 频谱图 + 透明指标 | 理解麻醉 EEG 的边界 |
| 连续监测 | [重症与新生儿](critical-care.md) | 背景、模式、发作负荷 | 事件时间线 | 连接术语、负荷和临床语境 |
| 临床静息态 | [神经退行性疾病](neurodegeneration.md) | 减慢、复杂度与同步变化 | 正则线性模型 | 识别年龄/设备/窗口泄漏 |

## 推荐的 12 周入门路径

完整训练营把任务拆成“会看信号—会回答实验问题—会做可信研究”三个里程碑，每周都有可验收交付物。

[打开 12 周训练营](study-plan.md){ .md-button .md-button--primary }
[先学预处理](methods/preprocessing.md){ .md-button }

## 你会真正学会什么

- 理解 10–20 电极系统、参考、体积传导、采样率和常见伪迹。
- 用 MNE 读取 EDF、BrainVision、EEGLAB 和 EEG-BIDS 数据。
- 从原始波形走到 PSD、ERP、头皮图、时频图和经典机器学习。
- 复现静息态、P300、SSVEP、运动想象、ERN、N170、MMN 和 ASSR 等经典范式。
- 理解临床研究中标签、数据单位、任务终点和评价指标的差别。
- 理解连接性、源定位、微状态、自监督预训练及其证据边界。
- 避免窗口级随机划分、测试集调参、伪重复和只报告 Accuracy。

## 三条使用原则

1. **先看波形，再算特征。** 自动模型不能代替数据质控。
2. **先按人划分，再切窗口。** 同一患者或受试者的片段不得跨训练集和测试集。
3. **先做透明基线，再上深度网络。** 只有这样才能知道性能来自信号还是数据泄漏。
