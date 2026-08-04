# Claim Contract Governance Benchmark v0.5 — Negative Result Ledger

## Status

Frozen with the first exploratory implementation using 100 seeds per scenario-agent pair.

This ledger records what v0.5 fails to establish and where the integrated governance architecture can fail.

---

## 1. The benchmark is constructed around the proposed representation

The evaluator explicitly scores scope errors, reopening access, dependency awareness, unresolved-state use, and irreversible commitments.

The full contract explicitly stores those objects.

Therefore:

\[
\boxed{
\text{better performance in v0.5}
\not\Rightarrow
\text{universal superiority of the vocabulary}.
}
\]

The benchmark first establishes representational adequacy for an evaluator-authored task.

A stronger result would require transfer to independently designed environments or comparison with mature existing methods that encode similar information differently.

---

## 2. Governance loss is externally authored

The loss function is:

\[
\Lambda=\sum_k\lambda_kL_k.
\]

Every weight is supplied by the evaluator.

Changing the weights can change which policy is preferred.

For example:

- a safety-critical domain may heavily weight irreversible false deployment;
- exploratory search may heavily weight excessive skepticism;
- low-cost reversible settings may tolerate broader provisional scope;
- expensive auditing may favor simpler contracts.

No universal weighting is identified.

---

## 3. The full contract pays overhead

In the stable-global-truth control, all agents make the correct decisions.

The authority-only agent receives zero governance loss, while the full contract pays representation and processing overhead.

Thus:

\[
\boxed{
\text{richer governance state}
\not\Rightarrow
\text{free improvement}.
}
\]

A domain with low misspecification risk may rationally prefer a simpler contract.

---

## 4. Scope is supplied rather than discovered

The evaluator defines scopes \(A\) and \(B\).

The agent does not discover which environmental dimensions define transfer, whether a new case belongs inside the old scope, whether scopes should be split or merged, or which latent variable caused the shift.

v0.5 tests scope bookkeeping, not autonomous scope induction.

---

## 5. The omitted hypothesis is represented only as unresolved

The full agent can activate:

\[
H_{?}.
\]

It does not generate a substantive missing explanation.

Therefore:

\[
\text{recognizing model incompleteness}
\neq
\text{inventing the omitted model}.
\]

The benchmark prevents forced certainty but does not demonstrate explanatory expansion.

---

## 6. Dependency groups are externally labeled

The correlated-confirmation condition supplies source-group identities.

The agent does not infer that ten observations share one generator.

It therefore does not solve hidden dataset overlap, shared preprocessing dependence, common evaluator bias, latent causal dependence, or adversarially concealed common-mode failure.

v0.5 tests use of \(\Pi\), not discovery of \(\Pi\).

---

## 7. Reopening rules are externally authored

The evaluator specifies which event is a reopening signal, whether the evidence is accessible, the minimum response magnitude, and whether replacement is permitted.

The claim-contract agent does not design \(\mathcal R\) or \(\Gamma\).

A mis-specified reopening rule can ignore a real contradiction, reopen too often, trigger an excessive contraction, preserve the wrong scope, or become another self-confirming interface.

---

## 8. Ground truth and high-stakes flags are privileged

The evaluator knows which deployments are valid and which commitments are irreversible.

Real systems may not know the true target, eventual harm, reversibility, correct time horizon, or which stakeholders bear the cost.

The benchmark does not solve target legitimacy or governance-loss legitimacy.

---

## 9. Policies are hand-authored rather than learned

The agents use fixed update rules and thresholds.

They do not learn the loss function, update magnitude, scope map, dependency map, reopening response, or cost of complexity.

The result concerns state representation plus authored policy, not autonomous governance learning.

---

## 10. Equivalent existing formalisms may absorb the result

The benchmark is compatible with hierarchical Bayesian models, distributionally robust decision theory, causal graphical models, selective prediction and abstention, model criticism, provenance-aware evidence aggregation, safety cases, and typed claims with validity domains.

If those formalisms reproduce all behavior without loss, the new vocabulary should be treated as synthesis rather than a separate theory.

---

## 11. The strongest positive result is partly tautological

An authority-only state cannot represent scope, dependency, or reopening structure.

A task that requires those distinctions will favor the richer state.

The important next question is:

\[
\boxed{
\text{Do real or independently designed systems exhibit costly failures that this integrated contract prevents better than existing practice?}
}
\]

---

## Frozen conclusion

v0.5 can support only:

\[
\boxed{
\text{Under one declared governance loss, explicit claim contracts avoid several representationally unavailable baseline errors while incurring overhead.}
}
\]

Its strongest negative result is:

\[
\boxed{
\text{The benchmark rewards the distinctions it was designed to encode; transfer and comparative advantage remain unestablished.}
}
