#!/usr/bin/env python3
"""Grid sweep helper for the Prediction 9 simulator."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import prediction9_boolean_network as p9


@dataclass(frozen=True)
class SweepRow:
    fitness_threshold: float
    population_size: int
    stability_weight: float
    selected_threshold_reached_fraction: float | None
    neutral_threshold_reached_fraction: float | None
    selected_mean_post_optimal_slope: float | None
    neutral_mean_post_optimal_slope: float | None
    slope_gap: float | None
    selected_positive_slope_fraction: float | None
    neutral_positive_slope_fraction: float | None
    positive_fraction_gap: float | None
    selected_mean_final_best_correctness: float | None
    neutral_mean_final_best_correctness: float | None
    selected_mean_final_best_frozen_fraction: float | None
    neutral_mean_final_best_frozen_fraction: float | None


def safe_number(value: float | None, default: float = 0.0) -> float:
    return default if value is None else value


def build_config(args: argparse.Namespace, fitness_threshold: float, population_size: int, stability_weight: float) -> p9.SimulationConfig:
    return p9.build_config(
        num_inputs=args.num_inputs,
        num_dynamic_nodes=args.num_dynamic_nodes,
        num_outputs=args.num_outputs,
        connectivity=args.connectivity,
        truth_bias=args.truth_bias,
        population_size=population_size,
        input_sample_limit=args.input_sample_limit,
        eval_trials=args.eval_trials,
        settle_steps=args.settle_steps,
        attractor_steps=args.attractor_steps,
        derrida_samples=args.derrida_samples,
        fitness_threshold=fitness_threshold,
        max_generations=args.max_generations,
        post_optimal_generations=args.post_optimal_generations,
        elite_count=args.elite_count,
        parent_pool_size=args.parent_pool_size,
        stability_weight=stability_weight,
        rewire_probability=args.rewire_probability,
        truth_table_flip_probability=args.truth_table_flip_probability,
    )


def aggregate_for_configuration(
    args: argparse.Namespace,
    fitness_threshold: float,
    population_size: int,
    stability_weight: float,
    config_index: int,
) -> tuple[SweepRow, list[dict[str, object]]]:
    config = build_config(args, fitness_threshold, population_size, stability_weight)
    replicate_payloads: list[dict[str, object]] = []
    summaries: list[p9.ReplicateSummary] = []

    regime_offsets = {regime: index * 100_000 for index, regime in enumerate(args.regimes)}
    base_offset = config_index * 1_000_000

    for regime in args.regimes:
        for replicate in range(args.replicates):
            seed = args.seed + base_offset + regime_offsets[regime] + replicate
            _, summary = p9.run_replicate(
                regime=regime,
                replicate=replicate,
                seed=seed,
                config=config,
            )
            summaries.append(summary)
            summary_dict = asdict(summary)
            summary_dict.update(
                {
                    "fitness_threshold": fitness_threshold,
                    "population_size": population_size,
                    "stability_weight": stability_weight,
                }
            )
            replicate_payloads.append(summary_dict)

    aggregate = p9.aggregate_summaries(summaries)
    selected = aggregate.get("selected", {})
    neutral = aggregate.get("neutral_post_threshold", {})

    selected_mean_slope = selected.get("mean_post_optimal_slope")
    neutral_mean_slope = neutral.get("mean_post_optimal_slope")
    selected_positive = selected.get("positive_slope_fraction")
    neutral_positive = neutral.get("positive_slope_fraction")

    row = SweepRow(
        fitness_threshold=fitness_threshold,
        population_size=population_size,
        stability_weight=stability_weight,
        selected_threshold_reached_fraction=selected.get("threshold_reached_fraction"),
        neutral_threshold_reached_fraction=neutral.get("threshold_reached_fraction"),
        selected_mean_post_optimal_slope=selected_mean_slope,
        neutral_mean_post_optimal_slope=neutral_mean_slope,
        slope_gap=(
            selected_mean_slope - neutral_mean_slope
            if selected_mean_slope is not None and neutral_mean_slope is not None
            else None
        ),
        selected_positive_slope_fraction=selected_positive,
        neutral_positive_slope_fraction=neutral_positive,
        positive_fraction_gap=(
            selected_positive - neutral_positive
            if selected_positive is not None and neutral_positive is not None
            else None
        ),
        selected_mean_final_best_correctness=selected.get("mean_final_best_correctness"),
        neutral_mean_final_best_correctness=neutral.get("mean_final_best_correctness"),
        selected_mean_final_best_frozen_fraction=selected.get("mean_final_best_frozen_fraction"),
        neutral_mean_final_best_frozen_fraction=neutral.get("mean_final_best_frozen_fraction"),
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
        safe_number(row.slope_gap, default=-1e9),
        safe_number(row.positive_fraction_gap, default=-1e9),
        safe_number(row.selected_threshold_reached_fraction, default=-1e9),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        default="Formalization/simulations/output/prediction9_calibration",
        help="Directory for sweep summaries.",
    )
    parser.add_argument(
        "--regimes",
        nargs="+",
        choices=["selected", "neutral_post_threshold"],
        default=["selected", "neutral_post_threshold"],
        help="Regimes to compare in the sweep.",
    )
    parser.add_argument("--replicates", type=int, default=6)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--fitness-thresholds", nargs="+", type=float, default=[0.82, 0.85, 0.88])
    parser.add_argument("--population-sizes", nargs="+", type=int, default=[24])
    parser.add_argument("--stability-weights", nargs="+", type=float, default=[0.2, 0.3, 0.4])
    parser.add_argument("--num-inputs", type=int, default=p9.DEFAULT_CONFIG.num_inputs)
    parser.add_argument("--num-dynamic-nodes", type=int, default=p9.DEFAULT_CONFIG.num_dynamic_nodes)
    parser.add_argument("--num-outputs", type=int, default=p9.DEFAULT_CONFIG.num_outputs)
    parser.add_argument("--connectivity", type=int, default=p9.DEFAULT_CONFIG.connectivity)
    parser.add_argument("--truth-bias", type=float, default=p9.DEFAULT_CONFIG.truth_bias)
    parser.add_argument("--input-sample-limit", type=int, default=p9.DEFAULT_CONFIG.input_sample_limit)
    parser.add_argument("--eval-trials", type=int, default=p9.DEFAULT_CONFIG.eval_trials)
    parser.add_argument("--settle-steps", type=int, default=p9.DEFAULT_CONFIG.settle_steps)
    parser.add_argument("--attractor-steps", type=int, default=p9.DEFAULT_CONFIG.attractor_steps)
    parser.add_argument("--derrida-samples", type=int, default=p9.DEFAULT_CONFIG.derrida_samples)
    parser.add_argument("--max-generations", type=int, default=p9.DEFAULT_CONFIG.max_generations)
    parser.add_argument(
        "--post-optimal-generations",
        type=int,
        default=p9.DEFAULT_CONFIG.post_optimal_generations,
    )
    parser.add_argument("--elite-count", type=int, default=p9.DEFAULT_CONFIG.elite_count)
    parser.add_argument("--parent-pool-size", type=int, default=p9.DEFAULT_CONFIG.parent_pool_size)
    parser.add_argument(
        "--rewire-probability",
        type=float,
        default=p9.DEFAULT_CONFIG.rewire_probability,
    )
    parser.add_argument(
        "--truth-table-flip-probability",
        type=float,
        default=p9.DEFAULT_CONFIG.truth_table_flip_probability,
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "sweep_parameters.json", vars(args))

    rows: list[SweepRow] = []
    replicate_payloads: list[dict[str, object]] = []

    combos = [
        (fitness_threshold, population_size, stability_weight)
        for fitness_threshold in args.fitness_thresholds
        for population_size in args.population_sizes
        for stability_weight in args.stability_weights
    ]

    total_configs = len(combos)

    for config_index, (fitness_threshold, population_size, stability_weight) in enumerate(combos, start=1):
        row, payloads = aggregate_for_configuration(
            args=args,
            fitness_threshold=fitness_threshold,
            population_size=population_size,
            stability_weight=stability_weight,
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
            f"threshold={fitness_threshold} pop={population_size} weight={stability_weight} "
            f"slope_gap={row.slope_gap} positive_gap={row.positive_fraction_gap}",
            flush=True,
        )

    ranked_rows = sorted(rows, key=ranking_key, reverse=True)
    write_csv(output_dir / "config_summaries.csv", ranked_rows)
    write_json(output_dir / "config_summaries.json", [asdict(row) for row in ranked_rows])
    write_json(output_dir / "replicate_summaries.json", replicate_payloads)

    print("Prediction 9 calibration sweep complete.")
    print(f"Output directory: {output_dir}")
    for row in ranked_rows[:5]:
        print(
            "threshold="
            f"{row.fitness_threshold} pop={row.population_size} weight={row.stability_weight} "
            f"slope_gap={row.slope_gap} positive_gap={row.positive_fraction_gap} "
            f"selected_threshold={row.selected_threshold_reached_fraction}"
        )


if __name__ == "__main__":
    main()
