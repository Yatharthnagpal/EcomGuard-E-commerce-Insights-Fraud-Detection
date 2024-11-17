# src/dashboard.py

import dash
from dash import html, dcc

def create_dashboard(app):
    """Create the Dash dashboard layout."""
    app.layout = html.Div([
        html.H1("E-commerce Insights & Fraud Detection"),
        dcc.Graph(id="transaction-trend"),
        dcc.Dropdown(
            id="product-category-dropdown",
            options=[
                {'label': 'Electronics', 'value': 'electronics'},
                {'label': 'Clothing', 'value': 'clothing'}
            ],
            value='electronics'
        )
    ])
