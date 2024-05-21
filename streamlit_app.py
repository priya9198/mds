import streamlit as st
import pickle
import pandas as pd

# Title of the app
st.title('Diabetes Prediction App')



# Create input fields for the features
age = st.number_input('Age', min_value=0, max_value=100, value=25)
hypertension = st.selectbox('Hypertension', ['No', 'Yes'])
heart_disease = st.selectbox('Heart Disease', ['No', 'Yes'])
HbA1c_level = st.number_input('HbA1c Level', min_value=0.0, max_value=15.0, value=5.0)
blood_glucose_level = st.number_input('Blood Glucose Level', min_value=0, max_value=200, value=100)
gender_Female = st.checkbox('Female')
gender_Male = st.checkbox('Male')
bmi_Under = st.checkbox('BMI Under')
bmi_normal = st.checkbox('BMI Normal')
bmi_Over = st.checkbox('BMI Over')
bmi_Obese = st.checkbox('BMI Obese')
smoking_history_ex = st.checkbox('Smoking History: Ex')
smoking_history_no = st.checkbox('Smoking History: No')
smoking_history_yes = st.checkbox('Smoking History: Yes')

# Predict button
if st.button('Predict'):
    try:
        # Create input data
        input_data = pd.DataFrame({
            'age': [age],
            'hypertension': [1 if hypertension == 'Yes' else 0],
            'heart_disease': [1 if heart_disease == 'Yes' else 0],
            'HbA1c_level': [HbA1c_level],
            'blood_glucose_level': [blood_glucose_level],
            'gender_Female': [1 if gender_Female else 0],
            'gender_Male': [1 if gender_Male else 0],
            'bmi_Under': [1 if bmi_Under else 0],
            'bmi_normal': [1 if bmi_normal else 0],
            'bmi_Over': [1 if bmi_Over else 0],
            'bmi_Obese': [1 if bmi_Obese else 0],
            'smoking_history_ex': [1 if smoking_history_ex else 0],
            'smoking_history_no': [1 if smoking_history_no else 0],
            'smoking_history_yes': [1 if smoking_history_yes else 0]
        })

        # Predict the output
        prediction = model.predict(input_data)[0]
        
        # Display the prediction
        st.write(f'The predicted diabetes status is: {"Positive" if prediction == 1 else "Negative"}')
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
