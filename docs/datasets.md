# EEG 数据集地图

选择数据集时不要只看“下载是否方便”。先问：人群是否匹配、标签是否回答你的问题、数据单位能否支持正确验证、许可是否允许你的用途。

## 入门选择表

| 方向 | Dataset | 规模/格式 | 访问 | 第一项练习 |
|---|---|---|---|---|
| 基础/MI | [EEGMMIDB](https://physionet.org/content/eegmmidb/1.0.0/) | 109 人，64 通道，160 Hz，EDF+ | 开放 | 一人睁闭眼 Alpha 与 MI |
| P300 | [OpenNeuro ds003061](https://openneuro.org/datasets/ds003061/versions/1.1.1) | EEG-BIDS / EEGLAB | CC0 | 目标/标准 ERP |
| SSVEP | [MNE SSVEP](https://mne.tools/stable/overview/datasets_index.html#ssvep) | 2 人，BrainVision/BIDS | 开放 | 基频/谐波与 CCA |
| ERP | [ERP CORE](https://erpinfo.org/erp-core) | ERN、N170、P300 等标准范式 | CC BY 4.0 | 复现一个预注册 ERP |
| 卒中 | [Liu2024](https://doi.org/10.1038/s41597-023-02787-8) | 50 名急性卒中，500 Hz | CC BY 4.0 | 单患者时频与 CSP |
| 癫痫 | [CHB-MIT](https://physionet.org/content/chbmit/1.0.0/) | 24 病例，256 Hz，EDF | 开放 | 连续发作事件指标 |
| 癫痫 | [TUSZ](https://isip.piconepress.com/projects/nedc/html/tuh_eeg/) | 大型临床语料，EDF | 注册 | 跨患者/记录泛化 |
| 睡眠 | [Sleep-EDF Expanded](https://physionet.org/content/sleep-edfx/1.0.0/) | 197 个 PSG 记录，100 Hz | 开放 | 一晚 Hypnogram 与五分类 |
| 麻醉 | [GABA anesthesia](https://physionet.org/content/eeg-gaba-anesthesia/1.0.0/) | MATLAB，意识状态事件 | 凭证 | 意识消失/恢复谱图 |
| 麻醉 | [VitalDB](https://vitaldb.net/dataset/) | 6388 例术中多参数 | 使用协议 | EEG/BIS/SQI 对齐 |
| 静息态 | [LEMON ds000221](https://openneuro.org/datasets/ds000221) | 227 人，多模态，BIDS | 开放 | 年龄与个体 Alpha 峰 |
| 临床静息态 | [TDBRAIN](https://www.synapse.org/TDBRAIN) | 1274 人，生命周期临床 EEG | 注册/DUA | 先用 20 人样例做批量质控 |
| 纵向静息态 | [Dortmund Vital ds005385](https://openneuro.org/datasets/ds005385/versions/1.0.2) | 608 人，208 人五年随访 | CC0 | 睁闭眼、任务前后与重测 |
| 神经退行 | [AD/FTD ds004504](https://openneuro.org/datasets/ds004504) | 88 人，19 导，500 Hz | CC0 | 患者级谱特征基线 |
| 新生儿发作 | [Helsinki neonatal](https://zenodo.org/records/1280684) | 79 人，三专家标注 | 开放 | 比较单专家与共识标签 |
| 跨用户 MI | [MI user profiles](https://zenodo.org/records/8089820) | 87 人，>20,800 trials | CC BY 4.0 | 跨用户泛化和公平性 |
| 跨日 MI | [Multi-day MI](https://doi.org/10.25452/figshare.plus.22671172) | 多日高质量运动想象 | 开放 | 会话漂移与目标日校准 |
| 临床常规 EEG | [NMT Scalp EEG](https://doi.org/10.3389/fnins.2021.755817) | 2417 条正常/异常记录 | 见官方数据页 | 患者级筛查与捷径审计 |

## 数据集下载前的 12 项检查

1. 人群：健康、患者、年龄、药物和疾病阶段。
2. 任务：静息、刺激、运动、整夜或术中连续监测。
3. 标签：谁标注、使用什么指南、是否有一致性信息。
4. 层级：受试者、Session、记录、Trial、窗口如何关联。
5. 设备：放大器、电极、采样率、在线滤波和单位。
6. 通道：Montage 是否一致，是否含 EOG/EMG/ECG。
7. 事件：时间基准、延迟、缺失和重复触发。
8. 缺失：哪些病例或时间段缺数据，原因是什么。
9. 许可：研究、商业、再分发和衍生数据限制。
10. 版本：固定数据集版本和下载日期。
11. 规模：独立受试者数，而不只是窗口数。
12. 适用性：数据能否真正回答你的目标问题。

## 从一名受试者开始

第一次不要下载整个临床语料。按以下顺序扩大：

<div class="learning-flow" aria-label="数据规模扩大顺序">
  <span>一个文件</span><b>→</b>
  <span>一名受试者</span><b>→</b>
  <span>一个完整 Session/夜晚</span><b>→</b>
  <span>小队列</span><b>→</b>
  <span>完整数据集</span>
</div>

每一步检查时长、事件数、通道、标签分布和输出图。这样能在下载数十 GB 前发现路径、单位或标签映射错误。

## 数据许可与医疗数据边界

- 本仓库不重新分发任何外部原始数据。
- “公开可下载”不等于可以任意再发布或商用。
- 凭证数据必须由使用者本人完成培训和协议，不能共享账号或绕过访问控制。
- 去标识数据仍可能具有隐私风险；不要尝试重新识别参与者。
- 研究输出中避免提交原始可识别记录、敏感时间戳和未经许可的派生数据。

完整、机器可读的数据卡位于 `catalog/datasets.yml`，可运行 `eeg-data <dataset-id>` 查看单个数据集要求。
