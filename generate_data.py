import pandas as pd
import random
import os
from faker import Faker

# Initialize Faker for generating fake data
fake = Faker()

# Define the output directory and file path
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
default_csv = os.path.join(output_dir, "ecommerce_data.csv")

def generate_synthetic_data(num_rows=100000):
    """
    Generate synthetic e-commerce data.
    
    Parameters:
        num_rows (int): Number of rows to generate.
    
    Returns:
        pd.DataFrame: Synthetic e-commerce data.
    """
    # Define categories and sample data
    categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Beauty", "Toys"]
    order_statuses = ["Delivered", "Cancelled", "Refunded", "Processing"]
    product_names = [f"Product_{i}" for i in range(1, 101)]
    
    data = {
        "order_id": [fake.uuid4() for _ in range(num_rows)],
        "order_date": [fake.date_between(start_date="-1y", end_date="today") for _ in range(num_rows)],
        "customer_id": [fake.uuid4() for _ in range(num_rows)],
        "product_name": [random.choice(product_names) for _ in range(num_rows)],
        "category": [random.choice(categories) for _ in range(num_rows)],
        "order_status": [random.choice(order_statuses) for _ in range(num_rows)],
        "quantity": [random.randint(1, 5) for _ in range(num_rows)],
        "unit_price": [round(random.uniform(10, 500), 2) for _ in range(num_rows)],
        "discount": [round(random.uniform(0, 100), 2) for _ in range(num_rows)],
    }
    
    # Calculate total price and profit
    df = pd.DataFrame(data)
    df["total_price"] = (df["quantity"] * df["unit_price"]).round(2)
    df["profit"] = (df["total_price"] - df["discount"]).round(2)
    
    return df

if __name__ == "__main__":
    # User input for the number of rows
    num_rows = input("Enter the number of rows to generate (default: 100,000): ")
    num_rows = int(num_rows) if num_rows.isdigit() else 100000

    # Generate data and save to CSV
    df = generate_synthetic_data(num_rows)
    df.to_csv(default_csv, index=False)
    
    print(f"Synthetic e-commerce data generated and saved to: {default_csv}")
