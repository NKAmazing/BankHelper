from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ..services.account_service import AccountService
from ..services.bank_service import BankService

class AccountControllerTests(TestCase):
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

        # Create an account to be used in the tests
        account_service = AccountService()
        account_service.add('00000000', 1000.00, 1)

    def test_create_account(self):
        '''
        Method to test the creation of an account
        '''
        data = {
            'account_number': '00000000',
            'balance': 1000.00,
            'bank_id': 1,
        }
        response = self.client.post('/bank/create_account/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_accounts(self):
        '''
        Method to test a request to get all the accounts
        '''
        response = self.client.get('/bank/get_accounts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifies that there is at least one account in the response
        self.assertGreater(len(response.data), 0)

    def test_get_account_by_id(self):
        '''
        Method to test a request to get an account by its ID
        '''
        response = self.client.get('/bank/get_account/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_account(self):
        '''
        Method to test a request to update an account
        '''
        data = {
            'account_number': '00000000',
            'balance': 1000.00,
            'bank_id': 1,
        }
        response = self.client.put('/bank/update_account/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_account(self):
        '''
        Method to test a request to delete an account
        '''
        response = self.client.delete('/bank/delete_account/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)