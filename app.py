import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model_hypertension.pkl")

st.set_page_config(
    page_title="Hypertension Prediction",
    page_icon="❤️"
)

st.title("❤️ Hypertension Risk Prediction")

age = st.number_input("Age", 18, 100, 30)
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
salt = st.number_input("Salt Intake", 0.0, 20.0, 5.0)
stress = st.number_input("Stress Score", 0.0, 10.0, 5.0)
sleep = st.number_input("Sleep Duration", 0.0, 12.0, 7.0)

family = st.selectbox(
    "Family History",
    ["No", "Yes"]
)

smoking = st.selectbox(
    "Smoking Status",
    ["Non-Smoker", "Smoker"]
)

if st.button("Predict"):

    family = 1 if family == "Yes" else 0
    smoking = 1 if smoking == "Smoker" else 0

    input_data = pd.DataFrame({
        "Age":[age],
        "Salt_Intake":[salt],
        "Stress_Score":[stress],
        "Sleep_Duration":[sleep],
        "BMI":[bmi],
        "Family_History":[family],
        "Smoking_Status":[smoking]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk Hypertension")
    else:
        st.success("Low Risk Hypertension")