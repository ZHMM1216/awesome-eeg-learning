import importlib.util
from pathlib import Path

import numpy as np


def load_module(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_seizure_event_metrics():
    module = load_module("examples/clinical/chbmit_event_metrics.py", "seizure_metrics")
    result = module.event_metrics([(10, 20)], [(12, 18), (30, 35)], duration_hours=1)
    assert result["event_sensitivity"] == 1.0
    assert result["false_alarms_per_hour"] == 1.0


def test_sleep_features_sum_to_one():
    module = load_module("examples/clinical/sleep_edf_baseline.py", "sleep_features")
    rng = np.random.default_rng(0)
    features = module.bandpower_features(rng.normal(size=3000), 100)
    assert 0.95 <= sum(features.values()) <= 1.05


def test_anesthesia_features():
    module = load_module("examples/clinical/anesthesia_spectral_features.py", "anesthesia_features")
    time = np.arange(1280) / 128
    signal = 20 * np.sin(2 * np.pi * 10 * time)
    assert 9 <= module.spectral_edge_frequency(signal, 128) <= 11
    assert 0 <= module.suppression_ratio(signal) <= 1

