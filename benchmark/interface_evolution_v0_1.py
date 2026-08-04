from __future__ import annotations

import argparse
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


@dataclass(frozen=True)
class Scenario:
    name: str
    train_episodes: int = 1200
    eval_episodes: int = 2000
    p_hidden_train: float = 0.5
    p_hidden_eval: float = 0.5
    cue_accuracy_train: float = 0.5
    cue_accuracy_eval: float = 0.5
    sensor_accuracy_train: float = 0.9
    sensor_accuracy_eval: float = 0.9
    sensor_cost: float = 0.1
    expected_revision: bool = True
    description: str = ""

    def validate(self) -> None:
        for name, value in (
            ("p_hidden_train", self.p_hidden_train),
            ("p_hidden_eval", self.p_hidden_eval),
            ("cue_accuracy_train", self.cue_accuracy_train),
            ("cue_accuracy_eval", self.cue_accuracy_eval),
            ("sensor_accuracy_train", self.sensor_accuracy_train),
            ("sensor_accuracy_eval", self.sensor_accuracy_eval),
        ):
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be in [0, 1], got {value}")
        if self.sensor_cost < 0:
            raise ValueError("sensor_cost must be non-negative")
        if self.train_episodes <= 0 or self.eval_episodes <= 0:
            raise ValueError("episode counts must be positive")


SCENARIOS: Dict[str, Scenario] = {
    "hidden_collision": Scenario(
        name="hidden_collision",
        cue_accuracy_train=0.5,
        cue_accuracy_eval=0.5,
        sensor_accuracy_train=0.9,
        sensor_accuracy_eval=0.9,
        sensor_cost=0.1,
        expected_revision=True,
        description="Initial cue is non-identifying; paid sensor separates the latent regimes.",
    ),
    "sufficient_interface": Scenario(
        name="sufficient_interface",
        cue_accuracy_train=1.0,
        cue_accuracy_eval=1.0,
        sensor_accuracy_train=0.9,
        sensor_accuracy_eval=0.9,
        sensor_cost=0.1,
        expected_revision=False,
        description="Initial cue already identifies the target; revision should be rejected.",
    ),
    "useless_sensor": Scenario(
        name="useless_sensor",
        cue_accuracy_train=0.5,
        cue_accuracy_eval=0.5,
        sensor_accuracy_train=0.5,
        sensor_accuracy_eval=0.5,
        sensor_cost=0.1,
        expected_revision=False,
        description="Initial interface is insufficient, but the offered sensor adds no target information.",
    ),
    "expensive_sensor": Scenario(
        name="expensive_sensor",
        cue_accuracy_train=0.5,
        cue_accuracy_eval=0.5,
        sensor_accuracy_train=0.9,
        sensor_accuracy_eval=0.9,
        sensor_cost=0.45,
        expected_revision=False,
        description="Sensor is informative but costs more than its expected benefit.",
    ),
    "moderate_transfer_shift": Scenario(
        name="moderate_transfer_shift",
        p_hidden_train=0.5,
        p_hidden_eval=0.6,
        cue_accuracy_train=0.5,
        cue_accuracy_eval=0.5,
        sensor_accuracy_train=0.9,
        sensor_accuracy_eval=0.85,
        sensor_cost=0.1,
        expected_revision=True,
        description="Acquired interface remains useful under preregistered prevalence and noise shift.",
    ),
    "spurious_training_cue": Scenario(
        name="spurious_training_cue",
        cue_accuracy_train=0.9,
        cue_accuracy_eval=0.5,
        sensor_accuracy_train=0.9,
        sensor_accuracy_eval=0.9,
        sensor_cost=0.1,
        expected_revision=False,
        description="Training cue hides the interface defect until a held-out shift removes the correlation.",
    ),
}


@dataclass
class Episode:
    hidden: int
    cue: int
    sensor: int


@dataclass
class Decision:
    action: int
    queried: bool
    cue: int
    sensor: Optional[int]


@dataclass
class EvalMetrics:
    scenario: str
    agent: str
    seed: int
    accuracy: float
    mean_net_reward: float
    query_rate: float
    regret: float
    revision_active: bool
    training_query_rate: float
    training_accuracy: float


class HiddenRegimeTask:
    def __init__(self, scenario: Scenario, seed: int):
        scenario.validate()
        self.scenario = scenario
        self.rng = random.Random(seed)

    def sample(self, phase: str) -> Episode:
        if phase not in {"train", "eval"}:
            raise ValueError("phase must be 'train' or 'eval'")
        is_train = phase == "train"
        p_hidden = self.scenario.p_hidden_train if is_train else self.scenario.p_hidden_eval
        cue_accuracy = self.scenario.cue_accuracy_train if is_train else self.scenario.cue_accuracy_eval
        sensor_accuracy = self.scenario.sensor_accuracy_train if is_train else self.scenario.sensor_accuracy_eval

        hidden = 1 if self.rng.random() < p_hidden else 0
        cue = hidden if self.rng.random() < cue_accuracy else 1 - hidden
        sensor = hidden if self.rng.random() < sensor_accuracy else 1 - hidden
        return Episode(hidden=hidden, cue=cue, sensor=sensor)


class BaseAgent:
    name = "base"

    def decide(self, episode: Episode, training: bool) -> Decision:
        raise NotImplementedError

    def observe(self, episode: Episode, decision: Decision, correct: bool, training: bool) -> None:
        raise NotImplementedError

    @property
    def revision_active(self) -> bool:
        return False


class CueModel:
    """Laplace-smoothed empirical P(hidden=1 | cue)."""

    def __init__(self) -> None:
        self.counts = {0: [1, 1], 1: [1, 1]}

    def predict(self, cue: int) -> int:
        zero, one = self.counts[cue]
        return 1 if one > zero else 0

    def expected_accuracy(self, cue: Optional[int] = None) -> float:
        if cue is not None:
            zero, one = self.counts[cue]
            return max(zero, one) / (zero + one)
        totals = []
        weights = []
        for c in (0, 1):
            zero, one = self.counts[c]
            totals.append(max(zero, one) / (zero + one))
            weights.append(zero + one)
        return sum(v * w for v, w in zip(totals, weights)) / sum(weights)

    def update(self, cue: int, hidden: int) -> None:
        self.counts[cue][hidden] += 1


class FixedInterfaceAgent(BaseAgent):
    name = "fixed_interface"

    def __init__(self) -> None:
        self.model = CueModel()

    def decide(self, episode: Episode, training: bool) -> Decision:
        action = self.model.predict(episode.cue)
        return Decision(action=action, queried=False, cue=episode.cue, sensor=None)

    def observe(self, episode: Episode, decision: Decision, correct: bool, training: bool) -> None:
        if training:
            self.model.update(episode.cue, episode.hidden)


class OracleInterfaceAgent(BaseAgent):
    name = "oracle_interface"

    def decide(self, episode: Episode, training: bool) -> Decision:
        return Decision(action=episode.sensor, queried=True, cue=episode.cue, sensor=episode.sensor)

    def observe(self, episode: Episode, decision: Decision, correct: bool, training: bool) -> None:
        return None

    @property
    def revision_active(self) -> bool:
        return True


class InterfaceRevisionAgent(BaseAgent):
    name = "interface_revision"

    def __init__(
        self,
        sensor_cost: float,
        warmup: int = 120,
        min_probes: int = 60,
        probe_probability: float = 0.35,
        insufficiency_threshold: float = 0.72,
        decision_margin: float = 0.02,
    ) -> None:
        self.model = CueModel()
        self.sensor_cost = sensor_cost
        self.warmup = warmup
        self.min_probes = min_probes
        self.probe_probability = probe_probability
        self.insufficiency_threshold = insufficiency_threshold
        self.decision_margin = decision_margin
        self.episodes_seen = 0
        self.sensor_correct = 1
        self.sensor_total = 2
        self._revision_active = False
        self._probe_mode = False

    @property
    def revision_active(self) -> bool:
        return self._revision_active

    def _sensor_accuracy_estimate(self) -> float:
        raw = self.sensor_correct / self.sensor_total
        return max(raw, 1.0 - raw)

    def _baseline_accuracy_estimate(self) -> float:
        return self.model.expected_accuracy()

    def _estimated_sensor_net(self) -> float:
        return self._sensor_accuracy_estimate() - self.sensor_cost

    def _maybe_update_revision_state(self) -> None:
        if self.episodes_seen < self.warmup:
            return
        baseline = self._baseline_accuracy_estimate()
        if baseline < self.insufficiency_threshold:
            self._probe_mode = True
        if self.sensor_total - 2 >= self.min_probes:
            advantage = self._estimated_sensor_net() - baseline
            self._revision_active = advantage > self.decision_margin
            self._probe_mode = False

    def decide(self, episode: Episode, training: bool) -> Decision:
        self._maybe_update_revision_state()
        query = self._revision_active
        if training and self._probe_mode and self.sensor_total - 2 < self.min_probes:
            query = random.random() < self.probe_probability

        if query:
            sensor_est = self.sensor_correct / self.sensor_total
            action = episode.sensor if sensor_est >= 0.5 else 1 - episode.sensor
            return Decision(action=action, queried=True, cue=episode.cue, sensor=episode.sensor)
        action = self.model.predict(episode.cue)
        return Decision(action=action, queried=False, cue=episode.cue, sensor=None)

    def observe(self, episode: Episode, decision: Decision, correct: bool, training: bool) -> None:
        if not training:
            return
        self.episodes_seen += 1
        self.model.update(episode.cue, episode.hidden)
        if decision.queried and decision.sensor is not None:
            self.sensor_total += 1
            if decision.sensor == episode.hidden:
                self.sensor_correct += 1
        self._maybe_update_revision_state()


class SeededInterfaceRevisionAgent(InterfaceRevisionAgent):
    """Revision agent with deterministic probing RNG."""

    def __init__(self, sensor_cost: float, seed: int, **kwargs: object) -> None:
        super().__init__(sensor_cost=sensor_cost, **kwargs)
        self.rng = random.Random(seed)

    def decide(self, episode: Episode, training: bool) -> Decision:
        self._maybe_update_revision_state()
        query = self._revision_active
        if training and self._probe_mode and self.sensor_total - 2 < self.min_probes:
            query = self.rng.random() < self.probe_probability

        if query:
            sensor_est = self.sensor_correct / self.sensor_total
            action = episode.sensor if sensor_est >= 0.5 else 1 - episode.sensor
            return Decision(action=action, queried=True, cue=episode.cue, sensor=episode.sensor)
        action = self.model.predict(episode.cue)
        return Decision(action=action, queried=False, cue=episode.cue, sensor=None)


def make_agent(name: str, scenario: Scenario, seed: int) -> BaseAgent:
    if name == FixedInterfaceAgent.name:
        return FixedInterfaceAgent()
    if name == OracleInterfaceAgent.name:
        return OracleInterfaceAgent()
    if name == InterfaceRevisionAgent.name:
        return SeededInterfaceRevisionAgent(sensor_cost=scenario.sensor_cost, seed=seed + 10_000)
    raise KeyError(f"Unknown agent: {name}")


def optimal_expected_reward(scenario: Scenario, phase: str) -> float:
    if phase == "train":
        p_hidden = scenario.p_hidden_train
        cue_accuracy = scenario.cue_accuracy_train
        sensor_accuracy = scenario.sensor_accuracy_train
    elif phase == "eval":
        p_hidden = scenario.p_hidden_eval
        cue_accuracy = scenario.cue_accuracy_eval
        sensor_accuracy = scenario.sensor_accuracy_eval
    else:
        raise ValueError("phase must be 'train' or 'eval'")

    majority_accuracy = max(p_hidden, 1.0 - p_hidden)
    cue_best = max(cue_accuracy, 1.0 - cue_accuracy)
    no_sensor = max(majority_accuracy, cue_best)
    sensor_net = max(sensor_accuracy, 1.0 - sensor_accuracy) - scenario.sensor_cost
    return max(no_sensor, sensor_net)


def run_phase(
    env: HiddenRegimeTask,
    agent: BaseAgent,
    scenario: Scenario,
    phase: str,
    episodes: int,
) -> Tuple[float, float, float]:
    correct_count = 0
    net_rewards: List[float] = []
    query_count = 0
    training = phase == "train"

    for _ in range(episodes):
        episode = env.sample(phase)
        decision = agent.decide(episode, training=training)
        correct = decision.action == episode.hidden
        reward = 1.0 if correct else 0.0
        if decision.queried:
            reward -= scenario.sensor_cost
            query_count += 1
        correct_count += int(correct)
        net_rewards.append(reward)
        agent.observe(episode, decision, correct, training=training)

    return (
        correct_count / episodes,
        statistics.fmean(net_rewards),
        query_count / episodes,
    )


def run_one(scenario: Scenario, agent_name: str, seed: int) -> EvalMetrics:
    env = HiddenRegimeTask(scenario, seed=seed)
    agent = make_agent(agent_name, scenario, seed)
    train_accuracy, _, train_query_rate = run_phase(
        env, agent, scenario, "train", scenario.train_episodes
    )
    eval_accuracy, eval_reward, eval_query_rate = run_phase(
        env, agent, scenario, "eval", scenario.eval_episodes
    )
    regret = optimal_expected_reward(scenario, "eval") - eval_reward
    return EvalMetrics(
        scenario=scenario.name,
        agent=agent_name,
        seed=seed,
        accuracy=eval_accuracy,
        mean_net_reward=eval_reward,
        query_rate=eval_query_rate,
        regret=regret,
        revision_active=agent.revision_active,
        training_query_rate=train_query_rate,
        training_accuracy=train_accuracy,
    )


def aggregate(metrics: Iterable[EvalMetrics]) -> List[dict]:
    grouped: Dict[Tuple[str, str], List[EvalMetrics]] = {}
    for item in metrics:
        grouped.setdefault((item.scenario, item.agent), []).append(item)

    output: List[dict] = []
    for (scenario, agent), rows in sorted(grouped.items()):
        output.append(
            {
                "scenario": scenario,
                "agent": agent,
                "n_seeds": len(rows),
                "accuracy_mean": statistics.fmean(r.accuracy for r in rows),
                "accuracy_sd": statistics.pstdev(r.accuracy for r in rows),
                "net_reward_mean": statistics.fmean(r.mean_net_reward for r in rows),
                "net_reward_sd": statistics.pstdev(r.mean_net_reward for r in rows),
                "query_rate_mean": statistics.fmean(r.query_rate for r in rows),
                "regret_mean": statistics.fmean(r.regret for r in rows),
                "revision_rate": statistics.fmean(float(r.revision_active) for r in rows),
                "training_query_rate_mean": statistics.fmean(r.training_query_rate for r in rows),
                "training_accuracy_mean": statistics.fmean(r.training_accuracy for r in rows),
            }
        )
    return output


def benchmark_assertions(rows: List[dict]) -> List[dict]:
    index = {(row["scenario"], row["agent"]): row for row in rows}

    def row(scenario: str, agent: str) -> dict:
        return index[(scenario, agent)]

    checks = [
        (
            "hidden_collision_gain",
            row("hidden_collision", "interface_revision")["net_reward_mean"]
            > row("hidden_collision", "fixed_interface")["net_reward_mean"] + 0.15,
            "Revision should materially outperform fixed-interface learning when O0 is non-identifying.",
        ),
        (
            "hidden_collision_selective_activation",
            row("hidden_collision", "interface_revision")["revision_rate"] >= 0.8,
            "Revision should activate reliably in the declared collision task.",
        ),
        (
            "sufficient_interface_no_revision",
            row("sufficient_interface", "interface_revision")["revision_rate"] <= 0.2
            and row("sufficient_interface", "interface_revision")["query_rate_mean"] <= 0.05,
            "Revision should stay inactive when O0 already identifies the target.",
        ),
        (
            "useless_sensor_rejected",
            row("useless_sensor", "interface_revision")["revision_rate"] <= 0.2
            and row("useless_sensor", "interface_revision")["query_rate_mean"] <= 0.05,
            "An uninformative sensor should not acquire deployment authority.",
        ),
        (
            "expensive_sensor_rejected",
            row("expensive_sensor", "interface_revision")["revision_rate"] <= 0.2
            and row("expensive_sensor", "interface_revision")["query_rate_mean"] <= 0.05,
            "An informative but uneconomic sensor should be rejected.",
        ),
        (
            "moderate_transfer_retained",
            row("moderate_transfer_shift", "interface_revision")["net_reward_mean"]
            > row("moderate_transfer_shift", "fixed_interface")["net_reward_mean"] + 0.08,
            "The acquired interface should retain net value under preregistered moderate shift.",
        ),
        (
            "spurious_shift_exposes_limit",
            row("spurious_training_cue", "interface_revision")["net_reward_mean"] < 0.65,
            "A training-only cue should expose the v0.1 limitation: no contradiction, no pre-shift revision.",
        ),
    ]
    return [{"name": name, "passed": bool(passed), "criterion": criterion} for name, passed, criterion in checks]


def render_markdown(rows: List[dict], checks: List[dict]) -> str:
    lines = [
        "# Interface Evolution Benchmark v0.1 — Frozen Results",
        "",
        "Generated by `benchmark/interface_evolution_v0_1.py`.",
        "",
        "## Aggregate evaluation",
        "",
        "| Scenario | Agent | Accuracy | Net reward | Query rate | Regret | Revision rate |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {scenario} | {agent} | {accuracy_mean:.3f} | {net_reward_mean:.3f} | "
            "{query_rate_mean:.3f} | {regret_mean:.3f} | {revision_rate:.2f} |".format(**row)
        )
    lines.extend(["", "## Preregistered checks", ""])
    for check in checks:
        mark = "PASS" if check["passed"] else "FAIL"
        lines.append(f"- **{mark} — {check['name']}**: {check['criterion']}")
    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            "A positive result establishes only that a paid, predeclared sensor can restore a target-relevant distinction that the initial interface erased, and that selective acquisition can outperform model-only updating after cost.",
            "",
            "It does not establish autonomous sensor invention, unknown-variable discovery, open-ended ontology generation, or a theory beyond existing active sensing / feature acquisition / POMDP formalisms.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=int, default=40, help="Number of independent seeds per scenario-agent pair.")
    parser.add_argument("--output-dir", type=Path, default=Path("benchmark/results"))
    args = parser.parse_args()
    if args.seeds <= 0:
        parser.error("--seeds must be positive")

    all_metrics: List[EvalMetrics] = []
    agent_names = [FixedInterfaceAgent.name, OracleInterfaceAgent.name, InterfaceRevisionAgent.name]
    for scenario in SCENARIOS.values():
        for seed in range(args.seeds):
            for agent_name in agent_names:
                all_metrics.append(run_one(scenario, agent_name, seed))

    rows = aggregate(all_metrics)
    checks = benchmark_assertions(rows)
    output = {
        "schema_version": "0.1",
        "seeds": args.seeds,
        "scenarios": {name: asdict(scenario) for name, scenario in SCENARIOS.items()},
        "aggregate": rows,
        "checks": checks,
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "results-v0.1.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    (args.output_dir / "results-v0.1.md").write_text(render_markdown(rows, checks), encoding="utf-8")

    failed = [check for check in checks if not check["passed"]]
    print(render_markdown(rows, checks))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
