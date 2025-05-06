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
st.markdown("<h4 style='text-align: center; color: gray;'>Developed by Amity Centre for Artificial Intelligence, Amity University Noida</h4>", unsafe_allow_html=True)

# Image
if os.path.exists("cervical.jpeg"):
    st.image("cervical.jpeg", caption="Generated with DALL·E", use_column_width=True)
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

# Reference and Credits
st.markdown("---")
st.markdown("**📖 Reference:**")
st.markdown(
    """Kaushik M. et al., *Cytokine gene variants and socio-demographic characteristics as predictors of cervical cancer: A machine learning approach*,
    Computers in Biology and Medicine, 2021. [Read More](https://doi.org/10.1016/j.compbiomed.2021.104559)"""
)








# "in terminal streamlit run Apps.py"


# import config as cfg
# import joblib
# import numpy as np
# import streamlit as st
# from config import doctor_search


# def cervicalcancer_app():
#     st.set_page_config(
#         page_title="Cervical Disease Prediction",
#         page_icon="🏥",
#     )

#     st.markdown(
#         f"<h1 style='text-align: center; color: black; fontSize : 60px;'>Cervical Cancer Disease Diagnosis Application</h1>",
#         unsafe_allow_html=True,
#     )
#     st.markdown(
#         f"<h1 style='text-align: center; color: blue;fontSize : 30px;'>This Application is Developed by Amity Centre for Artificial Intelligence, Amity University Noida</h1>",
#         unsafe_allow_html=True,
#     )
#     st.image(r"C:\Users\Rakesh\Desktop\Amity_practicals DL\streamlit gui\Healthcare_AI\pages\cervical.jpeg", caption="Image is generated by DALLE-3")
#     st.markdown(
#         "<h4 style='text-align: center; color: black;'>Choose below options according to the report to know the patient's status</h4>",
#         unsafe_allow_html=True,
#     )
    
#     model = joblib.load(cfg.CERVICAL_CANCER_MODEL)
    
#     st.session_state["user_input"] = st.text_input(label="Enter Your Name")


#     def my_callback(text_to_display):
#         st.text(str(text_to_display))


#     st.button("Enter Name", on_click=my_callback, args=(st.session_state["user_input"],))
    
    
#     st.session_state["user_location"] = st.text_input(label="Enter Your Location")


#     def my_callback(text_to_display):
#         st.text(str(text_to_display))


#     st.button("Enter Location", on_click=my_callback, args=(st.session_state["user_location"],))
    
#     # title = st.text_input("Name of the Patient, "Life)
#     # st.write("The current movie title is", title)
    
#     gender = st.radio("Gender", ("Male", "Female"))

#     if gender == "Male":
#         gender = 1
#     else:
#         gender = 0
#     Age = st.slider("Age", min_value=1, max_value=110)
#     PoR = st.radio("Place of Residence", ("Rural", "Urban"))

#     if PoR == "Urban":
#         PoR = 1
#     else:
#         PoR = 0
    
#     ES = st.radio("Educational Status", ("Illiterate", "Literate"))
#     if ES == "Literate":
#         ES = 1
#     else:
#         ES = 0
#     SES = st.radio("Socio-economic status", ("Upper", "Middle", "Lower"))
#     if SES == "Upper":
#         SES = 2
#     elif SES == "Middle":
#        SES = 1
#     else:
#         SES = 0
#     Parity = st.radio("Parity", ("None", "Less than or equal to 2", "More than 2"))
#     if Parity == "More than 2":
#         Parity = 2
#     if Parity == "Less than or equal to 2":
#        Parity = 1
#     else:
#         Parity = 0    

#     AgefirstP = st.radio("Age at first full term pregnancy", ("≤20", ">20"))
#     if AgefirstP == ">20":
#         AgefirstP = 1
#     else:
#         AgefirstP = 0
        
#     MC = st.radio("Menstrual Cycle", ("Regular", "Irregular"))
#     if MC == "Regular":
#         MC = 1
#     else:
#         MC = 0

#     MH = st.radio("Menstrual hygien", ("Napkin", "Cloths"))
#     if MH == "Napkin":
#         MH = 1
#     else:
#         MH = 0    
 
#     Contraception = st.radio("Use of Contraception", ("Oral contraceptive pills", "Others"))
#     if Contraception == "Others":
#         Contraception = 1
#     else:
#         Contraception = 0   

#     Smoking = st.radio("Smoking", ("Active", "Passive"))
#     if Smoking == "Active":
#         Smoking = 1
#     else:
#         Smoking = 0 

#     HRHPV = st.radio("High-risk Human Papillomavirus", ("Positive", "Negative"))
#     if HRHPV == "Positive":
#         HRHPV = 1
#     else:
#         HRHPV = 0        
     
#     IL6 = st.radio("IL6", ('GG', 'AA', 'AG'))
#     if IL6 == 'AG':
#         IL6 = 1
#     if IL6 == 'AA':
#        IL6 = 2
#     else:
#         IL6 = 3        
     
#     IL1beta = st.radio("IL1beta", ('TT', 'CT', 'CC'))
#     if IL1beta == 'TT':
#         IL1beta = 1
#     if IL1beta == 'CT':
#        IL1beta = 2
#     else:
#         IL1beta = 3
        
#     TNFalpha  = st.radio("TNFalpha ", ('GG', 'AA', 'GA'))
#     if TNFalpha  == 'GG':
#         TNFalpha  = 1
#     if TNFalpha  == 'AA':
#        TNFalpha  = 2
#     else:
#         TNFalpha  = 3
     
#     IL1RN  = st.radio("IL1RN ", ('I I', 'II II', 'I II', 'I IV', 'II III', 'I III', 'II IV'))
#     if IL1RN  == 'I I':
#         IL1RN  = 1
#     if IL1RN  == 'II II':
#         IL1RN  = 2
#     if IL1RN  == 'I II':
#          IL1RN  = 3
#     if IL1RN  == 'I IV':
#         IL1RN  = 4
#     if IL1RN  == 'II III':
#          IL1RN  = 5
#     if IL1RN  == 'I III':
#         IL1RN  = 6
#     if IL1RN  == 'II IV':
#         IL1RN  = 7
#     else:
#          IL1RN  = 0
   
#     # Beta_HCG = st.slider(
#     #     "Beta_HCG (in mg/dL)", min_value=0.1, max_value=500.0
#     # )

#     # AFP = st.slider("AFP (in mg/dL)", min_value=0.1, max_value=500.0)

#     # PD_L1 = st.slider("PD-L1(in mg/L", min_value=0.1, max_value=300.0)

#     # alamine_aminotransferase = st.slider(
#     #     "Alamine Aminotransferase (in units/L)", min_value=20, max_value=120
#     # )

#     # aspartate_aminotransferase = st.slider(
#     #     "Aspartate Aminotransferase (in units/L)", min_value=20, max_value=140
#     # )

#     # total_proteins = st.slider(
#     #     "Total Proteins (in g/dL)", min_value=2.0, max_value=10.0, step=0.1
#     # )

#     # albumin = st.slider("Albumin (in g/dL)", min_value=1.0, max_value=10.0, step=0.1)

#     # ratio = st.slider(
#     #     "Albumin and Globulin Ratio", min_value=0.1, max_value=3.0, step=0.01
#     # )

#     inp_array = np.array(
#         [
#             [
#                 Age,
#                 PoR,
#                 ES,
#                 SES,
#                 Parity,
#                 AgefirstP,
#                 MC,
#                 MH,
#                 Contraception,
#                 Smoking,
#                 HRHPV,
#                 IL6,
#                 IL1beta,
#                 TNFalpha,
#                 IL1RN,
#             ]
#         ]
#     )

#     predict = st.button("Predict")
    
#     st.markdown(
#         "<h4 style='text-align: center; color: blue;'> This work is Published in Computers in Biology and Medicine Journal -Q1 Indexed, Impact Factor: 7.0</h4>",
#         unsafe_allow_html=True,
#     )
    
#     st.markdown(
#         "<h4 style='text-align: left; color: black;'> Reference:",
#         unsafe_allow_html=True,
#     )
#     url = "https://doi.org/10.1016/j.compbiomed.2021.104559"
    
#     st.markdown("Manoj Kaushik, Rakesh Chandra Joshi, Atar Singh Kushwah, Maneesh Kumar Gupta, Monisha Banerjee, Radim Burget, Malay Kishore Dutta, “Cytokine gene variants and socio-demographic characteristics as predictors of cervical cancer: A machine learning approach,” Computers in Biology and Medicine, vol. 134, p. 104559, Jul. 2021, doi: 10.1016/j.compbiomed.2021.104559.")
    
#     st.write("check out this [link](%s)" % url)
#     # if gender == 1:
#     #     print("This app")
    
#     if predict:
#         breast_disease_prob = model.predict(inp_array)
#         if gender == 1:

#             st.subheader(
#                 "Dear "+st.session_state["user_input"]+ ", You are Male, This App is not meant for you.😄"
#             )
        
#         elif breast_disease_prob == 1:
#             st.subheader("Dear "+st.session_state["user_input"] + ", You have chances of having a Grade-I breast cancer disease 😔")
#             st.markdown("---")
#             st.error(
#                 "If you are a patient, consult with one of the following doctors immediately"
#             )
#             st.subheader("Specialists 👨‍⚕")

#             st.write(
#                 "Click on the specialists to get the specialists nearest to your location 📍"
#             )
#             pcp = doctor_search("Primary Care Provider")
#             infec = doctor_search("Radiation Oncologist")
#             st.markdown(f"- [Primary Care Doctor]({pcp}) 👨‍⚕")
#             st.markdown(f"- [Medical oncologist]({infec}) 👨‍⚕")
#             st.markdown("---")
#         # elif breast_disease_prob == 2:
#         #     st.subheader("Dear "+ st.session_state["user_input"] +", You have chances of having a Grade-II breast cancer disease 😔")
#         #     st.markdown("---")
#         #     st.error(
#         #         "If you are a patient, consult with one of the following doctors immediately"
#         #     )
#         #     st.subheader("Specialists 👨‍⚕")

#         #     st.write(
#         #         "Click on the specialists to get the specialists nearest to your location 📍"
#         #     )
#         #     pcp = doctor_search("Primary Care Provider")
#         #     infec = doctor_search("Radiation Oncologist")
#         #     st.markdown(f"- [Primary Care Doctor]({pcp}) 👨‍⚕")
#         #     st.markdown(f"- [Medical oncologist]({infec}) 👨‍⚕")
#         #     st.markdown("---")
#         # elif breast_disease_prob == 3:
#         #     st.subheader("Dear "+st.session_state["user_input"] + ", You  have chances of having a Grade-III breast cancer disease 😔")
#         #     st.markdown("---")
#         #     st.error(
#         #         "If you are a patient, consult with one of the following doctors immediately"
#         #     )
#         #     st.subheader("Specialists 👨‍⚕")

#         #     st.write(
#         #         "Click on the specialists to get the specialists nearest to your location 📍"
#         #     )
#         #     pcp = doctor_search("Primary Care Provider")
#         #     infec = doctor_search("Radiation Oncologist")
#         #     st.markdown(f"- [Primary Care Doctor]({pcp}) 👨‍⚕")
#         #     st.markdown(f"- [GMedical oncologist]({infec}) 👨‍⚕")
#         #     st.markdown("---")
#         # elif breast_disease_prob == 4:
#         #     st.subheader("Dear "+st.session_state["user_input"] + ", You have chances of having a Grade-IV breast cancer disease 😔")
#         #     st.markdown("---")
#         #     st.error(
#         #         "If you are a patient, consult with one of the following doctors immediately"
#         #     )
#         #     st.subheader("Specialists 👨‍⚕")

#         #     st.write(
#         #         "Click on the specialists to get the specialists nearest to your location 📍"
#         #     )
#         #     pcp = doctor_search("Primary Care Provider")
#         #     infec = doctor_search("Radiation Oncologist")
#         #     st.markdown(f"- [Primary Care Doctor]({pcp}) 👨‍⚕")
#         #     st.markdown(f"- [Medical oncologist]({infec}) 👨‍⚕")
#         #     st.markdown("---")
#         elif breast_disease_prob == 0:

#             st.subheader(
#                 "Dear "+st.session_state["user_input"]+ ", You doesn't have any chances of having a Cervical Cancer disease 😄"
#             )

#             st.balloons()


# if __name__ == "__main__":
#     cervicalcancer_app()
