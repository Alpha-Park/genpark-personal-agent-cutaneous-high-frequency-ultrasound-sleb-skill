---
name: genpark-personal-agent-cutaneous-high-frequency-ultrasound-sleb-skill
version: 1.0.0
description: Calculates 20-50 MHz High-Frequency Ultrasound (HFUS) Subepidermal Low-Echogenic Band (SLEB) thickness, Dermal Thickness, SLEB/Dermis ratio (SDR%), and Dermal Density Index (DDI%).
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - dermatology
  - ultrasound
  - hfus
  - sleb
  - photoaging
  - zero-dependency
---

# Cutaneous High-Frequency Ultrasound (HFUS) SLEB Skill

## Mathematical Formulation

Dermal depth conversion:

$$\text{Dermal Thickness} \, (\mu\text{m}) = \text{Dermal Thickness} \, (\text{mm}) \times 1000$$

Subepidermal Low-Echogenic Band (SLEB) to Dermis ratio:

$$\text{SDR} \, (\%) = \left(\frac{\text{SLEB} \, (\mu\text{m})}{\text{Dermal Thickness} \, (\mu\text{m})}\right) \times 100$$

Dermal Density Index (acoustic reflectance greyscale ratio):

$$\text{DDI} \, (\%) = \left(\frac{\text{Mean Dermal Greyscale}}{\text{Calibrated Max Greyscale}}\right) \times 100$$

## Clinical Grading
- **Grade 0-I (Intact / Photoprotected)**: $\text{SLEB} < 50 \, \mu\text{m}$, $\text{DDI} \ge 60\%$, $\text{SDR} < 5\%$
- **Grade II (Moderate Photoaging / Actinic Elastosis)**: $\text{SLEB} \in [50, 100] \, \mu\text{m}$, $\text{DDI} \in [45\%, 60\%]$
- **Grade III (Severe Solar Elastosis / Dermal Dissolution)**: $\text{SLEB} > 100 \, \mu\text{m}$, $\text{DDI} < 45\%$, $\text{SDR} > 10\%$
