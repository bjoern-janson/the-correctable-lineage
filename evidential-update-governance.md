# Evidential Update Governance

## Status

This document states a methodological kernel shared by the corpus's interface, authority, provenance, correction-path, temporal, and altered-state discussions.

It is a proposal for governing inference from observations to hypotheses.

It is not a universal theory of cognition, a replacement for Bayesian inference or causal inference, a validated scalar of rationality, or evidence for any historical, psychological, psychedelic, or metaphysical interpretation.

Its purpose is narrower:

\[
\boxed{
\text{Specify what an observation is allowed to change, why, by how much, and under what reopening conditions.}
}
\]

---

## 1. Minimal kernel

Let:

- \(O_t\): an observation or recorded event;
- \(\Phi_t\): the measurement or feature-extraction interface;
- \(F_t=\Phi_t(O_t)\): the extracted features used as evidence;
- \(\mathcal H_t=\{H_1,\ldots,H_n,H_{?}\}\): competing hypotheses, including an explicit unresolved or omitted-model state;
- \(T_t\): the discrimination contract specifying how possible observations bear differently on the hypotheses;
- \(\Pi_t\): provenance and dependency structure of the evidence and correction paths;
- \(W_t\): current operational authority assigned to the hypotheses;
- \(\mathcal R_t\): conditions under which each hypothesis must be reopened;
- \(\Gamma_t\): the admissible revision response under those conditions.

The observation pipeline is:

\[
O_t
\xrightarrow{\Phi_t}
F_t.
\]

The evidential update is:

\[
\boxed{
(\Delta W_t,\Delta\Gamma_t)
=
U_t(F_t,\mathcal H_t,T_t,\Pi_t,W_t,\mathcal R_t,\Gamma_t).
}
\]

\(U_t\) is the update operator.

It does not merely ask whether an observation is impressive, coherent, vivid, repeated, or useful.

It asks:

1. which hypothesis dimensions the measured feature can discriminate;
2. whether the evidence adds an independent correction path;
3. what update magnitude is justified;
4. what domain and scope the update applies to;
5. what future evidence must still be able to reduce the resulting authority.

The authority vector \(W_t\) need not always be interpreted as a normalized probability distribution.

Depending on the application, it may represent:

- credence;
- operational trust;
- deployment weight;
- evidential status;
- permission to inherit or act.

The meaning of \(W\) must be declared before comparison.

---

## 2. Three ledgers

The framework separates three records that are commonly collapsed.

### Observation and measurement ledger

\[
\mathcal L_O=(O_t,\Phi_t,F_t).
\]

This records:

- what occurred or was reported;
- how it was measured;
- which features were extracted;
- which distinctions the measurement interface could not preserve.

It answers:

> What was observed, and through what interface?

### Justification and discrimination ledger

\[
\mathcal L_J=(\mathcal H_t,T_t,\Pi_t,J_t).
\]

Here \(J_t\) records the proposed evidential edges:

\[
F_k\rightsquigarrow H_i.
\]

This ledger asks:

- which hypotheses were compared;
- what each hypothesis predicted;
- which feature supposedly favored or disfavored each hypothesis;
- whether the evidence path was independent or shared a hidden dependency;
- which result would reduce the preferred hypothesis's authority.

It answers:

> Why is this observation being treated as evidence for that hypothesis?

### Authority and correctability ledger

\[
\mathcal L_W=(W_t,\mathcal R_t,\Gamma_t).
\]

This records:

- current authority;
- reopening conditions;
- permitted update magnitude and direction;
- unresolved uncertainty;
- whether the claim can still be challenged through realistically reachable evidence.

It answers:

> What changed, and what could still change it back?

The no-collapse rule is:

\[
\boxed{
\mathcal L_O
\neq
\mathcal L_J
\neq
\mathcal L_W.
}
\]

An experience is not its interpretation.

An interpretation is not its justification.

A justification is not automatically sufficient to authorize a large or global update.

---

## 3. Application contract

An application is not governed inference until it declares all of the following.

### Competing hypotheses

\[
\mathcal H=\{H_1,H_2,\ldots,H_n,H_{?}\}.
\]

The preferred explanation cannot be evaluated only against an unspecified null.

An unresolved state \(H_{?}\) prevents forced choice among an incomplete hypothesis set.

### Operational measurements

The application must state how raw observations become features:

\[
F=\Phi(O).
\]

Examples include:

- target accuracy;
- prediction residuals;
- reported presence;
- source certainty;
- intervention outcomes;
- error agreement between correction channels.

### Discrimination contract

For each material hypothesis pair, state at least one observation expected to separate them:

\[
T_{ij}:F\mapsto
\text{relative support for }H_i\text{ versus }H_j.
\]

### Negative update condition

The application must predeclare a result that would reduce the preferred hypothesis's authority:

\[
F^{-}_i
\Rightarrow
\Delta W(H_i)<0.
\]

Without this, the interpretation lacks a defined correction path.

### Provenance and dependency map

The application must state whether apparently separate observations share:

- one instrument;
- one dataset;
- one participant;
- one generative process;
- one evaluator;
- one preprocessing pipeline;
- one cultural or institutional prior;
- one hidden causal dependency.

### Scope contract

Every update must name its valid domain:

\[
\mathcal D_i=(\text{class},\text{target},\text{interface},\text{conditions},\text{time horizon}).
\]

### Reopening path

The claim must preserve at least one realistically reachable route by which its authority can decrease.

If any of these objects is absent, the result may remain a useful interpretation, but it has not yet entered the governed update architecture.

---

## 4. Update gates

A legitimate update passes through several non-substitutable gates.

### Gate 1 — Measurement validity

Does \(\Phi\) preserve the distinction the feature claims to measure?

\[
L=\widehat L\circ\Phi
\]

over the declared class, when factorization is the appropriate criterion.

A persuasive feature extracted from an insufficient interface cannot identify the target.

### Gate 2 — Hypothesis relevance

Could the feature differ under the competing hypotheses?

If every candidate hypothesis predicts the observation equally well, then:

\[
\Delta W\approx0.
\]

### Gate 3 — Discriminating power

Does the observed result favor one hypothesis over another under the declared test?

Confirmation of a prediction shared by all hypotheses is not discriminating evidence.

### Gate 4 — Correction-path independence

Does the evidence add a genuinely new route through which the hypothesis could fail?

Correlated confirmations must not be counted as independent replications.

### Gate 5 — Magnitude calibration

The update depth must be proportional to:

- evidential strength;
- independence;
- measurement quality;
- model coverage;
- transfer evidence;
- consequence of error;
- reversibility of the resulting action.

No universal scalar is currently validated for combining these terms.

### Gate 6 — Scope locality

Evidence may update only the dimensions it identifies.

\[
\boxed{
\text{local evidence}
\not\Rightarrow
\text{global authority}.
}
\]

### Gate 7 — Reopening preservation

The update must not eliminate the correction paths needed to challenge it later.

A claim that becomes operationally unrevisable after one success has converted evidence into constitutional immunity.

---

## 5. Confidence and correctability

Confidence is not correctability.

For each hypothesis, retain:

\[
C_i=
(H_i,W_i,\mathcal R_i,\Gamma_i,\mathcal D_i,\mathcal L_i),
\]

where:

- \(H_i\): hypothesis content;
- \(W_i\): current authority;
- \(\mathcal R_i\): reopening conditions;
- \(\Gamma_i\): response to evidence within those conditions;
- \(\mathcal D_i\): demonstrated domain;
- \(\mathcal L_i\): known limits and unresolved alternatives.

A high-authority claim may remain highly correctable when:

- its reopening conditions are explicit;
- the relevant evidence is realistically obtainable;
- contradictory evidence can propagate to authority;
- the update response is not capped near zero;
- the institution or system permits replacement.

A low-authority claim may still be structurally insulated when:

- no possible observation counts against it;
- every contradiction is reclassified as confirmation;
- the required evidence is impossible to collect;
- the update operator is controlled by the defended hypothesis;
- revision is verbally permitted but operationally blocked.

Thus:

\[
\boxed{
\text{correctability}
\neq
1-W.
}
\]

A useful local question is:

> Which specified evidence class can reduce this hypothesis's authority, and can that evidence actually reach the update mechanism?

---

## 6. Benchmark interpretation

The four toy benchmarks probe different failure points in \(U\).

### v0.1 — Interface sufficiency

Can the system recognize that additional model optimization cannot recover a distinction erased by \(\Phi\) or \(O\)?

The relevant failure is upstream of ordinary belief updating.

### v0.2 — Challenge allocation

Can the system decide that apparent success is insufficient and purchase a supplied discrimination test before deployment?

This probes when \(U\) should seek additional evidence rather than update from the existing sample.

### v0.3 — Correction-path dependence

Can \(U\) value failure-conditioned correction coverage over marginal agreement or correlated vote count?

This probes \(\Pi\): whether evidence channels provide distinct opportunities for contradiction.

### v0.4 — Common-mode intervention

Can a supplied intervention change the support of a hidden upstream cause and reveal that the entire correction ecosystem fails together?

This probes whether \(T\) and \(\Pi\) remain valid outside ordinary calibration.

### Open frontier

The unimplemented problem is not merely another update over fixed objects.

It is whether the system can revise the objects governing update itself:

\[
(\Phi,\mathcal H,T,\Pi,U)
\rightarrow
(\Phi',\mathcal H',T',\Pi',U').
\]

That includes:

- generating omitted hypotheses;
- inventing measurements;
- designing interventions;
- identifying dependencies absent from the supplied causal model;
- discovering that the update rule itself protects a preferred conclusion.

No current benchmark establishes those capabilities.

---

## 7. Altered-state example

The DMT/entity discussion can be represented without granting authority to any source ontology.

### Observation ledger

\[
O=\text{participant report}.
\]

A provisional feature decomposition might include:

\[
F=(R,S,B,P,A,C,Q,X),
\]

where:

- \(R\): modality-specific rendering;
- \(S\): spatial organization;
- \(B\): embodiment;
- \(P\): sensed presence;
- \(A\): attributed agency;
- \(C\): apparent communication;
- \(Q\): emotional salience;
- \(X\): felt externality.

This is a measurement decomposition, not a discovered causal ontology.

### Hypothesis ledger

\[
\mathcal H=
\{
H_{\mathrm{external}},
H_{\mathrm{internal}},
H_{\mathrm{generator}},
H_{\mathrm{mixed}},
H_{?}
\}.
\]

### Candidate discrimination tests

Examples include:

- developmental comparison across congenital, early, late blindness, and sighted controls;
- immediate versus delayed reconstruction of phenomenology and source certainty;
- preregistered externally hidden targets with blinded scoring;
- manipulations that separate modality-specific rendering from agency or communication reports.

These tests update different dimensions.

A congenital-blindness result may update hypotheses about modality dependence.

It cannot by itself identify an external source.

A vivid or transformative experience may update phenomenological validity.

It cannot by itself identify telepathic transfer.

The governing rule remains:

\[
\boxed{
\text{Each surviving component updates only the hypothesis dimension the test can discriminate.}
}
\]

---

## 8. Preventing infinite meta-regression

The existence of possible failure in every test does not imply endless testing.

Meta-level status grants no special authority, but bounded systems still require stopping rules.

A provisional stopping condition is:

\[
\operatorname{EVI}_{\perp}(T_{k+1})
\leq
C(T_{k+1})+C_{\mathrm{delay}},
\]

where \(\operatorname{EVI}_{\perp}\) is the expected value of genuinely independent information rather than repeated correlated confirmation.

Stopping is justified only when:

- residual uncertainty is recorded rather than erased;
- the action's reversibility and stakes are declared;
- no known unresolved common-mode dependency exceeds the accepted risk threshold;
- the next available test adds insufficient independent correction value relative to its cost;
- reopening conditions remain attached to the resulting commitment.

The system stops because the marginal independent correction value is insufficient under a declared objective—not because the current meta-level has become infallible.

---

## 9. Characteristic failure modes

### Measurement laundering

A feature is treated as if it directly represented the target despite an unvalidated extraction interface.

### Hypothesis closure

The preferred explanation is compared only against a weak or unspecified alternative.

### Evidential-edge laundering

A feature correlated with a claim is treated as if it identified the claim's mechanism or source.

### Correlated confirmation

Multiple outputs from one generative process are counted as independent evidence.

### Authority spillover

Evidence for one dimension increases authority over provenance, mechanism, transfer, desirability, or deployment without a discriminating path.

### Update capture

The defended hypothesis controls what is measured, which contradictions count, and how strongly they may revise authority.

### Correctability theatre

A claim nominally permits challenge while its reopening conditions are impossible, inaccessible, or institutionally blocked.

### Interpretation rewritten as observation

A later narrative is entered into the record as though it were the original event.

### Universalization by vocabulary

The same abstract terms are applied across domains without naming domain-specific hypotheses, tests, negative results, or scope boundaries.

---

## 10. Claim boundary

This kernel is compatible with and partly restates concerns already formalized in:

- Bayesian model comparison;
- falsification and severe testing;
- causal inference;
- measurement theory;
- active experiment design;
- robust decision theory;
- source monitoring;
- provenance and reproducibility practice.

The vocabulary earns separate authority only where it creates useful discriminations, improves error localization, or prevents unsupported authority transfer better than existing formulations.

It does not establish that one update operator governs all cognition or science.

It does not establish a universal metric of evidence, independence, confidence, or correctability.

It does not eliminate judgment in selecting hypotheses, features, interventions, costs, or acceptable risk.

---

## 11. Operational protocol

Before allowing an observation to change authority, record:

1. **Observation** — What occurred or was reported?
2. **Measurement** — How was it converted into features?
3. **Alternatives** — Which hypotheses are genuinely competing?
4. **Discrimination** — Which result separates them?
5. **Negative result** — What would reduce the preferred hypothesis's authority?
6. **Dependency** — Which evidence paths share a generator or failure mode?
7. **Magnitude** — How large and deep may the update be?
8. **Scope** — Where does the update apply, and where does it not?
9. **Reopening** — What future evidence triggers revalidation?
10. **Replacement** — Can the measurement, hypothesis set, test, or update rule itself be revised?

Without this structure:

\[
\text{observation}
\rightarrow
\text{interpretation}
\rightarrow
\text{authority}
\]

can become an uninspected authority-laundering path.

With it:

\[
\boxed{
O
\rightarrow
F
\rightarrow
\mathcal H
\rightarrow
T
\rightarrow
\Pi
\rightarrow
\Delta W
\rightarrow
(\mathcal R,\Gamma).
}
\]

---

## Final compression

The corpus's broad methodological constraint is:

\[
\boxed{
\text{Every application must name the competing hypotheses, the discriminating observation, and the result that would reduce its preferred hypothesis's authority.}
}
\]

The corresponding update invariant is:

\[
\boxed{
\text{An observation may change authority only through a declared, discriminating, dependency-aware, scope-bounded, and reopenable evidential path.}
}
\]
