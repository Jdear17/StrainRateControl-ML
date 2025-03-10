# A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals

## Contents
- 📄 **Manuscript (PDF)** – The full research paper titled *"A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals"*, including background, methodology, results, and discussions.  
- 📊 **Supplementary Data** – Experimental datasets and additional figures or tables supporting the findings (e.g., strain distributions, temperature profiles, etc.).  
- 🔢 **Code** – Source code for the ML approach and analysis:  
  - **Data Preprocessing** scripts to format and normalize experimental data.  
  - **Model Training** code (LSTM network implementation) to learn the relationship between target conditions and required displacement.  
  - **Evaluation** scripts/notebooks to reproduce the results and generate comparison plots of strain rate error for conventional vs. ML approach.  
- 📚 **Instructions/Documentation** – Any additional notes or files (e.g., `requirements.txt` for dependencies) to help reproduce the experiments and results.  

## Usage Instructions
To get started with the materials in this repository, follow these steps:  

### 1. Clone the repository  
git clone <repo_url> cd <repo_name>

csharp
Copy
Edit

### 2. Setup environment  
Ensure you have Python 3.x installed. Install the required libraries by running:  
pip install -r requirements.txt

python
Copy
Edit

### 3. Prepare data  
The experimental dataset is provided in the `data/` directory (e.g., as CSV or MAT files). Ensure the file paths in the code point to the correct location of these data files.  

### 4. Run the code  
#### Train the model:  
python train_model.py

perl
Copy
Edit
or open `Model_Training.ipynb` to train the LSTM network.  

#### Evaluate the model:  
python evaluate_model.py

markdown
Copy
Edit
or use the notebook to generate plots and error metrics.  

### 5. Examine results  
Output figures and metrics will be generated, demonstrating the strain rate control performance.  

🔹 *Note:* If using a **GPU**, ensure the appropriate deep learning framework (e.g., TensorFlow or PyTorch with GPU support) is installed.  

## Contribution Guidelines
We welcome contributions, suggestions, and feedback from the community to improve this work:  
- **📝 Feedback and Issues**: If you encounter problems, have suggestions for improvements, or need clarification, please open an **issue** in this repository.  
- **🛠️ Contributing Code or Data**: Fork the repository and submit a pull request for any enhancements. Please include a clear description of changes and ensure your code is well-documented.  
- **💬 Discussion**: For general discussions or brainstorming new ideas related to this approach, you can start a discussion thread in the repository.  

By contributing, you agree to follow the repository’s **code of conduct** and best practices.  

## Citation
If you use the code, data, or findings from this repository in your research or engineering work, please cite the manuscript as follows:  

**James Dear, Ruiqiang Zhang, Zhusheng Shi, and Jianguo Lin (2025).**  
*A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals.*  

### BibTeX format:  
@article{Dear2025_strainrate_ML, author = {James Dear and Ruiqiang Zhang and Zhusheng Shi and Jianguo Lin}, title = {A Novel Data-Driven Machine Learning Approach for Improved Strain Rate Control in Thermomechanical Testing of Sheet Metals}, year = {2025}, note = {Under review. Available at GitHub Repository} }

markdown
Copy
Edit
📌 *Citing this work acknowledges the authors’ efforts and supports future development.*  

## License
🔖 This repository is licensed under the **MIT License**. See `LICENSE` for details.  

## Acknowledgments
This work was supported by the **Engineering and Physical Sciences Research Council (EPSRC)** under Grant **EP/R001715/1** as part of the **LightForm** project.  

## Contact
📧 Ruiqiang Zhang - **r.zhang17@imperial.ac.uk**  
📍 Department of Mechanical Engineering, Imperial College London, UK  
