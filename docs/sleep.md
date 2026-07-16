# 睡眠分期

标准睡眠分期把多导睡眠记录切成 30 秒 Epoch，结合 EEG、EOG 和下颏 EMG 标为 Wake、N1、N2、N3 或 REM。Sleep-EDF 使用历史 R&K 标注，映射到现代五分类时必须公开合并规则。

<div class="concept-figure" markdown="1">
![概念性整夜睡眠 Hypnogram](assets/figures/sleep-hypnogram.svg)
<small>单个 Epoch 分类只是局部判断；整夜 Hypnogram 才能检查转换、周期和异常跳变。</small>
</div>

### 为什么需要上下文

相邻睡眠阶段不是独立抽签。N2 往往持续一段时间，REM 常随夜晚推进发生变化，N1 又常出现在阶段转换处。序列模型可利用这种结构，但也可能过度依赖数据集特定的阶段转移模式，因此仍需跨中心验证。

## 各阶段的学习线索

| Stage | 常见线索 | 初学者注意 |
|---|---|---|
| Wake | Alpha、眼动、较高肌张力 | 闭眼清醒可能很像入睡前段 |
| N1 | Alpha 减弱、低幅混合频率 | 边界模糊且一致性通常较低 |
| N2 | 睡眠纺锤、K 复合波 | 单导 EEG 也可见，但检测有不确定性 |
| N3 | 高幅慢波占比增加 | 滤波和幅值标定会影响判断 |
| REM | 低幅混合 EEG、快速眼动、低肌张力 | 仅用 EEG 时更难区分 Wake/N1 |

## 数据和标签

[Sleep-EDF Expanded](https://physionet.org/content/sleep-edfx/1.0.0/)包含 197 个 PSG 记录，适合第一个完整夜晚的流程。每个 PSG 文件必须与对应 Hypnogram 对齐；Subject、Night、Record 三个层级要单独保留。

## 第一条可复现路线

1. 读取一晚 PSG 与 Hypnogram，检查起始时间、持续时间和采样率。
2. 显式映射 R&K 标签；记录是否合并 Stage 3/4、如何处理 Movement/Unknown。
3. 只在预先定义的范围裁剪长时间 Wake，避免为了平衡类别任意删除。
4. 每 30 秒提取 Delta/Theta/Alpha/Sigma/Beta 相对功率、谱熵和比值。
5. 按受试者拆分，训练随机森林或梯度提升透明基线。
6. 报告 Macro-F1、Cohen's κ、逐阶段召回、混淆矩阵和整夜 Hypnogram。

运行仓库特征示例：

```bash
python examples/clinical/sleep_stage_features.py
```

## 从单 Epoch 到序列模型

| Level | 模型 | 学习重点 |
|---:|---|---|
| 1 | 频谱特征 + 随机森林 | 标签、受试者级划分、可解释特征 |
| 2 | 单 Epoch CNN | 原始信号与频谱表示的差别 |
| 3 | CNN + RNN / Transformer | 相邻阶段转换与上下文 |
| 4 | 多数据集训练 | 导联、人群、设备和评分者泛化 |

序列上下文不能跨夜晚边界，也不能在切分前把相邻 Epoch 打乱。用于标准化的统计量只能从训练受试者估计。

## 必读论文与代码

| Year | Venue | Paper and interpretation | DOI | Code |
|---:|---|---|---|---|
| 2017 | IEEE TNSRE | DeepSleepNet：多尺度 CNN 与双向循环网络的代表方法 | [10.1109/TNSRE.2017.2721116](https://doi.org/10.1109/TNSRE.2017.2721116) | [作者代码](https://github.com/akaraspt/deepsleepnet) |
| 2021 | npj Digital Medicine | U-Sleep：强调多中心训练与跨数据泛化 | [10.1038/s41746-021-00440-5](https://doi.org/10.1038/s41746-021-00440-5) | [作者代码](https://github.com/perslev/U-Time) |
| 2021 | eLife | YASA：易用的开放自动分期工具，适合教学对照 | [10.7554/eLife.70092](https://doi.org/10.7554/eLife.70092) | [作者代码](https://github.com/raphaelvallat/yasa) |
| 2022 | IEEE TBME | SleepTransformer：序列建模、解释与不确定性 | [10.1109/TBME.2022.3147187](https://doi.org/10.1109/TBME.2022.3147187) | [作者代码](https://github.com/pquochuy/SleepTransformer) |
| 2025 | npj Digital Medicine | SLEEPYLAND：公平、多中心和外部分布评价 | [10.1038/s41746-025-02237-2](https://doi.org/10.1038/s41746-025-02237-2) | 未发现 |

!!! warning "工具不是评分者"
    YASA 或任何自动模型的输出适合教学和研究比较，不替代有资质睡眠技师依据完整 PSG 进行的临床评分。

??? question "完成本节前自测"
    - 为什么不能随机拆分 30 秒 Epoch？同一夜晚相邻 Epoch 高度相关，会泄漏个体和夜晚结构。
    - 为什么 Macro-F1 比总 Accuracy 更重要？它让少数且困难的 N1 等阶段获得同等权重。
    - 为什么还要画 Hypnogram？它能发现不合理快速跳变和整夜结构错误。
