from rest_framework.decorators import api_view
from ..services.bank_service import BankService
from rest_framework.response import Response
from rest_framework import status
from ..serializers import BankSerializer

bank_service = BankService()

# Auxiliary functions
def get_data(request):
    bank_name = request.data.get('bank_name')
    bank_email = request.data.get('bank_email')
    bank_accounts = request.data.get('bank_accounts')
    return bank_name, bank_email, bank_accounts

# Bank controllers
@api_view(['POST'])
def create(request):
    bank_name, bank_email = get_data(request)
    try:
        bank_service.add(bank_name, bank_email)
        return Response("Bank created successfully", status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all(request):
    try:
        banks = bank_service.get_all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_by_id(request, id):
    try:
        bank = bank_service.get_by_id(id)
        serializer = BankSerializer(bank)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update(request, id):
    bank_name, bank_email, bank_accounts = get_data(request)
    try:
        bank_service.update(id, bank_name, bank_email, bank_accounts)
        return Response("Bank updated successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete(request, id):
    try:
        bank_service.delete(id)
        return Response("Bank deleted successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)