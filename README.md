# End-to-End-Placement-Project
🚀 End-to-End ML Project: Placement Prediction using Logistic Regression
📊 Total Rows: 100 | Columns: CGPA, IQ, Placement (Target)

🎯 Goal:
Predict whether a student will be placed or not based on their CGPA and IQ score using a classification model.

🧠 Workflow Overview:

📥 Data Collection:

Source: GitHub CSV

Features: cgpa, iq

Target: placement (0 = No, 1 = Yes)

🧹 Data Preprocessing:

Checked for missing values

Scaled features using StandardScaler()

Transformed features to a numerical array for modeling

📊 Exploratory Data Analysis (EDA):

Used scatterplots and pairplots to visualize feature impact on placement

Found a linear separability between placed and non-placed students

🧾 Feature Selection:

Selected CGPA and IQ as independent variables

placement as dependent variable

🔀 Train-Test Split:

Split into training and test sets using train_test_split() (80/20 ratio)

🤖 Model Building:

Model: LogisticRegression() from scikit-learn

Fitted on training data

Achieved 100% accuracy on test set (toy dataset)

📈 Model Evaluation:

Metric: accuracy_score()

Confusion matrix analysis

💾 Model Export:

Saved the model using joblib for future deployment

☁️ Deployment:

Hosted on Google Colab for demo

Ready for deployment on any cloud platform (Streamlit, Flask, etc.)

📌 Key Learnings:

End-to-end ML workflow

Classification using Logistic Regression

Data visualization and feature scaling

Model export and deployment readiness
