## This is going to be a Streamlit App

import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor

st.title('Insurance Premium Charge Prediction')

age = st.slider('age', 16, 100)
sex = st.selectbox("sex", options=["male", "female"])
bmi = st.slider('bmi', 15, 100)
children = st.number_input('children', 0, 20)
smoker = st.selectbox('smoker', options=["yes", "no"])
region = st.selectbox('region', options=['northeast', 'northwest', 'southwest', 'southeast'])

input_data_dict = {
    "age": age,
    "sex": sex,
    "bmi": bmi,
    "children": children, 
    "smoker": smoker,
    "region": region
}

st.write(input_data_dict)

input_data = pd.DataFrame([input_data_dict])

st.write(input_data)

save_path = "models"

save_model_predictor = TabularPredictor.load(save_path)

submit = st.button("CLICK TO PREDICT INSURANCE CHARGES")

if submit:
    insurance_charge = save_model_predictor.predict(input_data)[0]
    st.write(f"The predicted insurance charges is: {insurance_charge}")
