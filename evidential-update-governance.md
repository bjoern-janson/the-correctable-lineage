# Evidential Update Governance

> **Historical formulation — superseded authority semantics**
>
> This document preserves an earlier corpus formulation in which \(W\), \(\Sigma\), and \(\Gamma\) may combine epistemic authority with operational trust, permission, deployment, rollback, or replacement. For current canonical semantics, use [research-core.md](research-core.md) and [research-claim-boundary.md](research-claim-boundary.md): \(W\) is typed epistemic authority, \(\Sigma\) records validity scope and action-class relevance, \(\Gamma\) records epistemic revision, and decision authority is determined separately under \(\Lambda\). Where this document conflicts, the current front-door documents control.

## Status

This document states a methodological kernel shared by the corpus's interface, authority, provenance, correction-path, temporal, benchmark, and altered-state discussions.

It governs inference from observations to hypotheses.

It is not:

- a universal theory of cognition;
- a replacement for Bayesian or causal inference;
- a validated scalar of rationality;
- a new benchmark result;
- evidence for any historical, psychological, psychedelic, or metaphysical interpretation.

Its purpose is narrower:

\[
\boxed{
\text{Specify what an observation may change, why, by how much, over what scope, and through which future correction paths.}
}
\]

---

## 1. Minimal kernel

Let:

- \(O_t\): an observation, event, report, or recorded outcome;
- \(\Phi_t\): the measurement or feature-extraction interface;
- \(F_t=\Phi_t(O_t)\): the extracted features admitted as evidence;
- \(\mathcal H_t=\{H_1,\ldots,H_n,H_{?}\}\): competing hypotheses, including an unresolved or omitted-model state;
- \(T_t\): the discrimination contract specifying how possible results bear differently on the hypotheses;
- \(\Pi_t\): provenance and shared-dependency structure of the evidence and correction paths;
- \(W_t\): current operational authority assigned to hypotheses or claim dimensions;
- \(\Sigma_t\): the scope map specifying where each authority assignment is valid;
- \(\mathcal R_t\): reopening conditions for each hypothesis;
- \(\Gamma_t\): the admissible response when reopening evidence occurs.

The observation pipeline is:

\[
O_t\xrightarrow{\Phi_t}F_t.
\]

The governed update is:

\[
\boxed{
(\Delta\mathcal H_t,\Delta W_t,\Delta\Sigma_t,\Delta\mathcal R_t,\Delta\Gamma_t)
=
U_t(F_t,\mathcal H_t,T_t,\Pi_t,W_t,\Sigma_t,\mathcal R_t,\Gamma_t).
}
\]

The update operator does not merely ask whether an observation is vivid, coherent, repeated, useful, surprising, or socially persuasive.

It asks:

1. which measured distinction is present;
2. which competing hypotheses that distinction can separate;
3. whether the evidential path adds independent corrective access;
4. whether authority should increase, decrease, or remain unresolved;
5. whether the hypothesis space itself must expand;
6. what scope the result has actually earned;
7. what future evidence must remain able to reopen the commitment.

The authority vector \(W\) need not always be a normalized probability distribution.

Depending on the application, it may represent:

- credence;
- operational trust;
- deployment weight;
- evidential status;
- permission to act;
- permission to inherit a mechanism or claim.

Its meaning must be declared before comparison.

---

## 2. Scope is part of the update

Authority without scope invites spillover.

For each hypothesis or claim dimension \(H_i\), define:

\[
\boxed{
\Sigma(H_i)=
(\mathcal F_i,L_i,O_i,C_i,\tau_i,A_i)
}
\]

where:

- \(\mathcal F_i\): demonstrated system or case class;
- \(L_i\): target actually identified;
- \(O_i\): observation and measurement interface;
- \(C_i\): operating conditions and controls;
- \(\tau_i\): validated time or transfer horizon;
- \(A_i\): action or authority type permitted by the evidence.

An update therefore produces not merely:

\[
\Delta W(H_i),
\]

but:

\[
\boxed{
(\Delta W(H_i),\Delta\Sigma(H_i)).
}
\]

A result may:

- increase authority while leaving scope narrow;
- shrink scope while preserving local validity;
- extend scope only after transfer evidence;
- preserve a result while rejecting its proposed mechanism;
- add a new hypothesis without changing authority over existing ones.

The governing rule is:

\[
\boxed{
\text{Evidence earns authority only inside the smallest scope it can identify.}
}
\]

### Example: benchmark v0.1

A successful result can support approximately:

> Under a declared hidden-state collision and supplied candidate sensor, selective acquisition can outperform further optimization over an insufficient interface after cost.

It does not support:

> Autonomous interface evolution has been demonstrated.

The difference is represented in \(\Sigma\), not left to later prose.

### Example: congenital-blindness comparison

A group difference could update:

\[
\Sigma(H_{\mathrm{modality}})
\]

for the developmental dependence of visual rendering.

It would not automatically update:

\[
W(H_{\mathrm{external\ source}}).
\]

---

## 3. Three ledgers

The framework separates three records that are commonly collapsed.

### Observation and measurement ledger

\[
\mathcal L_O=(O_t,\Phi_t,F_t).
\]

It records:

- what occurred or was reported;
- how it was measured;
- which features were extracted;
- which distinctions the interface could not preserve.

It answers:

> What entered the system, and through what measurement process?

### Justification and discrimination ledger

\[
\mathcal L_J=(\mathcal H_t,T_t,\Pi_t,J_t).
\]

Here \(J_t\) records proposed evidential edges:

\[
F_k\rightsquigarrow H_i.
\]

It records:

- which hypotheses were compared;
- what each hypothesis predicted;
- which observation favors or disfavors each hypothesis;
- whether apparently separate paths share a generator or failure mode;
- which result would reduce the preferred hypothesis's authority.

It answers:

> Why is this feature being treated as evidence for that hypothesis?

### Authority, scope, and correctability ledger

\[
\mathcal L_W=(W_t,\Sigma_t,\mathcal R_t,\Gamma_t).
\]

It records:

- current authority;
- the exact validity and deployment scope;
- reopening conditions;
- permitted update magnitude and direction;
- unresolved uncertainty;
- whether correction can operationally reach the commitment.

It answers:

> What changed, where does the change apply, and what could still change it back?

The no-collapse rule is:

\[
\boxed{
\mathcal L_O\neq\mathcal L_J\neq\mathcal L_W.
}
\]

An observation is not its interpretation.

An interpretation is not its justification.

A justification is not automatically sufficient to authorize a large, global, or irreversible update.

---

## 4. Four update operations

The update operator should distinguish at least four operations.

### Promotion

Increase authority within an earned scope:

\[
U_{+}:W(H_i)\uparrow.
\]

Promotion requires discriminating evidence, not merely consistency with the preferred hypothesis.

### Contraction

Reduce authority, confidence, deployment permission, or inherited status:

\[
U_{-}:W(H_i)\downarrow.
\]

Contraction may preserve unaffected dimensions and local results.

### Rescoping

Change where a claim applies:

\[
U_{\Sigma}:\Sigma(H_i)\rightarrow\Sigma'(H_i).
\]

A contradiction outside the demonstrated domain may require scope contraction rather than total rejection.

Transfer evidence may justify cautious expansion.

### Hypothesis expansion

Introduce a distinction absent from the current hypothesis space:

\[
U_{\mathrm{expand}}:
\mathcal H_t\rightarrow\mathcal H_{t+1}.
\]

Examples include:

- adding a hidden variable;
- separating result validity from source mechanism;
- introducing a mixed-source hypothesis;
- splitting one overloaded category;
- adding an unresolved state \(H_{?}\).

The complementary operation is ordinary authority revision over existing hypotheses:

\[
U_{\mathrm{contract/promote}}:
W_t\rightarrow W_{t+1}.
\]

The balance is:

\[
\boxed{
\text{expansion without contraction risks ontology inflation;}
}
\]

\[
\boxed{
\text{contraction without expansion risks skepticism without explanatory progress.}
}
\]

Hypothesis expansion does not itself establish the new hypothesis.

It only makes a previously unavailable discrimination representable.

---

## 5. Application contract

An application is not governed inference until it declares the following.

### Competing hypotheses

\[
\mathcal H=\{H_1,H_2,\ldots,H_n,H_{?}\}.
\]

The preferred explanation cannot be evaluated only against an unspecified null.

### Operational measurement

State how raw observations become features:

\[
F=\Phi(O).
\]

### Discrimination contract

For each material hypothesis pair, state at least one result expected to separate them:

\[
T_{ij}:F\mapsto
\text{relative support for }H_i\text{ versus }H_j.
\]

### Negative update condition

Predeclare a result that would reduce the preferred hypothesis's authority:

\[
F_i^{-}\Rightarrow\Delta W(H_i)<0.
\]

Without this, the interpretation has no defined correction path.

### Provenance and dependency map

State whether apparently separate observations share:

- one instrument;
- one dataset;
- one participant;
- one generative process;
- one evaluator;
- one preprocessing pipeline;
- one label source;
- one cultural or institutional prior;
- one hidden upstream cause.

### Scope map

Declare:

\[
\Sigma(H_i)=
(\mathcal F_i,L_i,O_i,C_i,\tau_i,A_i).
\]

### Reopening path

Declare which future evidence reopens the claim and how that evidence reaches authority revision.

If these objects are absent, a result may remain a useful interpretation, but it has not entered the governed update architecture.

---

## 6. Update gates

A legitimate update passes through non-substitutable gates.

### Gate 1 — Measurement validity

Does \(\Phi\) preserve the distinction the feature claims to measure?

Where factorization is the appropriate criterion:

\[
L=\widehat L\circ\Phi
\]

over the declared class.

### Gate 2 — Hypothesis relevance

Could the feature differ under the competing hypotheses?

If all live hypotheses predict the same result:

\[
\Delta W\approx0.
\]

### Gate 3 — Discriminating power

Does the observed result favor one hypothesis over another under the declared test?

A prediction shared by every hypothesis is not discriminating evidence.

### Gate 4 — Correction-path independence

Does the evidence add a genuinely new route through which the hypothesis could fail?

Correlated confirmations must not be counted as independent replication.

### Gate 5 — Magnitude calibration

Update depth should reflect:

- evidential strength;
- independence;
- measurement quality;
- model coverage;
- consequence of error;
- reversibility;
- transfer evidence.

No universal scalar is currently validated for combining these terms.

### Gate 6 — Scope locality

Evidence may update only the dimensions and domains it identifies:

\[
\boxed{
\text{local evidence}\not\Rightarrow\text{global authority}.
}
\]

### Gate 7 — Reopening preservation

The update must not eliminate the paths needed to challenge it later.

A claim that becomes operationally unrevisable after one success has converted evidence into constitutional immunity.

---

## 7. Formal and operational reopenability

Confidence is not correctability.

For each hypothesis retain:

\[
C_i=
(H_i,W_i,\Sigma_i,\mathcal R_i,\Gamma_i,\mathcal L_i),
\]

where \(\mathcal L_i\) records known limitations and unresolved alternatives.

### Formal reopenability

A hypothesis is formally reopenable when:

\[
\mathcal R_i\neq\varnothing.
\]

Some possible evidence is declared capable of reopening it.

### Operational reopenability

Formal reopenability is insufficient.

Define operational reopenability as the existence of at least one evidence path \(e\in\mathcal R_i\) such that:

1. the evidence is realistically obtainable;
2. the measurement interface can preserve it;
3. it can propagate to the update mechanism;
4. \(\Gamma_i(e)\) permits a non-negligible negative update;
5. institutional or architectural rules permit revision or replacement.

Symbolically:

\[
\boxed{
\operatorname{OR}(H_i)=1
\iff
\exists e\in\mathcal R_i:
\operatorname{Reach}(e,U)>0
\land
\|\Gamma_i(e)\|\geq\epsilon
\land
\operatorname{Replaceable}(H_i).
}
\]

This is a structural criterion, not a validated universal metric.

A claim can be formally falsifiable yet operationally insulated when:

- the required evidence cannot be collected;
- the defended hypothesis controls the measurement;
- contradictions are reclassified before reaching \(U\);
- the response function caps negative revision near zero;
- replacement is institutionally prohibited.

Thus:

\[
\boxed{
\text{formal reopenability}\neq\text{operational reopenability}.
}
\]

And:

\[
\boxed{
\text{correctability}\neq1-W.
}
\]

A high-authority claim may remain highly correctable.

A low-confidence claim may remain structurally immune to correction.

---

## 8. Epistemic topology

Epistemic topology is the directed dependency graph of routes through which observations can change authority.

Let:

\[
\mathcal G_E=(V,E).
\]

Nodes may include:

- world states or reported events;
- instruments and observation interfaces;
- extracted features;
- hypotheses;
- tests and interventions;
- evaluators and labels;
- authority states;
- reopening and replacement mechanisms.

Edges have at least four types.

### Measurement edges

\[
O\rightarrow F.
\]

They specify how observations become admissible features.

### Evidential edges

\[
F\rightsquigarrow H.
\]

They specify why a feature bears on a hypothesis.

### Dependency edges

\[
Z\rightarrow\{O_i,F_i,T_i\}.
\]

They represent shared instruments, datasets, generators, labels, assumptions, or latent causes that can induce common-mode failure.

### Correction edges

\[
F^{-}\rightarrow\Delta W^{-}.
\]

They specify how contradiction reduces authority.

A correction path is a route:

\[
p:O\rightarrow F\rightarrow T\rightarrow\Delta W.
\]

Two paths are not operationally independent merely because their outputs differ.

They are independent relative to a declared failure class only when no known single common-mode dependency disables both.

A useful local analysis therefore asks:

- What are the minimal cut sets that disconnect reality from negative authority revision?
- Which node controls multiple apparently independent paths?
- Can one intervention vary the suspected common cause?
- Does the topology contain a path to replace the measurement, hypothesis set, test, or update rule itself?

This makes epistemic topology operational rather than metaphorical.

It does not establish a universal independence metric.

---

## 9. Benchmark interpretation

The four toy benchmarks probe different parts of the kernel.

### v0.1 — measurement and interface sufficiency

Can the system recognize that additional optimization cannot recover a distinction erased before inference?

### v0.2 — discrimination acquisition

Can the system decide that apparent success is insufficient and purchase a supplied stress test?

### v0.3 — dependency-aware correction selection

Can the system prefer failure-conditioned correction coverage over marginal accuracy or correlated vote count?

### v0.4 — common-mode intervention

Can a supplied intervention change the support of a hidden upstream dependency and reveal that the correction ecosystem fails together?

Each benchmark earns only a local scope map \(\Sigma\).

None establishes autonomous hypothesis generation, dependency discovery, measurement invention, or intervention invention.

The open frontier is revision of the update-governing objects themselves:

\[
(\Phi,\mathcal H,T,\Pi,U,\Sigma,\mathcal R,\Gamma)
\rightarrow
(\Phi',\mathcal H',T',\Pi',U',\Sigma',\mathcal R',\Gamma').
\]

---

## 10. Altered-state example

The DMT/entity discussion can be represented without granting authority to any source ontology.

A provisional observation and feature ledger might be:

\[
O=\text{participant report},
\]

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

Candidate source hypotheses might include:

\[
\mathcal H=
\{H_{\mathrm{external}},H_{\mathrm{internal}},H_{\mathrm{generator}},H_{\mathrm{mixed}},H_{?}\}.
\]

Different tests have different scope maps.

A congenital-blindness comparison may update modality dependence of rendering, presence, agency, or communication.

It cannot by itself identify an external source.

Immediate versus delayed reports may update memory-reconstruction hypotheses.

Vividness and transformation may update phenomenological intensity or personal consequence.

They do not by themselves identify telepathic transfer.

The governing rule remains:

\[
\boxed{
\text{Each observation updates only the hypothesis dimension and scope its test can discriminate.}
}
\]

---

## 11. Preventing infinite meta-regression

Possible failure at every level does not imply endless testing.

Meta-level status grants no special authority, but bounded systems require stopping rules.

A provisional stopping condition is:

\[
\operatorname{EVI}_{\perp}(T_{k+1})
\leq
C(T_{k+1})+C_{\mathrm{delay}},
\]

where \(\operatorname{EVI}_{\perp}\) is the expected value of genuinely independent correction rather than repeated correlated confirmation.

Stopping is justified only when:

- residual uncertainty remains recorded;
- scope remains narrow enough for the evidence;
- stakes and reversibility are declared;
- no known common-mode dependency exceeds the accepted risk threshold;
- the next test adds insufficient independent correction value relative to cost;
- reopening conditions remain attached to the commitment.

The system stops because marginal independent correction value is insufficient under a declared objective—not because the current meta-level has become infallible.

---

## 12. Characteristic failure modes

### Measurement laundering

A feature is treated as if it directly represented the target despite an unvalidated extraction interface.

### Hypothesis closure

The preferred explanation is compared only against a weak or unspecified alternative.

### Evidential-edge laundering

A correlated feature is treated as if it identified a mechanism, source, or causal pathway.

### Correlated confirmation

Multiple outputs from one generator are counted as independent evidence.

### Authority spillover

Evidence for one dimension increases authority over provenance, mechanism, transfer, desirability, or deployment without a discriminating path.

### Scope laundering

A local result is rewritten as a global claim without transfer evidence.

### Ontology inflation

Unexplained residuals trigger unlimited hypothesis creation without discriminating tests or pruning.

### Skeptical collapse

Authority is repeatedly reduced without generating alternative hypotheses or actionable distinctions.

### Update capture

The defended hypothesis controls what is measured, which contradictions count, and how strongly they may revise authority.

### Correctability theatre

A claim nominally permits challenge while its reopening evidence is impossible, inaccessible, filtered, or institutionally powerless.

### Interpretation rewritten as observation

A later narrative is entered into the record as though it were the original event.

### Universalization by vocabulary

The same abstract terms are applied across domains without naming domain-specific hypotheses, tests, negative results, or scope boundaries.

---

## 13. Operational protocol

Before allowing an observation to change authority, record:

1. **Observation** — What occurred or was reported?
2. **Measurement** — How did \(\Phi\) convert it into features?
3. **Alternatives** — Which hypotheses genuinely compete, including \(H_{?}\)?
4. **Discrimination** — Which result separates them?
5. **Negative result** — What would reduce the preferred hypothesis's authority?
6. **Dependency** — Which paths share a generator, label, evaluator, dataset, or failure mode?
7. **Operation** — Is the update promotion, contraction, rescoping, or hypothesis expansion?
8. **Magnitude** — How large and deep may the update be?
9. **Scope** — What exactly has been established, and where does it not apply?
10. **Reopening** — What future evidence triggers revalidation?
11. **Reachability** — Can that evidence realistically reach the update mechanism?
12. **Replacement** — Can the measurement, hypothesis set, test, dependency model, or update rule itself be revised?

Without this structure:

\[
\text{observation}\rightarrow\text{interpretation}\rightarrow\text{authority}
\]

remains an uninspected inference path.

---

## 14. Claim boundary

This kernel is compatible with and partly restates concerns already formalized in:

- Bayesian model comparison;
- falsification and severe testing;
- causal inference;
- measurement theory;
- active experiment design;
- robust decision theory;
- source monitoring;
- provenance and reproducibility practice;
- common-mode failure analysis.

Its vocabulary earns separate authority only where the integrated decomposition:

- improves error localization;
- prevents unsupported authority or scope transfer;
- exposes operationally closed reopening paths;
- distinguishes correlated confirmation from independent correction;
- produces better correction behavior than simpler existing formulations.

It does not establish:

- one universal update operator for cognition or science;
- a universal metric of evidence, scope, independence, confidence, or correctability;
- autonomous generation of superior hypotheses, measurements, or interventions;
- that the same numerical update rule applies across domains.

---

## Final invariant

\[
\boxed{
\text{An observation may change authority only through a declared, discriminating, dependency-aware, scope-bounded, and operationally reopenable evidential path.}
}
\]

Operational compression:

\[
\boxed{
\text{Measure separately. Compare alternatives. Seek discrimination. Discount shared failure. Update locally. Scope explicitly. Preserve reachable reopening.}
}
\]
