# Orientation and Boundary Protocol

## Status

This protocol is a corpus-level methodological proposal derived from the Sidis stress test.

It is not a completed Interface Theory gate, an empirically validated benchmark, or an authorization to compare or select adaptive architectures.

Its purpose is to prevent four common substitutions:

\[
\text{local change}
\rightarrow
\text{system-level improvement},
\]

\[
\text{organized trace}
\rightarrow
\text{endogenous agency},
\]

\[
\text{available reverse path}
\rightarrow
\text{reachable correction},
\]

\[
\text{acknowledged objection}
\rightarrow
\text{revised authority}.
\]

---

## 1. Required declaration

Before testing an improvement or correction claim, declare:

\[
\mathcal P=(F,O,L,B,\mathcal D,\mathcal R)
\]

where:

- \(F\): system class;
- \(O\): observation interface;
- \(L\): target property;
- \(B\): causal and resource boundary;
- \(\mathcal D\): dependency graph among claims and mechanisms;
- \(\mathcal R\): admissible reversal, replay, scripting, and null controls.

A result is scoped to this declaration.

Changing the boundary, class, target, or control family changes the claim.

---

## 2. Gate -1: Boundary completeness

### Question

Which process actually performed the work attributed to the system?

### Required inventory

The causal ledger should include, where relevant:

- energy and material inputs;
- training data and pretrained structure;
- labels, rewards, residuals, or preferences;
- human-generated candidates;
- human or evaluator selection;
- external search and optimization;
- memory outside the declared system;
- resets, checkpoints, forks, and rollback support;
- task-authored telemetry;
- hidden state injected by the environment;
- infrastructure that removes failed variants;
- timing information unavailable to the system itself.

### Boundary condition

Let \(W_{\mathrm{int}}\) denote causal work performed inside the declared system and \(W_{\mathrm{ext}}\) work performed by exterior processes.

No universal common unit is assumed.

The required question is causal:

\[
\Delta L
=
f(W_{\mathrm{int}},W_{\mathrm{ext}}).
\]

A claim of endogenous improvement is unsupported when the observed target change disappears after matching or removing the exterior contribution.

### Failure witness

A boundary-completeness failure exists when two cases share the same declared internal mechanism but differ in omitted exterior support, and the claimed improvement follows the exterior support:

\[
M_{\mathrm{int}}^{(a)}=M_{\mathrm{int}}^{(b)},
\]

\[
W_{\mathrm{ext}}^{(a)}\neq W_{\mathrm{ext}}^{(b)},
\]

\[
L^{(a)}\neq L^{(b)}.
\]

The result may still demonstrate a useful coupled system.

It does not demonstrate the same property in the internal subsystem alone.

---

## 3. Gate 0: Orientation identifiability

### Question

Does the interface identify the claimed direction of causal update?

For a correction claim, the target relation is:

\[
E_t^*
\rightsquigarrow
\Delta C_{\mathrm{rev},t+1}.
\]

Temporal succession is insufficient.

The interface must distinguish live consequence-coupled revision from traces that preserve similar visible order without the claimed causal access.

### Required control family

#### Replay control

Replay a previously generated successful trajectory without online consequence access.

Purpose:

\[
\text{organized behavior}
\neq
\text{online correction}.
\]

#### Reverse-order control

Present the same states or events in reversed temporal order where physically and semantically admissible.

Purpose:

Test whether the metric identifies causal orientation or merely trajectory structure.

#### Shuffled-consequence control

Preserve the marginal distribution of consequences while breaking their alignment with the changes that generated them.

Purpose:

\[
\text{feedback exposure}
\neq
\text{attributable feedback coupling}.
\]

#### Scripted-update control

Supply updates externally while preserving the visible before-after pattern.

Purpose:

Distinguish system-generated revision from evaluator-authored or task-authored change.

#### Matched-state null control

Match initial state, resources, and observable trajectory statistics while preventing the consequence channel from reaching revision machinery.

Purpose:

Identify whether the causal path is necessary.

#### Delayed or wrong-lag control

Shift consequences outside the claimed update window.

Purpose:

Test whether the observed relation depends on the declared temporal interface rather than post hoc alignment.

### Factorization condition

Let \(F_{\mathrm{live}}\) contain consequence-coupled systems and \(F_{\mathrm{control}}\) contain matched replayed, reversed, shuffled, or scripted systems.

For target \(L_{\mathrm{orient}}\):

\[
L_{\mathrm{orient}}
=
\widehat L\circ O
\]

must hold over:

\[
F=F_{\mathrm{live}}\cup F_{\mathrm{control}}.
\]

If a live updater and a scripted or replayed control collide under \(O\) while their targets differ, orientation is not identifiable from that interface.

---

## 4. Gate 1: Target factorization

Only after boundary and orientation declarations are frozen should the standard Interface Theory factorization question be asked:

\[
O(f_a)=O(f_b)
\Rightarrow
L(f_a)=L(f_b)
\qquad
\forall f_a,f_b\in F.
\]

This protocol does not change Gate 1.

It expands the declared class so that convenient controls cannot be excluded merely because they undermine the intended interpretation.

A narrow class that contains only systems already labeled as genuine updaters may establish a tautological factorization while failing to identify the target in the scientifically relevant class.

---

## 5. Gates 2-4

If and only if the preceding gates pass:

### Gate 2: Estimation

Freeze sample size, noise model, lag, observation window, estimator, and uncertainty criterion.

### Gate 3: Predictive validity

Test preregistered held-out predictions against simple and adversarial baselines.

Include replay, scripting, and exterior-support baselines where relevant.

### Gate 4: Intervention

Intervene on the identified consequence-to-revision pathway and test the predicted target change with matched controls.

A successful intervention on a proxy does not establish the broader interpretation unless the proxy-target relation has already passed the earlier gates.

---

## 6. Dependency-propagation audit

### Dependency graph

Represent commitments, mechanisms, and conclusions as a directed acyclic graph where possible:

\[
h_i\rightarrow h_j
\]

means that \(h_j\)'s authority depends materially on \(h_i\).

Cycles should be made explicit rather than hidden inside mutual explanatory support.

### Downstream authority mass

Define a qualitative or declared weighted quantity:

\[
M_{\downarrow}(h_i)
=
\sum_{j\in\operatorname{Desc}(h_i)}w_j.
\]

The weights may represent:

- practical consequence;
- number of dependent claims;
- confidence carried by descendants;
- intervention authority;
- resource allocation;
- irreversibility of decisions based on the claim.

No universal weighting scheme is assumed.

### Evidence scaling rule

A premise with larger downstream authority requires stronger independent evidence:

\[
\Theta_i
=
g\bigl(M_{\downarrow}(h_i),R_i,H_i\bigr),
\]

where:

- \(R_i\): reversibility of actions authorized by the premise;
- \(H_i\): potential harm or lock-in if the premise is wrong.

The exact function remains open.

The monotonic relation is the proposed constraint.

### Revision rule

When evidence reduces the authority of \(h_i\), dependent claims should be classified as:

1. **independent residue** — remains supported without \(h_i\);
2. **partially dependent** — authority reduced proportionally;
3. **fully dependent** — suspended or withdrawn;
4. **anti-dependent** — gains relevance because \(h_i\) failed;
5. **unresolved** — dependency cannot yet be identified.

This prevents both global deletion and objection quarantine.

---

## 7. Minimal experimental record

A compliant experiment should preserve:

### System record

- exact system version;
- initial state distribution;
- external resources;
- update permissions;
- persistence and reset rules.

### Interface record

- observations available to the system;
- observations available only to the evaluator;
- timing and lag;
- hidden state;
- transformations applied to the trace.

### Control record

- replay construction;
- reverse-order construction;
- shuffled-consequence construction;
- scripted-update construction;
- null-path construction.

### Dependency record

- central assumptions;
- descendants;
- evidence supporting each edge;
- propagation rules if an assumption fails.

### Interpretation record

- passed gates;
- failed gates;
- non-claims;
- alternative mechanisms still compatible with the observations.

---

## 8. Sidis worked example

### Claim A

Life reverses the ordinary thermodynamic tendency.

### Boundary audit

The organism is treated locally while environmental energy and entropy flows are not fully included.

Result:

\[
\text{Gate -1 fails}.
\]

### Orientation audit

Apparent purpose in reversed films is used as evidence of reverse animation.

Replay and reverse-description controls are not distinguished from autonomous causal organization.

Result:

\[
\text{Gate 0 fails}.
\]

### Factorization audit

Apparent purpose, chemical order, and irritability do not uniquely identify total entropy reversal.

Result:

\[
\text{Gate 1 fails}.
\]

### Dependency audit

The equal-probability premise supports positive and negative tendencies, the definition of life, cosmic regions, dark stars, stellar cycles, pseudo-life, and reverse memory.

Its downstream authority mass is high.

When the premise fails, most of those claims must be suspended.

The reversibility problem, dynamic approach to life, and structure-process distinction survive as independent residue.

---

## 9. Application to corpus prototypes

### Representation discovery

A system should not be credited with autonomous representation discovery when:

- the operator space was supplied externally;
- the evaluator selects the representation;
- validation data is reused for fitting;
- the environment never reaches the intended shift;
- the state transition is not propagated through the loop.

The boundary and orientation gates ask which process actually generated and selected the representation.

### Authority revision

A benchmark should not infer system-level authority change from task-authored telemetry.

The scripted-update control should produce the same visible telemetry if the evaluator, rather than the system, supplies the change.

If it does, orientation fails.

### Recursive self-improvement

A system should not be called recursively self-improving merely because later versions perform better.

The protocol requires separation of:

- external engineering;
- external selection;
- copied checkpoints;
- automated search;
- consequence-coupled internal revision;
- inheritance of corrected update machinery.

### Institutional correction

An institution may publish objections, audits, and dissent while retaining the same operational authority structure.

The dependency audit asks whether the objection changes decisions, permissions, budgets, succession, or mechanism weight.

---

## 10. Failure signatures

The protocol should flag the following signatures.

### Local-success signature

Performance rises inside the measured component while external support or total correction cost rises faster.

### Replay equivalence

A fixed replay or scripted updater receives the same correction score as a live consequence-coupled system.

### Lag insensitivity

The claimed feedback mechanism performs similarly when consequences are shuffled or moved outside the update window.

### Telemetry substitution

Evaluator-generated fields are treated as system-generated state changes.

### Dependency amnesia

A central premise is downgraded while descendants retain unchanged authority.

### Compression immunity

The theory's broad explanatory reach is used as a reason not to revise the premise that generated that reach.

---

## 11. What would count as progress

Legitimate progress includes:

- a finite class in which orientation factors through a declared interface;
- a collision witness proving that a current interface cannot distinguish live correction from replay or scripting;
- a closed-boundary comparison that isolates endogenous from exterior causal work;
- a dependency graph that correctly predicts which claims should lose authority after a premise fails;
- an intervention showing that severing consequence access prevents the identified revision;
- a simpler non-adaptive mechanism matching an allegedly adaptive system;
- a negative result that narrows the class or target without being reinterpreted as hidden confirmation.

---

## 12. Boundary of the protocol

This protocol does not assume that:

- every causal boundary can be made complete;
- all relevant work can be expressed in one unit;
- orientation is identifiable from finite observations;
- a dependency graph is acyclic or objectively unique;
- endogenous improvement is always preferable to coupled human-machine improvement;
- replay controls are meaningful for every physical process;
- passing these gates establishes biological life, consciousness, alignment, or safety.

The protocol controls attribution.

It does not supply a universal target.

---

## Final compression

\[
\boxed{
\text{Before calling a process adaptive, identify the boundary that paid for the change and the direction by which consequences altered future-change machinery.}
}
\]

Then ask whether the target factors through the interface, can be estimated, predicts held-out behavior, and responds to controlled intervention.

Finally, when a central premise fails:

\[
\boxed{
\text{propagate the authority loss through its actual descendants while preserving independent residue.}
}
\]
