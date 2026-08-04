# Interface Evolution Benchmark v0.1

Executable companion to [`../interface-evolution-benchmark-v0.1.md`](../interface-evolution-benchmark-v0.1.md).

## Frozen question

Can an adaptive system distinguish a failure caused by an insufficient model from one caused by an insufficient observation interface?

The implementation deliberately uses a predeclared paid sensor. It tests selective interface acquisition, not autonomous sensor or ontology generation.

## Run

```bash
python benchmark/interface_evolution_v0_1.py --seeds 40
python -m unittest discover -s benchmark -p 'test_*.py' -v
```

The benchmark uses only the Python standard library.

Generated artifacts:

- `benchmark/results/results-v0.1.json`
- `benchmark/results/results-v0.1.md`

## Agents

- `fixed_interface`: updates a cue-conditioned model but cannot acquire the sensor.
- `oracle_interface`: receives the sensor on every episode and pays its cost.
- `interface_revision`: begins with the initial cue, probes the offered sensor after persistent low accuracy, and activates it only when estimated net value exceeds the fixed-interface alternative.

## Scenarios

- hidden collision;
- sufficient initial interface;
- useless added sensor;
- informative but uneconomic sensor;
- moderate held-out prevalence/noise shift;
- spurious training cue removed at evaluation.

## Interpretation boundary

The implementation is compatible with active sensing, costly feature acquisition, and POMDP formulations. A positive run does not establish a distinct general theory of interface evolution.
