# 睡眠分期

标准睡眠分期把多导睡眠记录切为 30 秒 Epoch，并结合 EEG、EOG、下颏 EMG 等信号标为 Wake、N1、N2、N3 或 REM。Sleep-EDF 的历史标注使用 R&K 标准，需要在映射到现代五分类时明确合并规则。

## 首个实验

1. 读取 Sleep-EDF PSG 与对应 Hypnogram。
2. 对齐标注，裁剪过长清醒段，映射阶段。
3. 提取 Delta/Theta/Alpha/Sigma/Beta 功率和比值。
4. 按受试者拆分，训练随机森林。
5. 报告 Macro-F1、κ、逐阶段召回和混淆矩阵。

之后可与 YASA 进行教学性比较，再阅读 DeepSleepNet、U-Sleep 和 SleepTransformer。不要在全部 30 秒片段上随机划分后宣称获得跨患者性能。

