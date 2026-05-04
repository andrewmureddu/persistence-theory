#!/usr/bin/env python3
"""Follower-sample nulls for Berlin honey-bee waggle recruitment data.

This companion analysis asks whether the lagged follower-channel result in
`bee_waggle_coupling_analysis.py` survives two mechanical nulls:

1. rarefaction, which computes follower entropy / concentration after drawing
   the same number of follower events from each later window; and
2. identity shuffling, which keeps each later window's event count and chosen
   day / feeder / dancer event-slot structure fixed while breaking the
   association between clock window and follower identity composition.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Callable, Sequence

from bee_waggle_coupling_analysis import (
    dominant_fraction,
    parse_time,
    pearson,
    shannon_from_counts,
    spearman,
    window_key,
)


@dataclass(frozen=True)
class FollowerWindow:
    window_start: str
    dances: int
    follower_events: int
    follow_events: int
    attendance_events: int
    follower_events_per_dance: float | None
    follower_entropy: float | None
    dominant_follower_fraction: float | None


@dataclass(frozen=True)
class FollowerEvent:
    follower_id: str
    label: str
    dancer_id: str
    feeder_cam_id: str


@dataclass(frozen=True)
class FollowerNullSummary:
    predictor: str
    outcome: str
    lag_windows: int
    lag_mode: str
    observations: int
    rarefaction_size: int | None
    rarefaction_replicates: int
    identity_permutations: int
    identity_shuffle_condition: str
    identity_shuffle_events: int
    identity_shuffle_strata: int
    identity_shuffle_singleton_strata: int
    raw_pearson: float | None
    raw_spearman: float | None
    rarefied_pearson: float | None
    rarefied_spearman: float | None
    identity_shuffle_pearson_mean: float | None
    identity_shuffle_pearson_sd: float | None
    identity_shuffle_spearman_mean: float | None
    identity_shuffle_spearman_sd: float | None
    identity_shuffle_pearson_p: float | None
    identity_shuffle_spearman_p: float | None


@dataclass(frozen=True)
class LagPair:
    current_start: datetime
    later_start: datetime
    current: FollowerWindow
    later: FollowerWindow
    later_follower_events: tuple[FollowerEvent, ...]

    @property
    def later_follower_ids(self) -> tuple[str, ...]:
        return tuple(event.follower_id for event in self.later_follower_events)


def read_dances(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["dance_id"]: row for row in csv.DictReader(handle)}


def summarize_follower_windows(
    dances_path: Path,
    followers_path: Path,
    window_minutes: int,
) -> tuple[list[FollowerWindow], dict[datetime, tuple[FollowerEvent, ...]]]:
    dance_by_id = read_dances(dances_path)
    dance_counts: Counter[datetime] = Counter()
    follower_events_by_window: dict[datetime, list[FollowerEvent]] = defaultdict(list)
    label_counts_by_window: dict[datetime, Counter[str]] = defaultdict(Counter)

    for dance in dance_by_id.values():
        dance_counts[window_key(parse_time(dance["ts_from"]), window_minutes)] += 1

    with followers_path.open(newline="", encoding="utf-8") as handle:
        for event in csv.DictReader(handle):
            dance = dance_by_id.get(event["dance_id"])
            if dance is None:
                continue
            start = window_key(parse_time(event["ts_from"]), window_minutes)
            follower_events_by_window[start].append(
                FollowerEvent(
                    follower_id=event["follower_id"],
                    label=event.get("label", ""),
                    dancer_id=dance.get("dancer_id", ""),
                    feeder_cam_id=dance.get("feeder_cam_id", ""),
                )
            )
            label_counts_by_window[start][event.get("label", "")] += 1

    windows: list[FollowerWindow] = []
    for start in sorted(set(dance_counts) | set(follower_events_by_window)):
        dances = dance_counts.get(start, 0)
        follower_ids = [event.follower_id for event in follower_events_by_window.get(start, [])]
        follower_counts = Counter(follower_ids)
        label_counts = label_counts_by_window.get(start, Counter())
        windows.append(
            FollowerWindow(
                window_start=start.isoformat(),
                dances=dances,
                follower_events=len(follower_ids),
                follow_events=label_counts.get("follower", 0),
                attendance_events=label_counts.get("attendance", 0),
                follower_events_per_dance=(len(follower_ids) / dances if dances else None),
                follower_entropy=shannon_from_counts(follower_counts),
                dominant_follower_fraction=dominant_fraction(follower_counts),
            )
        )

    return windows, {
        start: tuple(events)
        for start, events in follower_events_by_window.items()
    }


def parse_window_start(value: str) -> datetime:
    return datetime.fromisoformat(value)


def lagged_pairs(
    rows: Sequence[FollowerWindow],
    events_by_window: dict[datetime, tuple[FollowerEvent, ...]],
    lag_windows: int,
    window_minutes: int,
    lag_mode: str,
    min_dances: int,
) -> list[LagPair]:
    if lag_mode == "active-window":
        raw_pairs = [
            (rows[index], rows[index + lag_windows])
            for index in range(0, len(rows) - lag_windows)
        ]
    elif lag_mode == "contiguous":
        rows_by_start = {parse_window_start(row.window_start): row for row in rows}
        raw_pairs = []
        for row in rows:
            start = parse_window_start(row.window_start)
            later = rows_by_start.get(start + timedelta(minutes=lag_windows * window_minutes))
            if later is not None:
                raw_pairs.append((row, later))
    else:
        raise ValueError(f"Unknown lag mode: {lag_mode}")

    pairs: list[LagPair] = []
    for current, later in raw_pairs:
        if current.dances < min_dances or later.follower_events == 0:
            continue
        current_start = parse_window_start(current.window_start)
        later_start = parse_window_start(later.window_start)
        pairs.append(
            LagPair(
                current_start=current_start,
                later_start=later_start,
                current=current,
                later=later,
                later_follower_events=events_by_window.get(later_start, ()),
            )
        )
    return pairs


def metric_for_ids(ids: Sequence[str], outcome: str) -> float | None:
    counts = Counter(ids)
    if outcome == "follower_entropy":
        return shannon_from_counts(counts)
    if outcome == "dominant_follower_fraction":
        return dominant_fraction(counts)
    raise ValueError(f"Unsupported follower null outcome: {outcome}")


def row_value(row: FollowerWindow, field: str) -> float | None:
    value = getattr(row, field)
    if value is None:
        return None
    return float(value)


def rarefied_metric(
    ids: Sequence[str],
    outcome: str,
    sample_size: int,
    replicates: int,
    rng: random.Random,
) -> float | None:
    if sample_size <= 0 or len(ids) < sample_size:
        return None
    if len(ids) == sample_size:
        return metric_for_ids(ids, outcome)

    draws = max(1, replicates)
    values: list[float] = []
    ids_list = list(ids)
    for _ in range(draws):
        value = metric_for_ids(rng.sample(ids_list, sample_size), outcome)
        if value is not None:
            values.append(value)
    return statistics.fmean(values) if values else None


def choose_rarefaction_size(pairs: Sequence[LagPair], requested: int | None) -> int | None:
    available = [len(pair.later_follower_ids) for pair in pairs if pair.later_follower_ids]
    if not available:
        return None
    if requested is not None:
        return requested
    return min(available)


def finite_mean(values: Sequence[float | None]) -> float | None:
    clean = [value for value in values if value is not None and math.isfinite(value)]
    return statistics.fmean(clean) if clean else None


def finite_sd(values: Sequence[float | None]) -> float | None:
    clean = [value for value in values if value is not None and math.isfinite(value)]
    return statistics.stdev(clean) if len(clean) >= 2 else None


def shuffle_stratum(pair: LagPair, event: FollowerEvent, condition: str) -> tuple[str, ...]:
    day = pair.later_start.date().isoformat()
    if condition == "day":
        return (day,)
    if condition == "day-feeder":
        return (day, event.feeder_cam_id)
    if condition == "day-dancer":
        return (day, event.dancer_id)
    if condition == "day-dancer-feeder":
        return (day, event.dancer_id, event.feeder_cam_id)
    raise ValueError(f"Unknown identity shuffle condition: {condition}")


def identity_shuffle_diagnostics(
    pairs: Sequence[LagPair],
    condition: str,
) -> tuple[int, int, int]:
    strata_counts: Counter[tuple[str, ...]] = Counter()
    event_count = 0
    for pair in pairs:
        for event in pair.later_follower_events:
            strata_counts[shuffle_stratum(pair, event, condition)] += 1
            event_count += 1
    singleton_count = sum(1 for count in strata_counts.values() if count <= 1)
    return event_count, len(strata_counts), singleton_count


def identity_shuffle_correlations(
    pairs: Sequence[LagPair],
    left: Sequence[float],
    outcome: str,
    permutations: int,
    seed: int,
    condition: str,
    correlation_fn: Callable[[Sequence[float], Sequence[float]], float | None],
) -> tuple[float | None, float | None, float | None]:
    observed_right = [metric_for_ids(pair.later_follower_ids, outcome) for pair in pairs]
    if any(value is None for value in observed_right):
        return None, None, None

    observed = correlation_fn(left, [float(value) for value in observed_right if value is not None])
    if observed is None or permutations <= 0:
        return None, None, None

    slots_by_stratum: dict[tuple[str, ...], list[datetime]] = defaultdict(list)
    ids_by_stratum: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for pair in pairs:
        for event in pair.later_follower_events:
            stratum = shuffle_stratum(pair, event, condition)
            slots_by_stratum[stratum].append(pair.later_start)
            ids_by_stratum[stratum].append(event.follower_id)

    rng = random.Random(seed)
    null_correlations: list[float | None] = []
    exceedances = 1
    for _ in range(permutations):
        shuffled_ids_by_start: dict[datetime, list[str]] = defaultdict(list)
        for stratum, slots in slots_by_stratum.items():
            pool = ids_by_stratum[stratum][:]
            rng.shuffle(pool)
            for later_start, shuffled_id in zip(slots, pool):
                shuffled_ids_by_start[later_start].append(shuffled_id)

        shuffled_right = [
            metric_for_ids(shuffled_ids_by_start[pair.later_start], outcome)
            for pair in pairs
        ]
        if any(value is None for value in shuffled_right):
            continue
        shuffled_corr = correlation_fn(
            left,
            [float(value) for value in shuffled_right if value is not None],
        )
        null_correlations.append(shuffled_corr)
        if shuffled_corr is not None and abs(shuffled_corr) >= abs(observed):
            exceedances += 1

    return (
        finite_mean(null_correlations),
        finite_sd(null_correlations),
        exceedances / (permutations + 1),
    )


def null_summary(
    pairs: Sequence[LagPair],
    predictor: str,
    outcome: str,
    lag_windows: int,
    lag_mode: str,
    rarefaction_size: int | None,
    rarefaction_replicates: int,
    identity_permutations: int,
    identity_shuffle_condition: str,
    seed: int,
) -> FollowerNullSummary:
    usable_pairs: list[LagPair] = []
    left: list[float] = []
    raw_right: list[float] = []
    rarefied_right: list[float] = []
    rng = random.Random(seed)

    for pair in pairs:
        predictor_value = row_value(pair.current, predictor)
        raw_outcome = metric_for_ids(pair.later_follower_ids, outcome)
        if predictor_value is None or raw_outcome is None:
            continue

        rarefied_outcome = None
        if rarefaction_size is not None:
            rarefied_outcome = rarefied_metric(
                pair.later_follower_ids,
                outcome,
                rarefaction_size,
                rarefaction_replicates,
                rng,
            )
        if rarefaction_size is not None and rarefied_outcome is None:
            continue

        usable_pairs.append(pair)
        left.append(predictor_value)
        raw_right.append(raw_outcome)
        if rarefied_outcome is not None:
            rarefied_right.append(rarefied_outcome)

    shuffle_events, shuffle_strata, shuffle_singleton_strata = identity_shuffle_diagnostics(
        usable_pairs,
        identity_shuffle_condition,
    )
    pearson_mean, pearson_sd, pearson_p = identity_shuffle_correlations(
        usable_pairs,
        left,
        outcome,
        identity_permutations,
        seed + 17,
        identity_shuffle_condition,
        pearson,
    )
    spearman_mean, spearman_sd, spearman_p = identity_shuffle_correlations(
        usable_pairs,
        left,
        outcome,
        identity_permutations,
        seed + 31,
        identity_shuffle_condition,
        spearman,
    )

    return FollowerNullSummary(
        predictor=predictor,
        outcome=outcome,
        lag_windows=lag_windows,
        lag_mode=lag_mode,
        observations=len(left),
        rarefaction_size=rarefaction_size,
        rarefaction_replicates=rarefaction_replicates,
        identity_permutations=identity_permutations,
        identity_shuffle_condition=identity_shuffle_condition,
        identity_shuffle_events=shuffle_events,
        identity_shuffle_strata=shuffle_strata,
        identity_shuffle_singleton_strata=shuffle_singleton_strata,
        raw_pearson=pearson(left, raw_right),
        raw_spearman=spearman(left, raw_right),
        rarefied_pearson=pearson(left, rarefied_right) if rarefied_right else None,
        rarefied_spearman=spearman(left, rarefied_right) if rarefied_right else None,
        identity_shuffle_pearson_mean=pearson_mean,
        identity_shuffle_pearson_sd=pearson_sd,
        identity_shuffle_spearman_mean=spearman_mean,
        identity_shuffle_spearman_sd=spearman_sd,
        identity_shuffle_pearson_p=pearson_p,
        identity_shuffle_spearman_p=spearman_p,
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
    parser.add_argument("--min-dances", type=int, default=3)
    parser.add_argument("--rarefaction-size", type=int)
    parser.add_argument("--rarefaction-replicates", type=int, default=1000)
    parser.add_argument("--identity-permutations", type=int, default=1000)
    parser.add_argument(
        "--identity-shuffle-condition",
        choices=["day", "day-feeder", "day-dancer", "day-dancer-feeder"],
        default="day",
        help=(
            "Follower identities are shuffled only within this later-window "
            "condition while preserving each later window's event slots."
        ),
    )
    parser.add_argument("--seed", type=int, default=20260501)
    parser.add_argument(
        "--predictors",
        nargs="+",
        default=["dances", "follower_events", "follow_events", "follower_events_per_dance"],
    )
    parser.add_argument(
        "--outcomes",
        nargs="+",
        default=["follower_entropy", "dominant_follower_fraction"],
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
    rarefaction_size = choose_rarefaction_size(pairs, args.rarefaction_size)

    summaries = [
        null_summary(
            pairs=pairs,
            predictor=predictor,
            outcome=outcome,
            lag_windows=args.lag_windows,
            lag_mode=args.lag_mode,
            rarefaction_size=rarefaction_size,
            rarefaction_replicates=args.rarefaction_replicates,
            identity_permutations=args.identity_permutations,
            identity_shuffle_condition=args.identity_shuffle_condition,
            seed=args.seed + predictor_index * 1000 + outcome_index * 100,
        )
        for predictor_index, predictor in enumerate(args.predictors)
        for outcome_index, outcome in enumerate(args.outcomes)
    ]

    write_csv(output_dir / "follower_null_summaries.csv", summaries)
    write_json(output_dir / "follower_null_summaries.json", [asdict(row) for row in summaries])
    write_csv(output_dir / "window_follower_summaries.csv", windows)
    write_json(output_dir / "window_follower_summaries.json", [asdict(row) for row in windows])
    write_json(
        output_dir / "analysis_parameters.json",
        {
            **vars(args),
            "resolved_rarefaction_size": rarefaction_size,
            "lagged_pair_count": len(pairs),
        },
    )

    print(
        f"Wrote {len(summaries)} follower null summaries "
        f"from {len(pairs)} lagged pairs to {output_dir}"
    )
    ranked = sorted(
        [row for row in summaries if row.rarefied_spearman is not None],
        key=lambda row: abs(row.rarefied_spearman or 0.0),
        reverse=True,
    )
    for row in ranked[:10]:
        print(
            f"{row.predictor} -> {row.outcome}: "
            f"n={row.observations} raw_spearman={row.raw_spearman} "
            f"rarefied_spearman={row.rarefied_spearman} "
            f"identity_condition={row.identity_shuffle_condition} "
            f"identity_p={row.identity_shuffle_spearman_p}"
        )


if __name__ == "__main__":
    main()
