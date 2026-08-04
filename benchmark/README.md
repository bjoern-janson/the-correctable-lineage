# Interface Benchmarks

Executable companions to the frozen benchmark specifications.

The implementations use only the Python standard library.

## v0.1 — Reactive interface diagnosis

Question:

> Can an adaptive system distinguish a failure caused by an insufficient model from one caused by an insufficient observation interface after contradiction is visible?

Run:

```bash
python benchmark/interface_evolution_v0_1.py --seeds 40
python -m unittest discover -s benchmark -p 'test_*.py' -v
```

Artifacts:

- `benchmark/results/results-v0.1.json`
- `benchmark/results/results-v0.1.md`
- `benchmark/negative-result-ledger-v0.1.md`

Boundary:

The result is compatible with active sensing, costly feature acquisition, and POMDP formulations.

## v0.2 — Hidden fragility and adaptive skepticism

Question:

> Can an agent pay to challenge an apparently successful interface before deployment, while avoiding maximum skepticism?

The first implementation is exploratory rather than independently preregistered. Its checks and generated result ledger are now frozen and replayed exactly in CI.

Run:

```bash
python benchmark/interface_stress_v0_2.py --seeds 200 --strict
python -m unittest discover -s benchmark -p 'test_*.py' -v
```

Artifacts:

- `benchmark/results/results-v0.2.md`
- `benchmark/negative-result-ledger-v0.2.md`

Boundary:

v0.2 supplies the challenge operator, prior, target, sensor, cost, and horizon. It remains compatible with Bayesian value of information and active experiment design. It does not test autonomous interface discovery.

## v0.3 — Correction-path diversity

Question:

> Can an agent select correction channels by their coverage of primary failures rather than marginal accuracy or correlated vote count?

The first implementation is exploratory. It receives labeled calibration data, a bounded candidate set, channel costs, and an externally declared stress weight.

Run:

```bash
python benchmark/interface_diversity_v0_3.py --seeds 100
python -m unittest discover -s benchmark -p 'test_interface_diversity_v0_3.py' -v
```

Artifacts:

- `benchmark/results/results-v0.3.json`
- `benchmark/results/results-v0.3.md`
- `benchmark/negative-result-ledger-v0.3.md`

Boundary:

v0.3 supports only a local selection result under a declared shared-blind-spot shift. It remains compatible with robust ensemble selection and decision under correlated errors. It does not generate independent tests or identify correction-path independence from success-only data.

## v0.4 — Correction-ecosystem intervention

Question:

> Can a supplied intervention expose a hidden upstream dependency shared by apparently independent correction channels?

The first implementation is exploratory. It receives the candidate channel set, target labels, hidden dependency, support-changing intervention, costs, shift prior, and deployment horizon.

Run:

```bash
python benchmark/correction_ecosystem_v0_4.py --seeds 100 --strict
python -m unittest discover -s benchmark -p 'test_correction_ecosystem_v0_4.py' -v
```

Artifacts:

- `benchmark/results/results-v0.4.json`
- `benchmark/results/results-v0.4.md`
- `benchmark/negative-result-ledger-v0.4.md`

Boundary:

v0.4 supports only the local claim that a supplied intervention on an upstream dependency can expose common-mode failure hidden by ordinary calibration and output decorrelation. It remains compatible with causal experiment design and robust selection under common-mode failure. It does not discover latent dependencies, generate interventions, or identify truth without an external correctness reference.
