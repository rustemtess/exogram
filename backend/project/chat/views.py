from .models import Message, Chat
from rest_framework import viewsets
from .serializers import ChatSerializer, MessageSerializer, chat_serializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

class ChatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    lookup_field = 'id'


@api_view(['GET','POST'])
def chat_viewset(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    serializer = chat_serializer(chat=chat)
    return Response(serializer)
    

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer
    lookup_field = 'id'