from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Bank

class BankControllerTests(TestCase):
    def setUp(self):
        '''
        Set up method to create a test client to make HTTP requests
        '''
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        # Crea un banco de prueba con id=1 para usarlo en las pruebas
        Bank.objects.create(id=1, bank_name='Test Bank', bank_email='test@test.com')

    def test_create_bank(self):
        '''
        Method to test the creation of a bank
        '''
        data = {
            'bank_name': 'Test Bank',
            'bank_email': 'test@test.com',
        }
        response = self.client.post('/bank/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_banks(self):
        '''
        Method to test a request to get all the banks
        '''
        response = self.client.get('/bank/get_all/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifies that there is at least one bank in the response
        self.assertGreater(len(response.data), 0)

    def test_get_bank_by_id(self):
        '''
        Method to test a request to get a bank by its ID
        '''
        response = self.client.get('/bank/get/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_bank(self):
        '''
        Method to test a request to update a bank
        '''
        data = {
            'bank_name': 'Updated Bank',
            'bank_email': 'updated@test.com',
        }
        response = self.client.put('/bank/update/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_bank(self):
        '''
        Method to test a request to delete a bank
        '''
        response = self.client.delete('/bank/delete/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)