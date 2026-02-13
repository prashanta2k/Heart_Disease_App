import streamlit as st
import pickle 
st.set_page_config(page_title="Heart Disease app",page_icon=":heart",layout="centered")
st.title("Heart Disease Prediction Application")
st.write("This app predicts heart disease based on various parameters")

def load_model():
    return pickle.load(open('heart.pkl','rb'))

model = load_model()

#Input fields
# 	age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	
age  = st.number_input("Age")
st.write("Age", age)

sex = st.selectbox("Sex",[0,1])
st.write("Sex",sex)

cp = st.selectbox("cp",[0,1,2,3])
st.write("cp",cp)

trestbps  = st.number_input("Resting Blood Pressure")
st.write("tresResting Blood Pressure", trestbps)

chol  = st.number_input("Serum Cholestrol")
st.write("cSerum Cholestrol", chol)

fbs  = st.selectbox("Fasting Blood Pressure > 120.0 ",[0,1])
st.write("Fasting Blood Pressure", fbs)

restecg  = st.number_input("Resting Electro cardiographic Result")
st.write("Resting Electro cardiographic Result", restecg)

thalach  = st.number_input("Maximum Heart rate achived")
st.write("Maximum Heart rate achived", thalach)

#exang	oldpeak	slope	ca
exang  = st.selectbox("Excercise Induce Angina",[0,1])
st.write("Excercise Induce Angina", exang)

oldpeak  = st.number_input("ST depression Induced")
st.write("ST depression Induced", oldpeak)

slope  = st.selectbox("Slope",[0,1,2])
st.write("Slope", slope)

ca  = st.selectbox("No of major vessels colored by Fluroscopy",[0,1,2,3])
st.write("No of major vessels colored by Fluroscopy", ca)

thal  = st.selectbox("Thalasmea",[0,1,2,3])
st.write("Thalasmea", thal)

if st.button("Predict Heart Disease"):
    input_data = [[age,sex,	cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("The model predicts that you have heart disease. Please consult a doctor for further evaluation.")
    else:
        st.success("The model predicts that you do not have heart disease. However, please consult a doctor for a comprehensive health assessment.")