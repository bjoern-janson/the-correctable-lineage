# Correction Ecosystem Benchmark v0.4 — Negative Result Ledger

## Status

Frozen with the first exploratory implementation using 100 seeds per scenario-agent pair.

This ledger records what v0.4 fails to establish and where ecosystem auditing fails.

---

## 1. The hidden dependency is externally authored

The evaluator specifies:

- the latent dependency \(Z\);
- which channels share it;
- the intervention that changes it;
- the audit sample size;
- the target labels;
- channel and audit costs;
- the future shift prior;
- the deployment horizon.

The agent does not discover the dependency graph.

---

## 2. A blind intervention remains blind

### Condition

The audit preserves:

\[
P(Z=1)=0.
\]

### Result

The intervention selector pays the audit cost, continues observing apparently strong shared channels, and fails to select the independent path.

### Interpretation

\[
\boxed{
\text{An intervention that does not vary the hidden cause cannot identify dependence on that cause.}
}
\]

Meta-level status does not grant correction authority.

---

## 3. Diagnosis does not guarantee repair

### Condition

All supplied channels share the hidden dependency.

### Result

The intervention usually detects ecosystem-wide compromise, but no supplied path repairs it.

### Interpretation

\[
\boxed{
\text{identified common-mode failure}
\not\Rightarrow
\text{available independent correction path}.
}
\]

The benchmark records compromise and avoids laundering diagnosis into repair.

---

## 4. Labeled audit is privileged

The intervention selector uses target labels during audit.

Without labels or another correctness reference, the agent cannot determine whether a channel survived the intervention or merely changed differently.

Therefore:

\[
\text{channel disagreement}
\neq
\text{identified correctness}.
\]

v0.4 does not solve truth identification from unlabeled altered conditions.

---

## 5. Statistical decorrelation is not causal independence

Channels can appear weakly correlated during ordinary calibration because the common-mode variable never changes.

Conversely, channels can appear correlated despite different causal access because they observe the same easy target.

The benchmark identifies the shared dependency only because the generative structure and intervention are supplied.

It does not define a universal causal-independence metric.

---

## 6. Audit value uses declared risk

The audit decision depends on a supplied shift prior, scalar reward, and known horizon.

It does not infer:

- future dependency activation;
- catastrophic-tail importance;
- irreversible harm;
- ambiguity over the model class;
- heterogeneous stakeholder costs.

Expected-value rejection of an audit may still be unsafe under a different objective.

---

## 7. The DMT/entity analogy is not an experimental result

Reports of vivid DMT entity encounters motivate a source-identification question:

\[
\text{discovery channel}
\quad\text{vs.}\quad
\text{simulation channel}
\quad\text{vs.}\quad
\text{self-confirming channel}.
\]

But v0.4 contains no DMT data, no human subjects, no telepathy test, and no external-entity hypothesis.

Its result cannot increase authority for any ontological interpretation of psychedelic experience.

The analogy is structural only:

\[
\text{multiple reports or phenomenological features}
\not\Rightarrow
\text{multiple independent correction paths}.
\]

---

## 8. Formal redundancy remains

The implementation is describable through:

- causal intervention;
- robust feature or sensor selection;
- common-mode failure analysis;
- experimental design;
- decision theory under latent dependence.

The benchmark does not establish a distinct general theory of epistemic topology.

---

## 9. The recursive frontier moves outward again

v0.4 can use a supplied intervention to reveal one supplied hidden dependency.

It cannot determine whether:

- the target labels are wrong;
- the intervention misses a deeper dependency;
- every candidate intervention shares one upstream assumption;
- the evaluator's causal graph is mis-specified.

The remaining frontier is:

\[
\boxed{
\text{Can a system generate or select interventions that expose dependencies absent from its supplied causal model?}
}
\]

---

## Frozen conclusion

v0.4 supports only:

\[
\boxed{
\text{a supplied support-changing intervention can expose common-mode correction failure hidden by ordinary calibration.}
}
\]

Its strongest negative result is:

\[
\boxed{
\text{A blind intervention cannot validate a blind correction ecosystem.}
}
\]
