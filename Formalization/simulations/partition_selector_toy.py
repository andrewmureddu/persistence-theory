#!/usr/bin/env python3
"""Toy spectral selector for partition-generating functors.

This script checks the first finite examples from
``bridges/partition_generating_functors.md`` without external dependencies:

1. a fully symmetric system, where no nontrivial canonical partition should be
   selected because the relevant eigenspace is degenerate;
2. a two-community weighted graph, where a Fiedler-vector sign partition appears
   when within-community coupling exceeds between-community coupling.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


Matrix = list[list[float]]


@dataclass
class SelectorResult:
    name: str
    eigenvalues: list[float]
    fiedler_value: float
    fiedler_gap: float
    fiedler_vector: list[float]
    partition: tuple[list[int], list[int]] | None


def identity(n: int) -> Matrix:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def jacobi_eigh(a: Matrix, tolerance: float = 1e-12, max_sweeps: int = 200) -> tuple[list[float], Matrix]:
    """Eigen-decomposition of a real symmetric matrix by Jacobi rotations."""
    n = len(a)
    mat = [row[:] for row in a]
    vecs = identity(n)

    for _ in range(max_sweeps):
        p, q = 0, 1
        max_off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                value = abs(mat[i][j])
                if value > max_off:
                    max_off = value
                    p, q = i, j
        if max_off < tolerance:
            break

        if abs(mat[p][p] - mat[q][q]) < tolerance:
            angle = math.pi / 4.0
        else:
            angle = 0.5 * math.atan2(2.0 * mat[p][q], mat[q][q] - mat[p][p])
        c = math.cos(angle)
        s = math.sin(angle)

        app = c * c * mat[p][p] - 2.0 * s * c * mat[p][q] + s * s * mat[q][q]
        aqq = s * s * mat[p][p] + 2.0 * s * c * mat[p][q] + c * c * mat[q][q]
        mat[p][p] = app
        mat[q][q] = aqq
        mat[p][q] = 0.0
        mat[q][p] = 0.0

        for r in range(n):
            if r == p or r == q:
                continue
            arp = mat[r][p]
            arq = mat[r][q]
            mat[r][p] = c * arp - s * arq
            mat[p][r] = mat[r][p]
            mat[r][q] = s * arp + c * arq
            mat[q][r] = mat[r][q]

        for r in range(n):
            vrp = vecs[r][p]
            vrq = vecs[r][q]
            vecs[r][p] = c * vrp - s * vrq
            vecs[r][q] = s * vrp + c * vrq

    pairs = sorted((mat[i][i], [vecs[r][i] for r in range(n)]) for i in range(n))
    eigenvalues = [p[0] for p in pairs]
    eigenvectors = [[pairs[col][1][row] for col in range(n)] for row in range(n)]
    return eigenvalues, eigenvectors


def laplacian(weights: Matrix) -> Matrix:
    n = len(weights)
    result = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        degree = sum(weights[i][j] for j in range(n) if j != i)
        result[i][i] = degree
        for j in range(n):
            if i != j:
                result[i][j] = -weights[i][j]
    return result


def symmetric_weights(n: int, coupling: float) -> Matrix:
    return [[0.0 if i == j else coupling for j in range(n)] for i in range(n)]


def two_community_weights(p: int, q: int, within: float, between: float) -> Matrix:
    n = p + q
    weights = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            same_left = i < p and j < p
            same_right = i >= p and j >= p
            weights[i][j] = within if same_left or same_right else between
    return weights


def spectral_selector(name: str, weights: Matrix, zero_tolerance: float = 1e-7) -> SelectorResult:
    if len(weights) < 2:
        raise ValueError("spectral selector requires at least two nodes")
    values, vectors = jacobi_eigh(laplacian(weights))
    fiedler_index = 1
    fiedler_value = values[fiedler_index]
    left_gap = values[fiedler_index] - values[fiedler_index - 1]
    right_gap = values[fiedler_index + 1] - values[fiedler_index] if len(values) > 2 else float("inf")
    fiedler_gap = min(left_gap, right_gap)
    vector = [vectors[row][fiedler_index] for row in range(len(weights))]

    positive = [i for i, x in enumerate(vector) if x > zero_tolerance]
    negative = [i for i, x in enumerate(vector) if x < -zero_tolerance]
    has_unstable_coordinate = len(positive) + len(negative) != len(vector)
    if fiedler_gap <= zero_tolerance or has_unstable_coordinate or not positive or not negative:
        partition = None
    else:
        partition = (positive, negative)

    return SelectorResult(name, values, fiedler_value, fiedler_gap, vector, partition)


def format_result(result: SelectorResult) -> str:
    values = ", ".join(f"{v:.6g}" for v in result.eigenvalues)
    vector = ", ".join(f"{v:+.3f}" for v in result.fiedler_vector)
    if result.partition is None:
        partition = "none selected (degenerate or sign-unstable selector)"
    else:
        partition = f"{result.partition[0]} | {result.partition[1]}"
    return (
        f"{result.name}\n"
        f"  eigenvalues: [{values}]\n"
        f"  fiedler value: {result.fiedler_value:.6g}\n"
        f"  fiedler gap: {result.fiedler_gap:.6g}\n"
        f"  fiedler vector: [{vector}]\n"
        f"  partition: {partition}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=8)
    parser.add_argument("--left-size", type=int, default=4)
    parser.add_argument("--right-size", type=int, default=4)
    parser.add_argument("--within", type=float, default=1.0)
    parser.add_argument("--between", type=float, default=0.2)
    args = parser.parse_args()

    if args.size < 2:
        parser.error("--size must be at least 2")
    if args.left_size < 1 or args.right_size < 1:
        parser.error("--left-size and --right-size must both be at least 1")
    if args.within <= 0.0 or args.between < 0.0:
        parser.error("--within must be positive and --between must be non-negative")

    examples = [
        ("fully symmetric", symmetric_weights(args.size, args.within)),
        (
            "two community",
            two_community_weights(args.left_size, args.right_size, args.within, args.between),
        ),
    ]
    for name, weights in examples:
        print(format_result(spectral_selector(name, weights)))
        print()


if __name__ == "__main__":
    main()
