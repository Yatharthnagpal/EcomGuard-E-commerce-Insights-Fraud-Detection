import unittest
import pandas as pd
import sys, os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:\\Users\\Yatharth nagpal\\Desktop\\challenge3\\src')))
from fraud_detection import detect_fraud

class TestFraudDetection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load sample data for testing."""
        cls.data = pd.read_csv('C:\\Users\\Yatharth nagpal\\Desktop\\challenge3\\data\\ecommerce_data.csv')
        
        # Print column names to help identify the correct column
        print("Dataset Columns:", cls.data.columns)
        
        # Check if 'amount' exists or update with the correct column name
        if 'profit' in cls.data.columns:
            cls.data['is_fraud'] = (cls.data['profit'] > cls.data['profit'].quantile(0.9)).astype(int)
        else:
            # Example: Use another column like 'price' if 'amount' is not available
            if 'price' in cls.data.columns:
                cls.data['is_fraud'] = (cls.data['price'] > cls.data['price'].quantile(0.9)).astype(int)
            else:
                raise ValueError("Neither 'profit' nor 'price' columns found in dataset.")

    def test_detect_fraud(self):
        """Test fraud detection logic."""
        fraud_results = detect_fraud(self.data)
        self.assertIsInstance(fraud_results, pd.DataFrame)
        self.assertIn('is_fraud', fraud_results.columns)

    def test_fraud_flagging(self):
        """Test if fraud transactions are flagged correctly."""
        fraud_results = detect_fraud(self.data)
        flagged_fraud = fraud_results[fraud_results['is_fraud'] == 1]
        self.assertGreater(len(flagged_fraud), 0, "No fraud cases detected.")

if __name__ == '__main__':
    unittest.main()
