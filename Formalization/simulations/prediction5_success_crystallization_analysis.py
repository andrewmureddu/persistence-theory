#!/usr/bin/env python3
"""Analyze Prediction 5 in the Boolean-network simulation outputs.

Prediction 5 asks whether success is coupled to crystallization. For the
Kauffman-domain simulator, correctness is the success proxy and frozen fraction
is the crystallization proxy. This analyzer reads `generation_metrics.csv`
written by `prediction9_boolean_network.py` and reports within-replicate
correlations between success and cumulative frozen-fraction increase.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class ReplicateAnalysis:
    regime: str
    replicate: int
    observations: int
    lag: int
    success_delta_frozen_pearson: float | None
    success_delta_frozen_spearman: float | None
    lagged_success_to_delta_frozen_pearson: float | None
    reverse_delta_frozen_to_success_pearson: float | None
    final_success: float
    final_delta_frozen: float


def safe_float(value: str) -> float | None:
    if value == "":
        return None
    return float(value)


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


def exact_positive_tail(successes: int, trials: int) -> float | None:
    if trials <= 0:
        return None
    probability = 0.0
    for k in range(successes, trials + 1):
        probability += math.comb(trials, k) * (0.5 ** trials)
    return probability


def summarize_numbers(values: Iterable[float | None]) -> dict[str, float | int | None]:
    clean = [value for value in values if value is not None]
    if not clean:
        return {
            "count": 0,
            "mean": None,
            "median": None,
            "positive_fraction": None,
            "positive_tail_p_under_sign_null": None,
        }
    positives = sum(1 for value in clean if value > 0)
    return {
        "count": len(clean),
        "mean": statistics.fmean(clean),
        "median": statistics.median(clean),
        "positive_fraction": positives / len(clean),
        "positive_tail_p_under_sign_null": exact_positive_tail(positives, len(clean)),
    }


def read_generation_metrics(path: Path) -> dict[tuple[str, int], list[dict[str, float | int | str | None]]]:
    grouped: dict[tuple[str, int], list[dict[str, float | int | str | None]]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            regime = row["regime"]
            replicate = int(row["replicate"])
            parsed: dict[str, float | int | str | None] = {
                "regime": regime,
                "replicate": replicate,
                "generation": int(row["generation"]),
            }
            for key, value in row.items():
                if key in {"regime", "replicate", "generation"}:
                    continue
                parsed[key] = safe_float(value)
            grouped.setdefault((regime, replicate), []).append(parsed)

    for rows in grouped.values():
        rows.sort(key=lambda item: int(item["generation"]))
    return grouped


def analyze_replicate(
    regime: str,
    replicate: int,
    rows: Sequence[dict[str, float | int | str | None]],
    success_column: str,
    frozen_column: str,
    lag: int,
) -> ReplicateAnalysis | None:
    success: list[float] = []
    frozen: list[float] = []
    for row in rows:
        success_value = row.get(success_column)
        frozen_value = row.get(frozen_column)
        if isinstance(success_value, float) and isinstance(frozen_value, float):
            success.append(success_value)
            frozen.append(frozen_value)

    if len(success) < 3:
        return None

    baseline_frozen = frozen[0]
    delta_frozen = [value - baseline_frozen for value in frozen]
    effective_lag = min(lag, len(success) - 2)

    if effective_lag <= 0:
        lagged_success = []
        future_delta_frozen = []
        current_delta_frozen = []
        future_success = []
    else:
        lagged_success = success[:-effective_lag]
        future_delta_frozen = delta_frozen[effective_lag:]
        current_delta_frozen = delta_frozen[:-effective_lag]
        future_success = success[effective_lag:]

    return ReplicateAnalysis(
        regime=regime,
        replicate=replicate,
        observations=len(success),
        lag=effective_lag,
        success_delta_frozen_pearson=pearson(success, delta_frozen),
        success_delta_frozen_spearman=spearman(success, delta_frozen),
        lagged_success_to_delta_frozen_pearson=pearson(lagged_success, future_delta_frozen),
        reverse_delta_frozen_to_success_pearson=pearson(current_delta_frozen, future_success),
        final_success=success[-1],
        final_delta_frozen=delta_frozen[-1],
    )


def aggregate_analyses(analyses: Sequence[ReplicateAnalysis]) -> dict[str, object]:
    by_regime: dict[str, list[ReplicateAnalysis]] = {}
    for analysis in analyses:
        by_regime.setdefault(analysis.regime, []).append(analysis)

    aggregate: dict[str, object] = {}
    for regime, regime_analyses in by_regime.items():
        final_success = [analysis.final_success for analysis in regime_analyses]
        final_delta = [analysis.final_delta_frozen for analysis in regime_analyses]
        aggregate[regime] = {
            "replicates": len(regime_analyses),
            "success_delta_frozen_pearson": summarize_numbers(
                analysis.success_delta_frozen_pearson for analysis in regime_analyses
            ),
            "success_delta_frozen_spearman": summarize_numbers(
                analysis.success_delta_frozen_spearman for analysis in regime_analyses
            ),
            "lagged_success_to_delta_frozen_pearson": summarize_numbers(
                analysis.lagged_success_to_delta_frozen_pearson for analysis in regime_analyses
            ),
            "reverse_delta_frozen_to_success_pearson": summarize_numbers(
                analysis.reverse_delta_frozen_to_success_pearson for analysis in regime_analyses
            ),
            "cross_replicate_final_success_delta_frozen_pearson": pearson(final_success, final_delta),
            "mean_final_success": statistics.fmean(final_success),
            "mean_final_delta_frozen": statistics.fmean(final_delta),
        }
    return aggregate


def write_csv(path: Path, analyses: Iterable[ReplicateAnalysis]) -> None:
    analyses = list(analyses)
    if not analyses:
        return
    fieldnames = list(asdict(analyses[0]).keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for analysis in analyses:
            writer.writerow(asdict(analysis))


def write_json(path: Path, payload: object) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-csv",
        required=True,
        help="Path to generation_metrics.csv from prediction9_boolean_network.py.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory for Prediction 5 analysis outputs.",
    )
    parser.add_argument(
        "--success-column",
        default="mean_correctness",
        help="Generation metric to use as the success proxy.",
    )
    parser.add_argument(
        "--frozen-column",
        default="mean_frozen_fraction",
        help="Generation metric to use as the crystallization proxy.",
    )
    parser.add_argument(
        "--lag",
        type=int,
        default=5,
        help="Generation lag for the directional success-to-future-crystallization readout.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_csv = Path(args.input_csv)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    grouped = read_generation_metrics(input_csv)
    analyses = [
        analysis
        for (regime, replicate), rows in grouped.items()
        if (
            analysis := analyze_replicate(
                regime=regime,
                replicate=replicate,
                rows=rows,
                success_column=args.success_column,
                frozen_column=args.frozen_column,
                lag=args.lag,
            )
        )
        is not None
    ]

    aggregate = aggregate_analyses(analyses)
    write_csv(output_dir / "replicate_analysis.csv", analyses)
    write_json(
        output_dir / "analysis_parameters.json",
        {
            "input_csv": str(input_csv),
            "success_column": args.success_column,
            "frozen_column": args.frozen_column,
            "lag": args.lag,
        },
    )
    write_json(output_dir / "aggregate_analysis.json", aggregate)

    print("Prediction 5 success-crystallization analysis complete.")
    print(f"Output directory: {output_dir}")
    for regime, summary in aggregate.items():
        current = summary["success_delta_frozen_pearson"]
        lagged = summary["lagged_success_to_delta_frozen_pearson"]
        reverse = summary["reverse_delta_frozen_to_success_pearson"]
        print(
            f"{regime}: "
            f"current_mean_r={current['mean']} "
            f"current_positive_fraction={current['positive_fraction']} "
            f"lagged_mean_r={lagged['mean']} "
            f"reverse_mean_r={reverse['mean']}"
        )


if __name__ == "__main__":
    main()
