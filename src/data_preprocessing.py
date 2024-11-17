# src/data_preprocessing.py

import pandas as pd

def load_data(file_path):
    """Load the e-commerce data from a CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(data):
    """Clean and preprocess the e-commerce data."""
    # Example: Remove rows with missing values
    data = data.dropna()
    # Example: Convert date columns to datetime format
    data['order_date'] = pd.to_datetime(data['order_date'])
    return data
