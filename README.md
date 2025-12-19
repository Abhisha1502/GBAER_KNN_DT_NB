
👩‍💻 Author

Abhisha
B.E. Artificial Intelligence and Data Science

📜 License

This project is developed for academic purposes.# Global Pollution Analysis and Energy Recovery

## 📌 Project Overview
This project focuses on analyzing global pollution data and classifying countries into different pollution severity categories — **Low, Medium, and High** — using machine learning techniques. The classification is based on pollution indicators, energy consumption, and environmental factors.

The project demonstrates the complete machine learning workflow including data preprocessing, feature engineering, model training, evaluation, and insight generation.

---

## 🎯 Objective
The main objectives of this project are:
- To preprocess and clean global pollution data
- To classify countries based on pollution severity
- To compare the performance of different classification algorithms
- To generate actionable insights for pollution reduction and energy recovery

---

## 🗂️ Project Structure

Global_Pollution_Analysis/
│
├── data/
│ └── Global_Pollution_Analysis.csv
│
├── notebooks/
│ └── pollution_analysis.ipynb
│
├── src/
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── models.py
│ └── evaluation.py
│
├── reports/
│ └── figures/
│
├── venv/
│
├── requirements.txt
│
└── README.md



---

## 🧪 Dataset
- **File Name:** `Global_Pollution_Analysis.csv`
- **Description:**  
  Contains country-wise pollution indicators, CO₂ emissions (in MT), energy consumption data, and environmental factors over multiple years.

---

## ⚙️ Technologies Used
- **Programming Language:** Python
- **IDE:** Visual Studio Code
- **Libraries:**
  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn
  - Scikit-learn
  - ipykernel

---

## 🧹 Phase 1: Data Preprocessing
- Dataset loading and inspection
- Handling missing values
- Encoding categorical variables using Label Encoding
- Feature scaling using StandardScaler
- Creation of pollution severity labels (Low / Medium / High)

---

## 🤖 Phase 2: Classification Models
The following machine learning models were implemented:

1. **Naive Bayes Classifier**
   - Probabilistic model based on Bayes’ Theorem
   - Fast and efficient for large datasets

2. **K-Nearest Neighbors (KNN)**
   - Distance-based classification
   - Optimal K selected through experimentation

3. **Decision Tree Classifier**
   - Rule-based model
   - Provides interpretability and feature importance

### Evaluation Metrics:
- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-score

---

## 📊 Phase 3: Reporting and Insights
- Comparison of all models based on accuracy
- Visualization using confusion matrices and bar charts
- Identification of pollution patterns
- Actionable recommendations for pollution control and energy recovery

---

## 📈 Key Insights
- Higher CO₂ emissions strongly correlate with higher pollution severity.
- Energy consumption significantly impacts pollution levels.
- Decision Tree models offer better interpretability for environmental analysis.
- Feature scaling improves the performance of distance-based models like KNN.

---

## ✅ How to Run the Project

1. Clone or download the project
2. Navigate to the project directory
3. Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate


---