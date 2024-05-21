import streamlit as st
import pickle
import pandas as pd

# Title of the app
st.write('# Diabetes Prediction App')

# Load your trained model
try:
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'model.pkl' is in the current directory.")
    st.stop()

# Input fields for the features
st.sidebar.header('User Input Parameters')

def user_input_features():
    age = st.sidebar.number_input('Age', min_value=0, max_value=100, value=25)
    bmi = st.sidebar.number_input('BMI', min_value=0.0, max_value=50.0, value=25.0)
    # Add other necessary input fields here
    # Example:
    glucose = st.sidebar.number_input('Glucose Level', min_value=0.0, max_value=200.0, value=110.0)
    
    data = {
        'age': age,
        'bmi': bmi,
        'glucose': glucose,
        # Add other features here
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_data = user_input_features()

# Predict button
if st.button('Predict'):
    try:
        prediction = model.predict(input_data)[0]
        # Display the prediction
        st.write(f'The predicted diabetes status is: {"Positive" if prediction == 1 else "Negative"}')
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

# Display user input parameters
st.subheader('User Input parameters')
st.write(input_data)
