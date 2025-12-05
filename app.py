# app/app.py
import streamlit as st
from predict import predict

st.title("🌼 Iris Flower Species Predictor")
st.write("Enter the flower measurements below and click **Predict** to see the species.")

# Numeric input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)

#some changes
# Predict button
if st.button("Predict"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    result = predict(features)
    st.success(f"The predicted Iris species is: **{result.capitalize()}** 🌸")
