from django.contrib.auth.models import User
from accounts.models import UserExtension
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    #is_active/date_of_brith

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
    
    def get_first_name(self, obj):
        return obj.first_name
    def get_last_name(self, obj):
        return obj.last_name
    def get_email(self, obj):
        return obj.email

class UserExtensionSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()
    # all_messages = serializers.SerializerMethodField()
    class Meta:
        model = UserExtension
        fields = ['contacts', 'chats', 'messages', 'all_messages']

    def get_contacts(self, obj):
        return obj.contacts.values_list('username')
    # def get_all_messages(self, obj):
    #     return self.all_messages(self)#ulan self ile yapsam sonra kullanilan modelin fieldlarindan all_messages a baglansam