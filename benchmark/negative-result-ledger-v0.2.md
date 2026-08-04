# Interface Stress Benchmark v0.2 — Negative Result Ledger

## Status

Frozen with the first exploratory implementation: 200 seeds per scenario-agent pair.

This ledger records what v0.2 fails to establish and where adaptive skepticism itself fails.

---

## 1. The challenge operator is externally authored

The evaluator supplies:

- the possibility of hidden fragility;
- the prior probability of fragility;
- the challenge action;
- the challenge cost;
- the candidate sensor;
- the target and reward;
- the deployment horizon.

The agent does not invent a test.

It performs value-of-information allocation over a declared experiment.

---

## 2. Uninformative challenge

### Condition

The audit preserves the training correlation between cue and latent state.

### Result

The adaptive skeptic pays for the audit, observes continued success, rejects the sensor, and misses fragile worlds.

Aggregate diagnosis accuracy falls to approximately the robust-world frequency rather than identifying fragility.

### Interpretation

\[
\boxed{
\text{A system cannot escape a blind interface through a challenge that preserves the same blind spot.}
}
\]

v0.2 does not evaluate or generate the challenge interface itself.

---

## 3. Adaptive skepticism depends on an external prior

Rare fragility is rationally ignored under the declared expected-reward objective when audit cost exceeds expected benefit.

This can still produce catastrophic misses in the realized rare fragile world.

Therefore:

\[
\text{expected-value optimal}
\neq
\text{tail-risk safe}.
\]

v0.2 does not solve prior construction, ambiguity aversion, minimax regret, or catastrophic-risk governance.

---

## 4. Scalar reward governs doubt

The audit decision uses one known horizon and one scalar reward.

It does not model:

- irreversible harm;
- heterogeneous stakeholders;
- asymmetric false-negative cost;
- unknown horizons;
- nonstationary sensor costs;
- institutional or coordination consequences of challenging the interface.

A richer objective could reverse the audit decision.

---

## 5. Diagnosis is binary and supplied

The agent chooses between only two hypotheses:

- cue is structurally sufficient;
- cue is a training-only proxy for a latent target.

Real interface failures may involve:

- multiple hidden variables;
- target misspecification;
- intervention-dependent semantics;
- non-identifiable mixtures;
- shared assumptions across every available sensor.

v0.2 does not generate competing causal explanations.

---

## 6. Formal redundancy remains

The complete benchmark is compatible with:

- Bayesian value of information;
- active testing;
- costly feature acquisition;
- experimental design;
- POMDP and robust-decision formulations.

No distinct general theory of interface evolution is established.

---

## 7. The hardest failure moves one level outward

v0.1 failed when no contradiction appeared.

v0.2 can manufacture contradiction through a supplied stress test.

But it fails when the supplied stress test shares the original interface's blind spot.

The frontier is therefore:

\[
\boxed{
\text{not merely challenge the model, but challenge the challenge interface.}
}
\]

That frontier remains unimplemented.

---

## Frozen conclusion

v0.2 supports only:

\[
\boxed{
\text{cost-sensitive interface challenge can expose hidden fragility when a valid challenge operator is already available.}
}
\]

Its strongest negative result is:

\[
\boxed{
\text{A blind challenge cannot reveal a blind interface.}
}
