from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("interface_diversity_v0_3.py")
SPEC = importlib.util.spec_from_file_location("interface_diversity_v0_3", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class InterfaceDiversityV03Tests(unittest.TestCase):
    def calibration(self, scenario_name: str, seed: int = 0):
        scenario = MODULE.SCENARIOS[scenario_name]
        task = MODULE.CorrectionPathTask(scenario, seed)
        return scenario, MODULE.sample_phase(
            task, "calibration", scenario.calibration_episodes
        )

    def test_shared_blind_spot_selects_independent_channel(self):
        scenario, calibration = self.calibration("shared_blind_spot_shift")
        self.assertEqual(
            MODULE.select_independence_aware(scenario, calibration),
            "independent",
        )

    def test_raw_accuracy_prefers_redundant_channel(self):
        scenario, calibration = self.calibration("shared_blind_spot_shift")
        selected = MODULE.select_raw_accuracy(scenario, calibration)
        self.assertTrue(selected.startswith("redundant_"))

    def test_costly_channels_are_rejected(self):
        scenario, calibration = self.calibration("all_costly")
        self.assertEqual(
            MODULE.select_independence_aware(scenario, calibration),
            "primary",
        )

    def test_no_exposed_failures_blocks_independence_estimation(self):
        scenario, calibration = self.calibration(
            "no_exposed_primary_failures"
        )
        self.assertEqual(MODULE.primary_failure_count(calibration), 0)
        self.assertEqual(
            MODULE.select_independence_aware(scenario, calibration),
            "primary",
        )

    def test_frozen_checks_pass_on_small_replay(self):
        metrics = []
        for scenario in MODULE.SCENARIOS.values():
            for seed in range(10):
                metrics.extend(MODULE.run_seed(scenario, seed))
        rows = MODULE.aggregate(metrics)
        checks = MODULE.benchmark_assertions(rows)
        self.assertTrue(all(check["passed"] for check in checks), checks)


if __name__ == "__main__":
    unittest.main()
