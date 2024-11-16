import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define the number of rows
num_rows = 100000

# Define sample data
product_names = ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet", "Camera"]
categories = ["Electronics", "Fashion", "Home", "Toys", "Beauty"]
coupon_codes = ["SAVE10", "DISCOUNT20", "FREESHIP", "SUMMER50", None]
payment_methods = ["Credit Card", "PayPal", "Gift Card", "Bitcoin"]
statuses = ["Completed", "Pending", "Cancelled", "Refunded"]

# Helper function to generate synthetic data
def generate_data(num_rows):
    data = []
    for _ in range(num_rows):
        order_id = fake.uuid4()
        customer_name = fake.name()
        product_name = random.choice(product_names)
        category = random.choice(categories)
        quantity = random.randint(1, 10)
        unit_price = round(random.uniform(10, 1000), 2)
        total_price = round(unit_price * quantity, 2)
        discount = round(random.uniform(0, 0.3) * total_price, 2)
        total_discount = round(total_price - discount, 2)
        coupon_code = random.choice(coupon_codes)
        payment_method = random.choice(payment_methods)
        order_status = random.choice(statuses)
        order_date = fake.date_this_year()
        cost_price = round(unit_price * random.uniform(0.5, 0.8), 2)
        profit = total_price - discount - (cost_price * quantity)

        data.append([
            order_id, customer_name, product_name, category, quantity,
            unit_price, total_price, discount, total_discount,
            coupon_code, payment_method, order_status, order_date,
            cost_price, profit
        ])

    return data

# Define column names
columns = [
    "order_id", "customer_name", "product_name", "category", "quantity",
    "unit_price", "total_price", "discount", "total_discount",
    "coupon_code", "payment_method", "order_status", "order_date",
    "cost_price", "profit"
]

# Generate data and create DataFrame
data = generate_data(num_rows)
df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV
df.to_csv("ecommerce_data.csv", index=False)
print("Data generated and saved as 'ecommerce_data.csv'.")
