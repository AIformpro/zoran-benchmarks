#!/usr/bin/env python3
"""
run_benchmark.py

This script runs comparative benchmarks between a baseline LLM (e.g. GPT-4o) and the Zoran IA framework.
It loads tasks from the `benchmarks/creative_tasks.json` file and outputs results to `results/zoran_vs_gpt.csv`.
Actual model scoring is left as an exercise; this script provides a placeholder implementation.
"""

import json
import csv
import argparse
from pathlib import Path


def load_tasks(tasks_path: Path) -> list:
    """Load benchmark tasks from a JSON file."""
    with tasks_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("tasks", [])


def run_placeholder_benchmarks(tasks: list) -> list:
    """
    Generate placeholder benchmark results.
    Replace this with actual evaluation of a baseline LLM and Zoran IA.
    Each result record is a dict with keys: task, metric, llm_score, zoran_score.
    """
    results = []
    for task in tasks:
        task_name = task["name"]
        # Placeholder: assign random-like but deterministic scores based on string lengths
        llm_score = round(min(1.0, len(task_name) / 20.0), 2)
        zoran_score = round(min(1.0, (len(task_name) + 5) / 20.0), 2)
        metric = "placeholder_metric"
        results.append({
            "task": task_name,
            "metric": metric,
            "llm_score": llm_score,
            "zoran_score": zoran_score,
        })
    return results


def write_results(results_path: Path, results: list) -> None:
    """Write benchmark results to a CSV file."""
    with results_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["task", "metric", "llm_score", "zoran_score"])
        writer.writeheader()
        writer.writerows(results)


def main(tasks_path: Path, results_path: Path) -> None:
    tasks = load_tasks(tasks_path)
    results = run_placeholder_benchmarks(tasks)
    write_results(results_path, results)
    print(f"Benchmark complete. Results saved to {results_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Zoran IA vs baseline benchmarks.")
    parser.add_argument(
        "--tasks",
        type=Path,
        default=Path("benchmarks/creative_tasks.json"),
        help="Path to the JSON file containing benchmark tasks.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/zoran_vs_gpt.csv"),
        help="Path to the CSV file where results will be written.",
    )
    args = parser.parse_args()

    main(args.tasks, args.output)
