from rest_framework.decorators import api_view
from ..services.chat_service import ChatService
from rest_framework.response import Response
from rest_framework import status
from ..serializers import ChatSerializer
from datetime import datetime

chat_service = ChatService()

# Chat controllers

@api_view(['POST'])
def create(request):
    chat_name, date = get_data(request)
    try:
        chat_service.add(chat_name, date)
        return Response("Chat created successfully", status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all(request):
    try:
        chats = chat_service.get_all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_by_id(request, id):
    try:
        chat = chat_service.get_by_id(id)
        serializer = ChatSerializer(chat)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update(request, id):
    chat_name, date = get_data(request)
    try:
        chat_service.update(id, chat_name, date)
        return Response("Chat updated successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete(request, id):
    try:
        chat_service.delete(id)
        return Response("Chat deleted successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST) 

# Auxiliary functions

def get_data(request):
    chat_name = request.data.get('chat_name')
    date = datetime.now()
    return chat_name, date