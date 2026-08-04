# Governance Loss Contract

## Status

This document makes explicit the objective implicitly optimized by evidential-update governance.

It is a methodological contract, not a universal rationality function or a validated scalar of epistemic quality.

---

## 1. Why a loss object is necessary

An update policy cannot be judged without specifying which mistakes matter and how much.

A policy that minimizes false deployment may increase missed opportunity.

A policy that maximizes exploration may accept broader provisional scope.

A policy suitable for reversible toy decisions may be unacceptable for irreversible medical, engineering, or institutional commitments.

Therefore the update kernel should include a declared governance loss:

\[
\boxed{
\Lambda:
(\text{claim state},\text{update},\text{action},\text{outcome})
\rightarrow
\mathbb R_{\geq0}.
}
\]

The update operator is evaluated relative to that loss:

\[
\boxed{
U_{\Lambda}
\in
\arg\min_U
\mathbb E[\Lambda\mid O,\Phi,F,\mathcal H,T,\Pi].
}
\]

This expression is aspirational in the general framework. The current toy benchmarks use hand-authored policies and evaluator-supplied loss weights rather than solving a universal optimization problem.

---

## 2. Expanded kernel

The evidential pipeline becomes:

\[
(O,\Phi)
\rightarrow
F
\rightarrow
(\mathcal H,T,\Pi)
\rightarrow
U_{\Lambda}
\rightarrow
(W,\Sigma,\mathcal R,\Gamma).
\]

The loss contract answers:

> Which update errors is this system trying hardest to avoid, under which stakes, reversibility, time horizon, and stakeholder distribution?

---

## 3. Candidate loss components

A domain-specific loss may include:

### Overgeneralization

\[
L_{\mathrm{over}}
=
\text{authority or deployment outside the demonstrated scope}.
\]

### Undergeneralization

\[
L_{\mathrm{under}}
=
\text{failure to preserve or transfer a valid result when justified}.
\]

### Premature certainty

\[
L_{\mathrm{premature}}
=
\text{forced commitment under incomplete hypotheses or unresolved attribution}.
\]

### Excessive skepticism

\[
L_{\mathrm{skepticism}}
=
\text{avoidable delay, abstention, or reopening despite adequate evidence}.
\]

### Invalid irreversible commitment

\[
L_{\mathrm{irreversible}}
=
\text{high-cost action taken before sufficient correction access exists}.
\]

### Unnecessary reopening

\[
L_{\mathrm{reopening}}
=
\text{revalidation cost triggered without sufficient independent corrective value}.
\]

### Governance complexity

\[
L_{\mathrm{complexity}}
=
\text{storage, computation, coordination, audit, and latency cost of the claim contract}.
\]

A simple local form is:

\[
\Lambda
=
\sum_k\lambda_kL_k.
\]

No universal weights \(\lambda_k\) are claimed.

---

## 4. Domain dependence

Different domains can legitimately use different losses.

### Safety-critical deployment

May assign high weight to:

- invalid irreversible commitment;
- operationally closed reopening paths;
- hidden common-mode failure;
- authority spillover.

### Scientific exploration

May assign higher relative cost to:

- excessive skepticism;
- failure to preserve anomalous observations;
- hypothesis-space closure;
- premature rejection of low-authority candidates.

### Reversible online optimization

May tolerate:

- broader provisional scope;
- faster updates;
- weaker reopening contracts;

when consequences are cheap, observable, and rapidly reversible.

### Institutional governance

May need to include:

- unequal stakeholder harm;
- delayed consequences;
- lock-in and replacement cost;
- authority concentration;
- incentives to suppress reopening evidence.

The loss function must therefore declare its stakeholders and consequence horizon.

---

## 5. Loss legitimacy is itself governed

Making \(\Lambda\) explicit does not make it legitimate.

The loss may be wrong because:

- the target is misspecified;
- stakeholders are omitted;
- rare catastrophic outcomes are averaged away;
- reversibility is overestimated;
- complexity costs are assigned only to challengers;
- institutional power determines which harms count;
- the evaluator benefits from one outcome.

Therefore \(\Lambda\) also needs:

- provenance;
- scope;
- uncertainty;
- reopening conditions;
- replacement authority.

The framework must not create an unchallengeable loss function to govern challengeable claims.

---

## 6. Relationship to scope

Authority and scope errors are distinct loss terms.

A claim can have approximately correct authority but incorrect scope:

\[
W(H)\approx W^*(H),
\qquad
\Sigma(H)\neq\Sigma^*(H).
\]

Examples include:

- a valid laboratory result deployed outside laboratory conditions;
- a local benchmark promoted into a theory of intelligence;
- a valid subjective report promoted into a source-ontology claim;
- a treatment effect generalized to an untested population.

The governance loss should therefore score scope separately from confidence.

---

## 7. Relationship to reopening

Reopening has both benefit and cost.

Too little reopening permits lock-in:

\[
L_{\mathrm{closure}}\uparrow.
\]

Too much reopening produces paralysis and repeated audit cost:

\[
L_{\mathrm{reopening}}\uparrow.
\]

The relevant objective is not maximum skepticism but cost-sensitive independent correction:

\[
\operatorname{EVI}_{\perp}(T)
>
C(T)+C_{\mathrm{delay}}.
\]

Even this decision depends on the declared loss and risk model.

---

## 8. Benchmark role

Claim Contract Governance Benchmark v0.5 freezes one loss vector and compares:

\[
(H,W),
\]

\[
(H,W,\Sigma),
\]

and:

\[
(H,W,\Sigma,\Pi,H_{?},\mathcal R,\Gamma).
\]

It tests whether the richer state avoids evaluator-declared governance errors while paying explicit complexity overhead.

The benchmark does not establish that its loss weights are correct or transferable.

Its strongest negative result is that the evaluator rewards distinctions already encoded by the full contract.

---

## Final invariant

\[
\boxed{
\text{No update policy is preferable without a declared account of which mistakes, harms, delays, and complexity costs it is being optimized to avoid.}
}
