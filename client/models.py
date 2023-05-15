from django.db import models
from django.conf import settings
from bank.models import Account

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)