# External Reviewer Packet

## Purpose

This packet is for a pre-pilot hostile methods review.

It is not a request for endorsement, encouragement, or a general impression.

Before reviewing, please use the following boundary:

> This project does not claim to solve AI alignment, discover a new theory of intelligence or identifiability, or replace existing statistical and safety methods. Its narrower hypothesis is that explicit representation of identification limits and authority transitions may reduce specific evidence-update errors. The primary outcome of evaluation may be absorption into existing methods.

The requested task is:

> Identify where the proposal duplicates established practice, where its terms obscure existing concepts, and whether any remaining distinction is concrete enough to test.

The project should be narrowed, absorbed, or rejected wherever established methods already provide equivalent behavior at equal or lower cost.

---

## Primary hypothesis

The project proposes:

> Explicit representation of identified content, typed authority, validity scope, evidence dependencies, and reopening conditions may reduce invalid authority transfer during sequential evidence updates.

In compact form:

\[
\boxed{
\text{identified content}
\rightarrow
\text{typed and scoped authority update}
}
\]

The upstream identifiability mathematics is not claimed as new.

For observation operator:

\[
O:\mathcal F\rightarrow\mathcal P(\mathcal X),
\]

and target query \(L\), define:

\[
[f]_O=\{g:O(g)=O(f)\},
\]

\[
\mathcal I_L(O(f))=\{L(g):O(g)=O(f)\}.
\]

The proposed downstream rule is:

\[
\boxed{
\text{Authority may increase only over claims invariant under the remaining observational ambiguity.}
\]

Identification is necessary for the exact claim, but not sufficient for epistemic or decision authority.

---

## Candidate representation

A commitment may be recorded as:

\[
C=(H,W,\Sigma,\Pi,\mathcal R,\Gamma),
\]

where:

- \(H\): claim or hypothesis;
- \(W\): typed authority;
- \(\Sigma\): validity and action scope;
- \(\Pi\): provenance and shared evidence dependencies;
- \(\mathcal R\): reopening conditions;
- \(\Gamma\): required response when reopening occurs.

Decision authority is separate and depends on a declared consequence or loss model \(\Lambda\).

The representation is not claimed to be necessary, complete, or superior.

---

## Concrete failure targets

The proposed representation is intended to make the following errors easier to detect or prevent:

- **pointification** — converting an identified set or bound into an unsupported point;
- **mechanism laundering** — converting prediction or association into causal authority;
- **transport laundering** — converting local validity into general validity;
- **generator laundering** — converting result validity into trust in an opaque generator;
- **capability laundering** — converting task performance into governance legitimacy;
- **decision-story laundering** — converting a robust action choice into an identified mechanism;
- **dependency laundering** — treating correlated confirmations as independent evidence;
- **formal-reopening laundering** — treating a nominal but unreachable falsifier as operational correctability.

The empirical question is not whether these errors can be named. It is whether explicit representation changes correction behavior.

---

## Strongest alternatives

Please evaluate the proposal against native-strength forms of:

1. Bayesian workflows with model uncertainty, predictive checks, domain restrictions, monitoring triggers, and decision loss;
2. causal models with transportability assumptions, intervention access, and sensitivity analysis;
3. assurance cases with contexts, assumptions, defeaters, confidence arguments, and monitoring;
4. AGM-style belief revision with contraction, entrenchment, and revision triggers;
5. provenance-aware scientific and engineering workflows;
6. the smallest method-native augmentation that reproduces the suspected benefit.

A result that mature methods already encode the same distinctions more cheaply is a successful correction, not an evaluation failure.

---

## Reviewer questions

Please answer as directly and adversarially as possible.

1. Which parts are standard in your field under different names?
2. Which proposed distinctions are already operationally encoded in mature practice?
3. Which terms create unnecessary translation cost?
4. Does the representation prohibit or expose any error that a strong existing workflow would not?
5. What is the smallest method-native augmentation that would reproduce the proposed behavior?
6. Which Pilot 0 outcomes would distinguish operational value from relabeling?
7. Are the proposed cases likely to leak the intended ontology?
8. What evidence would make you conclude that the project should be absorbed or abandoned as a distinct contribution?

Please do not resolve ambiguity in the project's favor.

---

## Materials

Recommended reading order:

1. [research-claim-boundary.md](research-claim-boundary.md)
2. [research-core.md](research-core.md)
3. [literature-map.md](literature-map.md)
4. [pilot-0/README.md](pilot-0/README.md)
5. [pilot-0/neutral-cases.md](pilot-0/neutral-cases.md)
6. [pilot-0/translation-challenge.md](pilot-0/translation-challenge.md)

The remaining repository is historical provenance and is not required for this review.

---

## Requested output

A useful response can be short.

Please provide:

- **duplicate:** what is already known or practiced;
- **distinct:** any testable difference that remains;
- **weakened comparator:** any alternative represented unfairly;
- **case leakage:** where the evaluation reveals its intended categories;
- **decision:** proceed, revise, absorb, or stop;
- **reason:** the smallest set of observations supporting that decision.

The project should incorporate only corrections that change the claim boundary, comparator fidelity, case neutrality, scoring, or execution feasibility.
