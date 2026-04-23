#!/usr/bin/env python3
"""First-pass Tier-1 simulator for ACP Prediction 9.

This prototype implements an evolutionary random Boolean network (RBN) ensemble
under a fixed target function and tracks post-optimal drift in the frozen
component fraction f(t), following the scope fixed in
`bridges/empirical_predictions.md` A.16.11.2.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Iterable, Sequence


def bits_from_int(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> shift) & 1 for shift in reversed(range(width)))


def hamming_distance(left: Sequence[int], right: Sequence[int]) -> int:
    return sum(1 for a, b in zip(left, right) if a != b)


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


@dataclass(frozen=True)
class Gate:
    inputs: tuple[int, ...]
    table: tuple[int, ...]

    def evaluate(self, state: Sequence[int]) -> int:
        table_index = 0
        for source in self.inputs:
            table_index = (table_index << 1) | state[source]
        return self.table[table_index]


@dataclass(frozen=True)
class BooleanNetwork:
    num_inputs: int
    num_dynamic_nodes: int
    output_indices: tuple[int, ...]
    gates: tuple[Gate, ...]

    @property
    def total_nodes(self) -> int:
        return self.num_inputs + self.num_dynamic_nodes

    def step(self, input_bits: Sequence[int], dynamic_bits: Sequence[int]) -> tuple[int, ...]:
        state = tuple(input_bits) + tuple(dynamic_bits)
        return tuple(gate.evaluate(state) for gate in self.gates)

    def settle(
        self,
        input_bits: Sequence[int],
        dynamic_bits: Sequence[int],
        steps: int,
    ) -> tuple[int, ...]:
        state = tuple(dynamic_bits)
        for _ in range(steps):
            state = self.step(input_bits, state)
        return state

    def outputs(self, input_bits: Sequence[int], dynamic_bits: Sequence[int]) -> tuple[int, ...]:
        state = tuple(input_bits) + tuple(dynamic_bits)
        return tuple(state[index] for index in self.output_indices)

    def attractor_cycle(
        self,
        input_bits: Sequence[int],
        initial_dynamic_bits: Sequence[int],
        max_steps: int,
    ) -> list[tuple[int, ...]]:
        seen: dict[tuple[int, ...], int] = {}
        history: list[tuple[int, ...]] = []
        state = tuple(initial_dynamic_bits)
        for _ in range(max_steps):
            if state in seen:
                return history[seen[state] :]
            seen[state] = len(history)
            history.append(state)
            state = self.step(input_bits, state)
        return history[-1:] if history else [tuple(initial_dynamic_bits)]

    def mutate(self, rng: random.Random, config: "SimulationConfig") -> "BooleanNetwork":
        gates: list[Gate] = []
        changed = False
        for gate in self.gates:
            inputs = list(gate.inputs)
            table = list(gate.table)
            for index in range(len(inputs)):
                if rng.random() < config.rewire_probability:
                    inputs[index] = rng.randrange(self.total_nodes)
                    changed = True
            for index in range(len(table)):
                if rng.random() < config.truth_table_flip_probability:
                    table[index] = 1 - table[index]
                    changed = True
            gates.append(Gate(tuple(inputs), tuple(table)))

        if not changed:
            gate_index = rng.randrange(len(gates))
            table = list(gates[gate_index].table)
            flip_index = rng.randrange(len(table))
            table[flip_index] = 1 - table[flip_index]
            gates[gate_index] = Gate(gates[gate_index].inputs, tuple(table))

        return BooleanNetwork(
            num_inputs=self.num_inputs,
            num_dynamic_nodes=self.num_dynamic_nodes,
            output_indices=self.output_indices,
            gates=tuple(gates),
        )

    @classmethod
    def random(
        cls,
        rng: random.Random,
        num_inputs: int,
        num_dynamic_nodes: int,
        connectivity: int,
        num_outputs: int,
        truth_bias: float,
    ) -> "BooleanNetwork":
        total_nodes = num_inputs + num_dynamic_nodes
        gates = []
        for _ in range(num_dynamic_nodes):
            sources = tuple(rng.randrange(total_nodes) for _ in range(connectivity))
            table = tuple(1 if rng.random() < truth_bias else 0 for _ in range(1 << connectivity))
            gates.append(Gate(sources, table))
        output_indices = tuple(range(total_nodes - num_outputs, total_nodes))
        return cls(
            num_inputs=num_inputs,
            num_dynamic_nodes=num_dynamic_nodes,
            output_indices=output_indices,
            gates=tuple(gates),
        )


@dataclass(frozen=True)
class SimulationConfig:
    num_inputs: int
    num_dynamic_nodes: int
    num_outputs: int
    connectivity: int
    truth_bias: float
    population_size: int
    input_sample_limit: int
    eval_trials: int
    settle_steps: int
    attractor_steps: int
    derrida_samples: int
    fitness_threshold: float
    max_generations: int
    post_optimal_generations: int
    elite_count: int
    parent_pool_size: int
    stability_weight: float
    rewire_probability: float
    truth_table_flip_probability: float


DEFAULT_CONFIG = SimulationConfig(
    num_inputs=3,
    num_dynamic_nodes=24,
    num_outputs=2,
    connectivity=3,
    truth_bias=0.5,
    population_size=24,
    input_sample_limit=8,
    eval_trials=3,
    settle_steps=12,
    attractor_steps=96,
    derrida_samples=8,
    fitness_threshold=0.95,
    max_generations=80,
    post_optimal_generations=40,
    elite_count=2,
    parent_pool_size=8,
    stability_weight=0.2,
    rewire_probability=0.02,
    truth_table_flip_probability=0.01,
)


def build_config(**overrides: object) -> SimulationConfig:
    return replace(DEFAULT_CONFIG, **overrides)


@dataclass(frozen=True)
class NetworkEvaluation:
    correctness: float
    stability: float
    score: float
    frozen_fraction: float
    derrida_lambda: float
    attractor_cycle_length: int

    @property
    def selected_rank_key(self) -> tuple[float, float]:
        # Primary ranking is the weighted score; correctness breaks exact score ties.
        return (self.score, self.correctness)


@dataclass(frozen=True)
class GenerationMetrics:
    regime: str
    replicate: int
    generation: int
    best_correctness: float
    best_stability: float
    best_score: float
    best_frozen_fraction: float
    best_lambda: float
    best_cycle_length: int
    mean_correctness: float
    mean_stability: float
    mean_frozen_fraction: float
    mean_lambda: float
    mean_cycle_length: float
    threshold_generation: int | None


@dataclass(frozen=True)
class ReplicateSummary:
    regime: str
    replicate: int
    seed: int
    threshold_generation: int | None
    generations_completed: int
    post_optimal_slope: float | None
    final_best_correctness: float
    final_best_stability: float
    final_best_frozen_fraction: float
    final_best_lambda: float


def target_function(input_bits: Sequence[int], num_outputs: int) -> tuple[int, ...]:
    ones = sum(input_bits)
    parity = ones % 2
    majority = 1 if ones * 2 >= len(input_bits) else 0
    first = input_bits[0] if input_bits else 0
    outputs = (parity, majority, first ^ parity)
    return outputs[:num_outputs]


def generate_input_patterns(config: SimulationConfig, rng: random.Random) -> list[tuple[int, ...]]:
    total = 1 << config.num_inputs
    if total <= config.input_sample_limit:
        return [bits_from_int(index, config.num_inputs) for index in range(total)]

    patterns: set[tuple[int, ...]] = set()
    while len(patterns) < config.input_sample_limit:
        patterns.add(tuple(rng.randrange(2) for _ in range(config.num_inputs)))
    return sorted(patterns)


def evaluate_network(
    network: BooleanNetwork,
    config: SimulationConfig,
    rng: random.Random,
) -> NetworkEvaluation:
    input_patterns = generate_input_patterns(config, rng)
    correctness_scores: list[float] = []
    stability_scores: list[float] = []

    for input_bits in input_patterns:
        outputs: list[tuple[int, ...]] = []
        target = target_function(input_bits, config.num_outputs)
        for _ in range(config.eval_trials):
            initial_dynamic = tuple(rng.randrange(2) for _ in range(config.num_dynamic_nodes))
            settled = network.settle(input_bits, initial_dynamic, config.settle_steps)
            outputs.append(network.outputs(input_bits, settled))

        target_matches = [
            1.0 - (hamming_distance(output, target) / config.num_outputs)
            for output in outputs
        ]
        correctness_scores.append(statistics.fmean(target_matches))

        consensus = []
        for output_index in range(config.num_outputs):
            ones = sum(output[output_index] for output in outputs)
            consensus.append(1 if ones * 2 >= len(outputs) else 0)
        consensus_tuple = tuple(consensus)
        agreement = [
            1.0 - (hamming_distance(output, consensus_tuple) / config.num_outputs)
            for output in outputs
        ]
        stability_scores.append(statistics.fmean(agreement))

    probe_input = tuple(0 for _ in range(config.num_inputs))
    cycle = network.attractor_cycle(
        probe_input,
        tuple(0 for _ in range(config.num_dynamic_nodes)),
        config.attractor_steps,
    )
    frozen_nodes = 0
    for node_index in range(config.num_dynamic_nodes):
        values = {state[node_index] for state in cycle}
        if len(values) == 1:
            frozen_nodes += 1
    frozen_fraction = frozen_nodes / config.num_dynamic_nodes

    derrida_distances = []
    for _ in range(config.derrida_samples):
        state = tuple(rng.randrange(2) for _ in range(config.num_dynamic_nodes))
        flipped_index = rng.randrange(config.num_dynamic_nodes)
        perturbed = list(state)
        perturbed[flipped_index] = 1 - perturbed[flipped_index]
        next_a = network.step(probe_input, state)
        next_b = network.step(probe_input, tuple(perturbed))
        derrida_distances.append(hamming_distance(next_a, next_b))
    derrida_lambda = statistics.fmean(derrida_distances)

    correctness = statistics.fmean(correctness_scores)
    stability = statistics.fmean(stability_scores)
    score = correctness + (config.stability_weight * stability)
    return NetworkEvaluation(
        correctness=correctness,
        stability=stability,
        score=score,
        frozen_fraction=frozen_fraction,
        derrida_lambda=derrida_lambda,
        attractor_cycle_length=len(cycle),
    )


def initialize_population(config: SimulationConfig, rng: random.Random) -> list[BooleanNetwork]:
    return [
        BooleanNetwork.random(
            rng=rng,
            num_inputs=config.num_inputs,
            num_dynamic_nodes=config.num_dynamic_nodes,
            connectivity=config.connectivity,
            num_outputs=config.num_outputs,
            truth_bias=config.truth_bias,
        )
        for _ in range(config.population_size)
    ]


def select_next_population(
    regime: str,
    population: Sequence[BooleanNetwork],
    evaluations: Sequence[NetworkEvaluation],
    config: SimulationConfig,
    rng: random.Random,
    threshold_reached: bool,
) -> list[BooleanNetwork]:
    if regime == "mutation_only":
        return [rng.choice(population).mutate(rng, config) for _ in range(config.population_size)]

    ranked_indices = sorted(
        range(len(population)),
        key=lambda index: evaluations[index].selected_rank_key,
        reverse=True,
    )
    elites = [population[index] for index in ranked_indices[: config.elite_count]]

    if regime == "neutral_post_threshold" and threshold_reached:
        eligible = [
            population[index]
            for index, evaluation in enumerate(evaluations)
            if evaluation.correctness >= config.fitness_threshold
        ]
        parent_pool = eligible or [population[index] for index in ranked_indices[: config.parent_pool_size]]
    else:
        parent_pool = [population[index] for index in ranked_indices[: config.parent_pool_size]]

    next_population = list(elites)
    while len(next_population) < config.population_size:
        parent = rng.choice(parent_pool)
        next_population.append(parent.mutate(rng, config))
    return next_population


def summarize_generation(
    regime: str,
    replicate: int,
    generation: int,
    evaluations: Sequence[NetworkEvaluation],
    threshold_generation: int | None,
) -> GenerationMetrics:
    best = max(evaluations, key=lambda evaluation: evaluation.selected_rank_key)
    return GenerationMetrics(
        regime=regime,
        replicate=replicate,
        generation=generation,
        best_correctness=best.correctness,
        best_stability=best.stability,
        best_score=best.score,
        best_frozen_fraction=best.frozen_fraction,
        best_lambda=best.derrida_lambda,
        best_cycle_length=best.attractor_cycle_length,
        mean_correctness=statistics.fmean(evaluation.correctness for evaluation in evaluations),
        mean_stability=statistics.fmean(evaluation.stability for evaluation in evaluations),
        mean_frozen_fraction=statistics.fmean(evaluation.frozen_fraction for evaluation in evaluations),
        mean_lambda=statistics.fmean(evaluation.derrida_lambda for evaluation in evaluations),
        mean_cycle_length=statistics.fmean(evaluation.attractor_cycle_length for evaluation in evaluations),
        threshold_generation=threshold_generation,
    )


def run_replicate(
    regime: str,
    replicate: int,
    seed: int,
    config: SimulationConfig,
) -> tuple[list[GenerationMetrics], ReplicateSummary]:
    rng = random.Random(seed)
    population = initialize_population(config, rng)
    threshold_generation: int | None = None
    stop_generation: int | None = None
    generation_metrics: list[GenerationMetrics] = []

    generation = 0
    while generation < config.max_generations:
        evaluations = [evaluate_network(network, config, rng) for network in population]
        metrics = summarize_generation(regime, replicate, generation, evaluations, threshold_generation)
        generation_metrics.append(metrics)

        if threshold_generation is None and metrics.best_correctness >= config.fitness_threshold:
            threshold_generation = generation
            stop_generation = generation + config.post_optimal_generations

        if stop_generation is not None and generation >= stop_generation:
            break

        threshold_reached = threshold_generation is not None
        population = select_next_population(
            regime=regime,
            population=population,
            evaluations=evaluations,
            config=config,
            rng=rng,
            threshold_reached=threshold_reached,
        )
        generation += 1

    if threshold_generation is None:
        post_optimal_slope = None
    else:
        post_optimal_series = [
            metrics.best_frozen_fraction
            for metrics in generation_metrics
            if metrics.generation >= threshold_generation
        ]
        post_optimal_slope = linear_slope(post_optimal_series)

    final_metrics = generation_metrics[-1]
    summary = ReplicateSummary(
        regime=regime,
        replicate=replicate,
        seed=seed,
        threshold_generation=threshold_generation,
        generations_completed=final_metrics.generation + 1,
        post_optimal_slope=post_optimal_slope,
        final_best_correctness=final_metrics.best_correctness,
        final_best_stability=final_metrics.best_stability,
        final_best_frozen_fraction=final_metrics.best_frozen_fraction,
        final_best_lambda=final_metrics.best_lambda,
    )
    return generation_metrics, summary


def write_generation_metrics(path: Path, metrics: Iterable[GenerationMetrics]) -> None:
    fieldnames = [
        "regime",
        "replicate",
        "generation",
        "best_correctness",
        "best_stability",
        "best_score",
        "best_frozen_fraction",
        "best_lambda",
        "best_cycle_length",
        "mean_correctness",
        "mean_stability",
        "mean_frozen_fraction",
        "mean_lambda",
        "mean_cycle_length",
        "threshold_generation",
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
        slopes = [summary.post_optimal_slope for summary in regime_summaries if summary.post_optimal_slope is not None]
        aggregate[regime] = {
            "replicates": len(regime_summaries),
            "threshold_reached_fraction": sum(
                1 for summary in regime_summaries if summary.threshold_generation is not None
            )
            / len(regime_summaries),
            "mean_final_best_correctness": statistics.fmean(
                summary.final_best_correctness for summary in regime_summaries
            ),
            "mean_final_best_frozen_fraction": statistics.fmean(
                summary.final_best_frozen_fraction for summary in regime_summaries
            ),
            "mean_final_best_lambda": statistics.fmean(
                summary.final_best_lambda for summary in regime_summaries
            ),
            "mean_post_optimal_slope": statistics.fmean(slopes) if slopes else None,
            "median_post_optimal_slope": statistics.median(slopes) if slopes else None,
            "positive_slope_fraction": (
                sum(1 for slope in slopes if slope > 0) / len(slopes) if slopes else None
            ),
        }
    return aggregate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        default="Formalization/simulations/output/prediction9_pilot",
        help="Directory for CSV and JSON outputs.",
    )
    parser.add_argument(
        "--regimes",
        nargs="+",
        choices=["selected", "neutral_post_threshold", "mutation_only"],
        default=["selected", "neutral_post_threshold", "mutation_only"],
        help="Evolution regimes to run.",
    )
    parser.add_argument("--replicates", type=int, default=3)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--num-inputs", type=int, default=DEFAULT_CONFIG.num_inputs)
    parser.add_argument("--num-dynamic-nodes", type=int, default=DEFAULT_CONFIG.num_dynamic_nodes)
    parser.add_argument("--num-outputs", type=int, default=DEFAULT_CONFIG.num_outputs)
    parser.add_argument("--connectivity", type=int, default=DEFAULT_CONFIG.connectivity)
    parser.add_argument("--truth-bias", type=float, default=DEFAULT_CONFIG.truth_bias)
    parser.add_argument("--population-size", type=int, default=DEFAULT_CONFIG.population_size)
    parser.add_argument("--input-sample-limit", type=int, default=DEFAULT_CONFIG.input_sample_limit)
    parser.add_argument("--eval-trials", type=int, default=DEFAULT_CONFIG.eval_trials)
    parser.add_argument("--settle-steps", type=int, default=DEFAULT_CONFIG.settle_steps)
    parser.add_argument("--attractor-steps", type=int, default=DEFAULT_CONFIG.attractor_steps)
    parser.add_argument("--derrida-samples", type=int, default=DEFAULT_CONFIG.derrida_samples)
    parser.add_argument("--fitness-threshold", type=float, default=DEFAULT_CONFIG.fitness_threshold)
    parser.add_argument("--max-generations", type=int, default=DEFAULT_CONFIG.max_generations)
    parser.add_argument(
        "--post-optimal-generations",
        type=int,
        default=DEFAULT_CONFIG.post_optimal_generations,
    )
    parser.add_argument("--elite-count", type=int, default=DEFAULT_CONFIG.elite_count)
    parser.add_argument("--parent-pool-size", type=int, default=DEFAULT_CONFIG.parent_pool_size)
    parser.add_argument("--stability-weight", type=float, default=DEFAULT_CONFIG.stability_weight)
    parser.add_argument("--rewire-probability", type=float, default=DEFAULT_CONFIG.rewire_probability)
    parser.add_argument(
        "--truth-table-flip-probability",
        type=float,
        default=DEFAULT_CONFIG.truth_table_flip_probability,
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = build_config(
        num_inputs=args.num_inputs,
        num_dynamic_nodes=args.num_dynamic_nodes,
        num_outputs=args.num_outputs,
        connectivity=args.connectivity,
        truth_bias=args.truth_bias,
        population_size=args.population_size,
        input_sample_limit=args.input_sample_limit,
        eval_trials=args.eval_trials,
        settle_steps=args.settle_steps,
        attractor_steps=args.attractor_steps,
        derrida_samples=args.derrida_samples,
        fitness_threshold=args.fitness_threshold,
        max_generations=args.max_generations,
        post_optimal_generations=args.post_optimal_generations,
        elite_count=args.elite_count,
        parent_pool_size=args.parent_pool_size,
        stability_weight=args.stability_weight,
        rewire_probability=args.rewire_probability,
        truth_table_flip_probability=args.truth_table_flip_probability,
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    all_generation_metrics: list[GenerationMetrics] = []
    all_summaries: list[ReplicateSummary] = []
    regime_offsets = {regime: index * 100_000 for index, regime in enumerate(args.regimes)}

    for regime in args.regimes:
        for replicate in range(args.replicates):
            seed = args.seed + regime_offsets[regime] + replicate
            generation_metrics, summary = run_replicate(
                regime=regime,
                replicate=replicate,
                seed=seed,
                config=config,
            )
            all_generation_metrics.extend(generation_metrics)
            all_summaries.append(summary)

    write_generation_metrics(output_dir / "generation_metrics.csv", all_generation_metrics)
    write_json(output_dir / "simulation_config.json", config.__dict__)
    write_json(
        output_dir / "replicate_summaries.json",
        [summary.__dict__ for summary in all_summaries],
    )
    write_json(output_dir / "aggregate_summary.json", aggregate_summaries(all_summaries))

    aggregate = aggregate_summaries(all_summaries)
    print("Prediction 9 pilot complete.")
    print(f"Output directory: {output_dir}")
    for regime in args.regimes:
        regime_summary = aggregate.get(regime, {})
        print(
            f"{regime}: "
            f"threshold_reached_fraction={regime_summary.get('threshold_reached_fraction')} "
            f"positive_slope_fraction={regime_summary.get('positive_slope_fraction')} "
            f"mean_post_optimal_slope={regime_summary.get('mean_post_optimal_slope')}"
        )


if __name__ == "__main__":
    main()
