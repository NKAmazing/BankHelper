from rest_framework.decorators import api_view
from ..services.message_service import MessageService
from rest_framework.response import Response
from rest_framework import status
from ..serializers import MessageSerializer
from datetime import datetime

message_service = MessageService()

# Message controllers
@api_view(['POST'])
def create(request):
    content = request.data.get('content')
    date = datetime.now()
    user_id = request.data.get('user_id')
    chat_reference_id = request.data.get('chat_reference_id')
    try:
        message_service.add(content, date, user_id, chat_reference_id)
        return Response("Message created successfully", status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all(request):
    try:
        messages = message_service.get_all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_by_id(request, id):
    try:
        message = message_service.get_by_id(id)
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update(request, id):
    content = request.data.get('content')
    date = datetime.now()
    user_id = request.data.get('user_id')
    chat_reference_id = request.data.get('chat_reference_id')
    try:
        message_service.update(id, content, date, user_id, chat_reference_id)
        return Response("Message updated successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete(request, id):
    try:
        message_service.delete(id)
        return Response("Message deleted successfully", status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
