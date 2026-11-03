"""
Cutaneous High-Frequency Ultrasound (HFUS) Subepidermal Low-Echogenic Band (SLEB) Client.
Zero-mock pure Python standard library implementation.
Calculates Subepidermal Low-Echogenic Band (SLEB) thickness (microns),
Dermal Thickness (mm), SLEB-to-Dermis ratio (SDR%), and Dermal Density Index (DDI%).
"""

import math
from typing import Dict, Any, Optional


class HighFrequencyUltrasoundSLEBClient:
    """
    Evaluates cutaneous photoaging and dermal extracellular matrix degradation via 20-50 MHz HFUS:
    - SLEB thickness: edema, elastosis, glycosaminoglycan accumulation directly beneath epidermal echo
    - Dermal thickness: distance from dermo-epidermal junction to subcutaneous fat boundary
    - SDR%: (SLEB_um / (dermal_thickness_mm * 1000.0)) * 100.0
    - DDI%: percentage mean acoustic backscatter intensity of reticular dermis relative to intact calibrated standard
    """

    def __init__(self):
        pass

    def evaluate_sleb_metrics(
        self,
        sleb_thickness_um: float,
        total_dermal_thickness_mm: float,
        mean_dermal_echogenicity_greyscale: float,
        calibrated_max_greyscale: Optional[float] = 255.0,
        patient_age_years: Optional[int] = 40,
        anatomical_site: Optional[str] = "forearm"
    ) -> Dict[str, Any]:
        """
        Calculates HFUS dermal matrix integrity parameters.
        sleb_thickness_um: thickness of SLEB in micrometers (0 to 400 um)
        total_dermal_thickness_mm: total dermal depth in millimeters (0.5 to 3.0 mm)
        mean_dermal_echogenicity_greyscale: mean pixel intensity of reticular dermis (0 to 255)
        calibrated_max_greyscale: reference max greyscale intensity (default 255.0)
        """
        if sleb_thickness_um < 0 or total_dermal_thickness_mm <= 0:
            raise ValueError("SLEB thickness must be non-negative and dermal thickness strictly positive.")
        if mean_dermal_echogenicity_greyscale < 0 or mean_dermal_echogenicity_greyscale > calibrated_max_greyscale:
            raise ValueError(f"Dermal echogenicity must be between 0 and {calibrated_max_greyscale}.")

        dermal_thickness_um = total_dermal_thickness_mm * 1000.0
        if sleb_thickness_um > dermal_thickness_um:
            raise ValueError("SLEB thickness cannot exceed total dermal thickness.")

        # SLEB-to-Dermis Ratio (SDR %)
        sdr_pct = (sleb_thickness_um / dermal_thickness_um) * 100.0

        # Dermal Density Index (DDI %)
        ddi_pct = (mean_dermal_echogenicity_greyscale / calibrated_max_greyscale) * 100.0

        # Clinical photoaging / solar elastosis classification:
        # SLEB < 50 um and DDI >= 60%: Intact Juvenile / Photoprotected Dermis
        # SLEB 50 - 100 um or DDI 45 - 60%: Mild-to-Moderate Solar Elastosis / Chronic Photodamage
        # SLEB > 100 um or DDI < 45%: Severe Actinic Elastosis / Advanced Dermal Matrix Degradation
        if sleb_thickness_um < 50.0 and ddi_pct >= 60.0:
            photoaging_grade = "Grade 0-I: Intact Photoprotected Dermal Matrix"
            matrix_integrity = "Dense organized collagen and elastic bundles with minimal subepidermal elastosis."
        elif sleb_thickness_um <= 100.0 and ddi_pct >= 45.0:
            photoaging_grade = "Grade II: Moderate Actinic Elastosis / Photoaging"
            matrix_integrity = "Emergence of subepidermal low-echogenic band reflecting degraded elastotic fibers and localized extracellular edema."
        else:
            photoaging_grade = "Grade III: Severe Solar Elastosis & Dermal Matrix Dissolution"
            matrix_integrity = "Prominent SLEB band with profound loss of reticular dermal echodensity, typical of severe UV chronicity or topical corticosteroid atrophy."

        return {
            "status": "success",
            "ultrasound_measurements": {
                "sleb_thickness_um": round(sleb_thickness_um, 1),
                "total_dermal_thickness_mm": round(total_dermal_thickness_mm, 3),
                "dermal_thickness_um": round(dermal_thickness_um, 1),
                "mean_dermal_echogenicity_greyscale": round(mean_dermal_echogenicity_greyscale, 1)
            },
            "indices": {
                "sleb_dermis_ratio_pct": round(sdr_pct, 2),
                "dermal_density_index_pct": round(ddi_pct, 1)
            },
            "clinical_evaluation": {
                "photoaging_grade": photoaging_grade,
                "matrix_integrity_assessment": matrix_integrity,
                "anatomical_site": anatomical_site
            }
        }
