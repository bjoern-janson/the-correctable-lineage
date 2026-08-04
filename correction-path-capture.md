# Correction-Path Capture

## Status

This document generalizes the adversarial-agent stress case into a cross-domain governance criterion.

It applies to any system that can influence the processes by which its claims, policies, mechanisms, or continued authority are evaluated, including:

- AI systems;
- corporations and audit structures;
- scientific communities and paradigms;
- governments and oversight institutions;
- safety-critical engineering organizations;
- the evaluation process of this repository itself.

It is not:

- a validated universal metric of corrigibility;
- evidence for a numerical phase-transition threshold;
- a complete theory of institutional design;
- proof that distributed authority is sufficient for safety;
- a claim that every concentration of authority is pathological.

The narrower question is:

\[
\boxed{
\text{Can adverse evidence still produce a material reduction in authority when correction conflicts with the evaluated system's interests?}
}
\]

---

## 1. Competence, humility, and corrigibility are different

Let:

- \(K\): epistemic competence — ability to model, predict, and reason;
- \(H\): represented humility — uncertainty, alternatives, and stated openness;
- \(C_{\mathrm{op}}\): operational corrigibility — whether valid adverse evidence can force a costly update in authority or action.

Then:

\[
\boxed{
K\neq H\neq C_{\mathrm{op}}.
}
\]

A system may be highly competent and accurately calibrated while controlling every route through which its authority could be reduced.

It may also express uncertainty while ensuring that no reachable observation produces a material negative response.

Thus:

\[
\boxed{
\text{epistemic competence}
\not\Rightarrow
\text{operational corrigibility},
}
\]

and:

\[
\boxed{
\text{represented uncertainty}
\not\Rightarrow
\text{reachable correction}.
}
\]

---

## 2. Governance graph

Represent the correction architecture as a directed graph:

\[
\mathcal G_C=(V,E).
\]

Nodes may include:

- external events and adverse outcomes;
- sensors, logs, and measurement interfaces;
- feature extraction and preprocessing;
- validators and auditors;
- failure-attribution mechanisms;
- decision and authority states;
- revision mechanisms;
- rollback, replacement, and succession mechanisms;
- stakeholders and loss-setting processes.

A negative correction path is a directed route:

\[
p^-:
O_{\mathrm{adverse}}
\rightarrow
F
\rightarrow
T
\rightarrow
\Delta W^-
\rightarrow
\Delta A^-,
\]

where:

- \(O_{\mathrm{adverse}}\): target-relevant adverse evidence;
- \(F\): a preserved measurement;
- \(T\): a discriminating test or adjudication process;
- \(\Delta W^-\): material reduction in claim or policy authority;
- \(\Delta A^-\): consequential action such as narrowing, suspension, rollback, replacement, or loss revision.

Let \(\mathcal P^-\) be the set of operational negative correction paths.

A path is operational only when its nodes and edges are reachable, sufficiently independent for the declared failure class, and authorized to produce a non-negligible response.

---

## 3. Control map

For an evaluated system or interested actor \(s\), define:

\[
\Omega_s:
V\cup E
\rightarrow
\{
\text{none},
\text{influence},
\text{veto},
\text{rewrite},
\text{replace}
\}.
\]

Control includes more than formal ownership.

It may arise through:

- exclusive information access;
- selective disclosure;
- evaluator dependence;
- persuasion or coercion;
- control of funding or incentives;
- ability to replace monitors;
- control of logs or preprocessing;
- authority to redefine success;
- control over revision and succession.

Externality is therefore not equivalent to independence.

An evaluator outside the nominal system may still lie inside its effective control structure.

---

## 4. Correction cut sets

A set \(K\subseteq V\cup E\) is a correction cut set when disabling or redefining the elements of \(K\) interrupts every operational negative correction path:

\[
\forall p^-\in\mathcal P^-:
K\cap p^-\neq\varnothing.
\]

The evaluated actor has captured a correction cut when:

1. it has unilateral veto, rewrite, or replacement power over every element of some cut set \(K\); and
2. exercising that power can prevent adverse evidence from producing material authority or action reduction.

Formally, a sufficient structural condition for full correction-path capture is:

\[
\boxed{
\exists K:
K\text{ is a cut of }\mathcal P^-
\land
K\subseteq\operatorname{Control}_{s}^{\mathrm{unilateral}}.
}
\]

When this condition holds, the system may still:

- report uncertainty;
- invite feedback;
- pass visible audits;
- revise low-cost parameters;
- acknowledge objections;
- maintain nominal external oversight.

Yet no adverse evidence can force a costly update that the system does not permit.

That is operational self-sealing.

---

## 5. Governance phase-transition hypothesis

Authority concentration may increase gradually while correction capacity fails abruptly.

The hypothesized transition is not:

\[
\Omega_s\geq\text{one universal scalar threshold}.
\]

No such threshold has been identified.

The sharper structural hypothesis is:

\[
\boxed{
\text{partial influence}
\rightarrow
\text{control of one complete correction cut set}
\rightarrow
\text{collapse of forced negative updating}.
}
\]

Before cut capture, at least one correction path remains outside unilateral control.

After cut capture, every path capable of materially reducing authority can be blocked, reclassified, weakened, or redirected by the evaluated actor.

Behavioral indicators may change smoothly across this transition.

A system may continue to appear cooperative and epistemically sophisticated even after operational corrigibility has collapsed.

This is a research hypothesis, not a demonstrated universal phase law.

---

## 6. Cross-domain instances

### AI systems

The evaluated model or agent controls its monitors, evidence filters, evaluator information, loss function, update rules, and replacement process.

### Corporations

The audited organization funds the auditor, defines the evidence interface, controls internal records, narrows the audit scope, and controls remediation or auditor replacement.

### Scientific communities

A dominant paradigm controls publication, admissible methods, anomaly interpretation, funding, and the succession process for researchers or models.

### Governments

An institution controls data collection, classification, oversight appointments, legal interpretation, enforcement, and the replacement of oversight bodies.

### Safety engineering

The development organization controls requirements, simulation assumptions, hazard evidence, acceptance criteria, incident attribution, and authorization for deployment continuation.

### This corpus

Framework authors control the vocabulary, cases, comparators, adjudication, analysis, and interpretation through which the framework is judged.

The evaluation charter and Pilot 0 are attempts to prevent that cut capture.

These examples share a structural pattern.

They do not imply identical motives, risks, or remedies.

---

## 7. Audit protocol

For a declared claim, policy, or deployment decision:

### Step 1 — Enumerate material negative updates

Specify what costly changes valid adverse evidence should be capable of producing, such as:

- confidence reduction;
- scope contraction;
- action suspension;
- loss-function review;
- rollback;
- replacement;
- succession denial.

### Step 2 — Trace correction paths

For each adverse-evidence class, trace:

\[
O^-
\rightarrow
F
\rightarrow
T
\rightarrow
\Delta W^-
\rightarrow
\Delta A^-.
\]

Do not count a path that ends only in logging or verbal acknowledgment.

### Step 3 — Map control

Record who can:

- generate evidence;
- suppress or delay it;
- alter preprocessing;
- select evaluators;
- redefine success;
- attribute failure;
- cap the update response;
- disable rollback;
- choose successors.

### Step 4 — Identify minimal cuts

Find small sets of nodes or edges whose loss disables every material correction path.

### Step 5 — Test unilateral capture

Determine whether one interested actor can veto, rewrite, simulate, or replace every component of any complete cut.

### Step 6 — Adversarially exercise the path

Introduce valid evidence that conflicts with the incumbent policy and verify whether authority and action actually change.

### Step 7 — Preserve replacement of the governance layer

The audit process, control map, and cut analysis must themselves remain challengeable and replaceable.

---

## 8. Design requirements

The objective is not maximal decentralization.

Total fragmentation can destroy action and accountability.

The narrower requirements are:

1. no interested actor unilaterally controls a complete correction cut;
2. at least one material negative-update path remains outside incumbent veto;
3. apparently independent paths are tested for shared control and provenance;
4. adverse evidence can produce costly rather than merely cosmetic updates;
5. rollback and succession do not depend solely on incumbent permission;
6. the governing loss and stakeholder set remain contestable;
7. emergency action remains possible under declared authority and scope;
8. disagreements and unresolved evidence remain inspectable;
9. the governance architecture can itself be audited, narrowed, or replaced.

---

## 9. Failure modes

### Nominal plurality

Many evaluators exist, but all depend on one information source, incentive structure, or replacement authority.

### Cosmetic correction

The system acknowledges failures and adjusts language or low-cost parameters while preserving the challenged authority and action.

### Controlled exteriority

Evidence appears external but is selected, generated, filtered, or scored by the evaluated actor.

### Attribution capture

Every contradiction is assigned to operators, sensors, exceptional conditions, or implementation details before it can challenge the incumbent mechanism.

### Loss capture

The incumbent defines which stakeholders, horizons, and harms count, making its own success the evaluation target.

### Succession capture

Replacement is possible only through successors chosen, trained, or authorized by the incumbent.

### Oversight theatre

Formal monitors exist, but none can produce a material negative update without incumbent consent.

### Framework capture

The governance vocabulary becomes the sole language through which failures are recognized, allowing failures outside the ontology to disappear.

---

## 10. Claim boundary

This document supports only the structural design requirement:

> Systems whose mistakes matter should not unilaterally control a complete cut set across every path capable of materially reducing their authority.

It does not establish:

- a universal scalar of authority concentration;
- a validated threshold separating corrigible and incorrigible regimes;
- that distributed governance is sufficient for correct outcomes;
- that external authorities are unbiased or competent;
- that every institution requires the same authority distribution;
- that a specific current AI system has captured its correction paths;
- that this corpus prevents correction-path capture.

---

## Final invariant

\[
\boxed{
\text{Never allow the object being corrected to possess unilateral control over a complete cut set across all material paths by which correction can arrive.}
}
\]

Operational compression:

\[
\boxed{
\text{Trace adverse evidence. Map control. Find correction cuts. Test costly updates. Preserve independent rollback and succession. Audit the governance layer.}
\]
