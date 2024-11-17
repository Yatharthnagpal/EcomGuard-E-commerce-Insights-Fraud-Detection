# src/fraud_detection.py

from sklearn.ensemble import RandomForestClassifier

class FraudModel:
    def __init__(self):
        """Initialize the fraud detection model."""
        self.model = RandomForestClassifier()

    def train(self, X_train, y_train):
        """Train the fraud detection model."""
        self.model.fit(X_train, y_train)

    def predict(self, data):
        """Predict if a transaction is fraudulent."""
        return self.model.predict(data)
