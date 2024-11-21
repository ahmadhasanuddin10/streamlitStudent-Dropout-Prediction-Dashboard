import joblib
import numpy as np
import pandas as pd

# Load encoders and scalers
encoder_Tuition_fees_up_to_date = joblib.load("model/encoder_Tuition_fees_up_to_date.joblib")
encoder_Scholarship_holder = joblib.load("model/encoder_Scholarship_holder.joblib")
encoder_Debtor = joblib.load("model/encoder_Debtor.joblib")
encoder_Displaced = joblib.load("model/encoder_Displaced.joblib")
encoder_Daytime_evening_attendance = joblib.load("model/encoder_Daytime_evening_attendance.joblib")
encoder_Gender = joblib.load("model/encoder_Gender.joblib")
scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_credited = joblib.load("model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_credited = joblib.load("model/scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")

# Function to apply encoding and scaling
def apply_encoder_or_scaler(data, column, transformer, is_scaler=False):
    """Applies the encoder or scaler to a given column of data."""
    if column in data.columns:
        if is_scaler:
            return transformer.transform(np.asarray(data[column]).reshape(-1, 1))
        else:
            return transformer.transform(data[column])
    else:
        raise KeyError(f"Column '{column}' not found in the data.")

def data_preprocessing(data):
    """Preprocessing data

    Args:
        data (Pandas DataFrame): Dataframe that contains all the data to make predictions

    Returns:
        Pandas DataFrame: Dataframe with all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()

    # Apply transformations with error handling
    try:
        df["Tuition_fees_up_to_date"] = apply_encoder_or_scaler(data, "Tuition_fees_up_to_date", encoder_Tuition_fees_up_to_date)
        df["Scholarship_holder"] = apply_encoder_or_scaler(data, "Scholarship_holder", encoder_Scholarship_holder)
        df["Debtor"] = apply_encoder_or_scaler(data, "Debtor", encoder_Debtor)
        df["Displaced"] = apply_encoder_or_scaler(data, "Displaced", encoder_Displaced)
        df["Daytime_evening_attendance"] = apply_encoder_or_scaler(data, "Daytime_evening_attendance", encoder_Daytime_evening_attendance)
        df["Gender"] = apply_encoder_or_scaler(data, "Gender", encoder_Gender)
        df["Admission_grade"] = apply_encoder_or_scaler(data, "Admission_grade", scaler_Admission_grade, is_scaler=True)
        df["Curricular_units_1st_sem_approved"] = apply_encoder_or_scaler(data, "Curricular_units_1st_sem_approved", scaler_Curricular_units_1st_sem_approved, is_scaler=True)
        df["Curricular_units_1st_sem_credited"] = apply_encoder_or_scaler(data, "Curricular_units_1st_sem_credited", scaler_Curricular_units_1st_sem_credited, is_scaler=True)
        df["Curricular_units_1st_sem_enrolled"] = apply_encoder_or_scaler(data, "Curricular_units_1st_sem_enrolled", scaler_Curricular_units_1st_sem_enrolled, is_scaler=True)
        df["Curricular_units_1st_sem_grade"] = apply_encoder_or_scaler(data, "Curricular_units_1st_sem_grade", scaler_Curricular_units_1st_sem_grade, is_scaler=True)
        df["Curricular_units_2nd_sem_approved"] = apply_encoder_or_scaler(data, "Curricular_units_2nd_sem_approved", scaler_Curricular_units_2nd_sem_approved, is_scaler=True)
        df["Curricular_units_2nd_sem_credited"] = apply_encoder_or_scaler(data, "Curricular_units_2nd_sem_credited", scaler_Curricular_units_2nd_sem_credited, is_scaler=True)
        df["Curricular_units_2nd_sem_enrolled"] = apply_encoder_or_scaler(data, "Curricular_units_2nd_sem_enrolled", scaler_Curricular_units_2nd_sem_enrolled, is_scaler=True)
        df["Curricular_units_2nd_sem_grade"] = apply_encoder_or_scaler(data, "Curricular_units_2nd_sem_grade", scaler_Curricular_units_2nd_sem_grade, is_scaler=True)
        df["Previous_qualification_grade"] = apply_encoder_or_scaler(data, "Previous_qualification_grade", scaler_Previous_qualification_grade, is_scaler=True)
    except KeyError as e:
        print(f"Error: {e}")
        return None  # Or handle error appropriately

    return df
