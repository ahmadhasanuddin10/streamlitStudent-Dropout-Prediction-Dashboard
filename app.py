import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
from PIL import Image
import time
from data_preprocessing import data_preprocessing

from data_preprocessing import encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Displaced, encoder_Gender, encoder_Scholarship_holder, encoder_Tuition_fees_up_to_date
from data_preprocessing import scaler_Admission_grade, scaler_Curricular_units_1st_sem_approved, scaler_Curricular_units_1st_sem_credited, scaler_Curricular_units_1st_sem_enrolled, scaler_Curricular_units_1st_sem_grade, scaler_Curricular_units_2nd_sem_approved, scaler_Curricular_units_2nd_sem_credited, scaler_Curricular_units_2nd_sem_enrolled, scaler_Curricular_units_2nd_sem_grade, scaler_Previous_qualification_grade

from prediction import prediction




st.set_page_config(page_title="🎓 Students Performance", layout="wide")

# Customizing the app's look
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f4f9;
    }
    .css-ffhzg2 {
        background-color: #4CAF50;
        color: white;
        font-size: 1.5em;
    }
    .css-1v0mbdj {
        padding: 10px;
        background-color: #E0E0E0;
    }
    .css-1d391kg {
        background-color: #ffffff;
    }
    .css-12ttk8i {
        margin-top: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# Add logo
image_files = ['pubg.png']
desired_width = 160
desired_height = 160

# Create a row for the logo and introductory information
col1, col2 = st.columns([1, 3])

with col1:
    for idx, image_file in enumerate(image_files):
        img = Image.open(image_file)
        resized_img = img.resize((desired_width, desired_height))
        st.image(resized_img)
with col2:
    st.header('Jaya Jaya Institut')
    st.subheader("Students Performance Prediction")
    st.write("""
        Digunakan untuk memprediksi Performa Mahasiswa
    """)
    st.write("""
        **Nama:** Hasanuddin \n
        **Email:** hasanuddin5@gmail.com \n
        
    """)


# Initialize an empty dictionary to store user input
data = {}

# Convert user input dictionary to DataFrame
user_input_df = pd.DataFrame(data, index=[0])

def encode_selection(encoder, selection, labels):
    encoder.fit(labels)
    return encoder.transform([selection])[0]

def create_slider(label, min_value, max_value, value):
    data[label] = [st.slider(label=label.replace('_', ' '), min_value=min_value, max_value=max_value, value=value)]

# Create form for input fields
col1, col2, col3, col4 = st.columns(4)
with col1:
    encoder_Tuition_fees_up_to_date.fit([0, 1])
    Tuition_fees_up_to_date = st.selectbox(label='Tuition fees', options=[0, 1], index=0)
    data['Tuition_fees_up_to_date'] = [encoder_Tuition_fees_up_to_date.transform([Tuition_fees_up_to_date])[0]]
with col2:
    encoder_Scholarship_holder.fit([0, 1])
    Scholarship_holder = st.selectbox(label='Scholarship holder', options=[0, 1], index=0)
    data['Scholarship_holder'] = [encoder_Scholarship_holder.transform([Scholarship_holder])[0]]
with col3:
    encoder_Debtor.fit([0, 1])
    Debtor = st.selectbox(label='Debtor', options=[0, 1], index=1)
    data['Debtor'] = [encoder_Debtor.transform([Debtor])[0]]
with col4:
    encoder_Displaced.fit([0, 1])
    Displaced = st.selectbox(label='Displaced', options=[0, 1], index=0)
    data['Displaced'] = [encoder_Displaced.transform([Displaced])[0]]

col5, col6, col7, col8 = st.columns(4)
with col5:
    encoder_Daytime_evening_attendance.fit([0, 1])
    Daytime_evening_attendance = st.selectbox(label='Attendance', options=[0, 1], index=0)
    data['Daytime_evening_attendance'] = [encoder_Daytime_evening_attendance.transform([Daytime_evening_attendance])[0]]
with col6:
    encoder_Gender = LabelEncoder()
    encoder_Gender.fit(["Female", "Male"])
    Gender = st.selectbox(label='Gender', options=["Female", "Male"], index=1)
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

# Convert user input dictionary to DataFrame
user_input_df = pd.DataFrame(data, index=[0])

# Display user input
with st.expander("Raw Dataset"):
    st.dataframe(data=user_input_df, width=1200, height=20)

# Preprocess data and make prediction on button click
if st.button('Click Here to Predict'):
    new_data = data_preprocessing(data=data)
    with st.spinner('Predicting...'):
        time.sleep(2)  # Simulating prediction process
        output = prediction(new_data)
        st.success(f"Prediction: {output}")


