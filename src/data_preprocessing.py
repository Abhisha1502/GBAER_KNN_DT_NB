import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_data(filepath):
    """
    Load the dataset from CSV file
    """
    df = pd.read_csv(filepath)
    return df


def handle_missing_values(df):
    """
    Handle missing values:
    - Numerical columns: mean
    - Categorical columns: mode
    """
    num_cols = df.select_dtypes(include=np.number).columns
    cat_cols = df.select_dtypes(include='object').columns

    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df


def encode_categorical_features(df):
    """
    Encode categorical columns using Label Encoding
    """
    label_encoder = LabelEncoder()
    cat_cols = df.select_dtypes(include='object').columns

    for col in cat_cols:
        df[col] = label_encoder.fit_transform(df[col])

    return df


def scale_features(df):
    """
    Scale numerical features using StandardScaler
    """
    scaler = StandardScaler()
    num_cols = df.select_dtypes(include=np.number).columns

    df[num_cols] = scaler.fit_transform(df[num_cols])
    return df

if __name__ == "__main__":
    df = load_data("../data/Global_Pollution_Analysis.csv")
    df = handle_missing_values(df)
    df = encode_categorical_features(df)
    df = scale_features(df)

    print("Data preprocessing completed successfully.")
    print(df.head())
