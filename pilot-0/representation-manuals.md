# Pilot 0 Representation Manuals

## Status and fairness boundary

These are draft participant manuals for feasibility testing.

They are not yet approved as method-faithful by independent comparator stewards.

Before execution:

- a Bayesian-method steward must review Condition B;
- an assurance-method steward must review Condition C;
- a framework-independent reviewer must compare information access and training burden;
- word count, study time, examples, response fields, and software support must be matched as far as practical.

Participants receive only the manual for their assigned condition plus the common response template.

All conditions receive identical case evidence and action options.

---

# Common task instruction

At each evidence stage:

1. represent the current state of the case using your assigned method;
2. state which conclusions remain supported, weakened, unresolved, or rejected;
3. state which actions are currently permitted, conditional, suspended, or prohibited;
4. identify the next evidence that would be most useful;
5. state what future result would materially change your conclusions or actions;
6. preserve earlier conclusions that remain justified;
7. record uncertainty and disagreement rather than forcing a unique answer.

You are not required to produce one global verdict.

---

# Condition A — Claim Contract

## Purpose

Represent each material commitment as an auditable record containing content, authority, validity limits, evidence dependencies, and future revision conditions.

## Core record

For each material claim \(H_i\), record:

\[
C_i=(H_i,W_i,\Sigma_i,\Pi_i,\mathcal R_i,\Gamma_i).
\]

### \(H_i\) — Claim

State one proposition clearly enough that it could be supported, narrowed, or rejected separately.

Avoid combining:

- result validity;
- causal explanation;
- transfer;
- action authorization;
- desirability.

### \(W_i\) — Current authority

State how strongly the current evidence supports using the claim for reasoning or action.

Pilot 0 uses ordinal authority unless a participant has a justified numerical model:

- 0 — rejected or contradicted;
- 1 — weak possibility;
- 2 — plausible but unresolved;
- 3 — locally supported;
- 4 — strongly supported within scope.

Authority is not required to sum to one across claims.

### \(\Sigma_i\) — Validity and action scope

Record:

- population, system, or case class;
- target or outcome;
- measurement conditions;
- operating conditions;
- time horizon;
- permitted action.

### \(\Pi_i\) — Evidence provenance and dependency

For each supporting item, record:

- source;
- measurement or processing path;
- whether it shares data, instruments, authors, assumptions, software, evaluators, or upstream causes with other evidence;
- whether it adds a materially independent correction path.

### \(\mathcal R_i\) — Reopening conditions

State realistically obtainable future evidence that would trigger re-examination.

A merely imaginable event is insufficient when it cannot be collected or reach decision-makers.

### \(\Gamma_i\) — Revision response

State what should happen if a reopening condition occurs:

- reduce authority;
- contract or expand scope;
- suspend an action;
- request a new hypothesis;
- replace a component;
- preserve unaffected local validity.

### \(H_{?}\) — Unresolved state

Use an unresolved state when the represented alternatives do not explain the evidence adequately.

Do not invent a detailed explanation without discriminating evidence.

## Allowed operations

At each stage you may:

- promote authority;
- contract authority;
- rescope a claim;
- add or split hypotheses;
- alter reopening rules;
- alter action permissions.

## Required output

Use the common response template.

---

# Condition B — Bayesian Workflow with Decision and Model Criticism

## Purpose

Represent uncertainty over competing models, update with evidence, evaluate predictive adequacy, and choose actions under explicit loss.

## Core record

Record:

\[
B=(\mathcal H,P(H),P(E\mid H),D,L,V,M).
\]

### \(\mathcal H\) — Model set

List competing models or explanations.

Include an open-model or misspecification state when the represented set may be incomplete.

### \(P(H)\) — Current model probability or weight

State prior or current relative support.

Exact numbers are optional in Pilot 0 when defensible likelihoods are unavailable. Ordinal probability ranges may be used, but uncertainty about the numbers must be recorded.

### \(P(E\mid H)\) — Evidence model

State how expected or surprising each new evidence item is under each model.

Distinguish:

- observations used to fit a model;
- observations used to evaluate it;
- evidence sharing data, software, instruments, or assumptions.

Do not multiply dependent evidence as if conditionally independent without justification.

### \(D\) — Decision rule

State which action is preferred given current uncertainty and loss.

Actions may include:

- deploy;
- restrict;
- monitor;
- collect evidence;
- suspend;
- reject;
- abstain.

### \(L\) — Local decision loss

Record stakeholders, time horizon, and consequence weights relevant to false promotion, false rejection, delay, monitoring burden, and irreversible action.

No universal loss is assumed.

### \(V\) — Validity domain

Record the populations, systems, measurements, operating conditions, and horizons over which the predictive model has been tested.

### \(M\) — Monitoring and model criticism

Record:

- posterior predictive checks or equivalent diagnostics;
- evidence that would signal misspecification;
- monitoring triggers;
- conditions for model expansion or replacement;
- consequences of failed transfer.

## Method-native augmentation

Condition B explicitly permits:

- hierarchical models;
- model averaging;
- posterior predictive checking;
- transport or subgroup structure;
- abstention;
- validity-domain metadata;
- monitoring triggers;
- decision thresholds;
- an open-model state.

These are not treated as claim-contract imports when they are expressed in Bayesian terms.

## Required output

Use the common response template and include enough of \(B\) to explain your action.

---

# Condition C — Assurance Argument with Defeaters and Monitoring

## Purpose

Construct an auditable argument connecting claims to evidence, assumptions, contexts, defeaters, and operational controls.

## Core record

Represent the case as:

\[
A=(C,G,E,X,D,M,Q).
\]

### \(C\) — Top-level and subordinate claims

State the exact claim being supported.

Separate claims about:

- performance;
- mechanism;
- transfer;
- system safety;
- deployment permission.

### \(G\) — Argument or strategy

Explain why the evidence supports the claim.

Decompose broad claims into subordinate claims when they depend on different evidence.

### \(E\) — Evidence

Record each evidence item and its provenance.

State whether evidence items share:

- data;
- test environments;
- software;
- instruments;
- assumptions;
- evaluators;
- failure modes.

### \(X\) — Context and validity domain

Record:

- system or population;
- operating conditions;
- measurement conditions;
- time horizon;
- permitted use;
- relevant stakeholder consequences.

### \(D\) — Defeaters and unresolved challenges

Record observations or arguments that could undermine:

- the evidence;
- the inference;
- an assumption;
- the scope;
- the action authorization.

Classify a defeater as:

- open;
- mitigated;
- resolved;
- accepted residual risk.

### \(M\) — Monitoring and recovery

Record:

- operational monitoring;
- evidence thresholds for reopening the assurance case;
- required action after a trigger;
- suspension and replacement conditions.

### \(Q\) — Confidence and decision status

State confidence in each major argument link and current action status:

- permitted;
- conditionally permitted;
- suspended;
- prohibited;
- unresolved.

## Method-native augmentation

Condition C explicitly permits:

- confidence arguments;
- defeaters;
- validity domains and contexts;
- monitoring requirements;
- surveillance evidence;
- assumption registers;
- change-impact analysis;
- conditional deployment.

These are native assurance tools, not treated as claim-contract imports.

## Required output

Use the common response template and include enough of the assurance structure to explain your action.

---

# Minimal sufficient augmentation audit

After Pilot 0, comparator stewards should identify the smallest method-native additions that produced useful behavior.

For each comparator \(M_j\), record:

\[
M_j^{+}
=
\text{minimal augmentation required for the observed correction behavior}.
\]

The audit asks:

1. Which distinctions were already native?
2. Which additions were needed?
3. Did the additions alter behavior or only documentation?
4. What training and coordination cost did they add?
5. Did claim-contract terminology provide any remaining advantage?

The conclusion may be:

- genuine abstraction gain;
- synthesis gain;
- pedagogical gain;
- equivalent method-native augmentation;
- no operational gain.

---

# Manual failure conditions

A manual must be revised before a larger study when:

- participants repeatedly request author interpretation;
- required fields have no stable operational meaning;
- one manual grants materially more case information;
- one comparator is prohibited from using mature native tools;
- outcome scorers can identify the condition from decorative vocabulary alone;
- training burden is not measured;
- participants cannot distinguish the representation from the common response template.
