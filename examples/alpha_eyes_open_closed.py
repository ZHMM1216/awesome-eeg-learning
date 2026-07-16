"""Compare posterior alpha power during eyes-open and eyes-closed baselines."""

from __future__ import annotations

import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci


def relative_alpha(raw: mne.io.BaseRaw, channels: list[str]) -> float:
    spectrum = raw.compute_psd(method="welch", fmin=1, fmax=30, picks=channels)
    psds, freqs = spectrum.get_data(return_freqs=True)
    alpha = psds[:, (freqs >= 8) & (freqs <= 13)].sum()
    broadband = psds.sum()
    return float(alpha / broadband)


def main() -> None:
    mne.set_log_level("WARNING")
    subject = 1
    open_path, closed_path = eegbci.load_data(subject, runs=[1, 2], update_path=True)
    eyes_open = mne.io.read_raw_edf(open_path, preload=True)
    eyes_closed = mne.io.read_raw_edf(closed_path, preload=True)
    eegbci.standardize(eyes_open)
    eegbci.standardize(eyes_closed)
    montage = mne.channels.make_standard_montage("standard_1005")
    eyes_open.set_montage(montage)
    eyes_closed.set_montage(montage)
    for raw in (eyes_open, eyes_closed):
        raw.set_eeg_reference("average", projection=False)
        raw.filter(1, 30)

    posterior = [
        channel for channel in ["O1", "Oz", "O2", "PO3", "PO4"] if channel in eyes_open.ch_names
    ]
    values = [relative_alpha(eyes_open, posterior), relative_alpha(eyes_closed, posterior)]
    print(f"Posterior relative alpha — eyes open: {values[0]:.3f}, eyes closed: {values[1]:.3f}")

    figure, axis = plt.subplots(figsize=(6, 4))
    axis.bar(["Eyes open", "Eyes closed"], values, color=["#4c78a8", "#f58518"])
    axis.set_ylabel("Relative 8–13 Hz power")
    axis.set_title("EEGMMIDB subject 1: posterior alpha")
    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
