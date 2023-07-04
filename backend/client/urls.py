from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from client.controllers import user_controller as user
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('lobby/', views.lobby, name='lobby'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('create_user/', user.create, name='create_user'),
    path('get_users/', user.get_all, name='get_all_users'),
    path('get_user/<int:id>/', user.get_by_id, name='get_user'),
    path('get_user_by_email/<str:email>/', user.get_by_email, name='get_user_by_email'),
    path('update_user/<int:id>/', user.update, name='update_user'),
    path('delete_user/<int:id>/', user.delete, name='delete_user'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
