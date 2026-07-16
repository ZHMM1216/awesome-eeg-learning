"""Event-level seizure metrics used by the epilepsy tutorial."""

from __future__ import annotations

from collections.abc import Iterable


Interval = tuple[float, float]


def overlaps(left: Interval, right: Interval, tolerance: float = 0.0) -> bool:
    return left[0] <= right[1] + tolerance and right[0] <= left[1] + tolerance


def event_metrics(
    truth: Iterable[Interval],
    predictions: Iterable[Interval],
    duration_hours: float,
    tolerance_seconds: float = 0.0,
) -> dict[str, float]:
    true_events = list(truth)
    predicted_events = list(predictions)
    detected = sum(
        any(overlaps(event, prediction, tolerance_seconds) for prediction in predicted_events)
        for event in true_events
    )
    false_alarms = sum(
        not any(overlaps(event, prediction, tolerance_seconds) for event in true_events)
        for prediction in predicted_events
    )
    sensitivity = detected / len(true_events) if true_events else 0.0
    false_alarms_per_hour = false_alarms / duration_hours if duration_hours else float("inf")
    return {
        "event_sensitivity": sensitivity,
        "false_alarms_per_hour": false_alarms_per_hour,
        "detected_events": float(detected),
        "false_alarms": float(false_alarms),
    }


if __name__ == "__main__":
    print(event_metrics([(100, 130), (500, 540)], [(95, 125), (300, 315)], duration_hours=1.0))

