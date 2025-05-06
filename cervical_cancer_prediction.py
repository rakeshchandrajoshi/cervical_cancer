import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model and feature columns
with open("trained_model_with_features.pkl", "rb") as f:
    model_data = pickle.load(f)
    model = model_data["model"]
    feature_columns = model_data["feature_columns"]
    label_encoders = model_data["label_encoders"]
    target_encoder = model_data["target_encoder"]

# Streamlit UI for user input
st.title("Cervical Cancer Prediction")

# Assuming you have user inputs for each feature
user_input = {
    "Age": 30,
    "PoR": "Urban",
    "ES": "Literate",
    "SES": "Middle",
    "Parity": "≤2",
    "AgefirstP": "≤20",
    "MC": "Regular",
    "MH": "Napkin",
    "Contraception": "Oral contraceptive pills",
    "Smoking": "Active",
    "HRHPV": "Positive",
    "IL6": "AG",
    "IL1beta": "CT",
    "TNFalpha": "GA",
    "IL1RN": "I II"
}

# Encode user input
encoded_input = []
for feature in feature_columns:
    value = user_input.get(feature)
    if value in label_encoders.get(feature, {}):
        encoded_input.append(label_encoders[feature].transform([value])[0])
    else:
        encoded_input.append(value)

# Convert to DataFrame for prediction
input_data = pd.DataFrame([encoded_input], columns=feature_columns)

# Make prediction
prediction = model.predict(input_data)

# Display result
if prediction[0] == 1:
    st.error("High risk of Cervical Cancer")
else:
    st.success("Low risk of Cervical Cancer")
