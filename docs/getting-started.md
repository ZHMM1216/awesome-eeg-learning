# 环境与 10 周学习路线

## 环境

推荐 Python 3.10–3.12、Git 和至少 10 GB 可用磁盘。核心教程只需 CPU；深度学习属于选修。

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[bci,clinical,notebooks,docs,dev]"
```

## 学习路线

1. 第 1 周：EEG 来源、电极、采样、参考和单位。
2. 第 2 周：波形浏览、坏道、工频、眼电与肌电伪迹。
3. 第 3 周：滤波、重参考、ICA、Epoch 与基线校正。
4. 第 4 周：PSD、频带功率、睁闭眼 Alpha。
5. 第 5 周：Oddball/P300 与 ERP 统计。
6. 第 6 周：SSVEP、CCA 与信息传输率。
7. 第 7 周：运动想象、ERD/ERS、CSP+LDA。
8. 第 8 周：选择卒中、癫痫、睡眠或麻醉方向。
9. 第 9 周：按受试者设计验证、选择正确指标。
10. 第 10 周：复现实验、记录配置、写局限和数据卡。

## 下载策略

所有下载都放入本地 `data/` 或 MNE/MOABB 缓存，已经被 `.gitignore` 排除。受限数据必须由使用者本人注册并同意官方条款。

