from django.db import models
from client.models import User

# Create your models here.

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    chat_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    messages = models.ManyToManyField('Message', blank=True)

    
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_reference = models.ForeignKey(Chat, on_delete=models.CASCADE)