# A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals

This repository contains the code, data, and documentation for the paper:

📄 **[A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals](https://doi.org/10.1016/j.engappai.2025.110746)**
by James Dear, Ruiqiang Zhang, Zhusheng Shi, and Jianguo Lin, 2025.

---

## 📦 Contents

* **Manuscript** – Full PDF of the research paper \[link above].
* **Experimental Data** – Raw and processed datasets under `data/`, including strain field evolution and temperature profiles.
* **Source Code**

  * `src/data_processing.py`: preprocessing and feature generation
  * `src/model.py`: LSTM model definition
  * `train.py`: training script
* **Notebooks** – Interactive exploration and visualisation (in `notebooks/`).
* **Documentation** – `requirements.txt`, usage instructions, and citation info.

---

## 🚀 Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/Jdear17/StrainRateControl-ML.git
cd StrainRateControl-ML
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> ✅ Python 3.8+ and TensorFlow 2.x recommended.

### 3. Prepare the data

Ensure the raw `.xlsx` files are in `data/raw/`. These contain experimental strain field measurements for different temperature and strain rate conditions.

### 4. Train the model

To train the LSTM model using the default setup:

```bash
python train.py
```

Or use the notebook version:

```bash
notebooks/analysis.ipynb
```

### 5. Evaluate performance

Output metrics and plots will be generated showing predicted vs. experimental strain fields and strain rate control error.

---

## 📈 Reproducing Results

The training/validation split follows the paper’s experimental protocol. Strain centre, temperature, and estimated strain rate are used as input features, and the output is the full strain field in the x-direction.

All model hyperparameters and training settings are defined in `train.py`.

---

## 📚 Citation

If you use this repository in your work, please cite:

**James Dear, Ruiqiang Zhang, Zhusheng Shi, and Jianguo Lin (2025).**
*A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals.*

## 📚 Citation

If you use this repository in your work, please cite:

**James Dear, Ruiqiang Zhang, Zhusheng Shi, and Jianguo Lin (2025).**  
*A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals.*

## 📚 Citation

If you use this repository in your work, please cite:

**James Dear, Ruiqiang Zhang, Zhusheng Shi, and Jianguo Lin (2025).**  
*A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals.*

### BibTeX

```bibtex
@article{DEAR2025110746,
  title     = {A novel data-driven machine learning approach for improved strain rate control in thermomechanical testing of sheet metals},
  author    = {James Dear and Ruiqiang Zhang and Zhusheng Shi and Jianguo Lin},
  journal   = {Engineering Applications of Artificial Intelligence},
  volume    = {151},
  pages     = {110746},
  year      = {2025},
  issn      = {0952-1976},
  doi       = {10.1016/j.engappai.2025.110746},
  url       = {https://www.sciencedirect.com/science/article/pii/S0952197625007468},
  keywords  = {Uniaxial tensile test, Sheet metal, Strain rate control, Hot stamping, Thermomechanical behaviour, Long short-term memory},
  abstract  = {Thermomechanical tests on sheet metals are commonly conducted using Gleeble systems to investigate their viscoplastic behaviour. Accurate strain rate control is crucial in these tests to accurately determine the material's thermomechanical properties...}
}


## 🧱 Contributing

* 🐛 Found a bug? Open an [issue](https://github.com/Jdear17/StrainRateControl-ML/issues).
* 💡 Have an idea or improvement? Submit a pull request.
* 🙏 By contributing, you agree to follow the repository’s code of conduct.

---

## 📄 License

MIT License — see `LICENSE` for details.

---

## 🧠 Acknowledgements

This research was supported by the **Engineering and Physical Sciences Research Council (EPSRC)**, Grant **EP/R001715/1**, under the **LightForm** project.

---

## 📬 Contact

**James Dear**
📧 [james.dear17@imperial.ac.uk](mailto:james.dear17@imperial.ac.uk)
📍 Department of Mechanical Engineering, Imperial College London, UK
