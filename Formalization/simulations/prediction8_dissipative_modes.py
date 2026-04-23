#!/usr/bin/env python3
"""First-pass Tier-1 simulator for ACP Prediction 8.

This prototype implements the reduced dissipative-mode competition model scoped
in `bridges/empirical_predictions.md` A.16.11.3. It tracks a probe-based
accessible mode count N_epsilon(t) together with an estimated perturbation
threshold epsilon*(t) under two regimes:

- `reinforced`: active modes accumulate slow reinforcement that feeds back into
  pathway stability.
- `no_reinforcement`: the same fast competition dynamics run, but the slow
  reinforcement field is frozen at zero.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


def linear_slope(points: Sequence[float]) -> float | None:
    if len(points) < 2:
        return None
    x_mean = (len(points) - 1) / 2.0
    y_mean = statistics.fmean(points)
    numerator = sum((index - x_mean) * (value - y_mean) for index, value in enumerate(points))
    denominator = sum((index - x_mean) ** 2 for index in range(len(points)))
    if denominator == 0:
        return None
    return numerator / denominator


def normalize(weights: Sequence[float], minimum: float) -> tuple[float, ...]:
    clipped = [max(minimum, value) for value in weights]
    total = sum(clipped)
    if total == 0:
        return tuple(1.0 / len(clipped) for _ in clipped)
    return tuple(value / total for value in clipped)


def shannon_entropy(probabilities: Sequence[float]) -> float:
    return -sum(probability * math.log(probability) for probability in probabilities if probability > 0)


@dataclass(frozen=True)
class SimulationConfig:
    num_modes: int
    burn_in_steps: int
    total_steps: int
    probe_interval: int
    probe_relax_steps: int
    drive_center: float
    drive_jitter: float
    persistence_strength: float
    reinforcement_feedback: float
    reinforcement_rate: float
    reinforcement_decay: float
    reinforcement_cap: float
    competition_strength: float
    linear_decay: float
    self_saturation: float
    background_drive: float
    fast_noise_scale: float
    time_step: float
    min_share: float
    probe_kick: float
    max_probe_kick: float
    epsilon_steps: int
    dominance_threshold: float
    activity_threshold: float
    coactivation_tolerance: float
    switch_fraction_threshold: float

    @property
    def epsilon_grid(self) -> tuple[float, ...]:
        if self.epsilon_steps <= 1:
            return (self.max_probe_kick,)
        return tuple(
            self.max_probe_kick * (index + 1) / self.epsilon_steps
            for index in range(self.epsilon_steps)
        )


@dataclass(frozen=True)
class ProbeMetrics:
    regime: str
    replicate: int
    age_step: int
    incumbent_pattern: str
    incumbent_share: float
    mode_entropy: float
    total_reinforcement: float
    incumbent_reinforcement: float
    accessible_mode_count: int
    accessible_modes: str
    epsilon_star: float
    epsilon_star_censored: bool
    switch_fraction_at_epsilon_star: float


@dataclass(frozen=True)
class ReplicateSummary:
    regime: str
    replicate: int
    seed: int
    first_accessible_mode_count: int
    final_accessible_mode_count: int
    accessible_mode_slope: float | None
    first_epsilon_star: float
    final_epsilon_star: float
    epsilon_star_slope: float | None
    final_incumbent_pattern: str
    final_incumbent_share: float
    final_total_reinforcement: float


def initialize_state(config: SimulationConfig, rng: random.Random) -> tuple[tuple[float, ...], tuple[float, ...], tuple[float, ...]]:
    amplitudes = normalize(
        [1.0 + rng.uniform(-0.08, 0.08) for _ in range(config.num_modes)],
        config.min_share,
    )
    reinforcements = tuple(0.0 for _ in range(config.num_modes))
    drives = tuple(
        config.drive_center + rng.uniform(-config.drive_jitter, config.drive_jitter)
        for _ in range(config.num_modes)
    )
    return amplitudes, reinforcements, drives


def advance_state(
    amplitudes: Sequence[float],
    reinforcements: Sequence[float],
    drives: Sequence[float],
    config: SimulationConfig,
    rng: random.Random,
    *,
    update_reinforcement: bool,
    noise_scale: float,
) -> tuple[tuple[float, ...], tuple[float, ...]]:
    total_amplitude = sum(amplitudes)
    next_values: list[float] = []
    for index, amplitude in enumerate(amplitudes):
        competition = config.competition_strength * (total_amplitude - amplitude)
        growth = (
            drives[index]
            + (config.persistence_strength * amplitude)
            + (config.reinforcement_feedback * reinforcements[index])
            - (config.linear_decay * amplitude)
            - (config.self_saturation * amplitude * amplitude)
            - competition
            + rng.gauss(0.0, noise_scale)
        )
        updated = amplitude + config.time_step * (amplitude * growth + config.background_drive)
        next_values.append(max(config.min_share, updated))

    next_amplitudes = normalize(next_values, config.min_share)

    if update_reinforcement:
        next_reinforcements = tuple(
            min(
                config.reinforcement_cap,
                max(
                    0.0,
                    ((1.0 - config.reinforcement_decay) * reinforcement)
                    + (config.reinforcement_rate * next_amplitudes[index]),
                ),
            )
            for index, reinforcement in enumerate(reinforcements)
        )
    else:
        next_reinforcements = tuple(reinforcements)

    return next_amplitudes, next_reinforcements


def burn_in(
    amplitudes: Sequence[float],
    reinforcements: Sequence[float],
    drives: Sequence[float],
    config: SimulationConfig,
    rng: random.Random,
) -> tuple[tuple[float, ...], tuple[float, ...]]:
    current_amplitudes = tuple(amplitudes)
    current_reinforcements = tuple(reinforcements)
    for _ in range(config.burn_in_steps):
        current_amplitudes, current_reinforcements = advance_state(
            current_amplitudes,
            current_reinforcements,
            drives,
            config,
            rng,
            update_reinforcement=False,
            noise_scale=config.fast_noise_scale,
        )
    return current_amplitudes, current_reinforcements


def targeted_kick(
    amplitudes: Sequence[float],
    target_mode: int,
    magnitude: float,
    config: SimulationConfig,
) -> tuple[float, ...]:
    kicked = list(amplitudes)
    bleed = magnitude / max(1, config.num_modes - 1)
    for index in range(config.num_modes):
        if index == target_mode:
            kicked[index] += magnitude
        else:
            kicked[index] = max(config.min_share, kicked[index] - bleed)
    return normalize(kicked, config.min_share)


def relax_probe_state(
    amplitudes: Sequence[float],
    reinforcements: Sequence[float],
    drives: Sequence[float],
    config: SimulationConfig,
) -> tuple[float, ...]:
    rng = random.Random(0)
    current = tuple(amplitudes)
    frozen_reinforcements = tuple(reinforcements)
    for _ in range(config.probe_relax_steps):
        current, _ = advance_state(
            current,
            frozen_reinforcements,
            drives,
            config,
            rng,
            update_reinforcement=False,
            noise_scale=0.0,
        )
    return current


def classify_pattern(amplitudes: Sequence[float], config: SimulationConfig) -> str:
    max_share = max(amplitudes)
    leaders = [
        index
        for index, amplitude in enumerate(amplitudes)
        if (max_share - amplitude) <= config.coactivation_tolerance
    ]
    if max_share >= config.dominance_threshold and len(leaders) == 1:
        return f"mode_{leaders[0]}"

    active = [index for index, amplitude in enumerate(amplitudes) if amplitude >= config.activity_threshold]
    if not active:
        active = sorted(range(len(amplitudes)), key=lambda index: amplitudes[index], reverse=True)[:2]
    return "mixed_" + "_".join(str(index) for index in active[:3])


def incumbent_mode_index(pattern: str) -> int | None:
    if pattern.startswith("mode_"):
        return int(pattern.split("_", 1)[1])
    return None


def probe_recovered_patterns(
    amplitudes: Sequence[float],
    reinforcements: Sequence[float],
    drives: Sequence[float],
    config: SimulationConfig,
    magnitude: float,
) -> list[str]:
    labels: list[str] = []
    for mode_index in range(config.num_modes):
        kicked = targeted_kick(amplitudes, mode_index, magnitude, config)
        relaxed = relax_probe_state(kicked, reinforcements, drives, config)
        labels.append(classify_pattern(relaxed, config))
    return labels


def estimate_epsilon_star(
    amplitudes: Sequence[float],
    reinforcements: Sequence[float],
    drives: Sequence[float],
    config: SimulationConfig,
    incumbent_pattern: str,
) -> tuple[float, bool, float]:
    incumbent_index = incumbent_mode_index(incumbent_pattern)
    last_switch_fraction = 0.0
    for magnitude in config.epsilon_grid:
        labels = probe_recovered_patterns(amplitudes, reinforcements, drives, config, magnitude)
        relevant = [
            label
            for index, label in enumerate(labels)
            if incumbent_index is None or index != incumbent_index
        ]
        switch_fraction = (
            sum(1 for label in relevant if label != incumbent_pattern) / len(relevant)
            if relevant
            else 0.0
        )
        last_switch_fraction = switch_fraction
        if switch_fraction >= config.switch_fraction_threshold:
            return magnitude, False, switch_fraction
    return config.max_probe_kick, True, last_switch_fraction


def measure_probe(
    regime: str,
    replicate: int,
    age_step: int,
    amplitudes: Sequence[float],
    reinforcements: Sequence[float],
    drives: Sequence[float],
    config: SimulationConfig,
) -> ProbeMetrics:
    incumbent_pattern = classify_pattern(amplitudes, config)
    accessible_patterns = sorted(set(probe_recovered_patterns(amplitudes, reinforcements, drives, config, config.probe_kick)))
    epsilon_star, epsilon_star_censored, switch_fraction = estimate_epsilon_star(
        amplitudes,
        reinforcements,
        drives,
        config,
        incumbent_pattern,
    )
    incumbent_index = incumbent_mode_index(incumbent_pattern)
    incumbent_reinforcement = reinforcements[incumbent_index] if incumbent_index is not None else max(reinforcements)
    return ProbeMetrics(
        regime=regime,
        replicate=replicate,
        age_step=age_step,
        incumbent_pattern=incumbent_pattern,
        incumbent_share=max(amplitudes),
        mode_entropy=shannon_entropy(amplitudes),
        total_reinforcement=sum(reinforcements),
        incumbent_reinforcement=incumbent_reinforcement,
        accessible_mode_count=len(accessible_patterns),
        accessible_modes=";".join(accessible_patterns),
        epsilon_star=epsilon_star,
        epsilon_star_censored=epsilon_star_censored,
        switch_fraction_at_epsilon_star=switch_fraction,
    )


def run_replicate(
    regime: str,
    replicate: int,
    seed: int,
    config: SimulationConfig,
) -> tuple[list[ProbeMetrics], ReplicateSummary]:
    rng = random.Random(seed)
    amplitudes, reinforcements, drives = initialize_state(config, rng)
    amplitudes, reinforcements = burn_in(amplitudes, reinforcements, drives, config, rng)

    probe_metrics: list[ProbeMetrics] = []
    for step in range(config.total_steps + 1):
        if step % config.probe_interval == 0:
            probe_metrics.append(
                measure_probe(
                    regime=regime,
                    replicate=replicate,
                    age_step=step,
                    amplitudes=amplitudes,
                    reinforcements=reinforcements,
                    drives=drives,
                    config=config,
                )
            )

        if step == config.total_steps:
            break

        amplitudes, reinforcements = advance_state(
            amplitudes,
            reinforcements,
            drives,
            config,
            rng,
            update_reinforcement=(regime == "reinforced"),
            noise_scale=config.fast_noise_scale,
        )

    first = probe_metrics[0]
    last = probe_metrics[-1]
    summary = ReplicateSummary(
        regime=regime,
        replicate=replicate,
        seed=seed,
        first_accessible_mode_count=first.accessible_mode_count,
        final_accessible_mode_count=last.accessible_mode_count,
        accessible_mode_slope=linear_slope([metric.accessible_mode_count for metric in probe_metrics]),
        first_epsilon_star=first.epsilon_star,
        final_epsilon_star=last.epsilon_star,
        epsilon_star_slope=linear_slope([metric.epsilon_star for metric in probe_metrics]),
        final_incumbent_pattern=last.incumbent_pattern,
        final_incumbent_share=last.incumbent_share,
        final_total_reinforcement=last.total_reinforcement,
    )
    return probe_metrics, summary


def write_probe_metrics(path: Path, metrics: Iterable[ProbeMetrics]) -> None:
    fieldnames = [
        "regime",
        "replicate",
        "age_step",
        "incumbent_pattern",
        "incumbent_share",
        "mode_entropy",
        "total_reinforcement",
        "incumbent_reinforcement",
        "accessible_mode_count",
        "accessible_modes",
        "epsilon_star",
        "epsilon_star_censored",
        "switch_fraction_at_epsilon_star",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for metric in metrics:
            writer.writerow(metric.__dict__)


def write_json(path: Path, payload: object) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


def aggregate_summaries(summaries: Sequence[ReplicateSummary]) -> dict[str, object]:
    by_regime: dict[str, list[ReplicateSummary]] = {}
    for summary in summaries:
        by_regime.setdefault(summary.regime, []).append(summary)

    aggregate: dict[str, object] = {}
    for regime, regime_summaries in by_regime.items():
        accessible_slopes = [
            summary.accessible_mode_slope
            for summary in regime_summaries
            if summary.accessible_mode_slope is not None
        ]
        epsilon_slopes = [
            summary.epsilon_star_slope
            for summary in regime_summaries
            if summary.epsilon_star_slope is not None
        ]
        aggregate[regime] = {
            "replicates": len(regime_summaries),
            "mean_first_accessible_mode_count": statistics.fmean(
                summary.first_accessible_mode_count for summary in regime_summaries
            ),
            "mean_final_accessible_mode_count": statistics.fmean(
                summary.final_accessible_mode_count for summary in regime_summaries
            ),
            "mean_accessible_mode_slope": statistics.fmean(accessible_slopes) if accessible_slopes else None,
            "negative_accessible_mode_slope_fraction": (
                sum(1 for slope in accessible_slopes if slope < 0) / len(accessible_slopes)
                if accessible_slopes
                else None
            ),
            "mean_first_epsilon_star": statistics.fmean(
                summary.first_epsilon_star for summary in regime_summaries
            ),
            "mean_final_epsilon_star": statistics.fmean(
                summary.final_epsilon_star for summary in regime_summaries
            ),
            "mean_epsilon_star_slope": statistics.fmean(epsilon_slopes) if epsilon_slopes else None,
            "positive_epsilon_star_slope_fraction": (
                sum(1 for slope in epsilon_slopes if slope > 0) / len(epsilon_slopes)
                if epsilon_slopes
                else None
            ),
            "mean_final_total_reinforcement": statistics.fmean(
                summary.final_total_reinforcement for summary in regime_summaries
            ),
        }
    return aggregate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        default="Formalization/simulations/output/prediction8_pilot",
        help="Directory for CSV and JSON outputs.",
    )
    parser.add_argument(
        "--regimes",
        nargs="+",
        choices=["reinforced", "no_reinforcement"],
        default=["reinforced", "no_reinforcement"],
        help="Simulation regimes to run.",
    )
    parser.add_argument("--replicates", type=int, default=4)
    parser.add_argument("--seed", type=int, default=23)
    parser.add_argument("--num-modes", type=int, default=5)
    parser.add_argument("--burn-in-steps", type=int, default=120)
    parser.add_argument("--total-steps", type=int, default=240)
    parser.add_argument("--probe-interval", type=int, default=20)
    parser.add_argument("--probe-relax-steps", type=int, default=60)
    parser.add_argument("--drive-center", type=float, default=1.0)
    parser.add_argument("--drive-jitter", type=float, default=0.01)
    parser.add_argument("--persistence-strength", type=float, default=0.2)
    parser.add_argument("--reinforcement-feedback", type=float, default=1.2)
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
    parser.add_argument("--probe-kick", type=float, default=0.54)
    parser.add_argument("--max-probe-kick", type=float, default=0.66)
    parser.add_argument("--epsilon-steps", type=int, default=11)
    parser.add_argument("--dominance-threshold", type=float, default=0.42)
    parser.add_argument("--activity-threshold", type=float, default=0.18)
    parser.add_argument("--coactivation-tolerance", type=float, default=0.06)
    parser.add_argument("--switch-fraction-threshold", type=float, default=0.5)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = SimulationConfig(
        num_modes=args.num_modes,
        burn_in_steps=args.burn_in_steps,
        total_steps=args.total_steps,
        probe_interval=args.probe_interval,
        probe_relax_steps=args.probe_relax_steps,
        drive_center=args.drive_center,
        drive_jitter=args.drive_jitter,
        persistence_strength=args.persistence_strength,
        reinforcement_feedback=args.reinforcement_feedback,
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
        probe_kick=args.probe_kick,
        max_probe_kick=args.max_probe_kick,
        epsilon_steps=args.epsilon_steps,
        dominance_threshold=args.dominance_threshold,
        activity_threshold=args.activity_threshold,
        coactivation_tolerance=args.coactivation_tolerance,
        switch_fraction_threshold=args.switch_fraction_threshold,
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    all_probe_metrics: list[ProbeMetrics] = []
    all_summaries: list[ReplicateSummary] = []
    for regime in args.regimes:
        for replicate in range(args.replicates):
            seed = args.seed + replicate
            probe_metrics, summary = run_replicate(
                regime=regime,
                replicate=replicate,
                seed=seed,
                config=config,
            )
            all_probe_metrics.extend(probe_metrics)
            all_summaries.append(summary)

    write_probe_metrics(output_dir / "probe_metrics.csv", all_probe_metrics)
    write_json(
        output_dir / "replicate_summaries.json",
        [summary.__dict__ for summary in all_summaries],
    )
    aggregate = aggregate_summaries(all_summaries)
    write_json(output_dir / "aggregate_summary.json", aggregate)

    print("Prediction 8 pilot complete.")
    print(f"Output directory: {output_dir}")
    for regime in args.regimes:
        regime_summary = aggregate.get(regime, {})
        print(
            f"{regime}: "
            f"mean_accessible_mode_slope={regime_summary.get('mean_accessible_mode_slope')} "
            f"negative_accessible_mode_slope_fraction={regime_summary.get('negative_accessible_mode_slope_fraction')} "
            f"mean_epsilon_star_slope={regime_summary.get('mean_epsilon_star_slope')}"
        )


if __name__ == "__main__":
    main()
