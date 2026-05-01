#!/usr/bin/env python3
"""First-pass ACP observables for social-insect datasets.

The script is intentionally dependency-free so it can run on raw CSV exports
before we know each dataset's final schema. It currently supports two families:

- waggle-phase summaries: angular entropy, spatial entropy, and dance density;
- interaction summaries: interaction rate, actor entropy, and edge entropy.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class WaggleWindow:
    window_start: str
    observations: int
    angular_entropy: float | None
    angular_concentration: float | None
    spatial_entropy: float | None
    dominant_spatial_bin_fraction: float | None


@dataclass(frozen=True)
class InteractionWindow:
    window_start: str
    interactions: int
    actor_entropy: float | None
    edge_entropy: float | None
    dominant_actor_fraction: float | None
    dominant_edge_fraction: float | None


def parse_time(value: str) -> datetime:
    normalized = value.strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        for fmt in ("%Y-%m-%d %H:%M:%S", "%m/%d/%Y %H:%M:%S", "%Y-%m-%d %H:%M"):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue
    raise ValueError(f"Could not parse timestamp: {value!r}")


def window_key(timestamp: datetime, minutes: int) -> datetime:
    absolute_minutes = int(timestamp.timestamp() // 60)
    bucket = (absolute_minutes // minutes) * minutes
    return datetime.fromtimestamp(bucket * 60, tz=timestamp.tzinfo)


def shannon_from_counts(counts: Counter[object]) -> float | None:
    total = sum(counts.values())
    if total == 0:
        return None
    entropy = 0.0
    for count in counts.values():
        probability = count / total
        entropy -= probability * math.log(probability)
    return entropy


def dominant_fraction(counts: Counter[object]) -> float | None:
    total = sum(counts.values())
    if total == 0:
        return None
    return max(counts.values()) / total


def circular_concentration(angles: Sequence[float]) -> float | None:
    if not angles:
        return None
    x = sum(math.cos(angle) for angle in angles)
    y = sum(math.sin(angle) for angle in angles)
    return math.sqrt(x * x + y * y) / len(angles)


def angle_bin(angle: float, bins: int) -> int:
    normalized = angle % (2.0 * math.pi)
    return min(bins - 1, int((normalized / (2.0 * math.pi)) * bins))


def spatial_bin(x: float, y: float, bin_size: float) -> tuple[int, int]:
    return (math.floor(x / bin_size), math.floor(y / bin_size))


def read_csv_rows(path: Path) -> Iterable[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        yield from csv.DictReader(handle)


def analyze_waggle(args: argparse.Namespace) -> list[WaggleWindow]:
    grouped: dict[datetime, list[dict[str, str]]] = {}
    for row in read_csv_rows(Path(args.input_csv)):
        if not row.get(args.timestamp_column):
            continue
        timestamp = parse_time(row[args.timestamp_column])
        grouped.setdefault(window_key(timestamp, args.window_minutes), []).append(row)

    summaries: list[WaggleWindow] = []
    for start, rows in sorted(grouped.items()):
        angles: list[float] = []
        angle_counts: Counter[int] = Counter()
        spatial_counts: Counter[tuple[int, int]] = Counter()
        for row in rows:
            try:
                angle = float(row[args.angle_column])
                x = float(row[args.x_column])
                y = float(row[args.y_column])
            except (KeyError, TypeError, ValueError):
                continue
            angles.append(angle)
            angle_counts[angle_bin(angle, args.angle_bins)] += 1
            spatial_counts[spatial_bin(x, y, args.spatial_bin_size)] += 1

        summaries.append(
            WaggleWindow(
                window_start=start.isoformat(),
                observations=len(angles),
                angular_entropy=shannon_from_counts(angle_counts),
                angular_concentration=circular_concentration(angles),
                spatial_entropy=shannon_from_counts(spatial_counts),
                dominant_spatial_bin_fraction=dominant_fraction(spatial_counts),
            )
        )
    return summaries


def analyze_interactions(args: argparse.Namespace) -> list[InteractionWindow]:
    grouped: dict[datetime, list[dict[str, str]]] = {}
    for row in read_csv_rows(Path(args.input_csv)):
        if not row.get(args.timestamp_column):
            continue
        timestamp = parse_time(row[args.timestamp_column])
        grouped.setdefault(window_key(timestamp, args.window_minutes), []).append(row)

    summaries: list[InteractionWindow] = []
    for start, rows in sorted(grouped.items()):
        actor_counts: Counter[str] = Counter()
        edge_counts: Counter[tuple[str, str]] = Counter()
        for row in rows:
            left = row.get(args.actor_a_column, "").strip()
            right = row.get(args.actor_b_column, "").strip()
            if not left or not right:
                continue
            edge = tuple(sorted((left, right)))
            actor_counts[left] += 1
            actor_counts[right] += 1
            edge_counts[edge] += 1

        summaries.append(
            InteractionWindow(
                window_start=start.isoformat(),
                interactions=sum(edge_counts.values()),
                actor_entropy=shannon_from_counts(actor_counts),
                edge_entropy=shannon_from_counts(edge_counts),
                dominant_actor_fraction=dominant_fraction(actor_counts),
                dominant_edge_fraction=dominant_fraction(edge_counts),
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


def add_common_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--input-csv", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--timestamp-column", default="timestamp")
    parser.add_argument("--window-minutes", type=int, default=60)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    waggle = subparsers.add_parser("waggle", help="Summarize waggle-phase CSV files.")
    add_common_arguments(waggle)
    waggle.add_argument("--angle-column", default="waggle_angle")
    waggle.add_argument("--x-column", default="x_median")
    waggle.add_argument("--y-column", default="y_median")
    waggle.add_argument("--angle-bins", type=int, default=24)
    waggle.add_argument("--spatial-bin-size", type=float, default=25.0)

    interactions = subparsers.add_parser("interactions", help="Summarize interaction-pair CSV files.")
    add_common_arguments(interactions)
    interactions.add_argument("--actor-a-column", default="actor_a")
    interactions.add_argument("--actor-b-column", default="actor_b")

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.command == "waggle":
        summaries = analyze_waggle(args)
        output_stem = "waggle_observables"
    elif args.command == "interactions":
        summaries = analyze_interactions(args)
        output_stem = "interaction_observables"
    else:
        raise ValueError(f"Unknown command: {args.command}")

    write_csv(output_dir / f"{output_stem}.csv", summaries)
    write_json(output_dir / f"{output_stem}.json", [asdict(row) for row in summaries])
    write_json(output_dir / "analysis_parameters.json", vars(args))

    print(f"Wrote {len(summaries)} windows to {output_dir}")


if __name__ == "__main__":
    main()
