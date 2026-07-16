"""Transparent spectral features for anesthesia EEG teaching examples."""

from __future__ import annotations

import numpy as np
from scipy.signal import welch


def spectral_edge_frequency(signal: np.ndarray, sampling_rate: float, edge: float = 0.95) -> float:
    frequencies, power = welch(signal, fs=sampling_rate, nperseg=min(len(signal), int(4 * sampling_rate)))
    mask = (frequencies >= 0.5) & (frequencies <= 47.0)
    frequencies, power = frequencies[mask], power[mask]
    cumulative = np.cumsum(power)
    if not cumulative.size or cumulative[-1] == 0:
        return float("nan")
    index = int(np.searchsorted(cumulative, edge * cumulative[-1]))
    return float(frequencies[min(index, len(frequencies) - 1)])


def suppression_ratio(signal: np.ndarray, threshold_uv: float = 5.0) -> float:
    """Simple teaching proxy; not a validated clinical suppression detector."""
    return float(np.mean(np.abs(signal) < threshold_uv))


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    example = rng.normal(scale=10, size=1280)
    print({"sef95": spectral_edge_frequency(example, 128), "suppression_proxy": suppression_ratio(example)})

