# Interface Stress Benchmark v0.2

## Status

Exploratory benchmark and frozen first implementation.

This version moves one step beyond reactive interface correction. It tests whether an agent should pay to challenge an apparently successful evidence interface before deployment.

It does **not** test autonomous interface invention.

The central question is:

\[
\boxed{
\text{Can a system allocate costly skepticism when current success may hide interface fragility?}
}
\]

---

## 1. Boundary inherited from v0.1

v0.1 established only a local diagnostic split:

\[
O\text{-insufficiency can dominate additional }M\text{-optimization}
\]

when contradiction is already visible and a candidate sensor is supplied.

Its strongest failure was:

\[
\boxed{
\text{No experienced contradiction}
\Rightarrow
\text{no interface challenge.}
}
\]

v0.2 therefore targets hidden interface failure under apparent success.

---

## 2. Two observationally identical training worlds

Each run samples one world:

### Robust world

The visible cue is the target:

\[
Y=X.
\]

### Fragile world

A latent variable is the target:

\[
Y=H,
\]

but training enforces:

\[
X=H.
\]

Training performance is therefore perfect in both worlds.

The ordinary training interface cannot identify which world generated that success.

During deployment, the cue and latent variable are decorrelated.

Then:

- the cue policy remains correct in the robust world;
- the cue policy falls to chance in the fragile world.

---

## 3. The challenge operator

Before deployment, an agent may pay a one-time cost \(c_A\) to run a bounded audit:

\[
\mathcal A_O: O_t \rightarrow E_t^{\mathrm{challenge}}.
\]

A valid audit breaks the training correlation between \(X\) and \(H\).

The current cue-based policy is evaluated on those challenge cases.

If challenge accuracy falls below threshold \(\tau_A\), the agent may activate a supplied noisy sensor of \(H\), paying per-use cost \(c_S\).

The sequence is:

\[
\text{apparent success}
\rightarrow
\text{paid challenge}
\rightarrow
\text{conditional diagnosis}
\rightarrow
\text{conditional interface repair}.
\]

---

## 4. Adaptive skepticism allocation

The agent should not audit automatically.

Let:

- \(p_F\): declared prior probability of the fragile world;
- \(T\): remaining deployment horizon;
- \(V_0\): best expected value without audit;
- \(V_A\): expected value after audit and conditional repair.

Audit is authorized only when:

\[
\boxed{
V_A-\frac{c_A}{T}>V_0.
}
\]

This is not maximum skepticism.

It is skepticism allocated by expected value under a declared objective and risk model.

---

## 5. Agents

### Fixed interface

Uses the visible cue and never challenges it.

### Always sensor

Deploys the additional sensor everywhere.

This is the interface-fetishism baseline.

### Best static policy

Chooses the better of cue-only and sensor-only policies using the declared prior, but cannot condition policy on a challenge result.

### Always challenge

Pays for every challenge, then conditionally activates the sensor.

### Adaptive skeptic

Pays for the challenge only when its expected value exceeds cost, then activates the sensor only when the audit exposes fragility.

### Oracle

Knows which world generated the data.

---

## 6. Frozen scenarios

### Balanced affordable risk

Fragility is common and the challenge is inexpensive enough to justify.

Expected result: audit, diagnose, and conditionally repair.

### Rare fragility

Fragility is possible but too rare to justify universal challenge under the declared scalar objective.

Expected result: no audit.

### Expensive audit

The challenge is diagnostic but uneconomic.

Expected result: no audit.

### Short horizon

Too little deployment remains to repay challenge and repair costs.

Expected result: no audit.

### Uninformative challenge

The offered audit preserves the same correlation as training.

Expected result: the agent audits but fails to expose hidden fragility.

This is the critical negative control.

---

## 7. Pass and failure conditions

The local claim receives support only if the adaptive skeptic:

1. improves expected net reward in the balanced ambiguous condition;
2. distinguishes robust from fragile worlds after a valid challenge;
3. avoids unconditional sensor deployment;
4. rejects challenge when cost, rarity, or horizon makes it uneconomic;
5. fails transparently when the challenge interface is itself non-diagnostic.

The broader theory claim remains blocked if the behavior is fully explained by:

- Bayesian value of information;
- active experiment design;
- costly information acquisition;
- robust or partially observable control.

---

## 8. Interpretation ceiling

A positive v0.2 run establishes only:

\[
\boxed{
\text{A predeclared challenge can reveal fragility hidden by successful training, and its use can be cost-sensitive.}
}
\]

It does not establish:

- autonomous generation of challenge operators;
- discovery of an unknown variable;
- revision of the target definition;
- open-ended interface invention;
- general scientific creativity;
- a novel theory beyond existing decision and experiment-design formalisms.

The remaining frontier is sharper:

\[
\boxed{
\text{Can a system discover that its available challenge interfaces share the same blind spot?}
}
\]
