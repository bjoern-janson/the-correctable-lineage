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
