from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from client.controllers import user_controller as user

urlpatterns = [
    path('create_user/', user.create, name='create_user'),
    path('get_users/', user.get_all, name='get_all_users'),
    path('get_user/<int:id>/', user.get_by_id, name='get_user'),
    path('get_user_by_email/<str:email>/', user.get_by_email, name='get_user_by_email'),
    path('update_user/<int:id>/', user.update, name='update_user'),
    path('delete_user/<int:id>/', user.delete, name='delete_user'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
