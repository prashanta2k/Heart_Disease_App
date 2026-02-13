import streamlit as st 
import pickle

st.set_page_config(page_title="Heart Disease Prediction", page_icon=":heart:", layout="centered")  # page configuration

st.title("Heart Disease Prediction App") # title of the app
st.write("This app predicts the likelihood of heart disease based on various health parameters") #sub heading  

#loading the model
def load_model():
    return pickle.load(open('heart.pkl','rb'))

model = load_model()

# input fields

age = st.number_input("Age")
st.write("Age: ", age)

sex = st.selectbox("Sex", [0, 1])
st.write("Sex: ", sex)

cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])  
st.write("Chest Pain Type: ", cp)   

trestbps = st.number_input("Resting Blood Pressure")
st.write("Resting Blood Pressure: ", trestbps)

chol = st.number_input("Serum Cholesterol")
st.write("Serum Cholesterol: ", chol)   

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])   
st.write("Fasting Blood Sugar > 120 mg/dl: ", fbs)

restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
st.write("Resting Electrocardiographic Results: ", restecg)

thalach = st.number_input("Maximum Heart Rate Achieved")
st.write("Maximum Heart Rate Achieved: ", thalach)

exang = st.selectbox("Exercise Induced Angina", [0, 1])
st.write("Exercise Induced Angina: ", exang)    

oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest")
st.write("ST Depression Induced by Exercise Relative to Rest: ", oldpeak)

slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
st.write("Slope of the Peak Exercise ST Segment: ", slope)

ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3])
st.write("Number of Major Vessels Colored by Fluoroscopy: ", ca)

thal = st.selectbox("Thalassemia", [0, 1, 2, 3])
st.write("Thalassemia: ", thal)

if st.button("Predict Heart Disease"):
    input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    prediction = model.predict(input_data)  
    if prediction[0] == 1:
        st.error("The model predicts that you have heart disease. Please consult a doctor for further evaluation.")
    else:
        st.success("The model predicts that you do not have heart disease. However, please consult a doctor for a comprehensive health assessment.")
