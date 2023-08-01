from rest_framework.decorators import api_view
from ..services.user_service import UserService
from rest_framework.response import Response
from rest_framework import status
from ..serializers import UserSerializers

user_service = UserService()

# User controllers

@api_view(['POST'])
def create(request):
    username, email, password, address, phone, account_id = get_data(request)
    try:
        user_service.add(username, email, password, address, phone, account_id)
        return Response("User created successfully", status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all(request):
    try:
        users = user_service.get_all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_by_id(request, id):
    try:
        user = user_service.get_by_id(id)
        serializer = UserSerializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_by_username(request, username):
    try:
        user = user_service.get_by_username(username)
        serializer = UserSerializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_by_email(request, email):
    try:
        user = user_service.get_by_email(email)
        serializer = UserSerializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update(request, id):
    username, email, password, address, phone, account_id = get_data(request)
    try:
        user_service.update(id, username, email, password, address, phone, account_id)
        return Response("User updated successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete(request, id):
    try:
        user_service.delete(id)
        return Response("User deleted successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)

# Auxiliary functions

def get_data(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    address = request.data.get('address')
    phone = request.data.get('phone')
    account_id = request.data.get('account_id')
    return username, email, password, address, phone, account_id