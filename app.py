import streamlit as st
import pickle
import numpy as np
import joblib
# pickle : In pickle we save the model after training (fraud.pkl). this is used for loading the pre trained model into the file.
# joblib : library used for saving and loading models

# load trained model ,scaler & features
model = joblib.load("model/fraud_model.pkl")
scaler = joblib.load("model/fraud_scaler.pkl")
features = joblib.load("model/features.pkl")

# -------------Page 1--------------    

# title
st.title("💳 Credit Card Fraud Detection")

# add image
st.image('assets/fraud.webp',use_container_width=True)
st.markdown('---')
st.header("Objective : Detect fraudlent transactions to reduce financial loss")
st.markdown('---')

#description
st.write('''This project is a Credit Card Fraud Detection System which is built using Python./
            It uses Machine Learning algorithms to detect fraud transactions based on transaction details. 
            The dataset used in this app is Kaggle Credit Card Fraud Dataset which is slightly imbalenced , to handle this proper train-test split are applied.
            The trained model is saved using Pickle. It will be time consuming to load the model again and again that's why we use Pickle for saving the trained model./
            this model is deployed with Streamlit so that users can input transaction details and instantly check whether it is fraudlent or legitimate. /''')

st.markdown('''✨Tools & Libraries
- Python ⚡
- Pandas
- Scikit-learn
- Matplotlib & Seaborn 📊
- Steamlit 📟 ''')

st.markdown('---')

st.info("To check the Transaction 👉")

# button for navigation
if st.button("Go to Transaction Check"):
    st.switch_page("pages/transaction.py")

