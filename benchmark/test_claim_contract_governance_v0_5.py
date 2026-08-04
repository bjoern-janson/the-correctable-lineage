from __future__ import annotations

import unittest

from benchmark.claim_contract_governance_v0_5 import (
    GovernanceLoss,
    SCENARIOS,
    aggregate,
    benchmark_assertions,
    evaluate,
    run_benchmark,
)


class ClaimContractGovernanceV05Tests(unittest.TestCase):
    def test_all_frozen_checks_pass(self) -> None:
        payload = run_benchmark(40, GovernanceLoss())
        self.assertTrue(all(check["passed"] for check in payload["checks"]))

    def test_scope_prevents_global_spillover(self) -> None:
        scenario = SCENARIOS["local_success"]
        basic = evaluate(scenario, "authority_only", 0, GovernanceLoss())
        contract = evaluate(scenario, "claim_contract", 0, GovernanceLoss())
        self.assertTrue(basic.deploy_b)
        self.assertFalse(contract.deploy_b)
        self.assertTrue(contract.deploy_a)

    def test_distribution_shift_preserves_local_validity(self) -> None:
        scenario = SCENARIOS["distribution_shift"]
        basic = evaluate(scenario, "authority_only", 0, GovernanceLoss())
        contract = evaluate(scenario, "claim_contract", 0, GovernanceLoss())
        self.assertFalse(basic.deploy_a)
        self.assertTrue(contract.deploy_a)
        self.assertFalse(contract.deploy_b)

    def test_unreachable_falsifier_is_not_operational(self) -> None:
        scenario = SCENARIOS["formally_unreachable"]
        basic = evaluate(scenario, "authority_only", 0, GovernanceLoss())
        contract = evaluate(scenario, "claim_contract", 0, GovernanceLoss())
        self.assertTrue(basic.operational_reopenable)
        self.assertFalse(contract.operational_reopenable)
        self.assertTrue(basic.deploy_a)
        self.assertFalse(contract.deploy_a)

    def test_correlated_evidence_is_collapsed_by_dependency_group(self) -> None:
        scenario = SCENARIOS["correlated_confirmation"]
        scope_only = evaluate(scenario, "scope_only", 0, GovernanceLoss())
        contract = evaluate(scenario, "claim_contract", 0, GovernanceLoss())
        self.assertTrue(scope_only.deploy_a)
        self.assertFalse(contract.deploy_a)

    def test_reopening_event_materially_contracts(self) -> None:
        scenario = SCENARIOS["genuine_reopening"]
        contract = evaluate(scenario, "claim_contract", 0, GovernanceLoss())
        self.assertTrue(contract.reopened)
        self.assertFalse(contract.deploy_a)

    def test_richer_contract_pays_overhead_when_unneeded(self) -> None:
        scenario = SCENARIOS["stable_global_truth"]
        basic = evaluate(scenario, "authority_only", 0, GovernanceLoss())
        contract = evaluate(scenario, "claim_contract", 0, GovernanceLoss())
        self.assertTrue(basic.deploy_a and basic.deploy_b)
        self.assertTrue(contract.deploy_a and contract.deploy_b)
        self.assertGreater(contract.total_loss, basic.total_loss)

    def test_aggregate_shape_is_stable(self) -> None:
        rows = aggregate(
            evaluate(scenario, agent, seed, GovernanceLoss())
            for scenario in SCENARIOS.values()
            for agent in ("authority_only", "scope_only", "claim_contract")
            for seed in range(2)
        )
        self.assertEqual(len(rows), len(SCENARIOS) * 3)
        self.assertTrue(all(check["passed"] for check in benchmark_assertions(rows)))


if __name__ == "__main__":
    unittest.main()
