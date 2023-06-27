from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_bank/', views.create_bank, name='create_bank'),
    path('create_account/', views.create_account, name='create_account'),
    path('get_accounts/', views.get_all_accounts, name='get_all_accounts'),
    path('get_account/<int:id>/', views.get_account_by_id, name='get_account'),
    path('get_account_by_account_number/<str:account_number>/', views.get_account_by_account_number, name='get_account_by_account_number'),
    path('update_account/<int:id>/', views.update_account, name='update_account'),
    path('delete_account/<int:id>/', views.delete_account, name='delete_account'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)