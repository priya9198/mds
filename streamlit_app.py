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
