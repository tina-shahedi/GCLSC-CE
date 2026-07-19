# GCLSC-CE — Green Closed-Loop Supply Chain with Cannibalization Effects

![GAMS](https://img.shields.io/badge/GAMS-Augmecon2-blue?style=flat)
![Python](https://img.shields.io/badge/Python-NSGA--II-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-green?style=flat)

Bi-objective **location–inventory–pricing** optimization for a green closed-loop supply chain network (GCLSC) in the automotive tire industry, explicitly modeling the **cannibalization effect (CE)** between new and remanufactured tires.

## Overview

Remanufactured products compete with new ones — the cannibalization effect — and this interplay shapes both profit and environmental outcomes in the tire industry. This project formulates two mathematical models for location-inventory-pricing that maximize profit while minimizing environmental impact:

1. **MINLP with a linear demand–price function**
2. **MINLP with an inverted-U demand–price function**

Both are solved exactly with the **augmented ε-constraint method (AUGMECON2)** in GAMS for small and medium instances, and with the **NSGA-II** meta-heuristic in Python for large instances.

## Repository structure

```text
.
├── gams/                        # AUGMECON2 implementations (GAMS)
│   ├── LinearAugmecon.gms       # linear demand–price model
│   └── InUnew-Augmecon.gms      # inverted-U demand–price model
├── python/
│   ├── linear-demand/           # NSGA-II for the linear demand–price model
│   │   ├── Main1.py             # model data, solution encoding, NSGA-II operators
│   │   └── Algorithm.py         # entry point — runs the search and plots the Pareto front
│   └── inverted-u-demand/       # NSGA-II for the inverted-U demand–price model
│       ├── Main1.py
│       └── Algorithm.py
├── requirements.txt
└── LICENSE.txt
```

## Getting started

**GAMS models**

1. Install [GAMS](https://www.gams.com/) with a MINLP-capable solver.
2. Open a model from `gams/` in GAMS IDE.
3. Adjust the input data in the file to your problem instance and run.

**NSGA-II (Python)**

```bash
pip install -r requirements.txt
cd python/linear-demand        # or python/inverted-u-demand
python Algorithm.py
```

The script runs the evolutionary search and plots the resulting Pareto front (profit vs. environmental impact).

## Related work

- Companion repository: [GCLSC](https://github.com/tina-shahedi/GCLSC) — green closed-loop supply chain design under uncertainty (GAMS + MATLAB).
- Shahedi, T., Aghsami, A., & Rabani, M. (2021). *Designing a green closed-loop supply chain network for the automotive tire industry under uncertainty.* Journal of Industrial and Systems Engineering, 13(4), 226–261. [Article](https://www.jise.ir/article_136455.html)

## License

Released under the [GPL-3.0 License](LICENSE.txt).
