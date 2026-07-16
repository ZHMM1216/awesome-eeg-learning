"""Beginner motor-imagery baseline: CSP plus LDA on one EEGMMIDB subject."""

from __future__ import annotations

import mne
import numpy as np
from mne.datasets import eegbci
from mne.decoding import CSP
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline


def main() -> None:
    mne.set_log_level("WARNING")
    files = eegbci.load_data(subjects=1, runs=[4, 8, 12], update_path=True)
    raw = mne.concatenate_raws([mne.io.read_raw_edf(path, preload=True) for path in files])
    eegbci.standardize(raw)
    raw.set_montage(mne.channels.make_standard_montage("standard_1005"))
    raw.set_eeg_reference("average", projection=False)
    raw.filter(8, 30)

    events, event_id = mne.events_from_annotations(raw)
    selected = {label: event_id[label] for label in ("T1", "T2")}
    epochs = mne.Epochs(
        raw,
        events,
        selected,
        tmin=1.0,
        tmax=4.0,
        baseline=None,
        picks="eeg",
        preload=True,
    )
    labels = epochs.events[:, -1]
    pipeline = make_pipeline(
        CSP(n_components=6, reg="ledoit_wolf", log=True, norm_trace=False),
        LinearDiscriminantAnalysis(),
    )
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(pipeline, epochs.get_data(), labels, cv=cv, scoring="balanced_accuracy")
    print(f"Balanced accuracy: {np.mean(scores):.3f} ± {np.std(scores):.3f}")
    print("This is a within-subject teaching baseline, not evidence of cross-patient generalization.")


if __name__ == "__main__":
    main()
