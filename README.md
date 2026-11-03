# Cutaneous High-Frequency Ultrasound SLEB Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating 20-50 MHz High-Frequency Ultrasound (HFUS) Subepidermal Low-Echogenic Band (SLEB) thickness, Dermal Thickness, SLEB-to-Dermis ratio (SDR%), and Dermal Density Index (DDI%).

## Architecture

```mermaid
flowchart TD
    A[HFUS 20-50 MHz Acoustic Scan] --> B[Segment SLEB Band & Reticular Dermis]
    B --> C[Measure SLEB Depth um & Dermal Depth mm]
    C --> D[Compute SDR% & Dermal Density Index DDI%]
    D --> E[Stratify Photoaging Grade 0 to III]
```

## Quickstart

```python
from client import HighFrequencyUltrasoundSLEBClient

client = HighFrequencyUltrasoundSLEBClient()
result = client.evaluate_sleb_metrics(
    sleb_thickness_um=25.0,
    total_dermal_thickness_mm=1.35,
    mean_dermal_echogenicity_greyscale=175.0,
    patient_age_years=26
)
print(result)
```

## License

Apache-2.0
