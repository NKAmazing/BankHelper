from django.db import models
from django.conf import settings

# Create your models here.

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    transaction_amount = models.FloatField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_status = models.CharField(max_length=100)

class Account(models.Model):
    account_number = models.CharField(max_length=100)
    balance = models.FloatField()
    transactions = models.ManyToManyField(Transaction)
