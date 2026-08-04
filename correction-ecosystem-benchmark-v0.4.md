# Correction Ecosystem Benchmark v0.4

## Status

Exploratory benchmark design and first implementation.

This benchmark tests a narrower form of joint correction-path diagnosis:

\[
\boxed{
\text{Can a supplied intervention expose a hidden upstream dependency shared by apparently independent correction channels?}
}
\]

It does not test autonomous discovery of the dependency or autonomous generation of the intervention.

---

## 1. Motivation

v0.3 showed that failure-conditioned correction coverage can outperform marginal accuracy and correlated vote count when primary failures are represented in calibration.

Its strongest boundary was:

\[
\text{success-only calibration}
\not\Rightarrow
\text{identified correction-path independence}.
\]

Several channels can appear accurate and weakly correlated because the common failure mechanism never varies in calibration.

v0.4 introduces one additional operation:

\[
\operatorname{do}(Z=1),
\]

a supplied intervention on a latent upstream dependency \(Z\).

The question is whether that intervention reveals that multiple correction channels share one common-mode failure.

---

## 2. Minimal formalism

Let:

- \(Y\in\{0,1\}\): target;
- \(P\): primary interface;
- \(C_1,\ldots,C_n\): supplied correction channels;
- \(Z\in\{0,1\}\): hidden upstream dependency state;
- \(A_Z\): supplied intervention that changes the distribution of \(Z\);
- \(c_i\): per-use channel cost;
- \(c_A\): one-time audit cost;
- \(T\): deployment horizon.

For shared channels:

\[
C_i \approx Y
\quad\text{when}\quad
Z=0,
\]

but:

\[
C_i \approx 1-Y
\quad\text{when}\quad
Z=1.
\]

An independent channel \(C_\perp\) remains target-linked under both states:

\[
P(C_\perp=Y\mid Z=0)
\approx
P(C_\perp=Y\mid Z=1).
\]

Ordinary calibration holds \(Z=0\), so the shared dependency is not identified from output statistics alone.

The supplied audit changes the support:

\[
A_Z:
P(Z=1)\uparrow.
\]

---

## 3. Experimental conditions

### Hidden shared dependency

- calibration: \(P(Z=1)=0\);
- audit: \(P(Z=1)=0.5\);
- deployment: \(P(Z=1)=0.5\);
- one lower-marginal-accuracy channel is independent of \(Z\).

### Blind intervention

The audit preserves:

\[
P(Z=1)=0.
\]

It cannot reveal the common-mode dependency.

### All-independent control

All channels have distinct failure processes.

The audit policy should reduce to ordinary net-performance selection.

### Costly-audit control

The supplied intervention is valid but:

\[
\frac{c_A}{T}
\]

exceeds the declared upper bound on expected benefit.

The agent should not audit.

### No-independent-path control

The audit reveals that all supplied paths share the dependency.

The agent may diagnose ecosystem compromise but must not claim that a repair exists.

### Unlabeled-audit control

The intervention occurs without a correctness reference for audit cases.

The benchmark cannot identify which channel remains target-linked.

---

## 4. Agents

### Primary-only

Uses \(P\) throughout.

### Calibration selector

Chooses the channel with highest:

\[
\widehat A_i-c_i
\]

under ordinary calibration.

### Count-all-tests

Uses a majority vote over all supplied channels.

This tests whether correction-path quantity substitutes for common-mode independence.

### Intervention selector

First applies a finite audit decision:

\[
\frac{c_A}{T}
<
\overline V_A,
\]

where \(\overline V_A\) is a declared conservative upper bound on intervention value.

If auditing is justified, it scores channels using ordinary and intervention performance:

\[
S_i
=
(1-\lambda)\widehat A_i^{\mathrm{cal}}
+
\lambda\widehat A_i^{\mathrm{audit}}
-
c_i
-
\frac{c_A}{T}.
\]

If every supplied path falls near chance under audit, the agent records ecosystem compromise and retains the primary path rather than inventing a repair.

### Oracle selector

Chooses the best supplied path using deployment labels.

It defines a ceiling, not a realizable agent.

---

## 5. Primary metrics

- held-out accuracy;
- net reward after per-use and audit costs;
- audit rate;
- selected correction path;
- common-mode-compromise detection rate;
- gap to supplied-path oracle.

---

## 6. Pass conditions

The local claim receives support only if:

1. the intervention selector outperforms calibration-only selection under the hidden shared dependency;
2. it approaches the supplied-path oracle after cost;
3. a blind intervention fails to identify the independent channel;
4. all-independent conditions reduce to ordinary performance selection;
5. an uneconomic intervention is rejected;
6. common-mode compromise is diagnosed without falsely claiming repair;
7. unlabeled audit does not receive unsupported correctness authority.

---

## 7. Falsification and reduction conditions

The v0.4 framing becomes unnecessary or fails if:

1. ordinary calibration already identifies the shared dependency;
2. output-correlation analysis alone matches the intervention selector;
3. gains come only from privileged labels or extra samples rather than support-changing intervention;
4. the agent audits regardless of cost;
5. the agent claims repair when every supplied path fails;
6. a blind intervention performs as well as the valid intervention;
7. existing causal experiment-design or robust-selection formalisms describe the result without loss.

---

## 8. Interpretation boundary

A positive result would establish only that:

\[
\boxed{
\text{a supplied intervention on an upstream dependency can expose common-mode correction failure hidden by ordinary calibration.}
}
\]

It would not establish:

- autonomous discovery of latent dependencies;
- autonomous intervention generation;
- unlabeled truth identification;
- independent causal access from decorrelation alone;
- external validation of subjective or altered-state experiences;
- a universal theory of epistemic topology;
- interface invention.

---

## Final criterion

\[
\boxed{
\text{A correction ecosystem is not independently tested merely because its outputs disagree; the relevant hidden dependency must be made capable of varying.}
}
\]
