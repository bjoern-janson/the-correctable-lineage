# Identifiability Literature Placement

## Status

This document records an external literature-placement correction to the corpus.

It does not claim a new theory of identifiability.

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

Then target or query identifiability requires:

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

This is best treated as a standard factorization criterion for target or functional identifiability, adapted to the corpus notation.

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
| Gate 1 | population-level identifiability |
| Gate 2 | finite-sample estimation and uncertainty |
| Gate 3 | predictive validation |
| Gate 4 | causal or interventional validation |

The word **interface** remains useful as a corpus-level intuition.

When communicating with statistics or machine-learning audiences, the technical object should usually be declared as an observation operator or experiment:

\[
O:\mathcal F\rightarrow\mathcal P(\mathcal X).
\]

A sample is a realization from this induced distribution, not the observation operator itself.

---

## 3. What the reviewed literature already establishes

The following ideas belong to mature identifiability research rather than to a new corpus-specific theory.

### Identifiability precedes estimation

Identifiability is a property of the model and observation regime under population-level access.

If two candidate systems induce the same observable distribution but differ on the target, no estimator can recover the target even with unlimited data.

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

## 4. Identification boundary to authority boundary

The corpus's remaining hypothesis begins downstream of identifiability.

Identifiability theory asks:

\[
\boxed{
\text{Which target distinctions survive the declared observation process?}
}
\]

Evidential Update Governance asks:

\[
\boxed{
\text{Which downstream authorities may those identified distinctions legitimately change?}
}
\]

Let \(L_k\) be one target dimension and \(W_k\) the corresponding authority component.

The bridge hypothesis is:

\[
\boxed{
\Delta W_k>0
\text{ is permitted only when }
L_k
\text{ is identified under the declared observation process and test.}
}
\]

For example, if predictive performance is identified but causal mechanism is not:

\[
\Delta W_{\mathrm{prediction}}>0
\]

may be justified while:

\[
\Delta W_{\mathrm{causal}}>0
\]

is not.

The governing transition is therefore:

\[
\boxed{
\text{identification boundary}
\rightarrow
\text{authority boundary}.
}
\]

This is a proposed governance rule, not a result established by the two reviews.

---

## 5. Revised claim boundary

The corpus should no longer claim novelty for:

- the target-identifiability factorization criterion;
- impossibility under observational equivalence;
- identifiability before estimation;
- identification up to equivalence classes;
- use of auxiliary variables, environments, interventions, lags, or multiple views to break ambiguity.

The defensible placement is:

\[
\boxed{
\text{Interface Theory Gate 1}
=
\text{a corpus-specific reformulation of target-relative identifiability and experimental observability}.
}
\]

The still-open contribution is narrower:

\[
\boxed{
\text{Does transporting identifiability limits into explicit typed, scoped, dependency-aware, and reopenable claim records improve correction behavior?}
}
\]

That question requires comparison with mature Bayesian, causal, decision-theoretic, assurance, provenance, and scientific-governance practices.

It is not answered by conceptual coherence or by v0.1–v0.5.

---

## 6. Authority update ledger

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

## 7. Publication and communication strategy

### Established substrate

Use standard terminology and cite mature work on:

- statistical identifiability;
- nonlinear ICA;
- latent-variable models;
- structural-equation models;
- causal representation learning;
- experimental design;
- transportability and interventions.

### Proposed synthesis

Present as hypotheses or engineering objects:

- typed authority states;
- explicit scope maps;
- operational reopening;
- provenance-aware correction paths;
- governance-loss contracts;
- correction-cut capture.

### Required evidence

The central empirical question is:

\[
\boxed{
\text{Does explicit authority bookkeeping improve correction behavior relative to strongest fair alternatives after complexity cost?}
}
\]

Pilot 0 and the comparative protocol address this downstream question.

---

## Final invariant

\[
\boxed{
\text{Evidence may increase authority over a target dimension only when that dimension is identified under the declared observation process, assumptions, and discrimination test.}
}
\]

This invariant is a governance proposal anchored in established identifiability theory.

Its comparative value remains open.
