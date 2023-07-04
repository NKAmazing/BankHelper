from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test', views.test, name='test'),
    path('home/', views.home, name='home'),
    path('lobby/', views.lobby, name='lobby'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
