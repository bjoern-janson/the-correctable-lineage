# Interface Diversity Benchmark v0.3 — Negative Result Ledger

## Status

Frozen with the first exploratory implementation using 100 seeds per scenario-agent pair.

This ledger records where correction-path diversity fails, remains externally authored, or is reducible to existing formalisms.

---

## 1. No exposed primary failure

### Condition

Calibration contains no primary error.

Evaluation later introduces a shared blind spot.

### Result

The independence-aware selector retains the primary interface because:

\[
P(C_i=Y\mid P\neq Y)
\]

cannot be estimated when the conditioning event is absent.

It then loses to the oracle after shift.

### Interpretation

\[
\boxed{
\text{Failure-mode independence is not identifiable from success-only data.}
}
\]

A stress intervention or prior structural knowledge is still required.

---

## 2. Independence is externally oriented

The benchmark supplies a stress weight:

\[
\lambda.
\]

This parameter determines how much authority to grant ordinary marginal accuracy versus correction coverage on primary failures.

The agent does not infer:

- future shift probability;
- catastrophic-tail importance;
- stakeholder-specific loss;
- ambiguity about the deployment regime.

Therefore v0.3 does not solve skepticism allocation under unknown risk.

---

## 3. Labeled calibration is privileged

The evaluator reveals the target during calibration.

This allows direct estimation of:

- primary failures;
- channel correction coverage;
- error agreement.

Real systems may not receive target labels for the cases that matter.

The benchmark does not solve unlabeled independence estimation.

---

## 4. Candidate channels are externally authored

The agent chooses only among supplied correction paths.

It does not generate:

- a new instrument;
- a new experiment;
- a new decomposition;
- a new reference frame;
- a new adversarial test.

Therefore v0.3 remains below interface invention.

---

## 5. Correlation is not causation

Low observed error agreement does not prove independent causal access.

Two channels can appear statistically independent while sharing:

- one hidden preprocessing pipeline;
- one training corpus;
- one evaluator;
- one unobserved failure mechanism.

The benchmark contains known generative structure, so this ambiguity is suppressed.

It does not establish a universal measure of epistemic independence.

---

## 6. Diversity can be uneconomic

In the all-costly control, the independence-aware selector retains the primary interface.

This is intentional.

\[
\text{independence}
\not\Rightarrow
\text{positive operational value}.
\]

A correction path must repay its cost under the declared objective.

---

## 7. Test quantity can amplify one failure mode

In the redundant-quantity condition, five correlated channels dominate a majority vote while one independent channel provides the best correction.

The result supports:

\[
\boxed{
\text{correlated test count does not create independent evidence.}
}
\]

But this is already compatible with ensemble learning under correlated errors.

---

## 8. Formal redundancy remains

The full implementation is describable through:

- robust ensemble selection;
- conditional risk;
- classifier error correlation;
- mixture shift;
- decision theory under correlated observations.

The benchmark does not establish a distinct general theory of epistemic topology.

The interface vocabulary earns separate authority only if later work creates discriminations not already represented by those formalisms.

---

## 9. Recursive frontier remains open

v0.3 selects among supplied correction channels using supplied labels.

It does not determine whether the calibration process that measured channel independence shares a deeper blind spot.

The frontier therefore remains:

\[
\boxed{
\text{Can a system obtain evidence that its entire correction-path comparison is jointly mis-specified?}
}
\]

---

## Frozen conclusion

v0.3 supports only:

\[
\boxed{
\text{failure-conditioned correction coverage can outperform marginal accuracy and correlated vote count under a declared shared-blind-spot shift.}
}
\]

Its strongest negative result is:

\[
\boxed{
\text{No exposed failure or independent intervention}
\Rightarrow
\text{no identified correction-path independence.}
}
