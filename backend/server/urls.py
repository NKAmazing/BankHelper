from django.urls import path
from server.controllers import chat_controller as chat
from server.controllers import message_controller as message
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_chat/', chat.create, name='create_chat'),
    path('get_chats/', chat.get_all, name='get_all_chats'),
    path('get_chat/<int:id>/', chat.get_by_id, name='get_chat'),
    path('update_chat/<int:id>/', chat.update, name='update_chat'),
    path('delete_chat/<int:id>/', chat.delete, name='delete_chat'),
    path('create_message/', message.create, name='create_message'),
    path('get_messages/', message.get_all, name='get_all_messages'),
    path('get_message/<int:id>/', message.get_by_id, name='get_message'),
    path('update_message/<int:id>/', message.update, name='update_message'),
    path('delete_message/<int:id>/', message.delete, name='delete_message'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)