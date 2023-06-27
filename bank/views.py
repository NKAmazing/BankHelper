from django.shortcuts import render
from rest_framework.decorators import api_view
from .services.account_service import AccountService
from .services.bank_service import BankService
from rest_framework.response import Response
from rest_framework import status
from .serializers import AccountSerializer, BankSerializer, TransactionSerializer

# Create your views here.

bank_service = BankService()
account_service = AccountService()

# Bank controllers
@api_view(['POST'])
def create_bank(request):
    bank_name = request.data.get('bank_name')
    bank_email = request.data.get('bank_email')
    try:
        bank_service.add(bank_name, bank_email)
        return Response("Bank created successfully", status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all_banks(request):
    try:
        banks = bank_service.get_all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_bank_by_id(request, id):
    try:
        bank = bank_service.get_by_id(id)
        serializer = BankSerializer(bank)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update_bank(request, id):
    bank_name = request.data.get('bank_name')
    bank_email = request.data.get('bank_email')
    bank_accounts = request.data.get('bank_accounts')
    try:
        bank_service.update(id, bank_name, bank_email, bank_accounts)
        return Response("Bank updated successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_bank(request, id):
    try:
        bank_service.delete(id)
        return Response("Bank deleted successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

# Account controllers
@api_view(['POST'])
def create_account(request):
    account_number = request.data.get('account_number')
    balance = request.data.get('balance')
    try:
        account_service.add(account_number, balance)
        return Response("Account created successfully", status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all_accounts(request):
    try:
        accounts = account_service.get_all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_account_by_id(request, id):
    try:
        account = account_service.get_by_id(id)
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_account_by_account_number(request, account_number):
    try:
        account = account_service.get_by_account_number(account_number)
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update_account(request, id):
    account_number = request.data.get('account_number')
    balance = request.data.get('balance')
    try:
        account_service.update(id, account_number, balance)
        return Response("Account updated successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_account(request, id):
    try:
        account_service.delete(id)
        return Response("Account deleted successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)