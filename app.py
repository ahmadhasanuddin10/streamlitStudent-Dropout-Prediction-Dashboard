import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# Load data
@st.cache
def load_data():
    data = pd.read_csv("data(1).csv", sep=";")
    return data

# Preprocess data
def preprocess_data(data):
    categorical_features = ['Gender', 'Displaced', 'Debtor', 'Scholarship_holder', 'Tuition_fees_up_to_date', 'Daytime_evening_attendance']
    data[categorical_features] = data[categorical_features].replace({'0': 'No', '1': 'Yes'})

    # Encoding
    label_encoder = LabelEncoder()
    for col in categorical_features:
        data[col] = label_encoder.fit_transform(data[col])

    # Normalization
    scaler = StandardScaler()
    scaled_columns = ['Admission_grade', 'Previous_qualification_grade', 'Curricular_units_1st_sem_approved']
    data[scaled_columns] = scaler.fit_transform(data[scaled_columns])

    return data

# Model training
def train_models(X_train, y_train):
    # Train Decision Tree
    dt_model = DecisionTreeClassifier()
    dt_params = {'max_depth': [5, 10], 'min_samples_leaf': [1, 5], 'criterion': ['gini', 'entropy']}
    dt_grid = GridSearchCV(dt_model, dt_params, cv=5, scoring='accuracy')
    dt_grid.fit(X_train, y_train)

    # Train Logistic Regression
    lr_model = LogisticRegression()
    lr_params = {'C': [0.1, 1, 10], 'solver': ['liblinear', 'saga']}
    lr_grid = GridSearchCV(lr_model, lr_params, cv=5, scoring='accuracy')
    lr_grid.fit(X_train, y_train)

    # Train Random Forest
    rf_model = RandomForestClassifier()
    rf_params = {'n_estimators': [100, 200], 'max_depth': [10, 20]}
    rf_grid = GridSearchCV(rf_model, rf_params, cv=5, scoring='accuracy')
    rf_grid.fit(X_train, y_train)

    return dt_grid, lr_grid, rf_grid

# Predict and visualize results
def predict_and_visualize(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    st.write(f"{model_name} Confusion Matrix")
    st.pyplot(sns.heatmap(cm, annot=True, cmap='viridis', fmt='g'))

    st.write(f"{model_name} Classification Report:")
    st.text(classification_report(y_test, y_pred))

# Streamlit app layout
st.title("Machine Learning Model Deployment")
st.write("This is a simple Streamlit app for training and evaluating machine learning models.")

# Load and preprocess the data
data = load_data()
data = preprocess_data(data)

# Split the data
X = data.drop(['Status'], axis=1)
y = data['Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
dt_grid, lr_grid, rf_grid = train_models(X_train, y_train)

# Display model accuracy
st.write(f"Best Decision Tree Accuracy: {accuracy_score(y_test, dt_grid.predict(X_test))}")
st.write(f"Best Logistic Regression Accuracy: {accuracy_score(y_test, lr_grid.predict(X_test))}")
st.write(f"Best Random Forest Accuracy: {accuracy_score(y_test, rf_grid.predict(X_test))}")

# Visualize confusion matrices
predict_and_visualize(dt_grid, X_test, y_test, "Decision Tree")
predict_and_visualize(lr_grid, X_test, y_test, "Logistic Regression")
predict_and_visualize(rf_grid, X_test, y_test, "Random Forest")
