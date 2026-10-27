import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load the saved XGBoost model
# Ensure 'calorie_model.pkl' is in the exact same folder as this script
with open('calorie_model.pkl', 'rb') as file:
    model = pickle.load(file)
# Website Header
st.title("🔥 Calorie Burn Predictor")
st.write("Enter your workout details below to predict how many calories you burned.")

# Input fields matching your 7 training columns
gender = st.selectbox("Gender", ["male", "female"])
age = st.slider("Age", 20, 80, 25)                                        # ["Age","Body_Temp","BMI","Total_Exertion","Temp_Spike","Gender_male"]
height = st.slider("Height (cm)", 120.0, 230.0, 175.0)
weight = st.slider("Weight (kg)", 30.0, 140.0, 75.0)
duration = st.slider("Workout Duration (minutes)", 0.0, 40.0, 15.0)
heart_rate = st.slider("Average Heart Rate (bpm)", 60.0, 130.0, 95.0)
body_temp = st.slider("Body Temperature (°C)", 36.0, 42.0, 37.5)

# Prediction execution
if st.button("Predict Calories Burned"):
    gender_male = 1 if gender == "male" else 0
    
    height_m = height / 100.0
    bmi = weight / (height_m ** 2)
    total_exertion = duration * heart_rate
    temp_spike = body_temp - 37.0 
    
    # Build a Pandas DataFrame with exact column names instead of a NumPy array
    input_df = pd.DataFrame({
        "Age": [age],
        "Body_Temp": [body_temp],
        "BMI": [bmi],
        "Total_Exertion": [total_exertion],
        "Temp_Spike": [temp_spike],
        "Gender_male": [gender_male]
    })
    
    prediction = model.predict(input_df)
    st.success(f"Boom! Based on your XGBoost model, you burned approximately {int(prediction[0])} calories.")
    st.balloons()