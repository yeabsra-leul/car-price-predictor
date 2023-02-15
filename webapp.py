import streamlit as st
import pickle 
import pandas as pd
from math import trunc

title = '<p style="font-family:Arial; text-align:Center; color:White; font-size: 50px;"> Predict the Price of any Car</p>'

st.markdown(title,unsafe_allow_html=True)

#get user input
year = st.selectbox("Select the Model Year",range(1990,2022))
km_driven = st.number_input("Enter the Kilometer Driven :",step=1)
fuel = st.selectbox("Select the Fuel Type",["Petrol","Diesel","CNG","LPG","Electric"])
transmission = st.selectbox("Select the Transmission type",["Manual","Automatic"])
owner = st.selectbox("Select the Owner Type :",["First Owner","Second Owner","Third Owner","Fourth & Above Owner","Test Drive Car"])

df_pred = pd.DataFrame([[year,km_driven,fuel,transmission,owner]],
columns = ["year","km_driven","fuel","transmission","owner"])
df_pred["transmission"] = df_pred["transmission"].apply( lambda x: 1 if x == "Manual" else 0)


def transform_fuel(data):
    result = 5
    if(data == "Petrol"):
        result = 4
    elif(data == "Diesel"):
        result = 1
    elif(data == "CNG"):
        result = 0
    elif(data == "LPG"):
        result = 3
    elif(data == "Electric"):
        result = 2
    return result

def transform_owner(data):
    result = 5
    if(data == "First Owner"):
        result = 0
    elif(data == "Second Owner"):
        result = 2
    elif(data == "Third Owner"):
        result = 4
    elif(data == "Fourth & Above Owner"):
        result = 1
    elif(data == "Test Drive Car"):
        result = 3
    return result

df_pred["fuel"] = df_pred["fuel"].apply(transform_fuel)
df_pred["owner"] = df_pred["owner"].apply(transform_owner)

model = pickle.load(open('regressor.pkl', 'rb'))
prediction_result = model.predict(df_pred)
print(df_pred)


if st.button('Predict'):

    pred_result = pred_result = f"""
<style>
span {{
  font: bold 30px Courier;
}}
</style>
<span >{trunc(prediction_result[0])}</span>
"""
    st.write('The Predicted Price of the Car is :',pred_result," Birr",unsafe_allow_html=True)