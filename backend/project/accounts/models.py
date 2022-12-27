from django.db import models
from django.contrib.auth.models import User
from chat.models import Chat, Message

class UserExtension(models.Model):#when create user create automatically userextension
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='extension'
    )
    def __str__(self):
        return self.user.username
    
    contacts = models.ManyToManyField(User, null=True, blank=True)#maybe friends
    
    def chats(self):
        return self.user.chats.values_list('name_of_chat_room')
    def messages(self):
        return self.user.messages.values_list('message')#maybe message change
    def all_messages(self):
        all_messages = []
        for chat in self.user.chats.values_list('id'):
            all_messages.append(Chat.objects.get(id = chat[0]).messages.values_list('message', 'id', 'chat', 'sender_id', 'sent_time'))
        return all_messages


    def add_contact(self, contact_username):
        if contact_username == self.user.username: return 'ERROR: You cannot add yourself in your contacts'#mayle dont need
        else:
            self.contacts.add(User.objects.get(username=contact_username))
    def delete_contact(self, contact_username):
        self.contacts.remove(User.objects.get(username=contact_username))