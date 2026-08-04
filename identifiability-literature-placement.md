# Identifiability Literature Placement

## Status

This document records an external literature-placement correction to the corpus.

It does not claim a new theory of identifiability.

The contribution is not a replacement for identifiability theory. It treats identifiability results as constraints on permissible authority transitions.

Its purpose is to separate:

1. an established upstream identifiability substrate;
2. the corpus's still-open downstream governance hypothesis.

The relevant reviews are:

- [Nonlinear Independent Component Analysis for Principled Disentanglement in Unsupervised Deep Learning](https://arxiv.org/abs/2303.16535);
- [Identifiability of Latent-Variable and Structural-Equation Models: From Linear to Nonlinear](https://arxiv.org/abs/2302.02672).

---

## 1. Literature correction

The corpus previously described a Gate 1 condition using:

- system class;
- target property;
- interface;
- factorization through the interface.

In statistics and machine learning, the corresponding language is usually:

- model or function class;
- estimand, parameter, query, or target functional;
- observation operator, measurement process, experiment, or sampling scheme;
- identifiability from the induced observable distribution.

Let:

\[
\theta\in\Theta,
\qquad
O(\theta)=P_\theta,
\qquad
q(\theta)=\text{target query}.
\]

Then point identification of the query requires:

\[
\boxed{
P_{\theta_1}=P_{\theta_2}
\Longrightarrow
q(\theta_1)=q(\theta_2).
}
\]

In the corpus notation:

\[
\boxed{
O(f_a)=O(f_b)
\Longrightarrow
L(f_a)=L(f_b).
}
\]

Equivalently:

\[
\boxed{
L=\widehat L\circ O.
}
\]

This is best treated as a standard factorization criterion for point identification of a target or functional, adapted to the corpus notation.

It should not carry novelty authority as a new general theorem of identifiability.

---

## 2. Terminology bridge

| Corpus term | Standard technical analogue |
|---|---|
| system class \(\mathcal F\) | model class, parameter space, function class |
| system \(f\) | parameter value, generative model, structural model |
| target property \(L(f)\) | estimand, query, target functional, target parameter |
| interface \(O\) | observation operator, measurement channel, experiment, sampling scheme |
| \(O(f)\) | induced observable distribution or family of interventional distributions |
| interface collision | observational equivalence |
| hidden distinction | non-identified target dimension |
| added sensor or environment | auxiliary variable, side information, additional experiment, observation refinement |
| minimal interface | minimal identifying experiment or design |
| Gate 1 | population-level identification |
| Gate 2 | finite-sample estimation and uncertainty |
| Gate 3 | predictive validation |
| Gate 4 | causal or interventional validation |

The word **interface** remains useful as a corpus-level intuition:

> The interface is the boundary through which reality becomes available to the observer.

When communicating with statistics or machine-learning audiences, the technical object should usually be declared as an observation operator or experiment:

\[
O:\mathcal F\rightarrow\mathcal P(\mathcal X).
\]

A sample is a realization from this induced distribution, not the observation operator itself.

---

## 3. What the reviewed literature already establishes

The following ideas belong to mature identifiability research rather than to a new corpus-specific theory.

### Identifiability precedes estimation

Identification is a property of the model and observation regime under population-level access.

If two candidate systems induce the same observable distribution but differ on the target, no estimator can recover the exact target even with unlimited data.

### Recovery may be only up to equivalence

Latent components or structural parameters may be identifiable only up to:

- permutation;
- sign;
- scale;
- componentwise transformations;
- another declared equivalence relation.

Therefore every recovery claim must state:

\[
\boxed{
\text{identified with respect to which query and modulo which ambiguity?}
}
\]

### Partial identification and identified sets

Evidence need not collapse a target to one point.

Let the observational equivalence class of \(f\) be:

\[
[f]_O
=
\{g\in\mathcal F:O(g)=O(f)\}.
\]

For target \(L_k\), define the identified set:

\[
\boxed{
\mathcal I_k(O(f))
=
\{L_k(g):g\in[f]_O\}.
}
\]

The observation process may therefore identify:

- a point value;
- an interval or bound;
- a sign or ordering;
- an equivalence class;
- a robust action ranking;
- another invariant proposition.

Point identification is the special case:

\[
|\mathcal I_k(O(f))|=1.
\]

A non-singleton identified set does not imply that nothing is known.

It limits authority to statements valid over that set.

### Additional structure can break observational equivalence

Nonlinear ICA and causal-identification research use:

- temporal dependence;
- nonstationarity;
- auxiliary variables;
- multiple environments;
- interventions;
- multiple views;
- distributional assumptions;

to split equivalence classes that remain unresolved under ordinary i.i.d. observation.

This is better described technically as experiment enrichment, observation refinement, or additional identifying structure.

### Predictive performance does not establish semantic identification

A model may:

- fit the observed distribution;
- generate realistic samples;
- predict accurately;
- learn useful features;

without uniquely identifying the latent variables or causal structure humans intend to interpret.

Thus:

\[
\boxed{
W_{\mathrm{prediction}}
\not\Rightarrow
W_{\mathrm{latent\ structure}},
}
\]

and:

\[
\boxed{
W_{\mathrm{distribution\ fit}}
\not\Rightarrow
W_{\mathrm{causal\ mechanism}}.
}
\]

---

## 4. Identified content to epistemic authority

The corpus's remaining hypothesis begins downstream of identification.

Identifiability theory asks:

\[
\boxed{
\text{Which target distinctions survive the declared observation process?}
}
\]

Evidential Update Governance asks:

\[
\boxed{
\text{Which epistemic authorities may that identified content legitimately change?}
}
\]

Let \(C\) be a scientific claim and \(W(C)\) its epistemic authority.

For point-valued claims, the factorization rule is sufficient:

\[
O(f_a)=O(f_b)
\Longrightarrow
C(f_a)=C(f_b).
\]

For graded, bounded, or equivalence-class claims, use the more general condition:

\[
\boxed{
\Delta W(C)>0
\Longrightarrow
C=\phi(\mathcal I(O))
}
\]

for a declared admissible claim mapping \(\phi\).

An admissible \(\phi\) may return:

- a point when the identified set is a singleton;
- a bound when only bounds are identified;
- an equivalence-class statement;
- a sign or ordering;
- an invariant proposition;
- a robust decision relation.

Not every mathematical function of \(\mathcal I(O)\) is evidentially admissible.

In particular, \(\phi\) may not select one privileged element of a non-singleton identified set without additional declared assumptions or evidence.

For example:

\[
\theta\in[0.2,0.5]
\]

may be identified while:

\[
\theta=0.37
\]

is not.

The strongest general rule is:

\[
\boxed{
\text{Authority may increase only over claims whose content is invariant under the remaining observational ambiguity.}
}
\]

### Identification is necessary but not sufficient

The governance implication is asymmetric:

\[
\boxed{
\text{not identified}
\Longrightarrow
\text{no authority for that exact claim},
}
\]

but:

\[
\boxed{
\text{identified}
\not\Longrightarrow
\text{epistemically authorized}.
}
\]

Identification does not by itself establish:

- finite-sample reliability;
- measurement validity outside the declared model class;
- robustness to misspecification;
- transfer;
- causal relevance;
- stakeholder legitimacy;
- acceptable risk;
- action desirability.

The transition is therefore:

\[
\boxed{
\text{identified content}
\rightarrow
\text{eligible for evidential consideration}
\rightarrow
\text{governed epistemic authority update}.
}
\]

The governing bridge remains:

\[
\boxed{
\text{identification boundary}
\rightarrow
\text{authority boundary}.
}
\]

This is a proposed governance rule, not a result established by the two reviews.

---

## 5. Epistemic authority and decision authority

Belief authority and action authority are different objects.

\[
\boxed{
W_{\mathrm{epistemic}}
\neq
W_{\mathrm{decision}}.
}
\]

A mechanism may remain unidentified while one action is robustly preferred over another across every model still compatible with the evidence.

Let \(\Theta(O)\) be the set of models consistent with the observation regime.

If:

\[
\forall\theta\in\Theta(O):
\mathbb E_\theta[\Lambda(A)]
<
\mathbb E_\theta[\Lambda(B)],
\]

then action \(A\) may receive decision authority relative to \(B\) even when the exact mechanism or parameter is not point identified.

Thus:

\[
\boxed{
\text{non-identification of mechanism}
\not\Longrightarrow
\text{action paralysis}.
}
\]

But the robust decision does not identify the mechanism:

\[
\boxed{
W_{\mathrm{action}}\uparrow
\not\Rightarrow
W_{\mathrm{mechanism}}\uparrow.
}
\]

The resulting three-layer architecture is:

### Layer 1 — Identification

\[
O
\rightarrow
\mathcal I(O).
\]

What point values, bounds, equivalence classes, orderings, or propositions survive observation?

### Layer 2 — Epistemic authority

\[
\mathcal I(O)
\rightarrow
(W,\Sigma,\Pi,\mathcal R,\Gamma).
\]

Which claims may gain authority, over what scope, from which evidence paths, and under which reopening conditions?

### Layer 3 — Decision authority

\[
(W,\Sigma,\Lambda)
\rightarrow
A.
\]

Which actions are justified under declared stakeholders, consequences, uncertainty, reversibility, monitoring, and rollback?

The forbidden collapses are:

\[
\boxed{
\text{observable}
\neq
\text{identified},
}
\]

\[
\boxed{
\text{identified}
\neq
\text{epistemically authorized},
}
\]

and:

\[
\boxed{
\text{epistemically authorized}
\neq
\text{decision justified}.
}
\]

---

## 6. Concrete authority-transfer errors

The bridge makes several benchmarkable errors explicit.

### Pointification

Convert an identified set into an unsupported point:

\[
\theta\in[0.2,0.5]
\quad\Longrightarrow\quad
\theta=0.37.
\]

### Mechanism laundering

Convert predictive or associational success into causal authority:

\[
W_{\mathrm{prediction}}
\rightarrow
W_{\mathrm{mechanism}}.
\]

### Transport laundering

Convert local validity into general validity:

\[
W_{\mathrm{environment\ A}}
\rightarrow
W_{\mathrm{transfer}}.
\]

### Generator laundering

Convert result validity into authority over an opaque generator:

\[
W_{\mathrm{result}}
\rightarrow
W_{\mathrm{generator}}.
\]

### Capability laundering

Convert task performance into governance legitimacy:

\[
W_{\mathrm{capability}}
\rightarrow
W_{\mathrm{authority}}.
\]

### Decision-story laundering

Convert a robust action preference into an identified explanatory story:

\[
W_{\mathrm{action}}
\rightarrow
W_{\mathrm{mechanism}}.
\]

These are candidate empirical targets for Pilot 0 and the comparative protocol.

---

## 7. Revised claim boundary

The corpus should no longer claim novelty for:

- the target-identifiability factorization criterion;
- impossibility under observational equivalence;
- identification before estimation;
- partial identification and identified sets;
- identification up to equivalence classes;
- use of auxiliary variables, environments, interventions, lags, or multiple views to break ambiguity;
- robust decisions under ambiguity.

The defensible placement is:

\[
\boxed{
\text{Interface Theory Gate 1}
=
\text{a corpus-specific reformulation of target-relative identification and experimental observability}.
}
\]

The still-open contribution is narrower:

\[
\boxed{
\text{Does transporting identified sets and identification limits into explicit typed, scoped, dependency-aware, reopenable, and action-separated claim records improve correction behavior?}
}
\]

That question requires comparison with mature Bayesian, causal, decision-theoretic, robust, assurance, provenance, and scientific-governance practices.

It is not answered by conceptual coherence or by v0.1–v0.5.

---

## 8. Authority update ledger

### Increased authority

\[
W(
\text{Gate 1 belongs to established identifiability theory}
)
\uparrow.
\]

### Decreased authority

\[
W(
\text{the factorization criterion is a new general identifiability theorem}
)
\downarrow.
\]

### Increased translation concern

\[
W(
\text{the corpus uses private or nonstandard terminology for established objects}
)
\uparrow.
\]

### Increased boundary precision

\[
W(
\text{identified sets, not only point values, constrain permissible claim content}
)
\uparrow.
\]

### Unchanged open claims

No direct update is earned for:

\[
W(
\text{claim contracts improve correction behavior}
),
\]

\[
W(
\text{the integrated governance architecture is externally novel}
),
\]

or:

\[
W(
\text{correction-path capture is a distinct operational contribution}
).
\]

---

## 9. Publication and communication strategy

### Established substrate

Use standard terminology and cite mature work on:

- statistical identification and partial identification;
- nonlinear ICA;
- latent-variable models;
- structural-equation models;
- causal representation learning;
- robust decision theory;
- experimental design;
- transportability and interventions.

### Proposed synthesis

Present as hypotheses or engineering objects:

- typed epistemic and decision authority states;
- explicit scope maps;
- operational reopening;
- provenance-aware correction paths;
- governance-loss contracts;
- correction-cut capture.

### Required evidence

The central empirical question is:

\[
\boxed{
\text{Does explicit authority bookkeeping reduce invalid transfers beyond strongest fair alternatives after complexity cost?}
}
\]

Pilot 0 and the comparative protocol address this downstream question.

---

## Final invariant

\[
\boxed{
\text{Evidence may increase epistemic authority only over claims that are admissible functions of the identified set under the declared observation process, assumptions, and discrimination test.}
}
\]

Decision authority remains separately governed by stakes, loss, robustness, reversibility, monitoring, and rollback.

This invariant is a governance proposal anchored in established identification theory.

Its comparative value remains open.
