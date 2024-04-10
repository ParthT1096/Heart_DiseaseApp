import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle  # Used for loading the pre-trained model


st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://qtxasset.com/cdn-cgi/image/w=850,h=478,f=auto,fit=crop,g=0.5x0.5/https://qtxasset.com/quartz/qcloud5/media/image/Heart_medical_Paul%20Campbell_GettyImages-1130318299.jpg?VersionId=UXu9hjr7WX2w.5qzN.fnOwBQlD6UKbxS");
        background-attachment: fixed;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)


file_open =open('Ranfor_model.pkl', 'rb')
pipe = pickle.load(file_open) #file loading pipe is just a variable name



result=0
st.title("Heart Disease Predictor")
st.markdown("**This app predicts the likelihood of heart disease based on user input.**")

age=st.number_input("Enter Your Age: ")
gender=st.selectbox("Gender:",['F', 'M'])
cp=st.selectbox('Chest Pain Type:',['ASY', 'ATA', 'NAP', 'TA'])
res_bp = st.number_input('Resting Blood Pressure: ')
chol = st.number_input('Serum Cholesterol in mg/dl: ')
fbs = st.selectbox('Fasting Blood Sugar', [0, 1])
res = st.selectbox('Resting Electro-cardiography Results:',['LVH', 'Normal', 'ST'])
tha = st.number_input('Maximum Heart Rate achieved: ')
exa = st.selectbox('Exercise induced angina: ',['N', 'Y'])
old = st.number_input('OldPeak:')
slope = st.selectbox('The slope of the peak exercise ST segmen:',['Down', 'Flat', 'Up'])



if(st.button("Predict the Heart Disease Rate")):
    result=pipe.predict(pd.DataFrame([[age,gender,cp,res_bp,chol,fbs,res,tha,exa,old,slope]],columns=['Age', 'Gender', 'ChestPainType', 'RestingBP', 'Cholesterol',
       'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak',
       'ST_Slope']))
    result=int(result)
    if result==1:
        st.success("Your Heart Has a Chance of Failure")
    else:
        st.success("Your Heart is Healthy")
