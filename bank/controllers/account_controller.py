from rest_framework.decorators import api_view
from ..services.account_service import AccountService
from rest_framework.response import Response
from rest_framework import status
from ..serializers import AccountSerializer

account_service = AccountService()

# Account controllers
@api_view(['POST'])
def create(request):
    account_number = request.data.get('account_number')
    balance = request.data.get('balance')
    try:
        account_service.add(account_number, balance)
        return Response("Account created successfully", status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all(request):
    try:
        accounts = account_service.get_all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_by_id(request, id):
    try:
        account = account_service.get_by_id(id)
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_by_account_number(request, account_number):
    try:
        account = account_service.get_by_account_number(account_number)
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update(request, id):
    account_number = request.data.get('account_number')
    balance = request.data.get('balance')
    try:
        account_service.update(id, account_number, balance)
        return Response("Account updated successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete(request, id):
    try:
        account_service.delete(id)
        return Response("Account deleted successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)