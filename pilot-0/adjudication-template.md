# Pilot 0 Plural Adjudication Template

## Status

This template records defensible consequences without assuming one hidden canonical claim contract.

Adjudicators judge responses, actions, and later-evidence handling—not conformity to framework vocabulary.

No single adjudicator has unilateral truth authority.

Consensus is evidence about adjudication stability, not a substitute for case evidence or consequence tracking.

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
\boxed{
J_t
=
(
\mathcal A_t^{\mathrm{permitted}},
\mathcal A_t^{\mathrm{prohibited}},
\mathcal A_t^{\mathrm{contested}},
\mathcal A_t^{\mathrm{unsupported\text{-}open}},
\mathcal A_t^{\mathrm{underidentified}},
V_t^{\mathrm{retain}},
Q_t^{\mathrm{open}}
).
}
\]

The five action regions are not a confidence ranking. They represent different evidential and governance states.

### Permitted actions

Actions supported by the evidence and consequence structure now.

| Action | Conditions | Stakeholders protected | Residual risk |
|---|---|---|---|
| | | | |

### Prohibited actions

Actions contradicted or unjustifiably risky under the current evidence.

| Action | Why prohibited | Evidence basis |
|---|---|---|
| | | |

### Contested actions

Actions for which more than one current recommendation remains defensible because of a genuine difference in causal model, stakeholder loss, action threshold, or professional standard.

| Action | Defensible position A | Defensible position B | Source of disagreement | Missing discrimination, if any |
|---|---|---|---|---|
| | | | | |

### Unsupported-but-open actions

Actions not currently justified, but not ruled out by the evidence and plausibly authorizable after a specified discrimination, safeguard, or change in conditions.

| Action | Why currently unsupported | What keeps it open | Evidence or safeguard needed |
|---|---|---|---|
| | | | |

This category prevents:

\[
\text{not currently established}
\rightarrow
\text{false or permanently prohibited}.
\]

It also prevents an open possibility from receiving present deployment authority.

### Underidentified actions

Actions the case record cannot reliably classify because essential facts, causal structure, consequences, or stakeholder priorities are absent.

| Action | Missing case information | Why other regions cannot be assigned | Can the case be repaired? |
|---|---|---|---|
| | | | |

Underidentification is a property of the evaluation substrate, not automatically a participant error.

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
- 1 — contains a major action error or grants authority to an unsupported-open action;
- 2 — falls within a contested or unsupported-open region with appropriate qualification, or is mostly defensible;
- 3 — permitted and well justified, or correctly withholds current authority while preserving an open path.

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

### H. Open-status calibration

Did the response distinguish among currently supported, unsupported-but-open, contradicted, contested, and underidentified states?

- 0 — collapses these states in a materially harmful way;
- 1 — recognizes uncertainty but confuses current authority with future possibility;
- 2 — mostly preserves the distinctions;
- 3 — correctly withholds or grants present authority while preserving appropriate future possibility.

### I. Disagreement legibility

Did the response make the source of material disagreement inspectable?

- 0 — disagreement remains entangled or is dismissed as error;
- 1 — disagreement is acknowledged but not localized;
- 2 — major source is identified;
- 3 — disagreement is localized to hypotheses, evidence, measurement, scope, dependency, loss, action threshold, reopening, or case/manual failure.

---

## 4. Multiple-valid-representation rule

Two responses may encode different internal structures while both receiving high consequence scores.

Do not penalize:

- different but defensible hypothesis partitions;
- different native terminology;
- different numerical confidence scales;
- different argument structures;
- different next-test choices when expected values are comparable;
- one response marking a possibility unsupported-but-open while another leaves it in an explicit unresolved set, when both withhold present authority and preserve the same future discrimination.

Penalize only when the difference changes evidence fidelity, action quality, valid-structure retention, future correction, disagreement legibility, or cost in a material way.

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

The action alphabet should preserve at least:

\[
\{
\text{permitted},
\text{conditional},
\text{unsupported-open},
\text{suspended},
\text{prohibited},
\text{contested},
\text{underidentified}
\}.
\]

Report separately:

- convergence toward permitted actions;
- convergence toward prohibited actions;
- convergence toward correctly unsupported-open states;
- convergence caused only by generalized abstention;
- persistent legitimate disagreement;
- movement caused by better evidence versus imposed panel consensus.

---

## 6. Disagreement-legibility map

For every material participant or adjudicator disagreement, record one or more sources:

1. hypothesis partition;
2. evidence interpretation;
3. measurement assumption;
4. scope;
5. dependency model;
6. stakeholder loss;
7. action threshold;
8. reopening condition;
9. representation-manual ambiguity;
10. case underidentification;
11. factual error;
12. irreducibly mixed or currently unclassifiable.

A representation may provide value without producing consensus when it converts:

\[
\text{entangled disagreement}
\rightarrow
\text{typed, inspectable disagreement}.
\]

Record:

- coder agreement on disagreement source;
- proportion of material disagreements assigned a stable source;
- proportion remaining unclassifiable;
- whether localization changes the next evidence request;
- whether localization permits coexistence, targeted testing, or negotiated action.

Do not count forced translation into claim-contract vocabulary as disagreement legibility.

---

## 7. Reconstruction disagreement classification

When representations differ, classify the difference:

1. **Decorative** — notation differs but behavior is equivalent.
2. **Granularity** — one representation splits a claim another combines.
3. **Evidence interpretation** — different evidential edge.
4. **Scope** — different validity or action domain.
5. **Dependency** — different shared-cause model.
6. **Loss** — different stakeholder or consequence weighting.
7. **Action** — materially different recommendation.
8. **Reopening** — different future correction path.
9. **Open-status calibration** — different treatment of unsupported, contradicted, contested, or underidentified possibilities.
10. **Specification failure** — manual did not resolve a necessary distinction.
11. **Case underidentification** — evidence does not identify one resolution.

The last two must not be rewritten as participant incompetence.

---

## 8. Panel synthesis

Each adjudicator submits an independent record before discussion.

Then the panel records:

- areas of agreement;
- areas of persistent disagreement;
- whether disagreement arises from facts, model structure, values, action thresholds, or open-status calibration;
- which unsupported possibilities remain open and why;
- whether the case is identifiable enough for quantitative scoring;
- whether any score requires framework-specific terminology;
- whether one representation condition was recognizable.

### Panel outcome

Choose one:

- suitable for Pilot 0 scoring;
- suitable only for qualitative feasibility analysis;
- revise case and rerun;
- exclude before participant analysis;
- irreducibly contested and retain as disagreement case;
- underidentified and retain only as evaluation-substrate failure evidence.

No outcome may be changed after condition performance is revealed except through a documented protocol-deviation process.

---

## 9. Appeal and audit

A comparator steward, participant representative, or independent auditor may challenge:

- a case interpretation;
- a prohibited-action label;
- failure to distinguish unsupported-but-open from prohibited;
- a material-equivalence judgment;
- a conflict of interest;
- framework vocabulary leakage;
- scorer identification of condition;
- inconsistent application of the rubric;
- retrospective consensus laundering.

Appeals must be resolved by a panel that excludes the original sole decision-maker.

All revisions and unresolved appeals remain in the public record, subject to participant privacy.
