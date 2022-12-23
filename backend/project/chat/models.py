from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=30)#user
    receiver = models.CharField(max_length=30)#user
    message = models.CharField(max_length=1000)
    sent_time = models.DateTimeField(auto_now=True)

class Chat(models.Model):
    chat = [
        ['Bawer','hi Rustem'],
        ['Rustem','hi Bawer']
    ]
    contact = 'Rustem'#user