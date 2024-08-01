import sys
import os

# Adjust the Python path to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import patch, MagicMock
from data.database.queries import (
    generate_account_information_id,
    insert_generated_data,
    insert_sms_verification_data,
    update_email_verification_status,
    # Import other functions as needed
)

class TestQueries(unittest.TestCase):
    
    @patch('database.queries.Session')
    def test_generate_account_information_id(self, mock_session):
        # Mock the session object and its methods
        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance
        
        # Call the function under test
        result = generate_account_information_id(mock_session)
        
        # Assert that the function behaves as expected
        self.assertIsNotNone(result)
        mock_session_instance.add.assert_called()
        mock_session_instance.commit.assert_called()

    @patch('database.queries.Session')
    def test_insert_generated_data(self, mock_session):
        # Mock the session object and its methods
        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance
        
        # Prepare data for insertion
        generated_data = {'example_key': 'example_value'}
        
        # Call the function under test
        result = insert_generated_data(mock_session, **generated_data)
        
        # Assert that the function behaves as expected
        self.assertIsNotNone(result)
        mock_session_instance.add.assert_called()
        mock_session_instance.commit.assert_called()

    @patch('database.queries.Session')
    def test_insert_sms_verification_data(self, mock_session):
        # Mock the session object and its methods
        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance
        
        # Prepare data for SMS verification
        phone_number = '1234567890'
        verification_code = '123456'
        status = 'pending'
        
        # Call the function under test
        result = insert_sms_verification_data(mock_session, phone_number, verification_code, status)
        
        # Assert that the function behaves as expected
        self.assertIsNotNone(result)
        mock_session_instance.add.assert_called()
        mock_session_instance.commit.assert_called()

    @patch('database.queries.Session')
    def test_update_email_verification_status(self, mock_session):
        # Mock the session object and its methods
        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance
        
        # Prepare data for updating email verification status
        id = 1
        status = 'verified'
        
        # Call the function under test
        update_email_verification_status(mock_session, id, status)
        
        # Assert that the function behaves as expected
        mock_session_instance.commit.assert_called()

# Add tests for other functions following a similar pattern

if __name__ == '__main__':
    unittest.main()