from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ..services.bank_service import BankService
from ..services.account_service import AccountService
from ..services.transaction_service import TransactionService
from datetime import datetime

class TransactionControllerTests(TestCase):
    def setUp(self):
        '''
        Set up method to establish instances used in the tests
        '''
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        '''
        Method to set up data to be used in the tests
        '''
        # Create a bank to be used in the account
        bank_service = BankService()
        bank_service.add('Test Bank', 'test@test.com')

        # Create accounts to be used in the tests
        account_service = AccountService()
        account_service.add('00000000', 1000.00, 1)
        account_service.add('00000001', 1000.00, 1)

        # Create a transaction to be used in the tests
        transaction_service = TransactionService()
        transaction_service.add(100.00, datetime.now(), 'CONFIRMED', 1, 2)

    def test_create_transaction(self):
        '''
        Method to test the creation of a transaction
        '''
        data = {
            'amount': 100.00,
            'date': datetime.now(),
            'status': 'CONFIRMED',
            'source_account': 1,
            'destination_account': 2,
        }
        response = self.client.post('/bank/create_transaction/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_transactions(self):
        '''
        Method to test a request to get all the transactions
        '''
        response = self.client.get('/bank/get_transactions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifies that there is at least one transaction in the response
        self.assertGreater(len(response.data), 0)

    def test_get_transaction_by_id(self):
        '''
        Method to test a request to get a transaction by its ID
        '''
        response = self.client.get('/bank/get_transaction/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_transaction(self):
        '''
        Method to test a request to update a transaction
        '''
        data = {
            'amount': 200.00,
            'date': datetime.now(),
            'status': 'CONFIRMED',
            'source_account': 1,
            'destination_account': 2,
        }
        response = self.client.put('/bank/update_transaction/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_transaction(self):
        '''
        Method to test a request to delete a transaction
        '''
        response = self.client.delete('/bank/delete_transaction/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)