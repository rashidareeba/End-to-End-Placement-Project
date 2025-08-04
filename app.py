import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model.pkl")

# Streamlit page settings
st.set_page_config(page_title="Placement Predictor", page_icon="🎓", layout="centered")

# Title and description
st.title("🎯 Placement Prediction App")
st.markdown("""
Welcome to the **Placement Predictor**!  
Enter your details below to see if you're likely to get placed.
""")

# Input form
with st.form("placement_form"):
    cgpa = st.slider("📘 CGPA", min_value=0.0, max_value=10.0, value=7.0, step=0.1)
    iq = st.slider("🧠 IQ Score", min_value=50, max_value=150, value=100, step=1)

    submit = st.form_submit_button("🔍 Predict Placement")

# Prediction logic
if submit:
    input_data = np.array([[cgpa, iq]])
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.success("🎉 Congratulations! You are likely to be **Placed**.")
    else:
        st.error("📌 Sorry, you are likely **Not to be Placed**. Work on improving skills!")


