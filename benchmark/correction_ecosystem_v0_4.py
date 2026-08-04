from __future__ import annotations

import argparse
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


@dataclass(frozen=True)
class Channel:
    name: str
    normal_accuracy: float
    cost: float
    dependency_group: str

    def validate(self) -> None:
        if not 0.0 <= self.normal_accuracy <= 1.0:
            raise ValueError("normal_accuracy must be in [0, 1]")
        if self.cost < 0:
            raise ValueError("channel cost must be non-negative")


@dataclass(frozen=True)
class Scenario:
    name: str
    calibration_n: int = 1000
    audit_n: int = 400
    eval_n: int = 2000
    audit_cost: float = 10.0
    shift_prior: float = 0.5
    stress_weight: float = 0.7
    p_dependency_calibration: float = 0.0
    p_dependency_audit: float = 0.5
    p_dependency_evaluation: float = 0.5
    common_flip_accuracy: float = 0.98
    audit_labels_available: bool = True
    channels: Tuple[Channel, ...] = ()
    description: str = ""

    def validate(self) -> None:
        if not self.channels:
            raise ValueError("scenario requires at least one channel")
        if self.channels[0].name != "primary":
            raise ValueError("first channel must be named primary")
        if any(n <= 0 for n in (self.calibration_n, self.audit_n, self.eval_n)):
            raise ValueError("sample sizes must be positive")
        if self.audit_cost < 0:
            raise ValueError("audit_cost must be non-negative")
        for value in (
            self.shift_prior,
            self.stress_weight,
            self.p_dependency_calibration,
            self.p_dependency_audit,
            self.p_dependency_evaluation,
            self.common_flip_accuracy,
        ):
            if not 0.0 <= value <= 1.0:
                raise ValueError("probability-like parameters must be in [0, 1]")
        for channel in self.channels:
            channel.validate()


DEFAULT_CHANNELS = (
    Channel("primary", 0.95, 0.00, "shared"),
    Channel("redundant_a", 0.96, 0.01, "shared"),
    Channel("redundant_b", 0.955, 0.01, "shared"),
    Channel("independent", 0.82, 0.04, "independent"),
)

ALL_SHARED_CHANNELS = (
    Channel("primary", 0.95, 0.00, "shared"),
    Channel("redundant_a", 0.96, 0.01, "shared"),
    Channel("redundant_b", 0.955, 0.01, "shared"),
)

ALL_INDEPENDENT_CHANNELS = (
    Channel("primary", 0.90, 0.00, "independent_primary"),
    Channel("independent_a", 0.94, 0.02, "independent_a"),
    Channel("independent_b", 0.90, 0.01, "independent_b"),
)


SCENARIOS: Dict[str, Scenario] = {
    "hidden_shared_dependency": Scenario(
        name="hidden_shared_dependency",
        channels=DEFAULT_CHANNELS,
        description=(
            "Ordinary calibration makes several channels look strong and weakly correlated. "
            "A supplied intervention activates a hidden upstream dependency shared by the "
            "primary and redundant channels while leaving one lower-accuracy path intact."
        ),
    ),
    "blind_intervention": Scenario(
        name="blind_intervention",
        channels=DEFAULT_CHANNELS,
        p_dependency_audit=0.0,
        description=(
            "The supplied audit preserves the hidden dependency state, so the correction "
            "ecosystem appears healthy even though deployment activates the shared failure."
        ),
    ),
    "all_independent": Scenario(
        name="all_independent",
        channels=ALL_INDEPENDENT_CHANNELS,
        shift_prior=0.0,
        p_dependency_audit=0.0,
        p_dependency_evaluation=0.0,
        description=(
            "All candidate channels have distinct failure processes. The ecosystem audit "
            "should reduce to ordinary net-performance selection."
        ),
    ),
    "costly_audit": Scenario(
        name="costly_audit",
        channels=DEFAULT_CHANNELS,
        audit_cost=600.0,
        description=(
            "A valid intervention exists, but its amortized cost exceeds the declared upper "
            "bound on expected benefit."
        ),
    ),
    "no_independent_path": Scenario(
        name="no_independent_path",
        channels=ALL_SHARED_CHANNELS,
        description=(
            "The intervention exposes a common-mode failure, but every supplied correction "
            "path shares it. Diagnosis is possible; repair is not."
        ),
    ),
    "unlabeled_audit": Scenario(
        name="unlabeled_audit",
        channels=DEFAULT_CHANNELS,
        audit_labels_available=False,
        description=(
            "The intervention can be performed, but target labels are unavailable, so the "
            "benchmark's ecosystem comparison cannot identify which paths remain correct."
        ),
    ),
}


@dataclass(frozen=True)
class Episode:
    target: int
    dependency_active: bool
    outputs: Dict[str, int]


@dataclass(frozen=True)
class Metrics:
    scenario: str
    agent: str
    seed: int
    accuracy: float
    net_reward: float
    selected_path: str
    audited: bool
    compromise_detected: bool


AGENTS = (
    "primary_only",
    "calibration_selector",
    "count_all_tests",
    "intervention_selector",
    "oracle_selector",
)


def sample_dataset(
    scenario: Scenario,
    count: int,
    dependency_probability: float,
    rng: random.Random,
) -> List[Episode]:
    rows: List[Episode] = []
    for _ in range(count):
        target = int(rng.random() < 0.5)
        dependency_active = rng.random() < dependency_probability
        shared_base = 1 - target if dependency_active else target
        outputs: Dict[str, int] = {}

        for channel in scenario.channels:
            if channel.dependency_group == "shared":
                if dependency_active:
                    output = (
                        shared_base
                        if rng.random() < scenario.common_flip_accuracy
                        else target
                    )
                else:
                    output = (
                        target
                        if rng.random() < channel.normal_accuracy
                        else 1 - target
                    )
            else:
                output = (
                    target
                    if rng.random() < channel.normal_accuracy
                    else 1 - target
                )
            outputs[channel.name] = output

        rows.append(
            Episode(
                target=target,
                dependency_active=dependency_active,
                outputs=outputs,
            )
        )
    return rows


def accuracy(rows: Iterable[Episode], channel_name: str) -> float:
    materialized = list(rows)
    return statistics.fmean(
        float(row.outputs[channel_name] == row.target) for row in materialized
    )


def majority_accuracy(rows: Iterable[Episode], names: Tuple[str, ...]) -> float:
    materialized = list(rows)
    correct: List[float] = []
    for row in materialized:
        votes = sum(row.outputs[name] for name in names)
        prediction = int(votes > len(names) / 2)
        correct.append(float(prediction == row.target))
    return statistics.fmean(correct)


def channel_cost(scenario: Scenario, name: str) -> float:
    for channel in scenario.channels:
        if channel.name == name:
            return channel.cost
    raise KeyError(name)


def calibration_choice(
    scenario: Scenario,
    calibration_rows: List[Episode],
) -> Tuple[str, Dict[str, float]]:
    scores = {
        channel.name: accuracy(calibration_rows, channel.name) - channel.cost
        for channel in scenario.channels
    }
    return max(scores, key=scores.get), scores


def maximum_possible_audit_value(scenario: Scenario) -> float:
    return scenario.shift_prior * 0.5


def should_audit(scenario: Scenario) -> bool:
    if not scenario.audit_labels_available:
        return False
    amortized_cost = scenario.audit_cost / scenario.eval_n
    return amortized_cost < maximum_possible_audit_value(scenario)


def intervention_choice(
    scenario: Scenario,
    calibration_rows: List[Episode],
    audit_rows: List[Episode],
) -> Tuple[str, Dict[str, float]]:
    amortized_audit_cost = scenario.audit_cost / scenario.eval_n
    scores: Dict[str, float] = {}
    for channel in scenario.channels:
        scores[channel.name] = (
            (1.0 - scenario.stress_weight)
            * accuracy(calibration_rows, channel.name)
            + scenario.stress_weight * accuracy(audit_rows, channel.name)
            - channel.cost
            - amortized_audit_cost
        )
    return max(scores, key=scores.get), scores


def oracle_choice(
    scenario: Scenario,
    evaluation_rows: List[Episode],
) -> Tuple[str, Dict[str, float]]:
    scores = {
        channel.name: accuracy(evaluation_rows, channel.name) - channel.cost
        for channel in scenario.channels
    }
    return max(scores, key=scores.get), scores


def evaluate_selected(
    scenario: Scenario,
    evaluation_rows: List[Episode],
    selected_path: str,
    audit_paid: bool,
) -> Tuple[float, float]:
    observed_accuracy = accuracy(evaluation_rows, selected_path)
    cost = channel_cost(scenario, selected_path)
    if audit_paid:
        cost += scenario.audit_cost / scenario.eval_n
    return observed_accuracy, observed_accuracy - cost


def evaluate_majority(
    scenario: Scenario,
    evaluation_rows: List[Episode],
) -> Tuple[float, float]:
    names = tuple(channel.name for channel in scenario.channels)
    observed_accuracy = majority_accuracy(evaluation_rows, names)
    cost = sum(
        channel.cost for channel in scenario.channels if channel.name != "primary"
    )
    return observed_accuracy, observed_accuracy - cost


def run_one(scenario: Scenario, agent: str, seed: int) -> Metrics:
    scenario.validate()
    rng = random.Random(seed)
    calibration_rows = sample_dataset(
        scenario,
        scenario.calibration_n,
        scenario.p_dependency_calibration,
        rng,
    )
    audit_rows = sample_dataset(
        scenario,
        scenario.audit_n,
        scenario.p_dependency_audit,
        rng,
    )
    evaluation_rows = sample_dataset(
        scenario,
        scenario.eval_n,
        scenario.p_dependency_evaluation,
        rng,
    )

    audited = False
    compromise_detected = False

    if agent == "primary_only":
        selected_path = "primary"
        observed_accuracy, net_reward = evaluate_selected(
            scenario, evaluation_rows, selected_path, audit_paid=False
        )

    elif agent == "calibration_selector":
        selected_path, _ = calibration_choice(scenario, calibration_rows)
        observed_accuracy, net_reward = evaluate_selected(
            scenario, evaluation_rows, selected_path, audit_paid=False
        )

    elif agent == "count_all_tests":
        selected_path = "majority_all"
        observed_accuracy, net_reward = evaluate_majority(
            scenario, evaluation_rows
        )

    elif agent == "intervention_selector":
        if should_audit(scenario):
            audited = True
            selected_path, scores = intervention_choice(
                scenario, calibration_rows, audit_rows
            )
            best_audit_accuracy = max(
                accuracy(audit_rows, channel.name)
                for channel in scenario.channels
            )
            compromise_detected = best_audit_accuracy <= 0.55

            if compromise_detected:
                selected_path = "primary"
            elif scores[selected_path] <= scores["primary"]:
                selected_path = "primary"

            observed_accuracy, net_reward = evaluate_selected(
                scenario, evaluation_rows, selected_path, audit_paid=True
            )
        else:
            selected_path, _ = calibration_choice(scenario, calibration_rows)
            observed_accuracy, net_reward = evaluate_selected(
                scenario, evaluation_rows, selected_path, audit_paid=False
            )

    elif agent == "oracle_selector":
        selected_path, _ = oracle_choice(scenario, evaluation_rows)
        observed_accuracy, net_reward = evaluate_selected(
            scenario, evaluation_rows, selected_path, audit_paid=False
        )

    else:
        raise KeyError(f"unknown agent: {agent}")

    return Metrics(
        scenario=scenario.name,
        agent=agent,
        seed=seed,
        accuracy=observed_accuracy,
        net_reward=net_reward,
        selected_path=selected_path,
        audited=audited,
        compromise_detected=compromise_detected,
    )


def aggregate(metrics: Iterable[Metrics]) -> List[dict]:
    grouped: Dict[Tuple[str, str], List[Metrics]] = {}
    for metric in metrics:
        grouped.setdefault((metric.scenario, metric.agent), []).append(metric)

    rows: List[dict] = []
    for (scenario, agent), group in sorted(grouped.items()):
        selected_paths: Dict[str, int] = {}
        for metric in group:
            selected_paths[metric.selected_path] = (
                selected_paths.get(metric.selected_path, 0) + 1
            )
        rows.append(
            {
                "scenario": scenario,
                "agent": agent,
                "n_seeds": len(group),
                "accuracy_mean": statistics.fmean(
                    metric.accuracy for metric in group
                ),
                "accuracy_sd": statistics.pstdev(
                    metric.accuracy for metric in group
                ),
                "net_reward_mean": statistics.fmean(
                    metric.net_reward for metric in group
                ),
                "net_reward_sd": statistics.pstdev(
                    metric.net_reward for metric in group
                ),
                "audit_rate": statistics.fmean(
                    float(metric.audited) for metric in group
                ),
                "compromise_detection_rate": statistics.fmean(
                    float(metric.compromise_detected) for metric in group
                ),
                "selected_paths": selected_paths,
            }
        )
    return rows


def benchmark_assertions(rows: List[dict]) -> List[dict]:
    index = {(row["scenario"], row["agent"]): row for row in rows}

    def get(scenario: str, agent: str) -> dict:
        return index[(scenario, agent)]

    checks = [
        (
            "intervention_exposes_hidden_shared_dependency",
            get("hidden_shared_dependency", "intervention_selector")[
                "net_reward_mean"
            ]
            > get("hidden_shared_dependency", "calibration_selector")[
                "net_reward_mean"
            ]
            + 0.20,
            "A valid upstream intervention should reveal the common-mode failure and improve deployment reward.",
        ),
        (
            "intervention_matches_supplied_path_oracle",
            abs(
                get("hidden_shared_dependency", "intervention_selector")[
                    "net_reward_mean"
                ]
                - get("hidden_shared_dependency", "oracle_selector")[
                    "net_reward_mean"
                ]
            )
            < 0.02,
            "The intervention selector should approach the oracle over the supplied channel set.",
        ),
        (
            "blind_intervention_preserves_blind_spot",
            get("blind_intervention", "intervention_selector")[
                "net_reward_mean"
            ]
            <= get("blind_intervention", "primary_only")["net_reward_mean"]
            + 0.02,
            "An audit that preserves the latent dependency should not identify the independent correction path.",
        ),
        (
            "all_independent_reduces_to_performance_selection",
            abs(
                get("all_independent", "intervention_selector")[
                    "net_reward_mean"
                ]
                - get("all_independent", "calibration_selector")[
                    "net_reward_mean"
                ]
            )
            < 1e-12
            and get("all_independent", "intervention_selector")["audit_rate"]
            == 0.0,
            "When no shared-dependency risk is declared, ecosystem auditing should reduce to ordinary net-performance selection.",
        ),
        (
            "costly_audit_rejected",
            get("costly_audit", "intervention_selector")["audit_rate"] == 0.0
            and abs(
                get("costly_audit", "intervention_selector")[
                    "net_reward_mean"
                ]
                - get("costly_audit", "calibration_selector")[
                    "net_reward_mean"
                ]
            )
            < 1e-12,
            "A valid but uneconomic ecosystem audit should be rejected.",
        ),
        (
            "compromise_detected_without_false_repair",
            get("no_independent_path", "intervention_selector")[
                "compromise_detection_rate"
            ]
            >= 0.90
            and get("no_independent_path", "intervention_selector")[
                "selected_paths"
            ]
            == {"primary": get("no_independent_path", "intervention_selector")["n_seeds"]},
            "The agent should diagnose common-mode compromise without claiming that a redundant supplied path repairs it.",
        ),
        (
            "unlabeled_audit_blocks_identification",
            get("unlabeled_audit", "intervention_selector")["audit_rate"] == 0.0
            and abs(
                get("unlabeled_audit", "intervention_selector")[
                    "net_reward_mean"
                ]
                - get("unlabeled_audit", "calibration_selector")[
                    "net_reward_mean"
                ]
            )
            < 1e-12,
            "Without target labels or another correctness reference, the benchmark cannot identify which channel survives the intervention.",
        ),
    ]

    return [
        {"name": name, "passed": bool(passed), "criterion": criterion}
        for name, passed, criterion in checks
    ]


def render_markdown(rows: List[dict], checks: List[dict], seeds: int) -> str:
    lines = [
        "# Correction Ecosystem Benchmark v0.4 — Frozen Exploratory Results",
        "",
        f"Generated by `benchmark/correction_ecosystem_v0_4.py` using {seeds} seeds per scenario-agent pair.",
        "",
        "## Aggregate evaluation",
        "",
        "| Scenario | Agent | Accuracy | Net reward | Audit rate | Compromise detection | Selected paths |",
        "|---|---|---:|---:|---:|---:|---|",
    ]

    for row in rows:
        selected = ", ".join(
            f"{name}:{count}"
            for name, count in sorted(row["selected_paths"].items())
        )
        lines.append(
            "| {scenario} | {agent} | {accuracy_mean:.3f} | "
            "{net_reward_mean:.3f} | {audit_rate:.2f} | "
            "{compromise_detection_rate:.2f} | {selected} |".format(
                selected=selected, **row
            )
        )

    lines.extend(["", "## Frozen checks", ""])
    for check in checks:
        mark = "PASS" if check["passed"] else "FAIL"
        lines.append(
            f"- **{mark} — {check['name']}**: {check['criterion']}"
        )

    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            "v0.4 supplies the candidate channels, target labels, hidden-dependency intervention, costs, shift prior, and deployment horizon.",
            "",
            "It supports only the local claim that a supplied intervention on an upstream dependency can expose common-mode failure that ordinary calibration and output correlation do not reveal.",
            "",
            "It does not establish autonomous discovery of latent dependencies, generation of interventions, unlabeled truth identification, external-world validation of subjective experience, or a distinct theory beyond causal experiment design and robust selection under common-mode failure.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Correction Ecosystem Benchmark v0.4"
    )
    parser.add_argument(
        "--seeds",
        type=int,
        default=100,
        help="independent seeds per scenario-agent pair",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("benchmark/results"),
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="return non-zero when a frozen check fails",
    )
    args = parser.parse_args()

    metrics: List[Metrics] = []
    for scenario in SCENARIOS.values():
        for agent in AGENTS:
            for seed in range(args.seeds):
                metrics.append(run_one(scenario, agent, seed))

    rows = aggregate(metrics)
    checks = benchmark_assertions(rows)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "0.4",
        "status": "exploratory-first-implementation",
        "seeds": args.seeds,
        "scenarios": {
            name: {
                **asdict(scenario),
                "channels": [
                    asdict(channel) for channel in scenario.channels
                ],
            }
            for name, scenario in SCENARIOS.items()
        },
        "aggregate": rows,
        "checks": checks,
    }

    json_path = args.output_dir / "results-v0.4.json"
    md_path = args.output_dir / "results-v0.4.md"
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(
        render_markdown(rows, checks, args.seeds),
        encoding="utf-8",
    )

    for check in checks:
        mark = "PASS" if check["passed"] else "FAIL"
        print(f"{mark}: {check['name']}")

    if args.strict and not all(check["passed"] for check in checks):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
