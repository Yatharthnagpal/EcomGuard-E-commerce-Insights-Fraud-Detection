# EcomGuard - E-commerce Insights & Fraud Detection

EcomGuard is a comprehensive data visualization dashboard designed to provide deep insights into e-commerce transaction data and detect potential fraudulent activities. By leveraging data science techniques and machine learning models, this project helps e-commerce businesses make data-driven decisions and improve operational efficiency.

## Features

- **Interactive Dashboards:** View real-time key metrics, transaction trends, and patterns.
- **Fraud Detection:** Detect and flag potentially fraudulent transactions using machine learning models.
- **Data Exploration:** Explore various data dimensions such as sales, customer demographics, and product categories.
- **Customizable Visualizations:** Tailor charts and tables to focus on specific data points and user needs.

## Tech Stack

- **Python:** Core programming language for data analysis and machine learning.
- **Pandas:** Data manipulation and analysis.
- **Matplotlib & Seaborn:** Visualization libraries for generating static plots.
- **Plotly:** Interactive graphing for dynamic data visualizations.
- **Scikit-learn:** Machine learning library for building fraud detection models.
- **Dash:** Framework for building interactive web-based dashboards.
- **Jupyter Notebook:** Development environment for experimentation and testing.

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Yatharthnagpal/EcomGuard-E-commerce-Insights-Fraud-Detection.git
cd EcomGuard-E-commerce-Insights-Fraud-Detection
```

### 2. Set Up a Virtual Environment

It is recommended to use a virtual environment to manage the dependencies. To create and activate the virtual environment, run:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Next, install all the required libraries listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project directory to store any sensitive information such as API keys or database credentials (if required).

### 5. Running the Dashboard

Once all dependencies are installed, you can start the application by running:

```bash
python app.py
```

The dashboard will be accessible at `http://127.0.0.1:8050/` in your web browser.

## Data

The dataset used in this project can be accessed from the following link:

[Download Ecommerce Dataset](#)

### Data Error Resolution

During development, a few issues were identified with the dataset, particularly related to missing values, incorrect data types, and inconsistent formats in certain columns. The following steps have been taken to resolve these errors:

1. **Missing Values:** Handled missing data by either filling with appropriate default values or dropping rows with critical missing values.
2. **Data Type Corrections:** Some columns had incorrect data types (e.g., numeric columns were read as strings), which were corrected during data preprocessing.
3. **Standardizing Formats:** Uniform formatting was applied to date columns and product IDs for consistency.
4. **Fraud Detection Adjustments:** The fraud detection model was re-trained with clean data, resulting in improved accuracy and fewer false positives.

## Usage

The EcomGuard Dashboard provides various interactive visualizations to explore the data:

- **Transaction Analysis:** An overview of sales, returns, and customer trends.
- **Fraud Detection:** Insights into flagged transactions based on machine learning models.
- **Customer Insights:** In-depth analysis of customer purchasing behavior and segmentation.
- **Product Insights:** Trends and performance metrics for different product categories.

Users can filter and interact with the data by region, product category, or time period to gain more granular insights.

## License

This project is licensed under the [MIT License](https://github.com/Yatharthnagpal/EcomGuard-E-commerce-Insights-Fraud-Detection/blob/main/LICENSE).
