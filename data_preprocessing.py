import joblib
import numpy as np
import pandas as pd

def data_preprocessing(data):
    """Preprocessing data

    Args:
        data (Pandas DataFrame): Dataframe that contains all the data to make predictions

    Returns:
        Pandas DataFrame: Dataframe with all the preprocessed data
    """
    # Validasi apakah data adalah DataFrame
    if not isinstance(data, pd.DataFrame):
        raise TypeError(f"Expected input to be a Pandas DataFrame, but got {type(data).__name__} instead.")

    # Salin data untuk memastikan tidak memodifikasi input asli
    data = data.copy()
    
    # List kolom yang diperlukan
    required_columns = [
        "Tuition_fees_up_to_date",
        "Scholarship_holder",
        "Debtor",
        "Displaced",
        "Daytime_evening_attendance",
        "Gender",
        "Admission_grade",
        "Curricular_units_1st_sem_approved",
        "Curricular_units_1st_sem_credited",
        "Curricular_units_1st_sem_enrolled",
        "Curricular_units_1st_sem_grade",
        "Curricular_units_2nd_sem_approved",
        "Curricular_units_2nd_sem_credited",
        "Curricular_units_2nd_sem_enrolled",
        "Curricular_units_2nd_sem_grade",
        "Previous_qualification_grade",
    ]
    
    # Periksa kolom yang hilang
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise KeyError(f"The following columns are missing from the dataset: {missing_columns}")

def data_preprocessing(data):
    """Preprocessing data"""
    import logging

    # Debug: Periksa tipe data
    logging.debug(f"Received data type: {type(data)}")
    
    if not isinstance(data, pd.DataFrame):
        raise TypeError(f"Expected input to be a Pandas DataFrame, but got {type(data).__name__}.")

    # Debug: Periksa kolom data
    logging.debug(f"Data columns: {data.columns.tolist()}")

    # Lanjutkan proses data seperti biasa...







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

# Helper function to apply encoder or scaler
def apply_encoder_or_scaler(data, column, transformer, is_scaler=False):
    """Applies the encoder or scaler to a given column of data."""
    if column in data.columns:
        if is_scaler:
            try:
                return transformer.transform(np.asarray(data[column]).reshape(-1, 1))
            except Exception as e:
                raise ValueError(f"Error scaling column '{column}': {e}")
        else:
            try:
                return transformer.transform(data[column])
            except Exception as e:
                raise ValueError(f"Error encoding column '{column}': {e}")
    else:
        raise KeyError(f"Column '{column}' not found in the data.")

# Main preprocessing function
def data_preprocessing(data):
    """Preprocessing data

    Args:
        data (Pandas DataFrame): Dataframe that contains all the data to make predictions

    Returns:
        Pandas DataFrame: Dataframe with all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()

    # List of required columns
    required_columns = [
        "Tuition_fees_up_to_date",
        "Scholarship_holder",
        "Debtor",
        "Displaced",
        "Daytime_evening_attendance",
        "Gender",
        "Admission_grade",
        "Curricular_units_1st_sem_approved",
        "Curricular_units_1st_sem_credited",
        "Curricular_units_1st_sem_enrolled",
        "Curricular_units_1st_sem_grade",
        "Curricular_units_2nd_sem_approved",
        "Curricular_units_2nd_sem_credited",
        "Curricular_units_2nd_sem_enrolled",
        "Curricular_units_2nd_sem_grade",
        "Previous_qualification_grade",
    ]

    # Check for missing columns
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise KeyError(f"The following columns are missing from the dataset: {missing_columns}")

    # Preprocess each column
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
    except Exception as e:
        raise RuntimeError(f"An error occurred during preprocessing: {e}")

    return df
