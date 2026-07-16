"""Feature recipe for a subject-wise Sleep-EDF baseline.

The full tutorial downloads PSG/Hypnogram pairs from PhysioNet. This module keeps
the reusable, transparent feature extraction separate from access code.
"""

from __future__ import annotations

import numpy as np
from scipy.signal import welch

BANDS = {
    "delta": (0.5, 4.0),
    "theta": (4.0, 8.0),
    "alpha": (8.0, 12.0),
    "sigma": (12.0, 16.0),
    "beta": (16.0, 30.0),
}


def bandpower_features(epoch: np.ndarray, sampling_rate: float) -> dict[str, float]:
    frequencies, power = welch(epoch, fs=sampling_rate, nperseg=min(len(epoch), int(4 * sampling_rate)))
    total_mask = (frequencies >= 0.5) & (frequencies <= 30.0)
    total = np.trapezoid(power[total_mask], frequencies[total_mask])
    features: dict[str, float] = {}
    for name, (low, high) in BANDS.items():
        mask = (frequencies >= low) & (frequencies < high)
        band = np.trapezoid(power[mask], frequencies[mask])
        features[f"relative_{name}"] = float(band / total) if total else 0.0
    return features


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    sample_epoch = rng.normal(size=3000)
    print(bandpower_features(sample_epoch, sampling_rate=100))

