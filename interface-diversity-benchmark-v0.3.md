# Interface Diversity Benchmark v0.3

## Status

Exploratory benchmark design and first implementation.

This version does not add a new ontology layer. It tests the Level 4 frontier identified by v0.2 in the weakest bounded form:

\[
\boxed{
\text{Can a system select correction channels whose failure modes differ from the primary interface?}
}
\]

It does not test autonomous generation of new tests.

---

## 1. Research question

v0.2 showed:

\[
\text{A blind challenge cannot reveal a blind interface.}
\]

v0.3 therefore asks whether a bounded agent can distinguish:

- a correction channel with high marginal accuracy but shared blind spots;
- a channel with lower marginal accuracy but independent corrective coverage;
- many redundant channels whose vote count exaggerates confidence.

The hypothesis is:

\[
\boxed{
\text{correction value depends on failure-mode complementarity, not test count alone.}
}
\]

---

## 2. Minimal formalism

Let:

- \(Y\): target;
- \(P\): primary interface prediction;
- \(C_i\): candidate correction channel;
- \(e_P=\mathbf 1[P\neq Y]\);
- \(e_i=\mathbf 1[C_i\neq Y]\);
- \(c_i\): per-use cost.

Marginal accuracy is:

\[
A_i=P(C_i=Y).
\]

Correction coverage is:

\[
K_i=P(C_i=Y\mid P\neq Y).
\]

A channel can have:

\[
A_i>A_j
\]

while:

\[
K_i<K_j.
\]

That occurs when \(C_i\) performs well on ordinary cases but shares the primary interface's catastrophic failure mode.

The diversity-aware score is:

\[
S_i
=
(1-\lambda)\widehat A_i
+
\lambda\widehat K_i
-
c_i,
\]

where \(\lambda\in[0,1]\) is an externally declared stress weight.

The primary baseline is:

\[
S_P=(1-\lambda)\widehat A_P,
\]

because its correction coverage on its own failure set is zero.

This score is a benchmark mechanism, not a universal independence measure.

---

## 3. Environment

Every episode contains:

- a balanced binary target;
- a shared blind-spot event;
- a primary prediction;
- predictions from supplied correction channels.

If the shared blind spot occurs:

- the primary interface fails;
- every correlated correction channel fails with it;
- independent channels retain their own error process.

Outside the shared blind spot, each channel has its own residual error rate.

Calibration and evaluation may use different shared-failure frequencies.

This creates a distribution shift where marginally strong but correlated channels can lose to a less correlated channel.

---

## 4. Agents

### Primary only

Uses the original interface.

### Marginal-accuracy selector

Selects the supplied channel with the highest calibration accuracy after cost.

It does not condition on primary failures.

### Independence-aware selector

Uses labeled calibration data to estimate \(K_i\) and selects the path with the highest stress-weighted score.

It refuses to estimate independence when too few primary failures were observed.

### Count-all-tests baseline

Queries every supplied channel and takes a majority vote.

It treats correlated quantity as evidential weight.

### Oracle selector

Chooses the single path with the highest realized evaluation net reward.

---

## 5. Scenarios

### Shared blind-spot shift

Two high-marginal-accuracy channels share the primary blind spot.

One lower-marginal-accuracy channel has independent errors.

The shared blind spot becomes more frequent during evaluation.

### Redundant quantity

Five correlated channels compete with one independent channel.

This tests:

\[
\text{test count}\neq\text{failure-mode diversity}.
\]

### All independent

All candidate channels have independent errors.

The diversity-aware rule should reduce to ordinary net-performance selection rather than manufacturing a distinction.

### All costly

Every supplied correction path is uneconomic.

The system should retain the primary interface.

### No exposed primary failures

Calibration contains no primary failure.

Evaluation later introduces a shared blind spot.

The system should be unable to estimate correction-path independence from the supplied evidence.

---

## 6. Primary pass conditions

The local claim receives support only if:

1. failure-conditioned selection outperforms marginal-accuracy selection under the declared shared-blind-spot shift;
2. it approaches the supplied-path oracle;
3. one independent path beats a majority of correlated tests;
4. it agrees with ordinary performance selection when all candidates are independent;
5. it rejects all paths when every path is too costly;
6. it fails openly when calibration exposes no primary failures.

---

## 7. Stopping rule

The benchmark avoids infinite meta-recursion by using a bounded candidate set and one explicit rule:

\[
\boxed{
\text{stop when no supplied correction path has positive marginal stress-adjusted value over the current path.}
}
\]

Meta-level position grants no authority.

A channel earns authority only through:

- labeled corrective coverage;
- declared cost;
- held-out performance;
- distinct failure behavior.

---

## 8. Falsification and redundancy

The broader claim should be reduced or abandoned if:

- marginal accuracy explains all held-out behavior;
- correlated vote count performs equally well after cost;
- correction coverage does not transfer under the declared shift;
- the stress weight merely hard-codes the desired answer;
- robust ensemble selection or correlated-error decision theory fully explains the benchmark without a distinct interface framework.

A successful run does not establish a new theory merely because the vocabulary uses interfaces.

---

## 9. Interpretation boundary

v0.3 receives externally:

- the target;
- labeled calibration data;
- candidate correction channels;
- channel costs;
- the stress weight;
- the evaluation shift.

It does not:

- invent a correction channel;
- design an intervention;
- discover an unlabeled target;
- infer the stress weight;
- identify independence without observed failures;
- validate an unlimited hierarchy of auditors.

The benchmark tests **selection among supplied correction paths**, not interface invention.

---

## Final criterion

\[
\boxed{
\text{A system is more correctable when it selects correction paths by what they can reveal about its failures, not by how often they agree with it.}
}
\]
