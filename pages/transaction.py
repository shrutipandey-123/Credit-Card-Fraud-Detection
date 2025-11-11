import streamlit as st
import pandas as pd
import joblib
# ----------------page 2----------------

# load trained model ,scaler & features
model = joblib.load("model/fraud_model.pkl")
scaler = joblib.load("model/fraud_scaler.pkl")
features = joblib.load("model/features.pkl")

# title
st.title(" Check Transaction 💳")

# image
st.image("assets/check.webp",width=500)

# input
input_data={} #dictionary 
for feature in features: # loop is used here for retrieving all the features from the 'features.pkl' file and creatinf an input box
    input_data[feature] = st.number_input(f"Enter {feature}") # entered vlues will store in the dictionary 'input_data'

# creating a dataframe
input_df = pd.DataFrame([input_data]) #pd.DataFrame() is used for converting dictionary in dataframe so that it can be passed in the model
input_scaled = scaler.transform(input_df) # scaler is used so that the prediction can be done at same scale  

if st.button("🔍 Predict"):
    prediction = model.predict(input_scaled)[0]
    if prediction == 1:
        st.error("⚠ Fraud Transaction Detected !")
    else:
        st.success("✅ Legit Transaction")

st.markdown("---")
# st.header("Made with lots of love 💗")