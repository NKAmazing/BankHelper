from django.urls import path
from .views import chat
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('chat/', TemplateView.as_view(template_name='chat.html')),
    path('lobby/', TemplateView.as_view(template_name='lobby.html')),
    path('', TemplateView.as_view(template_name='index.html')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
