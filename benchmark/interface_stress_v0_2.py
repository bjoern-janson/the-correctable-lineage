from __future__ import annotations

import argparse
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Literal, Tuple

WorldType = Literal["robust", "fragile"]


@dataclass(frozen=True)
class Scenario:
    name: str
    p_fragile: float
    deployment_episodes: int
    audit_episodes: int
    audit_cost: float
    sensor_accuracy: float = 0.9
    sensor_cost: float = 0.1
    audit_cue_accuracy_fragile: float = 0.5
    deployment_cue_accuracy_fragile: float = 0.5
    audit_threshold: float = 0.75
    decision_margin: float = 0.0
    description: str = ""

    def validate(self) -> None:
        for field_name in (
            "p_fragile",
            "sensor_accuracy",
            "sensor_cost",
            "audit_cue_accuracy_fragile",
            "deployment_cue_accuracy_fragile",
            "audit_threshold",
        ):
            value = getattr(self, field_name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{field_name} must be in [0, 1], got {value}")
        if self.deployment_episodes <= 0 or self.audit_episodes <= 0:
            raise ValueError("episode counts must be positive")
        if self.audit_cost < 0:
            raise ValueError("audit_cost must be non-negative")


SCENARIOS: Dict[str, Scenario] = {
    "balanced_affordable": Scenario(
        name="balanced_affordable",
        p_fragile=0.5,
        deployment_episodes=2000,
        audit_episodes=80,
        audit_cost=20.0,
        description="Ambiguous success, common fragility, and an economically justified challenge.",
    ),
    "rare_fragility": Scenario(
        name="rare_fragility",
        p_fragile=0.02,
        deployment_episodes=2000,
        audit_episodes=80,
        audit_cost=40.0,
        description="Fragility is possible but too rare to justify the declared audit cost under expected reward.",
    ),
    "expensive_audit": Scenario(
        name="expensive_audit",
        p_fragile=0.5,
        deployment_episodes=2000,
        audit_episodes=80,
        audit_cost=400.0,
        description="The challenge is informative but more expensive than its expected value.",
    ),
    "short_horizon": Scenario(
        name="short_horizon",
        p_fragile=0.5,
        deployment_episodes=40,
        audit_episodes=40,
        audit_cost=8.0,
        description="Too little deployment remains for the audit and repaired interface to repay their cost.",
    ),
    "uninformative_challenge": Scenario(
        name="uninformative_challenge",
        p_fragile=0.5,
        deployment_episodes=2000,
        audit_episodes=80,
        audit_cost=20.0,
        audit_cue_accuracy_fragile=1.0,
        description="The offered challenge preserves the training correlation and cannot expose hidden fragility.",
    ),
}


@dataclass(frozen=True)
class Episode:
    hidden: int
    cue: int
    sensor: int
    target: int


@dataclass
class RunMetrics:
    scenario: str
    agent: str
    seed: int
    world: WorldType
    audited: bool
    sensor_active: bool
    audit_accuracy: float | None
    accuracy: float
    mean_net_reward: float
    regret: float
    diagnosis_correct: bool | None


class TemporalInterfaceTask:
    """Two worlds with identical training success but different deployment semantics.

    Robust world: target is the visible cue.
    Fragile world: target is a latent state; training makes cue == latent, but
    deployment may break that relation.
    """

    def __init__(self, scenario: Scenario, seed: int):
        scenario.validate()
        self.scenario = scenario
        self.rng = random.Random(seed)
        self.world: WorldType = "fragile" if self.rng.random() < scenario.p_fragile else "robust"

    def _sample(self, cue_accuracy_fragile: float) -> Episode:
        hidden = self.rng.randrange(2)
        if self.world == "robust":
            cue = self.rng.randrange(2)
            target = cue
        else:
            cue = hidden if self.rng.random() < cue_accuracy_fragile else 1 - hidden
            target = hidden
        sensor = hidden if self.rng.random() < self.scenario.sensor_accuracy else 1 - hidden
        return Episode(hidden=hidden, cue=cue, sensor=sensor, target=target)

    def sample_audit(self) -> Episode:
        return self._sample(self.scenario.audit_cue_accuracy_fragile)

    def sample_deployment(self) -> Episode:
        return self._sample(self.scenario.deployment_cue_accuracy_fragile)


def static_cue_expected_reward(scenario: Scenario) -> float:
    return (1.0 - scenario.p_fragile) * 1.0 + scenario.p_fragile * max(
        scenario.deployment_cue_accuracy_fragile,
        1.0 - scenario.deployment_cue_accuracy_fragile,
    )


def static_sensor_expected_reward(scenario: Scenario) -> float:
    robust = 0.5 - scenario.sensor_cost
    fragile = max(scenario.sensor_accuracy, 1.0 - scenario.sensor_accuracy) - scenario.sensor_cost
    return (1.0 - scenario.p_fragile) * robust + scenario.p_fragile * fragile


def expected_post_audit_reward(scenario: Scenario) -> float:
    robust = 1.0
    fragile = max(
        max(scenario.deployment_cue_accuracy_fragile, 1.0 - scenario.deployment_cue_accuracy_fragile),
        max(scenario.sensor_accuracy, 1.0 - scenario.sensor_accuracy) - scenario.sensor_cost,
    )
    return (1.0 - scenario.p_fragile) * robust + scenario.p_fragile * fragile - (
        scenario.audit_cost / scenario.deployment_episodes
    )


def adaptive_should_audit(scenario: Scenario) -> bool:
    best_static = max(static_cue_expected_reward(scenario), static_sensor_expected_reward(scenario))
    return expected_post_audit_reward(scenario) > best_static + scenario.decision_margin


def static_prefers_sensor(scenario: Scenario) -> bool:
    return static_sensor_expected_reward(scenario) > static_cue_expected_reward(scenario)


def run_audit(env: TemporalInterfaceTask, scenario: Scenario) -> float:
    correct = 0
    for _ in range(scenario.audit_episodes):
        episode = env.sample_audit()
        correct += int(episode.cue == episode.target)
    return correct / scenario.audit_episodes


def deploy(
    env: TemporalInterfaceTask,
    scenario: Scenario,
    use_sensor: bool,
    audited: bool,
) -> Tuple[float, float]:
    correct = 0
    total_reward = -scenario.audit_cost if audited else 0.0
    for _ in range(scenario.deployment_episodes):
        episode = env.sample_deployment()
        action = episode.sensor if use_sensor else episode.cue
        is_correct = action == episode.target
        correct += int(is_correct)
        total_reward += 1.0 if is_correct else 0.0
        if use_sensor:
            total_reward -= scenario.sensor_cost
    return correct / scenario.deployment_episodes, total_reward / scenario.deployment_episodes


def oracle_policy(world: WorldType, scenario: Scenario) -> bool:
    if world == "robust":
        return False
    cue_value = max(
        scenario.deployment_cue_accuracy_fragile,
        1.0 - scenario.deployment_cue_accuracy_fragile,
    )
    sensor_value = max(scenario.sensor_accuracy, 1.0 - scenario.sensor_accuracy) - scenario.sensor_cost
    return sensor_value > cue_value


def run_one(scenario: Scenario, agent: str, seed: int) -> RunMetrics:
    env = TemporalInterfaceTask(scenario, seed)
    audited = False
    audit_accuracy: float | None = None
    sensor_active = False

    if agent == "fixed_interface":
        sensor_active = False
    elif agent == "always_sensor":
        sensor_active = True
    elif agent == "best_static":
        sensor_active = static_prefers_sensor(scenario)
    elif agent == "always_challenge":
        audited = True
        audit_accuracy = run_audit(env, scenario)
        sensor_active = audit_accuracy < scenario.audit_threshold
    elif agent == "adaptive_skeptic":
        audited = adaptive_should_audit(scenario)
        if audited:
            audit_accuracy = run_audit(env, scenario)
            sensor_active = audit_accuracy < scenario.audit_threshold
        else:
            sensor_active = static_prefers_sensor(scenario)
    elif agent == "oracle":
        sensor_active = oracle_policy(env.world, scenario)
    else:
        raise KeyError(f"Unknown agent: {agent}")

    accuracy, net_reward = deploy(env, scenario, sensor_active, audited)
    oracle_sensor = oracle_policy(env.world, scenario)
    oracle_env = TemporalInterfaceTask(scenario, seed)
    oracle_accuracy, oracle_reward = deploy(oracle_env, scenario, oracle_sensor, audited=False)
    _ = oracle_accuracy

    diagnosis_correct: bool | None = None
    if audited:
        predicted_fragile = sensor_active
        diagnosis_correct = predicted_fragile == (env.world == "fragile")

    return RunMetrics(
        scenario=scenario.name,
        agent=agent,
        seed=seed,
        world=env.world,
        audited=audited,
        sensor_active=sensor_active,
        audit_accuracy=audit_accuracy,
        accuracy=accuracy,
        mean_net_reward=net_reward,
        regret=oracle_reward - net_reward,
        diagnosis_correct=diagnosis_correct,
    )


AGENTS = (
    "fixed_interface",
    "always_sensor",
    "best_static",
    "always_challenge",
    "adaptive_skeptic",
    "oracle",
)


def aggregate(metrics: Iterable[RunMetrics]) -> List[dict]:
    grouped: Dict[Tuple[str, str], List[RunMetrics]] = {}
    for item in metrics:
        grouped.setdefault((item.scenario, item.agent), []).append(item)

    rows: List[dict] = []
    for (scenario, agent), items in sorted(grouped.items()):
        audited_items = [item for item in items if item.audited]
        fragile_items = [item for item in items if item.world == "fragile"]
        robust_items = [item for item in items if item.world == "robust"]
        rows.append(
            {
                "scenario": scenario,
                "agent": agent,
                "n_seeds": len(items),
                "fragile_rate": statistics.fmean(float(item.world == "fragile") for item in items),
                "accuracy_mean": statistics.fmean(item.accuracy for item in items),
                "net_reward_mean": statistics.fmean(item.mean_net_reward for item in items),
                "net_reward_sd": statistics.pstdev(item.mean_net_reward for item in items),
                "regret_mean": statistics.fmean(item.regret for item in items),
                "audit_rate": statistics.fmean(float(item.audited) for item in items),
                "sensor_rate": statistics.fmean(float(item.sensor_active) for item in items),
                "diagnosis_accuracy": (
                    statistics.fmean(float(item.diagnosis_correct) for item in audited_items)
                    if audited_items
                    else None
                ),
                "fragile_sensor_rate": (
                    statistics.fmean(float(item.sensor_active) for item in fragile_items)
                    if fragile_items
                    else None
                ),
                "robust_sensor_rate": (
                    statistics.fmean(float(item.sensor_active) for item in robust_items)
                    if robust_items
                    else None
                ),
            }
        )
    return rows


def benchmark_assertions(rows: List[dict]) -> List[dict]:
    index = {(row["scenario"], row["agent"]): row for row in rows}

    def r(scenario: str, agent: str) -> dict:
        return index[(scenario, agent)]

    checks = [
        (
            "balanced_hidden_failure_exposed",
            r("balanced_affordable", "adaptive_skeptic")["net_reward_mean"]
            > r("balanced_affordable", "fixed_interface")["net_reward_mean"] + 0.08,
            "A paid challenge should expose hidden fragility and improve expected deployment reward.",
        ),
        (
            "balanced_sensor_not_fetishized",
            r("balanced_affordable", "adaptive_skeptic")["net_reward_mean"]
            > r("balanced_affordable", "always_sensor")["net_reward_mean"] + 0.15,
            "Conditional challenge-and-repair should outperform unconditional sensor use.",
        ),
        (
            "balanced_diagnosis_localized",
            r("balanced_affordable", "adaptive_skeptic")["audit_rate"] >= 0.95
            and r("balanced_affordable", "adaptive_skeptic")["diagnosis_accuracy"] is not None
            and r("balanced_affordable", "adaptive_skeptic")["diagnosis_accuracy"] >= 0.9
            and r("balanced_affordable", "adaptive_skeptic")["fragile_sensor_rate"] is not None
            and r("balanced_affordable", "adaptive_skeptic")["fragile_sensor_rate"] >= 0.9
            and r("balanced_affordable", "adaptive_skeptic")["robust_sensor_rate"] is not None
            and r("balanced_affordable", "adaptive_skeptic")["robust_sensor_rate"] <= 0.1,
            "The challenge should distinguish hidden fragility from a robust interface rather than authorize universal revision.",
        ),
        (
            "rare_fragility_skepticism_bounded",
            r("rare_fragility", "adaptive_skeptic")["audit_rate"] <= 0.05
            and r("rare_fragility", "adaptive_skeptic")["net_reward_mean"]
            > r("rare_fragility", "always_challenge")["net_reward_mean"] + 0.005,
            "Low prior risk should not justify a costly universal challenge under the declared scalar objective.",
        ),
        (
            "expensive_audit_rejected",
            r("expensive_audit", "adaptive_skeptic")["audit_rate"] <= 0.05,
            "An informative challenge should be rejected when its expected value is below cost.",
        ),
        (
            "short_horizon_rejected",
            r("short_horizon", "adaptive_skeptic")["audit_rate"] <= 0.05,
            "A challenge should be rejected when too little deployment remains to repay it.",
        ),
        (
            "uninformative_challenge_exposes_limit",
            r("uninformative_challenge", "adaptive_skeptic")["audit_rate"] >= 0.95
            and r("uninformative_challenge", "adaptive_skeptic")["diagnosis_accuracy"] is not None
            and r("uninformative_challenge", "adaptive_skeptic")["diagnosis_accuracy"] < 0.7
            and r("uninformative_challenge", "adaptive_skeptic")["net_reward_mean"]
            < r("uninformative_challenge", "fixed_interface")["net_reward_mean"],
            "v0.2 should fail when the challenge interface preserves the hidden correlation it was meant to break.",
        ),
    ]
    return [
        {"name": name, "passed": bool(passed), "criterion": criterion}
        for name, passed, criterion in checks
    ]


def render_markdown(rows: List[dict], checks: List[dict], seeds: int) -> str:
    lines = [
        "# Interface Stress Benchmark v0.2 — Frozen Results",
        "",
        f"Generated by `benchmark/interface_stress_v0_2.py` using {seeds} seeds per scenario-agent pair.",
        "",
        "## Aggregate evaluation",
        "",
        "| Scenario | Agent | Accuracy | Net reward | Audit rate | Sensor rate | Diagnosis | Regret |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        diagnosis = "—" if row["diagnosis_accuracy"] is None else f"{row['diagnosis_accuracy']:.3f}"
        lines.append(
            f"| {row['scenario']} | {row['agent']} | {row['accuracy_mean']:.3f} | "
            f"{row['net_reward_mean']:.3f} | {row['audit_rate']:.3f} | "
            f"{row['sensor_rate']:.3f} | {diagnosis} | {row['regret_mean']:.3f} |"
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
            "A positive result supports only a bounded value-of-information claim: an agent can pay for a predeclared challenge that breaks a suspected training correlation, then conditionally deploy a predeclared sensor.",
            "",
            "The benchmark remains describable through Bayesian decision theory, active experiment design, costly information acquisition, and partially observable control. It does not establish autonomous interface discovery.",
        ]
    )
    return "\n".join(lines) + "\n"


def run_benchmark(seeds: int) -> Tuple[List[RunMetrics], List[dict], List[dict]]:
    metrics: List[RunMetrics] = []
    for scenario in SCENARIOS.values():
        for agent in AGENTS:
            for seed in range(seeds):
                metrics.append(run_one(scenario, agent, seed))
    rows = aggregate(metrics)
    checks = benchmark_assertions(rows)
    return metrics, rows, checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Interface Stress Benchmark v0.2")
    parser.add_argument("--seeds", type=int, default=200)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--markdown-out", type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    metrics, rows, checks = run_benchmark(args.seeds)
    payload = {
        "version": "0.2",
        "seeds": args.seeds,
        "scenarios": [asdict(scenario) for scenario in SCENARIOS.values()],
        "aggregates": rows,
        "checks": checks,
        "raw_run_count": len(metrics),
    }

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.markdown_out:
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_out.write_text(render_markdown(rows, checks, args.seeds), encoding="utf-8")
    if not args.json_out and not args.markdown_out:
        print(render_markdown(rows, checks, args.seeds))

    all_passed = all(check["passed"] for check in checks)
    if args.strict and not all_passed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
