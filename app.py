import streamlit as st
import numpy as np
import joblib

# Load the trained Logistic Regression model
model = joblib.load("model.pkl")  # Make sure model.pkl is in the same directory

# Set Streamlit page config
st.set_page_config(page_title="Placement Predictor", page_icon="🎓", layout="centered")

# App Title
st.title("🎯 Placement Prediction System")
st.markdown(
    """
    Welcome to the **Placement Predictor App**!  
    Enter your academic details below to check whether you're likely to get placed based on a trained ML model.
    """
)

# User Inputs
st.subheader("📥 Enter Details:")

col1, col2 = st.columns(2)

with col1:
    iq = st.number_input("🧠 IQ Score", min_value=50, max_value=200, value=100, step=1)

with col2:
    cgpa = st.number_input("📘 CGPA", min_value=0.0, max_value=10.0, value=8.0, step=0.1)

# Prediction button
if st.button("📊 Predict Placement"):
    features = np.array([[iq, cgpa]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][prediction]

    if prediction == 1:
        st.success(f"🎓 Congratulations! The model predicts you will be **PLACED** ✅\n\nConfidence: {probability:.2%}")
    else:
        st.error(f"❌ Sorry! The model predicts you will **NOT be placed**\n\nConfidence: {probability:.2%}")
