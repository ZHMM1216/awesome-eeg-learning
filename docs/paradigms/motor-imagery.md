# 运动想象

运动想象不是“脑中有一段动作影片”这么简单。想象左右手运动时，感觉运动区 Mu/Beta 节律可出现事件相关去同步/同步（ERD/ERS），空间分布通常具有对侧倾向，但个体差异很大。

<div class="concept-figure" markdown="1">
![运动想象期间对侧与同侧 Mu Beta 功率变化概念图](../assets/figures/motor-imagery-erd.svg)
<small>颜色表示相对基线的功率变化；任务期间对侧 Mu/Beta ERD 通常更明显。</small>
</div>

### 时频图的三个坐标

- 横轴：相对提示的时间，0 秒前通常用作基线或准备期。
- 纵轴：频率，Mu 约 8–13 Hz，Beta 常约 13–30 Hz，但个体边界不同。
- 颜色：相对基线功率；必须看色条确认负值是否表示 ERD。

## 范式结构

| 阶段 | 常见时长 | 分析意义 |
|---|---:|---|
| 静息 | 2–3 秒 | 建立节律基线 |
| 提示 | 0.5–1 秒 | 告知左右手/脚/舌任务 |
| 想象 | 3–5 秒 | 主要解码窗口 |
| 间隔 | 2–4 秒 | 减少连续 Trial 相互影响 |

动作执行与动作想象必须分开标记。卒中患者还要记录患侧、优势手、病灶、发病时间和是否能够理解任务。

## 经典分析路线

1. 在 C3/C4/Cz 附近画 8–30 Hz 时频图，先观察 ERD/ERS。
2. 用训练数据选择 Mu/Beta 频带，避免根据测试结果调频段。
3. 计算正则化 CSP 空间滤波和对数方差特征。
4. 使用 LDA 或 Logistic Regression 建立基线。
5. 分别报告同一会话、跨会话和跨受试者结果；三者不能直接比较。

运行公开数据示例：

```bash
python examples/motor_imagery_csp.py --subject 1
```

## 正确评估

- 同一 Trial 的重叠窗口必须在同一数据折中。
- 所有滤波器、CSP 和标准化都应在每个训练折内拟合。
- 二分类优先报告 Balanced Accuracy；多分类同时报告 Macro-F1 和混淆矩阵。
- 组间比较应展示每位受试者分布，而不只报告所有 Trial 汇总值。

## 从健康 BCI 到卒中

健康受试者上可解码不等于卒中患者上可用；患者解码准确也不等于康复有效。继续学习时进入[卒中专题](../stroke.md)，把患者特征、临床量表、纵向变化和干预结局纳入设计。

## 代表论文

| Year | Paper | Interpretation | DOI | Code |
|---:|---|---|---|---|
| 2001 | Pfurtscheller & Neuper, *Motor imagery and direct brain-computer communication* | 运动想象、ERD/ERS 与反馈训练经典综述 | [10.1109/5.939829](https://doi.org/10.1109/5.939829) | 未发现 |
| 2018 | Cervera et al., *BCIs for post-stroke motor rehabilitation* | 区分 BCI 解码与康复临床证据 | [10.1002/acn3.544](https://doi.org/10.1002/acn3.544) | 未发现 |
| 2024 | Liu et al., acute stroke MI dataset | 可直接练习的急性卒中数据 | [10.1038/s41597-023-02787-8](https://doi.org/10.1038/s41597-023-02787-8) | [MOABB 接入](https://moabb.neurotechx.com/docs/generated/moabb.datasets.Liu2024.html) |
| 2025 | Kien et al., UET175 | 越南卒中患者多肢体运动想象 | [10.3389/fnins.2025.1580931](https://doi.org/10.3389/fnins.2025.1580931) | [作者代码](https://github.com/nmk-k66-uet/UET175) |

??? question "完成本节前自测"
    - CSP 为什么要放在交叉验证训练折内？它使用类别标签学习空间滤波器。
    - 同一 Trial 切出的重叠窗口能否分到不同折？不能，它们共享大量样本。
    - 没有明显对侧 ERD 是否说明受试者“没有运动意图”？不能，任务执行、频段、电极、噪声和个体差异都需检查。
