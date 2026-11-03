"""
Example usage of Cutaneous High-Frequency Ultrasound SLEB Skill.
Demonstrates young photoprotected skin vs severe actinic elastosis photoaging.
"""

import json
from client import HighFrequencyUltrasoundSLEBClient


def main():
    print("=== Testing Cutaneous HFUS SLEB Skill ===")
    client = HighFrequencyUltrasoundSLEBClient()

    # 1. Young photoprotected volar forearm skin (SLEB = 25 um, Dermis = 1.35 mm, Dermal Greyscale = 175 -> DDI = 68.6%, SDR = 1.85%)
    res_intact = client.evaluate_sleb_metrics(
        sleb_thickness_um=25.0,
        total_dermal_thickness_mm=1.35,
        mean_dermal_echogenicity_greyscale=175.0,
        patient_age_years=26,
        anatomical_site="volar forearm"
    )
    print("\n[Case 1: Intact Young Photoprotected Skin]")
    print(json.dumps(res_intact, indent=2))

    # 2. Chronically sun-damaged dorsal forearm skin (SLEB = 145 um, Dermis = 1.05 mm, Dermal Greyscale = 95 -> DDI = 37.3%, SDR = 13.8%)
    res_photoaged = client.evaluate_sleb_metrics(
        sleb_thickness_um=145.0,
        total_dermal_thickness_mm=1.05,
        mean_dermal_echogenicity_greyscale=95.0,
        patient_age_years=68,
        anatomical_site="dorsal forearm"
    )
    print("\n[Case 2: Severe Actinic Elastosis / Dermal Photoaging]")
    print(json.dumps(res_photoaged, indent=2))

    # Assertions
    assert res_intact["indices"]["sleb_dermis_ratio_pct"] < 5.0
    assert "Intact" in res_intact["clinical_evaluation"]["photoaging_grade"]
    assert res_photoaged["indices"]["sleb_dermis_ratio_pct"] > 10.0
    assert "Severe" in res_photoaged["clinical_evaluation"]["photoaging_grade"]
    print("\n[SUCCESS] Cutaneous HFUS SLEB tests passed!")


if __name__ == "__main__":
    main()
