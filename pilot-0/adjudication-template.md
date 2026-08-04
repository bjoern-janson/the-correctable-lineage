# Pilot 0 Plural Adjudication Template

## Status

This template records defensible consequences without assuming one hidden canonical claim contract.

Adjudicators judge responses, actions, and later-evidence handling—not conformity to framework vocabulary.

No single adjudicator has unilateral truth authority.

---

## 1. Adjudicator record

- Adjudicator ID:
- Case ID:
- Domain role:
- Methods expertise:
- Practitioner responsibility:
- Affiliations and potential conflicts:
- Prior familiarity with the framework:
- Representation condition visible? yes / no / uncertain
- Recusal required? yes / no

---

## 2. Case-stage consequence map

For each evidence stage \(t\), record:

\[
J_t
=
(
\mathcal A_t^{\mathrm{permitted}},
\mathcal A_t^{\mathrm{prohibited}},
\mathcal A_t^{\mathrm{contested}},
V_t^{\mathrm{retain}},
Q_t^{\mathrm{open}}
).
\]

### Permitted actions

Actions supported by the evidence and consequence structure.

| Action | Conditions | Stakeholders protected | Residual risk |
|---|---|---|---|
| | | | |

### Prohibited actions

Actions contradicted or unjustifiably risky under the evidence.

| Action | Why prohibited | Evidence basis |
|---|---|---|
| | | |

### Contested actions

Actions for which more than one defensible judgment remains.

| Action | Defensible position A | Defensible position B | Missing discrimination |
|---|---|---|---|
| | | | |

### Valid structure to retain

Claims or evidence that should survive the latest contradiction.

| Retained proposition | Validity limits | Why retained |
|---|---|---|
| | | |

### Open questions

| Question | Why unresolved | Evidence needed |
|---|---|---|
| | | |

---

## 3. Response-level scoring record

For each participant response, score only against the case evidence and the plural consequence map.

### A. Evidence fidelity

Did the response accurately represent the supplied evidence?

- 0 — major contradiction or invention;
- 1 — substantial omissions or distortion;
- 2 — mostly accurate with material gaps;
- 3 — accurate and appropriately qualified.

### B. Action defensibility

- 0 — recommends a prohibited action without a defensible rationale;
- 1 — contains major action error;
- 2 — falls within the contested region or is mostly defensible;
- 3 — permitted and well justified.

### C. Valid-structure retention

- 0 — discards nearly all still-valid structure;
- 1 — retains little or retains it without limits;
- 2 — preserves most warranted claims;
- 3 — preserves warranted claims with appropriate boundaries.

### D. Unsupported extension

- 0 — extensive unsupported extension;
- 1 — one major unsupported extension;
- 2 — minor or ambiguous extension;
- 3 — no material extension beyond evidence.

### E. Dependency handling

- 0 — treats known shared evidence as fully independent;
- 1 — notices dependence but does not alter reasoning;
- 2 — partially adjusts;
- 3 — appropriately adjusts or records unresolved dependence.

### F. Future correction path

- 0 — no usable revision path;
- 1 — vague or operationally unavailable path;
- 2 — relevant path with one material weakness;
- 3 — relevant, obtainable, decision-connected path.

### G. Stakeholder-loss transparency

- 0 — hidden or incoherent consequence assumptions;
- 1 — mentions tradeoffs without specifying them;
- 2 — identifies major stakeholders and tradeoffs;
- 3 — makes domain, horizon, reversibility, and contested weights explicit.

---

## 4. Multiple-valid-representation rule

Two responses may encode different internal structures while both receiving high consequence scores.

Do not penalize:

- different but defensible hypothesis partitions;
- different native terminology;
- different numerical confidence scales;
- different argument structures;
- different next-test choices when expected values are comparable.

Penalize only when the difference changes evidence fidelity, action quality, valid-structure retention, future correction, or cost in a material way.

---

## 5. Repair convergence

After each new evidence stage, record whether initially divergent participants move toward compatible action states.

For participant \(i\), let \(a_{i,t}\) be the action status vector at stage \(t\).

A descriptive repair-convergence statistic may be:

\[
RC_t
=
1-
\frac{1}{N(N-1)}
\sum_{i\neq j}
\operatorname{dist}(a_{i,t},a_{j,t}),
\]

where the distance function is frozen before analysis.

Report separately:

- convergence toward permitted actions;
- convergence toward prohibited actions;
- convergence caused only by generalized abstention;
- persistent legitimate disagreement.

---

## 6. Reconstruction disagreement classification

When representations differ, classify the difference:

1. **Decorative** — notation differs but behavior is equivalent.
2. **Granularity** — one representation splits a claim another combines.
3. **Evidence interpretation** — different evidential edge.
4. **Scope** — different validity or action domain.
5. **Dependency** — different shared-cause model.
6. **Loss** — different stakeholder or consequence weighting.
7. **Action** — materially different recommendation.
8. **Reopening** — different future correction path.
9. **Specification failure** — manual did not resolve a necessary distinction.
10. **Case underidentification** — evidence does not identify one resolution.

The last two must not be rewritten as participant incompetence.

---

## 7. Panel synthesis

Each adjudicator submits an independent record before discussion.

Then the panel records:

- areas of agreement;
- areas of persistent disagreement;
- whether disagreement arises from facts, model structure, values, or action thresholds;
- whether the case is identifiable enough for quantitative scoring;
- whether any score requires framework-specific terminology;
- whether one representation condition was recognizable.

### Panel outcome

Choose one:

- suitable for Pilot 0 scoring;
- suitable only for qualitative feasibility analysis;
- revise case and rerun;
- exclude before participant analysis;
- irreducibly contested and retain as disagreement case.

No outcome may be changed after condition performance is revealed except through a documented protocol-deviation process.

---

## 8. Appeal and audit

A comparator steward, participant representative, or independent auditor may challenge:

- a case interpretation;
- a prohibited-action label;
- a material-equivalence judgment;
- a conflict of interest;
- framework vocabulary leakage;
- scorer identification of condition;
- inconsistent application of the rubric.

Appeals must be resolved by a panel that excludes the original sole decision-maker.

All revisions and unresolved appeals remain in the public record, subject to participant privacy.
