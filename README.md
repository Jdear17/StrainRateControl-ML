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
2. **Setup environment**: Ensure you have Python 3.x installed. Install the required libraries by running:  

3. **Prepare data**: The experimental dataset is provided in the `data/` directory (e.g., as CSV or MAT files). Ensure the file paths in the code point to the correct location of these data files.  
4. **Run the code**:  
- Train the model:  
  ```
  python train_model.py
  ```
  or open `Model_Training.ipynb` to train the LSTM network.  
- Evaluate the model:  
  ```
  python evaluate_model.py
  ```
  or use the notebook to generate plots and error metrics.  
5. **Examine results**: Output figures and metrics will be generated, demonstrating the strain rate control performance.  

*Note:* If using a GPU, ensure the appropriate deep learning framework (e.g., TensorFlow or PyTorch with GPU support) is installed.

---

## Contribution Guidelines
We welcome contributions, suggestions, and feedback from the community to improve this work:

- **Feedback and Issues**: If you encounter problems, have suggestions for improvements, or need clarification, please open an issue in this repository.  
- **Contributing Code or Data**: Fork the repository and submit a pull request for any enhancements. Please include a clear description of changes and ensure your code is well-documented.  
- **Discussion**: For general discussions or brainstorming new ideas related to this approach, you can start a discussion thread in the repository.  

By contributing, you agree to follow the repository’s code of conduct and best practices.

---

## Citation
If you use the code, data, or findings from this repository in your research or engineering work, please cite the manuscript as follows:

**James Dear, Ruiqiang Zhang, Zhusheng Shi, and Jianguo Lin (2025).**  
*A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals.*  

**BibTeX format:**
```bibtex
@article{Dear2025_strainrate_ML,
author    = {James Dear and Ruiqiang Zhang and Zhusheng Shi and Jianguo Lin},
title     = {A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals},
year      = {2025},
note      = {Under review. Available at [GitHub Repository](https://github.com/YourUsername/StrainRateControl-ML)}
}


---

Now, follow these steps to set up your repository:

### **Steps to Create the GitHub Repository**
1. **Go to GitHub** ([https://github.com](https://github.com)) and sign in.  
2. Click on the **"+"** button (top-right corner) and select **"New repository"**.  
3. Set:
   - **Repository Name:** `StrainRateControl-ML`
   - **Description:** `Code, data, and manuscript for a data-driven ML approach to improved strain rate control in thermomechanical sheet metal tests.`
   - **Set to Public or Private**, based on your preference.  
   - Check **"Initialize with a README"** (optional, if you want to manually paste it).  
4. Click **"Create repository"**.  

---

### **Steps to Add Your Manuscript and README**
1. **Upload the Manuscript**:  
   - Click **"Add file" > "Upload files"**, then drag and drop `Manuscript - Clear version.docx`.  
   - Click **"Commit changes"**.  

2. **Add README.md** (If you didn't initialize with a README):  
   - Click **"Add file" > "Create new file"**.  
   - Name it `README.md`.  
   - Paste the **README content** above.  
   - Click **"Commit changes"**.  

---

### **Steps to Clone and Work Locally (Optional)**
If you want to work on this locally, run:
```bash
git clone https://github.com/YOUR_USERNAME/StrainRateControl-ML.git
cd StrainRateControl-ML
