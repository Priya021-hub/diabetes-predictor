import streamlit as st
import numpy as np
import pickle

from tensorflow.keras.models import load_model

# Load model
model = load_model("diabetes_model.h5")

# Load scaler
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Diabetes Risk Prediction")

pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
bloodpressure = st.number_input("Blood Pressure", min_value=0)
skinthickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

if st.button("Predict"):

    input_data = np.array([[
        pregnancies,
        glucose,
        bloodpressure,
        skinthickness,
        insulin,
        bmi,
        dpf,
        age
    ]])

    input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)

    if prediction[0][0] > 0.5:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Diabetes")