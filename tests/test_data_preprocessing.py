import unittest
import pandas as pd
# Add the src directory to the Python path
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:\\Users\\Yatharth nagpal\\Desktop\\challenge3\\src')))


# Now we can import the required functions from data_preprocessing

from data_preprocessing import load_data, preprocess_data


class TestDataPreprocessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test environment before all tests."""
        cls.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:\\Users\\Yatharth nagpal\\Desktop\\challenge3\\data\\ecommerce_data.csv'))
        print(f"Attempting to load file from: {cls.file_path}")
        cls.data = load_data(cls.file_path)

    def test_load_data(self):
        """Test loading of the CSV data file."""
        self.assertTrue(os.path.exists(self.file_path), f"File not found: {self.file_path}")
        self.assertIsInstance(self.data, pd.DataFrame, "Data is not a Pandas DataFrame")
        self.assertGreater(len(self.data), 0, "Loaded data is empty")

    def test_preprocess_data(self):
        """Test preprocessing of the data."""
        processed_data = preprocess_data(self.data)
        self.assertFalse(processed_data.isnull().values.any(), "Data contains NaN values after preprocessing")
        self.assertIn('order_date', processed_data.columns, "Column 'order_date' is missing after preprocessing")
        self.assertEqual(processed_data.loc[:, 'order_date'].dtype, 'datetime64[ns]', "Column 'order_date' is not in datetime format")

if __name__ == '__main__':
    unittest.main()
