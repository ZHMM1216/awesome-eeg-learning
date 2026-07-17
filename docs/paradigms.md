# 经典 EEG 范式总览

经典范式不是“要背的名词”，而是学习 EEG 分析的实验室。每个范式只突出一个相对清楚的信号结构，让你逐步掌握频谱、ERP、时频和解码。

## 一张表选学习入口

| 范式 | 典型任务 | 预期 EEG | 关键通道/频段 | 第一种分析 | 难度 |
|---|---|---|---|---|---|
| [睁闭眼 Alpha](paradigms/alpha.md) | 交替睁眼、闭眼 | 闭眼 Alpha 增强 | O1/O2/Oz，8–13 Hz | Welch PSD | ★ |
| [静息态 EEG](paradigms/resting-state.md) | 安静睁眼/闭眼 | 峰、1/f、微状态与连接 | 全头，重点后部 Alpha | 谱参数化 | ★★ |
| [Oddball / P300](paradigms/p300.md) | 识别稀有目标 | 约 250–500 ms 正波 | Pz/CPz/Cz | 条件 ERP | ★★ |
| [SSVEP](paradigms/ssvep.md) | 注视不同频率闪烁 | 同频及谐波峰 | 枕区，刺激频率 | PSD / CCA | ★★ |
| [运动想象](paradigms/motor-imagery.md) | 想象左右手运动 | 对侧 Mu/Beta ERD/ERS | C3/C4/Cz，8–30 Hz | 时频 / CSP | ★★★ |
| [Flanker / ERN](paradigms/ern-n170.md#flanker-ern) | 快速反应并产生错误 | 错误后负向成分 | FCz/Cz，约 0–100 ms | 反应锁定 ERP | ★★★ |
| [人脸 N170](paradigms/ern-n170.md#n170) | 人脸与非人脸判断 | 枕颞负向成分 | P7/P8/PO7/PO8，约 170 ms | 刺激锁定 ERP | ★★ |
| [MMN](paradigms/mmn-assr.md#mmn) | 标准音中插入偏差音 | 约 100–250 ms 差异负波 | Fz/FCz/Cz | 偏差−标准 ERP | ★★ |
| [ASSR](paradigms/mmn-assr.md#assr) | 周期点击或调幅音 | 刺激频率跟随 | 额中央/颞区 | 频谱 / ITPC | ★★ |

## 每个范式都要回答的 7 个问题

1. 操纵的实验变量是什么，对照条件是什么？
2. 事件码是否真的与刺激或反应时间对齐？
3. 预期成分出现在哪些通道、频段和时间窗？
4. 预处理的每一步会保留或破坏什么信号？
5. 分析单位是 Trial、Session 还是 Subject？
6. 基线模型是否比复杂模型更容易解释？
7. 结果可以支持“存在条件差异”，还是支持“可以泛化解码”？

## 推荐顺序

先完成 Alpha，再在 P300 和 SSVEP 中任选一个，随后学习运动想象。ERN/N170 用来巩固事件设计和 ERP 解释。进入临床任务前，至少完整复现一个频谱范式和一个 ERP 范式。

!!! tip "学习完成的标准"
    不以“代码能运行”为标准。你应能画出预期信号、解释每个处理参数、给出正确的数据划分，并主动展示至少一个失败案例。
