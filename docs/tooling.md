# EEG 工具与数据标准

不要同时学完所有工具。先选一个主工具完成端到端流程，再用第二个工具复核关键结果。

## 工具地图

| 工具 | 语言/界面 | 强项 | 适合谁 | 官方入口 |
|---|---|---|---|---|
| MNE-Python | Python | 读取、预处理、统计、解码、源定位 | 想要可测试脚本的初学者 | [mne.tools](https://mne.tools/) |
| EEGLAB | MATLAB GUI/脚本 | ICA、事件和插件生态 | 希望可视化操作并逐步脚本化 | [sccn.ucsd.edu/eeglab](https://sccn.ucsd.edu/eeglab/) |
| FieldTrip | MATLAB 脚本 | 时频、连接性、源分析 | 进阶方法与定制分析 | [fieldtriptoolbox.org](https://www.fieldtriptoolbox.org/) |
| Brainstorm | MATLAB GUI | 分析树、MEG/EEG 源定位 | 重视图形工作流和审计历史 | [neuroimage.usc.edu/brainstorm](https://neuroimage.usc.edu/brainstorm/) |
| Braindecode | Python/PyTorch | 深度学习与滑窗数据集 | 已掌握 EEG 基线后做深度模型 | [braindecode.org](https://braindecode.org/) |
| MOABB | Python | 公共 BCI 数据和统一评估 | 比较算法与数据集泛化 | [moabb.neurotechx.com](https://moabb.neurotechx.com/) |
| YASA | Python | 睡眠特征与自动分期 | 睡眠教学和基线比较 | [raphaelvallat.com/yasa](https://raphaelvallat.com/yasa/) |

## BIDS 为什么重要

EEG-BIDS 把原始数据、通道、事件、参与者和采集元数据放在固定目录与表格中。它不能自动保证研究质量，但能让程序发现文件、验证命名、追踪版本，并减少“事件含义只存在某个人电脑里”的问题。

最小结构示意：

```text
dataset_description.json
participants.tsv
sub-001/
  ses-01/
    eeg/
      sub-001_ses-01_task-oddball_eeg.vhdr
      sub-001_ses-01_task-oddball_eeg.eeg
      sub-001_ses-01_task-oddball_eeg.vmrk
      sub-001_ses-01_task-oddball_channels.tsv
      sub-001_ses-01_task-oddball_events.tsv
      sub-001_ses-01_task-oddball_eeg.json
```

## 项目结构建议

```text
data/raw/          # 只读或由下载脚本生成
data/derivatives/  # 预处理产物，带 pipeline 名和版本
configs/           # 参数，不藏在 notebook 单元格里
src/               # 可测试函数
notebooks/         # 探索和解释，不承担全部流水线
reports/qc/        # 每人和全队列质控
results/           # 由命令生成的表和图
```

## 环境与复现

- 固定 Python/MATLAB、工具箱和 CUDA 版本。
- 下载时保存数据集版本、许可和校验和。
- 参数放 YAML/JSON，命令和随机种子写进日志。
- 原始数据只读，衍生结果可以删除后从脚本重建。
- Notebook 先清空输出再从头运行，检查是否依赖隐藏状态。

## 推荐起点

本项目的可运行案例优先使用 MNE-Python；如果你的实验室以 EEGLAB/FieldTrip 为主，可以先在 Python 中理解概念，再用实验室工具复现同一张 PSD、ERP 或时频图。

