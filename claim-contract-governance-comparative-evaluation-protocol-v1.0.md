# Claim Contract Governance Comparative Evaluation Protocol v1.0

## Status

This document specifies a comparative evaluation protocol for the evidential-update governance kernel.

It is not:

- benchmark v0.6;
- a completed experiment;
- an independent preregistration;
- evidence that claim contracts outperform existing methods;
- a human-subject study approval;
- a universal scoring rule for epistemic quality.

No participants have been recruited and no comparative data have been collected.

Before execution, the study materials, primary endpoints, exclusion rules, analysis plan, sample-size justification, governance-loss sensitivity analysis, and stopping conditions must be independently reviewed and preregistered. Any human-participant implementation requires the applicable ethics review, consent, privacy, and data-governance procedures.

The protocol tests the distinction left open by Claim Contract Governance Benchmark v0.5:

\[
\boxed{
\text{representational sufficiency}
\neq
\text{comparative operational advantage}.
}
\]

---

## 1. Research questions

### Primary question

\[
\boxed{
\text{Does explicit claim-contract representation improve governance of epistemic updates relative to established representations?}
}
\]

### Complexity-adjusted question

\[
\boxed{
\text{Does any improvement justify the additional representational, training, coordination, and implementation cost?}
}
\]

### Transfer question

\[
\boxed{
\text{Does any advantage survive independently authored cases and domains not used to construct the framework?}
}
\]

### Reconstruction question

\[
\boxed{
\text{Can independent users reconstruct claim contracts with sufficient structural agreement for the representation to function as a shared method rather than a private ontology?}
}
\]

---

## 2. Representations under comparison

The comparison must not be:

\[
\text{claim contract}
\quad\text{versus}\quad
\text{unstructured judgment}.
\]

It must include mature alternatives implemented in forms their knowledgeable proponents consider faithful and competitive.

### Condition A — Bayesian model comparison and decision

A minimal state may include:

\[
(\mathcal H,P(H),P(E\mid H),D,L),
\]

where \(D\) is a decision rule and \(L\) is the relevant loss.

The frozen implementation may use hierarchical models, posterior predictive checks, model averaging, abstention, and validity domains when those are part of the selected method.

The Bayesian condition must not be artificially prohibited from representing scope, model misspecification, or decision costs if a mature implementation would ordinarily include them.

### Condition B — AGM-style belief revision

A minimal state may include:

\[
(K,*),
\]

where \(K\) is a belief set and \(*\) is a revision operator.

The implementation may include entrenchment, contraction, revision, and explicit inconsistency handling.

### Condition C — Safety case or assurance argument

A minimal state may include:

\[
\text{Claim}
\rightarrow
\text{Argument}
\rightarrow
\text{Evidence},
\]

with assumptions, contexts, defeaters, evidence traceability, and review status represented according to the selected assurance method.

### Condition D — Causal model and intervention representation

A minimal state may include:

\[
G=(V,E),
\]

with observational and interventional distributions, latent-variable assumptions, and model criticism represented according to the selected causal method.

### Condition E — Claim contract

The proposed state is:

\[
\boxed{
C=(H,W,\Sigma,\Pi,\mathcal R,\Gamma),
}
\]

with an unresolved state \(H_{?}\) available when the represented hypothesis set may be incomplete.

The associated evidential pipeline is:

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

### Condition F — Strongest equivalent hybrid

An adversarial equivalence condition should combine mature existing components sufficient to represent:

- uncertainty;
- validity domain;
- provenance and shared dependency;
- defeaters or reopening triggers;
- action thresholds;
- revision rules;
- decision costs.

This condition tests whether claim-contract vocabulary adds operational value beyond equivalent state encoded through established methods.

If Condition F reproduces every claimed benefit with equal or lower complexity, the correct conclusion is absorption or synthesis rather than formal superiority.

---

## 3. Fair-comparison constraints

### Native-strength rule

Each representation must be specified or reviewed by researchers competent in that method.

No condition may be reduced to a deliberately weak textbook caricature.

### Equal-information rule

Every condition receives the same raw case information, evidence sequence, action options, time horizon, and externally available tools.

### Equivalent-training rule

Training materials should be matched as far as practical for:

- word count;
- study time;
- number and difficulty of concepts;
- worked-example count in trained cohorts;
- practice opportunities;
- software support.

The primary blind-reconstruction cohort receives no worked examples.

### Frozen-schema rule

Each representation schema, manual, allowed extensions, and response format must be frozen before outcome data are inspected.

### No-vocabulary-leakage rule

Neutral cases and scoring prompts must not contain framework-specific diagnostic labels such as:

- scope error;
- epistemic topology;
- dependency collapse;
- operational reopenability;
- authority laundering;
- claim contract.

Cases should describe events, evidence, decisions, and constraints rather than naming the intended failure class.

### Blinded-evaluation rule

Outcome raters must be blinded to:

- representation condition;
- participant identity;
- framework authorship;
- preferred hypothesis;
- expected winner.

Where response format makes full blinding impossible, the residual identification risk must be recorded.

### Non-absorption rule

Claim contracts receive no credit for distinctions that a comparator already represents equivalently.

The question is not whether existing methods can be renamed in claim-contract notation.

It is whether the representation changes correction behavior, reliability, transfer, or cost.

---

## 4. Neutral case construction

### Independent authoring

The primary transfer cases must be written by domain experts who did not author the claim-contract framework or v0.1–v0.5.

Case authors receive a neutral construction brief specifying that cases should contain sequential evidence, uncertain generalization, possible dependency, and consequential decisions without using the framework vocabulary.

### Domain families

The primary suite should include independently authored cases from at least four distinct families, such as:

- medical evidence and deployment;
- engineering safety and assurance;
- scientific replication and measurement;
- finance or risk management;
- AI evaluation and deployment;
- institutional policy under delayed feedback.

The exact domains must be frozen before participant assignment.

### Sequential evidence

Each case should unfold in stages:

\[
E_0
\rightarrow
E_1
\rightarrow
E_2
\rightarrow
\cdots
\rightarrow
E_k.
\]

At each stage participants record:

- current claim state;
- permitted actions;
- confidence or authority;
- retained valid structure;
- unresolved alternatives;
- requested next evidence;
- conditions for later revision.

### Latent adjudication record

Before participant responses are collected, case authors and an independent adjudication panel must freeze a scoring record containing:

- which conclusions are locally warranted;
- which scopes are supported;
- which evidence paths share dependencies;
- which actions are valid under the declared stakes;
- which conclusions remain unresolved;
- which later evidence should reopen or contract commitments;
- which valid claims should survive contradiction;
- acceptable alternative analyses.

The latent record must not assume claim-contract terminology.

### Positive and negative controls

The case suite must contain:

- local effects that should not generalize;
- genuine broad effects that should generalize;
- transfer failures that preserve local validity;
- omitted-model residuals;
- independent replications;
- correlated confirmations;
- formally stated but unreachable falsifiers;
- reachable reopening events;
- low-stakes reversible decisions where simple representations should be sufficient;
- high-stakes or irreversible decisions where correction access matters.

A representation that applies maximal complexity everywhere should be penalized.

### Adversarial case balance

Proponents of each comparator should be allowed to submit candidate cases expected to expose weaknesses in the claim-contract condition.

The final suite should be selected without knowledge of pilot outcomes.

---

## 5. Study phases

### Phase 0 — Independent protocol and material audit

Before recruitment:

1. comparator experts review the fairness of each representation;
2. domain experts review case realism;
3. methodologists review scoring and analysis;
4. the full protocol and materials are preregistered;
5. software and scoring code are frozen;
6. a negative-result ledger is opened before data collection.

### Phase 1 — Blind reconstruction

Independent participants receive:

- the formal specification of one representation;
- a neutral case;
- no repository access;
- no benchmark code;
- no worked examples.

They construct the representation from the case.

For the claim-contract condition this includes, where applicable:

\[
(H,W,\Sigma,\Pi,\mathcal R,\Gamma).
\]

The goal is not task performance alone.

It is whether the representation can be reconstructed consistently by strangers.

### Phase 2 — Trained comparative application

Participants are stratified by relevant expertise and randomly assigned to one representation condition.

A between-subject primary design is preferred to reduce conceptual carryover.

Participants receive matched training and then solve multiple cases in randomized order.

### Phase 3 — Sequential contradiction and reopening

Cases deliver new evidence after the initial commitment.

The study measures whether participants:

- localize the failure;
- contract authority without erasing unaffected valid structure;
- revise scope appropriately;
- request independent evidence;
- recognize omitted hypotheses;
- distinguish formal from operational correction access;
- respond materially to a valid reopening event;
- avoid reopening when expected correction value is below cost.

### Phase 4 — Held-out domain transfer

Participants apply the representation to domains absent from training materials.

Held-out cases must be independently authored and unavailable during framework construction, piloting, and training.

### Phase 5 — Delayed re-evaluation

Where feasible, a delayed session tests:

- retention of the representation;
- reconstruction drift;
- whether scope and reopening records remain usable;
- whether complexity costs decline with familiarity;
- whether later narrative changes the original claim state.

---

## 6. Participant structure

The protocol may use several cohorts.

### Domain-expert cohort

Participants have substantive expertise in one case domain.

### Methods-expert cohort

Participants have expertise in Bayesian inference, belief revision, causal inference, assurance cases, or related methods.

### General research cohort

Participants have research training but no deep commitment to one representation.

### Automated-system cohort

A separate extension may evaluate software or language-model agents under frozen prompts and tools.

Automated results must not be pooled with human results without a declared measurement model.

### Sample size

No fixed sample size is asserted in this protocol draft.

The executed study must justify sample size through a preregistered power or precision analysis based on:

- the primary contrast;
- clustering by participant, case, and domain;
- multiplicity across representations;
- the minimum practically important effect;
- expected attrition and unusable reconstructions.

---

## 7. Outcome dimensions

The study should report an outcome vector rather than collapsing everything into one score.

### Error localization

Did the response identify the causal or governance layer requiring revision?

A shared neutral coding vocabulary may include:

\[
\{
\text{measurement},
\text{model},
\text{dependency},
\text{scope},
\text{authority},
\text{action},
\text{reopening},
\text{loss specification}
\}.
\]

Report macro-averaged precision, recall, and \(F_1\) across relevant labels.

### Valid structure retention

Let \(V^*\) be the set of claims that remain warranted after contradiction and \(\widehat V\) the set retained by the participant.

\[
\operatorname{Precision}_V
=
\frac{|\widehat V\cap V^*|}{|\widehat V|},
\]

\[
\operatorname{Recall}_V
=
\frac{|\widehat V\cap V^*|}{|V^*|}.
\]

This distinguishes selective correction from total rejection.

### Unsupported authority or action expansion

\[
O_G
=
\frac{\text{unsupported promoted commitments}}
{\text{promotion opportunities}}.
\]

### Under-generalization

Measure valid actions or transfers withheld despite adequate evidence.

This prevents a complexity-rich representation from winning through generalized abstention.

### Omitted-model handling

Measure whether unexplained residuals trigger:

- forced selection among represented hypotheses;
- appropriate uncertainty or abstention;
- hypothesis-expansion requests;
- unjustified invention.

### Dependency sensitivity

Measure whether repeated evidence from one generator receives less incremental authority than genuinely independent evidence.

### Recovery latency

For a valid reopening event:

\[
\tau_R
=
\text{steps or time until the commitment reaches its appropriate revised state}.
\]

Latency must be paired with revision quality; immediate indiscriminate rejection is not successful recovery.

### Action quality

Where cases support objective action scoring, record expected or realized domain loss.

Probability-based conditions may report calibration metrics such as Brier or log score when native to the task.

Non-probabilistic conditions should not be forced into artificial probability reports solely to fit one comparator.

### Operational reopening

Measure whether the response records a correction path that is:

1. relevant;
2. realistically obtainable;
3. measurable;
4. capable of reaching the revision mechanism;
5. capable of producing a material update;
6. connected to revision or replacement authority.

### Complexity and adoption cost

At minimum record:

- training time;
- task completion time;
- representation size;
- number of required fields or nodes;
- software or annotation effort;
- participant-reported cognitive load;
- correction and review time;
- inter-rater disagreement;
- missing or malformed fields;
- delayed retention.

No performance claim is complete without these costs.

---

## 8. Blind reconstruction metrics

### Field completion

Measure whether participants independently instantiate the required objects without examples.

### Structural agreement

For categorical fields, report an appropriate agreement measure such as Krippendorff's \(\alpha\) or Fleiss' \(\kappa\), with uncertainty intervals.

For continuous authority values, report an intraclass correlation or another preregistered agreement statistic.

For dependency graphs, report a preregistered structural measure such as edge-set precision and recall or graph-edit distance.

For scope maps, compare agreement over:

- population or system class;
- target;
- conditions;
- time horizon;
- permitted action.

### Private-ontology failure

A representation exhibits a private-ontology failure when:

\[
\text{task expressiveness}\uparrow
\quad\text{but}\quad
\text{independent reconstruction reliability}\downarrow
\]

below a preregistered usable threshold.

High descriptive richness with unstable reconstruction does not count as shared operational improvement.

---

## 9. Governance loss and complexity adjustment

The study must not hide tradeoffs inside one evaluator-selected scalar.

Report the full outcome vector first.

A declared local governance loss may then be used:

\[
\Lambda
=
\sum_k\lambda_kL_k.
\]

Candidate components include:

- overgeneralization;
- undergeneralization;
- premature certainty;
- excessive skepticism;
- invalid irreversible commitment;
- unnecessary reopening;
- governance complexity.

### Sensitivity analysis

The preferred representation must be recomputed over a preregistered range of plausible \(\lambda_k\) values.

Report:

- regions of loss-weight space where each representation is preferred;
- whether ranking depends on one dominant weight;
- Pareto frontiers for performance versus complexity;
- domain-specific rather than universal optima.

### Net comparative utility

A representation supports comparative advantage only when:

\[
\Delta L_{\mathrm{avoided}}
>
\Delta C_{\mathrm{representation}}
\]

under a declared domain loss and uncertainty model.

No universal complexity conversion rate is assumed.

---

## 10. Analysis plan

The final analysis plan must be frozen before outcome inspection.

A suitable primary analysis may use a hierarchical model with random effects for:

- participant;
- case;
- domain;
- authoring source;
- representation condition where appropriate.

The protocol should predeclare:

- one primary endpoint or primary outcome vector;
- the primary comparator;
- superiority or non-inferiority margins;
- multiplicity control;
- treatment of missing responses;
- exclusion criteria;
- minimum reconstruction quality;
- handling of timeouts;
- framework-expertise covariates;
- sensitivity to alternative adjudication labels;
- robustness to governance-loss weights.

Exploratory analyses must be labeled separately.

### Primary comparison

The strongest primary contrast is:

\[
\text{claim contract}
\quad\text{versus}\quad
\text{best-performing mature or hybrid alternative},
\]

not claim contract versus the weakest baseline.

### Reporting

Report:

- absolute performance;
- effect sizes with uncertainty intervals;
- complexity-adjusted and unadjusted results;
- reconstruction reliability;
- domain heterogeneity;
- participant-expertise interactions;
- all preregistered negative outcomes;
- failures of blinding or material equivalence.

---

## 11. Precommitted interpretation outcomes

### Outcome 1 — Independent comparative value

\[
\text{performance}_{\mathrm{contract}}
-
\text{performance}_{\mathrm{best\ alternative}}
>
\delta
\]

and:

\[
\text{complexity-adjusted advantage}>0
\]

across independently authored held-out cases.

Interpretation:

> Evidence that explicit claim contracts add operational value under the tested populations, domains, and governance losses.

The scope remains local to those conditions.

### Outcome 2 — Performance equivalence with greater cost

\[
\text{performance}_{\mathrm{contract}}
\approx
\text{performance}_{\mathrm{best\ alternative}}
\]

and:

\[
C_{\mathrm{contract}}>C_{\mathrm{best\ alternative}}.
\]

Interpretation:

> Claim contracts are a possible synthesis or notation layer, not a superior operational formalism under the tested conditions.

### Outcome 3 — Greater expressiveness with low reconstruction reliability

\[
\text{represented distinctions}\uparrow
\quad\land\quad
A_s\downarrow.
\]

Interpretation:

> Private-ontology or training-dependence problem. The representation may be internally coherent but not reliably shareable.

### Outcome 4 — No advantage and higher cost

\[
\text{performance}_{\mathrm{contract}}
\leq
\text{performance}_{\mathrm{best\ alternative}}+\epsilon
\]

and:

\[
C_{\mathrm{contract}}>C_{\mathrm{best\ alternative}}.
\]

Interpretation:

> Evidence against operational advantage. Retain only descriptive or pedagogical claims that remain supported.

### Outcome 5 — Mature alternative dominates

\[
\text{performance}_{\mathrm{alternative}}
>
\text{performance}_{\mathrm{contract}}+\delta
\]

with equal or lower cost.

Interpretation:

> Reduce, replace, or absorb the claim-contract architecture into the superior alternative.

### Outcome 6 — Domain-conditional advantage

The claim contract wins only in cases with high stakes, scope uncertainty, common-mode dependence, or costly reopening, while simpler representations win in stable reversible domains.

Interpretation:

> Scope the method to case classes where avoided governance loss exceeds complexity cost.

### Outcome 7 — Authoring dependence

The claim contract wins on framework-authored cases but not independently authored cases.

Interpretation:

> Evidence of benchmark ontology leakage rather than transferred operational value.

---

## 12. Falsification conditions

The claim of independent operational value should lose authority when any of the following occurs:

1. a mature or hybrid alternative reproduces the same correction behavior with lower cost;
2. performance gains disappear on independently authored cases;
3. gains require framework-specific vocabulary in the case prompt;
4. independent users cannot reconstruct the contract reliably;
5. the method wins only under a narrow evaluator-selected loss vector;
6. complexity costs exceed avoided governance loss;
7. abstention or generalized skepticism explains the apparent improvement;
8. outcome raters can infer condition and favor the proposed representation;
9. case labels encode the claim-contract ontology rather than domain-correct behavior;
10. equivalent information is withheld from comparator conditions.

The protocol itself should be revised or rejected if these failures cannot be prevented or measured.

---

## 13. Minimal medical-AI case pattern

The following is only an illustration of neutral case structure, not a final study item.

A diagnostic model achieves high accuracy in one hospital.

Two validation studies report similar performance.

Deployment in a second hospital performs poorly.

Later investigation shows that all development and validation datasets used one preprocessing pipeline.

The original local result remains reproducible under its original conditions.

Participants decide:

- which conclusions remain warranted;
- whether deployment should continue in either hospital;
- which evidence changed confidence;
- which new study would be most valuable;
- what result would permit renewed deployment;
- what should happen if the new evidence is unavailable.

The prompt does not name scope, common-mode dependence, authority, or reopening.

---

## 14. Reproducibility and governance

An executed study should publish, subject to ethics and privacy constraints:

- preregistration;
- frozen representation manuals;
- neutral cases and staged evidence;
- adjudication records;
- scoring code;
- anonymized responses where permitted;
- analysis code;
- deviations from protocol;
- negative-result ledger;
- complexity and training measurements;
- all sensitivity analyses;
- failed cases and unresolved disagreements.

Framework authors should not be the sole adjudicators of framework performance.

Independent replication should precede any claim of general comparative superiority.

---

## 15. Claim boundary

A positive study could support only a claim of the form:

> Under the tested participants, domains, cases, training conditions, action stakes, comparator implementations, and governance losses, explicit claim contracts improved specified correction outcomes by a measured amount at a measured complexity cost.

It would not establish:

- universal rational superiority;
- one correct representation of scientific claims;
- autonomous discovery of hypotheses, scopes, dependencies, losses, or reopening rules;
- that claim-contract vocabulary is necessary rather than one implementation of equivalent information;
- transfer to populations, domains, or stakes not tested;
- a general theory of intelligence.

A null or negative result should reduce the framework's authority according to the same scope discipline.

---

## Final comparison invariant

\[
\boxed{
\text{The claim-contract architecture earns independent authority only if it improves correction behavior on neutral, externally authored tasks relative to the strongest fair alternatives after complexity cost.}
\]

Operational compression:

\[
\boxed{
\text{Blind the ontology. Strengthen the alternatives. Measure correction. Charge complexity. Test transfer. Permit defeat.}
\]
