from rest_framework.decorators import api_view
from ..services.transaction_service import TransactionService
from rest_framework.response import Response
from rest_framework import status
from ..serializers import TransactionSerializer
from datetime import datetime

transaction_service = TransactionService()

# Transaction controllers
@api_view(['POST'])
def create(request):
    amount = request.data.get('amount')
    date = datetime.now()
    status_transaction = request.data.get('status')
    source_account = request.data.get('source_account')
    destination_account = request.data.get('destination_account')
    try:
        transaction_service.add(amount, date, status_transaction, source_account, destination_account)
        return Response("Transaction created successfully", status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all(request):
    try:
        transactions = transaction_service.get_all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_by_id(request, id):
    try:
        transaction = transaction_service.get_by_id(id)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update(request, id):
    amount = request.data.get('amount')
    date = datetime.now()
    status_transaction = request.data.get('status')
    source_account = request.data.get('source_account')
    destination_account = request.data.get('destination_account')
    try:
        transaction_service.update(id, amount, date, status_transaction, source_account, destination_account)
        return Response("Transaction updated successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete(request, id):
    try:
        transaction_service.delete(id)
        return Response("Transaction deleted successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)