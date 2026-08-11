import streamlit as st
import pandas as pd
import joblib

# ===========================
# Load Model
# ===========================

model = joblib.load("models/final_pipeline.pkl")


# ===========================
# BMI Category Function
# ===========================

def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    elif bmi < 35:
        return "Obesity I"

    elif bmi < 40:
        return "Obesity II"

    else:
        return "Obesity III"


# ===========================
# Age Category Function
# ===========================

def age_category(age):

    if age < 30:
        return "Young Adult"

    elif age < 45:
        return "Middle Aged"

    elif age < 60:
        return "Senior Adult"

    else:
        return "Elderly"


# ===========================
# Page Configuration
# ===========================

st.set_page_config(
    page_title="Medical Insurance Cost Prediction",
    page_icon="🏥",
    layout="centered"
)


# ===========================
# Page Title
# ===========================

st.title("🏥 Medical Insurance Cost Prediction")

st.write(
    "Enter the patient's information to estimate the medical insurance charges."
)


# ===========================
# Inputs
# ===========================

age = st.slider(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

sex = st.selectbox(
    "Sex",
    ["male", "female"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0,
    step=0.1
)

children = st.slider(
    "Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.selectbox(
    "Smoker",
    ["yes", "no"]
)

region = st.selectbox(
    "Region",
    [
        "northeast",
        "northwest",
        "southeast",
        "southwest"
    ]
)


# ===========================
# Prediction
# ===========================

if st.button("Predict Charges 💰"):

    # Create engineered features
    bmi_cat = bmi_category(bmi)
    age_cat = age_category(age)

    # Create input dataframe
    input_df = pd.DataFrame({

        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region],
        "bmi_category": [bmi_cat],
        "age_category": [age_cat]

    })

    # Prediction
    prediction = model.predict(input_df)[0]

    # Display result
    st.success(
        f"Estimated Insurance Charges: ${prediction:,.2f}"
    )