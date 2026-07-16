"""Generate deterministic conceptual SVG figures used by the beginner guides."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "assets" / "figures"
EXPECTED = {
    "electrode-map.svg",
    "signal-anatomy.svg",
    "alpha-psd.svg",
    "p300-erp.svg",
    "ssvep-spectrum.svg",
    "motor-imagery-erd.svg",
    "subject-split.svg",
    "seizure-event-metrics.svg",
    "sleep-hypnogram.svg",
    "anesthesia-spectrogram.svg",
}

NAVY = "#263a63"
BLUE = "#3366cc"
ORANGE = "#e07a3f"
GREEN = "#2f8f6b"
RED = "#c44e52"
PURPLE = "#7b61a8"
GRID = "#d7dde8"
TEXT = "#233044"


def setup() -> None:
    mpl.rcParams.update(
        {
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": NAVY,
            "axes.labelcolor": TEXT,
            "axes.titlecolor": TEXT,
            "xtick.color": TEXT,
            "ytick.color": TEXT,
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "svg.hashsalt": "awesome-eeg-learning",
        }
    )


def save(fig: plt.Figure, name: str, title: str, description: str) -> None:
    path = OUTPUT / name
    fig.savefig(
        path,
        format="svg",
        bbox_inches="tight",
        metadata={"Date": None, "Title": title, "Description": description},
    )
    content = path.read_text(encoding="utf-8")
    path.write_text(
        "\n".join(line.rstrip() for line in content.splitlines()) + "\n",
        encoding="utf-8",
    )
    plt.close(fig)


def electrode_map() -> None:
    positions = {
        "Fp1": (-0.34, 0.84),
        "Fp2": (0.34, 0.84),
        "F7": (-0.78, 0.48),
        "F3": (-0.36, 0.48),
        "Fz": (0.0, 0.52),
        "F4": (0.36, 0.48),
        "F8": (0.78, 0.48),
        "T7": (-0.92, 0.0),
        "C3": (-0.42, 0.0),
        "Cz": (0.0, 0.0),
        "C4": (0.42, 0.0),
        "T8": (0.92, 0.0),
        "P7": (-0.78, -0.45),
        "P3": (-0.36, -0.45),
        "Pz": (0.0, -0.5),
        "P4": (0.36, -0.45),
        "P8": (0.78, -0.45),
        "O1": (-0.34, -0.82),
        "Oz": (0.0, -0.88),
        "O2": (0.34, -0.82),
    }
    fig, ax = plt.subplots(figsize=(7.4, 5.3))
    ax.add_patch(Circle((0, 0), 1, fill=False, lw=2.2, color=NAVY))
    ax.add_patch(Polygon([(-0.13, 0.98), (0, 1.15), (0.13, 0.98)], fill=False, color=NAVY))
    ax.plot([-1.0, -1.1, -1.02], [0.22, 0, -0.22], color=NAVY, lw=1.8)
    ax.plot([1.0, 1.1, 1.02], [0.22, 0, -0.22], color=NAVY, lw=1.8)
    region_colors = {"F": ORANGE, "C": BLUE, "P": GREEN, "O": PURPLE, "T": RED}
    for label, (x, y) in positions.items():
        color = region_colors.get(label[0], NAVY)
        ax.scatter(x, y, s=250, color=color, edgecolor="white", linewidth=1.5, zorder=3)
        ax.text(x, y, label, ha="center", va="center", color="white", fontsize=8, weight="bold")
    ax.text(-1.42, 0.58, "Frontal\nattention / eye artifact", ha="center", color=ORANGE)
    ax.text(-1.42, 0.0, "Central\nsensorimotor", ha="center", color=BLUE)
    ax.text(1.42, -0.45, "Parietal\nP300", ha="center", color=GREEN)
    ax.text(1.42, -0.82, "Occipital\nalpha / SSVEP", ha="center", color=PURPLE)
    ax.set(xlim=(-1.75, 1.75), ylim=(-1.2, 1.22), aspect="equal")
    ax.axis("off")
    ax.set_title("10–20 electrode map: location guides interpretation, not source localization", pad=10)
    save(
        fig,
        "electrode-map.svg",
        "EEG 10-20 electrode map",
        "Conceptual top view of common scalp electrodes and beginner-relevant regions.",
    )


def signal_anatomy() -> None:
    rng = np.random.default_rng(14)
    fs = 250
    time = np.arange(0, 10, 1 / fs)
    drift = 9 * np.sin(2 * np.pi * 0.18 * time)
    alpha = 5 * np.sin(2 * np.pi * 10 * time)
    noise = rng.normal(0, 1.6, len(time))
    blink = 55 * np.exp(-((time - 2.0) / 0.12) ** 2)
    muscle_mask = (time >= 6.4) & (time <= 7.2)
    muscle = np.zeros_like(time)
    muscle[muscle_mask] = 13 * np.sin(2 * np.pi * 38 * time[muscle_mask])
    signal = drift + alpha + noise + blink + muscle

    fig, ax = plt.subplots(figsize=(10, 3.6))
    ax.plot(time, signal, color=NAVY, lw=0.8)
    ax.axvspan(1.72, 2.28, color=ORANGE, alpha=0.18)
    ax.axvspan(6.35, 7.25, color=RED, alpha=0.15)
    ax.annotate("eye blink", (2.0, 58), (2.7, 66), arrowprops={"arrowstyle": "->", "color": ORANGE})
    ax.annotate("muscle burst", (6.75, 8), (7.7, 52), arrowprops={"arrowstyle": "->", "color": RED})
    ax.annotate("slow drift", (4.6, -9), (3.5, -30), arrowprops={"arrowstyle": "->", "color": GREEN})
    ax.text(8.15, 18, "10 Hz alpha + broadband noise", color=BLUE)
    ax.set(xlabel="Time (s)", ylabel="Amplitude (µV)", xlim=(0, 10))
    ax.grid(axis="x", color=GRID, lw=0.7)
    ax.set_title("A raw EEG trace is a mixture: inspect before filtering")
    save(
        fig,
        "signal-anatomy.svg",
        "Anatomy of a conceptual EEG trace",
        "Synthetic trace showing slow drift, alpha activity, an eye blink, and a muscle burst.",
    )


def alpha_psd() -> None:
    freq = np.linspace(1, 40, 500)
    base = 18 / (freq**1.15) + 0.08
    closed = base + 3.2 * np.exp(-0.5 * ((freq - 10.2) / 1.0) ** 2)
    opened = base + 0.75 * np.exp(-0.5 * ((freq - 10.2) / 1.25) ** 2)
    fig, ax = plt.subplots(figsize=(8.5, 4.1))
    ax.axvspan(8, 13, color=PURPLE, alpha=0.12, label="alpha band (8–13 Hz)")
    ax.plot(freq, closed, color=BLUE, lw=2, label="eyes closed")
    ax.plot(freq, opened, color=ORANGE, lw=2, label="eyes open")
    ax.annotate("individual alpha peak", (10.2, closed.max()), (15.5, 3.2), arrowprops={"arrowstyle": "->"})
    ax.set(xlabel="Frequency (Hz)", ylabel="Power spectral density (a.u.)", xlim=(1, 40), yscale="log")
    ax.grid(color=GRID, lw=0.6, alpha=0.8)
    ax.legend(frameon=False)
    ax.set_title("Eyes-closed alpha is a peak, not simply all 8–13 Hz power")
    save(
        fig,
        "alpha-psd.svg",
        "Conceptual eyes-open and eyes-closed EEG power spectra",
        "Synthetic spectra demonstrating increased eyes-closed alpha power near 10 Hz.",
    )


def p300_erp() -> None:
    time = np.linspace(-200, 800, 501)
    n100 = -2.0 * np.exp(-0.5 * ((time - 110) / 35) ** 2)
    p200 = 1.3 * np.exp(-0.5 * ((time - 190) / 45) ** 2)
    standard = n100 + p200 + 0.25 * np.sin(time / 70)
    target = standard + 5.2 * np.exp(-0.5 * ((time - 360) / 105) ** 2)
    fig, ax = plt.subplots(figsize=(8.7, 4.2))
    ax.axvspan(-200, 0, color=GREEN, alpha=0.10, label="baseline")
    ax.axvspan(250, 500, color=PURPLE, alpha=0.10, label="P300 window")
    ax.axvline(0, color=TEXT, lw=1, ls="--")
    ax.plot(time, target, color=BLUE, lw=2, label="rare target")
    ax.plot(time, standard, color=ORANGE, lw=2, label="frequent standard")
    ax.annotate("P300 / P3b", (360, target.max()), (515, 5.5), arrowprops={"arrowstyle": "->"})
    ax.set(xlabel="Time from stimulus (ms)", ylabel="Amplitude (µV)", xlim=(-200, 800))
    ax.grid(axis="x", color=GRID, lw=0.7)
    ax.legend(frameon=False, ncol=2)
    ax.set_title("ERP averaging reveals a condition-linked waveform")
    save(
        fig,
        "p300-erp.svg",
        "Conceptual P300 event-related potential",
        "Synthetic target and standard ERPs with baseline and P300 analysis windows.",
    )


def ssvep_spectrum() -> None:
    freq = np.linspace(4, 40, 600)
    spectrum = 0.7 / np.sqrt(freq) + 0.03
    for peak, height, width in [(12, 1.7, 0.22), (24, 0.9, 0.28), (36, 0.35, 0.3)]:
        spectrum += height * np.exp(-0.5 * ((freq - peak) / width) ** 2)
    fig, ax = plt.subplots(figsize=(8.5, 4.0))
    ax.plot(freq, spectrum, color=BLUE, lw=2)
    for peak, label in [(12, "12 Hz stimulus"), (24, "2nd harmonic"), (36, "3rd harmonic")]:
        value = spectrum[np.abs(freq - peak).argmin()]
        ax.scatter([peak], [value], color=ORANGE, zorder=3)
        ax.annotate(label, (peak, value), (peak + 1.2, value + 0.13), arrowprops={"arrowstyle": "->"})
    ax.set(xlabel="Frequency (Hz)", ylabel="Occipital power (a.u.)", xlim=(4, 40), ylim=(0, 2.05))
    ax.grid(color=GRID, lw=0.7)
    ax.set_title("SSVEP decoding uses the stimulus frequency and its harmonics")
    save(
        fig,
        "ssvep-spectrum.svg",
        "Conceptual SSVEP power spectrum",
        "Synthetic occipital spectrum with peaks at a 12 Hz stimulus and its harmonics.",
    )


def motor_imagery_erd() -> None:
    time = np.linspace(-1, 4, 220)
    freq = np.linspace(4, 35, 100)
    tt, ff = np.meshgrid(time, freq)
    task = 1 / (1 + np.exp(-(tt - 0.3) * 7)) * 1 / (1 + np.exp((tt - 3.0) * 7))
    mu = np.exp(-0.5 * ((ff - 11) / 2.3) ** 2)
    beta = np.exp(-0.5 * ((ff - 22) / 4.0) ** 2)
    contralateral = -3.2 * task * (mu + 0.65 * beta)
    ipsilateral = -1.1 * task * (mu + 0.45 * beta)
    rebound = 1.2 * np.exp(-0.5 * ((tt - 3.35) / 0.23) ** 2) * beta

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.0), sharex=True, sharey=True)
    for ax, data, title in zip(
        axes,
        [contralateral + rebound, ipsilateral + 0.5 * rebound],
        ["Contralateral sensorimotor cortex", "Ipsilateral sensorimotor cortex"],
        strict=True,
    ):
        im = ax.imshow(
            data,
            extent=(time.min(), time.max(), freq.min(), freq.max()),
            origin="lower",
            aspect="auto",
            cmap="RdBu_r",
            vmin=-3.5,
            vmax=3.5,
            interpolation="bilinear",
        )
        ax.axvline(0, color="black", ls="--", lw=1)
        ax.axvline(3, color="black", ls="--", lw=1)
        ax.set(xlabel="Time from imagery cue (s)", title=title)
    axes[0].set_ylabel("Frequency (Hz)")
    cbar = fig.colorbar(im, ax=axes, shrink=0.9, pad=0.03)
    cbar.set_label("Power change from baseline (dB)")
    fig.suptitle("Motor imagery: Mu/Beta ERD is often stronger contralaterally", y=1.02)
    save(
        fig,
        "motor-imagery-erd.svg",
        "Conceptual motor imagery ERD time-frequency maps",
        "Synthetic contralateral and ipsilateral Mu and Beta power changes during imagery.",
    )


def subject_split() -> None:
    fig, axes = plt.subplots(2, 1, figsize=(10, 4.6))
    subjects = ["S01", "S02", "S03", "S04", "S05", "S06"]
    for ax, title in zip(
        axes,
        ["Wrong: random windows leak subject identity", "Correct: subjects stay in one split"],
        strict=True,
    ):
        ax.set(xlim=(0, 12), ylim=(0, 6), title=title)
        ax.axis("off")
    for row, subject in enumerate(subjects):
        axes[0].text(-0.15, 5.5 - row, subject, ha="right", va="center")
        for column in range(12):
            color = BLUE if (column + row) % 3 else ORANGE
            axes[0].add_patch(Rectangle((column + 0.04, 5.18 - row), 0.86, 0.64, color=color, alpha=0.82))
    axes[0].text(12.1, 4.2, "blue = train", color=BLUE, va="center")
    axes[0].text(12.1, 3.4, "orange = test", color=ORANGE, va="center")
    for row, subject in enumerate(subjects):
        axes[1].text(-0.15, 5.5 - row, subject, ha="right", va="center")
        color = BLUE if row < 4 else ORANGE
        for column in range(12):
            axes[1].add_patch(Rectangle((column + 0.04, 5.18 - row), 0.86, 0.64, color=color, alpha=0.82))
    axes[1].text(12.1, 4.2, "train subjects", color=BLUE, va="center")
    axes[1].text(12.1, 1.0, "held-out subjects", color=ORANGE, va="center")
    fig.tight_layout()
    save(
        fig,
        "subject-split.svg",
        "EEG train-test splitting comparison",
        "Schematic contrasting leaky random-window splitting with subject-level splitting.",
    )


def seizure_event_metrics() -> None:
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.broken_barh([(15, 3), (40, 3)], (18, 6), facecolors=ORANGE, label="true seizure")
    ax.broken_barh([(16, 3), (30, 1), (42, 2)], (7, 6), facecolors=BLUE, label="model alarm")
    ax.annotate("1 min latency", (16, 15), (19, 28), arrowprops={"arrowstyle": "->"})
    ax.annotate("false alarm", (30.5, 10), (32, 2), arrowprops={"arrowstyle": "->"})
    ax.annotate("2 min latency", (42, 15), (45, 28), arrowprops={"arrowstyle": "->"})
    ax.set(xlim=(0, 60), ylim=(0, 34), xlabel="Continuous recording time (min)", yticks=[])
    ax.grid(axis="x", color=GRID, lw=0.7)
    ax.legend(frameon=False, ncol=2, loc="upper left")
    ax.set_title("Seizure detection is evaluated as events on a continuous timeline")
    save(
        fig,
        "seizure-event-metrics.svg",
        "Seizure event detection timeline",
        "Conceptual timeline showing two seizures, detection delays, and one false alarm.",
    )


def sleep_hypnogram() -> None:
    stage_values = {"W": 4, "REM": 3, "N1": 2, "N2": 1, "N3": 0}
    sequence = [
        "W", "W", "N1", "N2", "N2", "N3", "N3", "N2", "REM", "W",
        "N1", "N2", "N3", "N3", "N2", "N2", "REM", "REM", "W", "N1",
        "N2", "N3", "N2", "N2", "REM", "REM", "W", "N1", "N2", "N2",
        "N3", "N2", "REM", "REM", "W", "N1", "N2", "N2", "REM", "W",
    ]
    time = np.linspace(0, 8, len(sequence))
    values = [stage_values[stage] for stage in sequence]
    fig, ax = plt.subplots(figsize=(10, 3.8))
    ax.step(time, values, where="post", color=BLUE, lw=2)
    ax.fill_between(time, values, step="post", alpha=0.08, color=BLUE)
    for cycle in [1.6, 3.3, 5.0, 6.7]:
        ax.axvline(cycle, color=GRID, lw=1, ls="--")
    ax.set(
        xlim=(0, 8),
        ylim=(-0.3, 4.3),
        xlabel="Hours from lights off",
        ylabel="Sleep stage",
        yticks=list(stage_values.values()),
        yticklabels=list(stage_values.keys()),
    )
    ax.grid(axis="y", color=GRID, lw=0.7)
    ax.set_title("A hypnogram shows architecture and transitions across the whole night")
    save(
        fig,
        "sleep-hypnogram.svg",
        "Conceptual overnight sleep hypnogram",
        "Synthetic whole-night progression through wake, REM, N1, N2, and N3.",
    )


def anesthesia_spectrogram() -> None:
    time = np.linspace(0, 60, 300)
    freq = np.linspace(0.5, 40, 160)
    tt, ff = np.meshgrid(time, freq)
    awake = np.exp(-0.5 * ((ff - 20) / 7) ** 2) * (tt < 10)
    slow = 1.6 * np.exp(-0.5 * ((ff - 2.0) / 1.8) ** 2) * ((tt >= 10) & (tt < 48))
    alpha = 1.25 * np.exp(-0.5 * ((ff - 10) / 2.0) ** 2) * ((tt >= 10) & (tt < 48))
    suppression = 0.18 + 0.82 * (np.sin(tt * 1.45) > 0.4)
    deep = (tt >= 32) & (tt < 40)
    power = 0.12 + awake + slow + alpha
    power[deep] *= suppression[deep]
    recovery = (tt >= 48) * np.exp(-0.5 * ((ff - 18) / 8) ** 2) * ((tt - 48) / 12)
    power += recovery
    fig, ax = plt.subplots(figsize=(10, 4.1))
    image = ax.imshow(
        10 * np.log10(power),
        extent=(time.min(), time.max(), freq.min(), freq.max()),
        origin="lower",
        aspect="auto",
        cmap="viridis",
        interpolation="bilinear",
    )
    for boundary, label in [(10, "induction"), (32, "deep / suppression"), (48, "recovery")]:
        ax.axvline(boundary, color="white", lw=1, ls="--")
        ax.text(boundary + 0.8, 37, label, color="white", va="top")
    cbar = fig.colorbar(image, ax=ax, pad=0.02)
    cbar.set_label("Conceptual power (dB)")
    ax.set(xlabel="Time (min)", ylabel="Frequency (Hz)", ylim=(0.5, 40))
    ax.set_title("Anesthesia EEG is a time-frequency pattern, not one universal depth number")
    save(
        fig,
        "anesthesia-spectrogram.svg",
        "Conceptual anesthesia EEG spectrogram",
        "Synthetic spectrogram showing awake activity, slow and alpha rhythms, suppression, and recovery.",
    )


def generate_all() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    setup()
    electrode_map()
    signal_anatomy()
    alpha_psd()
    p300_erp()
    ssvep_spectrum()
    motor_imagery_erd()
    subject_split()
    seizure_event_metrics()
    sleep_hypnogram()
    anesthesia_spectrogram()


def check() -> int:
    missing = sorted(name for name in EXPECTED if not (OUTPUT / name).exists())
    invalid = []
    for name in EXPECTED - set(missing):
        content = (OUTPUT / name).read_text(encoding="utf-8")
        if "<svg" not in content or "<title>" not in content or len(content) < 1000:
            invalid.append(name)
    if missing or invalid:
        if missing:
            print("missing figures:", ", ".join(missing))
        if invalid:
            print("invalid figures:", ", ".join(sorted(invalid)))
        return 1
    print(f"Tutorial figure validation passed ({len(EXPECTED)} SVG files).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        return check()
    generate_all()
    return check()


if __name__ == "__main__":
    raise SystemExit(main())
