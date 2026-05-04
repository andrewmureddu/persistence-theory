#!/usr/bin/env python3
"""Composition-driver diagnostics for Berlin honey-bee follower nulls.

The conditioned follower-identity shuffles suggest that the headline one-hour
follower broadening is explainable by day / feeder / dancer composition. This
script asks which strata line up with the current-window predictors strongly
enough to create that artifact.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Sequence

from bee_follower_null_analysis import (
    LagPair,
    lagged_pairs,
    metric_for_ids,
    row_value,
    shuffle_stratum,
    summarize_follower_windows,
)
from bee_waggle_coupling_analysis import pearson, spearman


CONDITION_LABELS = {
    "day": ("day",),
    "day-feeder": ("day", "feeder"),
    "day-dancer": ("day", "dancer"),
    "day-dancer-feeder": ("day", "dancer", "feeder"),
}


@dataclass(frozen=True)
class LagPairStratumShare:
    condition: str
    stratum: str
    current_start: str
    later_start: str
    later_follower_events: int
    stratum_events: int
    stratum_event_fraction: float
    current_dances: int
    current_follower_events_per_dance: float | None
    current_follow_events: int
    later_follower_entropy: float | None
    later_dominant_follower_fraction: float | None


@dataclass(frozen=True)
class StratumDriverSummary:
    condition: str
    stratum: str
    predictor: str
    lag_pairs: int
    event_slots: int
    total_event_slots: int
    event_fraction: float
    pair_coverage: float
    share_mean: float
    share_max: float
    pooled_follower_entropy: float | None
    pooled_dominant_follower_fraction: float | None
    global_follower_entropy: float | None
    global_dominant_follower_fraction: float | None
    mean_predictor_present: float | None
    mean_predictor_absent: float | None
    predictor_share_pearson: float | None
    predictor_share_spearman: float | None
    entropy_driver_score: float | None
    dominance_driver_score: float | None


def finite_mean(values: Sequence[float | None]) -> float | None:
    clean = [value for value in values if value is not None and math.isfinite(value)]
    return statistics.fmean(clean) if clean else None


def sample_covariance(left: Sequence[float], right: Sequence[float]) -> float | None:
    if len(left) != len(right) or len(left) < 2:
        return None
    left_mean = statistics.fmean(left)
    right_mean = statistics.fmean(right)
    return sum((x - left_mean) * (y - right_mean) for x, y in zip(left, right)) / (len(left) - 1)


def format_stratum(condition: str, key: tuple[str, ...]) -> str:
    labels = CONDITION_LABELS[condition]
    return " | ".join(f"{label}={value or 'NA'}" for label, value in zip(labels, key))


def stratum_counts_for_pair(pair: LagPair, condition: str) -> Counter[tuple[str, ...]]:
    counts: Counter[tuple[str, ...]] = Counter()
    for event in pair.later_follower_events:
        counts[shuffle_stratum(pair, event, condition)] += 1
    return counts


def stratum_ids(
    pairs: Sequence[LagPair],
    condition: str,
) -> dict[tuple[str, ...], list[str]]:
    ids_by_stratum: dict[tuple[str, ...], list[str]] = {}
    for pair in pairs:
        for event in pair.later_follower_events:
            ids_by_stratum.setdefault(shuffle_stratum(pair, event, condition), []).append(event.follower_id)
    return ids_by_stratum


def present_mean(
    predictor_values: Sequence[float],
    shares: Sequence[float],
    present: bool,
) -> float | None:
    if present:
        return finite_mean([value for value, share in zip(predictor_values, shares) if share > 0.0])
    return finite_mean([value for value, share in zip(predictor_values, shares) if share == 0.0])


def driver_summaries(
    pairs: Sequence[LagPair],
    predictors: Sequence[str],
    condition: str,
) -> tuple[list[LagPairStratumShare], list[StratumDriverSummary]]:
    ids_by_stratum = stratum_ids(pairs, condition)
    all_ids = [event.follower_id for pair in pairs for event in pair.later_follower_events]
    total_event_slots = len(all_ids)
    global_entropy = metric_for_ids(all_ids, "follower_entropy")
    global_dominance = metric_for_ids(all_ids, "dominant_follower_fraction")
    pair_counts = [stratum_counts_for_pair(pair, condition) for pair in pairs]
    all_strata = sorted(ids_by_stratum)

    pair_rows: list[LagPairStratumShare] = []
    for pair, counts in zip(pairs, pair_counts):
        later_total = len(pair.later_follower_ids)
        for key, count in sorted(counts.items()):
            pair_rows.append(
                LagPairStratumShare(
                    condition=condition,
                    stratum=format_stratum(condition, key),
                    current_start=pair.current_start.isoformat(),
                    later_start=pair.later_start.isoformat(),
                    later_follower_events=later_total,
                    stratum_events=count,
                    stratum_event_fraction=(count / later_total if later_total else 0.0),
                    current_dances=pair.current.dances,
                    current_follower_events_per_dance=pair.current.follower_events_per_dance,
                    current_follow_events=pair.current.follow_events,
                    later_follower_entropy=metric_for_ids(pair.later_follower_ids, "follower_entropy"),
                    later_dominant_follower_fraction=metric_for_ids(
                        pair.later_follower_ids,
                        "dominant_follower_fraction",
                    ),
                )
            )

    summary_rows: list[StratumDriverSummary] = []
    for key in all_strata:
        ids = ids_by_stratum[key]
        event_slots = len(ids)
        pooled_entropy = metric_for_ids(ids, "follower_entropy")
        pooled_dominance = metric_for_ids(ids, "dominant_follower_fraction")
        shares_all = [
            counts.get(key, 0) / len(pair.later_follower_ids)
            if pair.later_follower_ids
            else 0.0
            for pair, counts in zip(pairs, pair_counts)
        ]
        pair_coverage = sum(1 for share in shares_all if share > 0.0) / len(pairs) if pairs else 0.0

        for predictor in predictors:
            usable_left: list[float] = []
            usable_shares: list[float] = []
            for pair, share in zip(pairs, shares_all):
                predictor_value = row_value(pair.current, predictor)
                if predictor_value is None:
                    continue
                usable_left.append(predictor_value)
                usable_shares.append(share)

            covariance = sample_covariance(usable_left, usable_shares)
            entropy_delta = (
                pooled_entropy - global_entropy
                if pooled_entropy is not None and global_entropy is not None
                else None
            )
            dominance_delta = (
                pooled_dominance - global_dominance
                if pooled_dominance is not None and global_dominance is not None
                else None
            )
            summary_rows.append(
                StratumDriverSummary(
                    condition=condition,
                    stratum=format_stratum(condition, key),
                    predictor=predictor,
                    lag_pairs=len(usable_left),
                    event_slots=event_slots,
                    total_event_slots=total_event_slots,
                    event_fraction=(event_slots / total_event_slots if total_event_slots else 0.0),
                    pair_coverage=pair_coverage,
                    share_mean=statistics.fmean(usable_shares) if usable_shares else 0.0,
                    share_max=max(usable_shares) if usable_shares else 0.0,
                    pooled_follower_entropy=pooled_entropy,
                    pooled_dominant_follower_fraction=pooled_dominance,
                    global_follower_entropy=global_entropy,
                    global_dominant_follower_fraction=global_dominance,
                    mean_predictor_present=present_mean(usable_left, usable_shares, present=True),
                    mean_predictor_absent=present_mean(usable_left, usable_shares, present=False),
                    predictor_share_pearson=pearson(usable_left, usable_shares),
                    predictor_share_spearman=spearman(usable_left, usable_shares),
                    entropy_driver_score=(
                        covariance * entropy_delta
                        if covariance is not None and entropy_delta is not None
                        else None
                    ),
                    dominance_driver_score=(
                        covariance * dominance_delta
                        if covariance is not None and dominance_delta is not None
                        else None
                    ),
                )
            )

    return pair_rows, summary_rows


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
    parser.add_argument("--min-dances", type=int, default=3)
    parser.add_argument(
        "--min-later-follower-events",
        type=int,
        default=50,
        help="Filter to the same event-rich lag pairs used by the 50-event rarefaction headline.",
    )
    parser.add_argument(
        "--conditions",
        nargs="+",
        choices=sorted(CONDITION_LABELS),
        default=["day", "day-feeder", "day-dancer", "day-dancer-feeder"],
    )
    parser.add_argument(
        "--predictors",
        nargs="+",
        default=["follower_events_per_dance", "follow_events"],
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    windows, events_by_window = summarize_follower_windows(
        dances_path=Path(args.dances_csv),
        followers_path=Path(args.followers_csv),
        window_minutes=args.window_minutes,
    )
    pairs = lagged_pairs(
        rows=windows,
        events_by_window=events_by_window,
        lag_windows=args.lag_windows,
        window_minutes=args.window_minutes,
        lag_mode=args.lag_mode,
        min_dances=args.min_dances,
    )
    usable_pairs = [
        pair for pair in pairs
        if len(pair.later_follower_ids) >= args.min_later_follower_events
    ]

    all_pair_rows: list[LagPairStratumShare] = []
    all_summary_rows: list[StratumDriverSummary] = []
    for condition in args.conditions:
        pair_rows, summary_rows = driver_summaries(
            pairs=usable_pairs,
            predictors=args.predictors,
            condition=condition,
        )
        all_pair_rows.extend(pair_rows)
        all_summary_rows.extend(summary_rows)

    write_csv(output_dir / "lag_pair_stratum_shares.csv", all_pair_rows)
    write_json(output_dir / "lag_pair_stratum_shares.json", [asdict(row) for row in all_pair_rows])
    write_csv(output_dir / "stratum_driver_summaries.csv", all_summary_rows)
    write_json(output_dir / "stratum_driver_summaries.json", [asdict(row) for row in all_summary_rows])
    write_json(
        output_dir / "analysis_parameters.json",
        {
            **vars(args),
            "raw_lagged_pair_count": len(pairs),
            "usable_lagged_pair_count": len(usable_pairs),
        },
    )

    print(
        f"Wrote {len(all_summary_rows)} stratum-driver rows "
        f"from {len(usable_pairs)} lagged pairs to {output_dir}"
    )
    for condition in args.conditions:
        condition_rows = [
            row for row in all_summary_rows
            if row.condition == condition and row.predictor == args.predictors[0]
        ]
        ranked = sorted(
            condition_rows,
            key=lambda row: abs(row.entropy_driver_score or 0.0),
            reverse=True,
        )
        print(f"\nTop {condition} entropy-driver strata for {args.predictors[0]}:")
        for row in ranked[:5]:
            print(
                f"{row.stratum}: events={row.event_slots}, "
                f"share_corr={row.predictor_share_spearman}, "
                f"entropy={row.pooled_follower_entropy}, "
                f"entropy_driver={row.entropy_driver_score}"
            )


if __name__ == "__main__":
    main()
