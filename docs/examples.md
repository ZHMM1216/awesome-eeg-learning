# 可运行案例

所有示例默认只下载一名受试者或少量记录。运行前先读对应专题页，运行后必须检查图和数据摘要，不要只看终端最后一个数字。

## 建议运行顺序

| Level | Command | 你应看到 | 对应知识 |
|---:|---|---|---|
| 1 | `python examples/alpha_eyes_open_closed.py --subject 1` | 闭眼相对 Alpha 常高于睁眼 | Raw、PSD、相对功率 |
| 2 | `python examples/motor_imagery_csp.py --subject 1` | CSP+LDA 的折间性能分布 | Epoch、CSP、Group CV |
| 3 | `python examples/clinical/sleep_edf_baseline.py` | 频谱特征和五分类评估 | 30 秒 Epoch、Macro-F1 |
| 4 | `python examples/clinical/chbmit_event_metrics.py` | 事件敏感度、误报/小时、延迟 | 连续检测与事件后处理 |
| 5 | `python examples/clinical/anesthesia_spectral_features.py` | 频带功率、SEF 等透明特征 | 频谱图和状态时间轴 |

## 每次运行后的四个动作

1. 打印数据形状和标签数，确认 Trial/窗口不是异常膨胀。
2. 保存一张原始波形或完整时间轴图。
3. 改一个参数，并写出你预期它怎样影响结果。
4. 记录失败的人、折或阶段，不只复制平均分。

## Quickstart Notebook

`notebooks/00_quickstart_alpha.ipynb` 适合第一次交互式运行。Notebook 用于学习和探索；形成正式实验后，应把关键处理变成可测试脚本和配置，避免隐藏状态与手动执行顺序。

## 数据访问

需要注册的数据不会自动绕过官方流程。运行 `eeg-data` 查看所有数据集，或运行 `eeg-data chbmit` 查看单个数据集的许可、格式和访问说明。

!!! tip "把示例变成自己的实验"
    先复制实验配置而不是复制整段代码。明确输入数据、问题、划分和指标，再替换数据加载器；保留原来的最小基线作为回归检查。
