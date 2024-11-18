import unittest
from dash import Dash
from src.dashboard import create_dashboard

class TestDashboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the Dash app for testing
        cls.app = create_dashboard()

    def test_app_layout(self):
        """Test if the dashboard layout is set correctly."""
        self.assertIsNotNone(self.app.layout, "Dashboard layout is not set.")

    def test_callbacks(self):
        """Test if the callbacks are registered properly."""
        callbacks = self.app.callback_map
        self.assertGreater(len(callbacks), 0, "No callbacks found in the dashboard.")

if __name__ == '__main__':
    unittest.main()
