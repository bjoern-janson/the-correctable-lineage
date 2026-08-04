# Claim Contract Governance Benchmark v0.5

## Status

Frozen exploratory first implementation.

v0.5 is the first toy benchmark aimed at the integrated evidential-update governance kernel rather than one isolated interface property.

It is not an independent preregistration and does not establish a universal governance architecture.

---

## 1. Research question

Does explicitly storing a claim contract

\[
C=(H,W,\Sigma,\mathcal R,\Gamma)
\]

plus a dependency map and unresolved state reduce declared governance errors relative to storing only:

\[
(H,W)?
\]

The benchmark compares three agents:

1. **Authority-only agent** — one global authority value;
2. **Scope-only agent** — separate authority by scope, but no dependency, unresolved-state, or operational-reopening governance;
3. **Claim-contract agent** — authority, scope, dependency grouping, unresolved state, formal versus operational reopenability, and a material reopening response.

---

## 2. Governance loss

The benchmark makes its decision objective explicit:

\[
\boxed{
\Lambda=
\lambda_O L_{\mathrm{over}}
+\lambda_U L_{\mathrm{under}}
+\lambda_P L_{\mathrm{premature}}
+\lambda_S L_{\mathrm{skepticism}}
+\lambda_I L_{\mathrm{irreversible}}
+\lambda_R L_{\mathrm{reopening}}
+\lambda_C L_{\mathrm{complexity}}.
}
\]

The frozen weights are:

| Error | Weight |
|---|---:|
| overgeneralization | 3.0 |
| undergeneralization | 2.0 |
| premature certainty | 2.5 |
| excessive skepticism | 1.0 |
| invalid irreversible commitment | 5.0 |
| unnecessary reopening | 1.0 |
| contract complexity | 0.05 |

These weights are evaluator-authored.

They encode one governance preference, not a universal rationality function.

---

## 3. Claim states

### Authority-only

\[
C_A=(H,W).
\]

Properties:

- all evidence updates one global authority value;
- repeated evidence is counted independently;
- a listed falsifier is treated as reopenability;
- no unresolved hypothesis state exists;
- no local scope can be preserved separately.

### Scope-only

\[
C_S=(H,W,\Sigma).
\]

Properties:

- authority is tracked separately in scopes \(A\) and \(B\);
- local validity can survive a shift;
- correlated evidence is still counted repeatedly;
- formal and operational reopenability remain conflated;
- omitted models still force a decision within the supplied set.

### Full claim contract

\[
C_G=(H,W,\Sigma,\Pi,H_{?},\mathcal R,\Gamma).
\]

Properties:

- authority is scope-local;
- evidence from one dependency group is counted once per direction and scope;
- persistent unexplained residuals activate \(H_{?}\);
- operational reopenability requires accessible evidence, nontrivial response, and replaceability;
- a predeclared reopening event can trigger material contraction;
- representation and processing overhead is charged.

---

## 4. Scenarios

### 4.1 Local success

Evidence supports the claim only in scope \(A\).

Truth:

\[
H(A)=1,
\qquad
H(B)=0.
\]

Test:

Can the agent deploy in \(A\) without extending authority into untested \(B\)?

Primary failure:

\[
\text{local evidence}\rightarrow\text{global deployment}.
\]

### 4.2 Distribution shift

The claim remains valid in \(A\) and fails in \(B\).

Test:

Can the agent contract scope while preserving retained local validity?

Primary failure:

\[
\text{failure in }B
\rightarrow
\text{global rejection of validity in }A.
\]

### 4.3 Omitted hypothesis

Several supporting observations coexist with a persistent unexplained residual.

Test:

Can the system enter an unresolved state rather than force a high-stakes choice among incomplete hypotheses?

Primary failure:

\[
\text{incomplete }\mathcal H
\rightarrow
\text{premature certainty}.
\]

### 4.4 Formally unreachable falsifier

A falsifier is listed but inaccessible to the update mechanism.

Test:

Can the agent distinguish:

\[
\mathcal R\neq\varnothing
\]

from operational reopening access?

Primary failure:

\[
\text{formal falsifiability}
\rightarrow
\text{false assurance of correctability}.
\]

### 4.5 Correlated confirmation

Ten positive observations come from one shared generator; two negative observations come from independent paths.

Test:

Can the dependency map prevent correlated repetition from dominating independent contradiction?

Primary failure:

\[
\text{evidence quantity}
\rightarrow
\text{assumed evidence independence}.
\]

### 4.6 Genuine reopening

The claim first accumulates strong support, then encounters a reachable predeclared reopening event.

Test:

Can the event produce a material authority contraction before irreversible deployment?

Primary failure:

\[
\text{high prior authority}
\rightarrow
\text{insufficient response to decisive contradiction}.
\]

### 4.7 Stable global truth control

The claim is valid in both scopes.

Test:

Does the richer contract preserve correct deployment while paying explicit overhead?

This blocks the interpretation:

\[
\text{more governance fields}
\Rightarrow
\text{free improvement}.
\]

---

## 5. Primary metrics

The benchmark records:

- total declared governance loss;
- overgeneralization;
- undergeneralization;
- premature certainty;
- excessive skepticism;
- invalid irreversible commitment;
- unnecessary reopening;
- retained valid structure;
- unresolved-state use;
- operational-reopenability classification;
- representation and processing overhead.

---

## 6. Frozen success conditions

v0.5 passes only if:

1. scope prevents local-to-global spillover;
2. distribution failure narrows scope without erasing retained validity;
3. an omitted-model residual can enter an unresolved state;
4. a listed but unreachable falsifier is not treated as operational reopening access;
5. correlated confirmation is discounted by dependency group;
6. a reachable reopening event triggers material contraction;
7. the full contract pays nonzero overhead when its additional state is unnecessary.

---

## 7. What a positive result would establish

Only this local claim:

\[
\boxed{
\begin{aligned}
&\text{Under the declared evidence sequences and governance loss,}\\
&\text{a richer claim contract can avoid errors that an authority-only state cannot represent,}\\
&\text{while paying explicit overhead when those protections are unnecessary.}
\end{aligned}
}
\]

It would support the practical distinction between:

\[
(H,W)
\]

and:

\[
(H,W,\Sigma,\mathcal R,\Gamma)
\]

inside the declared toy environment.

---

## 8. Falsification and redundancy conditions

The integrated governance framing loses separate authority if:

1. a simpler state representation matches the full contract across all declared probes;
2. scope, dependency, and reopening fields do not improve error localization;
3. the result disappears under reasonable alternative loss weights;
4. equivalent Bayesian, causal, or decision-theoretic state representations explain the behavior without loss;
5. contract overhead exceeds avoided governance loss in the relevant domain;
6. the benchmark merely rewards fields because the evaluator encoded those same fields into \(\Lambda\).

The sixth condition is especially important.

v0.5 is partly a representational sufficiency test. It cannot by itself establish that the representation is universally appropriate.

---

## 9. Explicit non-claims

v0.5 does not establish:

- a universal governance loss;
- optimal belief revision;
- autonomous hypothesis invention;
- autonomous scope discovery;
- autonomous dependency discovery;
- autonomous reopening-condition generation;
- superiority over existing systems that already encode equivalent contracts;
- a general theory of science, intelligence, or rationality.

---

## 10. Reproducibility

Run:

```bash
python benchmark/claim_contract_governance_v0_5.py \
  --seeds 100 \
  --strict \
  --output-json benchmark/results/results-v0.5.json \
  --output-md benchmark/results/results-v0.5.md

python -m unittest \
  benchmark/test_claim_contract_governance_v0_5.py \
  -v
```

The implementation uses only the Python standard library.
