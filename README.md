# End-to-End-Placement-Project
![download](https://github.com/user-attachments/assets/8d5b9708-1d1a-4f6e-a950-915a4ef779b7)

# 🎯 End-to-End Placement Prediction ML Project

![Placement Prediction](https://github.com/user-attachments/assets/8d5b9708-1d1a-4f6e-a950-915a4ef779b7)

---

## 🚀 Project Overview

This end-to-end machine learning project predicts whether a student will be placed based on their **CGPA** and **IQ**, using a simple and interpretable **Logistic Regression** model.

> 🔍 Ideal for beginners learning ML pipelines — from data loading and preprocessing to model training, evaluation, and saving.

---

## 📊 Dataset Information

- **Total Rows**: 100  
- **Features**:  
  - `cgpa`: Student’s Cumulative Grade Point Average  
  - `iq`: Student’s IQ score  
  - `placement`: Target variable (1 = Placed, 0 = Not Placed)  

- **Source**: [`placement.csv`](https://github.com/campusx-official/placement-project-logistic-regression/blob/main/placement.csv)

---

## 🧠 ML Workflow Overview

### 📥 1. Data Collection
- Loaded CSV file using `pandas`.
- Verified column types and data integrity.

### 🧹 2. Data Preprocessing
- Checked for missing values (none found).
- Applied `StandardScaler` to normalize `cgpa` and `iq`.

### 📊 3. Exploratory Data Analysis (EDA)
- Used `seaborn` and `matplotlib` to create:
  - Scatterplots
  - Pairplots
- Observed linear separability between classes.

### 🧾 4. Feature Selection
- **Input Features**: `cgpa`, `iq`  
- **Target**: `placement`

### 🔀 5. Train-Test Split
- Split data using `train_test_split()` with an 80/20 ratio.

### 🤖 6. Model Building
- Algorithm: `LogisticRegression()` from `scikit-learn`
- Trained on scaled features from training set.

### 📈 7. Model Evaluation
- Evaluated using:
  - `accuracy_score`
  - `confusion_matrix`
- Achieved **100% accuracy** on test data (as expected on clean toy data).

### 💾 8. Model Export
- Saved trained model using `joblib` for future deployment.

---

## ✅ Key Highlights

- ✅ Built an end-to-end ML pipeline in Python
- ✅ Used logistic regression for binary classification
- ✅ Practiced feature scaling and visual analysis
- ✅ Exported model for deployment in real-world applications

---

## 🧰 Tech Stack

- **Language**: Python 3.x  
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `joblib`

---

