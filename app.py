import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder
import time

# Load model
model = joblib.load('Random_Forest_Model.joblib')

# Page configuration
st.set_page_config(page_title="🎓 Student Performance Prediction", layout="wide")

# App title
st.title("🎓 Student Performance Prediction")
st.write("""
Aplikasi untuk memprediksi performa mahasiswa berdasarkan berbagai atribut.
""")

# Sidebar for user input
st.sidebar.header("Input Features")
categorical_features = ['Gender', 'Displaced', 'Debtor', 'Scholarship_holder', 'Tuition_fees_up_to_date', 'Daytime_evening_attendance']
numerical_features = ['Admission_grade', 'Previous_qualification_grade', 'Curricular_units_1st_sem_approved']

# Helper for encoding categorical features
def encode_categorical(data):
    label_encoders = {col: LabelEncoder() for col in categorical_features}
    for col in categorical_features:
        label_encoders[col].fit(['No', 'Yes'])  # Assume binary values
        data[col] = label_encoders[col].transform(data[col])
    return data

# Helper for scaling numerical features
def scale_numerical(data):
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(data[numerical_features])
    return data

# User input
def user_input_features():
    inputs = {}
    inputs['Gender'] = st.sidebar.selectbox('Gender', ['Female', 'Male'])
    inputs['Displaced'] = st.sidebar.selectbox('Displaced', ['No', 'Yes'])
    inputs['Debtor'] = st.sidebar.selectbox('Debtor', ['No', 'Yes'])
    inputs['Scholarship_holder'] = st.sidebar.selectbox('Scholarship Holder', ['No', 'Yes'])
    inputs['Tuition_fees_up_to_date'] = st.sidebar.selectbox('Tuition Fees Up-to-date', ['No', 'Yes'])
    inputs['Daytime_evening_attendance'] = st.sidebar.selectbox('Daytime/Evening Attendance', ['No', 'Yes'])
    inputs['Admission_grade'] = st.sidebar.slider('Admission Grade', 0.0, 20.0, 10.0)
    inputs['Previous_qualification_grade'] = st.sidebar.slider('Previous Qualification Grade', 0.0, 20.0, 10.0)
    inputs['Curricular_units_1st_sem_approved'] = st.sidebar.slider('1st Sem Approved Units', 0, 20, 10)
    return pd.DataFrame([inputs])

# Get input data
input_df = user_input_features()

# Preprocessing
st.write("### Input Data")
st.write(input_df)
processed_data = encode_categorical(input_df.copy())
processed_data = scale_numerical(processed_data)

# Prediction
if st.button('Predict'):
    with st.spinner("Predicting..."):
        time.sleep(2)  # Simulate processing
        prediction = model.predict(processed_data)
        result = "Graduate" if prediction[0] == 1 else "Dropout"
        st.success(f"Prediction: The student is likely to {result}.")
