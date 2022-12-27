from django.db import models
from django.contrib.auth.models import User
#from accounts.models import User


class Chat(models.Model):
    name_of_chat_room = models.CharField(max_length=50)#if it is not a group it will be automaticaly the contacts name
    users = models.ManyToManyField(User, related_name='chats')
    def __str__(self):
        return self.name_of_chat_room
        #names = self.users.values_list('username', flat=True)#probabely will chance
        #return ', '.join(names)
    

    def add_user(self, username):
        self.users.add(User.objects.get(username=username))
    def remove_user(self, username):
        self.users.remove(User.objects.get(username=username))

    def messages(self):
        return self.messages.all()

    def add(self, sender, msg_text):
        Message.objects.create(sender=User.objects.get(username=sender), message=msg_text, chat=self)#for now sender will be selected manually

    def delete(self, msg_id):
        Message.objects.get(id=msg_id).delete()





    #def messages(self):
    #    return models.ManyToManyField(Message).values_list(flat=True)#if use it change add func



class Message(models.Model):#long msg search time?for optinixation maybe only text///the sender will be atomatically the request user
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='messages')#set default
    message = models.TextField(max_length=1000)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, default=5, related_name='messages')
    sent_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  "{}: {}".format(self.sender, self.message)
    
    class Meta():
        ordering = ['sent_time']