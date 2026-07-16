(() => {
  const NS = "http://www.w3.org/2000/svg";

  function pathData(points, xScale, yScale) {
    return points
      .map(([x, y], index) => `${index === 0 ? "M" : "L"}${xScale(x).toFixed(2)},${yScale(y).toFixed(2)}`)
      .join(" ");
  }

  function initLab(root) {
    const frequency = root.querySelector("#signal-frequency");
    const samplingRate = root.querySelector("#sampling-rate");
    const frequencyValue = root.querySelector("#signal-frequency-value");
    const samplingValue = root.querySelector("#sampling-rate-value");
    const status = root.querySelector("#sampling-status");
    const svg = root.querySelector("svg");
    const analogPath = root.querySelector("#analog-path");
    const sampledPath = root.querySelector("#sampled-path");
    const pointsGroup = root.querySelector("#sample-points");

    const width = 820;
    const height = 300;
    const margin = { left: 48, right: 18, top: 24, bottom: 42 };
    const xScale = (value) => margin.left + value * (width - margin.left - margin.right);
    const yScale = (value) => margin.top + (1 - (value + 1.2) / 2.4) * (height - margin.top - margin.bottom);

    function update() {
      const f = Number(frequency.value);
      const fs = Number(samplingRate.value);
      const analog = Array.from({ length: 500 }, (_, index) => {
        const t = index / 499;
        return [t, Math.sin(2 * Math.PI * f * t)];
      });
      const sampleCount = Math.floor(fs) + 1;
      const samples = Array.from({ length: sampleCount }, (_, index) => {
        const t = index / fs;
        return [t, Math.sin(2 * Math.PI * f * t)];
      }).filter(([t]) => t <= 1);

      analogPath.setAttribute("d", pathData(analog, xScale, yScale));
      sampledPath.setAttribute("d", pathData(samples, xScale, yScale));
      pointsGroup.replaceChildren();
      samples.forEach(([t, value]) => {
        const circle = document.createElementNS(NS, "circle");
        circle.setAttribute("cx", xScale(t));
        circle.setAttribute("cy", yScale(value));
        circle.setAttribute("r", "3.2");
        circle.setAttribute("fill", "#e07a3f");
        pointsGroup.appendChild(circle);
      });

      frequencyValue.textContent = `${f} Hz`;
      samplingValue.textContent = `${fs} Hz`;
      const adequate = fs >= 2 * f;
      const alias = Math.abs(((f + fs / 2) % fs) - fs / 2);
      status.classList.toggle("is-warning", !adequate);
      status.textContent = adequate
        ? `满足 Nyquist 条件：${fs} ≥ 2 × ${f}。采样点能够表达这个频率。`
        : `发生欠采样：${fs} < 2 × ${f}。这些采样点看起来约像 ${alias.toFixed(1)} Hz，原频率无法唯一恢复。`;
      svg.setAttribute(
        "aria-label",
        `信号频率 ${f} Hz，采样率 ${fs} Hz，${adequate ? "满足" : "不满足"} Nyquist 条件。`,
      );
    }

    frequency.addEventListener("input", update);
    samplingRate.addEventListener("input", update);
    update();
  }

  function initialize() {
    document.querySelectorAll("#sampling-lab").forEach((root) => {
      if (!root.dataset.initialized) {
        root.dataset.initialized = "true";
        initLab(root);
      }
    });
  }

  document.addEventListener("DOMContentLoaded", initialize);
  if (typeof document$ !== "undefined") {
    document$.subscribe(initialize);
  }
})();
