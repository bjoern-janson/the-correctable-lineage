from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).with_name("correction_ecosystem_v0_4.py")
SPEC = importlib.util.spec_from_file_location("correction_ecosystem_v0_4", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class CorrectionEcosystemV04Tests(unittest.TestCase):
    def aggregate(self, seeds: int = 20) -> list[dict]:
        metrics = []
        for scenario in MODULE.SCENARIOS.values():
            for agent in MODULE.AGENTS:
                for seed in range(seeds):
                    metrics.append(MODULE.run_one(scenario, agent, seed))
        return MODULE.aggregate(metrics)

    def test_frozen_checks_pass(self) -> None:
        checks = MODULE.benchmark_assertions(self.aggregate())
        self.assertTrue(all(check["passed"] for check in checks), checks)

    def test_valid_intervention_selects_independent_path(self) -> None:
        scenario = MODULE.SCENARIOS["hidden_shared_dependency"]
        for seed in range(10):
            result = MODULE.run_one(scenario, "intervention_selector", seed)
            self.assertTrue(result.audited)
            self.assertEqual(result.selected_path, "independent")

    def test_blind_intervention_does_not_find_independent_path(self) -> None:
        scenario = MODULE.SCENARIOS["blind_intervention"]
        selected = {
            MODULE.run_one(scenario, "intervention_selector", seed).selected_path
            for seed in range(20)
        }
        self.assertNotIn("independent", selected)

    def test_no_independent_path_reports_compromise(self) -> None:
        scenario = MODULE.SCENARIOS["no_independent_path"]
        detections = [
            MODULE.run_one(scenario, "intervention_selector", seed)
            for seed in range(20)
        ]
        self.assertGreaterEqual(
            sum(result.compromise_detected for result in detections),
            18,
        )
        self.assertTrue(
            all(result.selected_path == "primary" for result in detections)
        )

    def test_costly_audit_is_rejected(self) -> None:
        scenario = MODULE.SCENARIOS["costly_audit"]
        self.assertFalse(MODULE.should_audit(scenario))

    def test_unlabeled_audit_is_rejected(self) -> None:
        scenario = MODULE.SCENARIOS["unlabeled_audit"]
        self.assertFalse(MODULE.should_audit(scenario))


if __name__ == "__main__":
    unittest.main()
