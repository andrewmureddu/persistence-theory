#!/usr/bin/env python3
"""Grid sweep helper for the Prediction 8 dissipative-mode simulator."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import prediction8_dissipative_modes as p8


@dataclass(frozen=True)
class SweepRow:
    probe_kick: float
    drive_jitter: float
    reinforcement_feedback: float
    reinforced_mean_accessible_mode_slope: float | None
    null_mean_accessible_mode_slope: float | None
    accessible_slope_gap: float | None
    reinforced_negative_accessible_slope_fraction: float | None
    null_negative_accessible_slope_fraction: float | None
    negative_fraction_gap: float | None
    reinforced_mean_epsilon_star_slope: float | None
    null_mean_epsilon_star_slope: float | None
    epsilon_slope_gap: float | None
    reinforced_mean_final_accessible_mode_count: float | None
    null_mean_final_accessible_mode_count: float | None
    reinforced_mean_final_total_reinforcement: float | None


def safe_number(value: float | None, default: float = 0.0) -> float:
    return default if value is None else value


def build_config(
    args: argparse.Namespace,
    probe_kick: float,
    drive_jitter: float,
    reinforcement_feedback: float,
) -> p8.SimulationConfig:
    max_probe_kick = max(args.max_probe_kick, probe_kick)
    return p8.SimulationConfig(
        num_modes=args.num_modes,
        burn_in_steps=args.burn_in_steps,
        total_steps=args.total_steps,
        probe_interval=args.probe_interval,
        probe_relax_steps=args.probe_relax_steps,
        drive_center=args.drive_center,
        drive_jitter=drive_jitter,
        persistence_strength=args.persistence_strength,
        reinforcement_feedback=reinforcement_feedback,
        reinforcement_rate=args.reinforcement_rate,
        reinforcement_decay=args.reinforcement_decay,
        reinforcement_cap=args.reinforcement_cap,
        competition_strength=args.competition_strength,
        linear_decay=args.linear_decay,
        self_saturation=args.self_saturation,
        background_drive=args.background_drive,
        fast_noise_scale=args.fast_noise_scale,
        time_step=args.time_step,
        min_share=args.min_share,
        probe_kick=probe_kick,
        max_probe_kick=max_probe_kick,
        epsilon_steps=args.epsilon_steps,
        dominance_threshold=args.dominance_threshold,
        activity_threshold=args.activity_threshold,
        coactivation_tolerance=args.coactivation_tolerance,
        switch_fraction_threshold=args.switch_fraction_threshold,
    )


def aggregate_for_configuration(
    args: argparse.Namespace,
    probe_kick: float,
    drive_jitter: float,
    reinforcement_feedback: float,
    config_index: int,
) -> tuple[SweepRow, list[dict[str, object]]]:
    config = build_config(args, probe_kick, drive_jitter, reinforcement_feedback)
    replicate_payloads: list[dict[str, object]] = []
    summaries: list[p8.ReplicateSummary] = []

    regime_offsets = {regime: index * 100_000 for index, regime in enumerate(args.regimes)}
    base_offset = config_index * 1_000_000

    for regime in args.regimes:
        for replicate in range(args.replicates):
            seed = args.seed + base_offset + regime_offsets[regime] + replicate
            _, summary = p8.run_replicate(
                regime=regime,
                replicate=replicate,
                seed=seed,
                config=config,
            )
            summaries.append(summary)
            summary_dict = asdict(summary)
            summary_dict.update(
                {
                    "probe_kick": probe_kick,
                    "drive_jitter": drive_jitter,
                    "reinforcement_feedback": reinforcement_feedback,
                }
            )
            replicate_payloads.append(summary_dict)

    aggregate = p8.aggregate_summaries(summaries)
    reinforced = aggregate.get("reinforced", {})
    null = aggregate.get("no_reinforcement", {})

    reinforced_accessible_slope = reinforced.get("mean_accessible_mode_slope")
    null_accessible_slope = null.get("mean_accessible_mode_slope")
    reinforced_negative_fraction = reinforced.get("negative_accessible_mode_slope_fraction")
    null_negative_fraction = null.get("negative_accessible_mode_slope_fraction")
    reinforced_epsilon_slope = reinforced.get("mean_epsilon_star_slope")
    null_epsilon_slope = null.get("mean_epsilon_star_slope")

    row = SweepRow(
        probe_kick=probe_kick,
        drive_jitter=drive_jitter,
        reinforcement_feedback=reinforcement_feedback,
        reinforced_mean_accessible_mode_slope=reinforced_accessible_slope,
        null_mean_accessible_mode_slope=null_accessible_slope,
        accessible_slope_gap=(
            reinforced_accessible_slope - null_accessible_slope
            if reinforced_accessible_slope is not None and null_accessible_slope is not None
            else None
        ),
        reinforced_negative_accessible_slope_fraction=reinforced_negative_fraction,
        null_negative_accessible_slope_fraction=null_negative_fraction,
        negative_fraction_gap=(
            reinforced_negative_fraction - null_negative_fraction
            if reinforced_negative_fraction is not None and null_negative_fraction is not None
            else None
        ),
        reinforced_mean_epsilon_star_slope=reinforced_epsilon_slope,
        null_mean_epsilon_star_slope=null_epsilon_slope,
        epsilon_slope_gap=(
            reinforced_epsilon_slope - null_epsilon_slope
            if reinforced_epsilon_slope is not None and null_epsilon_slope is not None
            else None
        ),
        reinforced_mean_final_accessible_mode_count=reinforced.get("mean_final_accessible_mode_count"),
        null_mean_final_accessible_mode_count=null.get("mean_final_accessible_mode_count"),
        reinforced_mean_final_total_reinforcement=reinforced.get("mean_final_total_reinforcement"),
    )
    return row, replicate_payloads


def write_csv(path: Path, rows: Iterable[SweepRow]) -> None:
    rows = list(rows)
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


def ranking_key(row: SweepRow) -> tuple[float, float, float]:
    return (
        -safe_number(row.accessible_slope_gap, default=1e9),
        safe_number(row.negative_fraction_gap, default=-1e9),
        safe_number(row.epsilon_slope_gap, default=-1e9),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        default="Formalization/simulations/output/prediction8_calibration",
        help="Directory for sweep summaries.",
    )
    parser.add_argument(
        "--regimes",
        nargs="+",
        choices=["reinforced", "no_reinforcement"],
        default=["reinforced", "no_reinforcement"],
        help="Regimes to compare in the sweep.",
    )
    parser.add_argument("--replicates", type=int, default=6)
    parser.add_argument("--seed", type=int, default=23)
    parser.add_argument("--probe-kicks", nargs="+", type=float, default=[0.42, 0.54, 0.66])
    parser.add_argument("--drive-jitters", nargs="+", type=float, default=[0.0, 0.01, 0.03])
    parser.add_argument("--reinforcement-feedbacks", nargs="+", type=float, default=[0.6, 1.2, 1.8])
    parser.add_argument("--num-modes", type=int, default=5)
    parser.add_argument("--burn-in-steps", type=int, default=120)
    parser.add_argument("--total-steps", type=int, default=240)
    parser.add_argument("--probe-interval", type=int, default=20)
    parser.add_argument("--probe-relax-steps", type=int, default=60)
    parser.add_argument("--drive-center", type=float, default=1.0)
    parser.add_argument("--persistence-strength", type=float, default=0.2)
    parser.add_argument("--reinforcement-rate", type=float, default=0.035)
    parser.add_argument("--reinforcement-decay", type=float, default=0.01)
    parser.add_argument("--reinforcement-cap", type=float, default=2.5)
    parser.add_argument("--competition-strength", type=float, default=1.2)
    parser.add_argument("--linear-decay", type=float, default=0.85)
    parser.add_argument("--self-saturation", type=float, default=0.55)
    parser.add_argument("--background-drive", type=float, default=0.015)
    parser.add_argument("--fast-noise-scale", type=float, default=0.015)
    parser.add_argument("--time-step", type=float, default=0.35)
    parser.add_argument("--min-share", type=float, default=1e-4)
    parser.add_argument("--max-probe-kick", type=float, default=0.66)
    parser.add_argument("--epsilon-steps", type=int, default=11)
    parser.add_argument("--dominance-threshold", type=float, default=0.42)
    parser.add_argument("--activity-threshold", type=float, default=0.18)
    parser.add_argument("--coactivation-tolerance", type=float, default=0.06)
    parser.add_argument("--switch-fraction-threshold", type=float, default=0.5)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "sweep_parameters.json", vars(args))

    rows: list[SweepRow] = []
    replicate_payloads: list[dict[str, object]] = []

    combos = [
        (probe_kick, drive_jitter, reinforcement_feedback)
        for probe_kick in args.probe_kicks
        for drive_jitter in args.drive_jitters
        for reinforcement_feedback in args.reinforcement_feedbacks
    ]

    total_configs = len(combos)

    for config_index, (probe_kick, drive_jitter, reinforcement_feedback) in enumerate(combos, start=1):
        row, payloads = aggregate_for_configuration(
            args=args,
            probe_kick=probe_kick,
            drive_jitter=drive_jitter,
            reinforcement_feedback=reinforcement_feedback,
            config_index=config_index - 1,
        )
        rows.append(row)
        replicate_payloads.extend(payloads)

        ranked_rows = sorted(rows, key=ranking_key, reverse=True)
        write_csv(output_dir / "config_summaries.csv", ranked_rows)
        write_json(output_dir / "config_summaries.json", [asdict(row_item) for row_item in ranked_rows])
        write_json(output_dir / "replicate_summaries.json", replicate_payloads)
        print(
            f"[{config_index}/{total_configs}] "
            f"kick={probe_kick} jitter={drive_jitter} feedback={reinforcement_feedback} "
            f"accessible_gap={row.accessible_slope_gap} "
            f"negative_gap={row.negative_fraction_gap} "
            f"epsilon_gap={row.epsilon_slope_gap}",
            flush=True,
        )

    ranked_rows = sorted(rows, key=ranking_key, reverse=True)
    write_csv(output_dir / "config_summaries.csv", ranked_rows)
    write_json(output_dir / "config_summaries.json", [asdict(row) for row in ranked_rows])
    write_json(output_dir / "replicate_summaries.json", replicate_payloads)

    print("Prediction 8 calibration sweep complete.")
    print(f"Output directory: {output_dir}")
    for row in ranked_rows[:5]:
        print(
            f"kick={row.probe_kick} jitter={row.drive_jitter} feedback={row.reinforcement_feedback} "
            f"accessible_gap={row.accessible_slope_gap} "
            f"negative_gap={row.negative_fraction_gap} "
            f"epsilon_gap={row.epsilon_slope_gap}"
        )


if __name__ == "__main__":
    main()
