# Epistemic Governance

## Purpose

Recursive adaptation creates a governance problem.

A system capable of changing its own representations, mechanisms, evaluators, and objectives can also change the conditions under which those changes appear successful.

The governance question is:

\[
\boxed{
\text{Which kinds of evidence may authorize which kinds of revision?}
}
\]

This file describes the corpus's emerging answer.

It is not an implementation specification for autonomous recursive self-improvement.

---

## 1. Evidence must not authorize arbitrary depth

An observed error may originate in:

- noise;
- state;
- parameters;
- representation;
- causal mechanism;
- observation interface;
- target definition;
- attribution process;
- constitutional revision rules.

The existence of an error does not determine its causal depth.

Therefore:

\[
\boxed{
\text{error detection}
\neq
\text{failure attribution}
\neq
\text{revision authorization}
}
\]

A valid correction process must distinguish these stages.

---

## 2. Epistemic authorities

The corpus increasingly separates six forms of authority.

### Target authority

Who defines the property \(L\) being preserved, predicted, or improved?

### Observation authority

Who determines the interface \(O\) through which evidence becomes available?

### Validation authority

Who determines whether a residual is a contradiction, noise, corruption, or an out-of-scope event?

### Attribution authority

Who assigns causal responsibility for the contradiction?

### Revision authority

Who determines what may change, at what depth, and by how much?

### Succession authority

Who determines which revised mechanism persists and becomes substrate for later adaptation?

A dangerous configuration is:

\[
\boxed{
\text{one mechanism controls all six authorities}
}
\]

Such a mechanism can define its target, filter its evidence, judge its own failure, authorize its own revision, and select its successor.

That is epistemic autocracy.

---

## 3. Separation without paralysis

Total concentration of authority enables self-confirmation.

Total fragmentation creates indecision.

The desired architecture is not maximal decentralization.

It is a distribution in which:

- no current mechanism is the final judge of its own continued rule;
- evidence can still produce decisive action;
- disagreements between authorities remain inspectable;
- unresolved attribution can enter a holding state;
- high-cost revisions require stronger evidence than low-cost revisions.

---

## 4. No-bypass hierarchy

The strongest completed governance structure in the corpus is:

\[
\boxed{
\text{factorization}
\rightarrow
\text{estimation}
\rightarrow
\text{predictive validity}
\rightarrow
\text{causal intervention}
}
\]

### Gate 1: factorization

Does the declared target factor through the declared interface over the declared class?

\[
L=\widehat L\circ O
\]

### Gate 2: estimation

Can finite data estimate the existing target map with declared uncertainty?

### Gate 3: predictive validity

Does the estimate add held-out predictive value beyond preregistered baselines?

### Gate 4: intervention

Can a candidate mechanism causally alter the validated target?

A success at a later gate cannot repair a failure at an earlier gate.

This rule prevents:

- metric construction from establishing measurement;
- in-sample fit from establishing prediction;
- prediction from establishing mechanism;
- mechanism performance from establishing target legitimacy.

---

## 5. Qualification is not selection

The governance freeze preserves:

\[
\boxed{
\text{qualification}
\neq
\text{comparison}
\neq
\text{selection}
}
\]

### Qualification

A candidate satisfies a declared threshold under a frozen protocol.

### Comparison

Two or more candidates are evaluated under a common target, interface, estimator, uncertainty model, and decision rule.

### Selection

A candidate is chosen for deployment, inheritance, or further authority.

Each stage requires additional evidence and governance.

Passing an earlier stage does not silently authorize a later one.

---

## 6. Claim identity

A scientific claim is not only a sentence.

It has an address:

\[
C_i=
(F_i,O_i,L_i,E_i,P_i,U_i)
\]

where:

- \(F_i\): declared system class;
- \(O_i\): observation interface;
- \(L_i\): target;
- \(E_i\): evidence;
- \(P_i\): provenance;
- \(U_i\): uncertainty and interpretation limits.

Changing one of these objects may create a new claim rather than update the old one.

A result ledger preserves claim identity by preventing later narrative from silently changing its class, target, interface, or evidential status.

---

## 7. Provenance and causal memory

A correctable lineage must remember more than the current mechanism.

For each inherited commitment, it should preserve:

\[
H_i=
(m_i,E_i,F_i,O_i,L_i,U_i,R_i)
\]

where:

- \(m_i\): selected mechanism or claim;
- \(E_i\): supporting evidence;
- \(F_i,O_i,L_i\): validity contract;
- \(U_i\): unresolved uncertainty;
- \(R_i\): conditions that should trigger revalidation or reopening.

Without this structure, inheritance converts provisional success into unexplained authority.

---

## 8. Counterfactual governance

A selected modification cannot be evaluated only through the realized path.

It requires contrasts such as:

\[
Y_{t+1}^{\mathrm{revised}}
\quad\text{versus}\quad
Y_{t+1}^{\mathrm{unrevised}}.
\]

Useful counterfactual structures include:

- fixed baselines;
- null branches;
- ablations;
- matched-resource controls;
- delayed or shuffled feedback;
- oracle ceilings;
- rollback branches;
- removal tests.

The governing principle is:

\[
\boxed{
\text{Do not let adaptation destroy the contrast required to determine whether it improved.}
}
\]

---

## 9. Epistemic exteriority

A correction channel is not independent merely because it is physically external.

The important question is whether the target-relevant evidence is fully authored by the mechanism it evaluates.

A system becomes self-confirming when it controls:

- evidence generation;
- evidence filtering;
- evidence interpretation;
- success criteria;
- and the authority update produced by the evidence.

A correctable system must preserve access to constraint that its current adaptive regime cannot unilaterally redefine.

---

## 10. Structured incompleteness

The system must be closed enough to act but incomplete enough to learn.

Healthy epistemic closure is:

\[
\boxed{
\text{local} + \text{conditional} + \text{reopenable}
}
\]

A valid commitment should include:

1. declared scope;
2. evidence basis;
3. uncertainty;
4. revision triggers;
5. rollback or migration path;
6. distinction between settled and unresolved claims.

The objective is not permanent doubt.

It is the preservation of lawful reopening.

---

## 11. Governance of ontology change

When the system changes its decomposition:

\[
\mathcal D_t\rightarrow\mathcal D_{t+1},
\]

old evidence and authority must be transported into the new schema.

A migration map should preserve:

- which prior components contributed to new components;
- which evidence remains relevant;
- which validity boundaries survive;
- which contradictions remain unresolved;
- which authority should not transfer automatically.

Without such migration, refactoring can erase accountability.

---

## Final principle

\[
\boxed{
\text{No adaptive mechanism should possess unilateral authority to define its target, filter evidence, judge failure, authorize revision, and choose its successor.}
}
\]

The governance objective is not to prevent change.

It is to make deep change traceable, contestable, proportional, and conditionally inheritable.
