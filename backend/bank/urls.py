from django.urls import path
from bank.controllers import bank_controller as bank
from bank.controllers import account_controller as account
from bank.controllers import transaction_controller as transaction
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', bank.create, name='create_bank'),
    path('get_all/', bank.get_all, name='get_all_banks'),
    path('get/<int:id>/', bank.get_by_id, name='get_bank'),
    path('update/<int:id>/', bank.update, name='update_bank'),
    path('delete/<int:id>/', bank.delete, name='delete_bank'),
    path('create_account/', account.create, name='create_account'),
    path('get_accounts/', account.get_all, name='get_all_accounts'),
    path('get_account/<int:id>/', account.get_by_id, name='get_account'),
    path('get_account_by_account_number/<str:account_number>/', account.get_by_account_number, name='get_account_by_account_number'),
    path('update_account/<int:id>/', account.update, name='update_account'),
    path('delete_account/<int:id>/', account.delete, name='delete_account'),
    path('create_transaction/', transaction.create, name='create_transaction'),
    path('get_transactions/', transaction.get_all, name='get_all_transactions'),
    path('get_transaction/<int:id>/', transaction.get_by_id, name='get_transaction'),
    path('get_transactions_by_source_account/<int:source_account>/', transaction.get_all_by_source_account, name='get_transactions_by_source_account'),
    path('update_transaction/<int:id>/', transaction.update, name='update_transaction'),
    path('delete_transaction/<int:id>/', transaction.delete, name='delete_transaction'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)