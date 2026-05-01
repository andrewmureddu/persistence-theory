#!/usr/bin/env python3
"""ACP first-pass coupling analysis for Berlin honey-bee waggle data.

This script combines `Berlin2019_dances.csv` and `Berlin2019_followers.csv`
from Zenodo record 10.5281/zenodo.7928121. It summarizes dance, feeder,
dancer, spatial, and follower concentration by time window, then asks whether
current dance/recruitment volume predicts later repertoire narrowing.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Sequence


@dataclass(frozen=True)
class WindowSummary:
    window_start: str
    dances: int
    follower_events: int
    follow_events: int
    attendance_events: int
    distinct_dancers: int
    distinct_followers: int
    dancer_entropy: float | None
    feeder_entropy: float | None
    follower_entropy: float | None
    dance_spatial_entropy: float | None
    dominant_dancer_fraction: float | None
    dominant_feeder_fraction: float | None
    dominant_follower_fraction: float | None
    follower_events_per_dance: float | None


@dataclass(frozen=True)
class CouplingSummary:
    predictor: str
    outcome: str
    lag_windows: int
    lag_mode: str
    observations: int
    pearson: float | None
    spearman: float | None


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.strip().replace("Z", "+00:00"))


def window_key(timestamp: datetime, minutes: int) -> datetime:
    absolute_minutes = int(timestamp.timestamp() // 60)
    bucket = (absolute_minutes // minutes) * minutes
    return datetime.fromtimestamp(bucket * 60, tz=timestamp.tzinfo)


def shannon_from_counts(counts: Counter[object]) -> float | None:
    total = sum(counts.values())
    if total == 0:
        return None
    return -sum((count / total) * math.log(count / total) for count in counts.values())


def dominant_fraction(counts: Counter[object]) -> float | None:
    total = sum(counts.values())
    if total == 0:
        return None
    return max(counts.values()) / total


def spatial_bin(x: float, y: float, bin_size: float) -> tuple[int, int]:
    return (math.floor(x / bin_size), math.floor(y / bin_size))


def pearson(left: Sequence[float], right: Sequence[float]) -> float | None:
    if len(left) != len(right) or len(left) < 3:
        return None
    left_mean = statistics.fmean(left)
    right_mean = statistics.fmean(right)
    numerator = sum((a - left_mean) * (b - right_mean) for a, b in zip(left, right))
    left_ss = sum((a - left_mean) ** 2 for a in left)
    right_ss = sum((b - right_mean) ** 2 for b in right)
    denominator = math.sqrt(left_ss * right_ss)
    if denominator == 0:
        return None
    return numerator / denominator


def ranks(values: Sequence[float]) -> list[float]:
    indexed = sorted(enumerate(values), key=lambda item: item[1])
    result = [0.0] * len(values)
    index = 0
    while index < len(indexed):
        next_index = index + 1
        while next_index < len(indexed) and indexed[next_index][1] == indexed[index][1]:
            next_index += 1
        rank = (index + next_index - 1) / 2.0
        for original_index, _ in indexed[index:next_index]:
            result[original_index] = rank
        index = next_index
    return result


def spearman(left: Sequence[float], right: Sequence[float]) -> float | None:
    if len(left) != len(right) or len(left) < 3:
        return None
    return pearson(ranks(left), ranks(right))


def read_dances(path: Path) -> tuple[dict[str, dict[str, str]], dict[datetime, list[dict[str, str]]]]:
    by_id: dict[str, dict[str, str]] = {}
    by_window: dict[datetime, list[dict[str, str]]] = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            dance_id = row["dance_id"]
            by_id[dance_id] = row
    return by_id, by_window


def summarize_windows(
    dances_path: Path,
    followers_path: Path,
    window_minutes: int,
    spatial_bin_size: float,
) -> list[WindowSummary]:
    dance_by_id, _ = read_dances(dances_path)
    dance_windows: dict[datetime, list[dict[str, str]]] = defaultdict(list)
    follower_windows: dict[datetime, list[dict[str, str]]] = defaultdict(list)

    for dance in dance_by_id.values():
        start = window_key(parse_time(dance["ts_from"]), window_minutes)
        dance_windows[start].append(dance)

    with followers_path.open(newline="", encoding="utf-8") as handle:
        for follower_event in csv.DictReader(handle):
            dance = dance_by_id.get(follower_event["dance_id"])
            if dance is None:
                continue
            start = window_key(parse_time(follower_event["ts_from"]), window_minutes)
            merged = dict(follower_event)
            merged["dancer_id"] = dance["dancer_id"]
            merged["feeder_cam_id"] = dance["feeder_cam_id"]
            follower_windows[start].append(merged)

    summaries: list[WindowSummary] = []
    for start in sorted(set(dance_windows) | set(follower_windows)):
        dances = dance_windows.get(start, [])
        follower_events = follower_windows.get(start, [])

        dancer_counts: Counter[str] = Counter()
        feeder_counts: Counter[str] = Counter()
        follower_counts: Counter[str] = Counter()
        spatial_counts: Counter[tuple[int, int]] = Counter()
        label_counts: Counter[str] = Counter()

        for dance in dances:
            dancer_counts[dance["dancer_id"]] += 1
            feeder = dance.get("feeder_cam_id", "")
            if feeder:
                feeder_counts[feeder] += 1
            try:
                spatial_counts[spatial_bin(float(dance["median_x"]), float(dance["median_y"]), spatial_bin_size)] += 1
            except (KeyError, ValueError):
                pass

        for event in follower_events:
            follower_counts[event["follower_id"]] += 1
            label_counts[event.get("label", "")] += 1

        summaries.append(
            WindowSummary(
                window_start=start.isoformat(),
                dances=len(dances),
                follower_events=len(follower_events),
                follow_events=label_counts.get("follower", 0),
                attendance_events=label_counts.get("attendance", 0),
                distinct_dancers=len(dancer_counts),
                distinct_followers=len(follower_counts),
                dancer_entropy=shannon_from_counts(dancer_counts),
                feeder_entropy=shannon_from_counts(feeder_counts),
                follower_entropy=shannon_from_counts(follower_counts),
                dance_spatial_entropy=shannon_from_counts(spatial_counts),
                dominant_dancer_fraction=dominant_fraction(dancer_counts),
                dominant_feeder_fraction=dominant_fraction(feeder_counts),
                dominant_follower_fraction=dominant_fraction(follower_counts),
                follower_events_per_dance=(len(follower_events) / len(dances) if dances else None),
            )
        )
    return summaries


def lagged_pairs(
    rows: Sequence[WindowSummary],
    predictor: str,
    outcome: str,
    lag_windows: int,
    min_dances: int,
    window_minutes: int,
    lag_mode: str,
) -> tuple[list[float], list[float]]:
    left: list[float] = []
    right: list[float] = []

    if lag_mode == "active-window":
        row_pairs = (
            (rows[index], rows[index + lag_windows])
            for index in range(0, len(rows) - lag_windows)
        )
    elif lag_mode == "contiguous":
        rows_by_start = {parse_time(row.window_start): row for row in rows}
        row_pairs = (
            (
                row,
                rows_by_start.get(
                    parse_time(row.window_start) + timedelta(minutes=lag_windows * window_minutes)
                ),
            )
            for row in rows
        )
    else:
        raise ValueError(f"Unknown lag mode: {lag_mode}")

    for current, later in row_pairs:
        if later is None or current.dances < min_dances:
            continue
        predictor_value = getattr(current, predictor)
        outcome_value = getattr(later, outcome)
        if predictor_value is None or outcome_value is None:
            continue
        left.append(float(predictor_value))
        right.append(float(outcome_value))
    return left, right


def coupling_summaries(
    rows: Sequence[WindowSummary],
    predictors: Sequence[str],
    outcomes: Sequence[str],
    lag_windows: int,
    min_dances: int,
    window_minutes: int,
    lag_mode: str,
) -> list[CouplingSummary]:
    summaries: list[CouplingSummary] = []
    for predictor in predictors:
        for outcome in outcomes:
            left, right = lagged_pairs(
                rows,
                predictor,
                outcome,
                lag_windows,
                min_dances,
                window_minutes,
                lag_mode,
            )
            summaries.append(
                CouplingSummary(
                    predictor=predictor,
                    outcome=outcome,
                    lag_windows=lag_windows,
                    lag_mode=lag_mode,
                    observations=len(left),
                    pearson=pearson(left, right),
                    spearman=spearman(left, right),
                )
            )
    return summaries


def write_csv(path: Path, rows: Sequence[object]) -> None:
    if not rows:
        return
    fieldnames = list(asdict(rows[0]).keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def write_json(path: Path, payload: object) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dances-csv", required=True)
    parser.add_argument("--followers-csv", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--window-minutes", type=int, default=60)
    parser.add_argument("--lag-windows", type=int, default=1)
    parser.add_argument("--lag-mode", choices=["contiguous", "active-window"], default="contiguous")
    parser.add_argument("--spatial-bin-size", type=float, default=25.0)
    parser.add_argument("--min-dances", type=int, default=3)
    parser.add_argument(
        "--predictors",
        nargs="+",
        default=["dances", "follower_events", "follow_events", "follower_events_per_dance"],
    )
    parser.add_argument(
        "--outcomes",
        nargs="+",
        default=[
            "dancer_entropy",
            "feeder_entropy",
            "follower_entropy",
            "dance_spatial_entropy",
            "dominant_dancer_fraction",
            "dominant_feeder_fraction",
            "dominant_follower_fraction",
        ],
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    windows = summarize_windows(
        dances_path=Path(args.dances_csv),
        followers_path=Path(args.followers_csv),
        window_minutes=args.window_minutes,
        spatial_bin_size=args.spatial_bin_size,
    )
    couplings = coupling_summaries(
        windows,
        predictors=args.predictors,
        outcomes=args.outcomes,
        lag_windows=args.lag_windows,
        min_dances=args.min_dances,
        window_minutes=args.window_minutes,
        lag_mode=args.lag_mode,
    )

    write_csv(output_dir / "window_summaries.csv", windows)
    write_json(output_dir / "window_summaries.json", [asdict(row) for row in windows])
    write_csv(output_dir / "lagged_couplings.csv", couplings)
    write_json(output_dir / "lagged_couplings.json", [asdict(row) for row in couplings])
    write_json(output_dir / "analysis_parameters.json", vars(args))

    print(f"Wrote {len(windows)} windows and {len(couplings)} couplings to {output_dir}")
    ranked = sorted(
        [row for row in couplings if row.spearman is not None],
        key=lambda row: abs(row.spearman or 0.0),
        reverse=True,
    )
    for row in ranked[:10]:
        print(
            f"{row.predictor} -> {row.outcome}: "
            f"n={row.observations} pearson={row.pearson} spearman={row.spearman}"
        )


if __name__ == "__main__":
    main()
