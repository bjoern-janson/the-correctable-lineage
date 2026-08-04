from __future__ import annotations

import unittest

from interface_stress_v0_2 import (
    SCENARIOS,
    adaptive_should_audit,
    benchmark_assertions,
    run_benchmark,
    run_one,
)


class InterfaceStressV02Tests(unittest.TestCase):
    def test_adaptive_audit_decisions(self) -> None:
        self.assertTrue(adaptive_should_audit(SCENARIOS["balanced_affordable"]))
        self.assertTrue(adaptive_should_audit(SCENARIOS["uninformative_challenge"]))
        self.assertFalse(adaptive_should_audit(SCENARIOS["rare_fragility"]))
        self.assertFalse(adaptive_should_audit(SCENARIOS["expensive_audit"]))
        self.assertFalse(adaptive_should_audit(SCENARIOS["short_horizon"]))

    def test_robust_world_does_not_acquire_sensor_after_valid_audit(self) -> None:
        scenario = SCENARIOS["balanced_affordable"]
        result = run_one(scenario, "adaptive_skeptic", seed=0)
        self.assertEqual(result.world, "robust")
        self.assertTrue(result.audited)
        self.assertFalse(result.sensor_active)
        self.assertTrue(result.diagnosis_correct)

    def test_fragile_world_acquires_sensor_after_valid_audit(self) -> None:
        scenario = SCENARIOS["balanced_affordable"]
        result = run_one(scenario, "adaptive_skeptic", seed=1)
        self.assertEqual(result.world, "fragile")
        self.assertTrue(result.audited)
        self.assertTrue(result.sensor_active)
        self.assertTrue(result.diagnosis_correct)

    def test_uninformative_challenge_misses_fragile_world(self) -> None:
        scenario = SCENARIOS["uninformative_challenge"]
        result = run_one(scenario, "adaptive_skeptic", seed=1)
        self.assertEqual(result.world, "fragile")
        self.assertTrue(result.audited)
        self.assertFalse(result.sensor_active)
        self.assertFalse(result.diagnosis_correct)

    def test_frozen_checks_pass(self) -> None:
        _, rows, checks = run_benchmark(seeds=40)
        self.assertEqual(checks, benchmark_assertions(rows))
        self.assertTrue(all(check["passed"] for check in checks))


if __name__ == "__main__":
    unittest.main()
