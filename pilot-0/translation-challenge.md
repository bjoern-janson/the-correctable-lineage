# Pilot 0 Translation Challenge

## Status

This is a pre-pilot adversarial exercise.

It is not a participant condition in the current Pilot 0 preregistration draft and should not be added to the study without independent review and freezing.

Its purpose is to test whether the proposed distinctions can be reconstructed in mature external vocabularies without claim-contract terminology.

---

## Core question

\[
\boxed{
\text{Does the proposed representation preserve information across methods, or merely rename distinctions that existing methods already preserve?}
}
\]

The target outcome is not convergence on one vocabulary.

It is measurement of **translation loss**.

---

## Materials supplied to translator

Provide one neutral sequential case and only the following:

- the raw case facts available at the current evidence stage;
- the action choices available to the decision-maker;
- stakeholder and consequence information required by the case;
- a short specification of the translator's preferred method.

Do not provide:

- claim-contract terminology;
- labels such as scope error, dependency collapse, authority laundering, or reopening failure;
- worked examples from the repository;
- the framework author's preferred decomposition;
- scoring labels or hidden adjudication categories.

---

## Translator instruction

> Represent the case using your preferred technical framework. Record what is supported, what remains unresolved, what actions are justified, which assumptions or dependencies matter, what future evidence would change the conclusion, and what response that evidence should trigger.

The translator may use:

- a Bayesian workflow;
- a causal model;
- an assurance or safety case;
- a belief-revision structure;
- a provenance-aware workflow;
- another declared mature method.

The translator should use native terminology rather than attempting to imitate the claim contract.

---

## Common output surface

Regardless of method, the output must expose:

1. **Current claims** — what is presently supported.
2. **Unsupported-but-open possibilities** — what remains possible but lacks current authority.
3. **Rejected claims** — what the evidence currently rules out.
4. **Scope** — populations, environments, conditions, horizons, and action classes covered.
5. **Dependencies** — shared data, assumptions, tools, generators, evaluators, or preprocessing.
6. **Action recommendation** — proceed, narrow, monitor, suspend, rollback, replace, or collect evidence.
7. **Decision basis** — loss, risk, reversibility, and stakeholder assumptions.
8. **Reopening evidence** — realistically obtainable observations that would change the state.
9. **Revision response** — what would materially change if that evidence arrived.
10. **Residual disagreement** — where another competent analyst could disagree and why.

This common surface is not a hidden requirement to reproduce the claim-contract ontology. It records consequences needed for cross-method comparison.

---

## Translation directions

For each case, conduct at least two directions.

### Direction A — mature method to claim contract

1. An external method steward produces a native representation.
2. A separate translator maps it into:

\[
(H,W,\Sigma,\Pi,\mathcal R,\Gamma,\Lambda).
\]

3. The original steward reviews whether anything was added, distorted, or lost.

### Direction B — claim contract to mature method

1. A claim-contract record is produced without access to the external method's representation.
2. A separate translator maps it into the mature method.
3. A claim-contract user and method steward independently identify losses or additions.

Where possible, translators should be blinded to the study's preferred conclusion.

---

## Translation-loss record

For each direction, record:

\[
TL=(L_{drop},L_{invent},L_{blur},L_{cost},L_{action}),
\]

where:

- \(L_{drop}\): information present in the source but absent from the target;
- \(L_{invent}\): distinctions introduced by the translator but unsupported by the source;
- \(L_{blur}\): distinctions merged or made less precise;
- \(L_{cost}\): time, training, fields, and clarification required;
- \(L_{action}\): changes in recommended action, monitoring, or reopening behavior.

Do not collapse these into one scalar unless weights are declared and sensitivity is reported.

---

## Information units to compare

Potential units include:

- identified point, interval, ordering, or equivalence class;
- confidence or uncertainty state;
- target dimension receiving authority;
- validity and transfer scope;
- evidence provenance;
- shared dependencies;
- unresolved alternatives;
- defeaters;
- stakeholder loss assumptions;
- action threshold;
- operational reopening condition;
- required revision or rollback;
- responsibility and decision rights.

Credit should not be awarded merely because two methods use different names for the same unit.

---

## Interpretation regimes

### Absorption

A mature method preserves every behaviorally relevant distinction at equal or lower cost.

\[
\boxed{
TL_{mature\rightarrow contract}\approx0
\quad\text{and}\quad
C_{mature}\leq C_{contract}.
}
\]

Interpretation: the claim contract is a synthesis, teaching device, or redundant layer.

### Integration advantage

Individual mature methods preserve subsets, but the claim contract reduces cross-method translation loss or coordination cost.

Interpretation: possible value as an interoperability or audit layer, not as new underlying theory.

### Private ontology

Translation requires inventor mediation, retrospective relabeling, or unsupported additions.

Interpretation: the representation has not become a public instrument.

### External-method advantage

A mature method preserves more decision-relevant information or produces better correction at lower cost.

Interpretation: narrow, replace, or absorb the claim-contract representation.

### Case underidentification

Representations diverge because the case does not contain enough information to distinguish them.

Interpretation: revise the case or preserve disagreement; do not score one ontology as correct.

---

## Anti-leakage checks

A reviewer should reject or revise the challenge when:

- the case narrative contains corpus vocabulary;
- the output template reveals a preferred answer;
- the mature method is prohibited from adding native extensions;
- one representation receives more factual information;
- the adjudication key is derived from the claim-contract fields;
- translations are judged only by framework authors;
- missing information is treated as participant error;
- agreement is manufactured through retrospective expert mapping.

---

## Pre-pilot use

Before recruiting participants:

1. give one case to one statistics or Bayesian steward;
2. give the same case to one assurance or safety steward;
3. have each produce a native representation;
4. perform both translation directions;
5. record information loss and cost;
6. revise only the claim boundary, manuals, case neutrality, or scoring rules;
7. do not add new ontology unless both methods expose a behaviorally important unrepresentable distinction.

---

## Final criterion

\[
\boxed{
\text{A distinct contribution requires lower behaviorally relevant translation loss or better correction—not merely a new common vocabulary.}
}
