import streamlit as st
import joblib
import numpy as np
import os

# Load your model
MODEL_PATH = "cervicalcancer.pkl"
model = joblib.load(MODEL_PATH)

# Page config
st.set_page_config(page_title="Cervical Cancer Predictor", page_icon="🏥", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: darkblue;'>🧬 Cervical Cancer Diagnosis Application</h1>", unsafe_allow_html=True)
#st.markdown("<h4 style='text-align: center; color: gray;'>Developed by Amity Centre for Artificial Intelligence, Amity University Noida</h4>", unsafe_allow_html=True)

# Image
if os.path.exists("cervical.jpeg"):
    st.image("cervical.jpeg", caption="Generated with DALL·E", use_container_width=True)
else:
    st.warning("Image file 'cervical.jpeg' not found.")

# Sidebar Inputs
with st.sidebar:
    st.header("👤 Patient Info")
    user_name = st.text_input("Enter Your Name")
    user_location = st.text_input("Enter Your Location")

# Main input form
with st.form("cervical_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.radio("Gender", ["Female", "Male"])
        Age = st.slider("Age", 1, 110, 30)
        PoR = st.radio("Place of Residence", ["Rural", "Urban"])
        ES = st.radio("Educational Status", ["Illiterate", "Literate"])
        SES = st.radio("Socio-economic Status", ["Lower", "Middle", "Upper"])

    with col2:
        Parity = st.radio("Parity", ["None", "≤2", ">2"])
        AgefirstP = st.radio("Age at First Full-Term Pregnancy", ["≤20", ">20"])
        MC = st.radio("Menstrual Cycle", ["Regular", "Irregular"])
        MH = st.radio("Menstrual Hygiene", ["Napkin", "Cloths"])
        Contraception = st.radio("Use of Contraception", ["Oral contraceptive pills", "Others"])

    with col3:
        Smoking = st.radio("Smoking", ["Passive", "Active"])
        HRHPV = st.radio("High-risk HPV", ["Negative", "Positive"])
        IL6 = st.radio("IL6", ['GG', 'AA', 'AG'])
        IL1beta = st.radio("IL1beta", ['TT', 'CT', 'CC'])
        TNFalpha = st.radio("TNFalpha", ['GG', 'AA', 'GA'])
        IL1RN = st.selectbox("IL1RN", ['I I', 'II II', 'I II', 'I IV', 'II III', 'I III', 'II IV'])

    submitted = st.form_submit_button("Predict")

if submitted:
    # Encoding categorical variables
    gender_val = 1 if gender == "Male" else 0
    PoR_val = 1 if PoR == "Urban" else 0
    ES_val = 1 if ES == "Literate" else 0
    SES_val = {"Lower": 0, "Middle": 1, "Upper": 2}[SES]
    Parity_val = {"None": 0, "≤2": 1, ">2": 2}[Parity]
    AgefirstP_val = 1 if AgefirstP == ">20" else 0
    MC_val = 1 if MC == "Regular" else 0
    MH_val = 1 if MH == "Napkin" else 0
    Contraception_val = 1 if Contraception == "Others" else 0
    Smoking_val = 1 if Smoking == "Active" else 0
    HRHPV_val = 1 if HRHPV == "Positive" else 0
    IL6_val = {"AG": 1, "AA": 2, "GG": 3}[IL6]
    IL1beta_val = {"TT": 1, "CT": 2, "CC": 3}[IL1beta]
    TNFalpha_val = {"GG": 1, "AA": 2, "GA": 3}[TNFalpha]
    IL1RN_val = {
        'I I': 1, 'II II': 2, 'I II': 3, 'I IV': 4, 'II III': 5, 'I III': 6, 'II IV': 7
    }.get(IL1RN, 0)

    # Input for prediction
    input_features = np.array([
        [
            Age, PoR_val, ES_val, SES_val, Parity_val, AgefirstP_val, MC_val, MH_val,
            Contraception_val, Smoking_val, HRHPV_val, IL6_val, IL1beta_val,
            TNFalpha_val, IL1RN_val
        ]
    ])

    result = model.predict(input_features)

    st.markdown("---")
    st.subheader(f"👤 Patient: {user_name or 'Anonymous'}")

    if gender_val == 1:
        st.warning("This application is designed for biological females. Your result may not be valid.")
    elif result[0] == 1:
        st.error("🔬 Prediction: You may have a risk of Cervical Cancer. Please consult a specialist.")
        st.markdown("##### 📍 Suggested Doctors:")
        st.markdown("- [Primary Care Provider](https://www.google.com/search?q=Primary+Care+Provider+near+me)")
        st.markdown("- [Radiation Oncologist](https://www.google.com/search?q=Radiation+Oncologist+near+me)")
    else:
        st.success("✅ Prediction: You are unlikely to have Cervical Cancer. Stay healthy!")
        st.balloons()
