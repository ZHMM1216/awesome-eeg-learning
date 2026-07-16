# 采样与混叠实验室

EEG 是连续电压，但计算机只能保存离散采样点。要可靠表示最高频率为 `f` 的信号，采样率 `fs` 至少应大于 `2f`。下面的实验让你直接观察欠采样如何把高频“伪装”成较低频率。

<div class="sampling-lab" id="sampling-lab">
  <div class="sampling-lab__controls">
    <label for="signal-frequency">
      <strong>真实信号频率：<output id="signal-frequency-value">12 Hz</output></strong>
      <input id="signal-frequency" type="range" min="1" max="40" value="12" step="1">
    </label>
    <label for="sampling-rate">
      <strong>采样率：<output id="sampling-rate-value">50 Hz</output></strong>
      <input id="sampling-rate" type="range" min="10" max="100" value="50" step="1">
    </label>
  </div>
  <svg viewBox="0 0 820 300" role="img" aria-label="交互式采样示意图">
    <line x1="48" y1="141" x2="802" y2="141" stroke="currentColor" opacity="0.25"></line>
    <line x1="48" y1="24" x2="48" y2="258" stroke="currentColor" opacity="0.35"></line>
    <line x1="48" y1="258" x2="802" y2="258" stroke="currentColor" opacity="0.35"></line>
    <text x="48" y="282" fill="currentColor">0 s</text>
    <text x="784" y="282" fill="currentColor">1 s</text>
    <text x="8" y="145" fill="currentColor">0</text>
    <path id="analog-path" fill="none" stroke="#3366cc" stroke-width="2"></path>
    <path id="sampled-path" fill="none" stroke="#e07a3f" stroke-width="1.5"></path>
    <g id="sample-points"></g>
  </svg>
  <div class="sampling-lab__legend" aria-label="图例">
    <span><span class="sampling-lab__swatch" style="background:#3366cc"></span>连续信号</span>
    <span><span class="sampling-lab__swatch" style="background:#e07a3f"></span>采样点与连接线</span>
  </div>
  <p class="sampling-lab__status" id="sampling-status" aria-live="polite"></p>
</div>

## 建议做三个实验

1. 固定 12 Hz，把采样率从 100 Hz 缓慢降到 20 Hz，观察什么时候开始不满足 Nyquist 条件。
2. 固定采样率 50 Hz，把信号频率从 5 Hz 增加到 35 Hz，观察 30 Hz 为什么可能看起来像 20 Hz。
3. 思考：如果肌电含有高于目标分析频段的成分，重采样前为什么需要抗混叠低通滤波？

!!! info "这张图省略了什么"
    实际 EEG 不是单一正弦波，抗混叠滤波器也不是理想砖墙滤波器。实验只帮助理解采样的基本约束；真实重采样应使用经过验证的信号处理函数并记录参数。

??? question "检查答案"
    - 12 Hz 信号的理论最低采样率是 24 Hz，但实际采集通常需要更高采样率并保留滤波过渡带。
    - 50 Hz 采样下，30 Hz 会混叠到约 20 Hz。
    - 抗混叠低通先去掉新 Nyquist 频率以上的能量，避免它们折叠进保留频段。
