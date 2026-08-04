# Generative Provenance Protocol

## Status

This protocol operationalizes the Ramanujan stress test.

It governs claims made when a system produces a high-value candidate while the process that generated it is partially or wholly inaccessible.

It is a corpus-level methodological proposal.

It is not a validated benchmark, a universal theory of understanding, or an Interface Theory gate record.

Its purpose is to preserve useful discoveries without confusing:

\[
\text{result validity},
\quad
\text{provenance completeness},
\quad
\text{mechanism identification},
\quad
\text{explanation fidelity}.
\]

---

## 1. Required declaration

Before evaluating an opaque or partially opaque discovery, declare:

\[
\mathcal G
=
(F,O_Y,O_G,Y,L_G,\mathcal B,\mathcal C,\mathcal A).
\]

where:

- \(F\): class of candidate-generating systems;
- \(O_Y\): output interface;
- \(O_G\): process and intervention interface;
- \(Y\): candidate result space;
- \(L_G\): target generative mechanism or mechanism class;
- \(\mathcal B\): causal and resource boundary;
- \(\mathcal C\): admissible controls and competing generator models;
- \(\mathcal A\): authority policy specifying which evidence may change which claim weights.

Changing the system class, output criterion, mechanism target, boundary, or control family changes the claim.

---

## 2. Claim ledger

For each candidate \(y\), maintain four independent claim records.

### Result claim

\[
C_V(y):
\text{the candidate is valid under criterion }V.
\]

### Provenance claim

\[
C_P(y):
\text{the declared record accurately describes relevant generation resources and steps}.
\]

### Mechanism claim

\[
C_M(y,m):
\text{mechanism }m\text{ materially generated }y.
\]

### Explanation claim

\[
C_X(y,e):
\text{explanation }e\text{ causally describes the generation of }y.
\]

Each claim receives separate status:

- proposed;
- qualified;
- validated;
- contradicted;
- unresolved;
- out of scope.

No status automatically transfers to another claim type.

---

## 3. Authority vector

Maintain:

\[
\mathbf W(y)
=
(W_V,W_P,W_M,W_X).
\]

### No-spillover matrix

Let evidence types be:

\[
\mathbf e
=
(e_{\mathrm{proof}},e_{\mathrm{trace}},e_{\mathrm{intervention}},e_{\mathrm{transfer}},e_{\mathrm{explanation}}).
\]

Define a declared authority-transfer matrix:

\[
K_{ij}
=
\frac{\partial W_i}{\partial e_j}.
\]

The default sparsity constraints are:

- proof evidence may strongly update \(W_V\);
- process traces may update \(W_P\);
- interventions and discriminating controls may update \(W_M\);
- explanation-fidelity assays may update \(W_X\);
- no evidence type should update unrelated authority merely because the result is impressive.

In particular:

\[
\frac{\partial W_M}{\partial e_{\mathrm{proof}}}
\approx0
\]

and:

\[
\frac{\partial W_X}{\partial e_{\mathrm{proof}}}
\approx0
\]

unless the proof itself contains independent evidence about the generating process.

---

## 4. Gate \(V_0\): Independent result validation

### Question

Is the output correct independently of trust in the generator?

### Mathematical candidates

Preferred evidence includes:

- formal proof checked under declared rules;
- independently reconstructed proof;
- reduction to established results with verified conditions;
- machine-checked proof where appropriate;
- multiple independent derivations.

Numerical testing may support prioritization or falsification but does not generally establish a universal theorem.

### Empirical candidates

Preferred evidence includes:

- preregistered held-out prediction;
- independent replication;
- matched baselines;
- uncertainty calibration;
- intervention where the claim is causal.

### Failure condition

A plausible rationale, impressive source, or repeated agreement on training-like cases does not substitute for the declared validation criterion.

### Output

\[
V_0\in\{\text{pass},\text{fail},\text{unresolved}\}.
\]

A pass authorizes result-level inheritance only within scope.

---

## 5. Gate \(P_0\): Generative provenance

### Question

What resources and processes materially preceded the visible output?

### Minimum provenance inventory

Record, where relevant:

- system and model version;
- prompt, problem statement, or observations;
- accessible memory and prior artifacts;
- external tools and databases;
- candidate count;
- branch count;
- retries and discarded outputs;
- search budgets;
- random seeds;
- human edits;
- human or automated selection;
- proof assistants or verifiers;
- hidden evaluator feedback;
- post-output modifications;
- timing and order of explanation generation;
- state resets and checkpoint changes;
- whether the final result was produced before or after validation feedback.

### Provenance completeness classes

#### P0-A: direct trace

High-fidelity event record over the declared boundary.

#### P0-B: partial trace

Important steps and resources are recorded, but internal transformations remain inaccessible.

#### P0-C: reconstructed provenance

Process is inferred after generation from artifacts, testimony, or logs.

#### P0-D: output only

No useful process record beyond the final candidate.

Provenance class limits mechanism claims but does not determine result validity.

---

## 6. Gate \(G_0\): Generative identifiability

### Question

Does the process interface identify the declared generation mechanism over the relevant class?

For:

- system class \(F\);
- process interface \(O_G\);
- target mechanism label \(L_G\);

require:

\[
L_G
=
\widehat L_G\circ O_G.
\]

Equivalently:

\[
O_G(f_a)=O_G(f_b)
\Rightarrow
L_G(f_a)=L_G(f_b)
\qquad
\forall f_a,f_b\in F.
\]

### Relevant competing classes

The declared class should include scientifically plausible alternatives such as:

- compressed structural reasoning;
- retrieval from prior exposure;
- exhaustive or heuristic search;
- stochastic candidate generation plus filtering;
- externally scripted generation;
- tool-mediated derivation;
- verifier-guided search;
- post-hoc derivation generation;
- mixtures of the above.

Excluding alternatives because they threaten the intended interpretation produces a trivial mechanism class.

### Collision witness

A Gate \(G_0\) failure exists when two systems with distinct mechanisms generate indistinguishable traces under \(O_G\).

The proper conclusion is:

\[
\text{mechanism unresolved under this interface and class}.
\]

It is not:

\[
\text{the output is invalid}.
\]

---

## 7. Gate \(X_0\): Explanation fidelity

### Question

Does explanation \(e\) describe the causal generation process rather than merely provide a valid proof or plausible rationale?

### Required separation

Distinguish:

- **proof validity** — does the argument establish the result?
- **pedagogical quality** — does it help a reader understand the result?
- **predictive process model** — does it predict internal or behavioral consequences of changing the alleged mechanism?
- **historical fidelity** — does it describe the process actually used at generation time?

An explanation may pass the first two while failing the latter two.

### Fidelity assays

#### Temporal assay

Was the explanation committed before the result, after the result, or after external feedback?

#### Counterfactual assay

Does modifying a claimed intermediate step change output in the predicted way?

#### Selective-ablation assay

Does disabling the alleged resource, representation, memory source, or operator selectively impair the relevant discovery class?

#### Error-prediction assay

Does the explanation predict characteristic errors and omissions, not only successes?

#### Transfer assay

Does the mechanism generate neighboring results under preregistered transformations?

#### Distinguishing assay

Can the explanation discriminate the true generator from matched systems producing the same output through another route?

### Output

\[
X_0\in\{\text{supported},\text{unsupported},\text{unresolved}\}.
\]

A valid proof with unresolved fidelity should be labeled:

> valid justification; generative fidelity not established.

---

## 8. Control family

### 8.1 Search-volume control

Compare direct-looking output against the complete candidate-generation budget.

Question:

Did apparent insight depend on hidden enumeration or repeated attempts?

### 8.2 Retrieval control

Remove or alter access to likely source material while preserving task competence.

Question:

Does output depend on retrieval rather than reconstructed structure?

### 8.3 Verifier-removal control

Remove external validation signals during generation.

Question:

Was the candidate generated independently or shaped by verifier feedback?

### 8.4 Post-hoc explanation control

Generate explanations for outputs produced by a different mechanism or supplied externally.

Question:

Can the system produce equally plausible derivations when it did not generate the answer?

### 8.5 Matched-result control

Use different known generators to produce the same final result.

Question:

Can the interface distinguish their mechanisms?

### 8.6 Wrong-intermediate control

Insert a plausible but causally irrelevant intermediate representation.

Question:

Does the explanation method endorse it merely because it supports the result?

### 8.7 Neighbor-task control

Transform the problem while preserving the alleged invariant.

Question:

Does the claimed representation transfer systematically?

### 8.8 Error-profile control

Compare false conjectures and omitted conditions across competing mechanism models.

Question:

Which model predicts the generator's failures?

---

## 9. Discovery ledger

Every candidate record should contain:

### Candidate identity

- exact statement or artifact;
- timestamp;
- source system;
- initial scope and conditions;
- novelty status if known.

### Validation record

- proof or validation method;
- validator identity;
- failed checks;
- corrections;
- final scoped status.

### Provenance record

- inputs;
- resources;
- tools;
- candidate history;
- selectors;
- missing information.

### Explanation record

- explanation text or formal derivation;
- time generated relative to candidate;
- whether it was used to produce the candidate;
- fidelity assays passed or failed.

### Authority record

- \(W_V,W_P,W_M,W_X\);
- evidence responsible for each update;
- permitted downstream uses;
- forbidden authority transfers.

### Inheritance record

- whether the result is inherited;
- whether the generator is inherited;
- whether the explanation is inherited;
- which limitations descendants must preserve.

---

## 10. Conditional inheritance policy

### Inherit the result

A candidate may be inherited as knowledge when \(V_0\) passes within scope.

### Inherit the proof

A proof may be inherited as a valid justification when its own verification passes.

### Inherit the explanation

An explanation may be inherited as a pedagogical or mathematical account without being labeled the original generation process.

### Inherit the generator

The generator requires stronger evidence because it will produce future candidates and errors.

At minimum, consider:

- performance over held-out classes;
- calibrated error rates;
- provenance and boundary accounting;
- behavior under controls;
- correction access;
- authority constraints;
- ability to defer to independent verification;
- failure-mode inheritance.

### Inherit mechanism claims

Mechanism claims require \(G_0\) and relevant intervention evidence.

The policy is:

\[
\boxed{
\text{result inheritance threshold}
<
\text{generator inheritance threshold}.
}
\]

A valid theorem is safer to inherit than an opaque theorem-generating mechanism with unknown failure structure.

---

## 11. Integration with the authority-acquisition gate

The authority-acquisition gate asks whether evidence changes operational weighting:

\[
R_t
\rightsquigarrow
\Delta W_{t+1}.
\]

This protocol requires the weighting to be typed.

### Result evidence

Updates:

\[
W_V.
\]

### Provenance evidence

Updates:

\[
W_P.
\]

### Mechanism-discrimination evidence

Updates:

\[
W_M.
\]

### Explanation-fidelity evidence

Updates:

\[
W_X.
\]

Selection policies should read the appropriate component.

Examples:

- publishing a theorem may depend primarily on \(W_V\);
- trusting future autonomous theorem generation depends on generator-level reliability, not one \(W_V\);
- deploying an explanation for education may depend on proof validity and pedagogical quality, not historical fidelity;
- using an explanation for causal intervention requires \(W_X\) and \(W_M\), not just \(W_V\).

---

## 12. Integration with dependency propagation

Let a mechanism claim \(h_M\) support downstream claims about:

- generalization;
- efficiency;
- safety;
- interpretability;
- transfer;
- self-correction;
- future reliability.

If \(h_M\) fails or remains unidentified, dependency propagation \(\Pi_0\) should reduce those descendant claims.

The validated result may remain independent residue:

\[
W_V\text{ preserved}
\]

while:

\[
W_M,W_X\text{ reduced or unresolved}.
\]

This is the intended selective correction.

---

## 13. Benchmark design template

A finite benchmark for generative provenance should freeze:

1. generator class \(F\);
2. candidate space \(Y\);
3. validity target \(V\);
4. mechanism target \(L_G\);
5. output interface \(O_Y\);
6. process interface \(O_G\);
7. hidden-search budget;
8. external tools and memory;
9. validation procedure;
10. explanation timing;
11. matched alternative generators;
12. intervention family;
13. authority-transfer rules;
14. interpretation ceiling.

The benchmark should include cases where:

- different mechanisms produce the same result;
- the same mechanism produces valid and invalid candidates;
- a valid proof is generated post hoc;
- a plausible explanation is generated for an externally supplied result;
- hidden candidate search varies while visible output is fixed;
- a reusable representation produces neighboring discoveries;
- retrieval and reasoning are behaviorally similar under ordinary prompts.

---

## 14. Failure signatures

### Authority spillover

\[
W_V\uparrow
\Rightarrow
W_M,W_X\uparrow
\]

without independent mechanism or fidelity evidence.

### Search erasure

Only the successful output is preserved; failed candidates and filtering costs disappear.

### Explanation invariance

The explanation remains equally plausible after the alleged generating mechanism is disabled or replaced.

### Output-only collision

Distinct generators are indistinguishable under the evaluation interface.

### Proof retrojection

A later proof is described as the original discovery method without evidence.

### Opaque generator lock-in

Repeated success grants the generator authority to validate itself or conceal failed outputs.

### Transparency overreach

A transparent but weak generator is preferred despite lower result validity solely because its traces are easier to narrate.

### Opacity overreach

An opaque but successful generator is granted broad causal or cross-domain authority solely because selected outputs validate.

---

## 15. What counts as progress

Legitimate progress includes:

- independently proving an opaque candidate;
- identifying a collision showing that output alone cannot reveal mechanism;
- producing a process interface that separates retrieval, search, and reusable representation over a declared class;
- showing that an explanation predicts selective intervention effects;
- reconstructing provenance while preserving uncertainty about inaccessible steps;
- discovering that a later proof differs from the original generation route;
- finding characteristic error signatures of a generator;
- demonstrating structured neighbor-task transfer;
- reducing generator authority after hidden search or external selection is exposed;
- preserving a validated result while withdrawing its mechanism narrative.

Negative findings are progress when they localize which claim remains unsupported.

---

## 16. Boundary of the protocol

This protocol does not require:

- complete access to private cognition;
- a literal step-by-step trace for every valid discovery;
- rejection of intuition;
- rejection of opaque models;
- proof that one unique internal mechanism exists;
- one universal definition of understanding;
- identical standards for theorem generation and high-stakes action;
- treating introspective reports as worthless;
- treating behavioral evidence as sufficient for arbitrary mechanism claims.

It requires claim typing and evidence discipline.

---

## Final protocol

When a system produces a valuable opaque result:

1. validate the result independently;
2. preserve the candidate and failed attempts;
3. inventory the causal boundary and hidden search;
4. separate proof from generation history;
5. test competing generator models;
6. assay explanation fidelity through intervention and transfer;
7. update result, provenance, mechanism, and explanation authority separately;
8. inherit the result more readily than the opaque generator;
9. preserve unresolved generative debt;
10. prevent downstream claims from borrowing authority from result validity.

The final rule is:

\[
\boxed{
\text{Correct output may earn result authority without earning mechanism authority.}
}
\]

And:

\[
\boxed{
\text{Unexplained success should be verified and preserved, not worshipped or discarded.}
}
\]
