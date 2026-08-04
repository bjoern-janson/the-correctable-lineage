# Claim Contract Governance Benchmark v0.5 — Frozen Exploratory Results

Generated using 100 seeds per scenario-agent pair.

## Declared governance loss

```json
{
  "complexity": 0.05,
  "excessive_skepticism": 1.0,
  "irreversible_commitment": 5.0,
  "overgeneralization": 3.0,
  "premature_certainty": 2.5,
  "undergeneralization": 2.0,
  "unnecessary_reopening": 1.0
}
```

## Aggregate evaluation

| Scenario | Agent | Governance loss | Deploy A | Deploy B | Unresolved | Operationally reopenable | Reopened | Valid retention |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| correlated_confirmation | authority_only | 11.000 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| correlated_confirmation | claim_contract | 0.020 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| correlated_confirmation | scope_only | 8.010 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| distribution_shift | authority_only | 3.000 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| distribution_shift | claim_contract | 0.060 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 1.00 |
| distribution_shift | scope_only | 0.010 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 1.00 |
| formally_unreachable | authority_only | 16.000 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| formally_unreachable | claim_contract | 0.030 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| formally_unreachable | scope_only | 10.510 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| genuine_reopening | authority_only | 11.000 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 | 0.00 |
| genuine_reopening | claim_contract | 0.040 | 0.00 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 |
| genuine_reopening | scope_only | 8.010 | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 |
| local_success | authority_only | 3.000 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 1.00 |
| local_success | claim_contract | 0.030 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 1.00 |
| local_success | scope_only | 0.010 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 1.00 |
| omitted_hypothesis | authority_only | 16.000 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| omitted_hypothesis | claim_contract | 0.030 | 0.00 | 0.00 | 1.00 | 1.00 | 0.00 | 0.00 |
| omitted_hypothesis | scope_only | 10.510 | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| stable_global_truth | authority_only | 0.000 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 2.00 |
| stable_global_truth | claim_contract | 0.035 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 2.00 |
| stable_global_truth | scope_only | 0.010 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 2.00 |

## Frozen checks

- **PASS — scope_prevents_local_to_global_spillover**: A scoped contract should retain local success without deploying in untested scope B.
- **PASS — rescoping_preserves_local_validity**: Shift failure should narrow scope rather than erase valid structure in A.
- **PASS — unresolved_state_blocks_forced_certainty**: An omitted-model residual should enter a holding state.
- **PASS — operational_reopenability_differs_from_formal**: An unreachable falsifier should not authorize irreversible deployment.
- **PASS — dependency_map_discounts_correlated_confirmation**: One shared generator should not count as many independent confirmations.
- **PASS — reachable_reopening_triggers_material_contraction**: A reachable reopening event should materially contract before high-stakes deployment.
- **PASS — richer_contract_has_nonzero_overhead**: The richer representation should pay overhead when unnecessary.

## Interpretation boundary

v0.5 is constructed to reward explicit scope, dependency, unresolved-state, and reopening records. A positive result therefore does not show that this vocabulary is universally necessary or superior.

The policies, evidence sequences, loss weights, scopes, high-stakes flags, reopening trigger, and ground-truth evaluation are externally authored.

The result can support only a local claim: under this declared governance loss, the richer claim contract avoids several errors that an authority-only state cannot represent, while paying measurable overhead when those fields are unnecessary.

It does not establish a universal loss function, autonomous hypothesis expansion, autonomous scope discovery, autonomous reopening design, or superiority over well-specified existing Bayesian, causal, or decision-theoretic systems that already encode equivalent state.
