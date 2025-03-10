# A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals

## Abstract
Thermomechanical tests on sheet metals (using Gleeble systems) require accurate strain rate control to determine material properties, but temperature gradients along the specimen make this challenging with conventional methods. To address this, we developed a novel data-driven Machine Learning (ML) approach for strain rate control based on characteristics of experimental data from the conventional method. This approach uses Long Short-Term Memory (LSTM) neural networks with inputs of target deformation temperature and target strain rate, and outputs the strain distribution along the specimen gauge length during deformation. The predicted strain distribution is integrated over the gauge length to compute the time-dependent displacement required to achieve the target strain rate throughout the test.

Uniaxial hot-stamping tensile tests on an aluminum alloy were conducted to compare the conventional and ML-based control methods. The experimental data from the conventional approach were used to train and validate the LSTM model. **Results:** The ML-driven approach significantly improves strain rate control. The conventional method can produce a Percentage Error (PE) up to ~770% and Mean Absolute Percentage Error (MAPE) up to ~120% in strain rate, whereas the ML approach reduces both errors by over 88%. This demonstrates that the proposed ML method provides an effective solution for controlling strain rate in thermomechanical testing, enabling more accurate determination of the material’s thermomechanical properties.

---

## Contents
- **Manuscript (PDF)** – The full research paper titled *"A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals"*, including background, methodology, results, and discussions.  
- **Supplementary Data** – Experimental datasets and additional figures or tables supporting the findings (e.g. strain distributions, temperature profiles, etc.).  
- **Code** – Source code for the ML approach and analysis:
  - *Data Preprocessing* scripts to format and normalize experimental data.  
  - *Model Training* code (LSTM network implementation) to learn the relationship between target conditions and required displacement.  
  - *Evaluation* scripts/notebooks to reproduce the results and generate comparison plots of strain rate error for conventional vs. ML approach.  
- **Instructions/Documentation** – Any additional notes or files (e.g. `requirements.txt` for dependencies) to help reproduce the experiments and results.

---

## Usage Instructions
To get started with the materials in this repository, follow these steps:

1. **Clone the repository**:  
