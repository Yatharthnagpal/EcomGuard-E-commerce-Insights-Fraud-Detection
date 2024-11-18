# src/data_preprocessing.py
import pandas as pd

def load_data(file_path):
    """Load the e-commerce data from a CSV file."""
    return pd.read_csv(file_path)

import pandas as pd

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data, handling date conversion and missing values."""
    
    # Print the first few rows of 'order_date' before conversion
    print(f"First few rows of 'order_date' before conversion:\n{data['order_date'].head()}")
    
    # Convert 'order_date' to datetime format
    data['order_date'] = pd.to_datetime(data['order_date'], errors='coerce')
    
    # Print the first few rows of 'order_date' after conversion
    print(f"First few rows of 'order_date' after conversion:\n{data['order_date'].head()}")
    
    # Handle any NaN values if necessary (e.g., drop rows with NaN dates)
    data.dropna(subset=['order_date'], inplace=True)
    data.fillna(value = 'No', inplace=True)
    
    return data

