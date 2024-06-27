import unittest
from unittest.mock import patch
from CA2 import (
    MYSQLconnectionCheck,
    MYSQLconnection,
    userEntry,
    bookingRecord,
    searchCustomer,
    roomRent,
    Restaurent,
    Gaming,
    totalAmount,
    searchOldBill
)

class TestHotelManagementSystem(unittest.TestCase):

    @patch('builtins.input', side_effect=['test_username', 'test_password'])
    def test_MYSQLconnectionCheck(self, mock_input):
        self.assertIsNotNone(MYSQLconnectionCheck())

    @patch('builtins.input', side_effect=['test_username', 'test_password'])
    def test_MYSQLconnection(self, mock_input):
        self.assertIsNotNone(MYSQLconnection())

    @patch('builtins.input', side_effect=['1', 'Test User', 'Test Address', '30', 'Test Country', '1234567890', 'test@example.com'])
    def test_userEntry(self, mock_input):
        with patch('mysql.connector.connect') as mock_conn:
            self.assertIsNone(userEntry())

    @patch('builtins.input', side_effect=['2024-04-10', '2024-04-15'])
    def test_bookingRecord(self, mock_input):
        with patch('mysql.connector.connect') as mock_conn:
            self.assertIsNone(bookingRecord())

    @patch('builtins.input', side_effect=['test_cid'])
    def test_searchCustomer(self, mock_input):
        with patch('mysql.connector.connect') as mock_conn:
            self.assertTrue(searchCustomer())

    @patch('builtins.input', side_effect=['1', '101', '2'])
    def test_roomRent(self, mock_input):
        with patch('mysql.connector.connect') as mock_conn:
            self.assertIsNone(roomRent())

    @patch('builtins.input', side_effect=['test_cid', '1,2', '2,1'])
    def test_Restaurent(self, mock_input):
        with patch('mysql.connector.connect') as mock_conn:
            self.assertIsNone(Restaurent())

    @patch('builtins.input', side_effect=['test_cid', '1', '2'])
    def test_Gaming(self, mock_input):
        with patch('mysql.connector.connect') as mock_conn:
            self.assertIsNone(Gaming())

    @patch('builtins.input', side_effect=['test_cid'])
    def test_totalAmount(self, mock_input):
        with patch('mysql.connector.connect') as mock_conn:
            self.assertIsNone(totalAmount())

    @patch('builtins.input', side_effect=['test_cid'])
    def test_searchOldBill(self, mock_input):
        with patch('mysql.connector.connect') as mock_conn:
            self.assertIsNone(searchOldBill())

if __name__ == '__main__':
    unittest.main()
