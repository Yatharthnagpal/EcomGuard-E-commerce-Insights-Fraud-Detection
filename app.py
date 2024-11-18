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

# Define default file path
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
default_csv = os.path.join(output_dir, "ecommerce_data.csv")

# File Upload Section
st.subheader("Upload or Use Default CSV File")

# Initialize data frame
df = None

# Check if the default CSV file exists
if os.path.exists(default_csv):
    st.write(f"Default CSV file found: `{default_csv}`")
    use_default = st.checkbox("Use default CSV file", value=True)

    if use_default:
        df = pd.read_csv(default_csv)
    else:
        uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
else:
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

# Proceed if data is loaded
if df is not None:
    st.success("Data successfully loaded!")
    
    # Display data preview
    st.write("Data Preview:")
    st.dataframe(df.head())

    # Convert 'order_date' to datetime if present
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

    # Daily Profit/Loss Analysis
    if 'profit' in df.columns and 'order_date' in df.columns:
        st.subheader("Daily Profit/Loss")
        daily_profit = df.groupby('order_date')['profit'].sum().reset_index()
        
        if not daily_profit.empty:
            plt.figure(figsize=(10, 5))
            sns.lineplot(x='order_date', y='profit', data=daily_profit)
            plt.xticks(rotation=45)
            plt.title("Daily Profit/Loss")
            plt.xlabel("Date")
            plt.ylabel("Profit")
            st.pyplot(plt)
        else:
            st.info("No data available for Daily Profit/Loss analysis.")

    # Most Popular Products Analysis
    if 'product_name' in df.columns:
        st.subheader("Most Popular Products")
        popular_products = df['product_name'].value_counts().head(10)
        
        if not popular_products.empty:
            plt.figure(figsize=(10, 5))
            sns.barplot(x=popular_products.index, y=popular_products.values)
            plt.title("Top 10 Most Popular Products")
            plt.xlabel("Product Name")
            plt.ylabel("Number of Orders")
            plt.xticks(rotation=45)
            st.pyplot(plt)
        else:
            st.info("No data available for Popular Products analysis.")

    # Category and Order Status Filters
    if 'category' in df.columns and 'order_status' in df.columns:
        st.subheader("Filter Data by Category and Order Status")
        category_filter = st.selectbox("Select Category", options=df['category'].unique())
        status_filter = st.selectbox("Select Order Status", options=df['order_status'].unique())
        
        # Filter data
        filtered_df = df[(df['category'] == category_filter) & (df['order_status'] == status_filter)]
        st.write("Filtered Data:")
        st.dataframe(filtered_df)

    # Potential Fraud Detection
    if 'discount' in df.columns and 'total_price' in df.columns:
        st.subheader("Potential Fraudulent Orders")
        # Define fraud as orders with a discount greater than 50% of total price
        df['potential_fraud'] = df['discount'] > (0.5 * df['total_price'])
        fraud_orders = df[df['potential_fraud']]
        
        if not fraud_orders.empty:
            st.write("Flagged Fraudulent Orders:")
            st.dataframe(fraud_orders)
        else:
            st.info("No fraudulent orders detected.")
else:
    st.error("No data available. Please upload a CSV file.")
