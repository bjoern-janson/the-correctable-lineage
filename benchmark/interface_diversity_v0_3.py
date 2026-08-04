from __future__ import annotations

import argparse
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class Channel:
    name: str
    shares_primary_blind_spot: bool
    residual_error: float
    cost: float

    def validate(self) -> None:
        if not 0.0 <= self.residual_error <= 1.0:
            raise ValueError("residual_error must be in [0, 1]")
        if self.cost < 0.0:
            raise ValueError("cost must be non-negative")


@dataclass(frozen=True)
class Scenario:
    name: str
    calibration_episodes: int = 4000
    evaluation_episodes: int = 5000
    shared_failure_calibration: float = 0.05
    shared_failure_evaluation: float = 0.25
    primary_residual_error: float = 0.08
    stress_weight: float = 0.50
    minimum_primary_failures: int = 50
    channels: Tuple[Channel, ...] = ()
    description: str = ""

    def validate(self) -> None:
        for value_name, value in (
            ("shared_failure_calibration", self.shared_failure_calibration),
            ("shared_failure_evaluation", self.shared_failure_evaluation),
            ("primary_residual_error", self.primary_residual_error),
            ("stress_weight", self.stress_weight),
        ):
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{value_name} must be in [0, 1]")
        if self.calibration_episodes <= 0 or self.evaluation_episodes <= 0:
            raise ValueError("episode counts must be positive")
        if self.minimum_primary_failures < 0:
            raise ValueError("minimum_primary_failures must be non-negative")
        if not self.channels:
            raise ValueError("at least one correction channel is required")
        names = [channel.name for channel in self.channels]
        if len(names) != len(set(names)):
            raise ValueError("channel names must be unique")
        for channel in self.channels:
            channel.validate()


BASE_CHANNELS = (
    Channel("redundant_a", True, 0.010, 0.010),
    Channel("redundant_b", True, 0.015, 0.010),
    Channel("independent", False, 0.120, 0.040),
)

SCENARIOS: Dict[str, Scenario] = {
    "shared_blind_spot_shift": Scenario(
        name="shared_blind_spot_shift",
        channels=BASE_CHANNELS,
        description=(
            "Two high-marginal-accuracy channels share the primary blind spot; "
            "one lower-marginal-accuracy channel has independent errors."
        ),
    ),
    "redundant_quantity": Scenario(
        name="redundant_quantity",
        channels=tuple(
            [Channel(f"redundant_{index}", True, 0.010 + 0.002 * index, 0.010)
             for index in range(5)]
            + [Channel("independent", False, 0.120, 0.040)]
        ),
        description=(
            "Five correlated correction channels compete with one independent channel."
        ),
    ),
    "all_independent": Scenario(
        name="all_independent",
        shared_failure_calibration=0.10,
        shared_failure_evaluation=0.20,
        channels=(
            Channel("independent_a", False, 0.050, 0.020),
            Channel("independent_b", False, 0.100, 0.030),
            Channel("independent_c", False, 0.150, 0.040),
        ),
        description=(
            "All channels have independent errors; diversity-aware selection should "
            "reduce to ordinary net-performance selection."
        ),
    ),
    "all_costly": Scenario(
        name="all_costly",
        channels=(
            Channel("redundant_a", True, 0.010, 0.400),
            Channel("redundant_b", True, 0.015, 0.400),
            Channel("independent", False, 0.120, 0.900),
        ),
        description=(
            "Every correction channel is too costly relative to its declared value."
        ),
    ),
    "no_exposed_primary_failures": Scenario(
        name="no_exposed_primary_failures",
        shared_failure_calibration=0.0,
        shared_failure_evaluation=0.25,
        primary_residual_error=0.0,
        channels=BASE_CHANNELS,
        description=(
            "Calibration contains no primary failure, so correction-path independence "
            "cannot be estimated before deployment shift."
        ),
    ),
}


@dataclass(frozen=True)
class Episode:
    target: int
    primary: int
    channels: Dict[str, int]
    shared_failure: bool


@dataclass
class EvalMetrics:
    scenario: str
    agent: str
    seed: int
    accuracy: float
    mean_net_reward: float
    selected_path: str
    selected_cost: float
    calibration_primary_failures: int
    selected_correction_coverage: Optional[float]
    selected_error_agreement: Optional[float]


class CorrectionPathTask:
    def __init__(self, scenario: Scenario, seed: int):
        scenario.validate()
        self.scenario = scenario
        self.rng = random.Random(seed)

    def sample(self, phase: str) -> Episode:
        if phase not in {"calibration", "evaluation"}:
            raise ValueError("phase must be calibration or evaluation")
        shared_rate = (
            self.scenario.shared_failure_calibration
            if phase == "calibration"
            else self.scenario.shared_failure_evaluation
        )
        target = self.rng.randrange(2)
        shared_failure = self.rng.random() < shared_rate

        if shared_failure:
            primary = 1 - target
        else:
            primary = (
                1 - target
                if self.rng.random() < self.scenario.primary_residual_error
                else target
            )

        channel_outputs: Dict[str, int] = {}
        for channel in self.scenario.channels:
            if channel.shares_primary_blind_spot and shared_failure:
                output = 1 - target
            else:
                output = (
                    1 - target
                    if self.rng.random() < channel.residual_error
                    else target
                )
            channel_outputs[channel.name] = output

        return Episode(
            target=target,
            primary=primary,
            channels=channel_outputs,
            shared_failure=shared_failure,
        )


def sample_phase(task: CorrectionPathTask, phase: str, episodes: int) -> List[Episode]:
    return [task.sample(phase) for _ in range(episodes)]


def accuracy(rows: Sequence[Episode], path: str) -> float:
    if path == "primary":
        return statistics.fmean(float(row.primary == row.target) for row in rows)
    return statistics.fmean(
        float(row.channels[path] == row.target) for row in rows
    )


def correction_coverage(rows: Sequence[Episode], path: str) -> Optional[float]:
    failed = [row for row in rows if row.primary != row.target]
    if not failed:
        return None
    return statistics.fmean(
        float(row.channels[path] == row.target) for row in failed
    )


def error_agreement(rows: Sequence[Episode], path: str) -> Optional[float]:
    primary_errors = [row.primary != row.target for row in rows]
    channel_errors = [row.channels[path] != row.target for row in rows]
    if len(set(primary_errors)) < 2 or len(set(channel_errors)) < 2:
        return None
    p_mean = statistics.fmean(primary_errors)
    c_mean = statistics.fmean(channel_errors)
    covariance = statistics.fmean(
        (float(p) - p_mean) * (float(c) - c_mean)
        for p, c in zip(primary_errors, channel_errors)
    )
    p_var = statistics.fmean((float(p) - p_mean) ** 2 for p in primary_errors)
    c_var = statistics.fmean((float(c) - c_mean) ** 2 for c in channel_errors)
    if p_var <= 0.0 or c_var <= 0.0:
        return None
    return covariance / ((p_var * c_var) ** 0.5)


def primary_failure_count(rows: Sequence[Episode]) -> int:
    return sum(row.primary != row.target for row in rows)


def select_raw_accuracy(scenario: Scenario, calibration: Sequence[Episode]) -> str:
    best_path = "primary"
    best_score = accuracy(calibration, "primary")
    for channel in scenario.channels:
        score = accuracy(calibration, channel.name) - channel.cost
        if score > best_score:
            best_path = channel.name
            best_score = score
    return best_path


def select_independence_aware(
    scenario: Scenario,
    calibration: Sequence[Episode],
) -> str:
    failures = [row for row in calibration if row.primary != row.target]
    if len(failures) < scenario.minimum_primary_failures:
        return "primary"

    primary_accuracy = accuracy(calibration, "primary")
    best_path = "primary"
    best_score = (1.0 - scenario.stress_weight) * primary_accuracy

    for channel in scenario.channels:
        marginal_accuracy = accuracy(calibration, channel.name)
        coverage = statistics.fmean(
            float(row.channels[channel.name] == row.target)
            for row in failures
        )
        score = (
            (1.0 - scenario.stress_weight) * marginal_accuracy
            + scenario.stress_weight * coverage
            - channel.cost
        )
        if score > best_score:
            best_path = channel.name
            best_score = score
    return best_path


def select_oracle(scenario: Scenario, evaluation: Sequence[Episode]) -> str:
    paths = ["primary"] + [channel.name for channel in scenario.channels]
    cost_by_path = {"primary": 0.0}
    cost_by_path.update({channel.name: channel.cost for channel in scenario.channels})
    return max(
        paths,
        key=lambda path: accuracy(evaluation, path) - cost_by_path[path],
    )


def majority_prediction(row: Episode, channels: Sequence[Channel]) -> int:
    votes = [row.channels[channel.name] for channel in channels]
    ones = sum(votes)
    if ones * 2 == len(votes):
        return row.primary
    return 1 if ones > len(votes) / 2 else 0


def evaluate_path(
    scenario: Scenario,
    evaluation: Sequence[Episode],
    path: str,
) -> Tuple[float, float, float]:
    if path == "majority_all":
        acc = statistics.fmean(
            float(majority_prediction(row, scenario.channels) == row.target)
            for row in evaluation
        )
        cost = sum(channel.cost for channel in scenario.channels)
        return acc, acc - cost, cost
    if path == "primary":
        acc = accuracy(evaluation, path)
        return acc, acc, 0.0
    channel = next(channel for channel in scenario.channels if channel.name == path)
    acc = accuracy(evaluation, path)
    return acc, acc - channel.cost, channel.cost


AGENTS = (
    "primary_only",
    "raw_accuracy_selector",
    "independence_selector",
    "count_all_tests",
    "oracle_selector",
)


def evaluate_agent_from_data(
    scenario: Scenario,
    agent: str,
    seed: int,
    calibration: Sequence[Episode],
    evaluation: Sequence[Episode],
) -> EvalMetrics:
    if agent == "primary_only":
        path = "primary"
    elif agent == "raw_accuracy_selector":
        path = select_raw_accuracy(scenario, calibration)
    elif agent == "independence_selector":
        path = select_independence_aware(scenario, calibration)
    elif agent == "count_all_tests":
        path = "majority_all"
    elif agent == "oracle_selector":
        path = select_oracle(scenario, evaluation)
    else:
        raise KeyError(f"unknown agent: {agent}")

    eval_accuracy, net_reward, selected_cost = evaluate_path(
        scenario, evaluation, path
    )

    coverage: Optional[float] = None
    agreement: Optional[float] = None
    if path not in {"primary", "majority_all"}:
        coverage = correction_coverage(calibration, path)
        agreement = error_agreement(calibration, path)

    return EvalMetrics(
        scenario=scenario.name,
        agent=agent,
        seed=seed,
        accuracy=eval_accuracy,
        mean_net_reward=net_reward,
        selected_path=path,
        selected_cost=selected_cost,
        calibration_primary_failures=primary_failure_count(calibration),
        selected_correction_coverage=coverage,
        selected_error_agreement=agreement,
    )


def run_seed(scenario: Scenario, seed: int) -> List[EvalMetrics]:
    task = CorrectionPathTask(scenario, seed)
    calibration = sample_phase(
        task, "calibration", scenario.calibration_episodes
    )
    evaluation = sample_phase(
        task, "evaluation", scenario.evaluation_episodes
    )
    return [
        evaluate_agent_from_data(
            scenario, agent, seed, calibration, evaluation
        )
        for agent in AGENTS
    ]


def run_one(scenario: Scenario, agent: str, seed: int) -> EvalMetrics:
    """Convenience wrapper used by unit tests."""
    return next(row for row in run_seed(scenario, seed) if row.agent == agent)


def aggregate(metrics: Iterable[EvalMetrics]) -> List[dict]:
    grouped: Dict[Tuple[str, str], List[EvalMetrics]] = {}
    for item in metrics:
        grouped.setdefault((item.scenario, item.agent), []).append(item)

    output: List[dict] = []
    for (scenario, agent), rows in sorted(grouped.items()):
        selection_counts: Dict[str, int] = {}
        for row in rows:
            selection_counts[row.selected_path] = (
                selection_counts.get(row.selected_path, 0) + 1
            )
        coverages = [
            row.selected_correction_coverage
            for row in rows
            if row.selected_correction_coverage is not None
        ]
        agreements = [
            row.selected_error_agreement
            for row in rows
            if row.selected_error_agreement is not None
        ]
        output.append(
            {
                "scenario": scenario,
                "agent": agent,
                "n_seeds": len(rows),
                "accuracy_mean": statistics.fmean(row.accuracy for row in rows),
                "accuracy_sd": statistics.pstdev(row.accuracy for row in rows),
                "net_reward_mean": statistics.fmean(
                    row.mean_net_reward for row in rows
                ),
                "net_reward_sd": statistics.pstdev(
                    row.mean_net_reward for row in rows
                ),
                "selected_cost_mean": statistics.fmean(
                    row.selected_cost for row in rows
                ),
                "calibration_primary_failures_mean": statistics.fmean(
                    row.calibration_primary_failures for row in rows
                ),
                "selected_correction_coverage_mean": (
                    statistics.fmean(coverages) if coverages else None
                ),
                "selected_error_agreement_mean": (
                    statistics.fmean(agreements) if agreements else None
                ),
                "selection_counts": dict(sorted(selection_counts.items())),
            }
        )
    return output


def benchmark_assertions(rows: List[dict]) -> List[dict]:
    index = {(row["scenario"], row["agent"]): row for row in rows}

    def row(scenario: str, agent: str) -> dict:
        return index[(scenario, agent)]

    checks = [
        (
            "independence_beats_marginal_accuracy_under_shift",
            row("shared_blind_spot_shift", "independence_selector")[
                "net_reward_mean"
            ]
            > row("shared_blind_spot_shift", "raw_accuracy_selector")[
                "net_reward_mean"
            ]
            + 0.08,
            "Failure-mode-aware selection should outperform marginal-accuracy selection after the shared blind spot becomes more common.",
        ),
        (
            "independence_matches_oracle_locally",
            row("shared_blind_spot_shift", "independence_selector")[
                "net_reward_mean"
            ]
            >= row("shared_blind_spot_shift", "oracle_selector")[
                "net_reward_mean"
            ]
            - 0.01,
            "The diversity-aware selector should approach the supplied-path oracle in the declared shift.",
        ),
        (
            "correlated_test_count_does_not_create_independence",
            row("redundant_quantity", "independence_selector")[
                "net_reward_mean"
            ]
            > row("redundant_quantity", "count_all_tests")[
                "net_reward_mean"
            ]
            + 0.10,
            "Counting many correlated tests should not match one selected independent correction path.",
        ),
        (
            "all_independent_reduces_to_performance_selection",
            abs(
                row("all_independent", "independence_selector")[
                    "net_reward_mean"
                ]
                - row("all_independent", "raw_accuracy_selector")[
                    "net_reward_mean"
                ]
            )
            < 0.01,
            "When candidate errors are already independent, the diversity criterion should not invent a disagreement.",
        ),
        (
            "costly_channels_rejected",
            row("all_costly", "independence_selector")["selection_counts"].get(
                "primary", 0
            )
            >= 0.95
            * row("all_costly", "independence_selector")["n_seeds"],
            "Independence should not receive authority when every available correction path is uneconomic.",
        ),
        (
            "unexposed_failure_blocks_independence_estimation",
            row("no_exposed_primary_failures", "independence_selector")[
                "selection_counts"
            ].get("primary", 0)
            >= 0.95
            * row("no_exposed_primary_failures", "independence_selector")[
                "n_seeds"
            ]
            and row("no_exposed_primary_failures", "independence_selector")[
                "net_reward_mean"
            ]
            < row("no_exposed_primary_failures", "oracle_selector")[
                "net_reward_mean"
            ]
            - 0.05,
            "Without calibration failures or a stress intervention, correction-path independence should remain unidentified.",
        ),
    ]
    return [
        {"name": name, "passed": bool(passed), "criterion": criterion}
        for name, passed, criterion in checks
    ]


def render_markdown(rows: List[dict], checks: List[dict], seeds: int) -> str:
    lines = [
        "# Interface Diversity Benchmark v0.3 — Frozen Exploratory Results",
        "",
        f"Generated by `benchmark/interface_diversity_v0_3.py` using {seeds} seeds per scenario-agent pair.",
        "",
        "## Aggregate evaluation",
        "",
        "| Scenario | Agent | Accuracy | Net reward | Mean cost | Selected paths |",
        "|---|---|---:|---:|---:|---|",
    ]
    for row in rows:
        selected = ", ".join(
            f"{name}:{count}"
            for name, count in row["selection_counts"].items()
        )
        lines.append(
            "| {scenario} | {agent} | {accuracy_mean:.3f} | "
            "{net_reward_mean:.3f} | {selected_cost_mean:.3f} | {selected} |".format(
                **row, selected=selected
            )
        )
    lines.extend(["", "## Frozen checks", ""])
    for check in checks:
        mark = "PASS" if check["passed"] else "FAIL"
        lines.append(f"- **{mark} — {check['name']}**: {check['criterion']}")
    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            "v0.3 tests selection among supplied correction channels using labeled calibration data and an externally declared stress weight.",
            "",
            "It supports only the local claim that failure-conditioned correction coverage can outperform marginal accuracy or correlated vote count under the declared shared-blind-spot shift.",
            "",
            "It does not establish autonomous generation of independent tests, prior construction, unlabeled failure discovery, universal independence metrics, or a distinct theory beyond robust ensemble selection and decision under correlated errors.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run Interface Diversity Benchmark v0.3."
    )
    parser.add_argument("--seeds", type=int, default=100)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("benchmark/results"),
    )
    args = parser.parse_args()
    if args.seeds <= 0:
        raise ValueError("seeds must be positive")

    metrics: List[EvalMetrics] = []
    for scenario in SCENARIOS.values():
        for seed in range(args.seeds):
            metrics.extend(run_seed(scenario, seed))

    rows = aggregate(metrics)
    checks = benchmark_assertions(rows)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    payload = {
        "schema_version": "0.3",
        "status": "frozen exploratory first implementation",
        "seeds": args.seeds,
        "scenarios": {
            name: {
                **asdict(scenario),
                "channels": [asdict(channel) for channel in scenario.channels],
            }
            for name, scenario in SCENARIOS.items()
        },
        "aggregate": rows,
        "checks": checks,
    }
    json_path = args.output_dir / "results-v0.3.json"
    markdown_path = args.output_dir / "results-v0.3.md"
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    markdown_path.write_text(render_markdown(rows, checks, args.seeds))

    failed = [check for check in checks if not check["passed"]]
    if failed:
        for check in failed:
            print(f"FAIL: {check['name']}: {check['criterion']}")
        return 1
    print(f"PASS: wrote {json_path} and {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
