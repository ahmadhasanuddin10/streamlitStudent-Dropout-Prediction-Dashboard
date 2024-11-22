import streamlit as st
import pandas as pd
import joblib
import time
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load trained model
model_path = 'Random_Forest_Model.joblib'
model = joblib.load(model_path)

# Predefined encoders and scalers
categorical_features = ['Gender', 'Displaced', 'Debtor', 'Scholarship_holder', 'Tuition_fees_up_to_date', 'Daytime_evening_attendance']
scalers = {'Admission_grade': StandardScaler(), 
           'Previous_qualification_grade': StandardScaler(), 
           'Curricular_units_1st_sem_approved': StandardScaler()}

# Initialize encoders
encoders = {feature: LabelEncoder() for feature in categorical_features}
for feature in categorical_features:
    encoders[feature].fit(['No', 'Yes'])

# Custom function for preprocessing
def preprocess_input(data):
    # Encode categorical features
    for feature in categorical_features:
        data[feature] = encoders[feature].transform(data[feature])
    # Scale numerical features
    for feature, scaler in scalers.items():
        data[feature] = scaler.fit_transform(data[feature].values.reshape(-1, 1))
    return data

# Streamlit UI
st.set_page_config(page_title="🎓 Students Performance Prediction", layout="wide")

st.title("🎓 Students Performance Prediction")
st.write("Use this application to predict student performance outcomes.")

# User input
data = {}
columns = st.columns(2)

with columns[0]:
    data['Gender'] = st.selectbox('Gender', ['Male', 'Female'])
    data['Displaced'] = st.selectbox('Displaced', ['No', 'Yes'])
    data['Debtor'] = st.selectbox('Debtor', ['No', 'Yes'])
    data['Scholarship_holder'] = st.selectbox('Scholarship Holder', ['No', 'Yes'])

with columns[1]:
    data['Tuition_fees_up_to_date'] = st.selectbox('Tuition Fees Up-to-Date', ['No', 'Yes'])
    data['Daytime_evening_attendance'] = st.selectbox('Attendance', ['Daytime', 'Evening'])
    data['Admission_grade'] = st.slider('Admission Grade', 95, 190, 120)
    data['Previous_qualification_grade'] = st.slider('Previous Qualification Grade', 95, 190, 120)

data['Curricular_units_1st_sem_approved'] = st.slider('Curricular Units 1st Semester Approved', 0, 26, 10)

# Convert user input to DataFrame
user_input_df = pd.DataFrame([data])

# Display raw user input
st.write("### Raw User Input")
st.dataframe(user_input_df)

# Prediction
if st.button("Predict"):
    with st.spinner("Processing..."):
        # Preprocess data
        processed_data = preprocess_input(user_input_df)
        # Predict
        prediction = model.predict(processed_data)
        # Map prediction to labels
        result = "Graduate" if prediction[0] == 1 else "Dropout"
        st.success(f"The predicted status is: {result}")
