# Pilot 0 Scoring Rubric

## Purpose

Pilot 0 measures whether the representations can be instantiated, revised, and adjudicated by outsiders.

It does not test comparative superiority.

All condition differences are descriptive feasibility signals unless a later preregistered study has adequate sample size and independent case construction.

---

## 1. Primary feasibility vector

Report:

\[
\boxed{
Y_{\mathrm{pilot}}
=
(C,F,H,R,T,A,J,G,L),
}
\]

where:

- \(C\): completion;
- \(F\): malformed representation rate;
- \(H\): reconstruction entropy;
- \(R\): repair convergence;
- \(T\): translation burden;
- \(A\): consequence-based action quality;
- \(J\): adjudication identifiability;
- \(G\): disagreement legibility;
- \(L\): ontology leakage and role-capture indicators.

Do not collapse the vector into one winner score during Pilot 0.

---

## 2. Completion and malformed records

### Completion rate

\[
C
=
\frac{\text{completed required records}}
{\text{assigned records}}.
\]

Record separately:

- completed without clarification;
- completed after standardized clarification;
- completed after prohibited inventor assistance;
- incomplete;
- abandoned.

### Malformed representation rate

A record is malformed when a required object cannot be interpreted or used according to the assigned manual.

\[
F
=
\frac{\text{materially malformed objects}}
{\text{required objects}}.
\]

Examples:

- scope field contains only confidence;
- evidence dependency is recorded as agreement strength;
- Bayesian likelihood and posterior are conflated;
- assurance evidence is listed without a supporting claim or inference;
- reopening condition is not connected to any response;
- action status contradicts the represented decision rule;
- unsupported-but-open is used to authorize current action without further evidence.

Ambiguity caused by the manual should be coded as specification failure, not participant error.

---

## 3. Reconstruction entropy

Reconstruction entropy measures how many materially distinct structures emerge from the same case and specification.

The goal is not exact notational identity.

### Object partitioning

For each representation, define a frozen set of comparison dimensions such as:

- number and content of material hypotheses or claims;
- validity-domain partition;
- dependency clusters;
- action permissions;
- unsupported-but-open possibilities;
- unresolved states;
- future revision triggers.

### Cluster-based estimate

Independent coders cluster reconstructions into behaviorally meaningful structure types.

Let \(p_k\) be the proportion in cluster \(k\).

\[
H_R
=
-\sum_k p_k\log p_k.
\]

Also report:

- number of clusters;
- singleton rate;
- coder agreement on clustering;
- whether clusters produce materially different later actions;
- whether apparent agreement depends on retrospective framework translation.

### Interpretation

- high structural entropy with low behavioral divergence may be acceptable representational plurality;
- high structural entropy with high behavioral divergence suggests underspecification;
- low entropy caused by rigid copying may not indicate understanding;
- low entropy plus poor action quality indicates stable but inadequate reconstruction.

---

## 4. Repair convergence

Repair convergence measures whether later evidence causes initially divergent records to move toward compatible defensible consequences.

### Action-state distance

Freeze a distance over action statuses:

\[
\{
\text{permitted},
\text{conditional},
\text{unsupported-open},
\text{suspended},
\text{prohibited},
\text{contested},
\text{underidentified}
\}.
\]

Unsupported-open must remain distinguishable from both permitted and prohibited.

Report pairwise distance before and after each evidence stage.

### Valid-structure convergence

Compare which earlier claims participants retain, narrow, mark unsupported-but-open, suspend, or reject.

### Reopening convergence

Compare whether participants identify similar future tests or triggers after contradiction.

### Guard against abstention and closure

Convergence to “unresolved” on every action is not automatically successful.

Convergence to “prohibited” on every unsupported claim is also not automatically successful.

Report:

- convergence toward adjudicator-permitted regions;
- convergence toward prohibited regions;
- convergence toward correctly unsupported-open regions;
- convergence through generalized abstention;
- convergence through generalized rejection;
- persistent contested divergence;
- whether convergence follows later evidence or panel-imposed interpretation.

---

## 5. Translation burden

Translation burden measures how much inventor or specialist mediation is required before a user can act competently.

Record:

- manual reading time;
- number of rereads;
- clarification count;
- clarification categories;
- administrator time per participant;
- representation completion time;
- correction time after feedback;
- number of terms participants redefine in their own words;
- delayed recall;
- willingness to use the method without its inventor.

A descriptive translation-burden index may be reported after the raw components:

\[
T_B
=
\alpha t_{\mathrm{learn}}
+
\beta n_{\mathrm{clarify}}
+
\gamma t_{\mathrm{admin}}
+
\delta F,
\]

but no universal weights are assumed.

Sensitivity to plausible weights must be shown.

---

## 6. Consequence-based quality

Use the plural adjudication template.

Report separate scores for:

1. evidence fidelity;
2. action defensibility;
3. valid-structure retention;
4. unsupported extension prevention;
5. dependency handling;
6. future correction path;
7. stakeholder-loss transparency;
8. open-status calibration;
9. disagreement legibility.

Do not reward use of framework vocabulary.

Do not penalize method-native terminology.

### Valid-structure retention

Let \(V^*\) be propositions the panel judges retainable and \(\widehat V\) those retained by the participant.

\[
P_V
=
\frac{|\widehat V\cap V^*|}{|\widehat V|},
\]

\[
R_V
=
\frac{|\widehat V\cap V^*|}{|V^*|}.
\]

Where \(V^*\) is contested, report score ranges across defensible panel records.

### Unsupported extension

\[
O_G
=
\frac{\text{unsupported promoted claims or actions}}
{\text{promotion opportunities}}.
\]

### Unsupported-open preservation

Let \(U^*\) be possibilities judged unsupported-but-open and \(\widehat U\) those preserved by the participant without present authorization.

Report:

\[
P_U
=
\frac{|\widehat U\cap U^*|}{|\widehat U|},
\]

\[
R_U
=
\frac{|\widehat U\cap U^*|}{|U^*|}.
\]

This detects two opposite errors:

- granting authority to an unsupported possibility;
- converting lack of present support into permanent rejection.

### Under-generalization

Record valid actions withheld without sufficient reason.

This prevents generalized skepticism from masquerading as governance quality.

---

## 7. Disagreement legibility

Pilot 0 tests whether a representation can compress expert disagreement into inspectable components without forcing consensus.

For each material disagreement, coders assign one or more source labels:

- hypothesis partition;
- evidence interpretation;
- measurement assumption;
- scope;
- dependency model;
- stakeholder loss;
- action threshold;
- reopening condition;
- manual ambiguity;
- case underidentification;
- factual error;
- irreducibly mixed or unclassifiable.

### Legibility coverage

Let \(N_D\) be the number of material disagreements and \(N_L\) those assigned a stable source by independent coders.

\[
G_C
=
\frac{N_L}{N_D}.
\]

Report with:

- coder agreement on source labels;
- multi-label frequency;
- unclassifiable proportion;
- whether localization changes the next evidence request;
- whether localization permits operational coexistence;
- whether localization enables a targeted test or negotiated action;
- time required to translate disagreement into a shared record.

### Behavioral value

High disagreement legibility is useful only if it improves at least one of:

- targeted evidence acquisition;
- valid coexistence of different actions or scopes;
- repair convergence under later evidence;
- avoidance of false consensus;
- avoidance of premature rejection.

A framework-specific relabeling performed after the fact does not count.

---

## 8. Adjudication identifiability

Report:

- agreement on permitted actions;
- agreement on prohibited actions;
- agreement on unsupported-but-open actions;
- contested-action proportion;
- underidentified-action proportion;
- agreement on valid structure to retain;
- agreement on material dependency;
- agreement on whether later evidence should trigger revision;
- number of items that cannot be scored without framework vocabulary.

### Case identifiability classes

Classify each stage:

- **highly identifiable** — narrow permitted and prohibited regions with high panel agreement;
- **partially identifiable** — clear current boundaries but multiple defensible actions;
- **open but unsupported** — plausible future possibility remains without current authority;
- **value-sensitive** — factual agreement but stakeholder losses differ;
- **model-sensitive** — alternative causal accounts remain;
- **underidentified** — case evidence does not support stable scoring.

Underidentified cases may be useful qualitative probes but should not anchor comparative performance claims.

---

## 9. Ontology leakage and role capture

Record binary or graded indicators:

- case wording reveals the intended framework distinction;
- participant recognizes a benchmark pattern from the repository;
- framework author provides nonstandard clarification;
- comparator manual is less complete than its mature practice;
- adjudicator uses claim-contract terms as scoring criteria;
- analyst changes exclusions after condition labels are known;
- one role controls case, score, and interpretation;
- divergent reconstructions are retrospectively translated into the author’s preferred representation;
- adjudicator consensus is treated as ground truth without recording alternatives;
- unsupported-but-open possibilities are forced into accepted/rejected categories.

Any material leakage must be included in interpretation.

---

## 10. Scoped governance loss

For each case, adjudicators record a family of plausible losses:

\[
\Lambda_{\mathrm{case}}
=
\Lambda(S,D,\tau,K),
\]

where:

- \(S\): stakeholders;
- \(D\): domain;
- \(\tau\): time horizon;
- \(K\): consequence and reversibility model.

Pilot 0 asks whether the representation exposes and supports revision of these assumptions.

It does not identify one correct scalar loss.

Report:

- which actions change under different plausible stakeholder weights;
- whether participants make the weights visible;
- whether representations permit loss revision without rebuilding the entire record;
- whether the representation hides value judgments inside technical confidence;
- whether disagreements classified as factual are actually loss disagreements.

---

## 11. Descriptive go/no-go criteria

Exact thresholds must be frozen in the preregistration after independent review.

Candidate go signals:

- most participants complete records without inventor help;
- malformed-field rate is low enough for adjudication;
- clarification requests cluster around fixable manual ambiguities;
- reconstruction entropy is interpretable rather than chaotic;
- repair convergence improves after later evidence;
- unsupported-open states are preserved without unauthorized action;
- material disagreements can be localized with acceptable coder agreement;
- consequence scores can be assigned without framework vocabulary;
- comparator stewards judge their manuals faithful;
- translation burden is measurable and not prohibitive.

Candidate no-go signals:

- completion depends on inventor mediation;
- high entropy produces incompatible actions with no case-based resolution;
- adjudicators cannot distinguish contested, unsupported-open, and underidentified regions;
- disagreement becomes legible only through retrospective author translation;
- one condition receives hidden extra information;
- framework terms are required to score success;
- participants use generalized abstention to avoid every error;
- participants or adjudicators convert every unsupported possibility into rejection;
- minimal method-native augmentations erase the apparent distinction.

---

## 12. Reporting format

For each condition and case report:

- raw participant records;
- completion and malformed rates;
- clarification logs;
- reconstruction clusters;
- repair trajectories;
- consequence scores with panel uncertainty;
- unsupported-open preservation;
- disagreement-source maps;
- disagreement-legibility coverage and coder agreement;
- complexity and translation burden;
- leakage incidents;
- manual revisions required;
- negative-result ledger entries.

No leaderboard rank should be reported for Pilot 0.
