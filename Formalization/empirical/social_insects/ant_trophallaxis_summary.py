#!/usr/bin/env python3
"""First-pass ACP summaries for the Modlmeier ant trophallaxis spreadsheets.

The companion GitHub repository for Modlmeier et al. includes formatted
trophallaxis spreadsheets for three colonies under high- and low-density
treatments. This script reads those `.xlsx` files without third-party
dependencies, removes reciprocal duplicate rows, and summarizes interaction
rate, actor/edge entropy, and location entropy by treatment and time window.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import zipfile
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence
from xml.etree import ElementTree


@dataclass(frozen=True)
class TrophallaxisEvent:
    colony: int
    density: str
    location: str
    ant_a: str
    ant_b: str
    start_seconds: float
    end_seconds: float
    duration_seconds: float


@dataclass(frozen=True)
class AntWindowSummary:
    colony: int
    density: str
    window_start_seconds: int
    window_end_seconds: int
    interactions: int
    total_duration_seconds: float
    distinct_ants: int
    distinct_edges: int
    actor_entropy: float | None
    edge_entropy: float | None
    location_entropy: float | None
    dominant_actor_fraction: float | None
    dominant_edge_fraction: float | None
    dominant_location_fraction: float | None
    mean_duration_seconds: float | None


@dataclass(frozen=True)
class AntTreatmentSummary:
    colony: int
    density: str
    interactions: int
    observation_hours: float
    interaction_rate_per_hour: float | None
    total_duration_seconds: float
    distinct_ants: int
    distinct_edges: int
    actor_entropy: float | None
    edge_entropy: float | None
    location_entropy: float | None
    dominant_actor_fraction: float | None
    dominant_edge_fraction: float | None
    dominant_location_fraction: float | None
    mean_duration_seconds: float | None


@dataclass(frozen=True)
class AntDensityContrast:
    colony: int
    high_interactions: int
    low_interactions: int
    high_interaction_rate_per_hour: float | None
    low_interaction_rate_per_hour: float | None
    rate_pct_change_low_vs_high: float | None
    actor_entropy_delta_low_minus_high: float | None
    edge_entropy_delta_low_minus_high: float | None
    location_entropy_delta_low_minus_high: float | None
    dominant_actor_delta_low_minus_high: float | None
    dominant_edge_delta_low_minus_high: float | None
    dominant_location_delta_low_minus_high: float | None


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def text_content(element: ElementTree.Element) -> str:
    return "".join(node.text or "" for node in element.iter() if local_name(node.tag) == "t")


def shared_strings(archive: zipfile.ZipFile) -> list[str]:
    try:
        payload = archive.read("xl/sharedStrings.xml")
    except KeyError:
        return []
    root = ElementTree.fromstring(payload)
    return [text_content(item) for item in root if local_name(item.tag) == "si"]


def workbook_sheets(archive: zipfile.ZipFile) -> dict[str, str]:
    workbook = ElementTree.fromstring(archive.read("xl/workbook.xml"))
    rels = ElementTree.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    relationships = {
        rel.attrib["Id"]: rel.attrib["Target"]
        for rel in rels
        if local_name(rel.tag) == "Relationship"
    }

    sheets: dict[str, str] = {}
    for element in workbook.iter():
        if local_name(element.tag) != "sheet":
            continue
        rel_id = element.attrib.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        if rel_id is None:
            continue
        target = relationships[rel_id]
        path = target.lstrip("/") if target.startswith("/") else f"xl/{target}"
        sheets[element.attrib["name"]] = path
    return sheets


def column_index(cell_reference: str) -> int:
    letters = re.match(r"[A-Z]+", cell_reference)
    if letters is None:
        return 0
    index = 0
    for character in letters.group(0):
        index = index * 26 + (ord(character) - ord("A") + 1)
    return index - 1


def parse_cell(cell: ElementTree.Element, strings: Sequence[str]) -> object | None:
    cell_type = cell.attrib.get("t")
    value_node = next((child for child in cell if local_name(child.tag) == "v"), None)
    if cell_type == "inlineStr":
        inline = next((child for child in cell if local_name(child.tag) == "is"), None)
        return text_content(inline) if inline is not None else None
    if value_node is None or value_node.text is None:
        return None
    value = value_node.text
    if cell_type == "s":
        return strings[int(value)]
    if cell_type == "b":
        return value == "1"
    try:
        number = float(value)
    except ValueError:
        return value
    return int(number) if number.is_integer() else number


def read_xlsx_sheet(path: Path, sheet_name: str) -> list[dict[str, object | None]]:
    with zipfile.ZipFile(path) as archive:
        strings = shared_strings(archive)
        sheets = workbook_sheets(archive)
        if sheet_name not in sheets:
            raise ValueError(f"{path.name} has no sheet named {sheet_name!r}")
        root = ElementTree.fromstring(archive.read(sheets[sheet_name]))

    rows: list[list[object | None]] = []
    for row in root.iter():
        if local_name(row.tag) != "row":
            continue
        values: list[object | None] = []
        for cell in row:
            if local_name(cell.tag) != "c":
                continue
            index = column_index(cell.attrib.get("r", "A1"))
            while len(values) <= index:
                values.append(None)
            values[index] = parse_cell(cell, strings)
        if values:
            rows.append(values)

    if not rows:
        return []
    headers = [str(value) if value is not None else "" for value in rows[0]]
    records: list[dict[str, object | None]] = []
    for values in rows[1:]:
        record = {header: values[index] if index < len(values) else None for index, header in enumerate(headers)}
        if any(value is not None and value != "" for value in record.values()):
            records.append(record)
    return records


def normalize_ant_id(value: object | None) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    if text.lower() == "q":
        return "Queen"
    if text.endswith(".0"):
        text = text[:-2]
    return text


def numeric(value: object | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def canonical_edge(left: str, right: str) -> tuple[str, str]:
    return tuple(sorted((left, right)))


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


def summarize_events(
    colony: int,
    density: str,
    records: Sequence[dict[str, object | None]],
) -> list[TrophallaxisEvent]:
    seen: set[tuple[object, ...]] = set()
    events: list[TrophallaxisEvent] = []
    for record in records:
        ant_a = normalize_ant_id(record.get("Ant_ID"))
        ant_b = normalize_ant_id(record.get("Ant_ID_(partner)"))
        start = numeric(record.get("synced_start"))
        end = numeric(record.get("synced_end"))
        location = str(record.get("Location", "")).strip()
        if not ant_a or not ant_b or start is None or end is None or end < start:
            continue
        left, right = canonical_edge(ant_a, ant_b)
        key = (location, left, right, start, end)
        if key in seen:
            continue
        seen.add(key)
        events.append(
            TrophallaxisEvent(
                colony=colony,
                density=density,
                location=location,
                ant_a=left,
                ant_b=right,
                start_seconds=start,
                end_seconds=end,
                duration_seconds=end - start,
            )
        )
    return sorted(events, key=lambda event: (event.start_seconds, event.end_seconds, event.ant_a, event.ant_b))


def summary_from_events(
    colony: int,
    density: str,
    events: Sequence[TrophallaxisEvent],
    window_start: int | None = None,
    window_end: int | None = None,
) -> AntWindowSummary:
    actor_counts: Counter[str] = Counter()
    edge_counts: Counter[tuple[str, str]] = Counter()
    location_counts: Counter[str] = Counter()
    total_duration = 0.0
    for event in events:
        actor_counts[event.ant_a] += 1
        actor_counts[event.ant_b] += 1
        edge_counts[(event.ant_a, event.ant_b)] += 1
        location_counts[event.location] += 1
        total_duration += event.duration_seconds

    return AntWindowSummary(
        colony=colony,
        density=density,
        window_start_seconds=window_start or 0,
        window_end_seconds=window_end or 0,
        interactions=len(events),
        total_duration_seconds=total_duration,
        distinct_ants=len(actor_counts),
        distinct_edges=len(edge_counts),
        actor_entropy=shannon_from_counts(actor_counts),
        edge_entropy=shannon_from_counts(edge_counts),
        location_entropy=shannon_from_counts(location_counts),
        dominant_actor_fraction=dominant_fraction(actor_counts),
        dominant_edge_fraction=dominant_fraction(edge_counts),
        dominant_location_fraction=dominant_fraction(location_counts),
        mean_duration_seconds=(total_duration / len(events) if events else None),
    )


def window_summaries(events: Sequence[TrophallaxisEvent], window_seconds: int) -> list[AntWindowSummary]:
    grouped: dict[tuple[int, str, int], list[TrophallaxisEvent]] = {}
    for event in events:
        window_start = int(event.start_seconds // window_seconds) * window_seconds
        grouped.setdefault((event.colony, event.density, window_start), []).append(event)

    summaries: list[AntWindowSummary] = []
    for (colony, density, window_start), window_events in sorted(grouped.items()):
        summaries.append(
            summary_from_events(
                colony=colony,
                density=density,
                events=window_events,
                window_start=window_start,
                window_end=window_start + window_seconds,
            )
        )
    return summaries


def treatment_summaries(events: Sequence[TrophallaxisEvent]) -> list[AntTreatmentSummary]:
    grouped: dict[tuple[int, str], list[TrophallaxisEvent]] = {}
    for event in events:
        grouped.setdefault((event.colony, event.density), []).append(event)

    summaries: list[AntTreatmentSummary] = []
    for (colony, density), treatment_events in sorted(grouped.items()):
        whole = summary_from_events(colony, density, treatment_events)
        max_end = max((event.end_seconds for event in treatment_events), default=0.0)
        observation_hours = max_end / 3600.0 if max_end else 0.0
        summaries.append(
            AntTreatmentSummary(
                colony=colony,
                density=density,
                interactions=whole.interactions,
                observation_hours=observation_hours,
                interaction_rate_per_hour=(
                    whole.interactions / observation_hours if observation_hours else None
                ),
                total_duration_seconds=whole.total_duration_seconds,
                distinct_ants=whole.distinct_ants,
                distinct_edges=whole.distinct_edges,
                actor_entropy=whole.actor_entropy,
                edge_entropy=whole.edge_entropy,
                location_entropy=whole.location_entropy,
                dominant_actor_fraction=whole.dominant_actor_fraction,
                dominant_edge_fraction=whole.dominant_edge_fraction,
                dominant_location_fraction=whole.dominant_location_fraction,
                mean_duration_seconds=whole.mean_duration_seconds,
            )
        )
    return summaries


def pct_change(low: float | None, high: float | None) -> float | None:
    if low is None or high is None or high == 0:
        return None
    return ((low - high) / high) * 100.0


def delta(low: float | None, high: float | None) -> float | None:
    if low is None or high is None:
        return None
    return low - high


def density_contrasts(summaries: Sequence[AntTreatmentSummary]) -> list[AntDensityContrast]:
    by_colony_density = {(summary.colony, summary.density): summary for summary in summaries}
    contrasts: list[AntDensityContrast] = []
    for colony in sorted({summary.colony for summary in summaries}):
        high = by_colony_density.get((colony, "high"))
        low = by_colony_density.get((colony, "low"))
        if high is None or low is None:
            continue
        contrasts.append(
            AntDensityContrast(
                colony=colony,
                high_interactions=high.interactions,
                low_interactions=low.interactions,
                high_interaction_rate_per_hour=high.interaction_rate_per_hour,
                low_interaction_rate_per_hour=low.interaction_rate_per_hour,
                rate_pct_change_low_vs_high=pct_change(
                    low.interaction_rate_per_hour,
                    high.interaction_rate_per_hour,
                ),
                actor_entropy_delta_low_minus_high=delta(low.actor_entropy, high.actor_entropy),
                edge_entropy_delta_low_minus_high=delta(low.edge_entropy, high.edge_entropy),
                location_entropy_delta_low_minus_high=delta(low.location_entropy, high.location_entropy),
                dominant_actor_delta_low_minus_high=delta(
                    low.dominant_actor_fraction,
                    high.dominant_actor_fraction,
                ),
                dominant_edge_delta_low_minus_high=delta(
                    low.dominant_edge_fraction,
                    high.dominant_edge_fraction,
                ),
                dominant_location_delta_low_minus_high=delta(
                    low.dominant_location_fraction,
                    high.dominant_location_fraction,
                ),
            )
        )
    return contrasts


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
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--window-seconds", type=int, default=3600)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    events: list[TrophallaxisEvent] = []
    for colony in (1, 2, 3):
        workbook = input_dir / f"Colony_{colony}_trophallaxis_final.xlsx"
        for density in ("high", "low"):
            records = read_xlsx_sheet(workbook, f"{density} density")
            events.extend(summarize_events(colony, density, records))

    windows = window_summaries(events, args.window_seconds)
    treatments = treatment_summaries(events)
    contrasts = density_contrasts(treatments)

    write_csv(output_dir / "ant_trophallaxis_events.csv", events)
    write_json(output_dir / "ant_trophallaxis_events.json", [asdict(row) for row in events])
    write_csv(output_dir / "ant_trophallaxis_windows.csv", windows)
    write_json(output_dir / "ant_trophallaxis_windows.json", [asdict(row) for row in windows])
    write_csv(output_dir / "ant_trophallaxis_treatment_summary.csv", treatments)
    write_json(output_dir / "ant_trophallaxis_treatment_summary.json", [asdict(row) for row in treatments])
    write_csv(output_dir / "ant_trophallaxis_density_contrasts.csv", contrasts)
    write_json(output_dir / "ant_trophallaxis_density_contrasts.json", [asdict(row) for row in contrasts])
    write_json(output_dir / "analysis_parameters.json", vars(args))

    print(f"Wrote {len(events)} deduplicated trophallaxis events to {output_dir}")
    for contrast in contrasts:
        print(
            f"Colony {contrast.colony}: "
            f"rate_change={contrast.rate_pct_change_low_vs_high}%, "
            f"edge_entropy_delta={contrast.edge_entropy_delta_low_minus_high}, "
            f"location_entropy_delta={contrast.location_entropy_delta_low_minus_high}"
        )


if __name__ == "__main__":
    main()
