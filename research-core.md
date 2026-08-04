# Research Core

## Start here

This document is the compact formal core of the project.

Read with:

- [research-claim-boundary.md](research-claim-boundary.md) — what is and is not claimed;
- [literature-map.md](literature-map.md) — where the components already live;
- [identifiability-literature-placement.md](identifiability-literature-placement.md) — detailed placement of the upstream identifiability substrate.

The project does not propose a new theory of identifiability.

It proposes a testable downstream hypothesis:

\[
\boxed{
\text{Explicit representation of identification boundaries and authority structure may improve correction behavior.}
}
\]

---

## 1. Observation and ambiguity

Let:

\[
\mathcal F
\]

be a declared model or system class.

Let:

\[
O:\mathcal F\rightarrow\mathcal P(\mathcal X)
\]

be an observation operator, experiment, or measurement process mapping each candidate \(f\in\mathcal F\) to an observable distribution.

The observation process partitions \(\mathcal F\) into equivalence classes:

\[
[f]_O
=
\{g\in\mathcal F:O(g)=O(f)\}.
\]

Candidates inside one class are observationally indistinguishable under the declared regime.

No estimator can distinguish them from that population distribution alone.

This is the established identifiability substrate.

The intuitive term **interface** refers to this boundary through which the system becomes observable. In technical communication, the relevant object should be named as the observation operator, experiment, or measurement process.

---

## 2. Identified content

Let:

\[
L_k:\mathcal F\rightarrow\mathcal Y_k
\]

be a target query or claim dimension.

Its identified set at observation \(O(f)\) is:

\[
\boxed{
\mathcal I_k(O(f))
=
\{L_k(g):g\in[f]_O\}.
}
\]

The identified set records exactly which target values remain compatible with the observable distribution and declared model class.

Possible outputs include:

- a point value;
- an interval or bound;
- a sign;
- an ordering;
- an equivalence class;
- an invariant proposition;
- a robust decision relation.

Point identification is the special case:

\[
|\mathcal I_k(O(f))|=1.
\]

A non-singleton identified set does not mean nothing is known.

It means that authority must remain compatible with every possibility still inside the set.

---

## 3. Admissible claims

Let \(C\) be a scientific or operational claim.

A claim is eligible to receive authority from the observation only when its content is an admissible function of the identified set:

\[
\boxed{
C=\phi(\mathcal I(O)).
}
\]

An admissible \(\phi\) may return:

- an identified point;
- an identified interval;
- a sign or ranking shared by all compatible models;
- a declared equivalence-class claim;
- another proposition invariant under the remaining ambiguity.

Not every formal function is admissible.

In particular, \(\phi\) may not select a privileged member of a non-singleton identified set without additional assumptions or evidence.

For example:

\[
\mathcal I_\theta(O)=[0.2,0.5]
\]

may authorize:

\[
0.2\leq\theta\leq0.5,
\]

but not:

\[
\theta=0.37.
\]

This failure is **pointification**: converting partial identification into unsupported point authority.

The upstream authority constraint is therefore:

\[
\boxed{
\Delta W(C)>0
\Longrightarrow
C\text{ is invariant under the remaining observational ambiguity}.
}
\]

---

## 4. Identification is necessary but not sufficient

The implication is asymmetric:

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

Identification removes one impossibility. It does not establish:

- finite-sample reliability;
- correct measurement;
- adequate model specification;
- robustness to hidden dependencies;
- transfer to another environment;
- causal interpretation;
- acceptable operational risk;
- stakeholder legitimacy;
- action desirability.

The transition is therefore:

\[
\boxed{
\text{identified content}
\rightarrow
\text{eligible claim}
\rightarrow
\text{governed epistemic update}.
}
\]

---

## 5. Typed epistemic authority

Scientific success often occurs on one target dimension while interpretation expands into another.

Let:

\[
W=(W_1,\ldots,W_m)
\]

be a typed authority vector whose dimensions may include:

- predictive validity;
- latent or causal mechanism;
- intervention validity;
- transport;
- safety;
- coordination;
- generator reliability;
- governance legitimacy.

For each dimension \(W_k\), the evidence must identify the corresponding target content \(L_k\).

Thus:

\[
\boxed{
\Delta W_k>0
\Longrightarrow
C_k=\phi_k(\mathcal I_k(O))
}
\]

for a declared admissible mapping \(\phi_k\).

Success in one dimension does not transfer automatically:

\[
W_{\mathrm{prediction}}
\not\Rightarrow
W_{\mathrm{mechanism}},
\]

\[
W_{\mathrm{local}}
\not\Rightarrow
W_{\mathrm{transport}},
\]

\[
W_{\mathrm{result}}
\not\Rightarrow
W_{\mathrm{generator}},
\]

\[
W_{\mathrm{capability}}
\not\Rightarrow
W_{\mathrm{governance}}.
\]

The project calls these invalid transfers **authority laundering** when evidence earned in one dimension is used to promote another non-identified dimension.

---

## 6. Claim contracts

A commitment is represented as:

\[
\boxed{
C=(H,W,\Sigma,\Pi,\mathcal R,\Gamma),
}
\]

where:

- \(H\): claim or hypothesis content;
- \(W\): typed authority;
- \(\Sigma\): validity and action scope;
- \(\Pi\): provenance and shared evidence dependencies;
- \(\mathcal R\): conditions capable of reopening the commitment;
- \(\Gamma\): required response if reopening occurs.

The representation is intended to make explicit several distinctions that often remain scattered across different methods.

### Scope \(\Sigma\)

A useful scope record may include:

\[
\Sigma=(\mathcal F,L,O,C,\tau,A),
\]

where:

- \(\mathcal F\): model or system class;
- \(L\): target query;
- \(O\): observation process;
- \(C\): operating conditions;
- \(\tau\): time horizon;
- \(A\): permitted action class.

A local result should alter only the scope identified by the evidence.

### Provenance \(\Pi\)

Repeated results do not count as independent when they share a hidden generator, preprocessing pipeline, evaluator, dataset, simulator, or upstream assumption.

The provenance record makes those dependencies available to the update rule.

### Reopening \(\mathcal R\)

A claim is not operationally reopenable merely because a falsifier can be described verbally.

The reopening evidence must be:

1. realistically obtainable;
2. preserved by measurement;
3. able to reach the update process;
4. capable of producing a material negative response;
5. connected to revision, rollback, or replacement authority.

### Response \(\Gamma\)

When reopening occurs, the record should specify whether the response is:

- authority contraction;
- scope contraction;
- action suspension;
- monitoring increase;
- rollback;
- replacement;
- hypothesis expansion.

Acknowledgment without consequential change is not a material update.

---

## 7. Epistemic authority and decision authority

Belief and action are distinct governance objects:

\[
\boxed{
W_{\mathrm{epistemic}}
\neq
W_{\mathrm{decision}}.
}
\]

A mechanism may remain unidentified while one action robustly dominates another under every compatible model.

Let:

\[
\Theta(O)
\]

be the set of models compatible with the observation regime.

For a declared loss or consequence model \(\Lambda\), if:

\[
\forall\theta\in\Theta(O):
\mathbb E_\theta[\Lambda(A)]
<
\mathbb E_\theta[\Lambda(B)],
\]

then action \(A\) may receive decision authority relative to \(B\), even when the exact mechanism is not point identified.

Therefore:

\[
\boxed{
\text{non-identification of mechanism}
\not\Longrightarrow
\text{action paralysis}.
}
\]

But:

\[
\boxed{
W_{\mathrm{action}}\uparrow
\not\Rightarrow
W_{\mathrm{mechanism}}\uparrow.
}
\]

A robust decision cannot be laundered into a causal explanation.

---

## 8. Three-layer architecture

The compact architecture is:

### Layer 1 — Identification

\[
O
\rightarrow
\mathcal I(O).
\]

Question:

> What point values, bounds, equivalence classes, rankings, or propositions survive observation?

### Layer 2 — Epistemic authority

\[
\mathcal I(O)
\rightarrow
(H,W,\Sigma,\Pi,\mathcal R,\Gamma).
\]

Question:

> Which claims may gain authority, over what scope, from which evidence paths, and under which reopening conditions?

### Layer 3 — Decision authority

\[
(W,\Sigma,\Lambda)
\rightarrow
A.
\]

Question:

> Which actions are justified under declared stakeholders, consequences, uncertainty, reversibility, monitoring, and rollback?

The prohibited collapses are:

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

\[
\boxed{
\text{epistemically authorized}
\neq
\text{decision justified}.
}
\]

---

## 9. Concrete invalid-transfer errors

The representation hypothesis can be tested through recognizable failures.

### Pointification

\[
\theta\in[0.2,0.5]
\quad\Longrightarrow\quad
\theta=0.37.
\]

Partial identification is converted into unsupported exactness.

### Mechanism laundering

\[
W_{\mathrm{prediction}}
\rightarrow
W_{\mathrm{mechanism}}.
\]

Predictive or associational success is converted into causal authority.

### Transport laundering

\[
W_{\mathrm{environment\ A}}
\rightarrow
W_{\mathrm{transfer}}.
\]

Local validity is converted into general validity.

### Generator laundering

\[
W_{\mathrm{result}}
\rightarrow
W_{\mathrm{generator}}.
\]

A valid output is converted into trust in the opaque process that generated it.

### Capability laundering

\[
W_{\mathrm{task\ performance}}
\rightarrow
W_{\mathrm{governance}}.
\]

Superior capability is converted into legitimacy over goals, oversight, or succession.

### Decision-story laundering

\[
W_{\mathrm{robust\ action}}
\rightarrow
W_{\mathrm{mechanism}}.
\]

A decision justified under ambiguity is converted into an identified explanatory story.

### Dependency laundering

\[
\text{many correlated confirmations}
\rightarrow
\text{independent evidence authority}.
\]

Repeated outputs from one upstream source are treated as multiple correction paths.

### Formal-reopening laundering

\[
\mathcal R\neq\varnothing
\rightarrow
\text{claim is operationally correctable}.
\]

A nominal falsifier is treated as meaningful despite being unobtainable, unmeasured, nonbinding, or unable to trigger revision.

---

## 10. Evidential update pipeline

The broader methodological pipeline is:

\[
(O,\Phi)
\rightarrow
F
\rightarrow
(\mathcal H,T,\Pi)
\rightarrow
U_\Lambda
\rightarrow
(W,\Sigma,\mathcal R,\Gamma).
\]

where:

- \(O\): raw observation;
- \(\Phi\): measurement or observation process;
- \(F\): extracted features;
- \(\mathcal H\): competing hypotheses, including unresolved alternatives;
- \(T\): discrimination contract;
- \(\Pi\): provenance and shared dependency structure;
- \(U_\Lambda\): update process under a declared governance loss;
- \(W\): typed authority;
- \(\Sigma\): earned scope;
- \(\mathcal R\): reopening conditions;
- \(\Gamma\): revision response.

This is a candidate engineering decomposition.

It is not claimed as a universal rationality operator.

---

## 11. Primary empirical hypothesis

The project does not need to show that these distinctions can be named.

It must test whether explicitly representing them changes behavior.

The primary hypothesis is:

\[
\boxed{
\text{Explicit identification and authority records reduce invalid authority transfers during sequential evidence updates.}
}
\]

The complexity-adjusted hypothesis is:

\[
\boxed{
\Delta L_{\mathrm{avoided}}
>
\Delta C_{\mathrm{representation}}.
}
\]

Possible measurable outcomes include:

- fewer unsupported point claims;
- less mechanism, transport, generator, and capability laundering;
- better retention of still-valid local claims after contradiction;
- stronger discounting of shared evidence dependencies;
- more appropriate reopening and rollback;
- better separation of epistemic and action authority;
- lower repair latency;
- greater disagreement legibility;
- acceptable training, annotation, and coordination cost.

---

## 12. Current evidence

Benchmarks v0.1–v0.5 are synthetic supplied-object tests.

They show that the representation can encode and avoid selected evaluator-authored errors within frozen scenarios.

They do not establish:

- independent human usability;
- transfer to externally authored cases;
- necessity of the representation;
- superiority over mature methods;
- autonomous discovery of missing governance objects;
- strategic-agent corrigibility.

Pilot 0 tests whether outsiders can instantiate and revise the representations without inventor arbitration.

The comparative protocol tests whether any resulting correction benefit survives native-strength alternatives and complexity cost.

Neither has been executed.

---

## 13. Strongest alternatives

A fair evaluation must compare against:

- Bayesian workflows with model uncertainty, predictive checks, domain restrictions, monitoring, and decision loss;
- causal models with transportability, intervention access, and sensitivity analysis;
- assurance cases with contexts, assumptions, defeaters, confidence arguments, and monitoring;
- AGM-style belief revision with contraction, entrenchment, and revision triggers;
- provenance-aware scientific workflows;
- minimal method-native augmentations that capture the suspected advantage.

The claim-contract representation earns distinct authority only if it improves correction, coordination, or auditability after those alternatives are implemented faithfully.

---

## 14. Defeat conditions

The project should be narrowed, absorbed, or rejected as a distinct operational contribution if:

1. mature alternatives reproduce the same behavior at equal or lower cost;
2. outsiders cannot instantiate the representation without author mediation;
3. benefits disappear on independently authored cases;
4. framework vocabulary leaks the intended answer;
5. generalized abstention explains the apparent improvement;
6. evaluator-selected loss weights determine the outcome without robustness;
7. the representation improves description but not correction behavior;
8. its complexity exceeds avoided governance loss;
9. the framework becomes the sole authority over its own evaluation.

A legitimate outcome is that the work survives only as a synthesis layer, checklist, pedagogical decomposition, or domain-specific assurance method.

---

## 15. Current frontier

The immediate scientific question is:

\[
\boxed{
\text{Can independent users apply the representation without inventor arbitration, and does it improve sequential correction relative to strong alternatives?}
}
\]

The next information gain comes from external use, not conceptual expansion.

---

## Final compression

\[
\boxed{
\text{Observation determines an identified set; identified content constrains epistemic authority; explicit stakes and losses govern action.}
}
\]

And:

\[
\boxed{
\text{A representation earns authority only if outsiders can use it and it improves correction more than it costs.}
}
