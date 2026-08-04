# Evaluation Charter

## Status

This charter governs the design and execution of the Claim Contract Governance Comparative Evaluation Protocol v1.0.

It is not:

- benchmark v0.6;
- a completed study;
- ethics approval;
- a substitute for preregistration;
- evidence that claim contracts outperform existing methods;
- authority for framework authors to adjudicate their own success.

Its purpose is narrower:

\[
\boxed{
\text{Prevent the comparative evaluation from becoming a claim-contract-controlled test of claim contracts.}
}
\]

---

## 1. The evaluation substrate is itself a governed claim system

The comparative study depends on claims about:

- case realism;
- comparator fidelity;
- evidence equivalence;
- outcome correctness;
- acceptable alternative interpretations;
- complexity cost;
- practically important effect size;
- dissolution or replacement conditions.

Those claims do not become authoritative merely because they are made by an external evaluator.

Define evaluator authority as:

\[
\boxed{
\mathcal A_{\mathrm{eval}}
=
(R,P,C,A,D,Q,X),
}
\]

where:

- \(R\): evaluator role and permitted decision rights;
- \(P\): expertise, incentives, affiliations, and provenance;
- \(C\): declared decision criteria;
- \(A\): admissible alternative interpretations;
- \(D\): disagreement and deadlock process;
- \(Q\): quality-control and appeal procedures;
- \(X\): replacement, recusal, and authority-expiry conditions.

The governing rule is:

\[
\boxed{
\text{Externality does not grant truth authority; it creates a new evidential path whose reliability must be audited.}
}
\]

---

## 2. Separation of powers

No person or group should control more evaluation layers than necessary.

### Framework authors

May:

- specify the claim-contract representation;
- state its intended behavior;
- identify known failure modes;
- propose negative and adversarial cases;
- review factual descriptions of the framework.

May not be the sole authority over:

- case selection;
- comparator fidelity;
- adjudication labels;
- exclusion decisions;
- primary analysis;
- interpretation of comparative superiority.

### Comparator stewards

Each mature alternative should have at least one steward competent in that method.

Stewards may:

- specify a native-strength representation;
- identify unfair restrictions;
- propose method-native metrics and cases;
- challenge claims of material equivalence.

They may not alter their frozen method after inspecting comparative outcomes except through preregistered correction procedures.

### Domain case authors

Case authors provide realistic evidence sequences and consequence structures.

They should not be required to use claim-contract vocabulary and should not know which response pattern the framework expects.

### Adjudication panel

The adjudication panel determines the set of defensible consequences and actions under each evidence stage.

It does not determine which internal representation participants must use.

### Analysis team

The analysis team applies the preregistered statistical plan and records all deviations.

Where feasible, the primary analyst should be blinded to condition labels until data cleaning and exclusion decisions are frozen.

### Independent audit role

An independent audit role checks:

- ontology leakage;
- information asymmetry;
- comparator weakening;
- evaluator conflicts;
- post-outcome rule changes;
- suppressed disagreement;
- undocumented framework-author intervention.

---

## 3. Comparator authority

The hardest comparator is not one universal hybrid chosen by framework authors.

The study should use a comparator-family process.

For each mature method:

1. a method steward proposes a strong practical specification;
2. the specification declares its state, update rules, action rules, monitoring, and cost;
3. an independent equivalence panel records which governance functions it represents;
4. the schema is frozen before comparative outcome inspection;
5. unresolved disputes are preserved rather than settled in favor of claim-contract vocabulary.

### Minimal sufficient augmentation

For each comparator, define:

\[
M_j^{+}
=
\text{the smallest method-native augmentation that captures the suspected advantage}.
\]

Examples may include:

- Bayesian validity-domain metadata, posterior predictive checks, monitoring triggers, and decision thresholds;
- assurance-case defeaters, contexts, confidence arguments, and surveillance requirements;
- causal-model transportability assumptions and intervention-access records;
- belief-revision entrenchment and explicit revision triggers.

The decisive question is:

\[
\boxed{
\text{Does the claim contract add a necessary abstraction, or bundle extensions that existing methods can represent more cheaply?}
}
\]

If a minimal augmentation reproduces the benefit with equal or lower cost, the appropriate conclusion is absorption or synthesis.

### Material-equivalence disputes

No single party decides whether two representations contain equivalent information.

Equivalence must be assessed at three levels:

1. **Representational:** Can both encode the relevant distinction?
2. **Operational:** Do both produce the same correction and action behavior?
3. **Cost:** Do they require comparable training, time, storage, coordination, and review?

A representation receives no advantage for renaming information already present elsewhere.

---

## 4. Case-authority contract

A case is not authoritative merely because a domain expert wrote it.

Each case must carry a record:

\[
C_{\mathrm{case}}
=
(S,P,E,K,U,L),
\]

where:

- \(S\): intended domain and scope;
- \(P\): author expertise, affiliations, and conflicts;
- \(E\): staged evidence sequence;
- \(K\): known ambiguities and alternative causal accounts;
- \(U\): permissible actions and consequences;
- \(L\): limitations and realism compromises.

### Case acceptance gates

A case enters the primary suite only if:

1. domain reviewers judge it plausible;
2. the intended failure is not obvious from wording alone;
3. the case supports more than one initially defensible interpretation;
4. later evidence creates observable consequences that discriminate earlier commitments;
5. the scoring record does not require claim-contract terminology;
6. framework authors did not control the final evidence sequence;
7. comparator stewards can identify at least one defensible method-native response.

### Case balance

The suite must contain cases where:

- simple methods should win;
- the claim contract may win;
- a mature comparator may dominate;
- no representation has enough information;
- adjudicators legitimately disagree;
- abstention is correct;
- abstention is unnecessarily costly.

A suite composed only of scope, dependency, and reopening failures would encode the conclusion.

---

## 5. Reconstruction validity without framework circularity

The reconstruction phase must not ask whether participants reproduced the author's preferred contract.

It separates two questions.

### Structural reliability

Given the same specification and case, do independent users produce stable enough structures to support coordination?

This includes agreement over:

- hypothesis partitions;
- validity domains;
- evidence dependencies;
- action permissions;
- reopening triggers;
- unresolved states.

### Consequential validity

Do the reconstructed states support appropriate behavior under later evidence?

Define:

\[
\boxed{
V_R
=
f(
\text{future-evidence handling},
\text{action quality},
\text{scope calibration},
\text{valid-structure retention},
\text{recovery}
).
}
\]

Multiple internal reconstructions may be valid if they produce defensible consequences.

The protocol must not force convergence on one vocabulary when different models preserve the same justified commitments.

### Private-ontology diagnosis

The framework exhibits a private-ontology problem when:

\[
\text{author-rated coherence}\uparrow
\]

while:

\[
\text{independent structural reliability}\downarrow
\quad\text{or}\quad
\text{consequential validity}\downarrow.
\]

Expert arbitration that retroactively maps divergent answers into apparent agreement must be reported separately from raw agreement.

---

## 6. Adjudication authority

The adjudication layer must not assume one uniquely correct correction when several are defensible.

For each evidence stage, adjudicators should produce:

\[
J_t
=
(
\mathcal A_t^{\mathrm{permitted}},
\mathcal A_t^{\mathrm{prohibited}},
\mathcal A_t^{\mathrm{contested}},
V_t^{\mathrm{retain}},
Q_t^{\mathrm{open}}
),
\]

where:

- \(\mathcal A_t^{\mathrm{permitted}}\): defensible actions;
- \(\mathcal A_t^{\mathrm{prohibited}}\): actions contradicted by the record;
- \(\mathcal A_t^{\mathrm{contested}}\): actions with unresolved expert disagreement;
- \(V_t^{\mathrm{retain}}\): claims that remain justified;
- \(Q_t^{\mathrm{open}}\): unresolved questions.

### Plural panels

Where feasible, each case should be reviewed by:

- domain experts;
- methodology experts;
- practitioners responsible for consequences.

Their judgments should be recorded separately before synthesis.

### Disagreement is data

The study must report:

- raw disagreement;
- reasons for disagreement;
- whether disagreement is domain-, method-, or value-driven;
- how much results change across defensible adjudication sets.

Consensus produced only after framework terminology is introduced does not count as independent agreement.

### Appeal and replacement

Material adjudication decisions must permit:

- documented challenge;
- response from the original panel;
- review by a panel without overlapping members;
- revision before data unblinding where possible;
- sensitivity analysis when disagreement remains.

An adjudicator should be recused when authorship, institutional interest, or method allegiance creates a material conflict.

---

## 7. Evaluator-loss governance

The study's loss function is itself a claim contract.

For each loss component record:

\[
L_k
=
(
\text{stakeholder},
\text{harm},
\text{horizon},
\text{reversibility},
\text{weight provenance},
\text{uncertainty}
).
\]

No single scalar should determine the primary conclusion.

Required outputs include:

- the raw outcome vector;
- domain-specific loss analyses;
- sensitivity over plausible weights;
- Pareto frontiers;
- stakeholder-specific rankings;
- cases where rankings reverse.

Framework authors may propose loss terms but may not be the sole authority over weights or stakeholders.

---

## 8. Pilot 0 — Reconstruction and charter stress test

The first execution milestone should not claim comparative performance.

### Purpose

\[
\boxed{
\text{Can outsiders instantiate the representations, and can the evaluation authority system operate without framework capture?}
}
\]

### Minimal design

- 3 neutral cases;
- 5–10 researchers or practitioners;
- claim-contract specification and at least two mature comparator specifications;
- no repository access;
- no benchmark code;
- no worked examples in the primary reconstruction condition;
- multiple independent adjudicators.

### Primary measurements

- completion time;
- malformed or missing fields;
- structural agreement;
- consequential validity under staged evidence;
- cognitive load;
- requests for clarification;
- adjudicator disagreement;
- ability to preserve raw disagreement;
- evidence of ontology leakage;
- evidence of comparator weakening.

### Pilot success criteria

Pilot 0 supports progression only if:

1. at least one non-author can construct each representation without direct coaching;
2. the claim-contract condition reaches a preregistered minimum structural reliability or consequential validity threshold;
3. comparator stewards judge their conditions materially faithful;
4. adjudication can identify defensible response sets without relying on framework vocabulary;
5. the study team can preserve unresolved disagreement;
6. complexity and clarification burden are measurable;
7. no role has uncontrolled authority over cases, comparators, scoring, and interpretation simultaneously.

Failure should trigger revision or termination before a larger study.

---

## 9. Go/no-go gates for full execution

The comparative study should not begin until the following are frozen.

### Gate E0 — Role separation

All authorship, comparator, adjudication, analysis, audit, and appeal roles are assigned with conflicts recorded.

### Gate E1 — Comparator fidelity

Method stewards approve native-strength implementations or record unresolved objections.

### Gate E2 — Case independence

Primary cases are externally authored and pass the case-authority gates.

### Gate E3 — Adjudication plurality

Permitted, prohibited, and contested outcomes are recorded before participant data are unblinded.

### Gate E4 — Reconstruction feasibility

Pilot 0 establishes that the study instruments can be used without author coaching.

### Gate E5 — Analysis freeze

Primary endpoints, exclusions, models, sensitivity analyses, and dissolution outcomes are preregistered.

### Gate E6 — Ethics and data governance

Applicable human-participant, consent, privacy, compensation, and data-use requirements are approved.

### Gate E7 — Defeat authority

The study has a predeclared process that can reduce, absorb, replace, or terminate the framework's comparative claim.

No gate may be waived solely by framework authors.

---

## 10. Dissolution and narrowing triggers

The framework's comparative claim should be narrowed, absorbed, or rejected when:

1. a mature method or minimal augmentation matches performance with lower cost;
2. independent reconstruction is below the preregistered usable threshold;
3. consequential validity depends on author arbitration;
4. gains disappear on independently authored cases;
5. adjudication outcomes change substantially across reasonable panels;
6. the method wins mainly through generalized abstention;
7. comparator stewards document material weakening that cannot be corrected;
8. loss-weight changes reverse the conclusion across most plausible regions;
9. case construction repeatedly requires framework vocabulary;
10. the evaluation authority structure cannot prevent role capture;
11. complexity exceeds avoided governance loss in the tested domains;
12. equivalent established vocabulary explains all observed benefits.

Possible retained statuses include:

- pedagogical decomposition;
- synthesis or translation layer;
- domain-limited governance method;
- assurance checklist;
- no demonstrated operational advantage.

Dissolution of a superiority claim does not require deletion of useful descriptive artifacts.

---

## 11. Current blocker hierarchy

Before external recruitment, the blockers are:

| Blocker | Current severity | Required artifact or action |
|---|---:|---|
| Evaluation-role separation | Very high | Named role matrix, conflicts, appeal path |
| Comparator-family specification | Very high | Method-steward manuals and minimal augmentations |
| External adjudication criteria | Very high | Plural latent consequence records |
| Independent case authorship | High | Neutral authoring brief and candidate cases |
| Pilot reconstruction materials | High | Frozen specifications and three pilot cases |
| Participant recruitment | Medium | Cohort and sample plan |
| Benchmark harness | Low | Data capture and randomization tooling |
| Statistical execution | Low | Preregistered analysis code |

The main bottleneck is therefore:

\[
\boxed{
\text{freeze a fair evaluation substrate without allowing the framework to author its own victory conditions.}
}
\]

---

## 12. Charter self-application

This charter is also provisional.

It should be revised or replaced when:

- comparator experts identify unfair constraints;
- domain experts find the case-authority model unrealistic;
- adjudicators cannot apply its categories reliably;
- role separation is infeasible at the available scale;
- the charter's overhead exceeds the value of the pilot;
- a simpler research-governance standard provides equivalent protection.

The charter earns no special authority because it is meta-level.

---

## Final invariant

\[
\boxed{
\text{The evaluation earns authority only when no single interested party controls the cases, comparators, criteria, adjudication, and interpretation through which the framework is judged.}
}

Operational compression:

\[
\boxed{
\text{Separate powers. Strengthen rivals. Score consequences. Preserve disagreement. Pilot reconstruction. Permit absorption.}
\]
