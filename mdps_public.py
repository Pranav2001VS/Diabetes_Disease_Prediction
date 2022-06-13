


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Loading the saved models

diabetes_model = pickle.load(open("diabetes_model.sav, 'rb'))

# sidebar for navigate 

with st.sidebar:
    
    selected = option_menu('Diabetes Disease Prediction System',
                           ['Diabetes Prediction'],
                           
                           icons = ['activity'],
                           
                           default_index = 0)
    
    
# Diabetes Prediction Page

if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    #  Code For Prediction 
    
    diab_dignosis = ''
    
    # Creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_dignosis = 'The Person is Diabetic'
            
        else:
            diab_dignosis = 'The Person is Not Diabetic'
            
    st.success(diab_dignosis)
    
        

    
    
    
    

