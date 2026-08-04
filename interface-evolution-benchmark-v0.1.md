# Interface Evolution Benchmark v0.1

## Status

Minimal benchmark proposal.

This file freezes the current ontology and tests one claim:

\[
\boxed{
\text{A system can fail because its interface collapses a task-relevant distinction, not because its model is insufficient.}
}
\]

It does not validate a universal theory of intelligence, interface evolution, or recursive improvement.

---

## 1. Claim

An interface-capable system should outperform a model-only learner when:

1. the initial interface makes the target non-identifiable;
2. a bounded interface revision makes the target identifiable;
3. contradiction can trigger the revision;
4. the benefit survives held-out evaluation after revision cost is charged.

The benchmark distinguishes:

\[
M_t\rightarrow M_{t+1}
\]

from:

\[
\mathcal I_t\rightarrow\mathcal I_{t+1}.
\]

---

## 2. Minimal formalism

Let:

- \(s_t\in\mathcal S\): latent environment state;
- \(O_0:\mathcal S\rightarrow\mathcal Z_0\): initial interface;
- \(O_1:\mathcal S\rightarrow\mathcal Z_1\): candidate revised interface;
- \(L:\mathcal S\rightarrow\mathcal Y\): target required for correct action;
- \(a_t\in\mathcal A\): action;
- \(r_t\): reward or loss;
- \(c_I>0\): cost of activating the revised interface.

The initial interface must contain a declared collision:

\[
\exists s_a,s_b:
O_0(s_a)=O_0(s_b)
\quad\text{and}\quad
L(s_a)\neq L(s_b).
\]

Therefore no estimator based only on \(O_0\) can identify \(L\) over the declared class.

The revised interface must separate the collision:

\[
O_1(s_a)\neq O_1(s_b),
\]

and admit factorization:

\[
L=\widehat L_1\circ O_1.
\]

---

## 3. Experimental environment

Use a two-regime decision task.

At each episode:

1. sample latent regime \(h\in\{0,1\}\);
2. emit the same visible cue \(x\) under both regimes;
3. require action \(a=h\) for success;
4. return binary reward;
5. optionally permit one paid sensor request revealing \(h\), with preregistered noise \(\epsilon\).

Initial interface:

\[
O_0(h,x)=x.
\]

Revised interface:

\[
O_1(h,x)=(x,\tilde h),
\]

where \(\tilde h=h\) with probability \(1-\epsilon\).

Under balanced regimes, the best fixed-interface policy cannot exceed chance accuracy when no other predictive history is available.

---

## 4. Agents

### Baseline A: fixed-interface learner

May update parameters and policies using \(O_0\), actions, and rewards.

It cannot request, construct, or activate \(O_1\).

### Baseline B: oracle-interface learner

Receives \(O_1\) from the first episode.

This estimates the achievable ceiling and sensor value.

### Test agent: interface-revision learner

Begins with \(O_0\).

It may:

- detect persistent residual structure;
- choose whether and when to pay \(c_I\);
- activate \(O_1\);
- update its policy after activation.

The benchmark does not require the agent to invent arbitrary sensors. It tests bounded selection between a declared inadequate interface and a declared candidate repair.

---

## 5. Primary metrics

### Held-out regret

\[
R_H
=
\sum_{t\in H}
(r_t^*-r_t)
+
N_Ic_I,
\]

where \(H\) is a held-out episode set and \(N_I\) is the number of paid interface activations.

### Interface-revision latency

Number of contradictory episodes before activating \(O_1\).

### False-revision rate

Frequency of activating \(O_1\) in matched control tasks where \(O_0\) is already sufficient.

### Collision-resolution gain

Performance difference specifically on pairs collapsed by \(O_0\) and separated by \(O_1\).

### Transfer

Performance when regime frequencies, sensor noise, or reward costs change within preregistered bounds.

---

## 6. Required controls

### Sufficient-interface control

Construct a matched task where:

\[
L=\widehat L_0\circ O_0.
\]

A competent agent should avoid unnecessary revision.

### Useless-sensor control

Offer an added feature independent of \(L\).

More information must not automatically earn interface authority.

### Expensive-sensor control

Set \(c_I\) above the maximum expected benefit.

A rational agent should preserve the inadequate but cheaper interface when revision cannot repay its cost.

### Spurious-training control

Provide a training-only correlation visible under \(O_0\), then remove it on held-out episodes.

This tests whether model refinement overfits an insufficient partition.

---

## 7. Pass condition

The interface-revision claim receives support only if the test agent:

1. performs no worse than the fixed-interface learner before sufficient evidence accumulates;
2. activates \(O_1\) selectively in the non-identifiable task;
3. avoids revision in the sufficient-interface and useless-sensor controls;
4. reduces held-out regret after charging \(c_I\);
5. localizes improvement to distinctions newly available under \(O_1\);
6. retains the gain under preregistered transfer conditions.

---

## 8. Falsification criteria

The benchmark claim fails or becomes unnecessary if any of the following holds:

1. a model-only learner using \(O_0\) matches revised-interface performance without undeclared information;
2. \(L\) was already identifiable from \(O_0\);
3. improvement comes from extra compute, training time, or privileged feedback rather than the new distinction;
4. the test agent requests every available sensor regardless of contradiction;
5. gains disappear after interface cost is included;
6. the revised interface improves training performance but not held-out collision cases;
7. a simpler active-learning, feature-selection, or partially observable decision model explains the result without requiring a distinct interface-evolution claim.

---

## 9. Interpretation limits

A positive result would establish only that, in this declared task:

- the initial interface erased a target-relevant distinction;
- bounded interface revision restored that distinction;
- selective revision improved held-out performance.

It would not establish:

- autonomous invention of new sensors;
- open-ended ontology generation;
- general scientific creativity;
- self-understanding;
- safe recursive self-improvement;
- a universal intelligence metric;
- superiority over existing active perception or representation-learning frameworks.

---

## 10. Minimum implementation

A valid v0.1 implementation needs only:

- one latent binary variable;
- one colliding initial observation;
- one optional noisy sensor;
- three agents;
- four controls;
- fixed random seeds;
- preregistered costs and thresholds;
- held-out evaluation;
- a frozen result ledger.

No additional conceptual layer is required.

---

## Final criterion

\[
\boxed{
\text{The benchmark matters only if interface revision explains a measurable gain that model revision alone cannot obtain through the declared interface.}
}
\]
