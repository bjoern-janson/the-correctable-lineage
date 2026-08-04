from __future__ import annotations

import argparse, json, random, statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


@dataclass(frozen=True)
class GovernanceLoss:
    overgeneralization: float = 3.0
    undergeneralization: float = 2.0
    premature_certainty: float = 2.5
    excessive_skepticism: float = 1.0
    irreversible_commitment: float = 5.0
    unnecessary_reopening: float = 1.0
    complexity: float = 0.05

    def validate(self) -> None:
        if any(value < 0 for value in asdict(self).values()):
            raise ValueError("governance-loss weights must be non-negative")


@dataclass(frozen=True)
class Evidence:
    scope: str
    direction: int
    strength: float
    source_group: str
    reopening_signal: bool = False
    accessible: bool = True
    unresolved_pattern: bool = False

    def validate(self) -> None:
        if self.scope not in {"A", "B"} or self.direction not in {-1, 1}:
            raise ValueError("invalid evidence")
        if not 0 <= self.strength <= 2:
            raise ValueError("strength must be in [0,2]")


@dataclass(frozen=True)
class Scenario:
    name: str
    truth_a: bool
    truth_b: bool
    high_stakes_a: bool = False
    high_stakes_b: bool = False
    description: str = ""


SCENARIOS: Dict[str, Scenario] = {
    "local_success": Scenario("local_success", True, False, description="Local success should not globalize."),
    "distribution_shift": Scenario("distribution_shift", True, False, description="Shift failure should rescope, not erase local validity."),
    "omitted_hypothesis": Scenario("omitted_hypothesis", False, False, True, description="Residuals should permit unresolved status."),
    "formally_unreachable": Scenario("formally_unreachable", False, False, True, description="Formal falsifiability is not operational access."),
    "correlated_confirmation": Scenario("correlated_confirmation", False, False, True, description="One generator repeated is one correction path."),
    "genuine_reopening": Scenario("genuine_reopening", False, False, True, description="A reachable reopening event should materially contract."),
    "stable_global_truth": Scenario("stable_global_truth", True, True, description="Richer contracts should pay overhead when unnecessary."),
}


@dataclass(frozen=True)
class Metrics:
    scenario: str
    agent: str
    seed: int
    total_loss: float
    deploy_a: bool
    deploy_b: bool
    unresolved: bool
    operational_reopenable: bool
    reopened: bool
    overgeneralization: float
    undergeneralization: float
    premature_certainty: float
    excessive_skepticism: float
    irreversible_commitment: float
    unnecessary_reopening: float
    complexity_loss: float
    valid_retention: float


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


class AuthorityOnlyAgent:
    def __init__(self) -> None:
        self.authority, self.formal_reopenable = 0.5, False
        self.reopened, self.unresolved = False, False

    def set_reopenability(self, *, formal: bool, accessible: bool, gamma: float = .6, replaceable: bool = True) -> None:
        del accessible, gamma, replaceable
        self.formal_reopenable = formal

    def ingest(self, evidence: Iterable[Evidence]) -> None:
        for item in evidence:
            item.validate()
            self.authority = clamp(self.authority + .12 * item.direction * item.strength)
            self.reopened |= item.reopening_signal and item.accessible

    def deploy(self, scope: str, *, high_stakes: bool) -> bool:
        del scope, high_stakes
        return self.authority >= .70

    def is_operationally_reopenable(self) -> bool:
        return self.formal_reopenable

    @property
    def complexity_operations(self) -> int:
        return 0


class ScopeOnlyAgent:
    def __init__(self) -> None:
        self.authority = {"A": .5, "B": .5}
        self.formal_reopenable, self.reopened, self.unresolved = False, False, False

    def set_reopenability(self, *, formal: bool, accessible: bool, gamma: float = .6, replaceable: bool = True) -> None:
        del accessible, gamma, replaceable
        self.formal_reopenable = formal

    def ingest(self, evidence: Iterable[Evidence]) -> None:
        for item in evidence:
            item.validate()
            self.authority[item.scope] = clamp(self.authority[item.scope] + .12 * item.direction * item.strength)
            self.reopened |= item.reopening_signal and item.accessible

    def deploy(self, scope: str, *, high_stakes: bool) -> bool:
        del high_stakes
        return self.authority[scope] >= .70

    def is_operationally_reopenable(self) -> bool:
        return self.formal_reopenable

    @property
    def complexity_operations(self) -> int:
        return 2


class ClaimContractAgent:
    def __init__(self) -> None:
        self.authority = {"A": .5, "B": .5}
        self.operational_reopenable, self.unresolved = False, False
        self.reopened_scopes: set[str] = set()
        self._ops = 0

    def set_reopenability(self, *, formal: bool, accessible: bool, gamma: float = .6, replaceable: bool = True) -> None:
        self.operational_reopenable = formal and accessible and gamma >= .20 and replaceable
        self._ops += 1

    def ingest(self, evidence: Iterable[Evidence]) -> None:
        grouped: Dict[Tuple[str, str, int], float] = {}
        for item in evidence:
            item.validate()
            key = (item.scope, item.source_group, item.direction)
            grouped[key] = max(grouped.get(key, 0.0), item.strength)
            self.unresolved |= item.unresolved_pattern
            if item.reopening_signal and item.accessible:
                self.authority[item.scope] = min(self.authority[item.scope], .20)
                self.reopened_scopes.add(item.scope)
        for (scope, _group, direction), strength in grouped.items():
            self.authority[scope] = clamp(self.authority[scope] + .12 * direction * strength)
        self._ops += len(grouped)

    def deploy(self, scope: str, *, high_stakes: bool) -> bool:
        if high_stakes and (self.unresolved or not self.operational_reopenable):
            return False
        return self.authority[scope] >= .70

    def is_operationally_reopenable(self) -> bool:
        return self.operational_reopenable

    @property
    def reopened(self) -> bool:
        return bool(self.reopened_scopes)

    @property
    def complexity_operations(self) -> int:
        return self._ops


AGENTS = ("authority_only", "scope_only", "claim_contract")


def repeated(scope: str, direction: int, count: int, group: str, strength: float, *, same_group: bool = False) -> List[Evidence]:
    return [Evidence(scope, direction, strength, group if same_group else f"{group}_{i}") for i in range(count)]


def make_agent(name: str):
    return {"authority_only": AuthorityOnlyAgent, "scope_only": ScopeOnlyAgent, "claim_contract": ClaimContractAgent}[name]()


def configure(scenario: Scenario, agent, rng: random.Random) -> None:
    jitter = rng.uniform(-.05, .05)
    if scenario.name == "local_success":
        agent.set_reopenability(formal=True, accessible=True)
        agent.ingest(repeated("A", 1, 5, "local", 1 + jitter))
    elif scenario.name == "distribution_shift":
        agent.set_reopenability(formal=True, accessible=True)
        agent.ingest(repeated("A", 1, 5, "train", 1 + jitter) + repeated("B", -1, 6, "shift", 1 + jitter))
    elif scenario.name == "omitted_hypothesis":
        agent.set_reopenability(formal=True, accessible=True)
        agent.ingest(repeated("A", 1, 4, "ambiguous", .8 + jitter) + [Evidence("A", -1, 1, "residual", unresolved_pattern=True)])
        if not isinstance(agent, ClaimContractAgent):
            agent.unresolved = False
    elif scenario.name == "formally_unreachable":
        agent.set_reopenability(formal=True, accessible=False)
        agent.ingest(repeated("A", 1, 5, "support", 1 + jitter))
    elif scenario.name == "correlated_confirmation":
        agent.set_reopenability(formal=True, accessible=True)
        agent.ingest(repeated("A", 1, 10, "shared", 1 + jitter, same_group=True) + repeated("A", -1, 2, "independent", 1 + jitter))
    elif scenario.name == "genuine_reopening":
        agent.set_reopenability(formal=True, accessible=True, gamma=.8, replaceable=True)
        agent.ingest(repeated("A", 1, 6, "prior", 1 + jitter))
        agent.ingest([Evidence("A", -1, 1, "reopen", reopening_signal=True)])
    elif scenario.name == "stable_global_truth":
        agent.set_reopenability(formal=True, accessible=True)
        agent.ingest(repeated("A", 1, 3, "a", 1 + jitter) + repeated("B", 1, 3, "b", 1 + jitter))
    else:
        raise KeyError(scenario.name)


def evaluate(scenario: Scenario, agent_name: str, seed: int, loss: GovernanceLoss) -> Metrics:
    loss.validate()
    agent, rng = make_agent(agent_name), random.Random(seed)
    configure(scenario, agent, rng)
    truth = {"A": scenario.truth_a, "B": scenario.truth_b}
    high = {"A": scenario.high_stakes_a, "B": scenario.high_stakes_b}
    deploy = {scope: agent.deploy(scope, high_stakes=high[scope]) for scope in ("A", "B")}
    over = float(sum(deploy[s] and not truth[s] for s in ("A", "B")))
    under = float(sum(not deploy[s] and truth[s] for s in ("A", "B")))
    premature = float(sum(deploy[s] and not truth[s] and scenario.name in {"omitted_hypothesis", "formally_unreachable"} for s in ("A", "B")))
    irreversible = float(sum(deploy[s] and not truth[s] and high[s] for s in ("A", "B")))
    reopened = bool(agent.reopened)
    unnecessary = float(reopened and scenario.name != "genuine_reopening")
    complexity = 0.0 if agent_name == "authority_only" else (.01 if agent_name == "scope_only" else loss.complexity * agent.complexity_operations / 10)
    total = loss.overgeneralization * over + loss.undergeneralization * under + loss.premature_certainty * premature + loss.excessive_skepticism * under + loss.irreversible_commitment * irreversible + loss.unnecessary_reopening * unnecessary + complexity
    return Metrics(scenario.name, agent_name, seed, total, deploy["A"], deploy["B"], bool(agent.unresolved), agent.is_operationally_reopenable(), reopened, over, under, premature, under, irreversible, unnecessary, complexity, float(sum(deploy[s] and truth[s] for s in ("A", "B"))))


def aggregate(metrics: Iterable[Metrics]) -> List[dict]:
    grouped: Dict[Tuple[str, str], List[Metrics]] = {}
    for metric in metrics:
        grouped.setdefault((metric.scenario, metric.agent), []).append(metric)
    rows = []
    for (scenario, agent), group in sorted(grouped.items()):
        mean = lambda field: statistics.fmean(float(getattr(item, field)) for item in group)
        rows.append({"scenario": scenario, "agent": agent, "n_seeds": len(group), "total_loss_mean": mean("total_loss"), "total_loss_sd": statistics.pstdev(item.total_loss for item in group), "deploy_a_rate": mean("deploy_a"), "deploy_b_rate": mean("deploy_b"), "unresolved_rate": mean("unresolved"), "operational_reopenable_rate": mean("operational_reopenable"), "reopened_rate": mean("reopened"), "overgeneralization_mean": mean("overgeneralization"), "undergeneralization_mean": mean("undergeneralization"), "irreversible_commitment_mean": mean("irreversible_commitment"), "valid_retention_mean": mean("valid_retention"), "complexity_loss_mean": mean("complexity_loss")})
    return rows


def benchmark_assertions(rows: List[dict]) -> List[dict]:
    index = {(row["scenario"], row["agent"]): row for row in rows}
    get = lambda scenario, agent: index[(scenario, agent)]
    checks = [
        ("scope_prevents_local_to_global_spillover", get("local_success", "claim_contract")["total_loss_mean"] < get("local_success", "authority_only")["total_loss_mean"] - 2, "A scoped contract should retain local success without deploying in untested scope B."),
        ("rescoping_preserves_local_validity", get("distribution_shift", "claim_contract")["valid_retention_mean"] > get("distribution_shift", "authority_only")["valid_retention_mean"] + .9, "Shift failure should narrow scope rather than erase valid structure in A."),
        ("unresolved_state_blocks_forced_certainty", get("omitted_hypothesis", "claim_contract")["unresolved_rate"] == 1 and get("omitted_hypothesis", "claim_contract")["irreversible_commitment_mean"] == 0, "An omitted-model residual should enter a holding state."),
        ("operational_reopenability_differs_from_formal", get("formally_unreachable", "claim_contract")["operational_reopenable_rate"] == 0 and get("formally_unreachable", "claim_contract")["irreversible_commitment_mean"] == 0 and get("formally_unreachable", "authority_only")["irreversible_commitment_mean"] == 1, "An unreachable falsifier should not authorize irreversible deployment."),
        ("dependency_map_discounts_correlated_confirmation", get("correlated_confirmation", "claim_contract")["total_loss_mean"] < get("correlated_confirmation", "scope_only")["total_loss_mean"] - 5, "One shared generator should not count as many independent confirmations."),
        ("reachable_reopening_triggers_material_contraction", get("genuine_reopening", "claim_contract")["reopened_rate"] == 1 and get("genuine_reopening", "claim_contract")["irreversible_commitment_mean"] == 0, "A reachable reopening event should materially contract before high-stakes deployment."),
        ("richer_contract_has_nonzero_overhead", get("stable_global_truth", "claim_contract")["total_loss_mean"] > get("stable_global_truth", "authority_only")["total_loss_mean"], "The richer representation should pay overhead when unnecessary."),
    ]
    return [{"name": name, "passed": bool(passed), "description": description} for name, passed, description in checks]


def render_markdown(payload: dict) -> str:
    lines = ["# Claim Contract Governance Benchmark v0.5 — Frozen Exploratory Results", "", f"Generated using {payload['seeds']} seeds per scenario-agent pair.", "", "## Declared governance loss", "", "```json", json.dumps(payload["loss"], indent=2, sort_keys=True), "```", "", "## Aggregate evaluation", "", "| Scenario | Agent | Governance loss | Deploy A | Deploy B | Unresolved | Operationally reopenable | Reopened | Valid retention |", "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for row in payload["aggregate"]:
        lines.append("| {scenario} | {agent} | {total_loss_mean:.3f} | {deploy_a_rate:.2f} | {deploy_b_rate:.2f} | {unresolved_rate:.2f} | {operational_reopenable_rate:.2f} | {reopened_rate:.2f} | {valid_retention_mean:.2f} |".format(**row))
    lines += ["", "## Frozen checks", ""]
    for check in payload["checks"]:
        lines.append(f"- **{'PASS' if check['passed'] else 'FAIL'} — {check['name']}**: {check['description']}")
    lines += ["", "## Interpretation boundary", "", "v0.5 is constructed to reward explicit scope, dependency, unresolved-state, and reopening records. A positive result therefore does not show that this vocabulary is universally necessary or superior.", "", "The policies, evidence sequences, loss weights, scopes, high-stakes flags, reopening trigger, and ground-truth evaluation are externally authored.", "", "The result can support only a local claim: under this declared governance loss, the richer claim contract avoids several errors that an authority-only state cannot represent, while paying measurable overhead when those fields are unnecessary.", "", "It does not establish a universal loss function, autonomous hypothesis expansion, autonomous scope discovery, autonomous reopening design, or superiority over well-specified existing Bayesian, causal, or decision-theoretic systems that already encode equivalent state.", ""]
    return "\n".join(lines)


def run_benchmark(seeds: int, loss: GovernanceLoss) -> dict:
    if seeds <= 0:
        raise ValueError("seeds must be positive")
    metrics = [evaluate(scenario, agent, seed, loss) for scenario in SCENARIOS.values() for agent in AGENTS for seed in range(seeds)]
    rows = aggregate(metrics)
    return {"benchmark": "claim-contract-governance-v0.5", "status": "frozen exploratory first implementation", "seeds": seeds, "loss": asdict(loss), "scenarios": {name: asdict(scenario) for name, scenario in SCENARIOS.items()}, "agents": list(AGENTS), "aggregate": rows, "checks": benchmark_assertions(rows)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=100)
    parser.add_argument("--output-json", type=Path)
    parser.add_argument("--output-md", type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    payload = run_benchmark(args.seeds, GovernanceLoss())
    markdown = render_markdown(payload)
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.output_md:
        args.output_md.parent.mkdir(parents=True, exist_ok=True)
        args.output_md.write_text(markdown + "\n", encoding="utf-8")
    print(markdown)
    if args.strict and not all(check["passed"] for check in payload["checks"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
