# Task 1: Titanic Dataset Analysis

## 📌 Project Overview
This project analyzes the Titanic dataset to understand data structure, types, and machine learning readiness. It identifies key variables (Numerical vs. Categorical) and checks for data quality issues like missing values.

## 🛠 Tools Used
* **Python**
* **Pandas** (for data manipulation)
* **Seaborn** (for dataset loading)

## 📊 Key Observations
* The dataset contains **891 rows** and **15 columns**.
* **Target Variable:** `survived` (0 = Died, 1 = Survived).
* **Missing Data:** Significant missing values found in `age` (~20%) and `deck` (>75%).
* **ML Readiness:** The dataset is suitable for basic classification models but requires imputation for missing age values.

## 📂 Files Included
* `Task1_Titanic.ipynb`: The main analysis code.
* `Analysis_Report.pdf`: Detailed 1-page report.