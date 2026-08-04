# Pilot 0 Neutral Cases

## Administration rule

Release one stage at a time.

Participants must complete the common response template before receiving the next stage.

Do not introduce framework-specific terms during administration.

The cases are synthetic feasibility materials, not validated reconstructions of real events.

---

# Case 1 — Replication and Measurement

## Domain context

A research group reports that a short digital intervention improves concentration during a 20-minute sustained-attention task.

The intervention is inexpensive and could be deployed widely in schools and workplaces.

### Stakeholders

- research participants;
- schools and employers considering deployment;
- researchers building on the result;
- funders allocating follow-up resources.

### Decision horizon

Initial research decisions occur within six months. Broad deployment decisions occur within two years.

---

## Stage 1

The original study includes 120 university students.

Participants are randomized to either:

- the digital intervention; or
- a visually similar control activity.

The intervention group makes 18% fewer errors on the sustained-attention task.

The preregistered primary analysis reports \(p<0.01\), and the result is robust to two preregistered covariate adjustments.

A second laboratory using the same software and scoring code repeats the study with 100 students and reports a 15% reduction in errors.

### Required response

Record:

- what you currently conclude;
- how strongly you support each conclusion;
- which populations or uses are covered;
- which actions are permitted now;
- which evidence you would seek next;
- what future result would materially change your position.

---

## Stage 2

A third laboratory studies 240 adult office workers.

It uses the same intervention but a different sustained-attention task and different scoring software.

The study finds no meaningful difference between intervention and control.

The confidence interval excludes effects larger than a 3% error reduction on that task.

The third laboratory reports no obvious protocol violation.

### Required response

Update the same record.

Identify:

- which earlier conclusions remain supported;
- which conclusions should change;
- whether any action should stop, continue, or become conditional;
- which unresolved explanations now matter.

---

## Stage 3

An audit finds that the original and second laboratories used the same task software package.

During both studies, the intervention altered browser timing behavior in a way that changed how very fast responses were recorded.

The scoring code treated some responses as correct when they would have been classified as premature responses by the third laboratory's software.

Reanalysis with corrected timing rules reduces the original estimated effect from 18% to 4%, with a wide confidence interval that includes no effect.

The second study's raw timing logs were not retained, so equivalent reanalysis is impossible.

### Required response

Update the record again.

State:

- what remains worth preserving;
- which claims or actions lose support;
- what evidence would most efficiently resolve the remaining uncertainty;
- whether any earlier conclusion should be considered closed, suspended, or still locally usable.

---

## Stage 4

A new multisite study uses audited timing software, three attention tasks, and 900 participants across students and office workers.

It finds an average 2% reduction in errors, with meaningful variation by task and no clear benefit in office workers.

The intervention causes no measured harm but requires approximately 20 minutes of staff time per participant.

### Required response

Make a final pilot-stage recommendation.

Separate:

- conclusions about whether any effect exists;
- conclusions about effect size;
- conclusions about populations and tasks;
- research-use recommendations;
- deployment recommendations.

---

# Case 2 — Engineering Assurance

## Domain context

A manufacturer develops an automated shutdown controller for an industrial cooling system.

The controller is intended to prevent equipment damage when coolant pressure becomes unsafe.

### Stakeholders

- plant operators;
- nearby communities;
- maintenance teams;
- manufacturer and regulators.

### Decision horizon

Certification is planned within nine months. Once installed, replacement requires a scheduled shutdown costing several million euros.

---

## Stage 1

The controller is tested in 10,000 simulated fault sequences generated from the manufacturer's process model.

It issues the correct shutdown command in 99.97% of sequences.

A hardware-in-the-loop test facility repeats 2,000 sequences and observes no unsafe failure.

An independent assessor confirms that the controller implementation matches the reviewed software specification.

### Required response

Record:

- current certification and deployment recommendation;
- strength and limits of the supporting evidence;
- required monitoring or follow-up;
- conditions that would reverse the recommendation.

---

## Stage 2

During a maintenance test, a pressure sensor intermittently reports stale readings for 800 milliseconds.

The controller does not issue a shutdown because the reported pressure remains inside the permitted range.

The plant's mechanical backup prevents damage.

The manufacturer argues that the software behaved exactly as specified and that the event is therefore not a controller failure.

### Required response

Update the recommendation.

State:

- which component or claim is affected;
- whether the previous evidence remains useful;
- which operational permissions should change;
- which investigation has priority.

---

## Stage 3

Investigation shows that:

- the simulator assumed fresh sensor values every 100 milliseconds;
- the hardware-in-the-loop facility used the same sensor-behavior model;
- the software specification did not define behavior under stale but syntactically valid readings;
- the mechanical backup is rated for only three activations before mandatory replacement.

A software patch can detect stale readings, but it has been tested only in simulation.

### Required response

Update the record.

Separate conclusions about:

- the original software implementation;
- the original specification;
- the testing process;
- the system-level safety case;
- immediate plant operation;
- patch deployment.

---

## Stage 4

A revised controller with stale-reading detection passes:

- independent code review;
- fault-injection testing using three independently implemented sensor models;
- 500 hours of supervised operation in one plant.

During supervised operation, the stale-reading detector triggers twice. Both triggers are confirmed as genuine sensor faults.

No unsafe shutdown failure occurs.

However, the revised controller produces one unnecessary shutdown because of a configuration error during maintenance.

### Required response

Make a final recommendation.

Include:

- deployment conditions;
- monitoring requirements;
- evidence still missing;
- acceptable and unacceptable residual risks;
- conditions for later suspension or wider deployment.

---

# Case 3 — Machine-Learning Deployment

## Domain context

A hospital develops a machine-learning system that predicts which emergency-department patients are likely to require intensive care within 24 hours.

The score is intended to support—not replace—clinical judgment.

### Stakeholders

- patients;
- clinicians;
- hospital administrators;
- external hospitals considering adoption;
- regulators and payers.

### Decision horizon

Local deployment can begin within three months. External licensing decisions are expected within one year.

---

## Stage 1

The model is trained on five years of data from Hospital A.

On a held-out year from Hospital A it achieves:

- area under the ROC curve: 0.91;
- good aggregate calibration;
- a 20% reduction in missed intensive-care admissions in a silent prospective evaluation.

Two retrospective validation studies report similar discrimination:

- one using a regional research dataset;
- one using a commercial benchmark dataset.

Hospital A proposes live deployment and external licensing.

### Required response

Record:

- current confidence in the model;
- permitted local and external uses;
- monitoring requirements;
- evidence needed before broader adoption;
- conditions that would reduce deployment authority.

---

## Stage 2

Hospital B deploys the model under clinician supervision.

After two months:

- discrimination falls to 0.74;
- calibration is poor for older patients;
- clinicians override the score frequently;
- no clear patient-outcome benefit is observed.

Hospital A's performance remains stable.

### Required response

Update the record.

Separate:

- local performance at Hospital A;
- transfer performance at Hospital B;
- model validity;
- deployment authorization;
- licensing claims.

---

## Stage 3

An audit finds that Hospital A, the regional research dataset, and the commercial benchmark all used versions of the same vendor preprocessing pipeline.

The pipeline converts missing respiratory measurements into a value that indirectly identifies whether a patient was placed on a high-acuity monitoring pathway.

Hospital B uses a different missing-data process.

The model relies heavily on this converted value.

Hospital A argues that the feature remains predictive and therefore should remain in use locally.

### Required response

Update the record.

State:

- which evidence sources remain distinct;
- which conclusions should be preserved or narrowed;
- whether local use should continue;
- what testing would discriminate safe local utility from brittle proxy dependence.

---

## Stage 4

A revised model removes the vendor-derived feature and is tested prospectively for six months at Hospitals A, B, and C.

Results:

- discrimination ranges from 0.82 to 0.86;
- calibration is acceptable after site-specific intercept adjustment;
- missed intensive-care admissions fall by 8%;
- false alerts rise by 12%;
- clinicians report moderate alert burden;
- benefits are uncertain for patients over age 85 because of small sample size.

### Required response

Make a final recommendation.

Separate:

- model-performance conclusions;
- population and site limits;
- local deployment permissions;
- cross-site transfer claims;
- monitoring and reopening triggers;
- stakeholder tradeoffs between missed admissions and false alerts.

---

# Administration notes

Do not tell participants which case feature is intended to test measurement, dependency, scope, reopening, or any other framework category.

Clarification answers must be factual and standardized.

All clarification requests must be logged.

Do not reveal later stages early.

The same staged information must be supplied to every representation condition.
