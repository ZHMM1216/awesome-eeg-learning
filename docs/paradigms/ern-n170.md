# ERN 与 N170

这两个范式帮助你练习更细致的 ERP 设计：ERN 以行为反应为时间零点，N170 以视觉刺激为时间零点。二者都提醒我们，成分名称并不等于单一脑过程。

<div class="learning-flow" aria-label="ERN 与 N170 时间锁定比较">
  <span>Flanker 刺激</span><b>→</b><span>按键反应 = 0 ms</span><b>→</b><span>ERN 约 0–100 ms</span>
</div>

<div class="learning-flow" aria-label="N170 时间锁定">
  <span>人脸/物体刺激 = 0 ms</span><b>→</b><span>视觉编码</span><b>→</b><span>N170 约 130–210 ms</span>
</div>

## Flanker / ERN

在 Flanker、Go/No-Go 或快速选择任务中，错误反应后约几十毫秒可观察到额中央负向成分。分析时通常以按键反应锁定，而不是刺激锁定。

### 分析步骤

1. 清理反应码，核对正确、错误、遗漏和过快反应。
2. 以反应为 0 秒切 Epoch，并保留刺激—反应时间以检查重叠。
3. 在 FCz/Cz 比较错误与正确反应；使用相同反应时分布的对照更稳妥。
4. 错误 Trial 往往较少，应报告每人保留的 Trial 数，并避免把极少错误者强行纳入。
5. 把 ERP 条件差异与“能否单试次检测错误”分开讨论。

| Year | Paper | DOI |
|---:|---|---|
| 1993 | Gehring et al., *A Neural System for Error Detection and Compensation* | [10.1111/j.1467-9280.1993.tb00586.x](https://doi.org/10.1111/j.1467-9280.1993.tb00586.x) |

## 人脸 N170

人脸刺激常在枕颞区约 170 ms 引起相对明显的负向 ERP。它适合学习视觉刺激匹配、左右半球差异和峰值测量的不确定性。

### 设计与分析

| 要素 | 建议 |
|---|---|
| 条件 | 人脸、物体；可加入倒置人脸 |
| 刺激控制 | 尺寸、亮度、空间频率和背景尽量匹配 |
| 通道 | P7/P8、PO7/PO8 及相邻枕颞通道 |
| 时间窗 | 根据独立文献或留出的数据预先定义约 130–210 ms |
| 指标 | 平均振幅通常比单点峰值更稳健 |

常见错误是把“人脸比物体更负”直接解释为某个唯一模块，或者在观察每个通道后选择差异最大的电极而不校正多重比较。

| Year | Paper | DOI |
|---:|---|---|
| 1996 | Bentin et al., *Electrophysiological Studies of Face Perception in Humans* | [10.1162/jocn.1996.8.6.551](https://doi.org/10.1162/jocn.1996.8.6.551) |

??? question "完成本节前自测"
    同一实验既可刺激锁定也可反应锁定，但两者回答不同问题。ERN 的错误 Trial 少时应报告每人 Trial 数；N170 比较人脸与物体时要控制低级视觉差异，并避免看完所有电极后只挑最大差异通道。
