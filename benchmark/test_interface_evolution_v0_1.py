from __future__ import annotations

import unittest

from interface_evolution_v0_1 import (
    SCENARIOS,
    FixedInterfaceAgent,
    InterfaceRevisionAgent,
    aggregate,
    benchmark_assertions,
    run_one,
)


class InterfaceEvolutionBenchmarkTests(unittest.TestCase):
    def test_declared_collision_is_unsolved_by_fixed_interface(self) -> None:
        rows = [run_one(SCENARIOS["hidden_collision"], FixedInterfaceAgent.name, seed) for seed in range(12)]
        summary = aggregate(rows)[0]
        self.assertLess(summary["accuracy_mean"], 0.57)

    def test_revision_agent_selects_useful_sensor(self) -> None:
        rows = [run_one(SCENARIOS["hidden_collision"], InterfaceRevisionAgent.name, seed) for seed in range(12)]
        summary = aggregate(rows)[0]
        self.assertGreater(summary["net_reward_mean"], 0.72)
        self.assertGreater(summary["revision_rate"], 0.8)

    def test_revision_agent_rejects_sufficient_interface(self) -> None:
        rows = [run_one(SCENARIOS["sufficient_interface"], InterfaceRevisionAgent.name, seed) for seed in range(12)]
        summary = aggregate(rows)[0]
        self.assertLess(summary["query_rate_mean"], 0.05)
        self.assertLess(summary["revision_rate"], 0.2)

    def test_preregistered_suite(self) -> None:
        metrics = []
        for scenario in SCENARIOS.values():
            for seed in range(20):
                for agent in ("fixed_interface", "oracle_interface", "interface_revision"):
                    metrics.append(run_one(scenario, agent, seed))
        checks = benchmark_assertions(aggregate(metrics))
        failures = [check for check in checks if not check["passed"]]
        self.assertEqual([], failures)


if __name__ == "__main__":
    unittest.main()
