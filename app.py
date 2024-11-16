import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set page title and description
st.set_page_config(page_title="EcomGuard: E-commerce Insights & Fraud Detection")

# Title and description
st.title("EcomGuard: E-commerce Insights & Fraud Detection")
st.markdown("""
    **EcomGuard** provides insights into your e-commerce data and detects potential fraudulent orders.
    Analyze daily profits, identify the most popular products, and flag suspicious orders.
""")

# Check if the default file exists
default_csv = "ecommerce_data.csv"
df = None

# Load the default CSV file if it exists
if os.path.exists(default_csv):
    df = pd.read_csv(default_csv)
    st.write(f"Loaded default CSV file: {default_csv}")
else:
    # Allow user to upload a CSV file
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Loaded uploaded CSV file.")

# Check if data is available before proceeding with further operations
if df is not None:
    # Display data preview
    st.write("Data Preview:")
    st.dataframe(df.head())
    
    # Convert 'order_date' to datetime
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Daily Profit/Loss
    daily_profit = df.groupby('order_date')['profit'].sum().reset_index()
    st.subheader("Daily Profit/Loss")
    plt.figure(figsize=(10, 5))
    sns.lineplot(x='order_date', y='profit', data=daily_profit)
    plt.xticks(rotation=45)
    plt.title("Daily Profit/Loss")
    plt.xlabel("Date")
    plt.ylabel("Profit")
    st.pyplot(plt)

    # Most Popular Products
    popular_products = df['product_name'].value_counts().head(10)
    st.subheader("Most Popular Products")
    plt.figure(figsize=(10, 5))
    sns.barplot(x=popular_products.index, y=popular_products.values)
    plt.title("Top 10 Most Popular Products")
    plt.xlabel("Product Name")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Create filters for category and order status
    category_filter = st.selectbox("Select Category", options=df['category'].unique())
    status_filter = st.selectbox("Select Order Status", options=df['order_status'].unique())
    
    # Filter data based on selected category and order status
    filtered_df = df[(df['category'] == category_filter) & (df['order_status'] == status_filter)]
    st.write("Filtered Data:")
    st.dataframe(filtered_df)

    # Flagging potential fraudulent orders
    df['potential_fraud'] = df['discount'] > (0.5 * df['total_price'])
    fraud_orders = df[df['potential_fraud']]
    st.subheader("Potential Fraudulent Orders")
    st.dataframe(fraud_orders)

else:
    st.write("No data available. Please upload a CSV file.")
