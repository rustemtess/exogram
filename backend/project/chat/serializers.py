from .models import Message, Chat
from rest_framework import serializers

from accounts.serializers import UserSerializer
from django.core.serializers import json

class ChatSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()
    class Meta:
        model = Chat
        fields = ['name_of_chat_room', 'users', 'messages']
    
    def get_users(self, obj):
        return list(obj.users.values_list('username', flat=True))
    def get_messages(self, obj):
        #return list(obj.messages.values_list('sender', 'message', 'chat', 'sent_time'))
        messages = obj.messages.select_related('sender').values_list('sender__username', 'message', 'sent_time', 'id')#set chat name
        return list(messages)

def chat_serializer(chat):
    
    return {
        'id': chat.id,
        'name_of_chat_room': chat.name_of_chat_room,
        'users': list(chat.users.values_list('username', flat=True)),
        'messages':list(chat.messages.select_related('sender').values_list('sender__username', 'sender__id', 'message', 'sent_time', 'id'))
    }
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    sent_time = serializers.SerializerMethodField()
    class Meta:
        model = Message
        fields = ['sender', 'message', 'chat', 'sent_time']
    
    def get_sent_time(self, obj):
        return obj.sent_time.strftime('%d-%m-%Y %H:%M')