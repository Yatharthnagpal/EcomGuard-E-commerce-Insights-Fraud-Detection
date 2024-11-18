# src/fraud_detection.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score

class FraudModel:
    def __init__(self):
        """Initialize the fraud detection model."""
        self.model = RandomForestClassifier()
        self.scaler = StandardScaler()
        self.lbenc = LabelEncoder()

    def preprocess_data(self, data):
        """Preprocess the data for the model."""
        # Example: Feature engineering, handling missing values, and scaling
        data.fillna('No', inplace=True)  # Drop rows with missing values
        # Assuming 'amount' is the feature and 'is_fraud' is the target variable
        features = data.drop(columns=['is_fraud','order_id','customer_name','order_date'])
        target = data['is_fraud']
        
        catcol = ['product_name','category','coupon_code','payment_method','order_status']
        for col in catcol:
            features[col] = self.lbenc.fit_transform(features[col])
        
        # Scale the features for better model performance
        features_scaled = self.scaler.fit_transform(features)
        
        return features_scaled, target

    def train(self, data):
        """Train the fraud detection model."""
        X, y = self.preprocess_data(data)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Evaluate model accuracy
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy * 100:.2f}%")

    def predict(self, data):
        """Predict if a transaction is fraudulent."""
        # Preprocess the data before prediction
        features_scaled, _ = self.preprocess_data(data)
        return self.model.predict(features_scaled)

    def predict_proba(self, data):
        """Predict the probability of a transaction being fraudulent."""
        features_scaled, _ = self.preprocess_data(data)
        return self.model.predict_proba(features_scaled)[:, 1]  # Return probability of fraud

# Create a function for fraud detection that can be used in tests
def detect_fraud(data):
    """Function to detect fraud based on the fraud model."""
    fraud_model = FraudModel()
    fraud_model.train(data)  # Train the model on the data
    predictions = fraud_model.predict(data)  # Predict fraud
    data['is_fraud'] = predictions.tolist()
    # print(len(predictions))
    # print(type(predictions))
    return data
