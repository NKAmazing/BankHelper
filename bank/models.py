from django.db import models
from django.conf import settings

# Create your models here.

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    source_account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='source_account')
    destination_account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='destination_account')

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    account_number = models.CharField(max_length=100)
    balance = models.FloatField()
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE, blank=True, null=True)

class Bank(models.Model):
    id = models.AutoField(primary_key=True) 
    bank_name = models.CharField(max_length=100)
    bank_email = models.EmailField(max_length=100)