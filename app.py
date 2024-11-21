import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
from PIL import Image
import time
from data_preprocessing import preprocess_data, encode_feature
from prediction import generate_prediction

# Set up the Streamlit page
st.set_page_config(page_title="🎓 Predicting Student Performance", layout="wide")

# Displaying logo image
image_files = ['logouns.png']
desired_width = 160
desired_height = 160
col1, col2 = st.columns([2, 10])

with col1:
    for idx, image_file in enumerate(image_files):
        img = Image.open(image_file)
        resized_img = img.resize((desired_width, desired_height))
        st.image(resized_img)

with col2:
    st.header('UNS')
    st.subheader("Predicting Student's Academic Performance")

# Sidebar description
st.sidebar.write("""
    This web app is designed to predict the academic performance of students based on various factors.
""")
st.sidebar.write("""
    **Name:** hasan \n
    **Email:** hasan6@gmail.com \n
     -
""")

# Initialize an empty dictionary to store user input
user_data = {}

# Convert input dictionary to DataFrame
user_input_df = pd.DataFrame(user_data, index=[0])

# Function to encode categorical input using the provided encoder
def encode_user_input(encoder, user_selection, label_options):
    encoder.fit(label_options)
    return encoder.transform([user_selection])[0]

# Function to create slider for numeric input
def create_numeric_slider(label, min_value, max_value, default_value):
    user_data[label] = [st.slider(label=label.replace('_', ' ').title(), min_value=min_value, max_value=max_value, value=default_value)]

# Feature inputs for prediction
col1, col2, col3, col4 = st.columns(4)

with col1:
    tuition_fees = st.selectbox('Tuition Fees Status', options=[0, 1], index=0)
    user_data['Tuition_fees'] = [encode_user_input(LabelEncoder(), tuition_fees, [0, 1])]

with col2:
    scholarship_status = st.selectbox('Scholarship Holder', options=[0, 1], index=0)
    user_data['Scholarship'] = [encode_user_input(LabelEncoder(), scholarship_status, [0, 1])]

with col3:
    debtor_status = st.selectbox('Debtor Status', options=[0, 1], index=1)
    user_data['Debtor'] = [encode_user_input(LabelEncoder(), debtor_status, [0, 1])]

with col4:
    displaced_status = st.selectbox('Displaced Student', options=[0, 1], index=0)
    user_data['Displaced'] = [encode_user_input(LabelEncoder(), displaced_status, [0, 1])]

# Additional feature inputs in subsequent columns
col5, col6, col7, col8 = st.columns(4)

with col5:
    attendance_type = st.selectbox('Class Attendance', options=[0, 1], index=0)
    user_data['Attendance'] = [encode_user_input(LabelEncoder(), attendance_type, [0, 1])]

with col6:
    gender = st.selectbox('Gender', options=["Female", "Male"], index=1)
    user_data['Gender'] = LabelEncoder().fit(["Female", "Male"]).transform([gender])[0]

with col7:
    create_numeric_slider('Admission Grade', 95, 190, 100)

with col8:
    create_numeric_slider('Previous Qualification Grade', 95, 190, 100)

# Other academic features
col9, col10, col11, col12 = st.columns(4)
with col9:
    create_numeric_slider('1st Semester Approved Units', 0, 26, 5)

with col10:
    create_numeric_slider('1st Semester Grade', 0, 18, 5)

with col11:
    create_numeric_slider('1st Semester Enrolled Units', 0, 26, 5)

with col12:
    create_numeric_slider('1st Semester Credited Units', 0, 20, 5)

col13, col14, col15, col16 = st.columns(4)
with col13:
    create_numeric_slider('2nd Semester Approved Units', 0, 20, 5)

with col14:
    create_numeric_slider('2nd Semester Grade', 0, 20, 12)

with col15:
    create_numeric_slider('2nd Semester Enrolled Units', 0, 23, 5)

with col16:
    create_numeric_slider('2nd Semester Credited Units', 0, 19, 5)

# Convert the user input to DataFrame
user_input_df = pd.DataFrame(user_data, index=[0])

# Display the input data for review
with st.expander("Review Your Data"):
    st.dataframe(user_input_df, width=1200, height=300)

# Make prediction on button click
if st.button('Predict Student Performance'):
    preprocessed_data = preprocess_data(user_data)
    with st.spinner('Making Prediction...'):
        time.sleep(2)  # Simulating prediction delay
        prediction_result = generate_prediction(preprocessed_data)
        st.success(f"Predicted Performance: {prediction_result}")

st.snow()
