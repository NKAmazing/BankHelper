from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('chat/', TemplateView.as_view(template_name='chat.html')),
    path('lobby/', TemplateView.as_view(template_name='lobby.html')),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
