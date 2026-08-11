# 🏥 Medical Insurance Cost Prediction

An end-to-end Machine Learning project for predicting individual medical insurance charges using demographic and health-related information.

---

## 📌 Project Overview

The goal of this project is to predict medical insurance charges based on personal attributes such as age, BMI, smoking status, and region.

This project follows a complete Machine Learning workflow from data understanding to model deployment preparation.

---

## 📂 Dataset

**Dataset:** Medical Cost Personal Dataset

**Source:** Kaggle

**Number of Samples:** 1338

### Features

- Age
- Sex
- BMI
- Children
- Smoker
- Region

### Target

- Charges

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Optuna
- SHAP
- Joblib

---

## 📊 Project Workflow

### 1. Business Understanding

- Problem Definition
- Objectives
- Dataset Description

---

### 2. Data Cleaning

- Missing Values
- Duplicate Records
- Outlier Detection
- Data Validation

---

### 3. Exploratory Data Analysis (EDA)

Performed:

- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis
- Correlation Analysis

Key Findings:

- Smoking status has the strongest relationship with insurance charges.
- Charges are highly right-skewed.
- Age and BMI positively affect insurance costs.
- Region has little impact on the target.

---

### 4. Feature Engineering

Implemented:

- BMI Category Binning
- One-Hot Encoding
- Feature Selection
- Multiple preprocessing pipelines
- Comparison between BMI and BMI Category
- Scaling experiments
- Log transformation experiments

---

### 5. Modeling

Models evaluated:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

Evaluation method:

- 10-Fold Cross Validation

---

### 6. Hyperparameter Tuning

Hyperparameter optimization was performed using **Optuna**.

The best model was selected according to Cross Validation performance.

---

## 🏆 Final Model

**Model:** Random Forest Regressor

**Pipeline Components**

- One-Hot Encoding
- ColumnTransformer
- Random Forest Regressor

---

## 📈 Final Performance

| Metric | Score |
|--------|-------:|
| R² Score | **0.8780** |
| MAE | **2476.20** |
| RMSE | **4352.02** |

---

## 🔍 Model Explainability

Model interpretation was performed using:

- Actual vs Predicted Plot
- Residual Plot
- Residual Distribution
- Feature Importance
- SHAP Summary Plot
- SHAP Bar Plot
- SHAP Waterfall Plot

### Main Insights

- Smoking status is the most influential feature.
- BMI and Age significantly affect insurance charges.
- Region and Sex have relatively small influence.

---

## 📁 Project Structure

```text
Medical Cost Project/
│
├── .vscode/                             # VS Code settings
│
├── data/
│   └── insurance.csv                    # Original dataset
│
├── Figures/                             # Saved plots and visualizations
│
├── models/
│   └── final_pipeline.pkl               # Trained ML pipeline
│
├── notebooks/
│   ├── 01_Business_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning_analysis.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│   ├── 04_Feature_Engineering_Selection_analysis.ipynb
│   ├── 05_Modeling_Pipeline[best_model_and_best_preprocessor].ipynb
│   └── 06_HyperparameterTunning_and_Train&EvlauateFinalModel.ipynb
│   └── 07-VisualizeModelResult_and_FeatureImportance&Shape.ipynb
|   
│
├── src/
│   ├── Data_preprocessing.py                 # Data loading and preprocessing
│   ├── Feature_Engineering.py           # Feature engineering functions
│   ├── best_preprocessor.py                     # Model training pipeline
│   └── __pycache__/
│
├── Decisions.txt                        # Project decisions and notes
├── requirements.txt                     # Project dependencies
└── README.md                            # Project documentation
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/MennaAhmed404/Medical_Insurance_Cost_Prediction.git
cd Medical_Insurance_Cost_Prediction
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

### 4. Open your browser

The application will automatically open at:

```
http://localhost:8501
```

If it doesn't open automatically, copy and paste the link into your browser.

---

## 📒 Notebooks

The notebooks document the complete machine learning workflow:

1. Business Understanding
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Modeling & Hyperparameter Tuning
6. Final Model Evaluation

---


## 👩‍💻 Author

**Menna Ahmed**

Faculty of Computer Science & Artificial Intelligence

Machine Learning Engineer