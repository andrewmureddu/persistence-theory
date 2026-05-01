#!/usr/bin/env python3
"""Controlled lag analysis for Berlin honey-bee waggle recruitment data.

This is the second-pass companion to `bee_waggle_coupling_analysis.py`.
It asks whether lagged dance/follower signals survive simple observational
controls: baseline outcome level, current dance count, next-window sampling
effort, hour-of-day, and day fixed effects.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Sequence

from bee_waggle_coupling_analysis import (
    WindowSummary,
    pearson,
    ranks,
    spearman,
    summarize_windows,
)


@dataclass(frozen=True)
class ControlledCouplingSummary:
    predictor: str
    outcome: str
    lag_windows: int
    lag_mode: str
    observations: int
    model_rank: int
    controls: str
    raw_pearson: float | None
    raw_spearman: float | None
    partial_pearson: float | None
    partial_spearman: float | None
    partial_pearson_permutation_p: float | None
    partial_spearman_permutation_p: float | None


def parse_window_start(value: str) -> datetime:
    return datetime.fromisoformat(value)


def row_value(row: WindowSummary, field: str) -> float | None:
    value = getattr(row, field)
    if value is None:
        return None
    return float(value)


def outcome_exposure(row: WindowSummary, outcome: str) -> float:
    if "follower" in outcome:
        return float(row.follower_events)
    return float(row.dances)


def hour_terms(timestamp: datetime) -> tuple[float, float]:
    hour = timestamp.hour + timestamp.minute / 60.0 + timestamp.second / 3600.0
    angle = (2.0 * math.pi * hour) / 24.0
    return math.sin(angle), math.cos(angle)


def standardize_columns(columns: Sequence[Sequence[float]]) -> list[list[float]]:
    standardized: list[list[float]] = []
    for column in columns:
        values = [float(value) for value in column]
        if len(values) < 2:
            continue
        mean = statistics.fmean(values)
        variance = sum((value - mean) ** 2 for value in values) / len(values)
        if variance < 1e-12:
            continue
        scale = math.sqrt(variance)
        standardized.append([(value - mean) / scale for value in values])
    return standardized


def transpose(matrix: Sequence[Sequence[float]]) -> list[list[float]]:
    return [list(column) for column in zip(*matrix)]


def solve_linear_system(matrix: list[list[float]], values: list[float]) -> list[float] | None:
    size = len(values)
    augmented = [row[:] + [values[index]] for index, row in enumerate(matrix)]

    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-10:
            return None
        if pivot != column:
            augmented[column], augmented[pivot] = augmented[pivot], augmented[column]

        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor == 0:
                continue
            augmented[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(augmented[row], augmented[column])
            ]

    return [row[-1] for row in augmented]


def residualize(values: Sequence[float], controls: Sequence[Sequence[float]]) -> tuple[list[float], int]:
    usable_controls = standardize_columns(controls)
    design = [[1.0] + [column[index] for column in usable_controls] for index in range(len(values))]
    design_t = transpose(design)

    xtx: list[list[float]] = []
    for left in design_t:
        xtx.append([sum(a * b for a, b in zip(left, right)) for right in design_t])

    # Tiny ridge on non-intercept terms keeps near-collinear day/time controls
    # from making the first-pass diagnostic numerically fragile.
    for index in range(1, len(xtx)):
        xtx[index][index] += 1e-8

    xty = [sum(a * b for a, b in zip(column, values)) for column in design_t]
    coefficients = solve_linear_system(xtx, xty)
    if coefficients is None:
        return list(values), 1

    residuals: list[float] = []
    for row, observed in zip(design, values):
        fitted = sum(coefficient * value for coefficient, value in zip(coefficients, row))
        residuals.append(observed - fitted)
    return residuals, len(design[0])


def permutation_p(
    left: Sequence[float],
    right: Sequence[float],
    days: Sequence[str],
    permutations: int,
    seed: int,
) -> float | None:
    observed = pearson(left, right)
    if observed is None or permutations <= 0:
        return None

    grouped_indexes: dict[str, list[int]] = defaultdict(list)
    for index, day in enumerate(days):
        grouped_indexes[day].append(index)

    rng = random.Random(seed)
    exceedances = 1
    mutable_left = list(left)
    for _ in range(permutations):
        shuffled = mutable_left[:]
        for indexes in grouped_indexes.values():
            values = [shuffled[index] for index in indexes]
            rng.shuffle(values)
            for index, value in zip(indexes, values):
                shuffled[index] = value
        permuted = pearson(shuffled, right)
        if permuted is not None and abs(permuted) >= abs(observed):
            exceedances += 1
    return exceedances / (permutations + 1)


def day_dummy_columns(days: Sequence[str]) -> list[list[float]]:
    unique_days = sorted(set(days))
    return [[1.0 if day == unique_day else 0.0 for day in days] for unique_day in unique_days[1:]]


def lagged_row_pairs(
    rows: Sequence[WindowSummary],
    lag_windows: int,
    window_minutes: int,
    lag_mode: str,
) -> list[tuple[WindowSummary, WindowSummary]]:
    if lag_mode == "active-window":
        return [
            (rows[index], rows[index + lag_windows])
            for index in range(0, len(rows) - lag_windows)
        ]
    if lag_mode == "contiguous":
        rows_by_start = {parse_window_start(row.window_start): row for row in rows}
        pairs: list[tuple[WindowSummary, WindowSummary]] = []
        for row in rows:
            target = parse_window_start(row.window_start) + timedelta(minutes=lag_windows * window_minutes)
            later = rows_by_start.get(target)
            if later is not None:
                pairs.append((row, later))
        return pairs
    raise ValueError(f"Unknown lag mode: {lag_mode}")


def controlled_summary(
    rows: Sequence[WindowSummary],
    predictor: str,
    outcome: str,
    lag_windows: int,
    window_minutes: int,
    lag_mode: str,
    min_dances: int,
    day_fixed_effects: bool,
    permutations: int,
    seed: int,
) -> ControlledCouplingSummary:
    left: list[float] = []
    right: list[float] = []
    days: list[str] = []
    baseline_outcome: list[float] = []
    current_dances: list[float] = []
    next_exposure: list[float] = []
    hour_sin: list[float] = []
    hour_cos: list[float] = []

    for current, later in lagged_row_pairs(rows, lag_windows, window_minutes, lag_mode):
        if current.dances < min_dances:
            continue

        predictor_value = row_value(current, predictor)
        outcome_value = row_value(later, outcome)
        baseline_value = row_value(current, outcome)
        exposure_value = outcome_exposure(later, outcome)
        if (
            predictor_value is None
            or outcome_value is None
            or baseline_value is None
            or exposure_value <= 0
        ):
            continue

        start = parse_window_start(current.window_start)
        sine, cosine = hour_terms(start)
        left.append(predictor_value)
        right.append(outcome_value)
        days.append(start.date().isoformat())
        baseline_outcome.append(baseline_value)
        current_dances.append(float(current.dances))
        next_exposure.append(exposure_value)
        hour_sin.append(sine)
        hour_cos.append(cosine)

    controls = [
        baseline_outcome,
        current_dances,
        next_exposure,
        hour_sin,
        hour_cos,
    ]
    if day_fixed_effects:
        controls.extend(day_dummy_columns(days))
    residual_left, model_rank = residualize(left, controls) if left else ([], 0)
    residual_right, _ = residualize(right, controls) if right else ([], 0)

    rank_left = ranks(left) if left else []
    rank_right = ranks(right) if right else []
    residual_rank_left, _ = residualize(rank_left, controls) if rank_left else ([], 0)
    residual_rank_right, _ = residualize(rank_right, controls) if rank_right else ([], 0)

    partial_pearson = pearson(residual_left, residual_right)
    partial_spearman = pearson(residual_rank_left, residual_rank_right)

    control_names = [
        f"baseline_{outcome}",
        "current_dances",
        f"next_{'follower_events' if 'follower' in outcome else 'dances'}",
        "hour_sin",
        "hour_cos",
    ]
    if day_fixed_effects:
        control_names.append("day_fixed_effects")

    return ControlledCouplingSummary(
        predictor=predictor,
        outcome=outcome,
        lag_windows=lag_windows,
        lag_mode=lag_mode,
        observations=len(left),
        model_rank=model_rank,
        controls=";".join(control_names),
        raw_pearson=pearson(left, right),
        raw_spearman=spearman(left, right),
        partial_pearson=partial_pearson,
        partial_spearman=partial_spearman,
        partial_pearson_permutation_p=permutation_p(
            residual_left,
            residual_right,
            days,
            permutations,
            seed,
        ),
        partial_spearman_permutation_p=permutation_p(
            residual_rank_left,
            residual_rank_right,
            days,
            permutations,
            seed + 1,
        ),
    )


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
    parser.add_argument("--day-fixed-effects", action="store_true")
    parser.add_argument("--permutations", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260501)
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
    summaries = [
        controlled_summary(
            rows=windows,
            predictor=predictor,
            outcome=outcome,
            lag_windows=args.lag_windows,
            window_minutes=args.window_minutes,
            lag_mode=args.lag_mode,
            min_dances=args.min_dances,
            day_fixed_effects=args.day_fixed_effects,
            permutations=args.permutations,
            seed=args.seed + predictor_index * 100 + outcome_index,
        )
        for predictor_index, predictor in enumerate(args.predictors)
        for outcome_index, outcome in enumerate(args.outcomes)
    ]

    write_csv(output_dir / "controlled_lagged_couplings.csv", summaries)
    write_json(output_dir / "controlled_lagged_couplings.json", [asdict(row) for row in summaries])
    write_json(output_dir / "analysis_parameters.json", vars(args))

    print(f"Wrote {len(summaries)} controlled couplings to {output_dir}")
    ranked = sorted(
        [row for row in summaries if row.partial_spearman is not None],
        key=lambda row: abs(row.partial_spearman or 0.0),
        reverse=True,
    )
    for row in ranked[:10]:
        print(
            f"{row.predictor} -> {row.outcome}: "
            f"n={row.observations} raw_spearman={row.raw_spearman} "
            f"partial_spearman={row.partial_spearman} "
            f"p={row.partial_spearman_permutation_p}"
        )


if __name__ == "__main__":
    main()
