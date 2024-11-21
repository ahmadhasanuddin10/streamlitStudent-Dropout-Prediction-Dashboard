# Students_Performance.py
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
from PIL import Image
import time
from data_preprocessing import data_preprocessing

# Import encoder dan scaler
from data_preprocessing import (
    encoder_Daytime_evening_attendance,
    encoder_Debtor,
    encoder_Displaced,
    encoder_Gender,
    encoder_Scholarship_holder,
    encoder_Tuition_fees_up_to_date,
    scaler_Admission_grade,
    scaler_Curricular_units_1st_sem_approved,
    scaler_Curricular_units_1st_sem_credited,
    scaler_Curricular_units_1st_sem_enrolled,
    scaler_Curricular_units_1st_sem_grade,
    scaler_Curricular_units_2nd_sem_approved,
    scaler_Curricular_units_2nd_sem_credited,
    scaler_Curricular_units_2nd_sem_enrolled,
    scaler_Curricular_units_2nd_sem_grade,
    scaler_Previous_qualification_grade,
)

from prediction import prediction

# Konfigurasi halaman
st.set_page_config(page_title="🎓 Students Performance - Ahmad Hasanuddin", layout="wide")

# Header dan logo
image_files = ['logo-x.png']
desired_width = 160
desired_height = 160

col1, col2 = st.columns([2, 10])
with col1:
    for idx, image_file in enumerate(image_files):
        img = Image.open(image_file)
        resized_img = img.resize((desired_width, desired_height))
        st.image(resized_img)
with col2:
    st.header('Ahmad Hasanuddin Institute')
    st.subheader("Students Performance Prediction App")

# Sidebar untuk informasi pengembang
st.sidebar.write("""
    This web app predicts students' academic performance based on their input features.
""")
st.sidebar.write("""
    **Nama:** Ahmad Hasanuddin \n
    **Email:** ahmad.hasanuddin@app.com \n
    **Id Dicoding:** ahmadhasan
""")

# Fungsi utilitas untuk encoding dan slider
def encode_selection(encoder, selection, labels):
    encoder.fit(labels)
    return encoder.transform([selection])[0]

def create_slider(label, min_value, max_value, value):
    data[label] = [st.slider(label=label.replace('_', ' '), min_value=min_value, max_value=max_value, value=value)]

# Input pengguna
data = {}
col1, col2, col3, col4 = st.columns(4)
with col1:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition fees up to date', options=[0, 1], index=0)
    data['Tuition_fees_up_to_date'] = [Tuition_fees_up_to_date]
with col2:
    Scholarship_holder = st.selectbox(label='Scholarship holder', options=[0, 1], index=0)
    data['Scholarship_holder'] = [Scholarship_holder]
with col3:
    Debtor = st.selectbox(label='Debtor', options=[0, 1], index=1)
    data['Debtor'] = [Debtor]
with col4:
    Displaced = st.selectbox(label='Displaced', options=[0, 1], index=0)
    data['Displaced'] = [Displaced]

col5, col6, col7, col8 = st.columns(4)
with col5:
    Daytime_evening_attendance = st.selectbox(label='Daytime/Evening Attendance', options=[0, 1], index=0)
    data['Daytime_evening_attendance'] = [Daytime_evening_attendance]
with col6:
    Gender = st.selectbox(label='Gender', options=["Female", "Male"], index=1)
    encoder_Gender = LabelEncoder()
    encoder_Gender.fit(["Female", "Male"])
    data['Gender'] = encoder_Gender.transform([Gender])[0]
with col7:
    create_slider('Admission_grade', 95, 190, 100)
with col8:
    create_slider('Previous_qualification_grade', 95, 190, 100)

col9, col10, col11, col12 = st.columns(4)
with col9:
    create_slider('Curricular_units_1st_sem_approved', 0, 26, 5)
with col10:
    create_slider('Curricular_units_1st_sem_grade', 0, 18, 5)
with col11:
    create_slider('Curricular_units_1st_sem_enrolled', 0, 26, 5)
with col12:
    create_slider('Curricular_units_1st_sem_credited', 0, 20, 5)

col13, col14, col15, col16 = st.columns(4)
with col13:
    create_slider('Curricular_units_2nd_sem_approved', 0, 20, 5)
with col14:
    create_slider('Curricular_units_2nd_sem_grade', 0, 20, 12)
with col15:
    create_slider('Curricular_units_2nd_sem_enrolled', 0, 23, 5)
with col16:
    create_slider('Curricular_units_2nd_sem_credited', 0, 19, 5)

# Convert input menjadi DataFrame
user_input_df = pd.DataFrame(data, index=[0])

# Menampilkan input mentah
with st.expander("Input Data"):
    st.dataframe(user_input_df, width=1200, height=200)

# Prediksi
if st.button('Predict Performance'):
    new_data = data_preprocessing(data)
    with st.spinner('Predicting...'):
        time.sleep(2)  # Simulasi proses prediksi
        output = prediction(new_data)
        st.success(f"Predicted Academic Performance: {output}")

st.snow()
