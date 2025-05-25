# A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals

This repository contains the code, data, and documentation for the paper:

📄 **[A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals](insert-paper-link-here)**
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

### BibTeX

```bibtex
@article{Dear2025_strainrate_ML,
  author = {James Dear and Ruiqiang Zhang and Zhusheng Shi and Jianguo Lin},
  title = {A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals},
  year = {2025},
  note = {Under review. Available at GitHub Repository}
}
```

---

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
